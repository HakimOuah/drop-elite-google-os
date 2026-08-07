# Carte du corpus

La racine du corpus est découverte depuis le dépôt : `corpus/`.

- `manifest.json` : inventaire machine, empreintes et statistiques.
- `CATALOGUE.md` : vue humaine de couverture.
- `raw/vimeo/` : 45 VTT Vimeo du lot initial.
- `raw/youtube/` : 3 VTT YouTube et métadonnées minimisées.
- `raw/documents/` : frameworks GMC, checklist, politiques et scaling.
- `raw/references/` : gist de skill Shopify fourni comme ressource tierce.
- `canonical/sources/` : vidéo pilote avec audio et cinq formats de transcription.
- `derived/plain-text/` : textes sans timecodes pour recherche large.
- `derived/source-map.json` : correspondance exacte entre dérivé et source.

Les quantités sont générées dans le catalogue ; ne pas figer leurs valeurs dans une réponse sans relire le manifest courant.

## Chemin de recherche

1. recherche large dans les dérivés ;
2. retour au VTT pour le timecode ;
3. retour au PDF pour la page ;
4. écoute du média si le mot exact est déterminant et si le média existe.

Un fichier brut sans fiche sémantique est `INGERE_NON_ASSIMILE`. Il peut être recherché, mais ne prouve pas que toute sa méthode a été comprise ou validée.
