# Contenu éditorial du site Deks Nexa (référencement).
# Règle : aucun prix, chiffre, client ou avis inventé. Les modalités commerciales sont précisées dans le devis.

DEFAULT_WA = "Bonjour Deks Nexa, je souhaite parler de mon projet."

# ------------------------------------------------------------------ services (ordre de priorité)
SERVICES = [
    dict(
        url="/logiciel-de-gestion-benin/", anchor="logiciel-de-gestion", menu="Logiciel de gestion",
        tag="Logiciel de gestion · ERP", h1="Logiciel de gestion sur mesure au Bénin", h1_word="sur mesure",
        row_title="Tout centraliser et piloter dans un seul logiciel.",
        problem="Clients, ventes, factures et stocks sont éparpillés dans des cahiers et des fichiers Excel.",
        teaser="Clients, ventes, factures, stocks et tableaux de bord réunis dans un seul outil.",
        summary="Un logiciel conçu autour de vos règles : clients, ventes, devis, factures, stocks et tableaux de bord, accessibles selon le rôle de chacun.",
        checks=["Clients, fournisseurs et historique", "Devis, factures et suivi des paiements", "Stocks et achats",
                "Tableaux de bord de l'activité", "Accès par rôle : gérant, caisse, comptabilité"],
        wa="Bonjour Deks Nexa, je souhaite un logiciel de gestion pour mon entreprise.",
        ready=True, nav="services", og="logiciel-de-gestion-benin",
        title="Logiciel de gestion sur mesure au Bénin | Deks Nexa",
        description="Logiciel de gestion sur mesure au Bénin : clients, ventes, factures, stocks et tableaux de bord réunis dans un seul outil. Parlons-en sur WhatsApp.",
        og_alt="Logiciel de gestion sur mesure au Bénin, par Deks Nexa",
        service="Logiciel de gestion sur mesure", service_type="Développement de logiciel de gestion",
        crumbs=[("Accueil", "/"), ("Services", "/service.html"), ("Logiciel de gestion", "/logiciel-de-gestion-benin/")],
        label="Logiciel de gestion",
        intro=("À Cotonou comme dans tout le Bénin, beaucoup d'entreprises suivent encore leurs clients, leurs ventes et leurs stocks "
               "dans des cahiers, des fichiers Excel et des groupes WhatsApp. Deks Nexa conçoit votre logiciel de gestion sur mesure : "
               "un seul outil, à vos règles, pour savoir chaque jour où en est votre activité."),
        problem_label="Le problème", problem_title="Quand l'entreprise grandit, les fichiers ne suivent plus.", problem_word="ne suivent plus",
        problem_text=[
            "Au début, un cahier et quelques fichiers Excel suffisent. Puis les clients se multiplient, une deuxième personne encaisse, "
            "un fournisseur livre en retard, et les informations finissent dispersées entre plusieurs téléphones et plusieurs versions du même fichier.",
            "Les conséquences sont concrètes : une facture oubliée, un stock qui ne correspond plus à la réalité, un client relancé deux fois "
            "ou jamais, et un chiffre d'affaires qu'il faut reconstituer à la main en fin de mois. Le gérant passe ses soirées à vérifier au lieu de décider.",
            "<strong>Un logiciel de gestion d'entreprise sur mesure remet de l'ordre.</strong> Chaque vente, chaque paiement et chaque mouvement de stock "
            "est saisi une seule fois, au bon endroit, par la bonne personne. Les tableaux de bord se mettent à jour seuls et vous retrouvez une information en quelques secondes.",
        ],
        deliver_title="Un logiciel de gestion à la mesure de votre entreprise.", deliver_word="à la mesure",
        deliver_intro="Nous assemblons les modules dont vous avez besoin, rien de plus. Chaque écran est pensé pour les personnes qui l'utiliseront au quotidien.",
        deliver=[
            ("Clients et fournisseurs", "Fiches complètes, historique des achats, coordonnées et relances : toute la relation au même endroit."),
            ("Devis, factures et paiements", "Devis transformés en factures, numérotation automatique, documents PDF et suivi de ce qui reste à encaisser."),
            ("Stocks et achats", "Entrées, sorties, alertes avant la rupture et commandes fournisseurs. Pour un besoin plus poussé, voyez notre <a href=\"/logiciel-gestion-stock-benin/\">logiciel de gestion de stock et de caisse</a>."),
            ("Tableaux de bord", "Ventes du jour, chiffre d'affaires du mois, produits qui tournent, impayés : les chiffres qui comptent, sans calcul manuel."),
            ("Rôles et accès sécurisés", "Le gérant voit tout, la caisse encaisse, la comptabilité exporte. Chacun accède seulement à ce qui le concerne."),
            ("Accès depuis le bureau ou le téléphone", "Le logiciel s'utilise dans un navigateur. Si vos équipes travaillent sur le terrain, nous ajoutons une <a href=\"/application-mobile-benin/\">application mobile</a>."),
        ],
        steps_title="Du besoin au logiciel en service, en quatre étapes.", steps_word="quatre étapes",
        steps_intro="Vous restez associé à chaque étape. Rien n'est développé sans avoir été validé avec vous.",
        steps=[
            ("Écouter", "Nous observons votre façon de travailler : ce que vous vendez, qui saisit quoi, quels documents vous produisez et ce qui vous fait perdre du temps."),
            ("Proposer", "Vous recevez une proposition claire : les modules retenus, les écrans principaux, les étapes de livraison et un devis détaillé."),
            ("Construire", "Nous développons par étapes et vous montrons l'avancement régulièrement. Vos remarques sont intégrées au fil du projet."),
            ("Livrer et suivre", "Import de vos données, mise en service, prise en main par vos équipes, puis maintenance et évolutions quand votre activité change."),
        ],
        who_title="Pour les entreprises qui veulent piloter, pas seulement compter.", who_word="piloter",
        who_intro="Un logiciel de gestion commerciale ou un ERP sur mesure se justifie dès que plusieurs personnes partagent les mêmes informations.",
        who=[
            ("Commerces et quincailleries", "Ventes au comptoir, crédit clients, stock de milliers d'articles.", "/solutions/commerces/"),
            ("Écoles privées", "Inscriptions, scolarités, paiements des familles et suivi des élèves.", "/solutions/ecoles/"),
            ("Cliniques et cabinets", "Rendez-vous, dossiers patients et facturation des actes.", "/solutions/cliniques/"),
            ("PME de services et distributeurs", "Devis, interventions, livraisons et suivi des commandes clients.", None),
        ],
        extra=[
            "<strong>Logiciel sur mesure ou logiciel du marché ?</strong> Un logiciel du marché est prêt tout de suite, mais c'est votre entreprise qui doit "
            "s'adapter à lui : champs inutiles, étapes qui ne correspondent pas à votre façon de vendre, fonctionnalités payantes que vous n'utilisez pas. "
            "Un logiciel sur mesure part de vos habitudes et évolue avec vous. Il demande un peu plus de temps au départ, et c'est pour cela que nous livrons par étapes.",
        ],
        faq_title="Vos questions sur le logiciel de gestion.", faq_word="logiciel de gestion",
        faq=[
            ("Combien coûte un logiciel de gestion sur mesure au Bénin ?",
             "Le tarif dépend des modules, du nombre d'utilisateurs et des documents nécessaires. Après étude du besoin, nous vous remettons un devis détaillé."),
            ("Combien de temps faut-il pour le mettre en place ?",
             "Le projet est réalisé par étapes. Le calendrier est défini après étude du périmètre et des priorités."),
            ("Peut-on récupérer nos fichiers Excel actuels ?",
             "Oui. Lors de la mise en service, nous reprenons vos listes existantes de clients, de produits et de stocks pour que vous ne repartiez pas de zéro."),
            ("Qui s'occupe de la maintenance après la livraison ?",
             "Nous pouvons prévoir des corrections, des évolutions et de l'assistance après livraison. Les modalités sont précisées dans le devis."),
            ("Peut-on payer en plusieurs fois ?",
             "Les modalités de paiement sont précisées dans le devis, avant le démarrage du projet."),
            ("Travaillez-vous avec des entreprises hors de Cotonou ?",
             "Oui. Nous travaillons avec des entreprises de tout le Bénin et d'Afrique francophone : les échanges se font sur WhatsApp et en visioconférence."),
        ],
        related=["/logiciel-gestion-stock-benin/", "/solutions/commerces/", "/application-mobile-benin/"],
    ),
    dict(
        url="/logiciel-gestion-stock-benin/", anchor="gestion-de-stock", menu="Gestion de stock et caisse",
        tag="Stock · Caisse", h1="Logiciel de gestion de stock et de caisse au Bénin", h1_word="stock et de caisse",
        row_title="Des stocks justes et une caisse qui tombe juste.",
        problem="Les ruptures et les écarts de caisse se découvrent trop tard, souvent en fin de mois.",
        teaser="Entrées, sorties, inventaires et ventes au comptoir suivis au jour le jour.",
        summary="Entrées et sorties de marchandises, inventaires, ventes au comptoir et clôture de caisse : vous savez à tout moment ce qui est en rayon et ce qui est en caisse.",
        checks=["Entrées, sorties et transferts", "Alertes avant la rupture", "Ventes au comptoir et tickets", "Clôture de caisse quotidienne", "Inventaires simplifiés"],
        wa="Bonjour Deks Nexa, je souhaite un logiciel de gestion de stock et de caisse.",
    ),
    dict(
        url="/creation-site-web-benin/", anchor="site-web", menu="Création de site web",
        tag="Site web moderne", h1="Création de site web au Bénin", h1_word="site web",
        row_title="Un site web moderne qui inspire confiance.",
        problem="Vos clients vous cherchent sur Google et ne trouvent qu'une page Facebook.",
        teaser="Site vitrine ou boutique en ligne, rapide, clair et bien référencé.",
        summary="Site vitrine ou boutique en ligne, rapide sur mobile, clair pour vos clients et préparé pour le référencement Google.",
        checks=["Site vitrine ou boutique en ligne", "Rapide et lisible sur mobile", "Bouton WhatsApp et formulaire de contact", "Préparé pour Google", "Mises à jour et suivi"],
        wa="Bonjour Deks Nexa, je souhaite créer un site web pour mon entreprise.",
    ),
    dict(
        url="/application-mobile-benin/", anchor="application-mobile", menu="Application mobile",
        tag="Android · iOS", h1="Développement d'application mobile au Bénin", h1_word="application mobile",
        row_title="Une application mobile pour vos clients ou vos équipes.",
        problem="Vos équipes terrain remontent les informations sur papier ou par téléphone.",
        teaser="Applications Android et iOS connectées à vos données.",
        summary="Applications Android et iOS pour vos clients ou vos équipes terrain, connectées à votre logiciel de gestion.",
        checks=["Android et iOS", "Collecte de données sur le terrain", "Notifications", "Synchronisation avec votre logiciel", "Publication sur les stores"],
        wa="Bonjour Deks Nexa, je souhaite développer une application mobile.",
    ),
    dict(
        url="/automatisation-whatsapp-ia/", anchor="automatisation", menu="Automatisation WhatsApp et IA",
        tag="WhatsApp · IA", h1="Automatisation WhatsApp et assistants IA pour entreprises au Bénin", h1_word="assistants IA",
        row_title="Des réponses et des relances qui partent toutes seules.",
        problem="Les mêmes questions arrivent chaque jour sur WhatsApp et les relances se perdent.",
        teaser="Réponses automatiques, relances et assistants IA connectés à vos outils.",
        summary="Réponses automatiques sur WhatsApp, relances, notifications et assistants IA qui s'appuient sur vos propres informations.",
        checks=["Réponses automatiques WhatsApp", "Relances et rappels", "Assistant IA sur vos informations", "Notifications internes", "Connexion à votre logiciel"],
        wa="Bonjour Deks Nexa, je souhaite automatiser WhatsApp pour mon entreprise.",
    ),
    dict(
        url="/referencement-google-benin/", anchor="referencement", menu="Référencement Google",
        tag="Google · Maps", h1="Référencement Google et fiche Google Business au Bénin", h1_word="Google Business",
        row_title="Être trouvé sur Google et Google Maps.",
        problem="Quand un client cherche votre métier à Cotonou, ce sont vos concurrents qui apparaissent.",
        teaser="Référencement du site et fiche Google Business optimisée.",
        summary="Référencement de votre site, fiche Google Business et contenus utiles pour apparaître quand vos clients vous cherchent.",
        checks=["Audit de votre visibilité", "Fiche Google Business", "Optimisation des pages", "Contenus et articles", "Suivi des positions"],
        wa="Bonjour Deks Nexa, je souhaite améliorer ma visibilité sur Google.",
    ),
]

