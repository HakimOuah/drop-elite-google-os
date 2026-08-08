# Corpus privé de La Méthode Kraken

Ce dossier contient un lot autorisé fourni par Hakim le 2026-08-08.

## État initial

- 45 fichiers VTT Vimeo ;
- 3 fichiers de sous-titres YouTube et métadonnées minimisées ;
- 4 documents PDF ;
- 1 référence Gist tierce ;
- 1 vidéo pilote déjà transcrite localement, avec audio et formats TXT/SRT/VTT/TSV/JSON.

Les statistiques exactes et empreintes sont générées dans `manifest.json` et `CATALOGUE.md`.

## Niveaux

- `raw/` : source reçue, non éditée ;
- `canonical/` : source média structurée selon le contrat historique ;
- `derived/` : texte généré et régénérable pour recherche.

Un fichier `raw` n'est pas automatiquement « assimilé ». Les titres Vimeo ne sont pas connus à partir du seul identifiant de caption ; ils restent non observés tant qu'une métadonnée fiable ne les relie pas.

## Autorisation et redistribution

Base enregistrée : autorisation du propriétaire déclarée par Hakim pour cet usage personnel. Voir `RIGHTS.md`. Ne pas publier ce dossier.

## Régénération

```bash
python3 scripts/build_corpus.py
python3 scripts/validate_repo.py
```

Le build ne télécharge rien et ne modifie pas les sources brutes.
