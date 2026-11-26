# Génère les 5 pages du site Deks Nexa avec le système « éditorial tech ».
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = os.path.dirname(os.path.abspath(__file__))
SPRITE = io.open(os.path.join(SCRATCH, "sprite.svg"), encoding="utf-8").read()

FONTS = "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap"
WA_NUM = "2290194776256"
WA_URL = "https://wa.me/2290194776256?text=Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20parler%20de%20mon%20projet."

def icon(d, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return ('<svg%s viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="%s"/></svg>') % (c, d)

ARROW = icon("M5 12h14M13 6l6 6-6 6", "dn-arrow")
UP = icon("M12 19V5M6 11l6-6 6 6")
BELL = icon("M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 0 1-3.4 0")
HOME = icon("M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z")
SEARCH = icon("M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.35-4.35")
BAG = icon("M6 7h12l1 14H5L6 7zM9 7a3 3 0 0 1 6 0")
USER = icon("M20 21a8 8 0 0 0-16 0M12 13a5 5 0 1 0 0-10 5 5 0 0 0 0 10z")
USERPLUS = icon("M16 21a6 6 0 0 0-12 0M10 13a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM19 8v6M22 11h-6")
LOCK = icon("M7 11V8a5 5 0 0 1 10 0v3M5 11h14v10H5z")
MAIL = icon("M3 6h18v12H3zM3 7l9 6 9-6")
SPARK = icon("M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9zM19 16l.7 1.8 1.8.7-1.8.7L19 21l-.7-1.8-1.8-.7 1.8-.7z")
PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
         'aria-hidden="true" focusable="false"><rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/></svg>')
FB = icon("M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z")
IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
      'stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="2" y="2" width="20" height="20" rx="5"/>'
      '<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37zM17.5 6.5h.01"/></svg>')
WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>')
MENU = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
        'aria-hidden="true" focusable="false"><path class="dn-l1" d="M4 9h16"/><path class="dn-l2" d="M4 15h16"/></svg>')

def wa_btn(label="Parler de votre projet", url=WA_URL):
    return '<a class="dn-btn dn-btn-wa" href="%s" target="_blank" rel="noopener">%s%s</a>' % (url, WA, label)

def outline_btn(label, href):
    return '<a class="dn-btn dn-btn-outline" href="%s">%s%s</a>' % (href, label, ARROW)

def serif(text, word):
    assert word in text, (text, word)
    return text.replace(word, '<em class="dn-serif">%s</em>' % word, 1)

# ---------------------------------------------------------------- en-tête
def head(title, keywords, description):
    return f"""<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="{keywords}" name="keywords">
    <meta content="{description}" name="description">
    <meta name="theme-color" content="#0A0A0A">
    <script>document.documentElement.classList.add("js");</script>

    <!-- Favicon -->
    <link href="image/deks-logo-transparent.png" rel="icon">

    <!-- Polices : Geist, Geist Mono, Instrument Serif (chargement non bloquant) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style" href="{FONTS}">
    <link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="{FONTS}"></noscript>

    <!-- Feuille de style unique -->
    <link href="css/deks.css" rel="stylesheet">
</head>
"""

NAV_ITEMS = [("index.html", "Accueil"), ("about.html", "À propos"), ("service.html", "Solutions")]

def nav(active):
    links = []
    for href, label in NAV_ITEMS:
        if href == active:
            links.append('<li><a class="dn-nav-link is-active" href="%s" aria-current="page">%s</a></li>' % (href, label))
        else:
            links.append('<li><a class="dn-nav-link" href="%s">%s</a></li>' % (href, label))
    return f"""<body id="top">
    <a class="dn-skip" href="#contenu">Aller au contenu</a>

    <header class="dn-nav">
        <div class="dn-nav-inner">
            <a href="index.html" class="dn-nav-brand">
                <picture><source srcset="image/deks-logo-transparent.webp" type="image/webp"><img src="image/deks-logo-transparent.png" alt="Logo Deks" width="827" height="306"></picture>
            </a>
            <nav class="dn-nav-menu" id="dn-menu" aria-label="Navigation principale">
                <ul class="dn-nav-links">
                    {''.join(links)}
                </ul>
                <a href="contact.html" class="dn-nav-cta">Discutez du projet{ARROW}</a>
            </nav>
            <button class="dn-menu-btn" type="button" aria-expanded="false" aria-controls="dn-menu" aria-label="Ouvrir le menu">{MENU}</button>
        </div>
    </header>

    <main id="contenu">
"""

