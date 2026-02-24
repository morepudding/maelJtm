# BricoLoc 2.0 — Synthèse globale du dossier d'architecture

---

## 0. Organisation du groupe projet

### Cadre académique

Ce projet s'inscrit dans le cursus **Master 1 Architecte d'Application** à **CESI**. L'objectif est de concevoir une architecture logicielle complète pour le cas BricoLoc, en mobilisant les compétences acquises en analyse de SI, conception d'architecture, choix technologiques et conduite de projet.

### Composition de l'équipe

L'équipe était initialement composée de **4 membres** :

| Membre            | Rôle initial                         | Spécialité                                                                        |
| ----------------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| **Steven**  | Analyste                              | Analyse de l'existant, recueil des exigences, formalisation des besoins             |
| **Romain**  | Chef de projet                        | Coordination générale, planification, suivi de l'avancement et des livrables      |
| **Maëlle** | Lead Dev Back-end & Maître des BDD   | Architecture back-end, modélisation des données, conception des bases de données |
| **Loris**   | Lead Dev Front-end & Maître du reste | Architecture front-end, intégrations tierces, livrables transverses                |

### Départ de Steven et réorganisation

**Steven a quitté le groupe** en cours de projet alors qu'il occupait le rôle d'**analyste**. Son périmètre — qui couvrait l'analyse du SI existant, la formalisation des exigences non fonctionnelles et l'identification des points faibles — a dû être **intégralement redistribué** entre les trois membres restants.

La redistribution s'est faite selon les affinités et compétences de chacun :

| Membre            | Missions reprises de Steven                                                                            | En plus de son rôle initial                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Romain**  | Formalisation des axes d'amélioration, rédaction de la démarche de conception                       | Vision stratégique et lien avec les décideurs                           |
| **Maëlle** | Analyse des bases de données existantes, identification des anomalies BDD (PL/SQL, schéma dégradé) | Conception de l'architecture de données cible (PostgreSQL, Redis)        |
| **Loris**   | Cartographie du SI existant, schéma d'architecture, comparaison des styles architecturaux             | Rédaction des justifications technologiques et de l'architecture logique |

### Challenges rencontrés et surmontés

#### Challenge 1 — Absorber la charge d'un membre en moins sans décaler les livrables

Le départ de Steven a représenté une **perte de 25% de la capacité de travail** du groupe, alors que le volume de livrables attendu restait identique. L'équipe a réagi en réorganisant sa méthode de travail : des **points de synchronisation courts mais hebdomadaires** ont été mis en place pour éviter les doublons et les zones grises. Chaque membre a pris en charge des livrables supplémentaires en les intégrant dans son périmètre existant, plutôt que de traiter l'analyse comme un silo séparé. Cette approche a permis de **livrer l'intégralité du dossier dans les délais** sans sacrifier la qualité.

#### Challenge 2 — Maintenir la cohérence de l'architecture sans analyste dédié

Sans analyste attitré, le risque principal était de produire des documents d'architecture **déconnectés de l'analyse de l'existant**. Pour y répondre, l'équipe a adopté une démarche de **traçabilité systématique** : chaque choix architectural est explicitement relié aux points faibles identifiés (PF-01 à PF-09), aux exigences non fonctionnelles (ENF-01 à ENF-08), et aux axes d'amélioration (AXE-01 à AXE-06). Cette rigueur de traçabilité, visible dans l'ensemble des livrables, a transformé une contrainte organisationnelle en **force méthodologique**.

#### Challenge 3 — Coordonner des expertises complémentaires à trois

Avec une équipe réduite à 3 personnes aux profils différents (gestion de projet, back-end/BDD, front-end/transverse), la coordination aurait pu devenir un frein. L'équipe a mis en place une **revue croisée de chaque livrable** : chaque document produit par un membre était relu et challengé par les deux autres avant validation. Cette pratique a non seulement amélioré la **qualité globale des livrables**, mais a aussi permis à chaque membre de monter en compétence sur les domaines adjacents au sien — renforçant la polyvalence de l'équipe face à un projet de cette envergure.

---

## 1. Schéma du SI existant

**Application de 2013**, stack obsolète (Java EE 6, WebLogic 12c, Oracle 11g R2).

- **Front-end** : Tomcat 8.5 / Spring 5 sur Ubuntu — logique métier migrée dans le front au fil du temps, accès directs JDBC vers la BDD.
- **Back-end** : WebLogic 12c R1 sur Oracle Linux 6.5 (EOL).
- **BDD** : Cluster Oracle 11g R2 (2 nœuds physiques, surcoût licences) — 3 bases : `bricolocDB` (tables >150 col, PL/SQL métier), `autorisationDB`, `prixDB` + MySQL 5 pour le cache.
- **Stocks** : double voie fragile — batch CSV quotidien SAP → PL/SQL + client lourd C# → WCF VB.NET (code source perdu, SPOF absolu).
- **Infra siège** : AD, Exchange 2019, SAP B1 9.X, Power BI, serveur FTP sans Git, VM Red Hat fantôme (rôle inconnu).
- **10 entrepôts** via VPN : 4 sur SAP (test), 6 sur client lourd C#/WCF legacy.
- **9 anomalies architecturales majeures** identifiées (accès directs BDD, PL/SQL métier, WCF sans source, FTP sans versioning, VM fantôme…).

