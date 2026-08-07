# Sécurité

## Ne jamais committer

- secrets API, mots de passe, clés privées et jetons OAuth ;
- cookies, profils de navigateur et données de session ;
- URL actives portant `sig=`, `token=`, `expires=` ou une autre signature d'accès ;
- exports de commandes ou données personnelles clients ;
- fichiers `.env`, caches, builds et fichiers temporaires ;
- preuves contenant des coordonnées personnelles non nécessaires.

## Contrôle avant chaque push

1. lire `git status --short` ;
2. inspecter le diff et les fichiers non suivis ;
3. lancer `python3 scripts/validate_repo.py` ;
4. vérifier que le commit ne mélange pas un changement sans rapport ;
5. pousser uniquement après succès.

Une URL publique stable de documentation peut être conservée. Une URL signée d'accès à un média ne le peut pas.
