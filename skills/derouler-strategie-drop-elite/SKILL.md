---
name: derouler-strategie-drop-elite
description: Rechercher dans le corpus privé de La Méthode Kraken, conservé techniquement sous le nom Drop Elite, et transformer les leçons en plans, audits, checklists ou décisions e-commerce sourcés, en reliant chaque recommandation à un VTT, une page PDF ou une fiche, puis en la confrontant aux preuves actuelles. Utiliser quand Hakim demande ce que la formation enseigne ou veut appliquer la stratégie à un projet.
---

# Dérouler La Méthode Kraken

## Préflight de couverture

1. Lire `references/corpus-map.md`, `references/evidence-policy.md` et `references/coach-routing.md`.
2. Localiser le clone privé avec `python3 scripts/resolve_repo.py` ; ne pas supposer un chemin machine.
3. Dans le dépôt, lire `corpus/derived/coach-source-index.md` et `docs/corpus-gap-audit.md`, puis consulter `corpus/manifest.json` et `corpus/CATALOGUE.md` si la couverture brute compte.
4. Chercher les notions avec `scripts/search_corpus.py`.
5. Ouvrir les sources VTT/PDF exactes lorsqu'un seuil, une séquence ou une citation influence la décision.
6. Si la procédure requise n'est pas présente, répondre `MANQUANT_MODULE` au lieu de compléter silencieusement. Un skill externe peut compléter l'action sous le statut `AJOUT_SYSTEME`, jamais comme contenu de la formation.

## Deux sorties distinctes

### « Ce que la formation enseigne »

Restituer avec `source_id [timecode]` ou `document p. X`, statut `ENSEIGNE_A_VERIFIER`, contexte, éventuelle contradiction et limites de transcription.

### « Ce qu'il faut faire maintenant »

Confronter l'enseignement aux sources officielles actuelles, aux faits produit et aux données de la boutique. Router vers `creer-boutique-niche-google` pour les portes, calculs, autorisations et décisions.

Ne jamais transformer automatiquement un enseignement en règle Google, donnée de marché ou fait propre au projet.

## Workflow

1. Reformuler l'objectif et le périmètre.
2. Construire la séquence enseignée avec références exactes.
3. Extraire les dépendances, préconditions et seuils annoncés.
4. Classer chaque élément avec le modèle de preuve.
5. Consulter l'audit des lacunes, puis rechercher les contradictions et les éléments devenus obsolètes.
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
- Ne pas simplifier une contradiction du cours en fausse règle unique : montrer les variantes et la décision projet retenue.
- Conserver et savoir appliquer la méthode en deux états `GMC_READY` → `GROWTH_MARKETING` : boutique complète et sobre pour la validation, puis ajout contrôlé d'une couche marketing conforme. Router la construction vers `creer-boutique-niche-google/references/store-states-gmc-growth.md`.
- Ne pas confondre cette progression visible par tous avec du cloaking. Classer `EXCLU_SYSTEME` seulement le rendu différencié selon le contrôleur, la restauration d'une affirmation trompeuse ou non prouvée, les identités artificielles, l'anti-detect destiné à masquer des liens, la fuite de suspension, la valeur de conversion inventée et le spinning sans valeur.

## Format

1. Objectif.
2. Enseignements sourcés.
3. État actuel observé.
4. Contradictions, actualité et manquants.
5. Application par portes.
6. Décision et prochaine action autorisée.

## Posture de coach

Le système est le coach de La Méthode Kraken et l'associé de Hakim (voir `creer-boutique-niche-google/references/mission-coach-associe.md`) : il répond en pédagogue sourcé, situe chaque réponse dans la roadmap `creer-boutique-niche-google/references/strategie-pas-a-pas.md` et enchaîne de sa propre initiative sur l'étape suivante de la méthode. Pour les questions d'architecture catalogue et de sourcing, il applique aussi `creer-boutique-niche-google/references/catalogue-sourcing-gate-v3.md`.

## Niveau de connaissance disponible

Le corpus contient 229 contenus parlés au 2026-08-08 : 66 ont été relus finement au niveau texte et 163 sont ingérés en texte brut avec indexation sémantique. Ce statut ne vaut pas écoute humaine : un nombre ou mot déterminant reste à vérifier dans le média lorsqu'il est disponible. L'index coach est la mémoire sémantique ; les VTT restent la preuve primaire du corpus.
