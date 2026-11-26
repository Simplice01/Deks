# Générateur du site Deks Nexa (version référencement). Lancer : python _src/build_site.py
# Le contenu (pages, services, métiers, avis) est dans content3.py. Ce dossier n'est jamais mis en ligne.
# Une seule source pour l'en-tête SEO, le menu, le pied de page et les données structurées.
import html
import io
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common3 import (ARROW, BAG, FB, IG, LOCK, MAIL, MENU, PHONE, SPARK, SPRITE, UP, USER, WA, PROJECTS, STEPS,
                    TECH, WHY, icon, serif)
import content3 as C
import content_pages as CP
import content_blog as BLOG

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # racine du site
SITE = "https://deksnexa.com"
VERSION = "20261126"
TODAY = "2026-11-25"
FONTS = "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap"
WA_NUM = "2290194776256"
EMAIL = "contact@deksnexa.com"
CHEVRON = icon("M6 9l6 6 6-6", "dn-chevron")


def esc(text):
    return html.escape(text, quote=True)


def wa_url(text):
    return f"https://wa.me/{WA_NUM}?text=" + urllib.parse.quote(text, safe="")


def wa_btn(text, label="Parler de votre projet"):
    return f'<a class="dn-btn dn-btn-wa" href="{wa_url(text)}" target="_blank" rel="noopener">{WA}{label}</a>'


def outline_btn(label, href):
    return f'<a class="dn-btn dn-btn-outline" href="{href}">{label}{ARROW}</a>'


DEFAULT_WA = "Bonjour Deks Nexa, je souhaite parler de mon projet."

# ------------------------------------------------------------------ données structurées
ORG_ID = SITE + "/#organisation"
ORGANIZATION = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": ORG_ID,
    "name": "Deks Nexa",
    "url": SITE + "/",
    "logo": SITE + "/image/logo-deks-nexa-carre.png",
    "image": SITE + "/image/logo-deks-nexa-carre.png",
    "description": "Logiciels de gestion sur mesure, sites web, applications mobiles, automatisations WhatsApp et IA, et référencement Google pour les entreprises au Bénin et en Afrique francophone.",
    "email": EMAIL,
    "telephone": "+229 01 94 77 62 56",
    "sameAs": ["https://www.facebook.com/deksnexa", "https://www.instagram.com/deksnexa/", "https://www.linkedin.com/company/deksnexa/", "https://www.tiktok.com/@deksnexa", "https://maps.app.goo.gl/rzvPmQ1cR6AUEbaQ9"],
    "areaServed": [
        {"@type": "Country", "name": "Bénin"},
        {"@type": "City", "name": "Cotonou"},
        {"@type": "Place", "name": "Afrique francophone"},
    ],
}
AREA = ORGANIZATION["areaServed"]


def graph(page):
    url = SITE + page["url"]
    nodes = [ORGANIZATION,
             {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Deks Nexa", "alternateName": "Deks",
              "inLanguage": "fr", "publisher": {"@id": ORG_ID}}]
    webpage = {"@type": "WebPage", "@id": url + "#page", "url": url, "name": page["title"],
               "description": page["description"], "inLanguage": "fr", "isPartOf": {"@id": SITE + "/#site"},
               "about": {"@id": ORG_ID}}
    crumbs = page.get("crumbs")
    if crumbs:
        webpage["breadcrumb"] = {"@id": url + "#ariane"}
        nodes.append({"@type": "BreadcrumbList", "@id": url + "#ariane", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": SITE + link}
            for i, (name, link) in enumerate(crumbs, 1)]})
    nodes.append(webpage)
    if page.get("service"):
        nodes.append({"@type": "Service", "@id": url + "#service", "name": page["service"],
                      "serviceType": page.get("service_type", page["service"]), "url": url,
                      "description": page["description"], "provider": {"@id": ORG_ID}, "areaServed": AREA})
    if page.get("article"):
        nodes.append({"@type": "BlogPosting", "@id": url + "#article", "headline": page["h1"],
                      "description": page["description"], "url": url, "inLanguage": "fr",
                      "datePublished": BLOG.PUBLISHED, "dateModified": BLOG.PUBLISHED,
                      "image": f"{SITE}/image/og/{page['og']}.jpg", "wordCount": page["words"],
                      "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID},
                      "mainEntityOfPage": {"@id": url + "#page"}, "isPartOf": {"@id": SITE + "/blog/#blog"}})
    if page.get("blog"):
        nodes.append({"@type": "Blog", "@id": url + "#blog", "url": url, "name": "Blog Deks Nexa", "inLanguage": "fr",
                      "publisher": {"@id": ORG_ID},
                      "blogPost": [{"@type": "BlogPosting", "headline": a["h1"], "url": SITE + a["url"],
                                    "datePublished": BLOG.PUBLISHED} for a in BLOG.ARTICLES]})
    if page.get("faq"):
        nodes.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in page["faq"]]})
    data = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, indent=2)
    return data.replace("</", "<\\/")