FOOTER = f"""    </main>

    <footer class="dn-footer">
        <div class="dn-container">
            <div class="dn-g12 dn-footer-grid">
                <div class="dn-footer-about">
                    <p class="dn-footer-brand">Deks Nexa</p>
                    <p>Le digital qui fait avancer votre entreprise : logiciels métiers, automatisations, applications et plateformes sur mesure.</p>
                </div>
                <nav class="dn-footer-nav" aria-label="Pied de page">
                    <p class="dn-tag dn-footer-title">Navigation</p>
                    <ul><li><a href="index.html">Accueil</a></li><li><a href="service.html">Solutions</a></li><li><a href="projets.html">Réalisations</a></li><li><a href="about.html">À propos</a></li><li><a href="contact.html">Contact</a></li></ul>
                </nav>
                <div class="dn-footer-contact">
                    <p class="dn-tag dn-footer-title">Contact</p>
                    <ul><li><a href="https://wa.me/{WA_NUM}" target="_blank" rel="noopener">WhatsApp : +229 01 94 77 62 56</a></li><li><a href="mailto:deksinformatique@gmail.com">deksinformatique@gmail.com</a></li></ul>
                </div>
                <div class="dn-footer-social">
                    <p class="dn-tag dn-footer-title">Réseaux</p>
                    <ul><li><a href="https://www.facebook.com/deksnexa" target="_blank" rel="noopener">{FB}Facebook</a></li><li><a href="https://www.instagram.com/deksnexa/" target="_blank" rel="noopener">{IG}Instagram</a></li><li><a href="https://www.linkedin.com/company/deksnexa/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li><li><a href="https://www.tiktok.com/@deksnexa" target="_blank" rel="noopener noreferrer">TikTok</a></li></ul>
                </div>
            </div>
            <div class="dn-footer-bottom"><span>© Deks Nexa. Tous droits réservés.</span></div>
        </div>
    </footer>

    <a class="dn-top" href="#top" aria-label="Revenir en haut">{UP}</a>
"""

def scripts(extra_inline="", home=False):
    s = ""
    if extra_inline:
        s += extra_inline
    s += '    <script src="js/main.js" defer></script>\n'
    s += '    <script src="js/deks-ui.js" defer></script>\n'
    if home:
        s += '    <script src="js/accueil.js" defer></script>\n'
    s += "</body>\n\n</html>\n"
    return s

def section_head(label, title, word, intro=None, tag="h2", cls="dn-title"):
    out = '<div class="dn-head dn-reveal">\n<p class="dn-label">%s</p>\n<%s class="%s">%s</%s>\n' % (label, tag, cls, serif(title, word), tag)
    if intro:
        out += '<p class="dn-intro">%s</p>\n' % intro
    return out + "</div>\n"

def page_hero(label, title, word, intro, button=True):
    actions = '<div class="dn-actions">%s</div>\n' % wa_btn() if button else ""
    return ('<section class="dn-page-hero dn-dark">\n<div class="dn-container">\n<p class="dn-label">%s</p>\n'
            '<h1>%s</h1>\n<p class="dn-intro">%s</p>\n%s</div>\n</section>\n') % (label, serif(title, word), intro, actions)

CTA = f"""<section class="dn-section dn-dark dn-cta" id="contact">
<div class="dn-container dn-reveal">
<p class="dn-label">Contact</p>
<h2 class="dn-cta-title">{serif("Parlons de votre projet.", "votre projet")}</h2>
<p class="dn-intro">Expliquez-nous votre besoin en quelques mots. Nous vous répondons sur WhatsApp.</p>
<div class="dn-actions">{wa_btn()}{outline_btn("Remplir le formulaire", "contact.html")}</div>
<p class="dn-cta-note">Réponse sur WhatsApp, en général dans la journée</p>
</div>
</section>
"""