---

## 2. Exigences Non Fonctionnelles (ENF)

8 domaines d'exigences issus des problèmes opérationnels et des ambitions stratégiques :

- **ENF-01 Performance** — Réponse catalogue <2s (P95), APIs <500ms, stocks quasi temps réel, support pics x3. ★★★★★
- **ENF-02 Disponibilité** — SLA ≥99,5%, RTO <4h, RPO <1h, zéro SPOF non mitigé, isolation des pannes. ★★★★★
- **ENF-03 Scalabilité** — Scale-out sans interruption, expansion européenne en <1 sprint, nouveaux segments B2C/B2B, onboarding partenaire <2 semaines. ★★★★☆
- **ENF-04 Sécurité** — IAM centralisé (0 compte en BDD), RGPD, PCI-DSS Stripe, moindre privilège, audit. ★★★★★
- **ENF-05 Maintenabilité** — Tests ≥70%, zéro logique PL/SQL, APIs documentées OpenAPI, onboarding dev <2 semaines, stack Java/Python. ★★★★★
- **ENF-06 Interopérabilité** — APIs REST SAP, Stripe v3, comparateur de prix, Power BI, multi-tenant marque blanche. ★★★★☆
- **ENF-07 Portabilité** — Cloud-ready, Docker, indépendance SGBDR (marque blanche), CI/CD. ★★★☆☆
- **ENF-08 Observabilité** — Logs centralisés, alertes automatiques, traçabilité bout en bout. ★★★☆☆

---

## 3. Points faibles et axes d'amélioration

### Points faibles (9 identifiés)

| ID    | Résumé                                                                          | Criticité |
| ----- | --------------------------------------------------------------------------------- | :--------: |
| PF-01 | Monolithe obsolète (Java EE 6, WebLogic, Oracle Linux 6.5 EOL)                   |     🔴     |
| PF-02 | Logique métier éparpillée sur 3 couches (back, PL/SQL, front)                  |     🔴     |
| PF-03 | Stocks incohérents — batch CSV quotidien, cause directe perte clients           |     🔴     |
| PF-04 | Service WCF sans code source — SPOF absolu sur 6 entrepôts                      |     🔴     |
| PF-05 | Pas de gestion de configuration — FTP sans Git                                   |     🔴     |
| PF-06 | BDD Oracle surdimensionnée, coûteuse, schéma dégradé (>150 col)              |     🟠     |
| PF-07 | Sécurité insuffisante — comptes admin en BDD, accès directs, VM fantôme      |     🟠     |
| PF-08 | Dette humaine — dépendance DBA, équipe <6 ans ancienneté, innovation bloquée |     🟠     |
| PF-09 | Marque blanche non compétitive — déploiement trop complexe chez partenaires    |     🟡     |

### Axes d'amélioration (6)

- **AXE-01** — Refonte architecture modulaire (→ PF-01, PF-02, PF-03)
- **AXE-02** — Stocks temps réel, événementiel SAP (→ PF-03, PF-04)
- **AXE-03** — Git + CI/CD (→ PF-05, PF-08)
- **AXE-04** — Migration cloud, rationalisation coûts Oracle (→ PF-01, PF-06)
- **AXE-05** — Sécurité renforcée, conformité RGPD (→ PF-07)
- **AXE-06** — Marque blanche SaaS multi-tenant (→ PF-09)

---

## 4. Comparaison des styles architecturaux

5 styles analysés sur 11 critères :

| Style                           |  Score /55  | Verdict BricoLoc                                          |
| ------------------------------- | :----------: | --------------------------------------------------------- |
| **Monolithe modulaire**   | **40** | ✅ Faisable par 5 devs, migration progressive, ACID natif |
| **Événementiel ciblé** | **40** | ✅ Idéal pour stocks temps réel et découplage SAP      |
| **Microservices**         |      39      | ❌ Trop complexe (Kubernetes, DevOps) pour 5 devs         |
| **SOA / ESB**             |      33      | ❌ ESB coûteux, gouvernance disproportionnée            |
| **N-tiers (actuel)**      |      23      | ❌ Source de tous les problèmes actuels                  |

**Recommandation** : architecture **hybride** = monolithe modulaire + événementiel ciblé + APIs REST (SOA légère sans ESB).

---

## 5. Matrice de choix technologique

4 décisions structurantes évaluées sur 8 critères pondérés :