METIERS = [
    dict(url="/solutions/commerces/", menu="Commerces et quincailleries", tag="Commerce",
         h1="Logiciel de gestion pour commerces et quincailleries au Bénin", teaser="Stock, caisse et crédit clients sous contrôle."),
    dict(url="/solutions/ecoles/", menu="Écoles", tag="Éducation",
         h1="Logiciel de gestion scolaire et site d'école au Bénin", teaser="Inscriptions, scolarités, notes et site de l'école."),
    dict(url="/solutions/cliniques/", menu="Cliniques", tag="Santé",
         h1="Logiciel de gestion et prise de rendez-vous pour cliniques au Bénin", teaser="Rendez-vous, dossiers patients et facturation."),
    dict(url="/solutions/immobilier/", menu="Immobilier", tag="Immobilier",
         h1="Logiciel de gestion locative au Bénin", teaser="Biens, locataires, loyers et quittances."),
    dict(url="/solutions/cabinets-comptables/", menu="Cabinets comptables", tag="Comptabilité",
         h1="Logiciel et outils digitaux pour cabinets comptables au Bénin", teaser="Collecte des pièces et suivi des dossiers clients."),
    dict(url="/solutions/avocats-notaires/", menu="Avocats et notaires", tag="Juridique",
         h1="Site web et logiciel pour cabinets d'avocats et notaires au Bénin", teaser="Un site qui inspire confiance et des dossiers bien suivis."),
    dict(url="/solutions/ong/", menu="ONG", tag="Associatif",
         h1="Site web et collecte de données pour ONG au Bénin", teaser="Présenter vos projets et collecter les données du terrain."),
    dict(url="/solutions/hotels-restaurants/", menu="Hôtels et restaurants", tag="Hôtellerie",
         h1="Site, réservation et menu en ligne pour hôtels et restaurants au Bénin", teaser="Réservations, menu en ligne et visibilité."),
]

