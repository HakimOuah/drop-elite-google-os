# Architecture de connaissance

## Les quatre couches

```text
Sources brutes autorisées
        ↓ normalisation sans altération
Corpus canonique + dérivés recherchables
        ↓ synthèse avec statut de preuve
Skills, checklists et modèles
        ↓ application au contexte réel
Dossier de décision propre à chaque boutique
```

### 1. Sources brutes

Les VTT, PDF, métadonnées YouTube et médias autorisés sont conservés avec empreinte SHA-256. Une source brute n'est pas éditée après ingestion.

### 2. Corpus canonique

Les dérivés retirent les horodatages et doublons de sous-titres pour faciliter la recherche. Ils ne remplacent jamais la source brute lorsqu'une citation ou nuance doit être vérifiée.

### 3. Système de skills

Le skill global orchestre le parcours et charge uniquement les références requises par la porte courante. Les skills spécialisés restent responsables de leur domaine : recherche produit, recherche client, offre, copywriting, storefront, CRO, ingestion.

### 4. Preuves boutique

Chaque boutique obtient son propre dossier de travail. Les résultats d'une boutique ne sont pas transposés comme faits à une autre.

## Statuts de connaissance

| Statut | Sens | Usage permis |
|---|---|---|
| `OFFICIEL_ACTUEL` | source primaire officielle vérifiée et datée | exigence ou recommandation avec URL et date |
| `ENSEIGNE_A_VERIFIER` | proposition issue de la formation | hypothèse, checklist ou expérience à confronter |
| `OBSERVE_PROJET` | donnée ou état prouvé dans le projet courant | décision locale avec preuve datée |
| `HYPOTHESE` | raisonnement plausible mais non démontré | test explicite, jamais affirmation |
| `MANQUANT` | donnée nécessaire absente | blocage ou collecte à faire |
| `CONTREDIT` | incompatible avec une preuve plus forte | ne pas appliquer ; documenter l'écart |

## Règle de conflit

1. loi/réglementation applicable et politique officielle actuelle ;
2. vérité produit, données de plateforme et preuves du projet ;
3. méthode enseignée ;
4. opinion ou hypothèse.

Une méthode de formation peut rester utile tout en étant classée `ENSEIGNE_A_VERIFIER`. Elle n'est supprimée que si elle est illégale, trompeuse, dangereuse ou contredite.
