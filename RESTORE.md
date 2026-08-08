# Restauration sur une nouvelle machine

## Prérequis

- accès au compte GitHub autorisé ;
- `git`, `python3` et, pour l'ingestion audio, `ffmpeg` et un moteur Whisper local ;
- Codex configuré sur la machine.

## Procédure

```bash
git clone git@github.com:HakimOuah/drop-elite-google-os.git
cd drop-elite-google-os
python3 scripts/validate_repo.py
bash scripts/install_codex_skills.sh
```

Relancer ensuite Codex et vérifier que les skills `creer-boutique-niche-google`, `integrer-videos-formation` et `derouler-strategie-drop-elite` sont visibles.

Pour mettre à jour des copies déjà installées, utiliser `bash scripts/install_codex_skills.sh --force`. L'ancienne copie est sauvegardée avec un suffixe horodaté. Pour limiter l'opération, ajouter par exemple `--only derouler-strategie-drop-elite`. L'installateur inscrit dans le skill coach un pointeur vers le clone ; `DROP_ELITE_GOOGLE_OS_ROOT` peut le remplacer si le dépôt est déplacé.

## Règle de travail

Le dépôt GitHub est la source de vérité. Modifier d'abord le dépôt, exécuter les validations, committer et pousser, puis réinstaller les skills. Ne pas maintenir une version divergente uniquement dans `~/.codex/skills`.

## Données volontairement absentes

Les secrets, cookies de session, jetons, exports clients, fichiers temporaires et URL signées actives ne doivent pas être restaurés depuis GitHub. Ils doivent être recréés ou récupérés depuis le gestionnaire approprié.