# ---------------------------------------------------------------- contenus
SOLUTIONS = [
    dict(id="logiciel-metier", tag="Site web moderne · Logiciel métier · ERP &amp; CRM",
         problem="Nos clients, commandes et stocks sont éparpillés dans plusieurs fichiers.",
         title="Tout centraliser et piloter dans un seul outil.",
         desc="Nous réunissons vos clients, ventes, stocks, factures et validations dans un logiciel clair, pensé pour votre métier, avec des tableaux de bord pour suivre l'activité.",
         checks=["Site web moderne pour présenter votre activité", "Gestion des clients, des ventes et de la facturation", "Suivi des stocks et des opérations", "Demandes et validations avec traçabilité", "Tableaux de bord et indicateurs clés", "Accès sécurisés selon les rôles"],
         wa="Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20centraliser%20mes%20clients%2C%20commandes%20et%20stocks%20dans%20un%20seul%20outil."),
    dict(id="automatisation", tag="Automatisation",
         problem="Les validations et les relances se perdent dans les messages.",
         title="Automatiser validations, relances et notifications.",
         desc="Nous connectons les étapes clés de votre activité pour que chaque demande suive un circuit clair, sans tâches répétitives.",
         checks=["Relances automatiques", "Notifications internes", "Validation et affectation des demandes", "Génération de documents et de factures", "Suivi des actions en temps réel"],
         wa="Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20automatiser%20des%20validations%2C%20relances%20ou%20notifications."),
    dict(id="integration-api", tag="Intégration API",
         problem="Nous saisissons les mêmes informations dans plusieurs outils.",
         title="Connecter vos outils entre eux.",
         desc="Nous faisons circuler les données entre vos logiciels, vos paiements et vos services externes : une seule saisie, partout à jour.",
         checks=["Connexion aux solutions de paiement", "Synchronisation entre applications", "APIs REST pour vos services", "Automatisation des échanges de données", "Supervision et maintenance des intégrations"],
         wa="Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20connecter%20mes%20outils%20pour%20%C3%A9viter%20la%20double%20saisie."),
    dict(id="application-mobile", tag="Application mobile",
         problem="Nos équipes terrain remontent les informations sur papier ou par téléphone.",
         title="Une application mobile pour le terrain.",
         desc="Nous créons des applications Android et iOS connectées à vos données, simples à prendre en main pour les équipes terrain.",
         checks=["Collecte de données sur le terrain", "Notifications et alertes métier", "Synchronisation avec le système central", "Accès sécurisé par profil", "Écrans simples pour les équipes"],
         wa="Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20une%20application%20mobile%20pour%20mes%20%C3%A9quipes%20terrain."),
    dict(id="plateforme-saas", tag="Plateforme SaaS",
         problem="Nous voulons proposer notre service en ligne, avec des comptes clients.",
         title="Lancer votre plateforme en ligne.",
         desc="Nous développons des plateformes prêtes à accueillir vos utilisateurs, vos abonnements et vos processus métier.",
         checks=["Comptes et rôles utilisateurs", "Espaces clients et administration", "Abonnements ou paiements intégrés", "Suivi des usages et indicateurs", "Architecture pensée pour évoluer"],
         wa="Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20lancer%20une%20plateforme%20en%20ligne."),
    dict(id="maintenance", tag="Maintenance",
         problem="Notre outil actuel est lent, fragile ou dépassé.",
         title="Moderniser sans tout recommencer.",
         desc="Nous reprenons l'outil que vos équipes utilisent déjà pour le rendre plus stable, plus clair et plus sûr, étape par étape.",
         checks=["Audit de l'existant", "Corrections et stabilisation", "Améliorations progressives", "Sécurisation des accès et des données", "Maintenance et évolutions continues"],
         wa="Bonjour%20Deks%20Nexa%2C%20je%20souhaite%20moderniser%20une%20application%20existante."),
]

STEPS = [
    ("Écouter", "Nous clarifions vos processus, vos contraintes et vos priorités."),
    ("Proposer", "Une solution claire, découpée en étapes, avec un devis détaillé."),
    ("Construire", "Nous développons par étapes et vous montrons l'avancement régulièrement."),
    ("Livrer et suivre", "Mise en service, prise en main par vos équipes, maintenance et évolutions."),
]

WHY = [
    ("Sur mesure", "Chaque outil part de vos processus réels, pas d'un modèle tout fait."),
    ("IA intégrée", "L'intelligence artificielle là où elle fait vraiment gagner du temps."),
    ("Simple à utiliser", "Des écrans clairs, pensés pour que vos équipes l'adoptent vite."),
    ("Accompagnement", "Mise en service, prise en main, maintenance et évolutions."),
]

