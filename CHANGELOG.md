# Changelog

Toutes les modifications notables de ce dépôt sont documentées ici.

## 2026-08-08 — CSS Google Shopping France : vérification externe du corpus

- nouveau `docs/css-shopping-france.md` : enquête sourcée sur sources officielles Google (consultées le 2026-08-08), avec distinction explicite fait sourcé / interprétation / non vérifié ;
- **auto-CSS écarté** : les conditions du programme exigent un comparateur public affichant au moins 50 domaines marchands distincts par pays, un moteur de recherche propre et un accès sans inscription — hors de portée d'une boutique unique ;
- **correction d'une erreur du corpus de formation** : un CSS ne modifie aucune règle Merchant Center (« All campaigns need to follow the same Shopping ads policies »), n'accorde aucune immunité et n'« autorise » pas le dropshipping — que Google n'interdit pas, mais soumet à une transparence complète sur l'exécution ;
- **requalification du « −20 % sur les CPC »** : Google documente un « pourcentage fixe déduit des enchères » sans le chiffrer ; ce n'est pas une remise de facturation mais une différence de mécanique d'enchère (≈ +25 % de puissance d'enchère à budget égal) ;
- **relevé tarifaire** : 90 CSS Partners listés pour la France dans l'annuaire officiel, options publiques de 0 à 39 €/mois (Cobiro, ShopXYZ, Bigshopper, Producthero, Genie) — les 39,90 € puis 59-69 €/mois recommandés par la formation sont au-dessus du marché, et le prestataire « Deshops » reste introuvable ;
- recommandation pour une boutique unique à 30 €/jour : CSS tiers en self-service à 0-30 €/mois, jamais de CSS managé, conformité GMC traitée en priorité ;
- `docs/official-source-register.md` : nouvelle section CSS avec les huit sources primaires utilisées.

## 2026-08-08 — Gate V3 catalogue et sourcing

- remplacement du gate V2 trop strict au niveau PDP par une preuve portée par la niche et les collections ;
- interdiction du sourcing avant une étude concurrentielle profonde favorable ;
- conservation des PDP descriptives à volume zéro et suppression de l'obligation d'un jumeau concurrent ;
- formalisation des 200 produits au total boutique, des 10–20 produits par sous-catégorie et de l'ordre de sélection 80/20 ;
- maintien d'une revue humaine et de la vérification exacte SKU, fret, conformité et économie avant publication ;
- mise à jour du routage coach et des compteurs de couverture à 229 contenus parlés.

## 2026-08-08 — Cours Skool complet ingéré (229 contenus) + documents + stratégie enrichie

- récupération du **Classroom Skool complet** (29 modules) via l'onglet Classroom : 131 transcriptions Vimeo + 32 YouTube ingérées dans le corpus (66 → **229 contenus parlés**), 89 replays de coaching archivés dans `corpus/replays-coaching/`, 77 documents (slides PDF, checklists, briefs, templates, roadmaps) dans `corpus/raw/documents/` (7 fiches Marketplace écartées) ;
- extraction du texte des PDF via pymupdf ; index `coach-source-index.md` étendu (section « Second versement », statut `INGERE_TEXTE_BRUT`), compteur porté à 229, validation OK ;
- relecture ciblée des nouveaux modules par agents parallèles et enrichissement de `strategie-pas-a-pas.md` : construction Shopify de A à Z, intégration produit assistée par **Claude Code** (MCP Shopify, API REST Woo, skill + agent vérificateur), **agent fournisseur + ERP** (phase 9bis), tracking server-side, email **Brevo**, **scaling horizontal + international hreflang**, **revente/valorisation** (DOTMARKET), cash-flow ;
- note d'arbitrage sur la divergence **méthode « charognard » (archive) vs lancement direct tROAS (module 2025)** ;
- nouveau `references/structure-legale-fr.md` (statut, micro+SASU, TVA dropshipping, comptabilité, expatriation — daté, à re-vérifier 2026) ;
- `docs/inventaire-classroom-skool.md` (carte de couverture des 29 modules) ; audit des lacunes requalifié (délégation, revente désormais `COUVERT`).

## 2026-08-08 — Second lot de transcriptions, mission coach-associé et stratégie pas à pas

- ingestion de 17 nouveaux contenus fournis par Hakim (16 VTT Vimeo + 1 vidéo YouTube « PostPilot ») : netlinking, stratégie de contenu, avis clients, Facebook/retargeting, canal Shopify, SAV, email marketing Klaviyo (6 vidéos) et automatisation sociale Make — le corpus passe de 49 à 66 contenus parlés ;
- relecture sémantique du second lot et extension de l'index coach (nouvelles sections SEO off-site, réseaux sociaux, SAV, email marketing) ;
- relecture complète des 49 anciens contenus par quatre agents parallèles et consolidation de la séquence, des seuils et des procédures ;
- mise à jour de l'audit des lacunes : email, netlinking, SAV et retargeting Meta passent de `MANQUANT_MODULE` à couverts (ressources jointes toujours absentes) ;
- création de `references/strategie-pas-a-pas.md` : la roadmap opérationnelle en 11 phases, du choix de niche à la multiplication horizontale, sourcée sur les 66 contenus ;
- création de `references/mission-coach-associe.md` : la finalité du système est d'être le coach de La Méthode Kraken et l'associé de Hakim, avec règle de proactivité (dont l'étude concurrentielle profonde obligatoire après toute sélection de niche) ;
- création de `docs/parc-sites-enzo-honore.md` : parc de boutiques observé du formateur (capture SAV multi-boutiques), servant de banc de calibrage des niches ;
- mise à jour des SKILL.md (`creer-boutique-niche-google`, `derouler-strategie-drop-elite`) et du README pour ancrer la posture coach-associé et les nouveaux compteurs du corpus.

## 2026-08-08 — Deux états de boutique GMC et Growth

- attribution explicite du corpus à La Méthode Kraken d'Enzo Honoré, tout en conservant les identifiants techniques historiques ;
- reclassification de la progression boutique sobre → boutique marketing comme méthode Kraken conservée ;
- ajout des états `GMC_READY` et `GROWTH_MARKETING` et des modes de construction associés ;
- ajout d'un contrat d'invariants, d'une matrice des modules marketing, d'un protocole de transition et d'un template de preuve ;
- intégration du workflow aux portes storefront/GMC et au routage coach ;
- maintien d'une frontière précise avec le contenu différencié pour le contrôleur, les claims trompeurs et la fuite de suspension ;
- ajout d'une validation automatique de la présence et de la cohérence du workflow.

## 2026-08-08 — Base de connaissance coach exhaustive

- relecture sémantique intégrale des 48 VTT et de la transcription pilote, soit 49 contenus parlés ;
- création d'un index source par source couvrant enseignements, seuils, limites et tactiques exclues ;
- création d'un audit des modules, pièces jointes, contradictions et procédures manquants ;
- ajout d'un routage coach par question et des statuts `ASSIMILE_TEXTE`, `EXCLU_SYSTEME` et `AJOUT_SYSTEME` ;
- correction de la cartographie de `231663659`, consacrée au domaine expiré ;
- ajout d'une résolution portable du clone privé pour le skill installé ;
- validation automatique que chaque transcription du manifest apparaît dans l'index coach.

## 2026-08-08 — Mode catalogue-volume

- ajout du plancher boutique de 30 000 recherches commerciales nettoyées et de la zone de confort à 40 000+ ;
- ajout des cibles par collection : 1 000+ pour une collection cœur, 500+ pour une collection secondaire, avec bande de revue d'environ ±200 ;
- ajout d'un catalogue de lancement d'au moins 200 produits distincts ;
- suppression de tout plancher high-ticket dans ce mode : le low ticket est accepté si l'économie par commande est viable ;
- séparation explicite avec le pipeline historique high-ticket de `chasse-clusters-codex`.

## 2026-08-08 — Maintenance CI

- passage à `actions/checkout@v5` et `actions/setup-python@v6`, compatibles avec le runtime Node.js 24 de GitHub Actions.

## 2026-08-08 — Initialisation

- création du dépôt privé autonome ;
- intégration du corpus autorisé : VTT Vimeo, sous-titres YouTube, documents PDF et pilote audio/transcrit ;
- création du skill global détaillé pour boutiques de niche Google Ads/SEO ;
- adaptation des skills d'ingestion et de déroulage stratégique ;
- sauvegarde et routage des 11 skills spécialisés sélectionnés, avec lockfile SHA-256 ;
- création des modèles de politiques françaises paramétrables ;
- ajout d'une carte manuelle des modules et de la traçabilité corpus → portes ;
- ajout des scripts de génération, validation et installation ;
- documentation de la provenance, des droits, de la sécurité et de la restauration.
