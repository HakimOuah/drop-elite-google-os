# Porte 3 — Architecture SEO

## Décision

Concevoir une architecture qui aide les utilisateurs et les moteurs à comprendre le catalogue, sans pages artificielles ni cannibalisation.

## Entrées

- clusters commerciaux nettoyés ;
- vocabulaire client ;
- catalogue et attributs produits vrais ;
- saisonnalité ;
- carte des volumes dédupliqués par collection et total boutique lorsque le mode `catalogue-volume` est sélectionné ;
- capacités réelles de production de contenu ;
- contraintes de variantes, filtres et collections.

## Carte intention → page

Attribuer un rôle unique à chaque URL :

- accueil : promesse de la niche et chemins principaux ;
- collection : intention catégorie/comparaison ;
- produit : intention transactionnelle précise ;
- guide : problème, choix, usage, entretien ou comparaison ;
- politique/service : confiance et conditions ;
- page de marque/modèle uniquement si contenu et demande justifient une URL.

Une même intention principale ne doit pas être répartie sur plusieurs pages quasi identiques. Fusionner, canonicaliser ou `noindex` les facettes sans valeur.

## Volumes et URLs en mode `catalogue-volume`

- total commercial nettoyé de la boutique : plancher 30 000 recherches mensuelles France, 40 000+ en zone de confort ;
- collection cœur : cible 1 000+, bande de revue 800–999 ;
- collection secondaire : cible 500+, bande de revue 300–499 ;
- une collection sous sa bande de revue doit être fusionnée, gardée pour le merchandising sans objectif SEO autonome, ou justifiée par une preuve commerciale spécifique ;
- aucun volume minimum n'est imposé à une fiche produit : elle doit correspondre à un produit vrai et à une intention transactionnelle précise, sans dupliquer une autre URL ;
- la somme boutique ne compte chaque intention commerciale qu'une seule fois, même si plusieurs synonymes ou pages pourraient la revendiquer.

## Architecture

- navigation courte et compréhensible ;
- URLs lisibles et stables ;
- fil d'Ariane ;
- maillage contextuel entre guides, collections et produits ;
- profondeur limitée pour les pages commerciales ;
- sitemap et robots cohérents ;
- absence de liens internes vers redirections/404 ;
- pagination et filtres maîtrisés.

## On-page fondé sur la vérité

Chaque page doit posséder un objectif et une valeur propre : titre descriptif, H1 cohérent, introduction utile, attributs et réponses réelles, médias alt pertinents, FAQ fondée sur les questions observées. Éviter le bourrage de mots-clés et les descriptions génériques du fournisseur.

## Produit et données structurées

Le prix, la disponibilité, la variante, le SKU/GTIN/MPN lorsqu'ils existent, la livraison et les retours doivent être cohérents entre page, données structurées et feed. Ne jamais inventer un GTIN ou utiliser la boutique comme marque si elle ne fabrique pas le produit.

## Qualité et indexation

Avant publication :

- Googlebot non bloqué sur les pages visées ;
- réponse HTTP correcte ;
- contenu indexable rendu ;
- canonical attendu ;
- mobile utilisable ;
- aucun cloaking ni contenu conçu seulement pour manipuler le classement ;
- pages légales et panier volontairement gérés selon leur utilité d'indexation.

L'indexation et le classement ne sont jamais garantis.

## Plan de contenu

Prioriser par intersection : demande, proximité du revenu, avantage informationnel et capacité à produire mieux que l'existant. Pour chaque contenu : intention, angle, preuve, page cible, liens entrants/sortants, CTA et métrique.

Créer moins de pages mais plus utiles. Les contenus IA doivent être édités, fact-checkés, reliés aux faits produit et non multipliés pour occuper artificiellement les SERP.

## Mesure

Prévoir Search Console et analytics : indexation, requêtes, impressions, CTR, position, landing pages, engagement commercial et revenu assisté. Le trafic sans pertinence ni conversion n'est pas un succès.

## Critères de passage

- chaque cluster important a une URL cible unique ;
- en mode `catalogue-volume`, total boutique et seuils de collections sont calculés sans double comptage, et chaque exception est explicitée ;
- la navigation et le maillage sont spécifiés ;
- les facettes/variantes ne créent pas de duplication incontrôlée ;
- les données structurées pourront refléter les faits ;
- le plan de contenu est soutenable et mesurable.