TECH = [("laravel", "Laravel"), ("php", "PHP"), ("flutter", "Flutter"), ("mysql", "MySQL"), ("react", "React"),
        ("python", "Python"), ("figma", "Figma"), ("flask", "Flask"), ("django", "Django"), ("n8n", "n8n")]

PROJECTS = [
    dict(tag="Plateforme web", name="Innov-Deks", icon="SPARK", mark="", status="Livré", done=True,
         desc="Notre vitrine d'innovation : c'est sur Innov-Deks que nous lançons nos nouvelles solutions.",
         points=["La preuve concrète de notre capacité à innover", "Le lieu de lancement de nos nouvelles solutions", "Conçue, développée et mise en ligne par Deks Nexa"]),
    dict(tag="Application mobile", name="Life mood App", icon="PHONE", mark=" is-mobile", status="En cours", done=False,
         desc="Une application mobile conçue et développée par Deks Nexa, actuellement en cours de développement.",
         points=["Pensée pour Android et iOS", "De la conception à la publication sur les stores", "Bientôt disponible sur Play Store et App Store"]),
]

def rows():
    out = '<ol class="dn-rows">\n'
    for i, s in enumerate(SOLUTIONS, 1):
        out += ('<li class="dn-row dn-reveal">\n<span class="dn-row-num" aria-hidden="true">%02d</span>\n'
                '<div>\n<p class="dn-tag">%s</p>\n<h3>%s</h3>\n<p class="dn-row-problem">%s</p>\n</div>\n'
                '<a class="dn-row-go" href="service.html#%s" aria-label="Voir le détail : %s">%s</a>\n</li>\n') % (
                    i, s["tag"], s["title"], s["problem"], s["id"], s["title"], ARROW)
    return out + "</ol>\n"

def offers():
    out = '<ol class="dn-offers">\n'
    for i, s in enumerate(SOLUTIONS, 1):
        checks = "".join("<li>%s</li>" % c for c in s["checks"])
        out += ('<li class="dn-offer dn-g12 dn-reveal" id="%s">\n'
                '<div class="dn-offer-side"><span class="dn-offer-num" aria-hidden="true">%02d</span><p class="dn-tag">%s</p></div>\n'
                '<div class="dn-offer-main">\n<h3>%s</h3>\n<p class="dn-offer-problem">%s</p>\n<p>%s</p>\n</div>\n'
                '<div class="dn-offer-aside">\n<ul class="dn-checks">%s</ul>\n'
                '<a class="dn-link" href="https://wa.me/%s?text=%s" target="_blank" rel="noopener">Parler de ce besoin %s</a>\n</div>\n</li>\n') % (
                    s["id"], i, s["tag"], s["title"], s["problem"], s["desc"], checks, WA_NUM, s["wa"], ARROW)
    return out + "</ol>\n"

def steps():
    out = '<ol class="dn-steps dn-reveal">\n'
    for i, (t, p) in enumerate(STEPS, 1):
        out += '<li class="dn-step"><span class="dn-step-dot" aria-hidden="true"></span><span class="dn-step-num">%02d</span><h3>%s</h3><p>%s</p></li>\n' % (i, t, p)
    return out + "</ol>\n"

def tech():
    items = "".join('<li><svg aria-hidden="true" focusable="false"><use href="#si-%s"/></svg><span>%s</span></li>' % (k, n) for k, n in TECH)
    return ('<div class="dn-tech dn-reveal">\n<p class="dn-label dn-tech-title">Technologies utilisées</p>\n'
            '<div class="dn-marquee">\n<ul class="dn-marquee-track">%s</ul>\n<ul class="dn-marquee-track" aria-hidden="true">%s</ul>\n</div>\n</div>\n') % (items, items)

def projects():
    out = '<div class="dn-projects">\n'
    for p in PROJECTS:
        points = "".join("<li>%s</li>" % x for x in p["points"])
        out += ('<article class="dn-project dn-reveal">\n<div class="dn-project-top"><span class="dn-project-mark%s" aria-hidden="true">%s</span>'
                '<span class="dn-status%s">%s</span></div>\n'
                '<p class="dn-tag">%s</p>\n<h3>%s</h3>\n<p class="dn-project-desc">%s</p>\n<ul class="dn-checks">%s</ul>\n</article>\n') % (
                    p["mark"], globals()[p["icon"]], " is-done" if p["done"] else "", p["status"], p["tag"], p["name"], p["desc"], points)
    return out + "</div>\n"

