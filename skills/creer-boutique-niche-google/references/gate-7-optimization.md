# Porte 7 — Optimisation

## Décision

Identifier le goulot causal le plus probable et mener une expérience interprétable, sans modifier simultanément tout le système.

## Diagnostic en cascade

### 1. Intégrité des données

Réconcilier Google Ads, GA4/analytics, Shopify/backend et paiements sur la même période, même fuseau et même définition. Chercher doublons, conversions manquantes, devise, valeur, consentement, attribution et décalage de rapport.

### 2. Acquisition

Analyser pays, appareil, réseau/inventaire, requêtes/termes, CPC, CTR, promesse et exclusions. Un CTR élevé sur une mauvaise intention n'est pas une victoire.

### 3. Landing et produit

Analyser vues qualifiées, sélection variante, profondeur, interaction, ajout panier, objections, prix livré, preuve et mobile. Utiliser les retours utilisateur/recordings autorisés comme indices, pas comme statistiques universelles.

### 4. Checkout

Analyser panier → checkout → paiement : coûts surprises, confiance, moyens de paiement, erreurs, livraison, délais et formulaires.

### 5. Après-achat

Inclure annulations, remboursements, chargebacks, tickets et délais réels. Un ROAS brut peut masquer une offre destructrice après livraison.

## Carte d'expérience

```text
Observation : fait daté
Hypothèse : mécanisme attendu
Variable : un changement matériel principal
Population/période : périmètre
Métrique primaire : décision
Garde-fous : marge, retours, vitesse, erreurs
Stop rule : sécurité/économie
Résultat : valeur + incertitude
Décision : adopter, rejeter, retester
```

## Priorisation

Classer par impact potentiel, qualité de preuve, effort, risque et réversibilité. Corriger les erreurs et incohérences avant d'expérimenter des détails cosmétiques.

## Biais à éviter

- changer budget, enchères, offre, page et feed en même temps ;
- lire seulement les jours favorables ;
- déplacer la fenêtre pour sauver l'hypothèse ;
- confondre corrélation et cause ;
- ignorer retours et marge ;
- traiter l'état d'apprentissage d'une plateforme comme excuse indéfinie ;
- multiplier les boutiques au lieu de réparer un goulot prouvé.

## Sortie

- goulot et niveau de confiance ;
- preuves alternatives considérées ;
- une expérience prioritaire ;
- coût maximal, propriétaire, durée/revue ;
- décision après résultat.