# ------------------------------------------------------------------ pages existantes
HOME = dict(
    url="/", og="accueil", nav="home", wa=DEFAULT_WA,
    title="Logiciels de gestion et sites web au Bénin | Deks Nexa",
    description="Deks Nexa conçoit des logiciels de gestion, des sites web, des applications et des automatisations WhatsApp pour les entreprises de Cotonou et du Bénin.",
    og_alt="Deks Nexa : logiciels de gestion et sites web au Bénin",
    intro="Deks Nexa conçoit des logiciels de gestion, des sites web, des applications et des automatisations pour les entreprises de Cotonou, du Bénin et d'Afrique francophone.",
)

HUB = dict(
    url="/service.html", og="solutions", wa=DEFAULT_WA,
    title="Services : logiciels, sites web et apps au Bénin | Deks Nexa",
    description="Logiciels de gestion, sites web, applications, automatisations WhatsApp et référencement Google : les services Deks Nexa pour les entreprises du Bénin.",
    og_alt="Les services Deks Nexa au Bénin",
    crumbs=[("Accueil", "/"), ("Services", "/service.html")],
    intro="Logiciels de gestion, sites web, applications mobiles, automatisations WhatsApp et référencement Google, pensés pour les entreprises de Cotonou et du Bénin.",
)

