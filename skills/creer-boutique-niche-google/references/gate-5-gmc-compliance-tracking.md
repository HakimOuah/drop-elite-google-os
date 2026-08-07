# Porte 5 — GMC, conformité et mesure

## Décision

Vérifier que le commerce est identifiable, cohérent et achetable, que les données produit correspondent au site et qu'une commande est mesurée correctement avant toute dépense.

## A. Transparence commerciale

Contrôler sur le site rendu :

- identité légale, coordonnées et contact fonctionnel ;
- prix et devise cohérents ;
- moyens de paiement conventionnels dans un checkout sécurisé ;
- achat direct sur le domaine revendiqué ;
- livraison, frais, zones et délais réels ;
- retours, remboursements, rétractation et exceptions adaptées ;
- CGV, confidentialité, cookies et mentions requises ;
- absence de promesses, affiliations, avis ou badges trompeurs.

Les modèles `policies-fr/` doivent être renseignés avec des faits réels. Un texte générique contradictoire avec le checkout est un risque, pas une protection.

## B. Cohérence Merchant Center

Comparer automatiquement ou manuellement pour un échantillon représentatif puis tous les cas à risque :

| Champ | Source page | Feed | Données structurées | Checkout/compte GMC |
|---|---|---|---|---|
| id/SKU |  |  |  |  |
| titre/variante |  |  |  |  |
| prix/devise |  |  |  |  |
| disponibilité |  |  |  |  |
| image |  |  |  |  |
| marque/GTIN/MPN |  |  |  |  |
| livraison |  |  |  |  |
| retours |  |  |  |  |

Ne jamais inventer GTIN ou MPN. Fournir seulement les identifiants attribués par le fabricant et certains. Les coûts de livraison vers la France doivent être complets et au moins égaux à ce que l'utilisateur paiera.

## C. Discipline de revue

1. vérifier les politiques officielles actuelles dans `docs/official-source-register.md` ;
2. corriger la cause racine sur le site, le feed ou le compte ;
3. contrôler l'ensemble du parcours ;
4. documenter les preuves ;
5. demander un examen seulement lorsque l'autorisation explicite est donnée.

Ne pas multiplier les demandes sans correction. Ne jamais employer anti-detect, cloaking, fausse identité ou nouveau compte pour fuir une suspension. Aucun délai ou taux d'approbation n'est garanti.

## D. Mesure achat

Le test doit prouver une commande de bout en bout :

- événement achat déclenché uniquement après succès ;
- `value` dynamique égale à la valeur choisie et documentée ;
- `currency` ISO correcte, généralement `EUR` pour une boutique France ;
- `transaction_id` unique, dynamique, non personnel et identique entre sources ;
- produits/quantités si la mesure panier est utilisée ;
- déduplication entre Google tag, GA4 et import backend ;
- achat marqué comme objectif principal selon la stratégie ;
- diagnostics sans erreur bloquante ;
- consentement et information adaptés au cadre applicable ;
- comparaison avec la commande backend.

Ne pas optimiser une campagne e-commerce principale sur un simple `add_to_cart` en le faisant passer pour un achat.

## E. Consentement et données

Établir l'inventaire des traceurs, finalités, bases/consentements, durée, destinataires et mécanismes de retrait. Les conversions améliorées utilisent des données first-party hachées mais ne dispensent pas d'information ni des obligations applicables.

## Critères de passage

- commerce et politiques réels/cohérents ;
- produit test approuvé ou dossier GMC prêt selon le périmètre ;
- aucune incohérence critique page/feed/checkout ;
- achat test observé avec valeur, devise et transaction ID ;
- backend et rapports réconciliables ;
- autorisation de lancement explicite et budget borné.

Sans preuve achat : `REPARER_AVANT`, jamais « lancer pour voir ».
