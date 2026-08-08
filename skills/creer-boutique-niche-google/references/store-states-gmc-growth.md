# Deux états de boutique — `GMC_READY` et `GROWTH_MARKETING`

## Décision projet

La Méthode Kraken enseigne de faire valider un socle de boutique sobre, puis d'ajouter la couche marketing une fois le Merchant Center validé. Le système conserve cette méthode et doit savoir construire les deux états, soit successivement sur une même boutique, soit directement dans un thème de développement.

Cette progression n'est pas assimilée automatiquement à du cloaking : le même état doit être servi à Google et aux clients au même moment. La couche ajoutée après validation doit rester exacte, justifiable et cohérente avec le feed, les données structurées, le checkout et les politiques.

Sources de formation prioritaires :

- `vimeo-caption-240313004` [00:19:10–00:21:15] — contrôle des promesses, passage du flux, stabilité pendant la revue puis ajout de la couche marketing ;
- `vimeo-caption-262936735` [01:44:56–01:46:38] — réduction des textes marketing lors d'une demande d'examen ;
- `vimeo-caption-239965951` — audit pré-GMC de la cohérence du commerce.

Statut : méthode `ENSEIGNE_A_VERIFIER`, adoptée comme `DECISION_PROJET` par Hakim le 2026-08-08, avec les frontières ci-dessous.

## Les deux livrables

### État A — `GMC_READY`

Boutique commerciale complète, achetable, identifiable et sobre. Elle ne doit pas être une coquille vide ni un décor temporaire.

Elle contient au minimum :

- identité réelle de l'entreprise, domaine, contact et support fonctionnels ;
- catalogue réellement sourcé, prix, stock, variantes, images et délais exacts ;
- navigation, collections, recherche et parcours mobile utilisables ;
- pages produit suffisamment descriptives pour comprendre et acheter ;
- panier et checkout fonctionnels, sans frais ni conditions surprises ;
- livraison, retours, rétractation, paiements, CGV, confidentialité, cookies et mentions adaptées aux faits ;
- feed, données structurées et pages cohérents ;
- tracking achat testable avec valeur, devise et identifiant de transaction ;
- design de marque cohérent, mais sans surcouche promotionnelle inutile à l'examen.

La sobriété porte principalement sur la pression marketing : pas de promesse difficile à justifier, de promotion ambiguë, de preuve sociale non vérifiée, d'urgence permanente ou de module expérimental susceptible de créer une incohérence.

### État B — `GROWTH_MARKETING`

La boutique conserve intégralement le contrat de vérité de `GMC_READY` et ajoute une couche de persuasion, de merchandising et de conversion.

Cette couche peut inclure, si les preuves et l'économie le permettent :

- proposition de valeur et hero plus travaillés ;
- storytelling de marque et mise en scène des usages ;
- bénéfices produit reliés à des caractéristiques vérifiées ;
- merchandising de collections, best-sellers et recommandations ;
- bundles, paliers, cadeaux et seuil de livraison réellement configurés ;
- promotions datées, prix barrés justifiables et compte à rebours réellement expirant ;
- cross-sell, upsell et post-purchase cohérents avec le produit ;
- avis, UGC, témoignages ou logos uniquement lorsqu'ils sont réels et attribuables ;
- FAQ d'objections, comparatifs factuels et démonstrations ;
- capture email et popups avec consentement et règles de fréquence ;
- contenus SEO enrichis, originaux et utiles ;
- expériences CRO avec baseline, métrique, date et rollback.

`GROWTH_MARKETING` n'est pas un relâchement de la conformité. Il doit pouvoir être contrôlé à nouveau sans nécessiter de cacher un élément trompeur.

## Contrat d'invariants

Ces éléments ne changent pas entre les deux états sans nouvelle preuve, synchronisation et autorisation :

| Invariant | Sources à réconcilier | Preuve attendue |
|---|---|---|
| entreprise, adresse et contact | site, politiques, compte, facturation | documents et contact testés |
| domaine et vendeur réel | domaine, Merchant Center, checkout | propriété et identité cohérentes |
| produit et variante | fournisseur, PDP, feed, schema | SKU/variante et échantillon de contrôle |
| prix, devise et disponibilité | PDP, collection, feed, schema, checkout | comparaison automatisée ou rapport daté |
| livraison et frais | PDP, politiques, feed, checkout | route France réelle et commande test |
| retours et remboursement | politiques, FAQ, checkout, support | procédure réellement exécutable |
| identifiants produit | fabricant, feed, données structurées | GTIN/MPN/brand certains ou champ omis |
| promesse factuelle | source produit, test, certification | dossier de preuve de claim |
| achat et mesure | checkout, backend, Ads/analytics | transaction de test réconciliée |
| consentement et données | CMP, tags, politiques | scan et parcours de consentement |

Une modification d'un invariant déclenche un retour aux portes 2, 4 ou 5. L'approbation antérieure ne vaut pas validation automatique de la nouvelle information.

## Matrice de la couche marketing

