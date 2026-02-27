# BricoLoc 2.0 — Architecture d'Infrastructure Cible (V2)

## 1. Contexte et Alignement Stratégique

Afin de répondre aux nouveaux enjeux stratégiques de BricoLoc (ouverture au marché européen, nouvelle offre P2P "location entre particuliers", ciblage du B2B et déploiement en Marque Blanche), l'architecture d'infrastructure a été profondément repensée selon une logique de **Cloud-Native** et d'**amélioration continue**.

Hébergée sur **OVHcloud** (choix justifié par la souveraineté des données, l'éco-responsabilité et la prédictibilité des coûts), cette version V2 met en place :
* **Une scalabilité horizontale** via l'utilisation de clusters Kubernetes managés, essentielle pour absorber la charge lors de l'expansion européenne.
* **Un découplage des services métier** (Catalogue, B2B, P2P, Marque Blanche) pour réduire au maximum l'effet "boule de boue" (Big Ball of Mud) dont souffrait l'ancienne architecture monolithique.
* **Une sécurité périmétrique stricte** (Zero Trust local) avec un routage assuré par une API Gateway limitant l'exposition publique.

---

## 2. Schéma d'Architecture d'Infrastructure (SI) — V2 Cible

Ce schéma montre la déclinaison des services applicatifs et données au sein de l'environnement sécurisé d'OVHcloud, ainsi que leurs interactions avec le SI 'On-Premise' historique (notamment SAP) et les systèmes SaaS tiers.

```mermaid
flowchart TB

    %% ═══════════════════════════════════════════════
    %% UTILISATEURS / INTERNET / ZONES GÉOGRAPHIQUES
    %% ═══════════════════════════════════════════════
    subgraph EXTERNAL["🌐 INTERNET & CLIENTÈLE EUROPE (B2C, B2B, P2P)"]
        direction LR
        U_Web["👥 Clients Nav Web\n(B2C, B2B)"]
        U_Mob["📱 App Mobile\n(Loueurs & Locataires P2P)"]
        U_Part["🏷️ Partenaires\n(APIs Marque Blanche)"]
    end

    %% ═══════════════════════════════════════════════
    %% CDN & FRONT (Frontière)
    %% ═══════════════════════════════════════════════
    CDN["🚀 CDN Global & Edge Caching\n(Optimisation latence Europe & Sécurité Edge)"]
    EXTERNAL -->|"Trafic HTTPS (TLS 1.3)"| CDN

    %% ═══════════════════════════════════════════════
    %% OVHCLOUD PUBLIC & GATEWAYS
    %% ═══════════════════════════════════════════════
    subgraph OVH_PUBLIC["☁️ OVHCLOUD — Réseau Public DMZ"]
        direction TB
        FW["🛡️ OVH Anti-DDoS Edge\n& Pare-feu Applicatif (WAF)"]
        LB["⚖️ Managed Load Balancer\n(Haute Disponibilité Multizone)"]
        FW --> LB
    end
    CDN -->|"Trafic filtré"| FW

    %% ═══════════════════════════════════════════════
    %% OVHCLOUD VRACK (RÉSEAU PRIVÉ)
    %% ═══════════════════════════════════════════════
    subgraph OVH_VRACK["🔒 OVHCLOUD — vRack (Réseau Privé Backend)"]
        direction TB

        %% Zone Applicative (Kubernetes)
        subgraph ZONE_APP["⚙️ Zone Computing (OVH Managed Kubernetes Service - MKS)"]
            direction TB
            API_GW["🟢 API Gateway (Spring Cloud Gateway)\nRoutage, Rate Limiting, Authentification (OIDC)"]
            
            subgraph MICROSERVICES["Grappe de Services BricoLoc (Spring Boot 3 / Java 21)"]
                direction LR
                MS_CAT["📋 Service Catalogue\n(Moteur de recherche)"]
                MS_LOC["📅 Service Réservation\n(Core Location)"]
                MS_P2P["🤝 Service P2P\n(Mise en relation)"]
                MS_STOCK["📦 Service Stocks\n(Anti-Rupture)"]
                MS_MB["🏷️ Service Tenant\n(Logique Marque Blanche)"]
            end
            
            API_GW -->|"Dispatch Interne"| MICROSERVICES
        end
        LB -->|"Ingress Controller"| API_GW

        %% Zone Data & Messaging (Managed Services)
        subgraph ZONE_DATA["💾 Zone Persistance & Asynchronisme (PaaS Managé OVH)"]
            direction LR
            DB[("🐘 PostgreSQL Hautement Dispo.\n(Architecture Multi-Tenant\n pour la Marque Blanche)")]
            CACHE[("⚡ Redis Managé\n(Caches distribués\n & Sessions API)")]
            MQ["📨 RabbitMQ Managé\n(Bus d'évènements asynchrone)"]
        end

        %% Zone Object Storage
        subgraph ZONE_STORAGE["📦 Zone Stockage Médias (S3)"]
            OBJ_S3["☁️ OVH High Perf. Object Storage\n(Photos outils, Avatars P2P, Contrats)"]
        end

        MICROSERVICES -->|"R/W (JDBC)"| DB
        MICROSERVICES -->|"Pub/Sub (AMQP)"| MQ
        MICROSERVICES -->|"Get/Set (API Redis)"| CACHE
        MICROSERVICES -->|"Dépôt/Lecture Vues (API S3)"| OBJ_S3
        API_GW -->|"Vérification Token Session"| CACHE
    end

    %% ═══════════════════════════════════════════════
    %% SYSTÈMES TIERS (SaaS / On-Premise)
    %% ═══════════════════════════════════════════════
    subgraph TIERS["🌍 SYSTÈMES HISTORIQUES & SAAS"]
        direction TB
        AAD["🏢 Azure AD (Microsoft 365)\n(SSO Collaborateurs BricoLoc)"]
        SAP["📋 SAP Business One\n(ERP Hébergé DSI BricoLoc)"]
        STRIPE["💳 Stripe / Stripe Connect\n(Paiement direct & Escrow P2P)"]
        MAIL["📧 Serveur SMTP (OVH)\n(Notifications Transactionnelles)"]
    end

    %% Flux vers Tiers
    API_GW -->|"OIDC SSO"| AAD
    MS_LOC <-->|"API REST (Paiement Local)"| STRIPE
    MS_P2P <-->|"API REST (Stripe Connect Escrow)"| STRIPE
    MS_STOCK <-->|"Tunnel VPN (IPsec)\nÉchanges sécurisés EDI"| SAP
    MICROSERVICES -->|"Génération Emails"| MAIL

    %% Styles pour l'approche Académique et Architecturale
    style EXTERNAL fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    style CDN fill:#b3e5fc,stroke:#0288d1,stroke-width:2px,color:#01579b
    style OVH_PUBLIC fill:#e8eaf6,stroke:#3f51b5,stroke-width:2px,color:#1a237e
    style OVH_VRACK fill:#e0f2f1,stroke:#00695c,stroke-width:2px,color:#004d40
    style ZONE_APP fill:#ede7f6,stroke:#4527a0,stroke-width:2px,color:#311b92
    style ZONE_DATA fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style ZONE_STORAGE fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style TIERS fill:#fce4ec,stroke:#880e4f,stroke-width:2px,color:#880e4f
    style MICROSERVICES fill:#ffffff,stroke:#673ab7,stroke-width:2px,stroke-dasharray: 4 4,color:#311b92
```

---

## 3. Justifications Académiques et Architectoniques de la V2

Conformément à l'analyse de nos exigences non-fonctionnelles et en accord avec la grille d'architecture logicielle :

### 3.1. Approche de l'Extensibilité Européenne et P2P
L'introduction d'un **CDN (Content Delivery Network)** devient capitale pour mettre en cache les données statiques (images d'outils, assets front-end) au plus près des prochains utilisateurs (Bruxelles, Espagne, Italie).
De plus, la nouvelle brique **Service P2P** pour la location entre particuliers nécessite la délégation du cantonnement financier à **Stripe Connect** (Escrow payment), évitant à BricoLoc de lourdes responsabilités de conformité bancaire de type KYC/AML.

### 3.2. Séparation des Responsabilités (Microservices vs Monolithe)
Le passage progressif vers une grappe de services sur **Managed Kubernetes (MKS)** répond au problème identifié de la "grande boule de boue". Elle apporte deux avantages majeurs :
* Une scalabilité fine (ex. le *Service Catalogue* encaisse beaucoup plus de charge en lecture que le *Service Réservation*).
* Une meilleure maintenabilité pour l'équipe des 5 développeurs Java, qui peuvent désormais livrer et opérer leurs modules de manière dissociée.

### 3.3. Intégration du Système Historique (SAP ERP)
Le SI de BricoLoc n'est pas remplacé du jour au lendemain, nous sommes dans des **architectures hybrides**. La mise en place d'un pont **VPN IPsec** entre le réseau interne de l'entreprise (hébergeant SAP Business One) et le **vRack d'OVHcloud** garantit que nos données de gestion de stocks ne transitent de manière sécurisée et cryptée que dans un tunnel dédié.

### 3.4. Réponse au besoin "Marque Blanche"
Le déploiement en Marque Blanche était complexe car inadapté à l'installation directe par les partenaires. L'architecture **Multi-Tenant SaaS API-First** a été privilégiée :
L'API Gateway vérifie l'identité du partenaire via son Token d'API, pour le rediriger vers le *Service Tenant* (et le partitionnement logique dans la base PostgreSQL). Cela allège l'infrastructure du client sans exiger l'installation d'outils lourds chez lui.

### 3.5. Adoption du paradigme Asynchrone (Green IT et Performance)
Dans un contexte asynchrone, un service d'évènements comme **RabbitMQ Managé** permet à un module (ex: *Service P2P*) d'émettre un évènement sans attendre qu'un autre service (*Service de Notification SMTP*) le consomme. Cette élasticité lisse la demande de ressources de calcul sur les hyperviseurs, et concourt à la stratégie de rentabilité énergétique d'OVHcloud. 
