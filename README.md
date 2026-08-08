# Drop Elite Google OS

Système privé, reproductible et sourcé pour concevoir, valider, lancer et améliorer des boutiques de niche orientées Google Ads et SEO en France.

Ce dépôt réunit quatre couches qui doivent rester distinctes :

1. le **corpus autorisé** de la formation et ses documents ;
2. les **règles officielles actuelles** de Google et du droit français ;
3. les **méthodes opératoires** synthétisées dans des skills Codex ;
4. les **preuves propres à chaque boutique** : données marché, fournisseur, marge, tracking et résultats.

Une affirmation enseignée dans la formation n'est jamais automatiquement présentée comme une règle Google. Le système utilise les statuts `OFFICIEL_ACTUEL`, `ENSEIGNE_A_VERIFIER`, `OBSERVE_PROJET`, `HYPOTHESE` et `MANQUANT`.

## Skill principal

Le point d'entrée est [`skills/creer-boutique-niche-google/SKILL.md`](skills/creer-boutique-niche-google/SKILL.md). Il orchestre neuf portes de décision : contexte, marché, économie/offre, SEO, boutique, GMC/mesure, test Ads, optimisation et scaling.

Son mode `catalogue-volume` accepte le low ticket sans plancher arbitraire lorsque la demande France dédupliquée, l'économie de commande et un catalogue d'au moins 200 produits distincts sont prouvés. Les seuils opératoires sont documentés dans les portes 1 à 4 et restent des décisions de projet, pas des règles officielles Google.

Il route vers les compétences spécialisées existantes lorsqu'elles sont disponibles, notamment la chasse produit France, la recherche client, l'offre, le storefront, la CRO et le copywriting. Il ne duplique pas leurs savoir-faire.

## Principes non négociables

- Aucun chiffre, avis, délai, stock, certification ou avantage n'est inventé.
- Aucun contournement de contrôle Google : pas d'identités jetables, anti-detect, cloaking ou fuite après suspension.
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

La relecture sémantique des 49 contenus parlés est documentée source par source dans [`corpus/derived/coach-source-index.md`](corpus/derived/coach-source-index.md). Les modules, pièces jointes, contradictions et conseils exclus sont recensés dans [`docs/corpus-gap-audit.md`](docs/corpus-gap-audit.md). Le statut reste une assimilation du texte, pas une validation audio ni une validation officielle des affirmations.

## Confidentialité et droits

Le dépôt doit rester privé. Les contenus tiers ne sont pas redistribuables. Voir [`RIGHTS.md`](RIGHTS.md) et [`SECURITY.md`](SECURITY.md).
