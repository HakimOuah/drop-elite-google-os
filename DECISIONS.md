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

**Décision :** pour la stratégie Kraken `catalogue-volume`, retenir un plancher boutique de 30 000 recherches mensuelles commerciales nettoyées en France, une zone de confort à 40 000+, une cible de 1 000+ pour une collection cœur et 500+ pour une collection secondaire avec tolérance d'environ ±200. Le catalogue de lancement contient au moins 200 produits distincts. Aucun prix minimum de 150 € n'est imposé ; le low ticket est admissible si l'économie de commande est viable.

**Provenance :** décision explicite de Hakim, éclairée par les seuils retrouvés dans les transcriptions ; statut `DECISION_PROJET`.

**Périmètre :** ce mode n'écrase pas le pipeline high-ticket historique de `boutique-pipeline`. Lorsque `chasse-clusters-codex` fournit les mesures, ses anciens verdicts prix/low-ticket ne s'appliquent pas à ce mode.

**Conséquence :** les portes 1 à 4 contrôlent la déduplication des volumes, les seuils de collections, la profondeur de 200 produits et la marge au niveau de la commande plutôt qu'un prix unitaire arbitraire.

## D-007 — Assimilation texte distincte de la validation audio

**Date :** 2026-08-08

**Décision :** déclarer les 48 VTT et la transcription pilote `ASSIMILE_TEXTE` après lecture intégrale, tout en conservant les sources VTT en `AUTOMATIQUE_NON_RELUE` au sens audio.

**Pourquoi :** permettre des réponses de coach routées par source sans prétendre corriger les erreurs de transcription, les gestes visuels absents ou la véracité des affirmations.

**Conséquence :** chaque seuil déterminant revient au VTT/timecode et, si possible, au média ; chaque procédure absente devient `MANQUANT_MODULE`. Les tactiques de contournement repérées restent archivées mais portent le statut `EXCLU_SYSTEME`.

## D-008 — Méthode Kraken en deux états de boutique

**Date :** 2026-08-08

**Décision :** attribuer le corpus à La Méthode Kraken d'Enzo Honoré et conserver opérationnellement sa progression : construire un état `GMC_READY` complet et sobre, puis un état `GROWTH_MARKETING` enrichi après validation. Le système doit savoir construire chaque état séparément ou réaliser `TRANSITION_GMC_TO_GROWTH`.

**Provenance :** demande explicite de Hakim, soutenue par `vimeo-caption-240313004` [00:19:10–00:21:15] et `vimeo-caption-262936735` [01:44:56–01:46:38]. Statuts `ENSEIGNE_A_VERIFIER` et `DECISION_PROJET`.

**Contrat :** la boutique reste réelle, identifiable et achetable dans les deux états. Tous les visiteurs voient la même version publiée. Identité/contact, produit/variante, prix/stock, livraison/retours, feed/schema/checkout, tracking et consentement sont des invariants à réconcilier lors de chaque bascule.

**Éléments marketing autorisés :** proposition de valeur, storytelling, merchandising, promotions réelles, prix de référence justifiables, bundles, seuils de livraison, preuve sociale réelle, FAQ, email, contenus SEO et expériences CRO.

**Frontière maintenue :** contenu différent selon le contrôleur, restauration consciente d'un claim trompeur ou non prouvé, retrait des coordonnées/politiques, incohérence volontaire ou fuite de suspension restent `EXCLU_SYSTEME`.

**Conséquence :** toute construction ou transition utilise `references/store-states-gmc-growth.md`, complète `templates/gmc-growth-transition.md`, conserve une baseline, vérifie le rendu et prévoit un rollback avant publication.

## D-009 — Finalité coach-associé et proactivité

**Date :** 2026-08-08

**Décision :** la finalité du système est d'être le coach de La Méthode Kraken et l'associé de Hakim, pas un exécutant à la tâche. Le système suit la roadmap `skills/creer-boutique-niche-google/references/strategie-pas-a-pas.md`, connaît l'état de chaque boutique et enchaîne de sa propre initiative sur l'étape suivante — exécutée si locale et réversible, proposée sinon.

**Provenance :** demande explicite de Hakim (2026-08-08), après constat qu'une sélection de niches n'avait pas été suivie spontanément de l'étude concurrentielle profonde.

**Conséquence :** l'étude concurrentielle profonde (SEMrush, catalogue, Brand Search, marketing/angle/positionnement, persona, synthèse différenciante) est une étape non négociable après toute sélection de niche ; chaque réponse se termine en situant le travail dans la roadmap. Les garde-fous de preuve et d'autorisation restent inchangés (D-002, D-004).

## D-010 — Second lot de corpus et couverture des briques manquantes

**Date :** 2026-08-08

**Décision :** intégrer les 17 contenus fournis par Hakim (netlinking, contenu, avis, Facebook, SAV, email marketing, automatisation sociale) au corpus autorisé, porter l'index coach à 66 contenus et requalifier les modules concernés dans l'audit des lacunes.

**Provenance :** URLs transmises par Hakim le 2026-08-08 (sous-titres Vimeo signés + vidéo YouTube non répertoriée de la chaîne Kraken Formation), autorisation du propriétaire déclarée par Hakim.

**Conséquence :** la stratégie pas à pas couvre désormais l'intégralité de la chaîne muse (SEO off-site, email, SAV, retargeting social inclus) ; les ressources jointes citées dans ces vidéos (templates Klaviyo, calendrier éditorial, blueprint Make, tuto Help Scout) restent `MANQUANT` et ne doivent pas être inventées.
