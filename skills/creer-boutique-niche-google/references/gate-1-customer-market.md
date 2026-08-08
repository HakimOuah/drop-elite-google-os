# Porte 1 — Marché et client

## Décision

Prouver qu'une demande solvable existe, qu'elle correspond à une intention exploitable et qu'un angle crédible peut gagner face aux alternatives.

## Séquence

### 1. Définir l'unité de recherche

Formuler : problème, situation d'usage, acheteur, bénéficiaire, fourchette de prix, saisonnalité, contraintes logistiques et réglementaires. Ne pas commencer par un persona inventé.

### 2. Demande Search France

Lorsque `chasse-clusters-codex` est disponible, lui déléguer la recherche volume-first et la mesure SEMrush `db=fr`. Nettoyer les faux volumes : requêtes informationnelles, marque, emploi, gratuit, seconde main, pièces non compatibles et géographies hors cible.

Conserver séparément :

- volume brut ;
- volume commercial nettoyé ;
- CPC/pression publicitaire ;
- tendance et saisonnalité ;
- distribution par intention et par cluster.

Le volume n'est pas une preuve de rentabilité. Un retour terrain documenté ou un test antérieur peut invalider un candidat malgré le volume.

### 2a. Seuils du mode `catalogue-volume`

`DECISION_PROJET` du 2026-08-08, applicable à la stratégie Kraken de boutique catalogue :

- plancher boutique : **30 000 recherches mensuelles commerciales nettoyées en France** sur l'ensemble des intentions distinctes du catalogue ;
- zone de confort : **40 000 recherches mensuelles ou plus** ; ce nombre n'est pas un plafond ;
- collection cœur : cible **1 000 recherches mensuelles ou plus**, avec bande de revue autour de **800–999** ;
- collection secondaire : cible **500 recherches mensuelles ou plus**, avec bande de revue autour de **300–499** ;
- la tolérance est d'environ **± 200** autour de la cible retenue et produit un `GO_CONDITIONNEL`, jamais une validation automatique ;
- sous 300, une intention ne compte normalement pas comme collection SEO autonome : la fusion avec une collection plus large, une page non indexée de merchandising ou une justification exceptionnelle doit être étudiée ;
- avant d'engager la construction, prouver au **niveau des catégories** qu'au moins 200 concepts de produits distincts peuvent alimenter le catalogue total de la boutique. Une sonde fournisseur par famille doit confirmer la profondeur, mais la porte 1 n'exige ni jumeau concurrent, ni listing final, ni mot-clé positif pour chacune des 200 futures PDP. Les variantes de couleur/taille d'un même produit ne gonflent pas ce total ; appliquer ensuite `catalogue-sourcing-gate-v3.md`.

Le total boutique est une somme dédupliquée : une requête, un synonyme, un pluriel ou une intention recouvrante ne peut pas être compté dans plusieurs collections. Exclure marques concurrentes, informationnel sans proximité commerciale, occasion, emploi, gratuit, prestations et géographies hors cible. Conserver la base (`db=fr`), la date, les mots-clés et l'URL cible pressentie.

Les seuils `1 000 / 150` retrouvés dans la formation restent `ENSEIGNE_A_VERIFIER`. Pour ce mode, la décision projet ci-dessus retient un plancher plus exigeant de 500 pour une collection secondaire, avec tolérance documentée.

### 3. Voix du client

Collecter des formulations brutes depuis avis, forums, communautés, tickets ou entretiens autorisés :

- déclencheurs ;
- résultat recherché ;
- objections et craintes ;
- critères de choix ;
- alternatives utilisées ;
- vocabulaire exact ;
- après-achat, SAV et causes de retour.

Chaque insight doit conserver sa source. Distinguer fréquence observée et intensité exprimée.

### 4. Concurrence et droit de gagner

Évaluer au moins :

- type d'acteur : marketplace, dropship probable, spécialiste, marque établie ;
- assortiment, prix total livré, offre et garanties ;
- qualité du contenu, du SEO, du feed et du storefront ;
- délais, retours, réputation observable et preuves ;
- faiblesse exploitable sans mensonge.

La présence de Shopify est un indice technique, pas une preuve de fournisseur ni de dropshipping. Ne pas confondre un site faible avec un marché facile.

### 5. Risques structurels

Stopper ou durcir la preuve pour : conformité produit élevée, forte casse/retour, tailles complexes, batteries/liquides, promesses santé, propriété intellectuelle, SAV technique, livraison incompatible ou commodité extrême sans angle.

## Score de décision non automatique

Noter 0–3 pour rendre les écarts visibles, sans laisser la moyenne décider : demande commerciale, intensité du problème, valeur perçue, concurrence prouvée, différenciation, marge potentielle, logistique, conformité, contenu/SEO et capacité d'exécution.

Un seul risque fatal peut imposer `STOP` même si le total est élevé.

## Critères de passage

- cluster commercial nettoyé et sourcé ;
- en mode `catalogue-volume`, plancher boutique atteint ou écart explicitement classé `GO_CONDITIONNEL`, collections ventilées selon leurs cibles et potentiel fournisseur d'au moins 200 produits distincts démontré au niveau des familles ;
- au moins une alternative payante réellement observée ;
- problème et langage client non inventés ;
- différence exécutable et honnête ;
- risques fatals absents ou contrôlables ;
- hypothèse d'économie plausible à tester à la porte 2.

L'étude concurrentielle profonde est une condition de sortie de cette porte.
Un `STOP` ou un dossier incomplet produit `SUSPENDU_PHASE_2` et interdit le
sourcing catalogue ; seul un verdict documenté autorisant la suite ouvre
`catalogue-sourcing-gate-v3.md`.

## Sortie

Verdict `GO`, `GO_CONDITIONNEL` ou `STOP`, avec matrice demande/concurrence/VOC, droit de gagner et données manquantes.
