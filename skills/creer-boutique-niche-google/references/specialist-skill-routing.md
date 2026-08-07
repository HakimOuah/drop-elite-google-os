# Routage des skills spécialisés

Les 11 skills retenus sont vendoriés sous `vendor/agent-skills/` pour restauration privée. Ils ne doivent pas tous être exécutés à chaque projet. Appeler le minimum nécessaire au goulot actuel.

| Skill | Porte principale | Entrées obligatoires | Sortie attendue | Ne pas l'utiliser pour |
|---|---|---|---|---|
| `customer-research` | 1 | segments réels, sources clients | VOC, JTBD, objections sourcées | inventer un persona |
| `competitor-profiling` | 1 | URLs et date | snapshots bruts + profils comparables | déduire un fournisseur exact ou accepter les claims concurrents |
| `offers` | 2 | produit vrai, économie, VOC | architecture d'offre réalisable | créer une fausse urgence ou garantie inexécutable |
| `marketing-psychology` | 2, 4, 7 | comportement cible, contexte, preuve | hypothèses éthiques à tester | dark patterns, preuve sociale fictive, defaults trompeurs |
| `brandkit` | entre 2 et 4 | positionnement validé, audience, vérité produit | système visuel cohérent et applications | choisir la niche ou promettre un attribut absent |
| `copywriting` | 4 | objectif de page, audience, offre, trafic | accueil/landing/about clairs | descriptions catalogue à grande échelle sans vérité produit |
| `ecommerce-copywriting` | 3, 4 | mots-clés, attributs, objections | collections, PDP et méta | inventer bénéfices, avis ou spécifications |
| `storefront-best-practices` | 4, 5 | catalogue, architecture et policies | UI commerce accessible et QA | décider de la viabilité économique |
| `cro` | 7 | baseline, funnel, trafic suffisant | diagnostic + expérience | refaire un site sans diagnostic |
| `ecommerce-growth-strategy` | 0, 2, 8 | CAC, AOV, marge, capacité | arbitrage croissance/économie | utiliser un ROAS brut comme profit |
| `marketing-plan` | 0, 8 / transverse | stratégie validée, équipe, budget, canaux | roadmap, owners, métriques | remplacer les portes produit/GMC ou produire 12 mois de tactiques sans données |

## Séquence recommandée

```text
customer-research + competitor-profiling
            ↓
      offers + economics
            ↓
          brandkit
            ↓
copywriting + ecommerce-copywriting
            ↓
 storefront-best-practices
            ↓
       Ads/SEO test
            ↓
 cro + ecommerce-growth-strategy
            ↓
 marketing-plan si coordination multi-canal requise
```

`marketing-psychology` traverse l'offre, le copywriting et la CRO, mais chaque application doit être honnête, réversible et testable.

## Adaptations e-commerce nécessaires

Certains skills génériques ont été écrits pour SaaS ou supposent d'autres outils. Lors de leur usage :

- remplacer ARR/ARPC par les métriques e-commerce pertinentes ;
- intégrer retours, coûts produit, livraison, paiement, taxes et trésorerie ;
- remplacer les moyennes génériques par les données de la boutique ;
- ne pas appeler un outil externe qui n'est pas disponible ; utiliser une source primaire ou marquer `MANQUANT` ;
- appliquer les autorisations de `action-authorization.md` ;
- sauvegarder les preuves brutes datées dans le dépôt opérationnel de la boutique, pas dans le corpus de formation.

## Garde-fous éthiques communs

- preuve sociale uniquement observée et attribuable ;
- rareté/urgence uniquement vraie et synchronisée avec le stock/offre ;
- prix de comparaison justifiable ;
- pas de case marketing précochée lorsqu'un consentement positif est requis ;
- pas de dissimulation de coût ou d'information déterminante ;
- la psychologie sert à réduire l'incertitude et la friction, pas à empêcher un choix libre.
