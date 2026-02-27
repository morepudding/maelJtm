# BricoLoc 2.0 — Architecture d'Infrastructure (OVHcloud)

## 1. Introduction

Suite à la décision documentée dans la [matrice de choix Cloud (`matrice-choix-cloud-v2.md`)](matrice-choix-cloud-v2.md), le fournisseur retenu pour l'hébergement de BricoLoc 2.0 est **OVHcloud**. 
Ce choix garantit la **souveraineté des données** (hors de portée du CLOUD Act américain), des **coûts maîtrisés** (bande passante incluse/prévisible) et une approche **éco-responsable (Green IT)**.

Ce document décrit la projection de notre architecture logique (voir `architecture-logique.md` et `schema-couche-applicative.md`) sur les services d'infrastructure d'OVHcloud.

---

## 2. Schéma d'Architecture d'Infrastructure (SI)

```mermaid
flowchart TB

    %% ═══════════════════════════════════════════════
    %% UTILISATEURS / INTERNET
    %% ═══════════════════════════════════════════════
    subgraph EXTERNAL["🌐 INTERNET"]
        direction LR
        U_Web["Navigateurs Web\n(Clients, Admin)"]
        U_Mob["Application Mobile"]
        U_Part["Partenaires\n(Marque Blanche)"]
    end

    %% ═══════════════════════════════════════════════
    %% OVHCLOUD PUBLIC
    %% ═══════════════════════════════════════════════
    subgraph OVH_PUBLIC["☁️ OVHCLOUD — Réseau Public / Périmètre de sécurité"]
        direction TB
        FW["🛡️ OVH Anti-DDoS Edge\n& Firewall Réseau"]
        LB["⚖️ OVH Managed Load Balancer\n(Point d'entrée HTTPS / TLS)"]
        FW --> LB
    end

    %% ═══════════════════════════════════════════════
    %% OVHCLOUD VRACK (RÉSEAU PRIVÉ)
    %% ═══════════════════════════════════════════════
    subgraph OVH_VRACK["🔒 OVHCLOUD — vRack (Réseau Privé Isolé)"]
        direction TB

        %% Zone Applicative
        subgraph ZONE_APP["⚙️ Zone Applicative (OVH Managed Kubernetes ou Instances Cloud)"]
            direction TB
            API_GW["🟢 API Gateway\n(Spring Cloud Gateway)\nRoutage & Auth"]
            MONO["🟣 Monolithe Modulaire\n(Spring Boot 3 / Java 21)\nCatalogue, Résa, Stocks, Utilisateurs..."]
            
            API_GW -->|"Routage interne"| MONO
            MONO -.->|"Scale horizontal"| MONO
        end

        %% Zone Data & Messaging (Managed Services)
        subgraph ZONE_DATA["💾 Zone Données & Messagerie (OVH Managed Services)"]
            direction LR
            DB[("🐘 Managed PostgreSQL 16\nHaute Disponibilité\n(Base de données)")]
            CACHE_DB[("⚡ Managed Redis\n(Cache & Sessions)")]
            MQ["📨 Managed RabbitMQ\n(Bus événementiel)"]
        end

        %% Zone Object Storage
        subgraph ZONE_STORAGE["📦 Zone Stockage Fichiers"]
            OBJ_S3["☁️ OVH Object Storage (S3 API)\nPhotos outils, PDF, Factures"]
        end

        %% Flux internes
        MONO -->|"JDBC"| DB
        MONO -->|"Redis API"| CACHE_DB
        MONO -->|"AMQP"| MQ
        MONO -->|"S3 API"| OBJ_S3
        API_GW -->|"Vérif Token"| CACHE_DB
    end

    %% ═══════════════════════════════════════════════
    %% SYSTÈMES TIERS (SaaS / Externes)
    %% ═══════════════════════════════════════════════
    subgraph TIERS["🌍 SYSTÈMES TIERS (Externes)"]
        direction TB
        AAD["🏢 Microsoft Azure AD\n(SSO Salariés conservé)"]
        SAP["📋 SAP Business One\n(ERP On-Premise/Cloud)"]
        STRIPE["💳 Stripe\n(Paiement)"]
        SMTP["📧 OVH Mail / SMTP\n(Envoi emails transactionnels)"]
    end

    %% ═══════════════════════════════════════════════
    %% FLUX EXTERNES / GLOBAUX
    %% ═══════════════════════════════════════════════
    EXTERNAL -->|"HTTPS (443)"| FW
    LB -->|"Trafic HTTP réparti"| API_GW

    %% Flux vers Tiers
    MONO -->|"SSO (OIDC)"| AAD
    MONO <-->|"API REST / Webhooks"| STRIPE
    SAP -->|"Webhooks VPN/IPSec"| MONO
    MONO -->|"SMTP"| SMTP

    %% Styles
    style EXTERNAL fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    style OVH_PUBLIC fill:#e8eaf6,stroke:#3f51b5,stroke-width:2px,color:#1a237e
    style OVH_VRACK fill:#e0f2f1,stroke:#00695c,stroke-width:2px,color:#004d40
    style ZONE_APP fill:#ede7f6,stroke:#4527a0,stroke-width:2px,color:#311b92
    style ZONE_DATA fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style ZONE_STORAGE fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style TIERS fill:#fce4ec,stroke:#880e4f,stroke-width:2px,color:#880e4f
```

