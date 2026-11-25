# Images de partage 1200x630 aux couleurs Deks Nexa (Open Graph / Twitter).
import os
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent
OUT = SITE / "image" / "og"
OUT.mkdir(parents=True, exist_ok=True)
FONTS = HERE / "fonts"

FACES = {
    ("Geist", "normal"): "gyByhwUxId8gMEwcGFU.woff2",
    ("Geist Mono", "normal"): "or3nQ6H-1_WfwkMZI_qYFrcdmg.woff2",
    ("Instrument Serif", "italic"): "jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7M.woff2",
}

IMAGES = [
    ("accueil", "Logiciels sur mesure · Bénin", "Logiciels de gestion et sites web", "sites web", "pour les entreprises de Cotonou et du Bénin"),
    ("solutions", "Services", "Des logiciels conçus pour vos métiers", "vos métiers", "Gestion, sites web, applications, WhatsApp et IA, Google"),
    ("a-propos", "À propos", "Le digital qui fait avancer votre entreprise", "avancer", "Deks Nexa, partenaire technique sur le long terme"),
    ("realisations", "Réalisations", "Des projets concrets, livrés ou en cours", "concrets", "Plateformes web et applications mobiles"),
    ("contact", "Contact", "Parlons de votre projet", "votre projet", "Réponse sur WhatsApp : +229 01 94 77 62 56"),
    ("logiciel-de-gestion-benin", "Logiciel de gestion", "Logiciel de gestion sur mesure au Bénin", "sur mesure", "Clients, ventes, factures, stocks et tableaux de bord"),
]
sys.path.insert(0, str(HERE))
import build_site  # noqa: E402  (pages services, métiers et blog)
IMAGES += build_site.og_specs()


def face_css():
    css = ""
    for (family, style), name in FACES.items():
        url = (FONTS / name).as_uri()
        weight = "100 900" if family == "Geist" else "400 500" if family == "Geist Mono" else "400"
        css += f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};src:url('{url}') format('woff2');}}\n"
    return css


def page(label, title, word, subtitle):
    logo = (SITE / "image" / "deks-logo-transparent.png").as_uri()
    title_html = title.replace(word, f"<em>{word}</em>", 1)
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
{face_css()}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1200px;height:630px}}
body{{position:relative;overflow:hidden;background:#0A0A0A;color:#fff;font-family:'Geist',sans-serif;padding:64px 72px}}
.glow{{position:absolute;right:-260px;top:-300px;width:900px;height:900px;border-radius:50%;background:radial-gradient(closest-side,rgba(6,95,247,.32),rgba(6,95,247,.08) 55%,transparent)}}
.line{{position:absolute;left:72px;right:72px;bottom:120px;height:1px;background:#262626}}
img{{position:relative;height:52px;width:auto}}
.label{{position:relative;display:flex;align-items:center;gap:14px;margin-top:64px;color:#5B95FF;font-size:20px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}}
.label i{{width:16px;height:16px;background:linear-gradient(rgba(91,149,255,.6),rgba(91,149,255,.6)) 0 0/12px 12px no-repeat,linear-gradient(rgba(91,149,255,.6),rgba(91,149,255,.6)) 4px 4px/12px 12px no-repeat}}
h1{{position:relative;max-width:980px;margin-top:22px;font-size:68px;font-weight:600;line-height:1.04;letter-spacing:-.035em}}
h1 em{{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;letter-spacing:-.01em}}
.bar{{position:relative;width:64px;height:5px;margin-top:26px;background:linear-gradient(90deg,#5B95FF 0 54px,transparent 54px 59px,#5B95FF 59px)}}
.sub{{position:absolute;left:72px;bottom:56px;color:#C9CBCF;font-size:24px}}
.url{{position:absolute;right:72px;bottom:58px;color:#9A9DA3;font-family:'Geist Mono',monospace;font-size:20px}}
</style></head><body><div class="glow"></div><div class="line"></div>
<img src="{logo}" alt="">
<p class="label"><i></i>{label}</p>
<h1>{title_html}</h1>
<div class="bar"></div>
<p class="sub">{subtitle}</p><p class="url">deksnexa.com</p>
</body></html>"""


only = set(sys.argv[1:])
with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    ctx = browser.new_context(viewport={"width": 1200, "height": 630})
    tab = ctx.new_page()
    for slug, label, title, word, subtitle in IMAGES:
        if only and slug not in only:
            continue
        tmp = HERE / f"og_{slug}.html"
        tmp.write_text(page(label, title, word, subtitle), encoding="utf-8")
        tab.goto(tmp.as_uri())
        tab.evaluate("document.fonts.ready")
        tab.wait_for_timeout(200)
        target = OUT / f"{slug}.jpg"
        tab.screenshot(path=str(target), type="jpeg", quality=84)
        print(slug, target.stat().st_size // 1024, "Ko")
    browser.close()
