# Changelog

Toutes les modifications notables de ce dépôt sont documentées ici.

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
