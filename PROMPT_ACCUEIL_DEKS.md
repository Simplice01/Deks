# Prompt : moderniser l'accueil et la section « Cas d'usage »

> À coller dans Claude, dans Visual Studio Code, avec le dossier `site web` ouvert.
> Complète `PROMPT_SITE_DEKS.md` : l'identité visuelle et les règles de ce fichier s'appliquent toujours.

---

Tu travailles sur `index.html` du site DEKS. Ne modifie que **deux zones** :

1. le **héros d'accueil** (bloc `hero-header`, vers les lignes 69 à 113) ;
2. la section **« Des problèmes concrets que nous pouvons résoudre »** (bloc `id="actualites"`, vers les lignes 452 à 531).

Ne touche pas aux autres sections. Objectif : un accueil **moderne, vivant et « numérique »**, avec de petites animations discrètes qui donnent l'impression d'un vrai logiciel en marche. Ce doit rester premium et sobre, sans effet gadget.

## Règles générales

- Garde l'identité de `PROMPT_SITE_DEKS.md` : noir `#0A0A0A` / blanc, **un seul accent bleu `#075FF7`**, General Sans + Satoshi, boutons « bulle » (coin bas-gauche droit), bordures 1 px, pas d'ombre lourde, pas d'emoji.
- Pour les touches numériques, utilise une police monospace système : `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, en petite taille (12–13 px), pour les étiquettes, numéros et lignes de code.
- **Aucune bibliothèque** : CSS et JavaScript natifs. Le CSS va dans `css/deks.css` (blocs commentés `/* === ACCUEIL === */` et `/* === CAS D'USAGE === */`), le JS dans un nouveau fichier `js/accueil.js` chargé avec `defer`.
- Dans ces deux zones, retire `animate.css` (`animated zoomIn`, `slideInLeft`…), `wow fadeInUp`, les classes Bootstrap `card`, `shadow`, `rounded-pill` et `bg-primary`.
- N'anime que `transform` et `opacity` (pas de `width`, `top`, `height` en boucle).
- **`prefers-reduced-motion: reduce`** : aucune animation, chaque élément s'affiche directement dans son état final.
- Les animations s'arrêtent quand la zone sort de l'écran (`IntersectionObserver`) ou quand l'onglet est caché (`visibilitychange`).
- Tous les visuels décoratifs portent `aria-hidden="true"`. Navigation au clavier et `:focus-visible` obligatoires.
- **Aucun contenu inventé** : pas de faux clients, pas de vrais chiffres de résultats. Les seuls nombres permis sont ceux de la maquette d'interface, signalée « Exemple d'interface ».

---

## 1. Héros d'accueil

### Fond (noir)

- Grille de petits points (environ tous les 28 px) dessinée sur un `<canvas>`. Les points respirent doucement (légère variation d'opacité).
- Une **lueur bleue** (`#075FF7`, très diffuse, opacité ≤ 0,25) suit la souris avec un léger retard (interpolation). Les points proches de la lueur s'éclairent un peu.
- Sur mobile ou sans souris, la lueur se déplace seule, lentement.
- `devicePixelRatio` plafonné à 2, moins de points sur mobile, redimensionnement géré.

### Colonne gauche (texte)