# ------------------------------------------------------------------ en-tête
def head(page):
    url = SITE + page["url"]
    title, desc = page["title"], page["description"]
    assert len(title) <= 60, (page["url"], len(title), title)
    assert 140 <= len(desc) <= 155, (page["url"], len(desc), desc)
    image = f"{SITE}/image/og/{page['og']}.jpg"
    robots = '\n    <meta name="robots" content="noindex">' if page.get("noindex") else ""
    canonical = "" if page.get("noindex") else f'\n    <link rel="canonical" href="{url}">'
    return f"""<!DOCTYPE html>
<html lang="fr">

<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8QFXV31GH5"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-8QFXV31GH5');</script>
    <meta charset="utf-8">
    <title>{esc(title)}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{esc(desc)}">{robots}{canonical}
    <meta property="og:type" content="{page.get('og_type', 'website')}">
    <meta property="og:locale" content="fr_FR">
    <meta property="og:site_name" content="Deks Nexa">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{image}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{esc(page['og_alt'])}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{image}">
    <meta name="theme-color" content="#0A0A0A">
    <script>document.documentElement.classList.add("js");</script>

    <link rel="icon" href="/favicon.ico?v=4" sizes="48x48">
    <link rel="icon" href="/favicon.svg?v=4" type="image/svg+xml">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png?v=4">
    <link rel="manifest" href="/site.webmanifest?v=4">

    <!-- Polices : Geist, Geist Mono, Instrument Serif (chargement non bloquant) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" as="style" href="{FONTS}">
    <link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="{FONTS}"></noscript>

    <link rel="stylesheet" href="/css/deks.css?v={VERSION}">

    <script type="application/ld+json">
{graph(page)}
    </script>
</head>
"""


# ------------------------------------------------------------------ menu
def sub_menu(key, label, items, all_link, active):
    links = "".join(f'<li><a href="{href}">{esc(name)}</a></li>' for name, href in items)
    if all_link:
        links += f'<li class="dn-sub-all"><a href="{all_link[1]}">{esc(all_link[0])}{ARROW}</a></li>'
    cls = "dn-nav-link dn-sub-btn" + (" is-active" if active == key else "")
    return (f'<li class="dn-has-sub"><button class="{cls}" type="button" aria-expanded="false" '
            f'aria-controls="dn-sub-{key}">{label}{CHEVRON}</button>'
            f'<div class="dn-sub" id="dn-sub-{key}"><ul>{links}</ul></div></li>')


def nav(active):
    def link(key, href, label):
        on = active == key
        return (f'<li><a class="dn-nav-link{" is-active" if on else ""}" href="{href}"'
                f'{" aria-current=\"page\"" if on else ""}>{label}</a></li>')
    items = (sub_menu("services", "Services", [(s["menu"], s["url"]) for s in C.SERVICES],
                      ("Toutes les solutions", "/service.html"), active)
             + sub_menu("metiers", "Métiers", [(m["menu"], m["url"]) for m in C.METIERS], None, active)
             + link("realisations", "/projets.html", "Réalisations")
             + link("blog", "/blog/", "Blog")
             + link("about", "/about.html", "À propos"))
    return f"""<body id="top">
    <a class="dn-skip" href="#contenu">Aller au contenu</a>

    <header class="dn-nav">
        <div class="dn-nav-inner">
            <a href="/" class="dn-nav-brand">
                <picture><source srcset="/image/deks-logo-transparent.webp" type="image/webp"><img src="/image/deks-logo-transparent.png" alt="Logo Deks Nexa" width="827" height="306"></picture>
            </a>
            <nav class="dn-nav-menu" id="dn-menu" aria-label="Navigation principale">
                <ul class="dn-nav-links">
                    {items}
                </ul>
                <a href="/contact.html" class="dn-nav-cta{' is-active' if active == 'contact' else ''}">Contact{ARROW}</a>
            </nav>
            <button class="dn-menu-btn" type="button" aria-expanded="false" aria-controls="dn-menu" aria-label="Ouvrir le menu">{MENU}</button>
        </div>
    </header>

    <main id="contenu">
"""


