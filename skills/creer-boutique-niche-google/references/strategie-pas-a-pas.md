# La Méthode Kraken — stratégie étape par étape

**Rôle de ce document.** C'est la roadmap opérationnelle du coach-associé (`mission-coach-associe.md`) : la séquence complète pour lancer une boutique SEO/SEA à la manière d'Enzo Honoré, reconstruite le 2026-08-08 à partir de la relecture intégrale des 66 contenus du corpus. Chaque étape renvoie aux sources (`source_id`) et à la porte de décision correspondante du skill. Les seuils sont des repères enseignés (`ENSEIGNE_A_VERIFIER` par défaut) ou des décisions projet, jamais des règles officielles Google.

**Vue d'ensemble (la « muse »)** : niche mesurée → étude concurrentielle → architecture SEO → domaine (idéalement expiré) → boutique riche 200+ produits → conformité GMC → tracking → Google Ads (Shopping « charognard » → tROAS) → SEO continu (contenu + netlinking) → email + SAV + retargeting → scaling par paliers → multiplication horizontale. Le parc observé du formateur (`docs/parc-sites-enzo-honore.md`) montre le résultat : des dizaines de boutiques « type de produit », dupliquées par pays.

---

## Phase 1 — Trouver et mesurer la niche (porte 1)

**1.1 Choisir la famille de niche selon le niveau** (`231587893`, `231663658`)
- Débutant : un **type de produit dans un univers thématisé** (ex. porte-vélo bébé) — blog possible + un seul type de fournisseur.
- Intermédiaire : niche type de produit à nombreuses catégories. Équipe expérimentée : grande niche thématisée.
- Sans idée : parcourir les menus des généralistes (Amazon, AliExpress, Leroy Merlin, Decathlon…) et tester les mots-clés un par un.

**1.2 Miner et mesurer** (`231588620`, `hhPBbZZ7qHQ`)
- Ahrefs Keywords Explorer → Matching terms → **filtre KD 0–2** pour les futures catégories (le mot-clé principal peut être plus dur). Volume : **> 1 000** pour les têtes de catégorie, **> 150** pour la longue traîne ; sous ~300, on arrête de créer des sous-catégories.
- Variante SEMrush : miner les mots-clés organiques des géants (KD ≤ 30-35, intentions commerciale/transactionnelle, descendre loin dans les pages — un petit mot-clé révèle souvent une niche entière).
- Vérifier la saisonnalité (Google Trends) et la variante singulier/pluriel/accent la plus recherchée.

**1.3 Filtres économiques immédiats** (`234186329`, `231588620`, `246208721`)
- **CPC cible ~0,25–0,30 €** ; **ratio prix moyen ÷ CPC ≥ 100, viser 150–200**. Un produit à 12–15 € avec CPC 0,40–0,50 € tue la niche. Prix moyen : relevé à la louche sur Google Shopping + concurrents.
- Vérifier sur AliExpress que chaque catégorie a des produits sourçables ; **≥ 200 produits de qualité trouvables** chez les fournisseurs (< 100 → abandonner ; ~50 toléré sur niche très simple).