---

## 3. Choix des composants et services OVHcloud
*L'architecture s'appuie au maximum sur les services managés d'OVHcloud afin de libérer l'équipe de 5 développeurs des tâches d'administration système.*

| Composant Logique | Service OVHcloud correspondant | Justification |
|---|---|---|
| **Réseau Public / Point d'entrée** | **OVH Load Balancer** + **Anti-DDoS** | Distribue le trafic entrant sur plusieurs instances de l'API Gateway, gère les certificats SSL/HTTPS, et protège contre les attaques réseau. |
| **Réseau Privé** | **vRack** | Connecte tous nos serveurs et bases de données dans un réseau privé (LAN) isolé d'Internet. Seuls le Load Balancer et l'API Gateway sont exposés publiquement. |
| **Zone Applicative (API Gateway + Monolithe)** | **Managed Kubernetes Service (MKS)** ou **Public Cloud Instances** | L'encapsulation via conteneurs Docker (sur Kubernetes ou instances simples) permet de redémarrer et de mettre à l'échelle automatique le monolithe. |
| **Base de données relationnelle** | **Managed Databases for PostgreSQL** | Service entièrement géré par OVH (sauvegardes auto, mises à jour de sécurité, haute disponibilité). Remplace le vieux Oracle. |
| **Cache & Sessions** | **Managed Databases for Redis** | Indispensable pour stocker les sessions utilisateurs de manière distribuée et mettre en cache le catalogue (pour soulager la base de données). |
| **Bus Événementiel** | **Managed RabbitMQ** ou **Managed Kafka** | Assure la communication asynchrone entre les modules (ex: notification de stock bas, confirmation de réservation). Service géré pour éviter la maintenance. |
| **Stockage Fichiers (S3)** | **High Performance Object Storage** ou **Standard Object Storage** | Stockage évolutif avec une API compatible S3 pour les images d'outils, les PDF de factures. Remplace le choix initial d'Azure Blob Storage pour conserver nos données en France. |

## 4. Intégration des Systèmes Tiers

Bien que l'hébergement cœur soit sur OVHcloud, nous conservons nos systèmes tiers existants :
* **Active Directory (SSO) :** BricoLoc utilisant massivement l'écosystème Microsoft pour l'organisation interne, **Azure AD** reste le fournisseur d'identité pour les employés. Le monolithe (Module Utilisateurs) validera les connexions via OpenID Connect.
* **Mails :** Utilisation du service **Email Pro OVH** ou d'un relais SMTP associé pour les notifications transactionnelles (remplace Azure Email).
* **SAP Business One :** Communication sécurisée (IPSec/VPN ou flux whitelistes) entre notre infrastructure OVH et le serveur ERP pour synchroniser les stocks.