HUB_EXTRAS = [
    ("Intégration API", "Nous faisons circuler les données entre vos logiciels, vos paiements et vos services externes : une seule saisie, partout à jour."),
    ("Plateforme en ligne (SaaS)", "Comptes clients, abonnements et espace d'administration pour proposer votre service en ligne."),
    ("Maintenance et modernisation", "Nous reprenons un outil que vos équipes utilisent déjà pour le rendre plus stable, plus clair et plus sûr, étape par étape."),
]

ABOUT = dict(
    url="/about.html", og="a-propos", wa=DEFAULT_WA,
    title="À propos de Deks Nexa | Logiciels et sites web au Bénin",
    description="Deks Nexa accompagne les entreprises du Bénin et d'Afrique francophone : logiciels de gestion, sites web, applications et automatisations sur mesure.",
    og_alt="À propos de Deks Nexa",
    crumbs=[("Accueil", "/"), ("À propos", "/about.html")],
    intro="Deks Nexa conçoit des logiciels professionnels pour aider les organisations à structurer leurs opérations, automatiser leurs processus et mieux piloter leur activité.",
)

ABOUT_TEXT = [
    "<strong>Nous partons du métier avant la technologie.</strong> Chaque projet commence par la compréhension de vos processus, de vos contraintes et des résultats attendus. Le logiciel vient ensuite comme une réponse structurée.",
    "Nous accompagnons les entreprises qui veulent gagner du temps, mieux piloter leur activité et réduire la dépendance aux fichiers dispersés, aux tâches manuelles et aux outils mal connectés.",
    "<strong>Deks Nexa est un partenaire technique sur le long terme.</strong> Nous concevons, livrons, maintenons et améliorons les solutions pour qu'elles restent fiables quand votre organisation évolue.",
]