def footer(wa_text):
    services = "".join(f'<li><a href="{s["url"]}">{esc(s["menu"])}</a></li>' for s in C.SERVICES)
    metiers = "".join(f'<li><a href="{m["url"]}">{esc(m["menu"])}</a></li>' for m in C.METIERS)
    return f"""    </main>

    <footer class="dn-footer">
        <div class="dn-container">
            <div class="dn-g12 dn-footer-grid">
                <div class="dn-footer-about">
                    <p class="dn-footer-brand">Deks Nexa</p>
                    <p>Logiciels de gestion, sites web, applications et automatisations pour les entreprises de Cotonou, du Bénin et d'Afrique francophone.</p>
                    <ul class="dn-footer-contact-list">
                        <li><a href="https://wa.me/{WA_NUM}" target="_blank" rel="noopener">{WA}WhatsApp : +229 01 94 77 62 56</a></li>
                        <li><a href="mailto:{EMAIL}">{MAIL}{EMAIL}</a></li>
                        <li><a href="https://www.facebook.com/deksnexa" target="_blank" rel="noopener">{FB}Facebook</a></li>
                        <li><a href="https://www.instagram.com/deksnexa/" target="_blank" rel="noopener">{IG}Instagram</a></li>
                        <li><a href="https://www.linkedin.com/company/deksnexa/" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.32 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12ZM7.1 20.45H3.54V9H7.1v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg>LinkedIn</a></li>
                        <li><a href="https://www.tiktok.com/@deksnexa" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.33V2h-3.45v13.67a2.9 2.9 0 0 1-2.9 2.9 2.9 2.9 0 1 1 2.9-2.9c0-.22-.03-.43-.08-.63V11.5a6.36 6.36 0 1 0 3.53 5.7V10.2a8.25 8.25 0 0 0 4.83 1.56V8.32a4.82 4.82 0 0 1-1.06-.12Z"/></svg>TikTok</a></li>
                    </ul>
                </div>
                <nav class="dn-footer-col" aria-label="Services">
                    <p class="dn-tag dn-footer-title">Services</p>
                    <ul>{services}<li><a href="/service.html">Toutes les solutions</a></li></ul>
                </nav>
                <nav class="dn-footer-col" aria-label="Métiers">
                    <p class="dn-tag dn-footer-title">Solutions par métier</p>
                    <ul>{metiers}</ul>
                </nav>
                <nav class="dn-footer-col" aria-label="Deks Nexa">
                    <p class="dn-tag dn-footer-title">Deks Nexa</p>
                    <ul><li><a href="/">Accueil</a></li><li><a href="/projets.html">Réalisations</a></li><li><a href="/blog/">Blog</a></li><li><a href="/about.html">À propos</a></li><li><a href="/contact.html">Contact</a></li></ul>
                </nav>
            </div>
            <div class="dn-footer-bottom"><span>© Deks Nexa. Tous droits réservés.</span><span>Cotonou · Bénin · Afrique francophone</span></div>
        </div>
    </footer>

    <a class="dn-wa-float" href="{wa_url(wa_text)}" target="_blank" rel="noopener" aria-label="Écrire à Deks Nexa sur WhatsApp">{WA}<span>WhatsApp</span></a>
    <a class="dn-top" href="#top" aria-label="Revenir en haut">{UP}</a>
"""


def scripts(home=False, extra=""):
    out = extra
    out += f'    <script src="/js/main.js?v={VERSION}" defer></script>\n'
    out += f'    <script src="/js/deks-ui.js?v={VERSION}" defer></script>\n'
    out += '    <script src="/js/analytics.js" defer></script>\n'
    if home:
        out += f'    <script src="/js/accueil.js?v={VERSION}" defer></script>\n'
    return out + "</body>\n\n</html>\n"


# ------------------------------------------------------------------ blocs
def section_head(label, title, word, intro=None, tag="h2"):
    out = f'<div class="dn-head dn-reveal">\n<p class="dn-label">{label}</p>\n<{tag} class="dn-title">{serif(title, word)}</{tag}>\n'
    if intro:
        out += f'<p class="dn-intro">{intro}</p>\n'
    return out + "</div>\n"


def crumbs_html(crumbs):
    items = []
    for i, (name, link) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            items.append(f'<li><a href="{link}">{esc(name)}</a></li>')
    return f'<nav class="dn-crumbs" aria-label="Fil d\'Ariane"><ol>{"".join(items)}</ol></nav>\n'


def nbsp(text):
    """Typographie française : pas de « : » ni de « ? » en début de ligne."""
    return text.replace(" :", "&nbsp;:").replace(" ?", "&nbsp;?")


def page_hero(page, label, title, word, intro, buttons=True, second=None, meta=""):
    crumbs = crumbs_html(page["crumbs"]) if page.get("crumbs") else ""
    actions = f'<p class="dn-article-meta">{meta}</p>\n' if meta else ""
    if buttons:
        actions += '<div class="dn-actions">' + wa_btn(page["wa"]) + (outline_btn(*second) if second else "") + "</div>\n"
    return (f'<section class="dn-page-hero dn-dark">\n<div class="dn-container">\n{crumbs}<p class="dn-label">{label}</p>\n'
            f'<h1>{nbsp(serif(title, word))}</h1>\n<p class="dn-intro">{intro}</p>\n{actions}</div>\n</section>\n')


def cta(page):
    return f"""<section class="dn-section dn-dark dn-cta" id="contact">
<div class="dn-container dn-reveal">
<p class="dn-label">Contact</p>
<h2 class="dn-cta-title">{serif(page.get("cta_title", "Parlons de votre projet."), page.get("cta_word", "votre projet"))}</h2>
<p class="dn-intro">Expliquez-nous votre besoin en quelques mots. Nous vous répondons sur WhatsApp.</p>
<div class="dn-actions">{wa_btn(page["wa"])}{outline_btn("Remplir le formulaire", "/contact.html")}</div>
<p class="dn-cta-note">Réponse sur WhatsApp, en général dans la journée</p>
</div>
</section>
"""


