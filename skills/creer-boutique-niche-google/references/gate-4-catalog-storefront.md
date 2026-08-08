# Porte 4 — Catalogue et storefront

## Décision

Prouver qu'un visiteur mobile peut comprendre l'offre, vérifier ce qu'il reçoit, résoudre ses objections et acheter sans friction ni tromperie.

## Contrat de vérité catalogue

Pour chaque produit/variante : titre, SKU, prix, comparaison de prix justifiée, stock, images, couleur, dimensions, matière, contenu du colis, compatibilité, entretien, avertissements, délai et retours doivent correspondre à la source vérifiée.

Une photo fournisseur n'autorise pas à déduire une géométrie, un matériau ou un accessoire non confirmé. Les visuels générés doivent préserver le produit et être identifiés/conformes lorsque les plateformes l'exigent.

## Profondeur du catalogue en mode `catalogue-volume`

Le catalogue de lancement contient au moins **200 produits distincts, publiables et réellement sourçables**. Compter une fiche produit correspondant à un objet distinct ; les variantes de taille, couleur, lot ou matériau d'une même fiche ne sont pas 200 produits différents. Un doublon, un produit sans fournisseur vérifiable, une fiche vide ou un produit indisponible ne compte pas.

Répartir ces produits dans les collections validées par la porte 3 afin d'éviter les collections artificielles ou vides. Le low ticket est autorisé et n'entraîne aucun plancher de prix ; chaque produit et l'économie de commande restent soumis à la vérité catalogue et à la porte 2.

## Hiérarchie de page produit

Au-dessus de la ligne de flottaison mobile :

- produit identifiable ;
- bénéfice principal précis ;
- prix et variante ;
- délai/livraison suffisamment visible ;
- CTA clair ;
- preuve réelle ou aucune preuve ;
- accès aux informations essentielles.

Puis : problème et usage, bénéfices soutenus par caractéristiques, contenu du colis, dimensions/compatibilité, démonstration, comparaison honnête, livraison/retours, FAQ et CTA final.

## Galerie

Adapter le nombre de médias à la complexité. Une trame recommandée : hero produit vrai, usage, bénéfice, détail/texture, dimensions, contenu du colis, preuve ou comparaison. Chaque slide doit répondre à une question ; éviter sept variations décoratives identiques.

## Confiance réelle

Afficher identité du vendeur, contact fonctionnel, paiement, livraison, retours et politiques cohérentes. Ne pas afficher avis, compteurs d'achat, logos média, certifications, badges ou économies non prouvés.

## UX et accessibilité

- priorité mobile ;
- cible tactile suffisante, contraste et focus clavier ;
- labels explicites et erreurs de formulaire compréhensibles ;
- variantes sélectionnables sans ambiguïté ;
- panier et checkout sans surprise de coût ;
- aucune popup bloquante avant compréhension ;
- images optimisées, dimensions réservées, lazy-load hors écran ;
- navigation stable et retour arrière fiable.

## QA rendue

Ne pas valider à partir du code seul. Vérifier sur le storefront réellement rendu :

- mobile étroit et bureau ;
- variante → prix/image/stock ;
- ajout panier et modification quantité ;
- frais/délais affichés ;
- liens politiques/contact ;
- checkout test jusqu'à l'étape autorisée ;
- erreurs console/réseau significatives ;
- performance et éléments qui sautent au chargement.

## Copywriting

Transformer les faits en bénéfices sans les dépasser. Chaque promesse doit pouvoir répondre à « quelle caractéristique ou preuve permet de l'affirmer ? ». Traiter les objections observées, pas une liste générique.

## Critères de passage

- aucune contradiction catalogue/feed/politiques ;
- en mode `catalogue-volume`, au moins 200 produits distincts admissibles sont vérifiés et correctement distribués ;
- parcours mobile complet vérifié ;
- coûts et conditions importants visibles avant achat ;
- preuve honnête ;
- performance et accessibilité sans blocage critique ;
- capture ou rapport de QA daté.
