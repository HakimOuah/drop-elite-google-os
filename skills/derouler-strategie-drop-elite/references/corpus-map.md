# Carte du corpus

La racine du corpus est découverte depuis le dépôt : `corpus/`.

Depuis une copie installée dans `~/.codex/skills`, utiliser `scripts/resolve_repo.py`. Le script lit le pointeur créé par l'installateur, l'environnement `DROP_ELITE_GOOGLE_OS_ROOT` ou découvre un clone valide ; il ne dépend pas d'un chemin utilisateur figé.

- `manifest.json` : inventaire machine, empreintes et statistiques.
- `CATALOGUE.md` : vue humaine de couverture.
- `raw/vimeo/` : 45 VTT Vimeo du lot initial.
- `raw/youtube/` : 3 VTT YouTube et métadonnées minimisées.
- `raw/documents/` : frameworks GMC, checklist, politiques et scaling.
- `raw/references/` : gist de skill Shopify fourni comme ressource tierce.
- `canonical/sources/` : vidéo pilote avec audio et cinq formats de transcription.
- `derived/plain-text/` : textes sans timecodes pour recherche large.
- `derived/source-map.json` : correspondance exacte entre dérivé et source.
- `derived/coach-source-index.md` : relecture sémantique des 66 contenus parlés, source par source.
- `docs/corpus-gap-audit.md` : modules, pièces jointes, contradictions et procédures manquants.

Les quantités sont générées dans le catalogue ; ne pas figer leurs valeurs dans une réponse sans relire le manifest courant.

## Chemin de recherche

1. recherche large dans les dérivés ;
2. retour au VTT pour le timecode ;
3. retour au PDF pour la page ;
4. écoute du média si le mot exact est déterminant et si le média existe.

Les 65 VTT et le pilote sont `ASSIMILE_TEXTE` ou `ASSIMILE_TEXTE_QUALITE_LIMITEE` dans l'index coach. Ils ne deviennent pas `RELUE_AUDIO` : une lecture sémantique ne corrige pas automatiquement les erreurs de sous-titrage et ne valide pas les affirmations enseignées.

Un futur fichier brut sans entrée dans l'index reste `INGERE_NON_ASSIMILE`. Il peut être recherché, mais ne prouve pas que toute sa méthode a été comprise ou validée.