def steps(items=STEPS):
    out = '<ol class="dn-steps dn-reveal">\n'
    for i, (t, p) in enumerate(items, 1):
        out += f'<li class="dn-step"><span class="dn-step-dot" aria-hidden="true"></span><span class="dn-step-num">{i:02d}</span><h3>{t}</h3><p>{p}</p></li>\n'
    return out + "</ol>\n"


def service_rows(items):
    out = '<ol class="dn-rows">\n'
    for i, s in enumerate(items, 1):
        out += (f'<li class="dn-row dn-reveal">\n<span class="dn-row-num" aria-hidden="true">{i:02d}</span>\n'
                f'<div>\n<p class="dn-tag">{s["tag"]}</p>\n<h3>{s["row_title"]}</h3>\n<p class="dn-row-problem">{s["problem"]}</p>\n</div>\n'
                f'<a class="dn-row-go" href="{s["url"]}" aria-label="{esc(s["menu"])} : voir la page">{ARROW}</a>\n</li>\n')
    return out + "</ol>\n"


def metier_grid():
    out = '<ul class="dn-metiers">\n'
    for m in C.METIERS:
        out += (f'<li class="dn-reveal"><a href="{m["url"]}"><span class="dn-tag">{m["tag"]}</span>'
                f'<strong>{esc(m["menu"])}</strong><span class="dn-metier-text">{m["teaser"]}</span>{ARROW}</a></li>\n')
    return out + "</ul>\n"


def tech():
    items = "".join(f'<li><svg aria-hidden="true" focusable="false"><use href="#si-{k}"/></svg><span>{n}</span></li>' for k, n in TECH)
    return ('<div class="dn-tech dn-reveal">\n<p class="dn-label dn-tech-title">Technologies utilisées</p>\n'
            f'<div class="dn-marquee">\n<ul class="dn-marquee-track">{items}</ul>\n<ul class="dn-marquee-track" aria-hidden="true">{items}</ul>\n</div>\n</div>\n')


def projects():
    out = '<div class="dn-projects">\n'
    for p in PROJECTS:
        points = "".join(f"<li>{x}</li>" for x in p["points"])
        mark = SPARK if p["icon"] == "SPARK" else PHONE
        out += (f'<article class="dn-project dn-reveal">\n<div class="dn-project-top"><span class="dn-project-mark{p["mark"]}" aria-hidden="true">{mark}</span>'
                f'<span class="dn-status{" is-done" if p["done"] else ""}">{p["status"]}</span></div>\n'
                f'<p class="dn-tag">{p["tag"]}</p>\n<h3>{p["name"]}</h3>\n<p class="dn-project-desc">{p["desc"]}</p>\n<ul class="dn-checks">{points}</ul>\n</article>\n')
    return out + "</div>\n"


def faq_html(items):
    out = '<div class="dn-faq">\n'
    for q, a in items:
        out += f'<details class="dn-faq-item dn-reveal"><summary><h3>{q}</h3>{CHEVRON}</summary><div class="dn-faq-answer"><p>{a}</p></div></details>\n'
    return out + "</div>\n"


def related(urls):
    pages = {p["url"]: p for p in C.SERVICES + C.METIERS}
    out = '<ol class="dn-rows dn-rows-related">\n'
    for i, url in enumerate(urls, 1):
        p = pages[url]
        out += (f'<li class="dn-row dn-reveal">\n<span class="dn-row-num" aria-hidden="true">{i:02d}</span>\n<div>\n'
                f'<p class="dn-tag">{p["tag"]}</p>\n<h3>{esc(p["h1"])}</h3>\n<p class="dn-row-problem">{p["teaser"]}</p>\n</div>\n'
                f'<a class="dn-row-go" href="{url}" aria-label="{esc(p["h1"])}">{ARROW}</a>\n</li>\n')
    return out + "</ol>\n"


STAR = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
        'd="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>')