PROJETS = dict(
    url="/projets.html", og="realisations", wa=DEFAULT_WA,
    title="Réalisations : plateformes web et applications | Deks Nexa",
    description="Découvrez les projets conçus et développés par Deks Nexa au Bénin : Innov-Deks, notre vitrine d'innovation, et l'application mobile Life mood App.",
    og_alt="Les réalisations de Deks Nexa",
    crumbs=[("Accueil", "/"), ("Réalisations", "/projets.html")],
    intro="Des projets conçus et développés par Deks Nexa, livrés ou en cours.",
)

CONTACT = dict(
    url="/contact.html", og="contact", wa=DEFAULT_WA,
    title="Contact : parlez-nous de votre projet | Deks Nexa",
    description="Présentez votre projet à Deks Nexa : logiciel de gestion, site web ou application. Le formulaire prépare votre message WhatsApp, réponse rapide.",
    og_alt="Contacter Deks Nexa",
    crumbs=[("Accueil", "/"), ("Contact", "/contact.html")],
    intro="Remplissez le formulaire : nous préparons votre message WhatsApp avec les informations du projet. Vous pouvez aussi nous écrire directement.",
)

NOT_FOUND = dict(
    url="/404.html", og="accueil", wa=DEFAULT_WA, noindex=True,
    title="Page introuvable | Deks Nexa",
    description="Cette page n'existe pas ou a été déplacée. Retrouvez les services Deks Nexa : logiciels de gestion, sites web, applications, ou écrivez-nous.",
    og_alt="Deks Nexa",
    intro="L'adresse a peut-être changé ou n'existe plus. Voici nos services, ou écrivez-nous directement sur WhatsApp.",
)