Entrée en cascade au chargement (fondu + montée de 12 px, 80 ms d'écart entre chaque élément) :

1. **Étiquette** en forme de pastille, bordure 1 px, avec un point bleu qui pulse :
   `● Le digital qui fait avancer votre entreprise`
2. **H1** avec un mot qui change :
   `Transformez vos processus en [logiciels fiables].`
   - Le mot entre crochets, en bleu, est remplacé toutes les 2,5 s, effet machine à écrire avec curseur clignotant `|` : « logiciels fiables » → « automatisations » → « tableaux de bord » → « applications mobiles ».
   - SEO et accessibilité : le HTML contient la phrase complète « Transformez vos processus en logiciels fiables. ». Le mot animé est `aria-hidden`, et un texte masqué visuellement (`.visually-hidden`) donne la phrase complète aux lecteurs d'écran.
   - Réserve la largeur du mot le plus long pour éviter tout décalage de mise en page.
3. **Phrase** (plus courte qu'aujourd'hui) :
   « DEKS conçoit des logiciels métiers, des automatisations et des tableaux de bord qui font gagner du temps à vos équipes et vous aident à piloter votre activité. »
4. **Deux boutons** :
   - « Parler de votre projet » → `https://wa.me/2290194776256` (`.btn-blanc`, petite icône WhatsApp en trait fin) ;
   - « Voir les cas d'usage » → `#cas-usage` (`.btn-contour`), avec une flèche qui glisse au survol.
5. **Bande de réassurance** sans chiffres, qui remplace « Depuis 2021 » et « projets réalisés » (à supprimer) : `✓ Sur mesure` · `✓ IA intégrée` · `✓ Suivi après livraison`. Coches en SVG, texte gris clair, petite taille.

### Colonne droite : maquette animée « Exemple d'interface »

Modernise l'actuel bloc `deks-product-visual` (« DEKS Operations ») pour en faire une **fenêtre de logiciel vivante** :

- **Barre de fenêtre** : 3 pastilles, adresse en monospace `deks.app/tableau-de-bord`, petite mention `Exemple d'interface` à droite.
- **Fond de fenêtre** : `#111`, bordure 1 px `#232323`, coins `20px 20px 20px 0`.
- **Contenu en grille** (chaque bloc apparaît en cascade) :
  - **Indicateur** : « Commandes du jour », compteur qui monte de 0 à une valeur fictive, et petite courbe (sparkline SVG) qui se dessine (`stroke-dashoffset`).
  - **Histogramme** : 6 barres qui montent (`transform: scaleY`), la dernière en bleu.
  - **Circuit** : `Demande → Validation → Notification`. L'étape active change toutes les 1,8 s et un point bleu circule sur la ligne de liaison.
  - **Modules** : pastilles `CRM` · `Stock` · `Facturation` · `API`, reliées par de fines lignes avec un petit paquet de données qui transite.
  - **Terminal** sur une ligne, qui se tape en boucle : `> synchronisation des clients… ok ✓`, avec curseur clignotant.
- **Notifications flottantes** (desktop uniquement), hors de la fenêtre, avec un flottement lent (±6 px, 6 s) :
  - un toast « Facture envoyée ✓ » qui glisse puis disparaît toutes les 6 à 8 s ;
  - une pastille « API connectée » avec un point vert discret.
- **Effet 3D léger** : la fenêtre s'incline (2 à 4° maximum, `perspective`) en suivant la souris. Désactivé au tactile et en mouvement réduit.

### Bas du héros

- **Indicateur de défilement** : petite souris en trait fin avec un point qui descend, ou le mot « Défiler » avec une ligne animée.
- **Bandeau de technologies** en défilement infini (CSS), logos en gris (`grayscale` et opacité 0,6, couleur au survol), bords estompés par un `mask-image`, pause au survol.
  Utilise uniquement les technologies réellement utilisées par DEKS. Les logos `image/log-django.svg`, `image/log-flask.svg`, `image/log-n8n.svg` existent. **Demande-moi de confirmer la liste** avant d'en ajouter d'autres.

### Mobile (< 768 px)

Texte au-dessus, maquette en dessous, simplifiée (indicateur et circuit seulement). Notifications flottantes masquées, pas d'effet 3D, boutons en pleine largeur. Le H1 reste l'élément principal à l'affichage (LCP), sans décalage de mise en page (CLS ≈ 0).

---

## 2. Section « Cas d'usage » (à refaire)

Renomme `id="actualites"` en `id="cas-usage"` et mets à jour le lien du héros. Supprime les images `affiche1.jpg` et `affiche2.jpg` de cette section : elles ne vont pas avec le reste. Fond noir ou blanc selon l'alternance des sections.

### En-tête

- Étiquette monospace : `// Cas d'usage`, avec le `//` en bleu.
- **H2** : « Ce qui vous ralentit aujourd'hui, nous pouvons le régler. »
  (variante possible : « Des problèmes concrets, des solutions sur mesure. »)
- Introduction : « Voici les situations que nous rencontrons le plus souvent. Reconnaissez-vous la vôtre ? »

### Structure de chaque carte : problème → solution

```
[ mini-visuel animé, environ 140 px de haut ]
01   LOGICIEL MÉTIER                          ← numéro bleu + étiquette, en monospace
« Nos données sont éparpillées dans plusieurs fichiers. »   ← le problème, en gris
Tout centraliser dans un seul outil.          ← H3 = la solution
Une phrase d'explication.
Parlons de votre cas →                        ← lien WhatsApp avec message prérempli
```

**Interaction signature** : quand la carte entre à l'écran (mobile) ou au survol (desktop), une **ligne bleue barre la phrase du problème** de gauche à droite (`scaleX` de 0 à 1). Le problème est « réglé », et la solution passe au premier plan.

Style des cartes : bordure 1 px `#E6E6E6` (ou `#232323` sur fond noir), coins `20px 20px 20px 0`, padding 28 px.
Au survol : bordure plus foncée, `translateY(-4px)`, la flèche du lien glisse, le mini-visuel accélère, et un halo discret suit le curseur dans la carte (gradient radial gris ou bleu, opacité ≤ 0,08).
Apparition en cascade au défilement (`IntersectionObserver`). Grille : 3 colonnes ≥ 992 px, 2 colonnes ≥ 640 px, 1 colonne en dessous.

### Les 6 cartes (textes améliorés)

| # | Étiquette | Problème (citation) | Solution (H3) | Explication | Mini-visuel animé |
|---|---|---|---|---|---|
| 01 | Logiciel métier | « Nos clients, commandes et stocks sont éparpillés dans plusieurs fichiers. » | Tout centraliser dans un seul outil. | Clients, commandes, stocks et factures réunis dans un logiciel pensé pour votre métier. Fini les ressaisies. | 3 icônes de fichiers qui glissent et fusionnent dans une seule fenêtre, dont les lignes de tableau se remplissent. |
| 02 | Automatisation | « Les validations et les relances se perdent dans les messages. » | Automatiser validations, relances et notifications. | Chaque demande suit un circuit clair : validée, relancée et notifiée au bon moment, sans y penser. | 3 nœuds `Demande → Validation → Notifié`, un point bleu circule et chaque nœud se coche. |
| 03 | Tableau de bord | « Nous ne savons pas, au jour le jour, comment va l'activité. » | Piloter l'activité d'un coup d'œil. | Ventes, clients, équipes, stocks : les indicateurs essentiels sur un seul écran, toujours à jour. | Barres qui montent et courbe qui se dessine. |
| 04 | Intégration API | « Nous saisissons les mêmes informations dans plusieurs outils. » | Connecter vos outils entre eux. | Paiements, CRM, formulaires et bases de données synchronisés automatiquement. Une seule saisie, partout à jour. | Blocs `Paiement` · `CRM` · `Base` reliés par des pointillés où transitent des paquets de données. |
| 05 | Application mobile | « Nos équipes terrain remontent les informations sur papier ou par téléphone. » | Une application mobile pour le terrain. | Collecte de données, suivi des interventions et notifications, synchronisés avec votre système central. | Silhouette de téléphone : une notification glisse et une icône de synchronisation tourne. |
| 06 | Maintenance | « Notre outil actuel est lent, fragile ou dépassé. » | Moderniser sans tout recommencer. | Audit, corrections, améliorations progressives et sécurisation de l'outil que vos équipes utilisent déjà. | Barre `v1 → v2` qui se remplit, et liste `Audit ✓` `Sécurité ✓` `Performance ✓` qui se coche. |

Tous les mini-visuels sont en **SVG inline ou en CSS** (pas d'image), en gris et noir avec une seule touche de bleu, `aria-hidden="true"`. Ils tournent lentement en boucle seulement quand ils sont visibles à l'écran.

### Liens « Parlons de votre cas → »

Chaque lien ouvre WhatsApp avec un message prérempli, encodé avec `encodeURIComponent` :
`https://wa.me/2290194776256?text=...`

1. « Bonjour DEKS, je souhaite centraliser mes clients, commandes et stocks dans un seul outil. »
2. « Bonjour DEKS, je souhaite automatiser des validations, relances ou notifications. »
3. « Bonjour DEKS, je souhaite un tableau de bord pour piloter mon activité. »
4. « Bonjour DEKS, je souhaite connecter mes outils pour éviter la double saisie. »
5. « Bonjour DEKS, je souhaite une application mobile pour mes équipes terrain. »
6. « Bonjour DEKS, je souhaite moderniser une application existante. »

Ajoute `target="_blank" rel="noopener"` et un `aria-label` explicite (par exemple « Parler de ce cas sur WhatsApp : logiciel métier »).

### Bas de section

Une ligne centrée :
« **Votre situation n'est pas dans la liste ?** Décrivez-la-nous, nous trouverons la bonne solution. »
Bouton `.btn-wa` : « Expliquer mon besoin sur WhatsApp ».

---

## 3. Vérifications avant de me montrer le résultat

- Rendu testé à 360, 768, 1024 et 1440 px, sans défilement horizontal.
- Mouvement réduit testé : tout est statique et lisible.
- Aucune erreur dans la console, et le JS est léger.
- Contrastes ≥ 4,5:1, navigation au clavier complète, un seul `H1` sur la page.
- Lighthouse mobile : pas de régression en performance, CLS ≈ 0.

## 4. Comment travailler

1. Lis `index.html`, `css/deks.css` et `js/main.js`, puis propose-moi un **plan court** : ce que tu modifies, ce que tu supprimes, ce que tu crées. **Attends ma validation.**
2. Fais d'abord le **héros**, montre-le-moi, puis la **section Cas d'usage**.
3. Ne supprime aucun fichier sans me le dire.
4. S'il manque une information, mets `[À COMPLÉTER]` et signale-le.
5. À la fin, liste tous les changements effectués.