| Décision          | Retenu                    | Score | Justification clé                                                         |
| ------------------ | ------------------------- | :----: | -------------------------------------------------------------------------- |
| Framework back-end | **Spring Boot 3**   | 4,90/5 | Compétences équipe, migration incrémentale depuis Spring 5, open-source |
| SGBDR              | **PostgreSQL 16**   | 4,60/5 | Open-source, cloud-natif, élimine surcoût licences Oracle                |
| Bus de messages    | **RabbitMQ**        | 4,55/5 | Plus simple que Kafka pour 5 devs, compatible Spring AMQP                  |
| Cloud              | **Microsoft Azure** | 4,75/5 | Continuité écosystème Microsoft (AD, Office 365, Power BI)              |

---

## 6. Styles retenus et justification

### 3 styles retenus

1. **Monolithe modulaire** (core) — 1 JAR, modules Maven isolés (9 modules). Faisable par 5 devs, ACID natif, Strangler Fig compatible.
2. **Événementiel ciblé** (stocks, notifications) — RabbitMQ sur les flux asynchrones critiques. Remplace le batch CSV, isole les pannes.
3. **APIs REST** (intégrations, marque blanche) — Contrats OpenAPI versionnés, SOA légère sans ESB.

### 4 styles écartés

- Microservices purs (trop complexe), SOA/ESB (disproportionné), N-tiers reconduit (source des problèmes), Serverless (incompatible état persistant).

### Migration Strangler Fig en 7 phases

- Phase 0 : Fondations Git/CI/CD/PostgreSQL (2-3 mois)
- Phase 1 : Module Stocks + RabbitMQ (3-4 mois)
- Phase 2 : Utilisateurs & Auth (2-3 mois)
- Phase 3 : Catalogue & Réservation (4-6 mois)
- Phase 4 : Paiement & Notifications (2-3 mois)
- Phase 5 : Marque blanche & i18n (3-4 mois)
- Phase 6 : Extinction WCF & legacy (1-2 mois)

---

## 7. Architecture logique cible

### 5 couches

1. **Clients** — Web, mobile, partenaires marque blanche, salariés (SSO Azure AD)
2. **API Gateway** — Spring Cloud Gateway : JWT, rate limiting, TLS, routage, versioning `/api/v1/`
3. **Monolithe modulaire** — Spring Boot 3 / Java 21, 9 modules métier isolés
4. **Bus événementiel** — RabbitMQ : 5 types d'événements (`StockUpdated`, `ReservationCreated/Confirmed/Cancelled`, `PaymentValidated/Failed`, `PriceUpdated`, `StockLow`)
5. **Données** — PostgreSQL 16 (schéma par module), Redis (cache catalogue/sessions), Azure Blob Storage (photos, docs, factures PDF)

### 9 modules applicatifs

| Module         | Rôle clé                                                                 |
| -------------- | -------------------------------------------------------------------------- |
| Catalogue      | Outils, catégories, recherche, comparateur prix, cache Redis              |
| Réservation   | Cycle de vie location, calendrier, P2P, annulation                         |
| Stocks         | Source de vérité dispo, temps réel SAP, inter-entrepôts                |
| Paiement       | Stripe v3, PCI-DSS, transactions, remboursements                           |
| Utilisateurs   | Auth JWT, RBAC (5 rôles), RGPD, Azure AD SSO                              |
| Notifications  | Emails transactionnels, alertes logisticiens, chat, push (futur)           |
| Admin          | Back-office, gestion catalogue/stocks/utilisateurs/partenaires             |
| Marque Blanche | Multi-tenant (schéma ou `tenant_id`), personnalisation, APIs partenaire |
| Intégration   | Passerelle unique vers SAP, comparateur prix, Power BI, transporteurs      |

### 4 systèmes tiers

SAP Business One (stocks/compta) · Stripe (paiement) · Comparateur de prix SaaS · Power BI (analytics)

### 8 règles d'architecture (garde-fous)

R01 : Pas d'accès direct aux tables d'un autre module · R02 : Zéro logique métier en BDD · R03 : Tiers via module Intégration uniquement · R04 : JWT obligatoire via Gateway · R05 : Aucune donnée carte côté BricoLoc · R06 : Schéma BDD par module · R07 : Événements versionnés · R08 : Git obligatoire, zéro FTP

### Équipe (5 devs)

- Marion H. (Java back) → `reservation`, `stocks`
- Piotr S. (Java full-stack) → `catalogue`, `admin`
- Thibaut E. (Java back) → `utilisateurs`, `marque-blanche`
- Hervé D. (.NET/Java) → `paiement`, `intégration`
- Isabelle A. (Python/Data) → Analytics, Power BI, tests data

---

## 8. Démarche de conception

7 étapes séquentielles, chacune alimentant la suivante :

1. **Analyse existant** → `schema-SI-existant.md`
2. **ENF** → `ENF-exigences-non-fonctionnelles.md`
3. **Points faibles & axes** → `axes-amelioration-points-faibles.md`
4. **Comparaison styles** → `comparaison-styles-architecturaux.md`
5. **Matrice techno** → `matrice-choix-technologique.md`
6. **Styles retenus** → `styles-retenus-justification.md`
7. **Architecture logique** → `architecture-logique.md`

**Fil directeur** : les ENF traversent toute la démarche et chaque choix est tracé et justifié.
