# Porte 8 — Scaling

## Décision

Augmenter le volume uniquement si l'économie, la mesure, la stabilité du funnel, la capacité fournisseur/SAV et la trésorerie restent acceptables dans un scénario prudent.

## Conditions préalables

- achats réels et tracking réconcilié ;
- marge contributive après publicité positive sur fenêtre pertinente ;
- remboursements/retours intégrés ou réserve prudente ;
- performance non dépendante d'une seule journée ou commande atypique ;
- stock, délais, qualité, paiement et support capables d'absorber le palier ;
- plafond de trésorerie calculé ;
- absence de problème GMC/politique ;
- propriétaire de surveillance et rollback.

## Tableau économique

Suivre au minimum par jour/semaine et cohorte si possible :

- commandes et CA net ;
- coût produit + livraison ;
- frais de paiement/plateforme ;
- remises ;
- remboursements/retours/chargebacks ;
- dépense publicitaire ;
- marge contributive avant/après ads ;
- CAC, ROAS et MER ;
- taux de conversion ;
- délai de livraison et tickets par commande ;
- besoin de trésorerie.

`CA - ads` peut être appelé « revenu après ads » mais jamais profit.

## Paliers

Un palier de scaling doit préciser :

- budget avant/après ;
- hausse absolue et relative ;
- hypothèse ;
- durée/revue selon volume et cycle de conversion ;
- fourchette acceptable de CAC/marge ;
- garde-fous opérationnels ;
- règle de retour au palier précédent.

Ne pas encoder une hausse universelle de 20 %, 30 % ou 50 % comme vérité. Les changements de budget, d'enchères ou d'assets peuvent modifier l'apprentissage ; vérifier l'état du compte et la documentation actuelle.

## Vecteurs de croissance

Évaluer séparément :

- profondeur : plus de budget sur ce qui est déjà rentable ;
- largeur : nouvelles requêtes, produits, zones ou campagnes ;
- valeur : bundle, AOV, upsell, cross-sell ;
- rétention : email/SMS/service quand pertinent et consenti ;
- organique : contenu et maillage ;
- opération : coûts, délais, qualité et fournisseur.

Chaque vecteur possède sa propre hypothèse et son propre risque. Ne pas les déployer tous au même moment.

## Trois scénarios

Recalculer optimiste, central et prudent avec : CPA, conversion, coût fournisseur, change, retours et remises. Le scénario prudent doit respecter le plafond de perte et la trésorerie autorisés.

## Décisions

- `SCALER_PAR_PALIER` : toutes les conditions et garde-fous sont présents ;
- `MAINTENIR` : rentable mais données/capacité insuffisantes ;
- `ITERER` : goulot améliorable ;
- `REDUIRE` : dégradation au-delà du seuil ;
- `STOP` : économie, conformité ou opération invalide.

## Portfolio

Le scaling inclut le coût d'attention. Une nouvelle boutique n'est justifiée que si le système existant est compris, documenté et suffisamment stable. Sinon, elle dilue les apprentissages et augmente le risque opérationnel.
