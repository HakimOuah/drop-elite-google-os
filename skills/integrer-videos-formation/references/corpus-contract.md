# Contrat du corpus de La Méthode Kraken

## Arborescence

```text
corpus/
├── manifest.json             # inventaire et SHA-256 de toutes les sources
├── CATALOGUE.md              # vue humaine générée
├── raw/
│   ├── vimeo/                # VTT d'origine
│   ├── youtube/              # VTT + métadonnées minimisées
│   ├── documents/            # PDF d'origine
│   └── references/           # gists et ressources complémentaires
├── canonical/
│   ├── catalog.json
│   └── sources/<source_id>/  # médias transcrits selon le contrat historique
└── derived/
    ├── plain-text/           # textes recherchables générés
    └── source-map.json       # mapping dérivés → sources
```

## Immutabilité

Une source brute déjà cataloguée ne doit pas être éditée. Une nouvelle version reçoit un nouvel identifiant ou une entrée de version. Les dérivés peuvent être régénérés à partir du brut.

## Identifiants

- utiliser `a-z`, `0-9` et tirets ;
- préférer l'identifiant stable observé de la plateforme ;
- ne pas inventer un numéro de module ou un titre certain ;
- ne pas inclure signature, token ou paramètre d'expiration.

## Métadonnées

Pour chaque fichier : chemin relatif, type, octets, SHA-256, provenance stable, date d'ingestion, base d'autorisation, langue, durée/timecode ou pages si disponible, statut de titre et statut de relecture.

## Canonique média

Une source transcrite depuis audio conserve : `source.json`, audio, TXT/SRT/VTT/TSV/JSON, `lesson-brief.md` et éventuellement `brut/`. Le dernier timecode doit couvrir l'audio à cinq secondes près.

## Validation

- JSON lisibles ;
- aucun fichier source manquant ;
- SHA-256 exacts ;
- VTT non vides avec timecodes ;
- dérivé relié à une source ;
- aucune URL signée active ;
- aucune déclaration d'assimilation au-delà des fiches réellement produites.
