# Gate V3 — catalogue et sourcing après validation de la niche

## Rôle

Ce gate remplace le contrôle V2 qui exigeait, pour chaque produit, un jumeau
concurrent et un volume de recherche strictement positif. Il s'applique au mode
`catalogue-volume` et sépare la preuve du marché, portée par les collections, de
la sélection des produits qui les alimentent.

Il ne remplace ni la porte 2 (vérité fournisseur et économie), ni la porte 4
(catalogue publiable et QA). Il décide seulement si une niche validée peut
passer de l'architecture à la constitution de son catalogue.

## Précondition non négociable

Le sourcing catalogue ne commence qu'après cette séquence :

1. mesure express France et nettoyage des intentions ;
2. lecture SERP et prix ;
3. étude concurrentielle profonde ;
4. verdict explicite `GO` ou `GO_CONDITIONNEL` dont les conditions autorisent le sourcing ;
5. architecture chiffrée ;
6. sourcing catalogue.

Un verdict `STOP` ou `SUSPENDU_PHASE_2` bloque l'architecture et le sourcing.
Une niche arrêtée ne se rouvre que par une nouvelle qualification documentée,
jamais parce qu'un listing fournisseur semble intéressant.

## Niveau collection — preuve du marché

Une collection peut recevoir des produits lorsque :

- son intention commerciale France est mesurée, datée et dédupliquée ;
- la boutique atteint 30 000 recherches commerciales nettoyées, avec 40 000+
  comme zone de confort (`DECISION_PROJET`) ;
- une collection cœur vise 1 000+ recherches et une collection secondaire
  500+, avec la bande de revue d'environ ±200 définie par Hakim ;
- la SERP, les concurrents et les prix prouvent un marché payant et permettent
  de formuler un droit de gagner honnête ;
- le prix moyen et le CPC sont relevés sur la même intention ; le ratio
  `prix moyen / CPC` vaut au moins 100 et vise 150–200, comme heuristique
  `ENSEIGNE_A_VERIFIER`, jamais comme garantie de rentabilité ;
- une sonde de profondeur fournisseur montre que la famille peut réellement
  contribuer au catalogue de 200 produits de la boutique.

Les seuils `> 1 000` pour les premiers termes et `> 150` en fin de longue
traîne sont enseignés dans `vimeo-caption-231588620` [00:05:41–00:05:57]. Les
seuils 30 000 / 40 000 / 500 ±200 sont des décisions de projet et restent
étiquetés comme tels.

## Niveau produit — entrée dans une collection validée

Un produit candidat est admissible au gate V3 si :

1. il répond clairement à l'intention d'une collection déjà validée ;
2. il représente un concept fonctionnel distinct, pas une simple couleur,
   taille, quantité, marque ou référence de modèle ;
3. un listing fournisseur réel, pertinent et suffisamment stable est observé
   avec au minimum un identifiant ou une URL, un titre et un prix ;
4. son mot-clé PDP est descriptif, spécifique et fidèle au produit ; son volume
   peut être positif ou égal à zéro et ne doit jamais être inventé ;
5. une revue humaine confirme le couple produit ↔ collection ↔ listing.

La présence d'un équivalent chez un concurrent est un **bonus de confiance**,
pas une condition obligatoire. Les concurrents servent à découvrir les
catégories, les requêtes, les gammes, les prix et les produits déjà demandés ;
ils ne doivent pas devenir une liste fermée qui limite artificiellement le
catalogue.

Le listing observé à ce stade reste `FOURNISSEUR_CANDIDAT`. Variante exacte,
stock, coût rendu France, délai, contenu du colis, conformité et stabilité sont
encore à prouver à la porte 2 avant publication ou import.

## Profondeur et ordre de sélection

- viser **200 produits distincts au total sur la boutique**, et non 200 dans
  chaque micro-niche ;
- placer **10 à 20 produits par sous-catégorie** au lancement, puis laisser la
  data Google et les ventes révéler les meilleures références ;
- lors de l'ouverture ultérieure d'une catégorie, démarrer autour de 10
  produits ; ajouter au moins 20 produits par mois à l'échelle de la boutique
  lorsque l'exploitation le permet.

Pour composer une sous-catégorie, utiliser cet ordre de priorité
`DECISION_PROJET`. Les fourchettes guident une sélection de 10–20 produits et
ne sont pas des quotas additifs à remplir mécaniquement :

1. 5–8 best-sellers fournisseur pertinents ;
2. 3–5 équivalents ou fonctions observés chez les concurrents ;
3. 3–5 références qui construisent une échelle de prix/usage ;
4. 2–4 produits descriptifs ou longue traîne cohérents.

Chaque ajout doit apporter une fonction, un usage, une matière, un mécanisme ou
un niveau de gamme réellement distinct. Les variantes décoratives ne gonflent
pas le compteur.

## Sources et statut

- `vimeo-caption-231588530` [00:00:11–00:00:56] : 200 produits au lancement
  pour couvrir plusieurs catégories et laisser de la matière à Google ;
- `vimeo-caption-231588530` [00:02:30–00:03:46] : 20 ajouts mensuels, environ
  10 produits à l'ouverture d'une catégorie et sélection par la data ;
- `vimeo-caption-232117442` [00:01:49–00:02:34] : focus catégorie/sous-catégorie,
  10–20 produits et choix laissé au marché ;
- `vimeo-caption-231663690` [00:00:42–00:00:50] et [00:07:52–00:07:59] : la
  concurrence aide à découvrir catégories et mots-clés ;
- `vimeo-caption-246208721` [00:08:02–00:08:11] et [00:09:54–00:10:17] : des
  mots-clés à volume zéro peuvent rester pertinents lorsqu'ils précisent la
  collection ;
- `vimeo-caption-234186329` [00:01:21–00:03:29] : prix moyen, CPC et ratios
  100/150/200.

Les enseignements ci-dessus restent `ENSEIGNE_A_VERIFIER`. La hiérarchie
80/20, la revue humaine, le statut `FOURNISSEUR_CANDIDAT` et l'interdiction de
sourcer avant la phase 2 sont des `DECISION_PROJET` destinées à rendre la
méthode auditable et sûre.
