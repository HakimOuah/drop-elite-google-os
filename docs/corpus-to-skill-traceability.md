# Traçabilité du corpus vers le skill global

Ce document explique comment les notions du corpus ont été transformées, corrigées ou complétées dans `creer-boutique-niche-google`. Les sources de formation sont `ENSEIGNE_A_VERIFIER` tant qu'elles ne sont pas corroborées.

La relecture exhaustive au niveau texte est détaillée dans `corpus/derived/coach-source-index.md`. Les lacunes curriculaires et matérielles sont dans `docs/corpus-gap-audit.md`. Une notion absente de ces sources mais apportée par un autre skill doit être étiquetée `AJOUT_SYSTEME`.

| Porte | Sources de formation dominantes | Notions conservées | Ajouts/corrections du système |
|---|---|---|---|
| 0. Contexte | portefeuille `244603899`, suivis `245994245`, `245994758`, `249143021` | regarder les résultats et optimiser dans le temps | post-mortem multi-source, tracking avant diagnostic, focus sur un goulot et registre anti-répétition |
| 1. Marché/client | `231587893`, `231587930`, `231587882`, `231588530`, `231588620`, `231663659`, `231663690` | choix de niche, demande, concurrence, architecture assez profonde, heuristique 1 000/150 | nettoyage d'intention, VOC/JTBD sourcé, droit de gagner, risques fatals et seuils projet catalogue-volume |
| 2. Économie/offre | `232117442`, `232117523`, `232117816`, `232117915`, `234186329` | catalogue cohérent, coût d'intégration, CPC et rentabilité | vérité par variante, coût livré, marge contributive complète, retours/chargebacks, trésorerie et fournisseur de secours |
| 3. SEO | `231663788`, `231663822`, `234180398`, `234333488/499/543/561/580/583`, `237446074` et 3 YouTube | synergie SEO/SEA, architecture, catégories, briefs, blog, maillage | intention unique par URL, cannibalisation, facettes, données structurées, Search Console, contenu utile et règles antispam actuelles |
| 4. Storefront | `232117523`, `232119122`, `237446074`, `306109499` + gist | fiche produit, performance, mise en œuvre Shopify/IA et sobriété pré-GMC | contrat de vérité catalogue, états `GMC_READY`/`GROWTH_MARKETING`, mobile/accessibilité, QA rendue, preuve réelle et séparation génération visuelle/écriture live |
| 5. GMC/mesure | `239787221`, `239791167`, `239965951`, `240313004`, `240359870`, `262936735`, checklist et Fast-Track | cohérence identité/politiques/feed, version sobre pour validation puis ajout marketing, tracking propre | progression en deux états, matrice d'invariants, priorité aux politiques officielles, cohérence page/feed/schema/checkout, transaction ID, valeur/devise et frontière précise avec l'évasion |
| 6. Test Ads | `239785633`, `240591206`, `246208721` | prérequis, choix de mots-clés, lancement contrôlé | carte de test, plafond de perte, campagne choisie selon l'hypothèse, achat prouvé avant dépense et stop rules |
| 7. Optimisation | `240715193`, `245994245`, `245994758`, `249143021`, `249178958` | KPI, revue périodique, segmentation selon les données | réconciliation backend/Ads/analytics, diagnostic en cascade et une variable matérielle par expérience |
| 8. Scaling | `249178958`, `246485074`, `246532995`, document Scaling | scaling par étapes, tracking propre, AOV/CRO et retour au palier précédent | contribution après tous coûts, scénarios, cash, capacité fournisseur/SAV et aucun seuil universel |

## Décision catalogue-volume du 2026-08-08

Les transcriptions enseignent `> 1 000` pour les premiers mots-clés de catégories et `> 150` pour la longue traîne (`vimeo-caption-231588620` [00:05:29–00:05:57]). Elles montrent aussi une catégorie à 450 acceptée (`vimeo-caption-231663822` [00:03:47–00:04:04]), tandis que `hhPBbZZ7qHQ` [00:02:15–00:02:40] refuse un seuil universel pour la catégorie principale.

Hakim fixe donc, pour le mode `catalogue-volume`, la règle opératoire suivante : plancher boutique de 30 000 recherches mensuelles commerciales nettoyées, 40 000+ en zone de confort, 1 000+ pour une collection cœur, 500+ pour une collection secondaire avec tolérance d'environ ±200, et au moins 200 produits distincts au lancement. Le low ticket est autorisé sans plancher de 150 €, sous réserve de l'économie réelle par commande.

Cette règle est `DECISION_PROJET`, pas une exigence officielle Google. Les volumes doivent être France, datés, dédupliqués par intention et nettoyés. Le pipeline historique high-ticket de `chasse-clusters-codex` reste distinct ; en mode catalogue-volume, ses mesures peuvent être utilisées mais pas ses anciens verdicts de prix.

## Gate V3 catalogue et sourcing du 2026-08-08

La preuve de demande est portée par la niche et ses collections, pas par un
volume positif exigé sur chaque PDP. `vimeo-caption-232117442`
[00:01:49–00:02:34] enseigne de remplir une sous-catégorie avec 10–20 produits
et de laisser le marché choisir ; `vimeo-caption-246208721`
[00:08:02–00:10:17] conserve des formulations à volume zéro lorsqu'elles
précisent la collection. L'analyse concurrentielle (`231663690`) sert à trouver
les catégories, requêtes et références utiles, sans imposer un jumeau par fiche.

