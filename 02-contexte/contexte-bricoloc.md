





BricoLoc 2.0

Table des matières
I.	L’ORGANISATION DE L’ENTREPRISE	2
1.	La direction	2
2.	L’équipe administrative et commerciale	2
3.	L’équipe logistique	2
4.	La DSI	2
II.	DESCRIPTION MACROSCOPIQUE DE L'ARCHITECTURE DU SI	3
III.	L’APPLICATION DE LOCATION EN LIGNE D’OUTILS	4
1.	Description de l’application	4
2.	Elements  techniques de l’application	4
IV.	SCHEMA RECAPITULATIF DE L’ARCHITECTURE DU SI	6
V.	CADRE DE LA MISSION	8

 
Vous avez été contacté par une entreprise de location en ligne d’outils BricoLoc pour concevoir la nouvelle architecture logicielle de cette application de location B2C.
I.	L’organisation de l’entreprise
Le siège social de l’entreprise est basé à Toulouse. Ainsi qu’un des entrepôts de matériel de location.
Il y a 9 autres entrepôts hébergeant le matériel locatif : 1 à  Paris, 1 à Nancy, 1 à Strasbourg, 1  à Rennes, 1 à Nantes, 1 à Bordeaux, 1 à Montpellier et 1 à Avignon, 1 à Ajaccio
1.	La direction
La Directrice générale Sophie S. occupe aussi la fonction de DAF. Elle est assistée par la secrétaire de direction Samia M. 
Le responsable de la communication Alain D. s’occupe aussi du marketing. Il est secondé par Anne M., alternante en communication Web qui a aussi le rôle de community manager.
Benjamin O. occupe la fonction de DRH.
2.	L’équipe administrative et commerciale
Nadine B. est responsable de la comptabilité. Elle est aussi la correspondante directe fonctionnelle avec l’entreprise ManageYourself qui a intégré Sap Business One dans l’entreprise sur un serveur dédié. Elle est secondée par Maya V. qui gère principalement la facturation. Nadine tutore un alternant en comptabilité, Etienne B. 
Paul M. est responsable des achats. Il gère notamment la relation avec les fournisseurs pour l’achat des outils.
Il est secondé par Oussana O. et Mathilde Z. qui gèrent la relation commerciale avec les clients. C’est eux qui traitent les demandes et les insatisfactions clients  de l’application Bricoloc
Pauline M. est chargé de la relation avec les transporteurs qui livrent notamments les outils loués aux clients du site.
3.	L’équipe logistique
Tan F. est responsable de la logistique. Elle encadre plusieurs logisticiens. 
-	Fabienne K., logisticien repsonsable des entreprôts de Nancy et Strasbourg assisté de Fabrice P., 
-	Elena W., responsable des entreprôts de Rennes et Nantes, assistée de Bjorn R. et Jonathan I., 
-	Brian H. responsable du dépôt de Paris, assisté d’Edouard T. et Marie C., 
-	Dominique S. responsable du dépôt d’Ajaccio. 
-	Tan a la charge des entreprôts de Bordeaux, Toulouse, Montpellier et Avignon. Elle est assistée pour la gestion de ces 4 entreprôts par Boumi E., Eric E., Valentine V.  et un alternant Grégoire M.
Cette équipe à la charge de la gestion des stocks et  l’acheminement des outils entre les entreprôts. Ils sont aussi chargés d’animer le chat de l’application BricoLoc
4.	La DSI
Le résponsable du SI : Frédéric C. encadre 5 développeurs, 2 administrateurs Systèmes et réseaux, un technicien informatique et un administrateur de bases de données.
Marion H., Piotr S. et Thibaut E.  sont développeurs Java, ils gèrent le front-end et le back-end de l’application Bricoloc. 
Hervé D. est développeur .NET (C#, VB.NET) et a un background dans le développement C++. Il a quelques compétences Java lui permettant de venir en renfort de l’équipe développant l’application principale. Il crée aussi des utilitaires pour les salariés.
Isabelle A. est développeuse Python, elle aussi des compétences en data sciences.
La majorité du temps passé par les développeurs est sur de la maintenance corrective de l’application Bricoloc et des applicatifs internes. Cette maintenance entraine de nombreuses régressions, mal vécues par les utilisateurs qu’ils soient clients ou salariés de l’entreprise.

Didier L., l’administrateur de bases de données est un ancien d’Oracle. Il a cependant des compétences sur d’autres moteurs de bases de données et des compétences basiques en développement Java et PHP.

Florent D. et Lucas G. les administrateurs systèmes et réseaux ont la charge des serveurs et du réseau de, les entrepôts inclus. Ils n’interviennent cependant pas sur l’administration de Sap Business One, tâche sous la responsabilité de ManageYourself. 
Linda B., la technicienne s’occupe du parc des postes clients. Elle gère le support clients quand des demandes sont effectuées depuis l’application BricoLoc. Elle intègre aussi les remontées faites par Oussana et Mathilde quand il s’agit d’insatifactions clients dues à un bug. 

Tous les membres de la DSI ont moins de 6  ans d’ancienneté excepté Didier L. arrivé en 2015.

Pour simplifier dans le cadre du sujet, on considèrera que tous les employés sont rémunérés 3200 € bruts par mois et son cadres. Les alternants sont tous rémunérés 2300 € euros bruts et son non cadres. Si ça ce n’est pas une entreprise égalitaire.

II.	Description macroscopique de l'architecture du SI
L’insfrastructure technique de l’entreprise est presque totalement hebergée au siège. 
La communication entre le siège et les entreprôts se fait via VPN géré par le FAI de l’entreprise.
L’architecture système s’appuie sur un contrôleur de domaine redondé. Il y a 1 seul domaine Windows
Pour la partie bureautique tous les employés ont accès à la suite office 365 (Word, Excel, PowerPoint, Outlook, etc.). 
le serveur de messagerie est Microsoft Exchange 2019 et est hebergé sur un serveur Windows Server 2022
Un serveur de fichier Windows Server 2022 héberge les documentations d’outils mais aussi les documents administratifs de l’entreprise et autres. Il est intégré au domaine.
Un second serveur Ubuntu Server 20.04 de fichiers sert à « stocker » les codes sources. Les développeurs y accèdent en FTP. Ce serveur n’est pas pas intégré au domaine Windows. chaque développeur gère ses versions « internes ». 
L’ERP SAP Business One 9.X est aussi hébergé sur un serveur Microsoft Windows Server 22, intégré à l’AD du domaine Windows. L’ERP intègre les fonctionnalités classiques de gestion d’une PME.
PowerBI est utilisé pour créer des tableaux de bords – il utilise des sources de données SAP, mais aussi les bases de données hebergés sur le serveur de bases de données Oracle, des fichiers excels et les données extraites du comparateur de prix.
Des outils d’analyse de données ont été développés en Python pour alimenter aussi PowerBI.
L’entreprise est abonnée à un service de comparateurs de prix en mode SaaS.
Pour faire communiquer cette palteforme avec son SI, un service Java a été créé. Ce service utilise les APIs de type REST exposées par le comparateur de prix pour extraire les données, les transformer et les intégrer à l’ERP mais aussi à la solution de Data Analytics basée sur Power BI, ainsi qu’à l’application BricoLoc. Dans ce dernier cas les données transformées par le service sont insérées dans une base oracle prixDB qui est synchronisée via un batch Java avec la base bricolocDB.

Depuis 2020, ce service sert aussi de passerelle pour transférer, après transformation, les données relatives aux stocks gérées depuis l’ERP vers l’application BricoLoc. Tous les soirs un état CSV des stocks (outils achetés, retirés, etc.) est généré et stocker sur le serveur de fichier Windows Server 2022. Le service Java exécute une tâche asynchrone chaque jour pour lire, transformer et invoquer une procédure stockée PL/SQL pour mettre à jour la base bricolocDB.
A noter que depuis 2021, les entreprôts de Toulouse et Bordeaux Montpellier et Avignon testent la gestion des stocks via l’ERP à la place de l’outil de gestion des stock .NET (cf. ci-dessous).

Chaque entrepôt dispose d’un client lourd de gestion des stocks développé en C#. Ce client lourd communique avec un service WCF 4.X développé en VB.NET. Ce service est hebergé dans IIS 8  qui s’exécute dans un environnement Windows Server 2012, intégré à l’AD. Ce service communique directement avec la base de données bricolocDB de l’application bricoloc. Le code du service a été perdu. 

Et enfin il ya la mascotte de l’infrastructure :  le serveur hébergeant une VM VirtualBox Red Hat Linux dont personne ne sait à quoi elle sert mais qui est toujours en service et pour laquelle on n’a pas les accès utilisateurs mais qui est « pingable » donc présente sur le réseau local.

III.	L’application de location en ligne d’outils
1.	Description de l’application
Les internautes peuvent parcourir le catalogue de BriColoc des outils à louer par catégorie. Ils peuvent filtrer selon différents critères : la catégorie, le prix, la disponibilité, etc. Ils ont aussi accès à un comparateur de prix qui permet de visualiser les prix de ventes des outils proposés dans d’autres enseignes.
Chaque fiche d’outil  détaille les informations pour la location (prix, disponibilité, si réservé à des professionnels, etc.). le calendrier des disponibilités par contre nécessite d’être authentifié.
Pour pouvoir louer, il faut au préalable s’inscrire sur le site et renseigner des informations telles que l’adresse, si le client est un particulier ou un professionnel, etc.
Les clients ont un espace personnel où ils peuvent visualiser un calendrier de leurs locations (passées, en cours et à venir). Ils ont aussi accès à un chat et aux documentations des outils. Ainsi que d’autres services tels que le support pour remonter un bug, un problème de livraison ou toute autre demande.
Le client peut payer en ligne sa location. Il peut aussi régler la location dans un entrepôt. L’application BricoLoc s’appuie sur stripe.com et ses APIs pour le paiement en ligne.
Les clients ont le choix d’aller chercher dans un entrepôt leurs outils ou de se les faire livrer. Les « gros outils » doivent être récupérés sur place.
2.	Elements  techniques de l’application
La solution actuelle a été mise en service en 2013. L’architecture de l’application ainsi que les plateformes et infrastructures sous-jacentes ont peu évolué depuis.
elle est basée sur Java et  une base de données Oracle 11g R2, le tout hébergé en interne. 

Le front-end est développé avec Spring Framework 5, hebergé sur un serveur Apache Tomcat 8.5. Les requêtes front-end passent par un reverse proxy Apache HTTP Server. Le tout est déployé sur un serveur Ubuntu 20.04 TLS. La migration vers Spring 5 s’est faite en 2018.
Ce front-end Communique avec le back-end via des services web SOAP exposés par ce back-end.
Il est aussi associé à une base MySQL Community Server 5 colocalisée sur le serveur Ubuntu. Cette base sert en quelques sorte de cache pour  « optimiser » l’accès aux photos, aux documentations mises à disposition des clients pour l’affichage dynamique de textes, etc.
La partie back-end est développée avec Java EE 6 (EJB, JPA, etc.). Elle est déployée dans le serveur d’application WebLogic Server 12c R1 qui est installé sur sur un serveur Oracle Linux 6.5. Ce back-end implémente une partie de la logique métier de l’application BricoLoc.
Ce back-end  accède à la base de données relationnelle bricolocDB s’exécutant dans le serveur de bases de données Oracle 11g R2. Ce serveur de bases de données  est réparti sur 2 serveurs Oracle Linux 6.5. Elle contient aussi de nombreuses procédures stockées, fonctions et triggers PL/SQL qui implémentent une partie non négligeables de la logique métier de l’application BricoLoc. Malheuresuement aucun collaborateur n’y est vraiment formé en dehors de Didier L. En plus, de nombreuses tables et vues de la base ont plus de 150 colonnes, témoignage de prêt de 10 années de « maintenance » effectuées  bien souvent en absence de cohérence.
L’application BricoLoc, accède aussi à  la base autorisationDB qui contient notamment les tables pour la gestion des identités et des accès basés sur les rôles,  autrement-dit, les comptes utilisateurs de l’applications et leurs autorisations.
Le serveur de base de données Oracle a été déployé en même temps que l’application en ligne BricoLoc. La documentation de cette dernière n’est pas forcément à jour. 
Pour pallier aux problèmes de performance, le serveur  de bases de données  a été redéployé il y a environ 6 ans sur 2 serveurs physiques ayant des grosses capacités (nombre de cœurs, RAM et espace disque). Cela a occasionné de nombreux surcoûts en licences. 
L’application propose aussi une interface « admin »  pour les tâches classiques d’administration d’une application Web. Les comptes utilisateurs de type admin sont créés directement dans la base de données bricolocDB. Seuls les développeurs sont autorisés à accéder à l’interface admin. L’interface admin permet aussi de manipuler les données des stocks. 
Au fil des années des fonctions métiers ont commencé à être aussi implémentées dans le front-end. Certains composants métiers du front accèdent même directement à la base sans passer par le back-end.
BricoLoc propose également son application en marque blanche à plusieurs partenaires dont des chaînes d’hypermarchés.
Le client a la charge de déployer la solution dans son infrastructure. Le backend-end ayant été implémenté en respectant les standards Java EE, il  peut donc sur le papier être déployé  dans un serveur d’applicaton compatible autre que Weblogic moyennant quelques adaptation de configuration. Le partenaire peut connecter le backend à son propre SGBDR. BricoLoc fournit des scripts, pour la génération du schéma de la base, adaptés aux principaux SGBDR du marché (Oracle, MySQL, PostGreSQL et SQL Server)
Marion D. et Florent H. et Didier L. sont chargés d’assister le partenaire dans le déploiement de la solution.
Une information, entre eux les membres de l’équipes informatiques ont nommé BricoLoc, la grande boule de boue.
IV.	Schéma récapitulatif de l’architecture du SI
Ce schéma succinct de l’architecture applicative du SI n’est pas complet, mais c’est le seul qui existe dans l’enteprise. Le responsable informatique vous a expliqué qu’il faudrait le reprendre, le reviser et le compléter, mais que faute de temps c’est toujours remis à plus tard.
 
  
Le schéma de la page précédente est mis à disposition au format JPG et au format draw.io, lisible et modifiable via l’outil en ligne https://app.diagrams.net/
V.	Cadre de la mission
Depuis sont lancement en 2013, l’application de location BricoLoc n’a cessé de gagner en popularité jusqu’à 2020. Depuis cette date, elle a commencé à perdre régulièrement des clients du fait de bugs, de problèmes de performances. L’un des problèmes majeur relevé est l’incohérence dans la gestion des stocks.
De plus l’expérience utilisateur n’est plus en phase avec les plateformes web modernes.
S’ajoute à cela la concurrence de grands acteurs du web qui se sont aussi positionnés sur ce secteur de la location.
La direction, consciente des enjeux pour l’entreprise, vous a mandaté pour que vous proposiez une nouvelle architecture pour l’application BricoLoc, sans oublier l’adaptation de l’architecture globale de son SI pour que l’intégration de la nouvelle application soit optimale.

Pour se démarquer de la concurrence, l’entreprise désire que la nouvelle solution BricoLoc intègre les fonctionnalités pour la locations d’outils entre particuliers.
Dans les 3 années à venir, l’entreprise prévoit de s’ouvrir au marché européen. Elle prévoit d’implanter un entrepôt à Bruxelles, Lausanne, Francfort, puis dans un second temps des entreprots en Italie et en Espagne, prêt de la frontière.
La DG veut aussi se positionner sur le secteur de la location pour les grands acteurs du bâtiment. Pour l’instant les professionnels louant du matériel sont uniquement des indépendants. Elle se donne 5 ans pour y arriver.

La solution en marque blanche ne prend pas vraiment du fait de la difficulter à configurer et paramétrer la solution chez le partenaire. La direction vous demande de prendre en compte qu’elle désire conserver sa capacité à fournir une solution pour ses partenaires.

Le responsabile informatique souhaite que la conception de la nouvelle solution  inclue l'étude d'un hébergement de type "cloud", et que l’architecture BricoLoc puisse être développée par les 5 développeurs présents en interne.

Annexe
Schéma du SI version JPG et drawio modifiable