| Composant | `GMC_READY` | `GROWTH_MARKETING` | Condition de bascule |
|---|---|---|---|
| hero | identité, catégorie et bénéfice sobre | angle, usage, preuve et CTA enrichis | aucune promesse non soutenue |
| bannière promotionnelle | absente ou information simple | offre datée et reliée au backend | conditions, stock et dates exacts |
| prix barré | seulement si justifiable | peut être davantage mis en avant | prix de référence démontrable |
| compte à rebours | absent | autorisé pour une échéance réelle | expiration serveur et retrait automatique |
| preuve sociale | uniquement preuve vérifiée | avis/UGC mieux merchandisés | provenance et droit d'usage |
| bénéfices produit | faits essentiels | copywriting plus persuasif | chaîne caractéristique → bénéfice → preuve |
| bundles/upsells | optionnels | activés selon marge et compatibilité | règles backend et panier testés |
| seuil de livraison | affichage factuel | progression et relances UX | seuil identique au checkout/feed |
| popup email | généralement désactivée | activée avec ciblage et fréquence | consentement, fermeture et mobile QA |
| contenu SEO | minimum utile et original | enrichissement par intention | pas de texte généré sans valeur |
| retargeting | tags vérifiés sans pression commerciale | audiences/campagnes autorisées | consentement et exclusion adéquats |

## Construction de `GMC_READY`

1. **Fixer l'état cible** dans `templates/project-intake.md`.
2. **Créer un thème de développement ou une sauvegarde** ; ne pas modifier le live sans autorisation de classe C.
3. **Valider la vérité produit et l'économie** aux portes 2 et 3.
4. **Construire le socle storefront** selon la porte 4 : navigation, collections, PDP, panier, checkout et pages statiques.
5. **Renseigner les politiques** depuis les faits de l'entreprise ; ne jamais publier les placeholders.
6. **Désactiver les modules promotionnels non nécessaires** par configuration réversible, pas par suppression destructrice.
7. **Réconcilier page, feed, schema et checkout** sur les invariants.
8. **Tester l'achat et le contact** ainsi que la version mobile et bureau réellement rendue.
9. **Capturer la baseline** : URL, thème/version, horodatage, captures, export des réglages et hash Git si disponible.
10. **Soumettre ou demander l'examen** uniquement après autorisation explicite.

## Construction de `GROWTH_MARKETING`

1. Partir d'une baseline `GMC_READY` validée ou d'un thème de développement équivalent.
2. Créer un registre des modules marketing à activer ; un module = une hypothèse, une preuve et un rollback.
3. Construire d'abord dans un environnement non publié.
4. Vérifier chaque claim, promotion, prix de comparaison, témoignage et élément d'urgence.
5. Synchroniser immédiatement tout changement qui touche prix, stock, livraison, retours ou produit dans le feed, le schema et le checkout.
6. Exécuter la QA mobile, bureau, panier, checkout, pages légales, données structurées, tags et diagnostics.
7. Comparer automatiquement ou manuellement les invariants avant/après.
8. Publier seulement avec autorisation de classe C et journaliser l'exécuteur réel.
9. Surveiller après propagation : erreurs storefront, diagnostics GMC, produits refusés, tracking, performance et retours clients.
10. En cas d'incident, désactiver le module fautif ou restaurer la baseline ; corriger la cause avant une nouvelle demande d'examen.

## Trois modes de réalisation

Le coach doit savoir produire :

1. **`BUILD_GMC_READY`** — construire uniquement l'état sobre prêt à examiner ;
2. **`BUILD_GROWTH_MARKETING`** — construire directement l'état marketing lorsque le compte n'est pas en phase de revue, tout en respectant tous les invariants ;
3. **`TRANSITION_GMC_TO_GROWTH`** — préparer les deux thèmes/configurations et effectuer une bascule contrôlée après validation.

Pour chaque mode, fournir : inventaire des pages, composants activés, variables de contenu, preuves, QA, autorisation, version publiée et rollback.

## Ce qui distingue la progression du cloaking

La progression est acceptée par le système lorsque :

- tous les visiteurs et robots voient le même état publié ;
- la version `GMC_READY` est une vraie boutique achetable ;
- la version `GROWTH_MARKETING` reste conforme et factuelle ;
- les changements sont publiés normalement, tracés et vérifiables ;
- aucune relation, identité, condition commerciale ou violation n'est dissimulée.

Reste `EXCLU_SYSTEME` :

- servir un contenu différent selon user-agent, IP, provenance ou identité du contrôleur ;
- restaurer sciemment une affirmation trompeuse, interdite ou impossible à prouver ;
- retirer les coordonnées, politiques ou conditions réelles après approbation ;
- créer une incohérence volontaire entre site, feed, schema et checkout ;
- utiliser la bascule pour fuir une suspension ou masquer la cause d'un refus.

## Preuves de fin

Une construction ou transition n'est terminée que si `templates/gmc-growth-transition.md` contient :

- état initial et état final ;
- identifiant de version ou thème ;
- matrice des invariants validée ;
- captures mobile et bureau ;
- parcours panier/checkout testé ;
- contrôle feed/schema/politiques ;
- modules marketing et preuves associés ;
- autorisation, exécuteur, date et rollback ;
- résultat réellement observé après publication.