**1.4 Éviter les six erreurs** (`231587930`)
Intention informationnelle (volume qui ne rapporte rien), mots-clés de marque (KD 0 trompeur + contrefaçon), catalogue fournisseur trop pauvre, vêtements (10–20 % de retours, tailles chinoises), produits complexes à sourcer/livrer (batteries, lames : ≥ 23 jours par train — sauf si on sait les maîtriser : barrière à l'entrée), niches montrées en formation (brûlées).

**1.5 Verdict SERP** (`231588620`, `hhPBbZZ7qHQ`)
Que des généralistes sans spécialiste de la niche (Amazon top 3 = bon signe) → niche validée : devenir LE spécialiste. Garder **3–4 niches candidates** avant d'en choisir une (`231588530`).

## Phase 2 — Étude concurrentielle profonde (porte 1, obligatoire)

Jamais optionnelle : la sortie de la phase 1 alimente automatiquement cette phase (`mission-coach-associe.md`). Sources : `231663690`, `231588620`, `232117816` + protocole Hakim.

1. **Trouver la grappe** : taper les mots-clés dans Google → premier concurrent dropship → Ahrefs Site Explorer → « Top 10 compétiteurs organiques » → dérouler toute la grappe. Boucler : chaque nouveau mot-clé découvert → nouveaux concurrents.
2. **Par concurrent** : mots-clés positionnés et meilleures pages (SEMrush/Ahrefs), DR et backlinks, catalogue (profondeur, structure, prix), metrics Brand Search si Shopify, marketing (canaux, angle, offre, réassurance), persona (à qui il parle, quel ton).
3. **Récolter** : ajouter au mind map les mots-clés qu'il ranke et qu'on a ratés ; noter ses catégories gagnantes à recréer ; les sites d'affiliation de la niche = mine de sujets de blog, pas des concurrents.
4. **Conclure** : forces/faiblesses, et le **différenciant** que nous pouvons construire (« vache pourpre », `231587882`) — l'analyse sert à trouver l'espace vide, pas à imiter (« toutes les niches lancées en copiant des shops de formation se sont fait éclater », `231663822`).
5. Sortie : un profil par concurrent + synthèse d'angle, versionnés (router vers `competitor-profiling`).

## Phase 3 — Architecture SEO et domaine (porte 3)

**3.1 Architecture en silos avant le site** (`231663822`, `234180398`, `246208721`)
- Mind map : racine = mot-clé principal ; chaque mot-clé KD 0–2 validé (volume, CPC, produits sourçables) = une catégorie ; regrouper en parentes (validées par leur propre volume) ; menu principal **5–6 catégories parentes**.
- Les termes transverses (taille, âge, LED…) = étiquettes/attributs ou pages dédiées, **jamais** deux catégories aux mêmes produits (duplicate). Synonymes de fait (étoile/galaxie/projection) = une seule catégorie qui traite tous les termes.
- Google Sheet de pilotage : par collection → volume, CPC, prix moyen, marge, décision « pub oui/non » (une collection à CPC prohibitif mais KD faible s'importe pour le SEO et s'exclut des pubs).
- Lancement : **~20–30 collections** sur le potentiel total, 5–15 produits chacune (multiples de 4 pour la grille).

**3.2 Domaine** (`231663659`, `231663658`)
- Chercher un **domaine expiré** (outil gratuit type ExpiredDomains) : .com/.fr, backlinks réels propres (vérifier sur Ahrefs : pas de spam), ancienneté, historique compatible (Wayback Machine), nom brandable. ~300 € avec backlinks « vaut toujours le coup » ; sinon domaine neuf stylé + investissement direct en netlinking. Statut : préférence d'auteur assumée contre le discours officiel Google (`ENSEIGNE_A_VERIFIER`).
- **Mettre les catégories en ligne dès que possible**, même 3 mois avant le lancement : le temps d'indexation est un actif.

## Phase 4 — Construire la boutique (porte 4)

**4.1 Catalogue** (`231588530`, `232117442`, `232117523`, `234333489`)
- **200 produits minimum au lancement** (100 = trop peu ; 700–800 = rentable plus vite mais brûle du budget). On ne cherche jamais le « winner » : 10–20 produits par sous-catégorie, **la data Google désigne le best-seller**.
- Fiche produit : ≥ 250 mots (2 blocs), mot-clé de la sous-catégorie dans le titre et en gras, titre « pour le robot » d'abord, structure AIDA, photos propres (pas de modèles incohérents avec la cible), ~350 mots pour les fiches à booster.
- Catégorie : best-sellers en premier (c'est la page à ranker), description SEO **800–1 200 mots** en bas (accordéon autorisé), meta title/description/URL/alt soignés (priorité aux collections : elles rankent mieux que les produits, `237446074`).
- Maillage interne en silos complets (`l-XUJ9NTN40`) : home → mères → filles chaînées en boucle → produits (~4 liens/produit).

**4.2 Technique** (`232118785`, `232119122`)
- PageSpeed **≥ 50 mobile / ≥ 90 desktop**, images WebP compressées, max 2 polices, lazyload, CDN, scripts tiers en footer, pas de méga-menu sur grande niche, QA mobile réelle sur téléphone.

**4.3 Routine d'intégration continue** (`232117816`, `232117915`, `306109499`)
- Ajouts **quotidiens** (pas en batch) : ≥ 20 produits/mois ; nouvelle catégorie = 10 produits d'un coup, une nouvelle catégorie tous les 1–2 mois — c'est le moteur du scaling Shopping (ouvrir des requêtes plutôt que monter les enchères).
- Déléguer avec un process écrit + contrôle qualité (conformité produit incluse — jamais publier sans vérification normes/prises/notices). Version IA : 1 produit parfait → ~15 itérations → agent vérificateur → batch.

## Phase 5 — Conformité, GMC et tracking (porte 5)

**5.1 Audit anti-misrepresentation avant tout** (`239965951`, `240313004`, `262936735`)
- Cohérence absolue partout (site = CGV = FAQ = fiche = checkout = GMC) : délais (ex. 24–48 h + 8–15 j ouvrés), retours 14 jours, frais, moyens de paiement affichés = réels, téléphone + email au footer, zéro 404/lorem ipsum (y compris les pages légales du checkout Shopify), pas de faux stocks/compteurs/avis, pas de « soldes » hors période, claims santé masqués pendant l'examen. Astuce : faire comparer les pages politiques par une IA.
- Stratégie d'examen : état **`GMC_READY`** sobre (voir `store-states-gmc-growth.md`) — moins il y a de marketing pendant la review, mieux c'est ; réintroduire ensuite la couche `GROWTH_MARKETING` documentée et conforme.

**5.2 Merchant Center via CSS** (`239791167`)
- Compte Ads en mode expert (devise/fuseau irréversibles, code promo de lancement, 2FA). MC via **CSS privé** (~−20 % de CPC en Europe, `OFFICIEL_ACTUEL` côté mécanisme CSS) — n'ouvrir le compte que **site 100 % propre** : l'examen commence dès la création. Puis **gel du site ~8 jours** (robot à J+2, humain vers J+7/8). 2e refus = blocage : procéder par élimination, jamais griller un examen.

**5.3 Flux et tracking** (`240313004`, `240359870`, `249915990`)
- Flux via app dédiée (Simprosys : plan payant sinon la synchro s'arrête ; ID produit unique par variante ; jamais en doublon avec le canal Google natif). Livraison/retours du MC recopiés du site.
- Conversions : **une seule action principale « Achat »**, valeur dynamique (défaut = panier moyen), comptage « une par clic », attribution data-driven ; add-to-cart/checkout en **secondaire** (l'erreur n°1 des comptes audités est le double comptage). Vérifier le tag avant tout lancement. Bannière RGPD + consent mode (sinon audiences de remarketing vides).
- Custom labels : par collection et par **ROAS break-even** produit (TVA + frais CB + ~10 % frais fixes, arrondi au palier supérieur) — préparés dès maintenant, exploités en phase 8.

## Phase 6 — Lancement Google Ads (porte 6)

**Campagnes du jour 1** (`240591206`) : Shopping standard + Search branding. Remarketing : créé mais il ne dépensera que quand l'audience existera (≥ 500 personnes).

- **Shopping « charognard »** : CPC manuel (milieu de fourchette du planificateur, ex. 0,75 € ; cohérence budget/CPC : 30 €/j → CPC 0,16–0,25 €), budget **50 €/j minimum (idéal 100)**, géo France+Belgique+Suisse en **« Présence » uniquement**, mobile/tablette **−40 %** au départ, audiences en observation, refuser deux fois la bascule PMax. Objectif unique de la phase : **15 conversions en ~30 jours** au moindre coût — pas la rentabilité.
- **Search branding** : 10 €/j, mots-clés marque en **exact + expression, jamais large**, RSA sobres (3-4 titres dont marque épinglée, composant promotion, 4 liens annexes), CPC plafonné puis tROAS ~500 % ; CTR attendu 30–70 %, < 10 % = fuite hors marque. Jamais « maximiser les clics ». Décocher le réseau Display.
- Ne pas toucher au budget tant que non rentable ; surveiller quotidiennement pendant le charognard.

## Phase 7 — Optimiser jusqu'au tROAS (porte 7)

**Cycle hebdomadaire** (`245994245`, `245994758`) — jamais plus d'une fois par semaine, « Google est un diesel » :
1. Taux d'impression perdu (budget) → ajuster les enchères.
2. Appareils → ajuster (ex. mobile −30 %, PC +15 %) + auditer le site mobile.
3. Groupes de produits triés par coût → baisser ce qui dépense sans vendre, monter ce qui transforme (« faire à la main le travail du tROAS »).
4. Termes de recherche → exclure les évidences tout de suite (hors-catalogue, informationnel, spécialiste imbattable) ; attendre 150–200 € de data pour les ambigus ; marques généralistes : tester avant d'exclure.
5. Produits : exclure après 1–2× le prix de vente dépensé sans conversion — mais **jamais un produit qui a converti**, même à mauvais ROAS (l'objectif reste les 15 conversions).

**Bascule tROAS** (`246485074`, `246532995`) : à 15 conversions → tROAS volontairement atteignable (ex. 75 %), stop aux optimisations manuelles ; puis montée par paliers (125 → 150 → 175 → 200 %) chaque fois que le budget est tapé. Mécanique à connaître : tROAS ↑ ⇒ CPC ↓ ⇒ diffusion ↓. Si les 15 conversions n'arrivent pas : repli PMax (toujours avec target, brand exclue, applications exclues).

**~J+21 : remarketing** (`249143021`) : display dynamique avec flux MC (10 €/j, maximiser la valeur sans tROAS au début, **décocher « ciblage optimisé »** — l'erreur des 80 % de comptes audités, exclure les acheteurs) + Demand Gen (10 €/j, mêmes règles). Côté Meta (`233283052`, `233282981`, `246203665`) : retargeting catalogue ~5–10 €/j dès que le pixel a ~7 jours de data — sans remise avant 7 jours, avec code promo au-delà. Jamais d'acquisition froide Meta au lancement.

**Stratégies de portefeuille** (`244603899`) : tROAS + **cap CPC max** — obligatoire sur 100 % des campagnes de marque, au cas par cas ailleurs (calibrer le cap via le rapport termes de recherche trié par CPC).

**CRO tirée de la data Ads** (`262936735`) : fiches les plus cliquées sans conversion → retravailler (photos, FAQ-objections, guide des tailles) ; produits à forte dépense sans conversion = signal de sourcing ; panier moyen : frais de port payants (2,90–4,90 € + assurance ~9,90 €) offerts dès un seuil juste au-dessus du panier moyen, upsells.

## Phase 8 — SEO continu : contenu, netlinking, avis (porte 7, chantier parallèle dès le lancement)

**8.1 Contenu** (`234333510`, `234333543`, `234333583`, `234333561`, `43kJQkuviKY`)
- Ratios selon la niche : thématisée difficile → 1 intentionniste / 2 informatifs ; type de produit → 4 / 1 ; débutant → toutes les catégories d'abord, puis informatif. Plancher : ~3 contenus/mois ; cadence blog visée 2–3 articles/semaine, batchés et programmés.
- Briefs : catégorie 1 000–1 300 mots (SEOQuantum/1.fr pour la sémantique, questions Ahrefs en H2, titres tous les 300 mots, < 5 % plagiat) ; article 1 400–1 800 mots (listicle vs question selon la SERP, longues traînes en H2, 8 mots-clés, un lien interne + un lien source scientifique, conclusion incitative). Demander l'**indexation GSC immédiatement** après publication.
- Trouver les sujets : questions Ahrefs KD 0 (vérifier les DR réels de la SERP), meilleures pages des concurrents à DR proche, relecture de ses propres articles ; monétiser : encart produit, popup email, jeu concours evergreen (`234333580`).

**8.2 Pilotage Search Console** (à 2–5 mois, `234333499`)
Requêtes émergentes → identifier la page (produit ou catégorie) → booster les **pré-rankées** (~position 30) : description complète + produits + netlinking. Recopier les catégories gagnantes des concurrents à DR inférieur. Cadence minimum vitale : **2 catégories travaillées tous les 4 mois**.

**8.3 Netlinking** (`234333582`, `234333584`, `234333596`)
4 premiers mois : liens vers la page d'accueil (pendant que le contenu travaille) → puis cycles de 4 mois sur 2 catégories choisies via GSC, accueil en continu. Montée en gamme : massif peu cher au début → moins de liens mais plus qualitatifs à mesure que l'autorité monte. Gratuit : échanges contextualisés, plateformes à forte autorité (`ENSEIGNE_A_VERIFIER`, tactiques datées) ; payant recommandé pour aller vite.

**8.4 Avis** (`234333656`) : demande d'avis automatisée à J+10 sur les produits qui satisfont, demande après chaque interaction SAV réussie ; jamais d'achat d'avis. La réputation (Trustpilot) devient un signal SEO.

## Phase 9 — Backend : email, SAV, social (porte 7, dès les premières ventes)

**9.1 Email — objectif 20–30 % du CA** (`249495684` → `250135404`)
- Setup Klaviyo : DNS vérifié, listes single opt-in, sync Shopify. Popup (30–35 s/scroll/exit, un seul champ, 5–12 % d'opt-in attendu).
- Les 6 flows essentiels : panier abandonné (4 emails : ~20 min bénéfices, ~7 h réassurance, ~20 h promo, ~1 j urgence), post-achat (remerciement + upsell jour même, valeurs, tracking, entretien), bienvenue, abandon de fiche, abandon de site, win-back J+30/45. 2–3 emails ciblés par flow, qualité avant quantité — les flows peuvent porter ~80 % du CA email.
- Campagnes : 1 newsletter/semaine en alternant promo / contenu / engagement, début de semaine le matin, structure AIDA, DA de la marque.
- Segmentation : n'envoyer qu'aux engagés (ouverture < 45 j, activité < 30 j, exclure bounces et acheteurs récents) ; santé : ouverture ≥ 33 %, clic > 1,2 %, bounce < 3 %, spam < 1 %. A/B : une variable à la fois, objet testé sur 10 % puis envoi du gagnant.

**9.2 SAV — pilier de LTV** (`233700517`) : outil dédié (Zendesk/Help Scout), rôles opérateur/manager, mini-chat, anticipation des problèmes (séquences de suivi de colis, gestes proactifs), KPI : temps de première réponse, temps de résolution, satisfaction par opérateur. Le SAV nourrit les avis, les avis nourrissent le SEO et la conversion.

**9.3 Social automatisé** (`rj6Rx3zinOk`, `233283052`) : community management de base (branding, interaction) + scénario Make « PostPilot » : 1 produit/jour publié automatiquement sur Facebook/Pinterest/Instagram depuis le catalogue (gratuit ≤ 1 000 opérations/mois). Testing produits Meta seulement ensuite : winners Google + tendances de la niche, 10–12 produits, petits budgets, stabilité 3–5 jours avant de pousser.

## Phase 10 — Scaling (porte 8)

- **Danse budget/tROAS** (`262936735`) : monter les budgets au maximum pour ne plus être limité, puis piloter au ROAS seul (baisser le target → la dépense monte → remonter le budget…). Lire la data sur 30 jours glissants, coût vs ROAS jour par jour.
- **Groupe top produits** : produits à ≥ 3–5 conversions et bon ROAS → groupe dédié à tROAS plus bas (le produit diffuse dans le groupe au target le plus bas) — uniquement là où il y a de la marge.
- **Split par ROAS break-even** (`249178958`) — l'« apothéose », à 6–12 mois avec plusieurs conversions/jour et ≥ 15–30 conversions/mois par groupe : un groupe d'annonces par palier de custom label (2.2 → 3.4 + « reste » agressif), tROAS = palier, exclure « tout le reste » par groupe, bouger tous les targets du même intervalle ensemble. « On ne gère plus au ROAS, on gère au profit » — cohérent avec la règle maison : le scaling se décide sur la **marge contributive**, jamais sur CA − ads.
- **Scaling par le catalogue** : ouvrir des catégories/requêtes nouvelles plutôt que monter les enchères (`232117816`).
- **Q4** (`262936735`) : promos progressives dès début novembre ; la marge se fait sur la black week (lundi–jeudi), Black Friday lui-même = CPC explosés ; surveiller Amazon qui donne le départ.
- Fournisseurs : sortir les best-sellers d'AliExpress vers un partenaire/agent (ratio ~80 % long-tail plateforme / 20 % best-sellers partenaire, `232117915`, `strategie-muse`).

## Phase 11 — Multiplication horizontale (porte 8 → nouvelle porte 0)

Quand une boutique est rentable et déléguée (process écrits, SAV outillé, intégration continue) : ne pas la sur-pousser verticalement — **dupliquer la muse** (`strategie-muse`) : même thème vers d'autres pays (Tabloide FR/DE/IT/NL) ou nouveau type de produit sur le même marché (parc observé : `docs/parc-sites-enzo-honore.md`). La profondeur de catalogue est la barrière défensive. Ne jamais dépendre d'un seul site (vagues de bans GMC). Chaque nouvelle boutique repart à la phase 1 avec porte 0 (post-mortem de la précédente).

---

## Rappels transverses du coach

- Une phase = un objectif (charognard = conversions pas cher ; jamais volume ET marge en même temps).
- Le CTR est la métrique-mère (quality score → CPC → ROAS) ; la campagne de marque dope tout le compte.
- 70–80 % du CA réel attribué dans Ads = normal.
- Les chiffres du formateur sont des résultats personnels (`ENSEIGNE_A_VERIFIER`), les seuils des repères — la porte décide sur preuves, pas sur enthousiasme.
- Interdits inchangés : inventions, faux avis, contournements de contrôle, garanties de résultat (`SKILL.md` § Interdictions).
