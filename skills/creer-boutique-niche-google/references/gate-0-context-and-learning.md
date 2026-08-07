# Porte 0 — Contexte et apprentissage

## Décision

Déterminer si le prochain meilleur investissement est une nouvelle boutique, une réparation, une itération ou l'arrêt d'un projet existant.

## Collecte minimale

- objectif économique, horizon et disponibilité de trésorerie ;
- pays, langue, canal principal et niveau d'autorisation ;
- boutiques actives et historique récent ;
- par boutique : dépenses, impressions, clics, requêtes, sessions, vues produit, ajout panier, checkout, achats, CA et remboursements ;
- état du tracking achat : valeur, devise, transaction ID, déduplication, diagnostic ;
- changements déjà tentés et dates ;
- capacité fournisseur/SAV et temps humain disponible.

## Post-mortem obligatoire si trafic ou dépense existe

Construire le funnel dans une même fenêtre temporelle :

```text
Impressions → clics → sessions qualifiées → vues produit
→ ajout panier → checkout → paiement → commande non remboursée
```

Séparer :

- problème d'acquisition : mauvaise intention, pays, requêtes, promesse publicitaire ;
- problème produit/offre : clics qualifiés sans intérêt ;
- problème page : vues produit sans ajout panier ;
- problème checkout : panier sans achat ;
- problème mesure : backend et plateforme publicitaire divergent ;
- insuffisance d'échantillon : données trop faibles pour conclure.

## Critères

`GO` vers un nouveau projet seulement si :

- l'objectif et les ressources sont explicites ;
- les apprentissages des tests précédents sont consignés ;
- aucun goulot évident plus rentable à réparer n'est laissé sans décision ;
- les actions en cours ne créent pas une dispersion incontrôlable.

Sinon : `REPARER_AVANT`, `ITERER` ou `STOP`.

## Ajout intelligent — registre anti-répétition

Avant une nouvelle recherche, enregistrer les produits, angles et causes d'échec déjà rencontrés : prix, intention, fournisseur, conformité, logistique, conversion, marge. Un nouveau nom pour le même risque ne constitue pas une nouvelle idée.

## Sortie

- baseline chiffrée et dates ;
- goulot principal avec niveau de confiance ;
- décision de focus unique ;
- prochaine porte et condition de revue.
