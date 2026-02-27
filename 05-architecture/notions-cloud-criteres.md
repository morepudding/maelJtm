# Synthèse des Notions et Critères de Sélection Cloud

Ce document extrait les notions importantes issues des supports de cours sur le Cloud Computing. Il a pour but de définir un nouveau faisceau d'indices et de critères d'évaluation pour compléter notre matrice de choix d'hébergement cloud pour BricoLoc.

## 1. Notions Fondamentales du Cloud Computing

*   **Définition clé** : `Cloud = Virtualisation + Pay As You Go + Self Service`
*   **Modèles de services (XaaS)** :
    *   **IaaS (Infrastructure as a Service)** : Location d'infrastructures (serveurs, stockage, réseau). Permet des architectures sur mesure.
    *   **PaaS (Platform as a Service)** : Fourniture de plateformes d'exécution pour développeurs. Le Time-To-Market est accéléré mais avec plus de contraintes technologiques.
    *   **SaaS (Software as a Service)** : Logiciels clef en main accessibles via navigateur, mis à jour par l'éditeur.
*   **Modèles de déploiement** :
    *   **Cloud Public** : Infrastructure partagée et accessible via Internet.
    *   **Cloud Privé** : Réservé à une seule entreprise (internalisé ou hébergé).
    *   **Cloud Hybride** : Mixte entre cloud public (pour le débordement) et cloud privé (pour les données critiques).
    *   **Cloud Souverain / National** : Hébergement garantissant l'immunité aux lois extra-territoriales (ex. programme européen GAIA-X, label SecNumcloud de l'ANSSI en France).

---

## 2. Nouveaux Critères de Sélection pour la Matrice

L'analyse des documents met en évidence de nouvelles dimensions critiques (Juridique, Sécurité, DSI, Achats et RSE) à intégrer dans l'évaluation des fournisseurs cloud.

### A. Axe Juridique & Réglementaire (Conformité)
*   **Localisation des données** : Les données doivent-elles être hébergées en France ou dans l'Union Européenne ? 
*   **CLOUD Act vs RGPD** : Les fournisseurs américains (AWS, Azure, Google) sont soumis au CLOUD Act (droit de saisie par les autorités US), ce qui peut entrer en conflit avec le RGPD selon la criticité des données.
*   **Certifications de confiance** : L'opérateur bénéficie-t-il du label **SecNumcloud** ou fait-il partie des initiatives comme **GAIA-X** ?

### B. Axe Sécurité (CIA : Confidentialité, Intégrité, Disponibilité)
*   **Certifications de sécurité** : L'opérateur est-il certifié **ISO 27001** (management de la sécurité), **ISO 27017** (sécurité cloud), **ISO 27018** (protection données personnelles), ou possède-t-il des rapports **SOC 1, 2, 3** / **SAS 70** ?
*   **Politique d'identités** : Capacité à s'intégrer avec l'annuaire de l'entreprise via une **fédération d'identités** (SSO) et à imposer une authentification **multi-facteurs (MFA/U2F)**.
*   **Chiffrement et Confidentialité** : Offre-t-il le **BYOK (Bring Your Own Key)** pour que l'entreprise conserve la maîtrise du déchiffrement ? Chiffrement robuste en transit (SSL/IPSEC).
*   **Durabilité et SLA** : Niveau de fiabilité des centres de données (engagement de temps de disponibilité type 99,99% et durabilité des données pour le stockage).
*   **Traçabilité** : Fourniture complète et inaltérable de logs accessibles (SIEM).

### C. Axe Stratégie DSI (Intégrabilité et Réversibilité)
*   **Réversibilité** : Critère **non négociable**. Facilité de récupérer ses données et ses modèles dans un format standard en fin de contrat, assurance de suppression définitive. Éviter le *vendor lock-in* (dépendance forte à un opérateur).
*   **Intégrabilité avec le SI Existant** : Proposition de technologies d'échanges bidirectionnels, de middlewares standards, ou de liens réseaux dédiés/privés vers le SI de l'entreprise (ex: Azure Connect).
*   **Latence réseau** : Nécessite des serveurs/cache géographiquement proches (Europe, France) pour garantir un bon confort d'utilisation au quotidien.
*   **Support technique** : Accessibilité, temps de réponse, langue du support (support Niveau 3). Les géants du web ont parfois des supports plus "opaques" pour les PME.

### D. Axe Achats et FinOps
*   **Modèle OPEX** : Maîtrise des coûts à l'usage.
*   **Complexité de facturation (FinOps)** : La capacité à anticiper les dépenses (surtout liées au transfert de données / bande passante sortante). La tarification cloud peut être difficile à prévoir : existence de plafonds, d'alertes ?
*   **Politique tarifaire** : Transparence et modèle par carte bancaire ou facturation entreprise ?

### E. Axe Eco-Responsabilité (Green IT)
*   **Empreinte carbone** : Transparence sur le PUE (*Power Usage Effectiveness*) et le WUE (*Water Usage Effectiveness*).
*   **Cycle de vie du matériel** : Politique de l'hébergeur sur l'achat et le recyclage des composants informatiques, ainsi que l'utilisation d'énergies renouvelables (ex. OVHcloud met en avant un refroidissement innovant).

---

## 3. Impact pour la Matrice Technologique BricoLoc

Pour la matrice de choix du cloud BricoLoc (comparant Azure, Scaleway, Google Cloud, OVHcloud, AWS, etc.), ces nouveaux critères peuvent affiner notre évaluation, en particulier via 4 grands filtres :

1.  **Souveraineté et Juridique** : Donne un fort avantage aux acteurs européens (OVHcloud, Scaleway) face aux GAFAM (impact extra-territorial).
2.  **Sécurité et Réversibilité** : Différenciateur majeur pour s’assurer qu’un changement de direction ne gèlera pas l’entreprise.
3.  **Complexité Financière (FinOps)** : Les fournisseurs IaaS européens (Scaleway, OVHcloud) ont souvent des tarifs plus prévisibles en bande passante que les hyperscalers.
4.  **Green IT** : Devenu un véritable argument de choix en adéquation avec la RSE de BricoLoc.