Le système ajoute `catalogue-sourcing-gate-v3.md` : phase 2 obligatoire avant
sourcing, 200 produits sur la boutique entière, concept distinct, listing réel,
mot-clé descriptif pouvant valoir zéro, équivalent concurrent facultatif et
revue humaine. L'ordre 80/20 de constitution des sous-catégories est une
`DECISION_PROJET`; les timecodes restent `ENSEIGNE_A_VERIFIER`.

## Ce qui a été retenu des documents GMC

- identité et coordonnées réelles ;
- cohérence entre footer, politiques, checkout, feed et compte ;
- pages fonctionnelles, absence de faux avis/urgence/claims ;
- construction d'un état `GMC_READY` complet et sobre ;
- ajout post-approbation d'une couche `GROWTH_MARKETING` factuelle et contrôlée ;
- baseline, matrice d'invariants, QA et rollback pour la transition ;
- correction de la cause avant une demande d'examen ;
- surveillance après approbation ;
- aucune garantie d'approbation.

## Ce qui reste une hypothèse d'auteur

- fenêtres fixes de 48 heures, 7 jours ou 30 jours ;
- score PageSpeed minimal de 65 comme règle GMC ;
- âge de domaine de 30 jours ;
- minimum universel de cinq produits par collection ;
- taux Trustpilot de 3,0 comme seuil dur ;
- délais d'examen fixes ;
- wording strictement identique « ligne par ligne » dans tous les champs ;
- supériorité universelle d'une application ou d'un flux précis.

Ces éléments peuvent orienter un audit, mais doivent être vérifiés auprès de Google et du compte courant.

## Décision GMC en deux états du 2026-08-08

Hakim demande de conserver la méthode de présentation d'une boutique sobre pour la validation GMC, puis d'ajout du marketing après approbation. Le système sait désormais construire `GMC_READY`, `GROWTH_MARKETING` et `TRANSITION_GMC_TO_GROWTH`.

La frontière retenue n'est pas « avant/après approbation », mais le comportement : la transition est acceptée si la même version est publiée pour tous, si les deux états sont des commerces réels et si les informations déterminantes restent exactes. Sont invariants : identité/contact, produit/variante, prix/stock, livraison/retours, feed/schema/checkout, tracking et consentement. Les modules marketing sont versionnés, prouvés et réversibles.

## Ce qui reste exclu

- proxy/anti-detect comme voie d'approbation ;
- adresses, téléphones ou identités artificiellement « uniques » ;
- échauffement de Gmail présenté comme exigence Google ;
- isolation destinée à masquer des liens ou à fuir une suspension ;
- contenu différent selon le contrôleur ou restauration consciente d'un claim trompeur/non prouvé ;
- toute garantie, shortcut ou manipulation du système.

Une entreprise peut légitimement séparer ses opérations et ses accès pour la sécurité. Elle ne doit pas fabriquer des identités ou dissimuler un lien pertinent.

## Correction du framework de scaling

Le document définit une journée verte par `revenu - ad spend` et nomme ce résultat « net profitable ». Cette définition omet produit, livraison, paiements, remises, taxes, retours, chargebacks et SAV. Le skill remplace donc cette métrique par :

```text
marge contributive après ads
= CA net
- produit et livraison
- frais variables
- retours/remboursements attendus
- publicité
```

La règle « deux jours verts/rouges » et l'ajustement de 20–30 % sont conservés comme une discipline enseignée, pas comme règle universelle. Les paliers dépendent du volume, du cycle de conversion, de la variabilité, de la trésorerie et de la capacité opérationnelle.

## Adaptation des politiques

Les modèles anglais fournis sont une base thématique, pas un texte publiable en France. Les versions `policies-fr/` ajoutent les variables réelles, la rétractation, les garanties légales, la médiation, l'information RGPD/cookies et retirent les exclusions générales de responsabilité ou promesses non prouvées. Une validation juridique reste nécessaire.

## Notions ajoutées au-delà de la formation

- autorisations d'action A/B/C et exécuteur réel ;
- actualité datée des règles ;
- registre de preuve et contradictions ;
- recherche client brute et alternatives ;
- trésorerie et capacité de service ;
- accessibilité, performance perçue et QA mobile ;
- déduplication des conversions ;
- causalité expérimentale ;
- coût d'attention et discipline portfolio ;
- sauvegarde reproductible, manifestes SHA-256 et GitHub comme source de vérité.

## Frontière coach après relecture exhaustive

Le coach peut restituer la formation avec un routage précis sur niche, architecture, catalogue, SEO on-site, GMC, Shopping, optimisation et scaling par segmentation. Il doit répondre `MANQUANT_MODULE` pour l'email marketing, le SEO off-site complet, l'affiliation, le branding complet, la délégation globale, le module de valorisation et les calculateurs mentionnés mais absents.

La progression `GMC_READY` → `GROWTH_MARKETING` est conservée et opérationnalisée. Restent `EXCLU_SYSTEME` le contenu différencié pour le contrôleur, les claims trompeurs rétablis après validation, l'anti-ban, l'anti-detect destiné à masquer des liens, l'identité artificielle multi-boutiques, la valeur de conversion inventée et le spinning sans valeur.