HERO_VISUAL = """<div class="dn-hero-visual" role="img" aria-label="Illustration : le site internet de votre marque, avec une nouvelle demande reçue via le site et une activité en hausse">
<div class="dn-scene" aria-hidden="true">
<div class="dn-browser">
<div class="dn-br-bar"><span class="dn-br-dots"><i></i><i></i><i></i></span><span class="dn-br-address">{LOCK}</span></div>
<div class="dn-site">
<div class="dn-site-nav"><span class="dn-site-logo">V</span><span class="dn-site-name">Votre marque</span><span class="dn-site-links"><b></b><b></b><b></b></span><span class="dn-site-cta">Contact</span></div>
<div class="dn-site-hero">
<div><p class="dn-site-title">Faites grandir<br><em>votre marque</em>.</p><span class="dn-site-lines"><b></b><b></b></span><span class="dn-site-btn">Découvrir</span></div>
<div class="dn-site-visual"><span></span></div>
</div>
<div class="dn-site-cards"><div><i></i><b></b><b></b></div><div><i></i><b></b><b></b></div><div><i></i><b></b><b></b></div></div>
</div>
</div>
<div class="dn-pop dn-pop-lead"><span class="dn-pop-icon">{MAIL}</span><span><strong>Nouvelle demande</strong><small>Reçue via votre site</small></span></div>
<div class="dn-pop dn-growth"><div class="dn-growth-head"><strong>Votre activité</strong><span>en hausse ↗</span></div><svg class="dn-growth-chart" viewBox="0 0 200 64" focusable="false"><defs><linearGradient id="dn-growth-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5B95FF" stop-opacity=".35"/><stop offset="1" stop-color="#5B95FF" stop-opacity="0"/></linearGradient></defs><path class="dn-growth-area" d="M2 56C32 54 46 47 70 44S110 36 130 28S172 12 196 8V64H2Z"/><path class="dn-growth-line" pathLength="1" d="M2 56C32 54 46 47 70 44S110 36 130 28S172 12 196 8"/><circle class="dn-growth-dot" cx="196" cy="8" r="4"/></svg></div>
</div>
</div>"""

CONTACT_FORM = """<section class="dn-section">
<div class="dn-container dn-g12 dn-contact">
<div class="dn-reveal">
<h2 class="dn-block-title">Décrivez votre <em class="dn-serif">besoin</em></h2>
<p>Nous continuons la discussion sur WhatsApp.</p>
<form id="contactForm" class="dn-form" novalidate>
<div class="dn-fields">
<div class="dn-field"><label class="dn-tag" for="name">Nom</label><input type="text" id="name" name="name" placeholder="Votre nom" autocomplete="name" required></div>
<div class="dn-field"><label class="dn-tag" for="email">E-mail professionnel</label><input type="email" id="email" name="email" placeholder="Votre e-mail professionnel" autocomplete="email" required></div>
<div class="dn-field dn-field-full"><label class="dn-tag" for="subject">Type de projet</label><input type="text" id="subject" name="subject" placeholder="Type de projet" required></div>
<div class="dn-field dn-field-full"><label class="dn-tag" for="message">Votre besoin</label><textarea id="message" name="message" placeholder="Décrivez votre besoin" required></textarea></div>
</div>
<button class="dn-btn dn-btn-wa" type="submit">{WA}Préparer mon message WhatsApp</button>
<div class="deks-form-status" id="contactFormStatus" role="status" aria-live="polite"></div>
</form>
</div>
<aside class="dn-contact-aside dn-reveal" aria-labelledby="contact-direct">
<h2 class="dn-block-title" id="contact-direct">Contact <em class="dn-serif">direct</em></h2>
<p>Pour une question rapide, écrivez-nous directement.</p>
<ul class="dn-contact-list"><li><span class="dn-tag">WhatsApp</span><a href="https://wa.me/2290194776256" target="_blank" rel="noopener">+229 01 94 77 62 56</a></li><li><span class="dn-tag">E-mail</span><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
<div class="dn-actions">{WA_LINK}</div>
</aside>
</div>
</section>
"""

