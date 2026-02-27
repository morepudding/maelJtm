# BricoLoc 2.0 — Matrice de Choix Fournisseur Cloud

## 1. Contexte et Objectif

Dans le cadre de la refonte de BricoLoc, l'infrastructure, actuellement hébergée sur des serveurs physiques au siège (Toulouse) arrivant en fin de vie, doit être migrée vers le cloud (AXE-04). 

L'objectif de ce document est de comparer plusieurs fournisseurs cloud (Azure, Hostinger, Scaleway, OVHcloud, AWS, Google Cloud, Alibaba Cloud) selon la grille de critères définie et de retenir le **Top 3** correspondant le mieux aux enjeux de BricoLoc (5 développeurs, besoin d'intégration avec l'écosystème Microsoft, refonte modulaire, architecture PostgreSQL/RabbitMQ).

---

## 2. Grille de pondération

Nous reprenons la grille standardisée des décisions architecturales du projet :

| # | Critère | Description | Poids |
|---|---|---|:---:|
| C1 | **Maturité & stabilité** | La solution est robuste, documentée et propose un SLA d'entreprise (≥99,5%). | 15% |
| C2 | **Maîtrise interne** | Adéquation avec les compétences de l'équipe existante (Java, .NET, écosystème MS). | 20% |
| C3 | **Compatibilité existant** | Facilité d'intégration avec le SI (Active Directory, Office 365, SAP B1). | 15% |
| C4 | **Performance** | Performance globale, réseau, capacités de scaling. | 10% |
| C5 | **Coût total (TCO)** | Coûts récurrents (compute, stockage, bandwidth) maîtrisés, sans mauvaises surprises. | 15% |
| C6 | **Portabilité & Cloud** | Support natif des standards open-source (Docker, PostgreSQL, Kubernetes). | 10% |
| C7 | **Maintenabilité** | Richesse de l'écosystème, outils de monitoring, console simple d'administration. | 10% |
| C8 | **Support** | Qualité du support technique interne ou communautaire. | 5% |

**Total : 100%** (Notation de 1 à 5).

---

## 3. Évaluation des Fournisseurs Cloud

| Critère | Poids | Azure | Scaleway | Google Cloud | OVHcloud | AWS | Alibaba Cloud | Hostinger |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| C1 Maturité | 15% | 5 | 4 | 5 | 4 | 5 | 4 | 3 |
| C2 Maîtrise interne | 20% | **4** | 4 | 3 | 4 | 3 | 2 | 4 |
| C3 Compatibilité existant | 15% | **5** | 3 | 3 | 3 | 3 | 2 | 2 |
| C4 Performance | 10% | 5 | 4 | 5 | 4 | 5 | 5 | 3 |
| C5 Coût total (TCO) | 15% | 4 | **5** | 4 | **5** | 3 | 4 | **5** |
| C6 Portabilité | 10% | 5 | 5 | 5 | 4 | 5 | 4 | 2 |
| C7 Maintenabilité | 10% | 5 | 4 | 4 | 4 | 4 | 3 | 2 |
| C8 Support | 5% | 5 | 4 | 5 | 4 | 5 | 4 | 2 |
| **Score pondéré** | **100%** | **4,65** | **4,10** | **4,05** | **4,00** | **3,90** | **3,30** | **3,10** |
| **Classement** | | **1er** | **2ème** | **3ème** | 4ème | 5ème | 6ème | 7ème |

---

## 4. Conclusion & Top 3 Retenu

Le **Top 3** retenu pour l'architecture cloud cible de BricoLoc est constitué de :

### 1. Microsoft Azure (Score : 4,65 / 5) - Choix Recommandé
L'écosystème BricoLoc reposant déjà fortement sur Microsoft (Active Directory, Office 365, Power BI), l'intégration via **Azure Active Directory (SSO)** est native. Azure propose de solides offres managées pour PostgreSQL et RabbitMQ sans lock-in, assurant le score maximal sur la compatibilité avec l'existant.

### 2. Scaleway (Score : 4,10 / 5)
Acteur européen, Scaleway propose une offre cloud performante axée sur les développeurs avec une tarification très lisible et maitrisée. La souveraineté des données (RGPD natif) et la simplicité de gestion compensent l'absence de certains services ultra-avancés, ce qui le place comme une solide alternative.

### 3. Google Cloud Platform (Score : 4,05 / 5) - GCP
Excellente plateforme technique axée sur les containers et l'open-source. Ses performances réseau mondiales et son expertise data sont de très haut niveau, mais son intégration dans le SI historique Microsoft (AD) demande plus d'efforts et son TCO est légèrement plus complexe à anticiper pour une PME.

> **Note sur le reste du panel** :  
> OVHcloud (4,00) et AWS (3,90) offrent également des garanties solides mais se retrouvent distancés de justesse dans le contexte particulier de BricoLoc. AWS souffre ici de coûts réseaux (egress) potentiellement élevés (C5) et d'une moindre compatibilité "Out-of-the-box" avec l'infrastructure AD existante par rapport à Azure. Enfin, Alibaba Cloud (3,30) et Hostinger (3,10) s'avèrent inadaptés à cause d'un manque d'adoption locale ou d'outillage entreprise.
