# BricoLoc 2.0 — Matrice de choix pour notre hébergeur Cloud (V2)

## 1. Pourquoi ce document ?

Dans le cadre du nouveau BricoLoc, nous devons remplacer nos vieux serveurs situés à Toulouse par une solution "Cloud" (sur internet). 
Ce document compare différents fournisseurs (ou "hébergeurs") pour trouver la meilleure option pour notre entreprise. L'objectif est de s'assurer que notre choix est non seulement **rentable**, mais aussi **sécurisé**, **légalement solide** pour nos données, et **maniable** pour notre équipe technique de 5 personnes.

---

## 2. Nos critères de choix (vulgarisés)

Suite à l'analyse de nos besoins, nous avons défini 5 grands critères pour noter les candidats, sur 100% :

| Critère | Description simple | Poids |
|---|---|:---:|
| **1. Légal & Souveraineté** | Où sont stockées nos données ? Sont-elles protégées par les lois européennes (le RGPD) ou soumises aux lois étrangères (comme la loi américaine qui autorise la saisie de données) ? | 20% |
| **2. Sécurité & Confiance** | Le fournisseur a-t-il les bonnes certifications de sécurité (normes ISO, chiffrements robustes des données) ? Le système ne tombera-t-il pas en panne ? | 25% |
| **3. Indépendance technique** | Si on veut quitter ce fournisseur demain, est-ce facile de récupérer nos données (ce qu'on appelle la réversibilité) ? Le service s'intègre-t-il bien avec nos outils actuels (notamment Microsoft) ? | 25% |
| **4. Maîtrise financière** | Est-ce que la facture à la fin du mois est facile à prévoir (FinOps), ou y a-t-il facilement des frais cachés ou imprévisibles (comme pour le transfert de données sortantes) ? | 20% |
| **5. Écologie (Green IT)** | Le fournisseur fait-il des efforts mesurables pour réduire et recycler sa consommation d'énergie et d'eau ? | 10% |

> *Pour ce tableau, 1 = Mauvais pour BricoLoc / 5 = Parfait pour BricoLoc*

---

## 3. Le tableau de comparaison (sur 5 points)

| Critère | Poids | Azure (Microsoft) | Scaleway | OVHcloud | Google Cloud | AWS (Amazon) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Légal & Souveraineté** | 20% | 3 | **5** | **5** | 3 | 2 |
| **2. Sécurité & Confiance** | 25% | **5** | 4 | 4 | **5** | 5 |
| **3. Indépendance technique**| 25% | **5** | 4 | 4 | 3 | 4 |
| **4. Maîtrise financière** | 20% | 3 | **5** | **5** | 3 | 2 |
| **5. Écologie (Green IT)** | 10% | 4 | 4 | **5** | 4 | 3 |
| **Score global** | **100%** | **4,10** | **4,40** | **4,50** | **3,60** | **3,35** |
| **Classement** | | **3ème** | **2ème** | **1er** | 4ème | 5ème |

*(Note : Alibaba Cloud et Hostinger ont été écartés d'emblée car ne répondant pas aux standards attendus pour notre taille d'entreprise et notre localisation).*

---

## 4. Bilan et Recommandations

En intégrant pleinement les aspects légaux (où vont nos données) et la protection de notre portefeuille, le classement évolue par rapport à une simple vision "purement technologique" :

### 🥇 1. OVHcloud (Score : 4,50 / 5) - Le grand gagnant
C'est le leader français. Son atout majeur est qu'il est 100% protégé par le droit européen (RGPD) et n'est pas soumis aux lois américaines : nos données et celles de nos clients sont en sécurité. Il offre une grille tarifaire très prévisible (pas de frais exorbitants cachés liés au réseau) et c'est un des champions de l'écologie avec un système de refroidissement de ses serveurs innovant (Green IT). 

### 🥈 2. Scaleway (Score : 4,40 / 5)
Il s'agit d'un autre acteur européen très solide. Tout comme OVH, il garantit la sécurité juridique de nos données et le respect de la confidentialité. Sa facturation est tout aussi claire pour une PME. Il lui manque juste certaines petites briques techniques très avancées que proposent les géants, mais c'est un excellent candidat.

### 🥉 3. Microsoft Azure (Score : 4,10 / 5)
C'est le choix technologique historique car BricoLoc utilise déjà énormément Microsoft pour ses mots de passe et son organisation. Son intégration est "magique" techniquement parlant (notre critère d'indépendance technique). Néanmoins, étant une société américaine, elle subit la contrainte du "CLOUD Act" américain, et les coûts de bande passante y sont plus difficiles à maîtriser qu'un acteur français, le faisant chuter à la troisième place de cette matrice élargie.

> **Et les autres ?**  
> **Google Cloud** et **AWS (Amazon)** sont des monstres de puissance technique. Cependant, ce sont des sociétés américaines (pas de souveraineté légale forte vis-à-vis du CLOUD Act), et dans le cas d'AWS, anticiper la facture de fin de mois est souvent un vrai casse-tête qui nécessite l'embauche d'un spécialiste financier dédié au cloud. Ils s'avèrent donc moins appropriés pour un groupe comme BricoLoc avec notre budget de PME.
