# Prompt : améliorer le site officiel DEKS

> À coller dans Claude, dans Visual Studio Code, avec le dossier `site web` ouvert.

---

Tu travailles sur le site officiel de **DEKS**, dans ce dossier. **Améliore le site existant**, ne le reconstruis pas de zéro : garde les pages (`index.html`, `about.html`, `service.html`, `projets.html`, `contact.html`), le chatbot et ce qui fonctionne, et transforme le tout en un site **premium, épuré, rapide et bien référencé**.

## 1. Qui est DEKS

DEKS est une entreprise de **solutions digitales intelligentes**. Elle accompagne les entreprises, commerces, ONG, écoles, structures de santé et indépendants avec 5 services :

1. **Sites web** : vitrines, institutionnels, boutiques en ligne, pages de vente, refontes.
2. **Logiciels de gestion sur mesure** : stock, ventes, facturation, paiements, gestion scolaire, rendez-vous, tableaux de bord.
3. **IA & automatisation** : assistants intelligents (WhatsApp, site), chatbots, automatisation des tâches répétitives.
4. **Référencement & présence en ligne** : SEO, fiche Google, contenus optimisés, réseaux sociaux.
5. **Motion design & contenus** : vidéos animées avec voix off, visuels et carrousels pour les réseaux et la publicité.

L'IA est présentée comme intégrée aux solutions, là où elle fait gagner du temps.

**Promesse** : « Le digital qui fait avancer votre entreprise. »

**Ton** : professionnel, clair, direct, chaleureux. Phrases courtes. Vouvoiement. Pas de jargon inutile, pas de superlatifs creux.

## 2. Identité visuelle attendue

- **Noir et blanc prioritaires** (95 % du site) :
  - noir `#0A0A0A`, blanc `#FFFFFF`, gris clair `#F4F4F2` ;
  - texte `#3A3A3A`, texte secondaire `#6B6B6B`, lignes `#E6E6E6` (fond clair) et `#232323` (fond noir).
- **Un seul accent : le bleu du logo `#075FF7`**, en petites touches (un mot clé, un numéro, une icône, un détail). Jamais en grands aplats.
- **Vert WhatsApp `#25D366`** réservé uniquement aux boutons WhatsApp.
- **Typographie** :
  - titres en **General Sans** (600/700), texte en **Satoshi** (400/500), chargées depuis Fontshare : `https://api.fontshare.com/v2/css?f[]=general-sans@500,600,700&f[]=satoshi@400,500,700&display=swap` ;
  - secours : `system-ui, sans-serif` ;
  - grands titres serrés (`letter-spacing: -0.03em`, `line-height: ~1.05`).
- **Rythme** : les sections **alternent strictement fond noir / fond blanc** jusqu'en bas de chaque page. Beaucoup d'espace (`padding` vertical ~120 px desktop), une idée par section, peu d'éléments par écran.
- **Détails premium** : bordures fines de 1 px, aucune ombre lourde, aucun dégradé coloré, aucun emoji dans l'interface, icônes en trait fin (SVG inline).
- **Accueil** : fond noir avec une **grille de petits points** (environ tous les 28 px) qui respirent doucement. Une lueur **bleue** se déplace lentement sur la grille et suit la souris. Animation légère en CSS ou `<canvas>`, sans bibliothèque, désactivée si `prefers-reduced-motion`.
- **Logo** : `image/deks-logo-transparent.png` (blanc) sur fond noir ; version sombre sur fond blanc.

### Forme des boutons (signature DEKS, obligatoire partout)

Forme « bulle de discussion » : **trois coins arrondis, le coin bas-gauche droit**.

```css
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:10px;
  font-weight:600;font-size:16px;line-height:1;
  padding:18px 26px;
  border-radius:18px 18px 18px 0;   /* coin bas-gauche droit */
  border:1.5px solid transparent;
  transition:transform .2s ease, background-color .2s ease, color .2s ease;
}
.btn:hover{transform:translateY(-2px)}
.btn:focus-visible{outline:3px solid #075FF7;outline-offset:3px}

.btn-noir{background:#0A0A0A;color:#fff}            /* principal sur fond blanc */
.btn-blanc{background:#fff;color:#0A0A0A}           /* principal sur fond noir */
.btn-contour{border-color:#0A0A0A;color:#0A0A0A;background:transparent}  /* secondaire */
.fond-noir .btn-contour{border-color:#4A4A4A;color:#fff}
.btn-wa{background:#25D366;color:#04210F}           /* WhatsApp uniquement */
```

- Petits boutons : `border-radius:12px 12px 12px 0`.
- Cartes, badges et puces numérotées reprennent la même logique d'angle (coin bas-gauche droit), sans excès.
- Sur mobile (< 560 px) : boutons en pleine largeur.

