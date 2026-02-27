# Plan des Livrables BricoLoc 2.0 (Présentation & Schémas)

Ce document définit la structure de la présentation finale et des schémas architecturaux, en stricte adéquation avec la grille d'évaluation académique (INFMAALSIAPC1) et les exigences professionnelles du projet BricoLoc 2.0.

## 1. Objectifs de la Présentation
- **Public cible :** Direction Générale (Focus métier/coûts) et DSI (Focus technique/migration).
- **Tonalité attendue :** Professionnelle, rigoureuse (académique), axée sur l'amélioration continue et la justification systématique de chaque choix technique par rapport au contexte BricoLoc.
- **Support :** Diaporama PPTX (généré via scripts Python si besoin) intégrant des schémas d'architecture (modélisés sous Draw.io / Mermaid).

---

## 2. Structure détaillée du Slide Deck (Pitch)

### Partie 1 : Introduction & Analyse de l'Existant (Évaluation : 4 pts)
*L'objectif est de démontrer une parfaite compréhension du SI actuel et de ses points douloureux.*
- **Slide 1 : Titre & Équipe.** "BricoLoc 2.0 : Modernisation et Cloudification du SI".
- **Slide 2 : Le Contexte BricoLoc & Défis.** Croissance B2C freinée depuis 2020, insatisfaction client, internationalisation prévue (Europe).
- **Slide 3 : L'Architecture Existante.** Présentation du schéma SI actuel (Monolithe fortement couplé Java EE/Oracle, batchs fragiles, données éclatées).
- **Slide 4 : Diagnostic & Exigences Non Fonctionnelles (ENF).**
  - *Points de douleur :* Incohérence des stocks (impact business direct), "grande boule de boue" (dette technique), déploiement marque blanche difficile.
  - *ENF critiques :* Disponibilité (99,5%), Maintenabilité (équipe de 5 devs), Sécurité de l'IAM, Interopérabilité (Partenaires/SAP).

### Partie 2 : Conception Architecturale & Choix Cloud (Évaluation : 9 pts)
*C'est le cœu de la soutenance. Chaque choix doit être un compromis justifié, pas une "recette miracle".*
- **Slide 5 : Stratégie Cloud — Matrice de choix.** Présentation de la matrice (OVHcloud vs Scaleway vs Azure vs AWS/GCP).
- **Slide 6 : Justification du choix OVHcloud.** 
  - *Légal/Sécurité :* Souveraineté européenne (RGPD, échappement au CLOUD Act).
  - *FinOps & Green IT :* Prévisibilité financière parfaite pour une PME, refroidissement éco-responsable.
- **Slide 7 : Choix des Styles Architecturaux.** Pourquoi pas les Microservices ? (Complexité vs maturité de l'équipe).
  - *Style 1 : Monolithe Modulaire.* Isolement parfait des contextes, transactionnalité ACID conservée (crucial pour catalogue + stock).
  - *Style 2 : Événementiel ciblé.* Découplage via RabbitMQ (SAP <-> BricoLoc) pour la mise à jour des stocks en temps réel.
- **Slide 8 : Schéma d'Architecture Cible (Logique).** Présentation du diagramme Mermaid/Draw.io cible (API Gateway, Modules Spring Boot, Bus de messages RabbitMQ, PostgreSQL).

### Partie 3 : Conseil, Amélioration Continue & Migration (Évaluation : 2 pts)
*Démontrer une vision pragmatique : comment va-t-on y aller sans tout casser.*
- **Slide 9 : Stratégie de Migration (Strangler Fig).** Approche progressive "sans Big Bang". Phase 1 (Stocks/RabbitMQ) pour stopper "l'hémorragie" métier.
- **Slide 10 : Analyse des risques & Sécurité.** Gestion des identités (JWT au lieu de droits BDD directs), plan de reprise (PRA/PCA sur infrastructure OVH).
- **Slide 11 : Axes d'amélioration continue & Bilan.** 
  - Que se passera-t-il dans 3 ans ? (Déploiement Europe, ajustement de capacité).
  - Organisation du groupe de projet (Retour d'expérience, points forts, axes d'amélioration de la méthode de travail).

### Partie 4 : Conclusion
- **Slide 12 : BricoLoc demain.** Un SI résilient, sécurisé, souverain et prêt pour la marque blanche B2B et l'Europe.
- **Slide 13 : Q&A.** Diapositive d'ouverture aux questions du jury.

---

## 3. Schémas et Ressources à produire/intégrer

1. **Le Schéma de l'Existant :** (`02-contexte/contexte_bricoloc (2).drawio`) - Démontrant les silos et le batch de synchronisation problématique.
2. **Le Schéma Cible (Cœur Applicatif) :** Déjà formalisé en Mermaid dans `styles-retenus-justification.md`. À intégrer au propre dans le PPTX ou `schema-infrastructure-cible-v4.drawio`.
3. **Le Schéma d'Infrastructure Cloud OVH :** Montrant le VPC, la répartition Public/Private subnets, les bases managées, et le load balancing.

## 4. Prochaines Étapes Techniques (Actionnables)
- [ ] Valider ou ajuster cette trame (en répondant à ce prompt si vous souhaitez des modifications).
- [ ] Générer le code Python (`gen_pptx_part1.py` et `part2`) pour l'automatisation de la création de ce PPTX.
- [ ] Finaliser l'export des schémas Draw.io (Cible V4 et Existant) en PNG pour intégration dans les scripts Python.
