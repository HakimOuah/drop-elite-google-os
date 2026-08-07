---
name: derouler-strategie-drop-elite
description: Rechercher dans le corpus privé Drop Elite et transformer les leçons en plans, audits, checklists ou décisions e-commerce sourcés, en reliant chaque recommandation à un VTT, une page PDF ou une fiche, puis en la confrontant aux preuves actuelles. Utiliser quand Hakim demande ce que la formation enseigne ou veut appliquer la stratégie à un projet.
---

# Dérouler la stratégie Drop Elite

## Préflight de couverture

1. Lire `references/corpus-map.md` et `references/evidence-policy.md`.
2. Lire `corpus/manifest.json` et `corpus/CATALOGUE.md`.
3. Chercher les notions avec `scripts/search_corpus.py`.
4. Ouvrir les sources VTT/PDF ou fiches exactes lorsqu'un seuil, une séquence ou une citation influence la décision.
5. Si la procédure requise n'est pas présente, répondre `MANQUANT_MODULE` au lieu de compléter silencieusement.

## Deux sorties distinctes

### « Ce que la formation enseigne »

Restituer avec `source_id [timecode]` ou `document p. X`, statut `ENSEIGNE_A_VERIFIER`, contexte et limites de transcription.

### « Ce qu'il faut faire maintenant »

Confronter l'enseignement aux sources officielles actuelles, aux faits produit et aux données de la boutique. Router vers `creer-boutique-niche-google` pour les portes, calculs, autorisations et décisions.

Ne jamais transformer automatiquement un enseignement en règle Google, donnée de marché ou fait propre au projet.

## Workflow

1. Reformuler l'objectif et le périmètre.
2. Construire la séquence enseignée avec références exactes.
3. Extraire les dépendances, préconditions et seuils annoncés.
4. Classer chaque élément avec le modèle de preuve.
5. Rechercher les contradictions et les éléments devenus obsolètes.
6. Produire un plan par portes : entrée, action, preuve, critère de sortie, responsable et autorisation.
7. Exécuter seulement les actions locales/réversibles demandées.
8. Documenter le résultat durable et le pousser sur GitHub.

## Garde-fous

- Revalider fonctionnalités Ads, Merchant Center, SEO, droit, prix, stock, livraison et réglementation.
- Ne pas recommander de contournement de suspension ou contrôle.
- Ne pas inventer un timecode ou une page.
- Ne pas qualifier les résultats personnels du formateur de benchmark représentatif.
- Ne pas appeler profit `CA - ads`.
- Conserver les promotions d'outils/affiliations comme contexte, non comme choix recommandé par défaut.

## Format

1. Objectif.
2. Enseignements sourcés.
3. État actuel observé.
4. Contradictions, actualité et manquants.
5. Application par portes.
6. Décision et prochaine action autorisée.