CONTACT_SCRIPT = """    <script>
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault();

            const form = event.currentTarget;
            const status = document.getElementById('contactFormStatus');
            form.classList.add('was-validated');

            if (!form.checkValidity()) {
                if (status) {
                    status.textContent = 'Merci de compléter les champs requis avant de soumettre votre demande.';
                    status.classList.add('is-visible');
                }
                return;
            }

            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();

            const whatsappMessage = [
                'Bonjour Deks Nexa, je souhaite discuter d’un projet logiciel.',
                '',
                `Nom : ${name}`,
                `Email : ${email}`,
                `Type de projet : ${subject}`,
                '',
                `Besoin : ${message}`
            ].join('\\n');

            if (status) {
                status.textContent = 'Votre message est prêt. Redirection vers WhatsApp...';
                status.classList.add('is-visible');
            }

            // Redirection vers WhatsApp dès que GA4 a envoyé l'événement (au plus tard 1,5 s) : jamais bloquée.
            let redirected = false;
            const goToWhatsApp = function () {
                if (redirected) {
                    return;
                }
                redirected = true;
                window.location.href = `https://wa.me/2290194776256?text=${encodeURIComponent(whatsappMessage)}`;
            };

            if (typeof window.gtag === 'function') {
                window.gtag('event', 'contact_form_submit', {
                    page_path: window.location.pathname,
                    transport_type: 'beacon',
                    event_callback: goToWhatsApp,
                    event_timeout: 1200
                });
                window.setTimeout(goToWhatsApp, 1500);
            } else {
                window.setTimeout(goToWhatsApp, 450);
            }
        });
    </script>
"""

# ------------------------------------------------------------------ avis Google (affichés en HTML, sans widget)
# Recopiés MOT POUR MOT depuis la fiche Google. Pour ajouter un avis : une ligne de plus dans REVIEWS.
# Un avis dont le texte est vide n'est pas affiché (on n'invente rien).
# AUCUNE donnée structurée AggregateRating / Review pour ces avis (interdit par Google pour ses propres avis).
REVIEWS_SOURCE = "Avis Google · novembre 2026"
REVIEWS = [
    dict(name="Tania G.", stars=5, text="Je suis très satisfait du travail réalisé par DEKS NEXA pour la création de mon site web. Le design est moderne, la navigation est fluide et le résultat est vraiment professionnel. Merci pour votre sérieux !"),
    dict(name="Audrey H.", stars=5, text="J'ai fait appel à DEKS NEXA pour développer une application adaptée à mon activité. Je suis satisfait du résultat, l'application répond bien à mes besoins et le suivi a été appréciable. Merci pour le travail !"),
    dict(name="Odette D.", stars=5, text="J'avais besoin d'une solution pour mieux organiser et gérer certaines activités de mon entreprise. DEKS NEXA a su proposer une solution adaptée à mes besoins. Je suis satisfait de cette collaboration."),
    dict(name="Géraud", stars=5, text="Une équipe dynamique, professionnelle et à l'écoute. DEKS NEXA prend le temps de comprendre les besoins du client avant de proposer une solution. Très bonne collaboration du début à la fin."),
    dict(name="Seho", stars=5, text="Ce que j'apprécie particulièrement chez DEKS NEXA, c'est le suivi après la livraison. L'équipe reste disponible pour répondre aux questions et apporter les ajustements nécessaires. Un accompagnement sérieux et rassurant."),
    dict(name="K. S.", stars=5, text="Très bonne expérience avec DEKS NEXA. L'équipe a su comprendre mes besoins et développer une solution informatique adaptée à mon activité. Le travail est professionnel et le résultat correspond à mes attentes. Je recommande vivement."),
    dict(name="Edmond F.", stars=5, text="C'était une belle expérience de collaborer avec vous sur mon projet. Merci à vous"),
]
REVIEWS_URL = "https://maps.app.goo.gl/rzvPmQ1cR6AUEbaQ9"  # Google Business Profile link