def reviews_block():
    """Avis Google recopiés tels quels, en HTML statique. Aucune donnée structurée d'avis."""
    cards = ""
    for r in C.REVIEWS:
        if not r["text"].strip():
            continue  # texte non fourni : on n'affiche pas
        cards += (f'<li class="dn-review"><figure>'
                  f'<div class="dn-stars" role="img" aria-label="{r["stars"]} étoiles sur 5">{STAR * r["stars"]}</div>'
                  f'<blockquote><p>{html.escape(r["text"], quote=False)}</p></blockquote>'
                  f'<figcaption><strong>{html.escape(r["name"], quote=False)}</strong><span>{C.REVIEWS_SOURCE} <img class="dn-google-logo" src="/image/google-g.png" alt="Google" width="18" height="18"></span></figcaption>'
                  f'</figure></li>\n')
    if C.REVIEWS_URL:
        button = f'<a class="dn-btn dn-btn-outline" href="{esc(C.REVIEWS_URL)}" target="_blank" rel="noopener noreferrer">Voir tous les avis sur Google{ARROW}</a>'
    else:
        button = (f'<a class="dn-btn dn-btn-outline" href="#avis">Voir tous les avis sur Google{ARROW}</a>'
                  f'<p class="dn-reviews-note"><mark class="dn-todo">[À COMPLÉTER]</mark> lien Google Maps de la fiche</p>')
    return (f'<div class="dn-reviews" id="avis">\n'
            f'<div class="dn-subhead dn-reveal"><p class="dn-label">Avis clients</p>'
            f'<h2 class="dn-subtitle">Ce que disent <em class="dn-serif">nos clients</em>.</h2></div>\n'
            f'<div class="dn-carousel" data-carousel>\n'
            f'<ul class="dn-reviews-list" tabindex="0" aria-label="Avis clients">\n{cards}</ul>\n'
            f'<div class="dn-reviews-bar dn-reveal"><div class="dn-actions">{button}</div>'
            f'<div class="dn-carousel-nav"><button class="dn-carousel-btn" type="button" data-dir="-1" aria-label="Avis précédents">{ARROW}</button>'
            f'<button class="dn-carousel-btn" type="button" data-dir="1" aria-label="Avis suivants">{ARROW}</button></div></div>\n'
            f'</div>\n</div>\n')

# ------------------------------------------------------------------ page service / métier
def landing(p):
    hero = page_hero(p, p["label"], p["h1"], p["h1_word"], p["intro"],
                     second=("Voir nos réalisations", "/projets.html"))
    deliver = "".join(f'<li class="dn-feature dn-reveal"><h3>{t}</h3><p>{d}</p></li>\n' for t, d in p["deliver"])
    who = "".join(
        f'<li class="dn-feature dn-reveal"><h3>{f"<a href=\"{link}\">{t}</a>" if link else t}</h3><p>{d}</p></li>\n'
        for t, d, link in p["who"])
    body = hero
    body += ('<section class="dn-section">\n<div class="dn-container dn-g12 dn-split">\n'
             + section_head(p["problem_label"], p["problem_title"], p["problem_word"])
             + '<div class="dn-prose dn-reveal">\n' + "".join(f"<p>{x}</p>\n" for x in p["problem_text"]) + "</div>\n</div>\n</section>\n")
    body += ('<section class="dn-section dn-dark">\n<div class="dn-container">\n'
             + section_head("Ce que nous réalisons", p["deliver_title"], p["deliver_word"], p.get("deliver_intro"))
             + f'<ul class="dn-features dn-features-3">\n{deliver}</ul>\n</div>\n</section>\n')
    body += ('<section class="dn-section">\n<div class="dn-container">\n'
             + section_head("Comment ça se passe", p["steps_title"], p["steps_word"], p.get("steps_intro"))
             + steps(p["steps"]) + "</div>\n</section>\n")
    body += ('<section class="dn-section dn-dark">\n<div class="dn-container">\n'
             + section_head("Pour qui", p["who_title"], p["who_word"], p.get("who_intro"))
             + f'<ul class="dn-features">\n{who}</ul>\n'
             + ('<div class="dn-prose dn-prose-wide dn-reveal">' + "".join(f"<p>{x}</p>" for x in p["extra"]) + "</div>\n" if p.get("extra") else "")
             + "</div>\n</section>\n")
    body += ('<section class="dn-section" id="faq">\n<div class="dn-container">\n<div class="dn-g12 dn-split">\n'
             + section_head("Questions fréquentes", p["faq_title"], p["faq_word"])
             + faq_html(p["faq"]) + "</div>\n"
             + '<div class="dn-subhead dn-reveal"><p class="dn-label">À voir aussi</p><h2 class="dn-subtitle">Pages proches de votre besoin.</h2></div>\n'
             + related(p["related"]) + "</div>\n</section>\n")
    body += cta(p)
    return head(p) + nav(p["nav"]) + body + footer(p["wa"]) + scripts()


# ------------------------------------------------------------------ blog
def md(text):
    """Mini-format des articles : « ## » intertitre, « - » liste, sinon paragraphe."""
    out = ""
    for block in text.strip().split("\n\n"):
        lines = [x.strip() for x in block.strip().split("\n")]
        if lines[0].startswith("## "):
            out += f'<h2 id="{slug(lines[0][3:])}">{lines[0][3:]}</h2>\n'
        elif all(x.startswith("- ") for x in lines):
            out += "<ul>\n" + "".join(f"<li>{x[2:]}</li>\n" for x in lines) + "</ul>\n"
        else:
            out += f"<p>{' '.join(lines)}</p>\n"
    return out


