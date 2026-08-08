# La Méthode Kraken — Google OS

Système privé, reproductible et sourcé pour concevoir, valider, lancer et améliorer des boutiques de niche orientées Google Ads et SEO en France.

Le dépôt et certains identifiants techniques conservent le nom historique `drop-elite-google-os` pour rester compatibles avec les installations existantes. La formation source est désormais attribuée à **La Méthode Kraken d'Enzo Honoré** conformément à l'indication de Hakim.

Ce dépôt réunit quatre couches qui doivent rester distinctes :

1. le **corpus autorisé** de la formation et ses documents ;
2. les **règles officielles actuelles** de Google et du droit français ;
3. les **méthodes opératoires** synthétisées dans des skills Codex ;
4. les **preuves propres à chaque boutique** : données marché, fournisseur, marge, tracking et résultats.

Une affirmation enseignée dans la formation n'est jamais automatiquement présentée comme une règle Google. Le système utilise les statuts `OFFICIEL_ACTUEL`, `ENSEIGNE_A_VERIFIER`, `OBSERVE_PROJET`, `HYPOTHESE` et `MANQUANT`.

## Finalité : coach et associé

Le système n'est pas un exécutant à la tâche : il est le **coach de La Méthode Kraken et l'associé de Hakim**. Il connaît la méthode de bout en bout, sait où en est chaque boutique, répond aux questions avec sources, et enchaîne de sa propre initiative sur l'étape suivante de la roadmap. Cette posture est définie dans [`skills/creer-boutique-niche-google/references/mission-coach-associe.md`](skills/creer-boutique-niche-google/references/mission-coach-associe.md) ; la roadmap opérationnelle complète est [`skills/creer-boutique-niche-google/references/strategie-pas-a-pas.md`](skills/creer-boutique-niche-google/references/strategie-pas-a-pas.md). Le parc de boutiques observé du formateur, qui sert de banc de calibrage des niches, est décrit dans [`docs/parc-sites-enzo-honore.md`](docs/parc-sites-enzo-honore.md).

## Skill principal

Le point d'entrée est [`skills/creer-boutique-niche-google/SKILL.md`](skills/creer-boutique-niche-google/SKILL.md). Il orchestre neuf portes de décision : contexte, marché, économie/offre, SEO, boutique, GMC/mesure, test Ads, optimisation et scaling.

Son mode `catalogue-volume` accepte le low ticket sans plancher arbitraire lorsque la demande France dédupliquée, l'économie de commande et un catalogue d'au moins 200 produits distincts sont prouvés. Les seuils opératoires sont documentés dans les portes 1 à 4 et restent des décisions de projet, pas des règles officielles Google.

Pour Merchant Center, il sait construire deux états de storefront : `GMC_READY`, commerce complet et sobre pour la validation, puis `GROWTH_MARKETING`, même socle enrichi d'une couche de persuasion, merchandising, offre et CRO. La méthode, la matrice d'invariants et le protocole de bascule sont détaillés dans [`store-states-gmc-growth.md`](skills/creer-boutique-niche-google/references/store-states-gmc-growth.md).

Il route vers les compétences spécialisées existantes lorsqu'elles sont disponibles, notamment la chasse produit France, la recherche client, l'offre, le storefront, la CRO et le copywriting. Il ne duplique pas leurs savoir-faire.

## Principes non négociables

- Aucun chiffre, avis, délai, stock, certification ou avantage n'est inventé.
- Aucun contournement de contrôle Google : pas d'identités jetables, anti-detect destiné à masquer des liens, contenu différencié pour le contrôleur ou fuite après suspension. La transition documentée `GMC_READY` → `GROWTH_MARKETING`, identique pour tous et conforme dans les deux états, est une méthode conservée.
- Une approbation GMC n'est jamais garantie.
- Aucun budget média n'est lancé sans achat testable avec valeur, devise et identifiant de transaction unique.
- Le scaling se décide sur la marge contributive et la trésorerie, pas sur `CA - dépenses publicitaires`.
- Les modifications commerciales sensibles restent soumises à autorisation explicite.
- Chaque évolution durable est documentée, validée, commitée et poussée sur GitHub.

## Organisation

- `skills/` : skills installables et leurs références.
- `corpus/` : sources brutes autorisées, copie canonique et dérivés textuels.
- `policies-fr/` : modèles français paramétrables à adapter aux faits réels.
- `docs/` : architecture, provenance et registre des sources officielles.
- `scripts/` : génération des dérivés, validation et installation locale.

## Installation sur une nouvelle machine

Suivre [`RESTORE.md`](RESTORE.md). Le dépôt privé est la source de vérité portable ; les dossiers installés dans `~/.codex/skills` sont des copies de travail.

La transformation du cours vers les portes et les corrections apportées sont détaillées dans [`docs/corpus-to-skill-traceability.md`](docs/corpus-to-skill-traceability.md).

Le corpus couvre le **cours Skool complet (29 modules, 229 contenus parlés)** ingéré le 2026-08-08, plus **77 documents** (slides, checklists, briefs, templates) et **89 replays de coaching** archivés à part. L'index source par source est dans [`corpus/derived/coach-source-index.md`](corpus/derived/coach-source-index.md) ; la carte de couverture module par module dans [`docs/inventaire-classroom-skool.md`](docs/inventaire-classroom-skool.md) ; les lacunes et ressources encore manquantes dans [`docs/corpus-gap-audit.md`](docs/corpus-gap-audit.md). Les 163 transcriptions du versement complet sont en statut `INGERE_TEXTE_BRUT` (titre observé + texte disponible, relecture fine à la demande) ; les 66 contenus du premier lot restent relus en détail. Le statut reste une assimilation du texte, pas une validation audio ni officielle.

## Confidentialité et droits

Le dépôt doit rester privé. Les contenus tiers ne sont pas redistribuables. Voir [`RIGHTS.md`](RIGHTS.md) et [`SECURITY.md`](SECURITY.md).
