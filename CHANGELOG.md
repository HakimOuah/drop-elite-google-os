# Changelog

Toutes les modifications notables de ce dépôt sont documentées ici.

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
