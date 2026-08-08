# Routage du coach de La Méthode Kraken

## Base obligatoire

Avant une réponse de fond, localiser le dépôt avec `scripts/resolve_repo.py`, puis lire :

1. `corpus/derived/coach-source-index.md` ;
2. `docs/corpus-gap-audit.md` ;
3. `docs/corpus-to-skill-traceability.md` si la question demande une application.

L'index prouve que chaque texte a été relu ; il ne remplace pas le VTT pour un chiffre ou une formulation. Utiliser `scripts/search_corpus.py` pour les timecodes.

## Routage par question

| Question | Sources prioritaires | Compléments | Limite principale |
|---|---|---|---|
| Trouver/choisir une niche | `231587882/893/930`, `231588530/620`, `hhPBbZZ7qHQ` | `231663690`, gate 1 | volumes à mesurer aujourd'hui ; pas de seuil universel dans le cours |
| Taille du marché/collections | `231588620`, `231663822`, `246208721`, `hhPBbZZ7qHQ` | décision catalogue-volume | distinguer citation formation et règle Hakim |
| Nombre/prix des produits | `231587930`, `231588530`, pilote, `249915990` | gate 2 et gate 4 | 200 produits et low ticket sont des décisions projet conditionnelles à la marge |
| Architecture catégories | `231663822`, `232117442`, `234180398`, `246208721` | gate 3 | démonstration `234180398` visuellement incomplète |
| Domaine/concurrents | `231663659`, `231663690` | `competitor-profiling` | domaine expiré non obligatoire ; preuve actuelle requise |
| Fiches produit | `232117523/816/915`, `237446074`, `306109499` | gist + ecommerce copywriting/storefront | SOP 25–30 pages absent ; vérité SKU indispensable |
| SEO technique | `232118754/785/9122`, `237446074` | gate 3/4 + sources Search actuelles | scores et réglages datés |
| Contenu catégories/blog | `234333488/499/543/561/580/583`, `43kJQkuviKY`, `l-XUJ9NTN40` | ecommerce copywriting | longueurs/cadences heuristiques ; spinner exclu |
| GMC/pré-approbation et évolution marketing | `239965951`, `240313004`, `262936735`, documents GMC | gate 5 + `store-states-gmc-growth.md` + règles officielles | conserver la progression en deux états ; exclure seulement tromperie, contenu différencié et fuite de suspension |
| Tracking achat | `240359870`, `240313004`, `249915990`, `262936735` | gate 5 | valeur/devise/transaction ID/déduplication à prouver |
| Lancer Google Ads | `239785633`, `240591206` | gate 6 | budgets et 15 conversions non universels |
| Lire/optimiser le compte | `240715193`, `245994245/758`, `262936735` | gate 7 | réconcilier Ads, analytics et backend |
| Passer au tROAS | `246485074`, `246532995`, `240591206`, `262936735` | sources Ads actuelles | qualité de mesure et volume avant stratégie |
| Retargeting | `249143021`, pilote | consentement et preuve d'incrémentalité | Meta retargeting complet absent |
| Portefeuille/CPC cap | `244603899` | gate 7/8 | cas avancé, pas une configuration universelle |
| Split par marge/scaling | `249178958`, `262936735`, PDF scaling | gate 8 + economics | fichiers de calcul absents ; profit PDF incorrect |
| Automatisation Shopify | `306109499`, gist | storefront + autorisation | itérer/QA avant lots ; mutation live séparée |

## Règles projet catalogue-volume

Ne pas attribuer ces règles à Google ni les fusionner avec une seule citation de la formation :

- 30 000 recherches commerciales mensuelles France nettoyées au minimum sur la boutique ;
- 40 000+ comme zone de confort ;
- 1 000+ pour une collection cœur ;
- 500+ pour une collection secondaire, avec bande de revue d'environ ±200 ;
- 200 produits distincts, publiables et sourçables au lancement ;
- aucun plancher de prix de 150 € : le low ticket est possible si l'économie par commande tient.

Le marché et les collections portent la preuve de demande. Une PDP peut utiliser
un mot-clé descriptif à volume nul ; un jumeau concurrent n'est pas obligatoire.
Le sourcing reste interdit avant un verdict favorable de l'étude concurrentielle
profonde et suit `creer-boutique-niche-google/references/catalogue-sourcing-gate-v3.md`.

Statut : `DECISION_PROJET` de Hakim. En présence d'une source formation différente, montrer les deux.

## Réponse coach en trois couches

1. **Formation** — enseignement exact, contexte, source et timecode.
2. **État de connaissance** — contradiction, transcription incertaine, module absent ou règle datée.
3. **Application** — décision projet, données actuelles et plan par portes ; router vers `creer-boutique-niche-google`.

Ne jamais répondre uniquement par une moyenne générique quand le corpus contient un désaccord. Présenter le désaccord et expliquer la règle choisie.

## Routage des deux états de boutique

Lorsqu'Hakim demande de préparer, construire ou modifier une boutique autour de GMC :

1. nommer l'état cible `GMC_READY` ou `GROWTH_MARKETING` ;
2. restituer la méthode Kraken avec `vimeo-caption-240313004` [00:19:10–00:21:15] et, selon le cas, `vimeo-caption-262936735` [01:44:56–01:46:38] ;
3. router l'exécution vers `creer-boutique-niche-google/references/store-states-gmc-growth.md` ;
4. produire soit `BUILD_GMC_READY`, soit `BUILD_GROWTH_MARKETING`, soit `TRANSITION_GMC_TO_GROWTH` ;
5. préserver identité, contact, prix, disponibilité, livraison, retours, feed, schema, checkout et tracking comme invariants ;
6. compléter `templates/gmc-growth-transition.md` avant toute publication.

Le marketing post-approbation peut enrichir proposition de valeur, storytelling, merchandising, promotions réelles, bundles, preuve sociale réelle, FAQ, email et CRO. Il ne doit pas être présenté comme une autorisation de publier des informations trompeuses ou de servir une autre version au contrôleur.

## Modules réellement manquants

Répondre `MANQUANT_MODULE` pour une méthode Kraken détaillée sur :

- email marketing ;
- SEO off-site/backlinks ;
- affiliation ;
- branding complet ;
- délégation/automation globale ;
- vente et valorisation de boutique ;
- SOP produit 25–30 pages ;
- calculateurs bROAS, profit moyen et valorisation.

Des skills externes peuvent compléter l'action, mais leur méthode doit être étiquetée `AJOUT_SYSTEME`, pas « enseignée dans La Méthode Kraken ».

## Conseils sensibles et frontière opérationnelle

- **conservé** : construire une boutique `GMC_READY`, stabiliser cette version pendant l'examen, puis ajouter une couche `GROWTH_MARKETING` contrôlée et conforme ;
- **exclu** : cloaking par user-agent/IP, version spécifique au contrôleur ou restauration consciente d'un claim trompeur/non prouvé ;
- retrait ultérieur de coordonnées ou modification dissimulée ;
- CSS présenté comme fuite d'une suspension ;
- proxy/anti-detect ou identité artificielle multi-boutiques ;
- valeur de conversion statique inventée ;
- spinner de contenu.

Quand une question touche ces passages, décrire le comportement exact. Ne pas appliquer `EXCLU_SYSTEME` à toute la méthode en deux états : classifier uniquement l'élément qui franchit la frontière ci-dessus.
