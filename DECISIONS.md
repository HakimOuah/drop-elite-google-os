# Journal des décisions

## D-001 — Dépôt autonome privé

**Date :** 2026-08-08  
**Décision :** créer `HakimOuah/drop-elite-google-os` au lieu d'intégrer le corpus à un dépôt existant.  
**Pourquoi :** séparer la connaissance de formation et les skills des boutiques opérationnelles, conserver les droits privés et permettre une restauration indépendante.  
**Alternatives écartées :** gonfler `boutique-pipeline` avec le corpus ; utiliser `dropshipping-product-factory`, désormais historique ; mélanger les sources dans le hub `boutiques-drop`.

## D-002 — Hiérarchie des preuves

**Décision :** une règle officielle actuelle prime sur une affirmation de formation ; une preuve propre au projet prime sur une généralité ; un élément non démontré conserve un statut explicite.  
**Conséquence :** le corpus sert à formuler des hypothèses et méthodes, jamais à inventer une exigence Google.

## D-003 — Scaling économique réel

**Décision :** piloter le scaling sur la marge contributive après produit, livraison, frais de paiement, remises, remboursements/retours, taxes applicables et publicité.  
**Conséquence :** `CA - publicité` n'est pas appelé profit.

## D-004 — Conformité sans contournement

**Décision :** exclure toute tactique d'évasion ou de dissimulation : anti-detect, identité incohérente, cloaking, multiplication de comptes pour fuir une suspension.  
**Conséquence :** une suspension déclenche diagnostic, correction et recours documenté.

## D-005 — GitHub comme sauvegarde durable

**Décision :** toute évolution durable est inscrite dans le changelog ou le journal d'opérations, validée, commitée et poussée.  
**Conséquence :** les copies locales installées ne sont jamais l'unique détenteur du travail.

## D-006 — Mode catalogue-volume sans plancher high-ticket

**Date :** 2026-08-08

**Décision :** pour la stratégie Drop Elite `catalogue-volume`, retenir un plancher boutique de 30 000 recherches mensuelles commerciales nettoyées en France, une zone de confort à 40 000+, une cible de 1 000+ pour une collection cœur et 500+ pour une collection secondaire avec tolérance d'environ ±200. Le catalogue de lancement contient au moins 200 produits distincts. Aucun prix minimum de 150 € n'est imposé ; le low ticket est admissible si l'économie de commande est viable.

**Provenance :** décision explicite de Hakim, éclairée par les seuils retrouvés dans les transcriptions ; statut `DECISION_PROJET`.

**Périmètre :** ce mode n'écrase pas le pipeline high-ticket historique de `boutique-pipeline`. Lorsque `chasse-clusters-codex` fournit les mesures, ses anciens verdicts prix/low-ticket ne s'appliquent pas à ce mode.

**Conséquence :** les portes 1 à 4 contrôlent la déduplication des volumes, les seuils de collections, la profondeur de 200 produits et la marge au niveau de la commande plutôt qu'un prix unitaire arbitraire.