def slug(text):
    import unicodedata
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def words(text):
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9’'-]+", re.sub(r"<[^>]+>", " ", html.unescape(text))))


def blog_rows(posts):
    out = '<ol class="dn-rows">\n'
    for i, a in enumerate(posts, 1):
        out += (f'<li class="dn-row dn-reveal">\n<span class="dn-row-num" aria-hidden="true">{i:02d}</span>\n<div>\n'
                f'<p class="dn-tag">{a["label"]}</p>\n<h3><a href="{a["url"]}">{esc(a["h1"])}</a></h3>\n'
                f'<p class="dn-row-problem">{a["description"]}</p>\n</div>\n'
                f'<a class="dn-row-go" href="{a["url"]}" aria-label="Lire l\'article : {esc(a["h1"])}">{ARROW}</a>\n</li>\n')
    return out + "</ol>\n"


def page_blog():
    p = BLOG.BLOG
    body = (page_hero(p, p["label"], p["h1"], p["h1_word"], p["intro"], second=("Voir nos services", "/service.html"))
            + '<section class="dn-section">\n<div class="dn-container">\n'
            + section_head("Articles", "À lire pour avancer sur votre projet.", "avancer",
                           "Des réponses claires aux questions que se posent les entreprises avant de se lancer.")
            + blog_rows(BLOG.ARTICLES) + "</div>\n</section>\n" + cta(p))
    return head(p) + nav("blog") + body + footer(p["wa"]) + scripts()


def page_article(p):
    minutes = max(1, round(p["words"] / 200))
    meta = f'Publié le {BLOG.PUBLISHED_FR} · {minutes} min de lecture'
    others = [a for a in BLOG.ARTICLES if a["url"] != p["url"]]
    body = (page_hero(p, "Blog · " + p["label"], p["h1"], p["h1_word"], p["intro"], buttons=False, meta=meta)
            + '<section class="dn-section">\n<div class="dn-container">\n'
            + f'<article class="dn-prose dn-article">\n{md(p["body"])}</article>\n'
            + '<div class="dn-subhead dn-reveal"><p class="dn-label">À voir aussi</p><h2 class="dn-subtitle">Nos services liés à cet article.</h2></div>\n'
            + related(p["related"])
            + '<div class="dn-subhead dn-reveal"><p class="dn-label">Sur le blog</p><h2 class="dn-subtitle">Autres articles.</h2></div>\n'
            + blog_rows(others) + "</div>\n</section>\n" + cta(p))
    return head(p) + nav("blog") + body + footer(p["wa"]) + scripts()


# ------------------------------------------------------------------ pages services, métiers et blog : préparation
def prepare():
    for s in C.SERVICES:
        extra = CP.SERVICE_PAGES.get(s["url"])
        if extra:
            s.update(extra)
            s.setdefault("ready", True)
            s.setdefault("nav", "services")
            s.setdefault("og", s["url"].strip("/"))
            s.setdefault("crumbs", [("Accueil", "/"), ("Services", "/service.html"), (s["menu"], s["url"])])
    for m in C.METIERS:
        extra = CP.METIER_PAGES.get(m["url"])
        if extra:
            m.update(extra)
            m.setdefault("ready", True)
            m.setdefault("nav", "metiers")
            m.setdefault("og", "solutions-" + m["url"].strip("/").split("/")[-1])
            m.setdefault("crumbs", [("Accueil", "/"), ("Solutions par métier", "/service.html#metiers"), (m["menu"], m["url"])])
    for s in C.SERVICES + C.METIERS:
        if s.get("ready"):
            s.setdefault("og_alt", s["h1"] + ", par Deks Nexa")
            s.setdefault("service", s["h1"].replace(" au Bénin", ""))
            s.setdefault("problem_label", "Le problème")
    BLOG.BLOG["blog"] = True
    for a in BLOG.ARTICLES:
        a.update(nav="blog", article=True, og_type="article", og_alt=a["h1"],
                 crumbs=[("Accueil", "/"), ("Blog", "/blog/"), (a["short"], a["url"])], words=words(md(a["body"])))


def og_specs():
    """Images de partage des pages générées ici (utilisé par og_images.py)."""
    prepare()
    specs = []
    for s in C.SERVICES + C.METIERS:
        if s.get("ready") and s["og"] != "logiciel-de-gestion-benin":
            specs.append((s["og"], s["label"], s["h1"].replace(" au Bénin", ""), s["h1_word"], s["teaser"].rstrip(".") + " · Bénin"))
    b = BLOG.BLOG
    specs.append((b["og"], "Blog", b["og_title"], b["og_word"], b["og_sub"]))
    for a in BLOG.ARTICLES:
        specs.append((a["og"], "Blog · " + a["label"], a["og_title"], a["og_word"], "Le blog Deks Nexa"))
    return specs


