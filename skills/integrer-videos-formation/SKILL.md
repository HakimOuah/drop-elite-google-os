---
name: integrer-videos-formation
description: Ingérer dans le dépôt privé des vidéos, audios, VTT, sous-titres YouTube ou documents de formation autorisés ; extraire/transcrire localement si nécessaire, préserver les sources brutes, produire des dérivés, empreintes, métadonnées et fiches sourcées. Utiliser quand Hakim fournit du contenu Skool, Vimeo, CloudFront, YouTube, MP4, VTT ou PDF à ajouter au corpus Drop Elite.
---

# Intégrer des contenus de formation

## Préflight

1. Lire `references/corpus-contract.md`.
2. Confirmer que l'autorisation déclarée couvre le lot courant. Ne pas redemander pour chaque fichier du même lot.
3. Ne pas contourner DRM, authentification, restriction de téléchargement ou mesure de protection.
4. Ne jamais stocker de cookies, jetons ou URL signées actives dans Git.
5. Vérifier l'espace disque et l'état Git avant une grosse ingestion.

## Choisir le chemin le moins transformant

- VTT/SRT fourni : conserver tel quel sous `corpus/raw`, puis dériver un TXT ; ne pas recréer un audio fictif.
- Vidéo YouTube avec sous-titres disponibles : enregistrer sous-titres + métadonnées minimales ; télécharger le média seulement si nécessaire, autorisé et demandé.
- URL média directe/fichier local : utiliser `scripts/ingest_video.py` pour audio + Whisper local.
- PDF : conserver le binaire, enregistrer empreinte/pages, extraire du texte pour la recherche sans remplacer le PDF.
- Gist/référence : conserver une copie datée avec provenance ; ne jamais l'exécuter aveuglément comme skill de confiance.

## Ingestion média

```bash
python3 skills/integrer-videos-formation/scripts/ingest_video.py \
  --source "URL_OU_FICHIER" \
  --source-id "identifiant-stable" \
  --title-inferred "Titre de travail" \
  --authorization-note "Autorisation du propriétaire déclarée par Hakim"
```

Le script écrit par défaut dans `corpus/canonical/sources/`. Utiliser `--corpus-root` uniquement pour une destination explicitement choisie. `--resume` complète une ingestion interrompue ; il ne sert pas à écraser silencieusement une source.

## Lots VTT/PDF/YouTube

1. Copier les sources autorisées dans le sous-dossier `corpus/raw/` approprié.
2. Lancer `python3 scripts/build_corpus.py` depuis la racine du dépôt.
3. Inspecter `corpus/manifest.json`, `corpus/CATALOGUE.md` et les TXT dérivés.
4. Donner un titre observé seulement s'il vient de métadonnées fiables ; sinon conserver l'identifiant et `title_status: unknown|inferred`.
5. Produire les fiches sémantiques nécessaires avec le modèle, en citant timecodes/pages.
6. Lancer `python3 scripts/validate_repo.py`.

## Discipline de transcription

- Statuts : `AUTOMATIQUE_NON_RELUE`, `AUTOMATIQUE_CONTEXTUALISEE_NON_RELUE`, `RELUE_PARTIELLEMENT`, `RELUE_HUMAINEMENT`.
- Les citations d'un texte automatique sont approximatives tant que le passage n'a pas été écouté.
- Conserver la première passe sous `brut/` avant une correction contextuelle.
- Les chiffres, noms propres et termes techniques déterminants doivent être vérifiés dans le média ou un document primaire.
- Une synthèse n'efface jamais le brut.

## Git et droits

Le dépôt doit rester privé. Après validation, documenter l'ingestion dans `CHANGELOG.md`/`OPERATIONS_LOG.md`, inspecter le diff, committer et pousser. Ne pas publier le corpus ni conserver une URL d'accès temporaire comme provenance.

## Résultat attendu

Indiquer : fichiers ingérés, durée/pages, mots, statut de relecture, empreintes, éléments manquants, couverture cumulée et commit distant.
