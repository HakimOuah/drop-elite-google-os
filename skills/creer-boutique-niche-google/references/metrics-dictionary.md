# Dictionnaire de métriques

| Métrique | Formule | Attention |
|---|---|---|
| CTR | clics / impressions | ne mesure pas la qualité après clic |
| CPC | dépense / clics | dépend de l'intention et de l'enchère |
| CVR session | commandes / sessions qualifiées | préciser source et fenêtre |
| ATC rate | ajouts panier / vues produit ou sessions | toujours préciser le dénominateur |
| checkout rate | checkouts / paniers | événements dédupliqués |
| purchase rate | achats / checkouts ou sessions | préciser le dénominateur |
| CAC | dépense d'acquisition / nouveaux clients ou commandes | préciser paid blended et nouveaux/récurrents |
| ROAS | CA attribué / dépense Ads | ne tient pas compte des coûts produit/retours |
| MER | CA total / dépense marketing totale | sensible à l'organique et à la marque |
| AOV | CA net / commandes | enlever annulations selon la convention |
| marge brute | CA net - coût des marchandises | convention comptable à expliciter |
| marge contributive pré-ads | CA net - coûts variables hors ads | inclure paiement, transport, retours attendus |
| marge contributive après ads | marge pré-ads - acquisition | base du scaling court terme |
| CAC de rupture | marge contributive pré-ads par commande/client | dépend de la convention de cohorte |
| ROAS de rupture | CA net / CAC de rupture | supérieur à 1 sauf marge de 100 % |
| refund rate | commandes ou valeur remboursée / base correspondante | ne pas mélanger unité et valeur |
| contribution payback | temps pour récupérer le CAC par contribution | utile si réachat réel |

## Conventions

Chaque rapport doit préciser : période, fuseau, devise, taxes, attribution, statut des remboursements, définition du client, source et date d'extraction.

Si une métrique est indisponible, la marquer `MANQUANT`. Ne pas la remplacer par une moyenne sectorielle non sourcée.
