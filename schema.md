flowchart TB
    subgraph Front["Front-end – Ubuntu 20.04 LTS"]
        Apache("Apache HTTP Server\n(reverse proxy)")
        Tomcat("Tomcat 8.5 + Spring 5")
        MySQLCache[("MySQL 5\ncache photos & docs")]
        BusinessInFront("Logique métier\ndéplacée dans le front-end\nau fil des années"):::verybad
    end

    subgraph Back["Back-end – Oracle Linux 6.5"]
        WebLogic("WebLogic 12c R1\nJava EE 6 – EJB/JPA"):::legacy
        PLSQL("Logique métier PL/SQL\n(triggers, procédures)"):::sfo
    end

    subgraph OracleCluster["Cluster Oracle 11g R2 – 2 nœuds"]
        BricolocDB[("bricolocDB\n(Coût licences / Obsolète)")]:::legacy
        AutorisationDB[("autorisationDB")]
        PrixDB[("prixDB\nconcurrents")]
    end

    subgraph Windows["Infrastructure Windows – Siège"]
        Win2022("Windows Server 2022")
        SAP("ERP SAP Business One 9.X"):::erp
        Exchange("Exchange 2019")
        Fichiers("Partages fichiers + CSV stocks")
        AD("Active Directory\n2 DC redondés")
        IIS_WCF("IIS 8 + WCF VB.NET\nWin2012 – code perdu"):::danger
    end

    %% === CLIENTS & ACCÈS ===
    ClientWeb(("Client Web / Mobile")) --> Apache --> Tomcat
    Tomcat --> MySQLCache
    Tomcat -- SOAP --> WebLogic

    %% Dérives majeures
    Tomcat -. "accès direct JDBC" .-> BricolocDB:::violation
    BusinessInFront -. "viol de l'architecture" .-> BricolocDB:::violation

    WebLogic --> BricolocDB & AutorisationDB
    PLSQL --> BricolocDB

    %% Gestion des stocks
    EntrepotNet(("5-6 entrepôts\n→ Client lourd C#")):::legacy --> IIS_WCF
    EntrepotSAP(("4 entrepôts en test SAP")) -->|saisie directe| SAP

    InterfaceAdmin("Interface « Admin »")
    InterfaceAdmin --> Tomcat
    InterfaceAdmin --> BricolocDB
    DevCreateAdmin("Comptes admin créés\ndirectement en base")
    DevCreateAdmin --> BricolocDB

    %% Flux prix & batch
    ComparateurSaaS("Comparateur de prix SaaS") --> ServicePrix("Service Java passerelle")
    ServicePrix --> PrixDB & SAP & PowerBI("Power BI") & BatchStocks("Batch Java quotidien\nCSV → PL/SQL")
    BatchStocks("Batch Java quotidien\n(Risqué / Lent)"):::danger --> BricolocDB
    SAP --> Fichiers --> BatchStocks

    PowerBI --> SAP & BricolocDB & PrixDB & PythonScripts("Scripts Python Data")

    Stripe("Stripe\npaiement") --> Tomcat
    Salarie(("Salarié")) --> SAP & Exchange & Fichiers
    Partenaire(("Partenaire\nmarque blanche")) -- "échec configuration" --> Tomcat:::violation

    UbuntuFTP("Ubuntu 20.04\nFTP sources (Pas de Git)"):::danger
    VMFantome("VM Red Hat fantôme\naccès perdu"):::ghost

    %% === STYLES BASÉS SUR LE PPTX ===
    classDef legacy fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#e65100
    classDef danger fill:#ffebee,stroke:#c62828,stroke-width:4px,color:#b71c1c,font-weight:bold
    classDef verybad fill:#ffcdd2,stroke:#c62828,stroke-width:6px,stroke-dasharray:10 5,color:#b71c1c,font-weight:bold
    classDef violation fill:#fce4ec,stroke:#880e4f,stroke-width:3px,stroke-dasharray:5 5
    classDef sfo fill:#706fd3,stroke:#474787,stroke-width:4px,color:#fff
    classDef ghost fill:#f3e5f5,stroke:#7b1fa2,stroke-dasharray:8 4
    classDef erp fill:#e3f2fd,stroke:#1565c0,stroke-width:2px

    class WebLogic,BricolocDB,EntrepotNet legacy
    class IIS_WCF,BatchStocks,UbuntuFTP danger
    class BusinessInFront verybad
    class PLSQL sfo
    class VMFantome ghost