# ------------------------------------------------------------------ pages existantes
def page_index():
    p = C.HOME
    hero_visual = C.HERO_VISUAL.replace("{LOCK}", LOCK).replace("{MAIL}", MAIL)
    hero = f"""<section class="dn-hero dn-dark" id="accueil" aria-labelledby="dn-hero-title">
<canvas class="dn-hero-canvas" data-dots="off" aria-hidden="true"></canvas>
<div class="dn-hero-glow" aria-hidden="true"></div>
<div class="dn-container dn-g12 dn-hero-grid">
<div class="dn-hero-text">
<p class="dn-label">Logiciels sur mesure · Bénin</p>
<h1 class="dn-hero-title" id="dn-hero-title">Transformez vos processus en <em class="dn-serif">logiciels fiables</em></h1>
<p class="dn-intro">{p["intro"]}</p>
<div class="dn-actions">{wa_btn(p["wa"])}{outline_btn("Voir nos services", "#solutions")}</div>
<ul class="dn-assurance"><li>Sur mesure</li><li>IA intégrée</li><li>Suivi après livraison</li></ul>
</div>
{hero_visual}
</div>
</section>
"""
    solutions = ('<section class="dn-section" id="solutions">\n<div class="dn-container">\n'
                 + section_head("Services", "Ce qui vous ralentit aujourd'hui, nous pouvons le régler.", "régler",
                                "Six services, en commençant par les logiciels de gestion. Reconnaissez-vous votre besoin&nbsp;?")
                 + service_rows(C.SERVICES)
                 + f'<div class="dn-more dn-reveal">{outline_btn("Toutes les solutions en détail", "/service.html")}</div>\n'
                 + '<div class="dn-subhead dn-reveal"><p class="dn-label">Solutions par métier</p><h3 class="dn-subtitle">Votre secteur a ses habitudes. Nos outils aussi.</h3></div>\n'
                 + metier_grid() + "</div>\n</section>\n")
    methode = ('<section class="dn-section dn-dark" id="methode">\n<div class="dn-container">\n'
               + section_head("Méthode", "Une méthode simple, du besoin au logiciel en service.", "simple",
                              "Quatre étapes claires, avec vous à chaque moment du projet.")
               + steps() + tech() + "</div>\n</section>\n")
    realisations = ('<section class="dn-section" id="realisations">\n<div class="dn-container">\n<div class="dn-head-row">\n'
                    + section_head("Réalisations", "Des projets concrets, livrés ou en cours.", "concrets",
                                   "Quelques projets conçus et développés par Deks Nexa.")
                    + f'<a class="dn-link dn-reveal" href="/projets.html">Voir les réalisations {ARROW}</a>\n</div>\n'
                    + projects() + reviews_block() + "</div>\n</section>\n")
    body = SPRITE + "\n" + hero + solutions + methode + realisations + cta(p)
    return head(p) + nav("home") + body + footer(p["wa"]) + scripts(home=True)


def page_service():
    p = C.HUB
    offers = '<ol class="dn-offers">\n'
    for i, s in enumerate(C.SERVICES, 1):
        checks = "".join(f"<li>{c}</li>" for c in s["checks"])
        offers += (f'<li class="dn-offer dn-g12 dn-reveal" id="{s["anchor"]}">\n'
                   f'<div class="dn-offer-side"><span class="dn-offer-num" aria-hidden="true">{i:02d}</span><p class="dn-tag">{s["tag"]}</p></div>\n'
                   f'<div class="dn-offer-main">\n<h3><a href="{s["url"]}">{s["h1"]}</a></h3>\n<p class="dn-offer-problem">{s["problem"]}</p>\n<p>{s["summary"]}</p>\n'
                   f'<a class="dn-link" href="{s["url"]}">Découvrir ce service {ARROW}</a>\n</div>\n'
                   f'<div class="dn-offer-aside">\n<ul class="dn-checks">{checks}</ul>\n'
                   f'<a class="dn-link" href="{wa_url(s["wa"])}" target="_blank" rel="noopener">Parler de ce besoin {ARROW}</a>\n</div>\n</li>\n')
    offers += "</ol>\n"
    extras = "".join(f'<li class="dn-feature dn-reveal"><h3>{t}</h3><p>{d}</p></li>\n' for t, d in C.HUB_EXTRAS)
    body = (page_hero(p, "Solutions", "Des logiciels conçus pour vos métiers.", "vos métiers", p["intro"])
            + '<section class="dn-section" id="solutions">\n<div class="dn-container">\n'
            + section_head("6 services", "Choisissez le besoin qui vous ressemble.", "ressemble",
                           "Chaque service part d'un problème concret et aboutit à un outil simple à utiliser.")
            + offers + "</div>\n</section>\n"
            + '<section class="dn-section dn-dark">\n<div class="dn-container">\n'
            + section_head("Et aussi", "Ce que nous faisons en complément.", "en complément")
            + f'<ul class="dn-features dn-features-3">\n{extras}</ul>\n</div>\n</section>\n'
            + '<section class="dn-section" id="metiers">\n<div class="dn-container">\n'
            + section_head("Solutions par métier", "Votre secteur a ses habitudes. Nos outils aussi.", "Nos outils aussi")
            + metier_grid() + "</div>\n</section>\n" + cta(p))
    return head(p) + nav("services") + body + footer(p["wa"]) + scripts()


