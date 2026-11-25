# Contenu des pages services, des pages métiers et du blog (Deks Nexa).
# Règles : aucun client, chiffre, statistique, témoignage, prix ou délai inventé ;
# aucune adresse, aucune année de création, aucune équipe présentée.
# Le paiement est toujours « précisé dans le devis ».

PAY_Q = "Comment se passe le paiement ?"
PAY_A = "Les modalités de paiement sont précisées dans le devis, avant le démarrage du projet."

# ------------------------------------------------------------------ pages services
SERVICE_PAGES = {
    "/logiciel-gestion-stock-benin/": dict(
        title="Logiciel de gestion de stock et caisse au Bénin | Deks Nexa",
        description="Logiciel de gestion de stock et de caisse au Bénin : entrées, sorties, ventes au comptoir, inventaires et alertes de rupture. Parlons-en sur WhatsApp.",
        label="Stock et caisse",
        intro=("Dans un magasin, une boutique ou un dépôt à Cotonou, le stock et la caisse sont le cœur de l'activité. Quand ils sont "
               "suivis sur un cahier, les écarts apparaissent tard et sont difficiles à expliquer. Deks Nexa conçoit un logiciel de gestion "
               "de stock et de caisse adapté à votre façon de vendre, pour savoir à tout moment ce qui est en rayon et ce qui est en caisse."),
        problem_title="Les écarts se découvrent toujours trop tard.", problem_word="trop tard",
        problem_text=[
            "Un article vendu mais pas noté, une livraison rangée sans être comptée, un produit sorti pour un client puis oublié : chaque petite "
            "erreur fait diverger le stock réel du stock théorique. On ne s'en rend compte qu'à l'inventaire, ou quand un client demande un article qui n'est plus là.",
            "Côté caisse, c'est la même chose. Les ventes au comptant, les ventes à crédit et les paiements mobiles se mélangent, et la clôture "
            "de fin de journée devient un exercice de reconstitution. Plus il y a de vendeurs, plus il est difficile de savoir qui a encaissé quoi.",
            "<strong>Un logiciel de stock et de caisse enregistre chaque mouvement au moment où il se produit.</strong> La vente met le stock à jour, "
            "la réception de marchandise aussi, et la caisse se clôture avec un récapitulatif clair par mode de paiement et par vendeur.",
        ],
        deliver_title="Un outil de stock et de caisse pensé pour le comptoir.", deliver_word="pour le comptoir",
        deliver_intro="Des écrans rapides pour vendre, des écrans détaillés pour contrôler. Chaque utilisateur voit ce dont il a besoin.",
        deliver=[
            ("Articles et catalogue", "Références, variantes, unités de vente, prix d'achat et de vente, et codes-barres si vous en utilisez."),
            ("Entrées et sorties", "Réceptions fournisseurs, transferts entre dépôts, retours et pertes : chaque mouvement avec sa date et son auteur."),
            ("Vente au comptoir", "Un écran de caisse simple : recherche d'article, panier, remise autorisée, ticket ou facture."),
            ("Clôture de caisse", "Fond de caisse, espèces, paiements mobiles et ventes à crédit récapitulés en fin de journée, par vendeur."),
            ("Alertes et inventaires", "Seuils d'alerte avant la rupture et inventaires guidés pour corriger le stock en quelques étapes."),
            ("Lien avec la gestion", "Le stock peut s'intégrer à un <a href=\"/logiciel-de-gestion-benin/\">logiciel de gestion</a> plus complet : clients, factures et tableaux de bord."),
        ],
        steps_title="Mettre en place le logiciel sans arrêter la vente.", steps_word="sans arrêter la vente",
        steps_intro="Votre commerce continue de tourner pendant le projet : la bascule se prépare à l'avance.",
        steps=[
            ("Observer", "Nous regardons comment vous recevez, rangez et vendez : vos articles, vos unités et vos modes de paiement."),
            ("Préparer", "Nous structurons votre catalogue et proposons les écrans de caisse et de stock, avec un devis détaillé."),
            ("Construire", "Le logiciel est développé par étapes et testé avec vos vendeurs sur des cas réels."),
            ("Basculer et suivre", "Inventaire de départ, prise en main, mise en service, puis ajustements et maintenance."),
        ],
        who_title="Pour les commerces où chaque article compte.", who_word="chaque article",
        who_intro="Le besoin apparaît dès que plusieurs personnes vendent ou que le stock se répartit entre plusieurs lieux.",
        who=[
            ("Commerces et quincailleries", "Nombreuses références, ventes rapides et crédit client.", "/solutions/commerces/"),
            ("Hôtels et restaurants", "Boissons, denrées et consommables à suivre au plus près.", "/solutions/hotels-restaurants/"),
            ("Cliniques", "Consommables et produits à tracer, entrées et sorties justifiées.", "/solutions/cliniques/"),
            ("Distributeurs et dépôts", "Plusieurs points de stock et des transferts réguliers entre eux.", None),
        ],
        extra=["<strong>Faut-il un lecteur de codes-barres ?</strong> Ce n'est pas indispensable. Le logiciel peut fonctionner avec une simple "
               "recherche par nom ou par référence, et accueillir un lecteur plus tard si votre volume de ventes le justifie."],
        faq_title="Vos questions sur le stock et la caisse.", faq_word="le stock et la caisse",
        faq=[
            ("Le logiciel peut-il gérer plusieurs magasins ou dépôts ?",
             "Oui. Chaque lieu a son propre stock, et les transferts entre dépôts sont enregistrés pour que les quantités restent justes partout."),
            ("Peut-on enregistrer les ventes à crédit ?",
             "Oui. Les ventes à crédit sont rattachées au client, et vous suivez ce qui reste à encaisser ainsi que les remboursements."),
            ("Combien coûte un logiciel de stock et de caisse ?",
             "Le tarif dépend du nombre de points de vente, d'utilisateurs et des fonctions retenues. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/solutions/commerces/", "/logiciel-de-gestion-benin/", "/solutions/hotels-restaurants/"],
    ),
    "/creation-site-web-benin/": dict(
        title="Création de site web à Cotonou et au Bénin | Deks Nexa",
        description="Création de site web au Bénin : site vitrine ou boutique en ligne, rapide sur mobile, préparé pour Google et relié à WhatsApp. Parlons de votre projet.",
        label="Site web",
        intro=("Avant d'appeler, vos futurs clients cherchent votre entreprise sur Google. À Cotonou comme ailleurs, une simple page "
               "Facebook ne suffit plus à rassurer. Deks Nexa crée des sites web modernes, rapides sur téléphone et pensés pour "
               "transformer une visite en prise de contact."),
        problem_title="Sans site, vos clients doutent avant même de vous appeler.", problem_word="doutent",
        problem_text=[
            "Une recherche sur Google qui ne renvoie rien, ou seulement un ancien profil de réseau social, laisse une impression d'amateurisme. "
            "Le client potentiel ne sait pas exactement ce que vous proposez, ni comment vous joindre, et il passe au résultat suivant.",
            "Beaucoup de sites existants posent un autre problème : lents à charger sur un téléphone, difficiles à lire, avec des informations "
            "dépassées. Ils coûtent de l'argent sans rapporter de demandes.",
            "<strong>Un bon site web répond aux questions du client et l'invite à vous contacter.</strong> Ce que vous faites, pour qui, "
            "comment vous travaillez, et un bouton WhatsApp toujours à portée de pouce.",
        ],
        deliver_title="Un site web moderne, rapide et facile à faire évoluer.", deliver_word="facile à faire évoluer",
        deliver_intro="Chaque page a un objectif : informer, rassurer ou faire passer à l'action.",
        deliver=[
            ("Site vitrine", "Présentation de l'entreprise, des services, des réalisations et des moyens de contact, sur quelques pages bien construites."),
            ("Boutique en ligne", "Catalogue de produits, fiches détaillées, commande et suivi, avec le mode de paiement adapté à vos clients."),
            ("Pensé pour le téléphone", "Vos clients vous consultent souvent depuis leur téléphone : textes lisibles, boutons faciles à toucher, pages légères."),
            ("Contact immédiat", "Bouton WhatsApp, formulaire et appel en un geste, pour ne perdre aucune demande."),
            ("Préparé pour Google", "Titres, descriptions, structure des pages et vitesse soignés dès la conception. Pour aller plus loin, voyez notre offre de <a href=\"/referencement-google-benin/\">référencement Google</a>."),
            ("Mises à jour et suivi", "Ajout de pages, changements de textes, sauvegardes et petites évolutions après la mise en ligne."),
        ],
        steps_title="De la première discussion à la mise en ligne.", steps_word="la mise en ligne",
        steps_intro="Vous validez chaque étape avant de passer à la suivante.",
        steps=[
            ("Comprendre", "Votre activité, vos clients, vos concurrents et ce que le site doit vous apporter."),
            ("Structurer", "Le plan des pages, les textes à rassembler et la maquette, avec un devis détaillé."),
            ("Réaliser", "Le site est construit, vous le testez sur votre propre téléphone et nous ajustons."),
            ("Publier et suivre", "Mise en ligne, nom de domaine et adresse e-mail professionnelle si besoin, puis suivi."),
        ],
        who_title="Pour les entreprises qui veulent être prises au sérieux.", who_word="au sérieux",
        who_intro="Un site professionnel sert toutes les activités où la confiance se gagne avant le premier rendez-vous.",
        who=[
            ("Avocats et notaires", "Présenter les domaines d'intervention avec sobriété.", "/solutions/avocats-notaires/"),
            ("Hôtels et restaurants", "Chambres, menu, réservations et accès visibles en un coup d'œil.", "/solutions/hotels-restaurants/"),
            ("Écoles privées", "Informations pour les parents, inscriptions et vie de l'établissement.", "/solutions/ecoles/"),
            ("ONG", "Présenter les projets et rendre compte aux partenaires.", "/solutions/ong/"),
        ],
        extra=["<strong>Site vitrine, boutique en ligne ou page Facebook ?</strong> Une page Facebook est utile pour animer une communauté, "
               "mais vous n'en maîtrisez ni la présentation ni la visibilité. Le site vitrine est votre adresse officielle sur internet. "
               "La boutique en ligne se justifie quand vos clients peuvent commander sans vous parler au préalable."],
        faq_title="Vos questions sur la création de site web.", faq_word="site web",
        faq=[
            ("Combien coûte la création d'un site web au Bénin ?",
             "Le tarif dépend du nombre de pages, des fonctions (boutique, réservation, espace client) et des contenus à produire. Après étude du besoin, nous vous remettons un devis détaillé."),
            ("Pourrai-je modifier le site moi-même ?",
             "Si vous le souhaitez, nous prévoyons un espace d'administration pour les contenus que vous changez souvent. Nous pouvons aussi nous charger des mises à jour."),
            ("Le site sera-t-il bien affiché sur téléphone ?",
             "Oui. Chaque page est conçue et vérifiée sur téléphone, tablette et ordinateur avant la mise en ligne."),
            (PAY_Q, PAY_A),
        ],
        related=["/referencement-google-benin/", "/solutions/hotels-restaurants/", "/solutions/avocats-notaires/"],
    ),
    "/application-mobile-benin/": dict(
        title="Développement d'application mobile au Bénin | Deks Nexa",
        description="Développement d'application mobile au Bénin : applications Android et iOS pour vos clients ou vos équipes terrain, reliées à vos données. Parlons-en.",
        label="Application mobile",
        intro=("Certaines tâches se font loin du bureau : visites de clients, relevés sur le terrain, livraisons, contrôles. Deks Nexa "
               "développe des applications mobiles Android et iOS pour vos équipes ou pour vos clients, reliées à vos données, pour que "
               "l'information arrive au bon endroit sans ressaisie, à Cotonou comme partout au Bénin."),
        problem_title="L'information du terrain arrive tard, ou pas du tout.", problem_word="pas du tout",
        problem_text=[
            "Sur le terrain, on note sur papier, on prend des photos dans la galerie du téléphone et on envoie des messages vocaux. "
            "Au bureau, quelqu'un doit tout retranscrire, et une partie se perd en route.",
            "Vos clients, eux, attendent de pouvoir commander, réserver ou suivre une demande depuis leur téléphone, sans passer un appel à chaque fois.",
            "<strong>Une application mobile bien pensée fait le lien entre le terrain et le bureau.</strong> Les saisies sont structurées, "
            "datées, accompagnées de photos ou d'une position si nécessaire, et arrivent directement dans votre logiciel.",
        ],
        deliver_title="Une application simple à utiliser, même en déplacement.", deliver_word="en déplacement",
        deliver_intro="Des écrans courts et clairs, pensés pour être utilisés debout, d'une main, parfois avec une connexion faible.",
        deliver=[
            ("Formulaires de terrain", "Relevés, visites, contrôles et rapports saisis directement dans l'application, avec photos si besoin."),
            ("Application pour vos clients", "Commandes, réservations, suivi de demande ou fidélité, aux couleurs de votre marque."),
            ("Notifications", "Alertes et rappels envoyés au bon moment : nouvelle tâche, commande prête, rendez-vous."),
            ("Synchronisation", "Les données remontent vers votre <a href=\"/logiciel-de-gestion-benin/\">logiciel de gestion</a> ; la saisie hors connexion peut être prévue selon le projet."),
            ("Accès par profil", "Chaque utilisateur voit ses propres tâches et ses propres informations."),
            ("Publication sur les stores", "Préparation et publication sur Google Play et l'App Store, puis mises à jour."),
        ],
        steps_title="De l'idée à l'application publiée.", steps_word="publiée",
        steps_intro="Une application réussie commence par les usages réels de ceux qui vont s'en servir.",
        steps=[
            ("Écouter les utilisateurs", "Nous partons des tâches réelles : qui utilise l'application, où et à quel moment."),
            ("Maquetter", "Les écrans principaux sont dessinés et validés avec vous avant le développement, avec un devis détaillé."),
            ("Développer et tester", "L'application est construite par étapes et testée sur de vrais téléphones."),
            ("Publier et suivre", "Publication sur les stores, prise en main, puis évolutions et maintenance."),
        ],
        who_title="Pour les activités qui se passent hors du bureau.", who_word="hors du bureau",
        who_intro="L'application mobile prend tout son sens quand l'information naît sur le terrain ou chez le client.",
        who=[
            ("ONG et projets de terrain", "Collecte de données lors des visites et des enquêtes.", "/solutions/ong/"),
            ("Cliniques", "Rendez-vous et rappels pour les patients.", "/solutions/cliniques/"),
            ("Écoles", "Informations et communications pour les parents.", "/solutions/ecoles/"),
            ("Commerciaux et livreurs", "Visites clients, commandes et preuves de livraison.", None),
        ],
        extra=["<strong>Application mobile ou site adapté au téléphone ?</strong> Si vos utilisateurs ont surtout besoin de consulter des "
               "informations, un site bien conçu pour le mobile peut suffire. L'application devient utile quand on l'utilise souvent, "
               "qu'on a besoin de notifications, de photos ou de saisies répétées."],
        faq_title="Vos questions sur les applications mobiles.", faq_word="applications mobiles",
        faq=[
            ("L'application fonctionnera-t-elle sur Android et sur iPhone ?",
             "Oui. Nous développons pour Android et iOS ; le choix des plateformes se fait avec vous selon vos utilisateurs."),
            ("L'application peut-elle se connecter à notre logiciel actuel ?",
             "Oui si votre logiciel le permet : nous étudions ses possibilités d'échange de données au début du projet."),
            ("Combien coûte le développement d'une application mobile ?",
             "Le tarif dépend du nombre d'écrans, des fonctions et des connexions à prévoir. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/solutions/ong/", "/logiciel-de-gestion-benin/", "/solutions/cliniques/"],
    ),
    "/automatisation-whatsapp-ia/": dict(
        title="Automatisation WhatsApp et IA au Bénin | Deks Nexa",
        description="Automatisation WhatsApp et assistants IA pour entreprises au Bénin : réponses aux questions fréquentes, relances et suivi, sans perdre le contact humain.",
        label="WhatsApp et IA",
        intro=("À Cotonou, WhatsApp est souvent le premier canal de contact entre une entreprise et ses clients. Les messages arrivent à "
               "toute heure, les mêmes questions reviennent et certaines demandes restent sans réponse. Deks Nexa met en place des "
               "automatisations WhatsApp et des assistants IA qui répondent vite, relancent au bon moment et passent la main à une "
               "personne quand c'est nécessaire."),
        problem_title="Les messages s'accumulent plus vite qu'on ne peut y répondre.", problem_word="plus vite",
        problem_text=[
            "Horaires, prix, disponibilité, livraison, suivi de commande : une grande partie des messages reçus pose des questions déjà "
            "posées la veille. Y répondre un par un occupe quelqu'un une bonne partie de la journée.",
            "Pendant ce temps, les demandes importantes se noient dans le fil de discussion, les devis promis ne sont pas relancés et les "
            "clients qui écrivent le soir attendent le lendemain.",
            "<strong>L'automatisation traite le répétitif ; l'humain garde le relationnel.</strong> Les réponses simples partent tout de "
            "suite, les demandes sont classées et vous intervenez là où votre expertise fait la différence.",
        ],
        deliver_title="Des automatisations utiles, reliées à vos outils.", deliver_word="reliées à vos outils",
        deliver_intro="Chaque automatisation part d'un échange réel avec vos clients et reste sous votre contrôle.",
        deliver=[
            ("Réponses aux questions fréquentes", "Message d'accueil, horaires, catalogue, conditions : envoyés automatiquement, dans le ton de votre entreprise."),
            ("Assistant IA sur vos informations", "Un assistant qui s'appuie sur vos propres documents et vos règles, et qui sait dire quand il ne sait pas."),
            ("Relances et rappels", "Devis en attente, rendez-vous, paiements : des rappels envoyés au bon moment."),
            ("Passage à une personne", "Dès qu'une demande sort du cadre, la conversation est transférée à la bonne personne avec son historique."),
            ("Classement des demandes", "Les messages sont triés par type et alimentent votre suivi, au lieu de rester dans un seul téléphone."),
            ("Connexion à votre logiciel", "Les informations utiles remontent vers votre <a href=\"/logiciel-de-gestion-benin/\">logiciel de gestion</a> : client, demande, statut."),
        ],
        steps_title="Automatiser sans perdre la relation client.", steps_word="la relation client",
        steps_intro="Nous commençons par ce qui fait gagner le plus de temps, puis nous élargissons.",
        steps=[
            ("Analyser les échanges", "Nous identifions avec vous les questions qui reviennent et les moments où des demandes se perdent."),
            ("Écrire les scénarios", "Messages, règles de transfert et limites de l'assistant sont validés avec vous, avec un devis détaillé."),
            ("Mettre en place", "Les automatisations sont configurées, testées sur des cas réels, puis activées progressivement."),
            ("Ajuster", "Nous relisons les conversations avec vous et améliorons les réponses au fil du temps."),
        ],
        who_title="Pour les entreprises qui vivent sur WhatsApp.", who_word="sur WhatsApp",
        who_intro="Plus le volume de messages est important, plus l'automatisation libère du temps.",
        who=[
            ("Hôtels et restaurants", "Réservations, menus et questions pratiques à toute heure.", "/solutions/hotels-restaurants/"),
            ("Cliniques", "Prises de rendez-vous et rappels pour les patients.", "/solutions/cliniques/"),
            ("Commerces", "Disponibilité des produits, prix et suivi des commandes.", "/solutions/commerces/"),
            ("Écoles", "Informations aux parents et rappels de scolarité.", "/solutions/ecoles/"),
        ],
        extra=["<strong>Un assistant IA peut-il se tromper ?</strong> Oui, comme toute personne qui répond vite. C'est pourquoi nous "
               "limitons l'assistant aux sujets que vous avez validés, nous lui faisons transférer les demandes sensibles et nous relisons "
               "régulièrement ses réponses avec vous. Pour en savoir plus, lisez notre article sur "
               "<a href=\"/blog/whatsapp-business-automatiser-reponses/\">WhatsApp Business et l'automatisation des réponses</a>."],
        faq_title="Vos questions sur l'automatisation WhatsApp.", faq_word="WhatsApp",
        faq=[
            ("Faut-il WhatsApp Business pour automatiser ?",
             "Oui : l'automatisation repose sur l'application WhatsApp Business ou sur l'API WhatsApp Business, selon le volume et les fonctions voulues. Nous vous aidons à choisir."),
            ("Mes clients sauront-ils qu'ils parlent à un assistant ?",
             "Nous recommandons de l'indiquer clairement et de toujours proposer de parler à une personne. C'est plus honnête et cela rassure."),
            ("Combien coûte une automatisation WhatsApp ?",
             "Le tarif dépend des scénarios, du volume de messages et des connexions à vos outils. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/solutions/hotels-restaurants/", "/solutions/commerces/", "/solutions/cliniques/"],
    ),
    "/referencement-google-benin/": dict(
        title="Référencement Google et fiche Google au Bénin | Deks Nexa",
        description="Référencement Google au Bénin : fiche Google Business, site optimisé et contenus utiles pour être trouvé à Cotonou quand vos clients vous cherchent.",
        label="Référencement Google",
        intro=("Quand quelqu'un cherche votre métier à Cotonou, Google affiche une carte, quelques fiches d'entreprises et des sites. "
               "Si vous n'y êtes pas, le client contacte quelqu'un d'autre. Deks Nexa travaille votre fiche Google Business et votre "
               "site pour que vous apparaissiez au bon moment, avec des informations justes et rassurantes."),
        problem_title="Être bon dans son métier ne suffit pas si personne ne vous trouve.", problem_word="personne ne vous trouve",
        problem_text=[
            "Beaucoup d'entreprises n'ont pas encore de fiche Google Business, ou une fiche incomplète : pas d'horaires, pas de photos, "
            "un numéro qui ne répond plus. Pour le client, c'est un signal de doute.",
            "Côté site, des pages sans titre clair, lentes sur téléphone ou sans contenu utile ont peu de chances d'être bien classées, "
            "même si l'entreprise est sérieuse.",
            "<strong>Le référencement consiste à donner à Google, et aux clients, les bonnes informations.</strong> Une fiche complète et "
            "vérifiée, un site clair et rapide, et des pages qui répondent aux vraies questions de vos clients.",
        ],
        deliver_title="Une présence sur Google complète et soignée.", deliver_word="complète et soignée",
        deliver_intro="Nous travaillons à la fois sur la fiche, sur le site et sur les contenus, car les trois se renforcent.",
        deliver=[
            ("Fiche Google Business", "Création ou reprise de la fiche, catégories, horaires, photos, services et lien vers votre site."),
            ("Avis clients", "Une démarche simple pour inviter vos clients satisfaits à donner leur avis, et pour répondre à ceux que vous recevez."),
            ("Optimisation du site", "Titres, descriptions, structure des pages, vitesse sur mobile et données structurées."),
            ("Pages par service", "Des pages claires pour chaque service important, écrites pour vos clients avant de l'être pour Google."),
            ("Articles utiles", "Des articles qui répondent aux questions de vos clients, comme ceux de notre <a href=\"/blog/\">blog</a>."),
            ("Suivi et ajustements", "Suivi de la visibilité et des demandes reçues, puis ajustements réguliers."),
        ],
        steps_title="Une démarche claire, sans promesse irréaliste.", steps_word="sans promesse irréaliste",
        steps_intro="Personne ne peut garantir une première place sur Google. Nous mettons en place ce qui compte vraiment, et nous mesurons.",
        steps=[
            ("Faire le point", "Nous regardons votre fiche, votre site et ce qui apparaît quand on cherche votre métier."),
            ("Prioriser", "Les actions les plus utiles sont listées et chiffrées dans un devis détaillé."),
            ("Mettre en œuvre", "Fiche, pages, contenus et corrections techniques sont réalisés étape par étape."),
            ("Suivre", "Nous suivons les résultats avec vous et ajustons les contenus dans la durée."),
        ],
        who_title="Pour les entreprises que l'on cherche près de chez soi.", who_word="près de chez soi",
        who_intro="Le référencement local compte surtout quand le client choisit en fonction de la proximité et de la confiance.",
        who=[
            ("Cliniques", "Les patients cherchent un établissement proche et bien noté.", "/solutions/cliniques/"),
            ("Hôtels et restaurants", "Les voyageurs comparent sur Google avant de réserver.", "/solutions/hotels-restaurants/"),
            ("Avocats et notaires", "La confiance se construit dès la recherche.", "/solutions/avocats-notaires/"),
            ("Commerces et quincailleries", "Les clients vérifient horaires et disponibilité avant de se déplacer.", "/solutions/commerces/"),
        ],
        extra=["<strong>Combien de temps avant de voir des résultats ?</strong> Une fiche Google Business peut apparaître assez vite une "
               "fois validée. Le référencement d'un site se construit plus progressivement : il dépend de la concurrence sur votre métier "
               "et de la régularité des contenus publiés. Nous détaillons ces points dans notre article "
               "<a href=\"/blog/apparaitre-sur-google-cotonou/\">pourquoi apparaître sur Google à Cotonou</a>."],
        faq_title="Vos questions sur le référencement Google.", faq_word="référencement Google",
        faq=[
            ("Pouvez-vous garantir la première place sur Google ?",
             "Non, et personne ne peut le garantir honnêtement. Nous mettons en place les bonnes pratiques et nous suivons les résultats avec vous."),
            ("Faut-il un site pour être sur Google Maps ?",
             "Non, une fiche Google Business suffit pour apparaître sur la carte. Un site bien construit renforce néanmoins la fiche et rassure les clients."),
            ("Combien coûte le référencement ?",
             "Le tarif dépend de l'état de départ, du nombre de pages et du suivi souhaité. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/creation-site-web-benin/", "/solutions/cliniques/", "/solutions/hotels-restaurants/"],
    ),
}

# ------------------------------------------------------------------ pages métiers
METIER_PAGES = {
    "/solutions/commerces/": dict(
        h1_word="commerces et quincailleries",
        title="Logiciel commerce et quincaillerie au Bénin | Deks Nexa",
        description="Logiciel de gestion pour commerces et quincailleries au Bénin : stock de nombreux articles, caisse, crédit clients et fournisseurs suivis au jour le jour.",
        label="Commerces et quincailleries",
        intro=("Une quincaillerie ou un commerce de gros à Cotonou gère de nombreuses références, des clients qui achètent à crédit et "
               "des fournisseurs à payer. Deks Nexa conçoit des logiciels de gestion qui suivent le stock, la caisse et les comptes "
               "clients sans alourdir le travail au comptoir."),
        problem_title="Au comptoir, tout va vite. Le stock, lui, se dérègle.", problem_word="se dérègle",
        problem_text=[
            "Vis, câbles, sacs de ciment, peinture au litre, articles vendus à l'unité ou au carton : les unités de vente varient et les "
            "références se ressemblent. Sans outil adapté, le prix appliqué dépend du vendeur et le stock réel s'éloigne de ce que l'on croit avoir.",
            "Le crédit client complique encore les choses. Les ardoises sont notées dans un cahier, les remboursements partiels s'oublient "
            "et il devient difficile de savoir qui doit quoi.",
            "<strong>Un logiciel pensé pour le commerce</strong> fixe les prix, suit chaque vente et chaque paiement, et vous dit en fin de "
            "journée ce qui est sorti, ce qui est encaissé et ce qui reste dû.",
        ],
        deliver_title="Les fonctions dont un commerce a vraiment besoin.", deliver_word="vraiment besoin",
        deliver_intro="Rien de superflu : des écrans rapides au comptoir et des tableaux clairs pour le gérant.",
        deliver=[
            ("Catalogue et unités de vente", "Articles à l'unité, au mètre, au carton ou au sac, avec un prix par unité et, si vous le souhaitez, par type de client."),
            ("Caisse rapide", "Recherche d'article par nom ou référence, remises encadrées, ticket ou facture."),
            ("Crédit et comptes clients", "Ventes à crédit, acomptes, remboursements partiels et relevé de compte par client."),
            ("Fournisseurs et achats", "Commandes, réceptions et dettes fournisseurs suivies au même endroit."),
            ("Stock et inventaires", "Mouvements enregistrés à chaque vente et réception, alertes avant la rupture et inventaires guidés."),
            ("Tableau de bord du gérant", "Ventes du jour, articles qui tournent, marges et sommes à encaisser."),
        ],
        steps_title="Un logiciel adapté à votre magasin, pas l'inverse.", steps_word="pas l'inverse",
        steps_intro="Nous partons de votre comptoir, de vos habitudes de vente et de vos contraintes.",
        steps=[
            ("Observer le magasin", "Comment les clients achètent, comment les prix sont fixés, comment le crédit est accordé."),
            ("Organiser le catalogue", "Nous structurons vos articles et vos unités, puis proposons les écrans avec un devis détaillé."),
            ("Développer et tester", "Le logiciel est construit par étapes et essayé avec vos vendeurs sur de vraies ventes."),
            ("Démarrer et suivre", "Inventaire de départ, prise en main, puis ajustements et maintenance."),
        ],
        who_title="Pour les commerces de détail et de gros.", who_word="de détail et de gros",
        who_intro="Le logiciel s'adapte à la taille du commerce et au nombre de points de vente.",
        who=[
            ("Quincailleries et matériaux", "Nombreuses références et unités de vente variées.", None),
            ("Boutiques et supérettes", "Ventes rapides et réapprovisionnement régulier.", None),
            ("Grossistes et distributeurs", "Clients professionnels, crédit et livraisons.", None),
            ("Magasins avec dépôt", "Stock réparti entre le magasin et l'entrepôt.", None),
        ],
        extra=["<strong>Faut-il tout informatiser d'un coup ?</strong> Non. On peut commencer par le stock et la caisse, puis ajouter le "
               "crédit client, les fournisseurs ou un tableau de bord. Le logiciel est conçu pour grandir avec le magasin. "
               "Notre article <a href=\"/blog/logiciel-gestion-stock-benin-comment-savoir/\">comment savoir s'il vous faut un logiciel de stock</a> "
               "vous aide à faire le point."],
        faq_title="Vos questions sur le logiciel pour commerces.", faq_word="commerces",
        faq=[
            ("Le logiciel gère-t-il les ventes au mètre ou au carton ?",
             "Oui. Chaque article peut avoir plusieurs unités de vente et un prix pour chacune."),
            ("Peut-on suivre ce que chaque client nous doit ?",
             "Oui. Chaque vente à crédit et chaque remboursement sont enregistrés sur le compte du client, qui peut recevoir un relevé."),
            ("Combien coûte un logiciel pour un commerce ?",
             "Le tarif dépend des fonctions retenues, du nombre d'utilisateurs et de points de vente. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/logiciel-gestion-stock-benin/", "/logiciel-de-gestion-benin/", "/referencement-google-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un logiciel de gestion pour mon commerce.",
    ),
    "/solutions/ecoles/": dict(
        h1_word="gestion scolaire",
        title="Logiciel de gestion scolaire au Bénin | Deks Nexa",
        description="Logiciel de gestion scolaire au Bénin : inscriptions, scolarités, notes, bulletins et communication avec les parents, plus un site clair pour votre école.",
        label="Écoles",
        intro=("Une école privée à Cotonou gère à la fois des élèves, des familles, des enseignants et des paiements étalés sur l'année. "
               "Deks Nexa conçoit des logiciels de gestion scolaire et des sites d'école qui simplifient l'administration et rassurent les parents."),
        problem_title="L'administration prend le temps qui devrait aller aux élèves.", problem_word="aux élèves",
        problem_text=[
            "Inscriptions sur papier, scolarités suivies dans un tableur, reçus à retrouver, bulletins recopiés à la main : chaque rentrée "
            "et chaque période d'examens mobilisent le personnel administratif pendant des semaines.",
            "Les parents, eux, veulent savoir où en sont les paiements, les notes et les absences, sans devoir se déplacer à chaque question.",
            "<strong>Un logiciel de gestion scolaire centralise la vie de l'école.</strong> Les dossiers des élèves, les paiements, les notes "
            "et les communications sont au même endroit, avec des accès adaptés à chaque profil.",
        ],
        deliver_title="Tout ce qu'une école privée doit pouvoir suivre.", deliver_word="doit pouvoir suivre",
        deliver_intro="Des modules choisis selon l'organisation de votre établissement.",
        deliver=[
            ("Inscriptions et dossiers", "Fiche de chaque élève, pièces du dossier, classe, responsables légaux et historique."),
            ("Scolarités et paiements", "Échéanciers, versements, reçus et relances pour les montants en retard."),
            ("Notes et bulletins", "Saisie des notes par les enseignants, calcul des moyennes selon vos règles et bulletins prêts à imprimer."),
            ("Absences et discipline", "Suivi des absences et des retards, et information des familles."),
            ("Communication avec les parents", "Messages, annonces et, si vous le souhaitez, une <a href=\"/application-mobile-benin/\">application mobile pour les parents</a>."),
            ("Site de l'école", "Un <a href=\"/creation-site-web-benin/\">site web</a> clair : présentation, cycles, inscriptions, actualités et contact."),
        ],
        steps_title="Mettre en place l'outil au bon moment de l'année.", steps_word="au bon moment",
        steps_intro="Une bascule réussie se prépare avant la rentrée ou entre deux périodes.",
        steps=[
            ("Comprendre l'établissement", "Cycles, classes, règles de calcul des moyennes et modalités de paiement des familles."),
            ("Proposer", "Les modules prioritaires et le calendrier de mise en place, avec un devis détaillé."),
            ("Construire et importer", "Développement par étapes et reprise des listes d'élèves existantes."),
            ("Former et accompagner", "Prise en main par l'administration et les enseignants, puis suivi pendant l'année."),
        ],
        who_title="Pour tous les établissements privés.", who_word="établissements privés",
        who_intro="Le logiciel s'adapte au nombre de cycles et à l'organisation de chaque école.",
        who=[
            ("Écoles maternelles et primaires", "Suivi des familles et des paiements simplifié.", None),
            ("Collèges et lycées privés", "Notes, bulletins et examens selon vos règles.", None),
            ("Centres de formation", "Sessions, inscriptions et attestations.", None),
            ("Groupes scolaires", "Plusieurs établissements suivis dans un même outil.", None),
        ],
        extra=["<strong>Qui a accès aux informations des élèves ?</strong> Les accès sont définis par profil : direction, secrétariat, "
               "enseignants, parents. Chacun ne voit que ce qui le concerne, et les données restent sous le contrôle de l'établissement."],
        faq_title="Vos questions sur la gestion scolaire.", faq_word="gestion scolaire",
        faq=[
            ("Le calcul des moyennes peut-il suivre nos propres règles ?",
             "Oui. Les coefficients, les périodes et le mode de calcul sont paramétrés selon le fonctionnement de votre établissement."),
            ("Peut-on reprendre nos listes d'élèves actuelles ?",
             "Oui. Les listes existantes sont importées lors de la mise en service pour éviter une nouvelle saisie."),
            ("Combien coûte un logiciel de gestion scolaire ?",
             "Le tarif dépend des modules, du nombre d'élèves et des accès prévus. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/logiciel-de-gestion-benin/", "/creation-site-web-benin/", "/application-mobile-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un logiciel de gestion pour mon école.",
    ),
    "/solutions/cliniques/": dict(
        h1_word="prise de rendez-vous",
        title="Logiciel pour clinique et rendez-vous au Bénin | Deks Nexa",
        description="Logiciel de gestion pour cliniques au Bénin : prise de rendez-vous, dossiers patients, facturation des actes et suivi des consommables, en toute sécurité.",
        label="Cliniques",
        intro=("Une clinique ou un cabinet médical à Cotonou jongle chaque jour entre l'accueil des patients, les rendez-vous, les dossiers, "
               "la facturation et les consommables. Deks Nexa conçoit des logiciels qui fluidifient l'accueil et protègent les informations, "
               "pour que les soignants se concentrent sur les patients."),
        problem_title="L'accueil déborde et les dossiers se dispersent.", problem_word="se dispersent",
        problem_text=[
            "Rendez-vous pris par téléphone et notés dans un agenda papier, patients qui attendent sans savoir quand ils passeront, dossiers "
            "répartis entre plusieurs classeurs : l'organisation repose sur la mémoire de quelques personnes.",
            "À la caisse, il faut retrouver les actes réalisés, appliquer les bons tarifs et suivre ce qui est pris en charge par une assurance ou une entreprise.",
            "<strong>Un logiciel adapté à la clinique</strong> organise le parcours du patient, de la prise de rendez-vous à la facture, avec "
            "un dossier accessible aux bonnes personnes et à elles seules.",
        ],
        deliver_title="Un outil qui suit le patient de l'accueil à la facture.", deliver_word="de l'accueil à la facture",
        deliver_intro="Chaque module est conçu avec le personnel qui l'utilisera : accueil, soignants, caisse et direction.",
        deliver=[
            ("Prise de rendez-vous", "Agenda par praticien et par service, rendez-vous pris à l'accueil, par téléphone ou en ligne, et rappels aux patients."),
            ("Dossier patient", "Identité, antécédents, consultations et documents, avec des accès limités selon le rôle."),
            ("File d'attente", "Ordre de passage clair à l'accueil et dans les salles de consultation."),
            ("Facturation des actes", "Actes et tarifs, part du patient et prise en charge, reçus et suivi des impayés."),
            ("Consommables et pharmacie interne", "Entrées, sorties et alertes avant la rupture, avec la logique d'un <a href=\"/logiciel-gestion-stock-benin/\">logiciel de stock</a>."),
            ("Tableaux de bord", "Activité par service, rendez-vous honorés ou manqués, encaissements."),
        ],
        steps_title="Une mise en place qui respecte le rythme des soins.", steps_word="le rythme des soins",
        steps_intro="Le projet avance par étapes, sans interrompre l'accueil des patients.",
        steps=[
            ("Observer le parcours", "De l'arrivée du patient à sa sortie : qui fait quoi, et où l'information se perd."),
            ("Proposer", "Les modules prioritaires, les profils d'accès et un devis détaillé."),
            ("Construire et tester", "Développement par étapes et essais avec l'accueil et les soignants."),
            ("Former et suivre", "Mise en service service par service, prise en main, puis maintenance."),
        ],
        who_title="Pour les structures de santé privées.", who_word="de santé privées",
        who_intro="Le logiciel s'adapte à la taille de la structure et au nombre de services.",
        who=[
            ("Cliniques privées", "Plusieurs services, plusieurs praticiens, un parcours patient complet.", None),
            ("Cabinets médicaux", "Agenda, dossiers et facturation pour quelques praticiens.", None),
            ("Centres de santé", "Accueil de nombreux patients et suivi des consultations.", None),
            ("Laboratoires et centres d'imagerie", "Rendez-vous, examens et remise des résultats.", None),
        ],
        extra=["<strong>Et la confidentialité des données de santé ?</strong> Les informations médicales sont sensibles. Les accès sont "
               "nominatifs et limités selon le rôle de chacun, les actions importantes sont tracées et des sauvegardes régulières sont prévues dès la conception."],
        faq_title="Vos questions sur le logiciel pour cliniques.", faq_word="cliniques",
        faq=[
            ("Les patients peuvent-ils prendre rendez-vous en ligne ?",
             "Si vous le souhaitez, oui : les créneaux disponibles peuvent être proposés en ligne ou via WhatsApp, et l'agenda se met à jour automatiquement."),
            ("Qui peut consulter les dossiers patients ?",
             "Seules les personnes autorisées, selon leur rôle. Les accès sont définis avec la direction de la clinique."),
            ("Combien coûte un logiciel pour une clinique ?",
             "Le tarif dépend des modules, du nombre de services et d'utilisateurs. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/logiciel-de-gestion-benin/", "/automatisation-whatsapp-ia/", "/application-mobile-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un logiciel de gestion pour ma clinique.",
    ),
    "/solutions/immobilier/": dict(
        h1_word="gestion locative",
        title="Logiciel de gestion locative au Bénin | Deks Nexa",
        description="Logiciel de gestion locative au Bénin : biens, locataires, loyers, quittances, relances et comptes des propriétaires réunis dans un seul outil clair.",
        label="Immobilier",
        intro=("Gérer des appartements, des boutiques ou des maisons en location à Cotonou demande un suivi rigoureux : loyers, cautions, "
               "quittances, réparations et comptes rendus aux propriétaires. Deks Nexa conçoit des logiciels de gestion locative qui "
               "remplacent les cahiers et les tableurs par un suivi clair et à jour."),
        problem_title="Les impayés se repèrent quand ils sont déjà lourds.", problem_word="déjà lourds",
        problem_text=[
            "Quand les biens se multiplient, il devient difficile de savoir d'un coup d'œil qui a payé, qui est en retard et depuis quand. "
            "Les relances se font au cas par cas, souvent trop tard.",
            "Les propriétaires attendent des comptes clairs : loyers encaissés, frais engagés, sommes reversées. Les préparer à la main "
            "prend du temps et laisse place aux erreurs.",
            "<strong>Un logiciel de gestion locative</strong> rattache chaque bien à son bail, à son locataire et à son propriétaire, et "
            "suit les échéances, les paiements et les relances.",
        ],
        deliver_title="Une vue claire sur chaque bien et chaque bail.", deliver_word="chaque bail",
        deliver_intro="Pour les agences comme pour les propriétaires qui gèrent eux-mêmes plusieurs biens.",
        deliver=[
            ("Biens et lots", "Immeubles, appartements, boutiques : caractéristiques, documents et historique de chaque lot."),
            ("Baux et locataires", "Contrats, dates, montants, cautions et pièces des locataires."),
            ("Loyers et quittances", "Échéances, encaissements, quittances générées et relevés par locataire."),
            ("Relances", "Rappels avant l'échéance et relances des retards, par message ou par une <a href=\"/automatisation-whatsapp-ia/\">automatisation WhatsApp</a>."),
            ("Comptes propriétaires", "Loyers perçus, frais déduits et reversements, avec un relevé par propriétaire."),
            ("Travaux et interventions", "Demandes d'intervention, devis et suivi des réparations par bien."),
        ],
        steps_title="Reprendre votre portefeuille sans rien perdre.", steps_word="sans rien perdre",
        steps_intro="La reprise des baux en cours est préparée avec soin avant la mise en service.",
        steps=[
            ("Faire l'état des lieux", "Biens gérés, baux en cours, modes de paiement et attentes des propriétaires."),
            ("Proposer", "Les modules utiles et l'organisation de la reprise, avec un devis détaillé."),
            ("Construire et reprendre", "Développement par étapes, puis saisie ou import des baux existants."),
            ("Mettre en service", "Prise en main, premiers encaissements suivis ensemble, puis maintenance."),
        ],
        who_title="Pour ceux qui gèrent des biens, pour eux ou pour d'autres.", who_word="pour d'autres",
        who_intro="Le logiciel s'adapte au nombre de biens et au mode de gestion.",
        who=[
            ("Agences immobilières", "Gestion pour le compte de plusieurs propriétaires.", None),
            ("Propriétaires de plusieurs biens", "Suivi de ses propres locations, sans tableur.", None),
            ("Gestionnaires d'immeubles", "Parties communes, charges et interventions.", None),
            ("Promoteurs", "Suivi des lots mis en location ou en vente.", None),
        ],
        extra=["<strong>Les locataires peuvent-ils payer par mobile ?</strong> Le logiciel enregistre les paiements par mobile money, en "
               "espèces ou par virement. Une connexion automatique avec un service de paiement peut être étudiée selon le prestataire choisi."],
        faq_title="Vos questions sur la gestion locative.", faq_word="gestion locative",
        faq=[
            ("Le logiciel produit-il les quittances ?",
             "Oui. Une quittance est produite pour chaque loyer encaissé et peut être envoyée au locataire."),
            ("Peut-on suivre plusieurs propriétaires ?",
             "Oui. Chaque bien est rattaché à son propriétaire, qui dispose de son propre relevé de compte."),
            ("Combien coûte un logiciel de gestion locative ?",
             "Le tarif dépend du nombre de biens, des modules et des accès prévus. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/logiciel-de-gestion-benin/", "/automatisation-whatsapp-ia/", "/creation-site-web-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un logiciel de gestion locative.",
    ),
    "/solutions/cabinets-comptables/": dict(
        h1_word="cabinets comptables",
        title="Logiciel pour cabinets comptables au Bénin | Deks Nexa",
        description="Outils digitaux pour cabinets comptables au Bénin : collecte des pièces clients, suivi des dossiers et des échéances, échanges sécurisés, tableau de bord.",
        label="Cabinets comptables",
        intro=("Dans un cabinet comptable, le temps se perd souvent avant même la saisie : pièces qui arrivent par WhatsApp, par e-mail "
               "ou sur papier, relances pour obtenir les documents, échéances à surveiller pour chaque client. Deks Nexa conçoit des outils "
               "qui organisent cette collecte et le suivi des dossiers, pour les cabinets de Cotonou et du Bénin comme pour leurs clients."),
        problem_title="Courir après les pièces coûte plus cher que de les traiter.", problem_word="de les traiter",
        problem_text=[
            "Factures photographiées, relevés envoyés en retard, documents manquants découverts au moment de clôturer : la collecte des "
            "pièces repose sur des relances répétées et des fils de discussion difficiles à retrouver.",
            "Côté cabinet, savoir où en est chaque dossier, quelles déclarations approchent et qui s'en occupe demande souvent de consulter plusieurs personnes.",
            "<strong>Un outil sur mesure structure la relation entre le cabinet et ses clients</strong> : chaque pièce arrive au bon endroit, "
            "chaque dossier a un statut et chaque échéance est visible.",
        ],
        deliver_title="Des outils pour collecter, suivre et rendre compte.", deliver_word="rendre compte",
        deliver_intro="Ces outils complètent votre logiciel de comptabilité ; ils ne le remplacent pas.",
        deliver=[
            ("Espace de dépôt des pièces", "Vos clients déposent leurs documents dans un espace dédié, classés par période et par type."),
            ("Suivi des dossiers", "Statut de chaque dossier, collaborateur responsable et tâches en cours."),
            ("Échéances et rappels", "Calendrier des échéances par client et rappels automatiques, y compris par <a href=\"/automatisation-whatsapp-ia/\">WhatsApp</a>."),
            ("Pièces manquantes", "Listes de documents attendus et relances suivies jusqu'à réception."),
            ("Échanges sécurisés", "Documents et messages centralisés, accessibles aux seules personnes autorisées."),
            ("Tableau de bord du cabinet", "Charge de travail, dossiers en retard et échéances à venir."),
        ],
        steps_title="Partir de vos procédures, pas d'un modèle tout fait.", steps_word="vos procédures",
        steps_intro="Chaque cabinet a ses habitudes ; l'outil doit les soutenir.",
        steps=[
            ("Comprendre l'organisation", "Types de clients, missions, circuit des pièces et répartition du travail."),
            ("Proposer", "Les outils prioritaires et leur articulation avec vos logiciels existants, avec un devis détaillé."),
            ("Construire et tester", "Développement par étapes et essais avec quelques clients volontaires."),
            ("Déployer et suivre", "Invitation progressive des clients, prise en main, puis évolutions."),
        ],
        who_title="Pour les professionnels du chiffre.", who_word="du chiffre",
        who_intro="Les outils s'adaptent à la taille du cabinet et au profil de ses clients.",
        who=[
            ("Cabinets d'expertise comptable", "Nombreux dossiers et échéances réglementaires.", None),
            ("Comptables indépendants", "Gagner du temps sur la collecte et les relances.", None),
            ("Centres de gestion", "Accompagnement de nombreuses petites entreprises.", None),
            ("Services comptables d'entreprise", "Collecte interne des pièces auprès des autres services.", None),
        ],
        extra=["<strong>Faut-il changer de logiciel de comptabilité ?</strong> Non. Les outils de collecte et de suivi s'ajoutent à votre "
               "logiciel actuel. Lorsque c'est possible, les données sont exportées dans un format qu'il sait importer."],
        faq_title="Vos questions sur les outils pour cabinets comptables.", faq_word="cabinets comptables",
        faq=[
            ("Nos clients doivent-ils installer une application ?",
             "Pas nécessairement. L'espace de dépôt peut fonctionner dans un navigateur, sur ordinateur comme sur téléphone."),
            ("Les documents des clients sont-ils protégés ?",
             "Oui. Les accès sont personnels et limités selon les rôles, et les échanges sont centralisés plutôt que dispersés dans des messageries."),
            ("Combien coûtent ces outils ?",
             "Le tarif dépend des fonctions retenues et du nombre de clients concernés. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/logiciel-de-gestion-benin/", "/automatisation-whatsapp-ia/", "/creation-site-web-benin/"],
        wa="Bonjour Deks Nexa, je souhaite des outils digitaux pour mon cabinet comptable.",
    ),
    "/solutions/avocats-notaires/": dict(
        h1_word="avocats et notaires",
        title="Site web pour avocats et notaires au Bénin | Deks Nexa",
        description="Site web et logiciel pour cabinets d'avocats et notaires au Bénin : présence sobre et rassurante, suivi des dossiers, des échéances et des documents.",
        label="Avocats et notaires",
        intro=("Le choix d'un avocat ou d'un notaire repose sur la confiance, et cette confiance se construit souvent dès la première "
               "recherche. Deks Nexa crée pour les cabinets de Cotonou des sites web sobres et précis, ainsi que des outils de suivi des "
               "dossiers adaptés au travail juridique."),
        problem_title="La confiance se joue avant le premier rendez-vous.", problem_word="le premier rendez-vous",
        problem_text=[
            "Un client qui cherche un professionnel du droit veut comprendre rapidement ses domaines d'intervention, sa façon de travailler "
            "et le moyen de le joindre. Sans site, ou avec un site daté, le cabinet laisse ce premier jugement au hasard.",
            "Au quotidien, les dossiers s'accumulent : échéances de procédure, pièces à réunir, actes à préparer, clients qui demandent où en est leur affaire.",
            "<strong>Un site soigné et un outil de suivi adapté</strong> donnent une image fidèle du sérieux du cabinet et libèrent du temps pour le travail de fond.",
        ],
        deliver_title="Une présence en ligne sobre et des dossiers bien tenus.", deliver_word="bien tenus",
        deliver_intro="Le ton reste celui du cabinet : précis, discret et professionnel.",
        deliver=[
            ("Site du cabinet", "Présentation, domaines d'intervention, modalités de rendez-vous et contact, dans un <a href=\"/creation-site-web-benin/\">site web</a> sobre et rapide."),
            ("Demandes de rendez-vous", "Demandes qualifiées : objet, disponibilités et coordonnées, reçues au même endroit."),
            ("Suivi des dossiers", "Fiche par dossier : parties, pièces, étapes, échéances et responsable."),
            ("Échéancier", "Dates d'audience, délais et rappels visibles par tout le cabinet."),
            ("Documents et modèles", "Classement des pièces et modèles de documents pour gagner du temps à la rédaction."),
            ("Visibilité locale", "Fiche Google Business et pages claires pour être trouvé à Cotonou, avec notre offre de <a href=\"/referencement-google-benin/\">référencement Google</a>."),
        ],
        steps_title="Un accompagnement discret et structuré.", steps_word="discret et structuré",
        steps_intro="La confidentialité guide chaque choix, de la conception à la mise en service.",
        steps=[
            ("Écouter le cabinet", "Activités, image souhaitée, organisation des dossiers et contraintes de confidentialité."),
            ("Proposer", "Le site, les outils utiles et leur ordre de mise en place, avec un devis détaillé."),
            ("Réaliser", "Rédaction des pages avec vous, développement des outils et tests."),
            ("Mettre en ligne et suivre", "Publication, prise en main et évolutions selon les besoins du cabinet."),
        ],
        who_title="Pour les professions juridiques.", who_word="juridiques",
        who_intro="Chaque profession a ses règles de communication ; le site les respecte.",
        who=[
            ("Cabinets d'avocats", "Domaines d'intervention et suivi des procédures.", None),
            ("Études notariales", "Actes, pièces à fournir et rendez-vous de signature.", None),
            ("Huissiers de justice", "Suivi des missions et des significations.", None),
            ("Conseils juridiques d'entreprise", "Suivi des contrats et des échéances.", None),
        ],
        extra=["<strong>Un site d'avocat peut-il faire de la publicité ?</strong> La communication des professions juridiques est encadrée. "
               "Nous construisons un site informatif et sobre, et vous validez chaque contenu au regard des règles de votre ordre."],
        faq_title="Vos questions sur le site et le suivi des dossiers.", faq_word="suivi des dossiers",
        faq=[
            ("Le site présentera-t-il nos honoraires ?",
             "C'est votre choix. Le site peut présenter vos modalités d'intervention sans afficher de tarifs, ou les préciser si vos règles professionnelles le permettent."),
            ("Les informations des dossiers sont-elles confidentielles ?",
             "Oui. L'outil de suivi est réservé au cabinet, avec des accès personnels et limités selon le rôle de chacun."),
            ("Combien coûtent un site et un outil de suivi ?",
             "Le tarif dépend du nombre de pages et des fonctions de suivi retenues. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/creation-site-web-benin/", "/referencement-google-benin/", "/logiciel-de-gestion-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un site web pour mon cabinet.",
    ),
    "/solutions/ong/": dict(
        h1_word="collecte de données",
        title="Site web et outils de collecte pour ONG au Bénin | Deks Nexa",
        description="Site web et collecte de données pour ONG au Bénin : présenter vos projets, collecter les données du terrain sur mobile et rendre compte aux partenaires.",
        label="ONG",
        intro=("Une ONG doit à la fois agir sur le terrain, documenter ses actions et rendre compte à ses partenaires. Deks Nexa conçoit "
               "pour les organisations du Bénin des sites web clairs pour présenter les projets, et des outils de collecte de données "
               "mobiles qui facilitent le suivi et la préparation des rapports."),
        problem_title="Les données du terrain mettent trop de temps à remonter.", problem_word="à remonter",
        problem_text=[
            "Questionnaires papier, fichiers envoyés par plusieurs animateurs, photos dispersées : consolider les informations du terrain "
            "prend des jours, et les erreurs de saisie s'invitent à chaque étape.",
            "Au moment du rapport, il faut retrouver les données, les illustrer et les présenter de façon convaincante aux bailleurs et aux partenaires.",
            "<strong>Des outils adaptés relient le terrain, le bureau et les partenaires</strong> : les données sont saisies une fois, "
            "vérifiées dès la collecte et disponibles pour les rapports.",
        ],
        deliver_title="Montrer votre impact et suivre vos activités.", deliver_word="votre impact",
        deliver_intro="Des outils simples pour ceux qui collectent, et clairs pour ceux qui lisent les rapports.",
        deliver=[
            ("Site de l'ONG", "Mission, projets, zones d'intervention, partenaires et actualités, dans un <a href=\"/creation-site-web-benin/\">site web</a> clair."),
            ("Formulaires mobiles", "Questionnaires sur téléphone, avec contrôles de saisie, photos et localisation si nécessaire, via une <a href=\"/application-mobile-benin/\">application mobile</a>."),
            ("Base des bénéficiaires", "Suivi des personnes ou des structures accompagnées, avec des accès limités."),
            ("Tableaux de bord", "Indicateurs des projets mis à jour à partir des données collectées."),
            ("Exports pour les rapports", "Données prêtes à intégrer dans les rapports destinés aux partenaires."),
            ("Pages projets", "Une page par projet pour présenter objectifs, activités et résultats publiés."),
        ],
        steps_title="Des outils construits avec ceux qui collectent.", steps_word="ceux qui collectent",
        steps_intro="Les formulaires sont testés sur le terrain avant d'être généralisés.",
        steps=[
            ("Comprendre les projets", "Indicateurs suivis, données à collecter, contraintes du terrain et exigences des partenaires."),
            ("Concevoir", "Formulaires, tableaux de bord et pages du site, avec un devis détaillé."),
            ("Tester sur le terrain", "Essai avec quelques animateurs, ajustements, puis généralisation."),
            ("Former et suivre", "Formation des utilisateurs, puis maintenance et évolutions au fil des projets."),
        ],
        who_title="Pour les organisations qui rendent compte de leur action.", who_word="de leur action",
        who_intro="Associations, ONG nationales ou internationales, projets financés par des partenaires.",
        who=[
            ("ONG nationales", "Visibilité et suivi des activités dans plusieurs zones.", None),
            ("Associations", "Présenter l'association et mobiliser les soutiens.", None),
            ("Projets de développement", "Collecte d'indicateurs et rapports aux bailleurs.", None),
            ("Fondations", "Suivi des initiatives soutenues.", None),
        ],
        extra=["<strong>Et la protection des données des bénéficiaires ?</strong> Les données personnelles sont collectées au strict nécessaire, "
               "avec des accès limités et des règles de conservation définies avec vous."],
        faq_title="Vos questions sur les outils pour ONG.", faq_word="ONG",
        faq=[
            ("La collecte fonctionne-t-elle sans connexion internet ?",
             "Cela peut être prévu : le formulaire enregistre alors les réponses sur le téléphone et les envoie dès que la connexion revient."),
            ("Pouvons-nous modifier les questionnaires nous-mêmes ?",
             "Si vous le souhaitez, nous prévoyons un espace pour créer ou adapter les formulaires sans développement."),
            ("Combien coûtent un site et des outils de collecte ?",
             "Le tarif dépend des fonctions retenues, du nombre de formulaires et d'utilisateurs. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/creation-site-web-benin/", "/application-mobile-benin/", "/logiciel-de-gestion-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un site ou un outil de collecte pour mon ONG.",
    ),
    "/solutions/hotels-restaurants/": dict(
        h1_word="menu en ligne",
        title="Site hôtel et restaurant, réservation à Cotonou | Deks Nexa",
        description="Site web, réservation et menu en ligne pour hôtels et restaurants au Bénin : chambres, tables, commandes et visibilité sur Google à Cotonou.",
        label="Hôtels et restaurants",
        intro=("Avant de réserver une chambre ou une table à Cotonou, les clients regardent des photos, comparent et cherchent à joindre "
               "l'établissement rapidement. Deks Nexa crée pour les hôtels et les restaurants des sites clairs, des systèmes de "
               "réservation et des menus en ligne qui facilitent la décision et la prise de contact."),
        problem_title="Les clients décident vite, souvent sur leur téléphone.", problem_word="sur leur téléphone",
        problem_text=[
            "Un menu en photo floue, des tarifs introuvables, un numéro qui ne répond pas le soir : chaque obstacle envoie le client vers un autre établissement.",
            "En interne, les réservations notées sur plusieurs supports se chevauchent, et les commandes passées par téléphone ou par "
            "message se perdent aux heures de pointe.",
            "<strong>Un site et des outils pensés pour l'accueil</strong> montrent l'établissement sous son meilleur jour, recueillent les "
            "réservations au même endroit et répondent aux questions pratiques sans attendre.",
        ],
        deliver_title="Donner envie, puis faciliter la réservation.", deliver_word="faciliter la réservation",
        deliver_intro="Chaque outil peut être mis en place seul ou avec les autres.",
        deliver=[
            ("Site de l'établissement", "Photos, chambres ou salles, ambiance, accès et contact, dans un <a href=\"/creation-site-web-benin/\">site web</a> rapide sur mobile."),
            ("Réservations", "Demandes de chambres ou de tables centralisées, avec confirmation au client."),
            ("Menu en ligne", "Menu consultable sur téléphone, facile à mettre à jour, accessible par un lien ou un QR code."),
            ("Commandes à emporter", "Prise de commande en ligne ou via WhatsApp, avec suivi jusqu'à la remise."),
            ("Réponses automatiques", "Horaires, disponibilités et questions fréquentes traitées par une <a href=\"/automatisation-whatsapp-ia/\">automatisation WhatsApp</a>."),
            ("Stock des boissons et denrées", "Suivi des entrées et des sorties avec un <a href=\"/logiciel-gestion-stock-benin/\">logiciel de stock</a> adapté."),
        ],
        steps_title="Des outils prêts avant le prochain coup de feu.", steps_word="coup de feu",
        steps_intro="La mise en place s'organise en fonction de vos périodes d'affluence.",
        steps=[
            ("Découvrir l'établissement", "Votre clientèle, vos canaux de réservation et vos moments de forte affluence."),
            ("Proposer", "Le site, les outils prioritaires et un devis détaillé."),
            ("Réaliser", "Photos et textes rassemblés avec vous, développement et tests avec le personnel d'accueil."),
            ("Lancer et suivre", "Mise en ligne, prise en main, puis mises à jour du menu et des offres."),
        ],
        who_title="Pour les lieux qui accueillent.", who_word="qui accueillent",
        who_intro="Les outils s'adaptent à la taille de l'établissement et à sa clientèle.",
        who=[
            ("Hôtels et résidences", "Chambres, services et réservations directes.", None),
            ("Restaurants et maquis", "Menu, réservations et commandes à emporter.", None),
            ("Bars et lounges", "Événements, carte et réservation de tables.", None),
            ("Traiteurs et salles de réception", "Demandes de devis et calendrier des événements.", None),
        ],
        extra=["<strong>Faut-il passer par les plateformes de réservation ?</strong> Elles apportent de la visibilité, mais prélèvent une "
               "commission et gardent la relation client. Un site avec réservation directe vous permet de recevoir une partie des demandes "
               "sans intermédiaire, en complément de ces plateformes."],
        faq_title="Vos questions sur le site et les réservations.", faq_word="les réservations",
        faq=[
            ("Le menu en ligne est-il facile à modifier ?",
             "Oui. Les plats, les prix et les disponibilités se mettent à jour depuis un espace simple."),
            ("Les clients peuvent-ils réserver sans appeler ?",
             "Oui. Le formulaire de réservation ou WhatsApp permet de demander une chambre ou une table, et vous confirmez la demande."),
            ("Combien coûte un site avec réservation ?",
             "Le tarif dépend des pages et des fonctions de réservation et de commande retenues. Après étude du besoin, nous vous remettons un devis détaillé."),
            (PAY_Q, PAY_A),
        ],
        related=["/creation-site-web-benin/", "/automatisation-whatsapp-ia/", "/referencement-google-benin/"],
        wa="Bonjour Deks Nexa, je souhaite un site avec réservation pour mon établissement.",
    ),
}