## 3. Rôle de chaque section (page d'accueil)

1. **Accueil** (noir) : dire en 5 secondes qui est DEKS et ce qu'il fait. Titre + une phrase + 2 boutons (« Parler de votre projet » → WhatsApp, « Nos services »).
2. **Services** (blanc) : les 5 services en cartes courtes (titre + une ligne), chacune menant à sa section ou page détaillée, plus une carte « Un autre besoin ? ».
3. **Pourquoi DEKS** (noir) : 4 différences courtes (sur mesure, IA intégrée, simple à utiliser, accompagnement).
4. **Réalisations** (blanc) : uniquement de **vrais** projets DEKS (par ex. Innov-Deks, Kidi). Si aucun n'est prêt, prévois la section en commentaire et ne l'affiche pas.
5. **Méthode** (noir ou blanc selon l'alternance) : 4 étapes (écoute, proposition, réalisation, livraison et suivi).
6. **Questions fréquentes** : 4 à 6 questions courtes (prix, délais, travail à distance, maintenance).
7. **Contact** : WhatsApp en action principale, e-mail en secondaire.

Parcours voulu : comprendre → trouver son besoin → faire confiance → lever les doutes → écrire sur WhatsApp.

**L'accueil reste léger** (peu de texte). Le contenu détaillé va dans `service.html` : une section complète par service (titre H2 avec mot-clé, 2 paragraphes, liste « Ce que nous réalisons », « Pour qui », bouton). Idéalement, à terme, une page par service.

## 4. Corrections obligatoires sur le site actuel

- **Supprimer les faux témoignages et les faux chiffres** de `js/main.js` (« Entreprise Alpha », « Groupe Horizon », « 35+ clients », « 96 % »…). Ne jamais inventer de clients, d'avis ou de statistiques.
- **Numéro WhatsApp** : partout `2290194776256` (liens `https://wa.me/2290194776256`), affiché `+229 01 94 77 62 56`. Corriger le formulaire de contact (`wa.me/22994776256` est faux) et le pied de page.
- **Ne jamais afficher la ville** (Cotonou, Abomey-Calavi), **l'année de création** (« Depuis 2021 », « 5 ans d'expérience ») ni l'équipe.
- **Réseaux sociaux** : garder uniquement les comptes DEKS (page Facebook DEKS, Instagram `deks_solutions`). Retirer les comptes personnels.
- Corriger les fautes (« playstor/Appstor » → « Play Store / App Store ») et mettre à jour le `README.md`.
- Retirer l'écran « Loading… ».

## 5. Référencement (priorité)

- Un `<title>` unique par page (≤ 60 caractères, mot-clé + DEKS) et une `meta description` unique (≤ 155 caractères).
- Une seule balise `H1` par page, une hiérarchie `H2`/`H3` logique, des mots-clés naturels : « création de site web », « logiciel de gestion », « intelligence artificielle », « automatisation », « référencement Google », « motion design ».
- Balises Open Graph (`og:title`, `og:description`, `og:image` 1200×630) et `link rel="canonical"`.
- Données structurées JSON-LD : `Organization` (nom, logo, téléphone, e-mail, `sameAs`), `Service` pour chaque service, `FAQPage` pour les questions.
- Ajouter `sitemap.xml` et `robots.txt`.
- `alt` descriptif sur toutes les images, liens internes entre l'accueil et les services.
- `lang="fr"` sur toutes les pages.

## 6. Performance et qualité

- Objectif : **PageSpeed mobile ≥ 90**.
- Supprimer progressivement jQuery et les bibliothèques d'animation inutiles (wow, owl, waypoints…) en les remplaçant par du CSS et un peu de JS natif.
- Une seule feuille de style principale avec des variables CSS (`:root`). Supprimer `css1/` et les fichiers non utilisés (images de modèle « team », « testimonial », « portfolio », `circuit-board.jpg` de 14 Mo).
- Images en WebP, dimensionnées, `loading="lazy"` sous la ligne de flottaison.
- Responsive impeccable de 360 px à 1440 px, sans défilement horizontal.
- Accessibilité : contrastes ≥ 4.5:1, vrais `<button>`/`<a>`, `aria-label` sur les icônes seules, navigation au clavier.

## 7. Comment travailler

1. Commence par analyser le dossier et propose-moi un **plan court** (fichiers touchés, ce qui est supprimé, ce qui est gardé). Attends ma validation.
2. Travaille **page par page**, en commençant par `index.html`, et montre-moi le résultat avant de passer à la suivante.
3. Ne supprime aucun fichier sans me le dire.
4. Ne mets **aucun contenu inventé** : là où une information manque (prix, projets, chiffres), mets `[À COMPLÉTER]` et signale-le.
5. À la fin de chaque étape, liste ce que tu as changé.
