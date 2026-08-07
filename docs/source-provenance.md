# Provenance et citation interne

## Identifiants

- Vimeo : `vimeo-caption-<id>` ; aucune signature temporaire n'est stockée.
- YouTube : identifiant vidéo stable et métadonnées publiques fournies par la plateforme.
- Documents : nom de fichier normalisé, SHA-256 et nombre de pages lorsque disponible.
- Vidéo pilote : identifiant canonique `de-6417462fa6547-strategie-muse`.

## Citation d'une recommandation

Une recommandation substantielle doit pouvoir être reliée à au moins une entrée :

```text
[OFFICIEL_ACTUEL] URL officielle, consultée le AAAA-MM-JJ
[ENSEIGNE_A_VERIFIER] source_id, timecode ou page
[OBSERVE_PROJET] chemin/rapport, date, métrique
[HYPOTHESE] raisonnement + test prévu
```

Si le titre d'un VTT n'est pas connu, utiliser l'identifiant de caption et marquer `title_status: inferred` ou `unknown`. Ne jamais fabriquer un titre certain.

## Qualité des sous-titres

Les sous-titres automatiques peuvent contenir des erreurs de noms, chiffres et termes techniques. Toute décision irréversible fondée sur une valeur exacte doit être vérifiée dans la vidéo ou un document primaire.

## Actualité

Les règles Google, Shopify, fiscales, juridiques et publicitaires évoluent. Le registre officiel porte une date de vérification. Avant une action à risque, actualiser la source et inscrire la nouvelle date.