def page_about():
    p = C.ABOUT
    features = '<ul class="dn-features">\n' + "".join(
        f'<li class="dn-feature dn-reveal"><h3>{t}</h3><p>{d}</p></li>\n' for t, d in WHY) + "</ul>\n"
    body = (page_hero(p, "À propos", "Le digital qui fait avancer votre entreprise.", "avancer", p["intro"])
            + '<section class="dn-section">\n<div class="dn-container dn-g12 dn-split">\n'
            + section_head("Qui nous sommes", "Des solutions utiles, pas des outils décoratifs.", "utiles")
            + '<div class="dn-prose dn-reveal">\n' + "".join(f"<p>{x}</p>\n" for x in C.ABOUT_TEXT) + "</div>\n</div>\n</section>\n"
            + '<section class="dn-section dn-dark">\n<div class="dn-container">\n'
            + section_head("Pourquoi Deks Nexa", "Quatre engagements pour des logiciels qui durent.", "durent")
            + features + "</div>\n</section>\n"
            + '<section class="dn-section" id="methode">\n<div class="dn-container">\n'
            + section_head("Méthode", "Une méthode simple, du besoin au logiciel en service.", "simple",
                           "Quatre étapes claires, avec vous à chaque moment du projet.")
            + steps() + "</div>\n</section>\n" + cta(p))
    return head(p) + nav("about") + body + footer(p["wa"]) + scripts()


def page_projets():
    p = C.PROJETS
    body = (page_hero(p, "Réalisations", "Nos réalisations.", "réalisations", p["intro"])
            + '<section class="dn-section">\n<div class="dn-container">\n'
            + section_head("Projets", "Plateformes web et applications mobiles.", "applications mobiles")
            + projects() + "</div>\n</section>\n" + cta(p))
    return head(p) + nav("realisations") + body + footer(p["wa"]) + scripts()


def page_contact():
    p = C.CONTACT
    form = C.CONTACT_FORM.replace("{WA}", WA).replace("{EMAIL}", EMAIL).replace("{WA_LINK}", wa_btn(p["wa"], "Écrire sur WhatsApp"))
    body = page_hero(p, "Contact", "Parlez-nous de votre projet.", "votre projet", p["intro"], buttons=False) + form
    return head(p) + nav("contact") + body + footer(p["wa"]) + scripts(extra=C.CONTACT_SCRIPT)


def page_404():
    p = C.NOT_FOUND
    body = (page_hero(p, "Erreur 404", "Cette page est introuvable.", "introuvable", p["intro"],
                      second=("Retour à l'accueil", "/"))
            + '<section class="dn-section">\n<div class="dn-container">\n'
            + section_head("Pages utiles", "Par où continuer ?", "continuer")
            + service_rows(C.SERVICES) + "</div>\n</section>\n")
    return head(p) + nav("") + body + footer(p["wa"]) + scripts()


# ------------------------------------------------------------------ écriture
def write(rel, text):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text.replace("\r\n", "\n").replace("\n", "\r\n"))


def main_words(text):
    main = re.search(r"<main id=\"contenu\">(.*)</main>", text, re.S).group(1)
    main = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", main, flags=re.S)
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9’'-]+", re.sub(r"<[^>]+>", " ", html.unescape(main))))


if __name__ == "__main__":
    prepare()
    built = []
    pages = [("index.html", page_index, C.HOME), ("service.html", page_service, C.HUB),
             ("about.html", page_about, C.ABOUT), ("projets.html", page_projets, C.PROJETS),
             ("contact.html", page_contact, C.CONTACT), ("404.html", page_404, C.NOT_FOUND)]
    for s in C.SERVICES + C.METIERS:
        if s.get("ready"):
            pages.append((s["url"].strip("/") + "/index.html", lambda s=s: landing(s), s))
    pages.append(("blog/index.html", page_blog, BLOG.BLOG))
    for a in BLOG.ARTICLES:
        assert a["words"] >= 800, (a["url"], a["words"])
        pages.append((a["url"].strip("/") + "/index.html", lambda a=a: page_article(a), a))
    for rel, fn, meta in pages:
        text = fn()
        write(rel, text)
        built.append(meta)
        extra = f"  article {meta['words']}" if meta.get("article") else ""
        print(f"{rel:64} title {len(meta['title']):2}  desc {len(meta['description'])}  mots {main_words(text)}{extra}")
    # Plan du site : uniquement les pages publiées et indexables
    urls = "".join(f"  <url><loc>{SITE}{m['url']}</loc><lastmod>{TODAY}</lastmod></url>\n" for m in built if not m.get("noindex"))
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print("sitemap.xml :", urls.count("<url>"), "pages")
