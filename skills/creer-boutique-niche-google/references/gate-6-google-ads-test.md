# Porte 6 — Test Google Ads

## Décision

Concevoir un test qui peut invalider une hypothèse commerciale avec une dépense limitée, une mesure fiable et des critères définis avant lecture des résultats.

## Carte de test

```yaml
hypothesis: ""
market: FR
offer_and_landing_page: ""
campaign_type: Search|Shopping|Performance Max|other
why_this_type: ""
primary_conversion: purchase
secondary_diagnostics: [view_item, add_to_cart, begin_checkout]
budget_total_cap_eur: 0
budget_daily_eur: 0
break_even_cac_eur: 0
break_even_roas: 0
minimum_signal_or_review_date: ""
stop_rules: []
success_rules: []
authorized_by: ""
```

## Choix du type de campagne

Choisir selon l'hypothèse et la qualité des entrées, pas selon une recette universelle :

- **Search** : tester une intention/requête et garder davantage de lecture sémantique ;
- **Shopping** : tester le couple feed/produit/prix avec données produit propres ;
- **Performance Max** : couverture automatisée multi-inventaire, utile seulement avec objectifs, feed/assets et mesure solides ; les signaux d'audience guident mais ne bornent pas strictement la diffusion.

Les interfaces et options évoluent : vérifier la documentation et le compte actuel. Une chronologie fixe enseignée reste `ENSEIGNE_A_VERIFIER`.

## Structure minimale

- segmentation alignée sur intention, économie et landing page ;
- localisation et langue réelles ;
- exclusions de zones non servies ;
- annonces et assets cohérents avec la page ;
- URL finale exacte ;
- feed propre et produits non pertinents exclus ;
- requêtes/exclusions surveillées ;
- budget compatible avec le plafond de perte et les données nécessaires.

## Stop rules

Définir avant lancement des causes immédiates :

- tracking achat ou checkout cassé ;
- prix/stock/livraison incohérents ;
- trafic hors zone ou requêtes manifestement hors intention ;
- dépense dépassant le plafond autorisé ;
- politique/suspension ;
- incident fournisseur, paiement ou SAV.

Définir aussi les règles économiques : dépenses par rapport au CAC de rupture, marge et signal du funnel. Ne pas utiliser un seuil universel sans tenir compte du CPC, du taux de conversion attendu et de l'incertitude.

## Lecture responsable

Ne pas conclure « produit gagnant/perdant » à partir d'un seul indicateur. Vérifier d'abord :

1. mesure ;
2. qualité du trafic ;
3. cohérence annonce/landing ;
4. funnel ;
5. économie ;
6. taille d'échantillon et variabilité.

## Critères de lancement

- carte complète et approuvée ;
- conversion achat prouvée ;
- budget/plafond explicites ;
- requêtes, assets, feed et landing QA ;
- surveillance et propriétaire nommés ;
- rollback possible.

Le lancement, l'augmentation de budget et la dépense sont des actions de classe C.
