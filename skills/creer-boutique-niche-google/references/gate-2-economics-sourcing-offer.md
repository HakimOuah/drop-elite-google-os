# Porte 2 — Économie, sourcing et offre

## Décision

Vérifier que l'offre peut être livrée telle qu'annoncée, avec marge contributive, trésorerie et capacité opérationnelle suffisantes.

## Vérité fournisseur par variante

Ne jamais qualifier seulement une vignette ou un prix « à partir de ». Pour chaque variante vendue, obtenir :

- identifiant fournisseur et URL stable ;
- variante exacte, composants, dimensions, matériau, couleur et contenu du colis ;
- prix unitaire réel par quantité ;
- livraison vers la France, délai de traitement et transit ;
- TVA/douane selon le montage connu ;
- stock ou disponibilité vérifiée et date ;
- évaluations/commandes observées sans en déduire une qualité certaine ;
- risque IP, conformité, sécurité, batterie, notice ou marquage ;
- procédure défaut/retour ;
- fournisseur de secours et différence de spécification.

Si AliExpress ou une autre source bloque l'automatisation, conserver `MANQUANT`. Ne pas bypasser les protections. Les mutations DSers restent humaines sauf autorisation explicite.

## Économie par commande

Calculer au minimum :

```text
CA net = prix TTC encaissé - remises - remboursements attendus
Coût variable hors ads = produit + transport fournisseur + emballage
  + droits/TVA non récupérable + paiement + plateforme variable
  + SAV/retours attendus + fulfilment
Marge contributive pré-ads = CA net - coût variable hors ads
Marge contributive après ads = marge pré-ads - CAC
CAC de rupture = marge contributive pré-ads
ROAS de rupture = CA net / CAC de rupture
```

Adapter le traitement de TVA et fiscalité au statut réel de l'entreprise avec un professionnel compétent. Ne pas compter deux fois un coût ni considérer une TVA collectée comme marge.

### Réserves attendues

Utiliser les données réelles quand elles existent. Sinon, créer des scénarios explicites, pas un chiffre caché : optimiste, central, prudent. Tester : hausse fournisseur, hausse transport, taux de remboursement, chargeback, CPA et taux de change.

## Trésorerie

Documenter :

- délai d'encaissement du prestataire de paiement ;
- paiement fournisseur avant encaissement disponible ;
- réserve/hold éventuel ;
- cadence de remboursement ;
- besoin en fonds pour 7, 14 et 30 jours au rythme envisagé ;
- plafond de commandes que le SAV et la trésorerie peuvent absorber.

Une campagne peut être rentable sur le papier et provoquer une crise de trésorerie.

## Construction de l'offre

L'offre doit relier :

1. résultat désiré et situation d'usage ;
2. mécanisme ou sélection crédible ;
3. produit principal et variantes nécessaires ;
4. bundles/quantités cohérents avec la marge ;
5. bonus réellement fournis ;
6. garantie compatible avec l'opération et le droit ;
7. preuve disponible ;
8. réduction du délai, de l'effort et du risque perçus ;
9. objections traitées sans fausse urgence.

Ne pas fabriquer prix barré, compteur, rareté, avis ou exclusivité. Une garantie commerciale ne doit pas réduire les droits légaux.

## Critères de passage

- variante et coût livré prouvés ;
- promesse compatible avec le produit réel ;
- scénario central positif et scénario prudent connu ;
- CAC et ROAS de rupture calculés ;
- trésorerie compatible avec le test prévu ;
- solution pour retours, défauts et fournisseur de secours ;
- offre distincte, honnête et réalisable.

Sinon, `REPARER_AVANT` ou `STOP`.
