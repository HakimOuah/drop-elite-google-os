# Autorisations d'action

## Classes

### A — Lecture et préparation réversible

Autorisées dans le périmètre demandé : lire, auditer, calculer, créer un brouillon local, préparer un feed de test, produire une checklist, valider un rendu local.

### B — Mutation réversible d'un système en portée

Nécessite que la demande inclue clairement l'implémentation : modifier un thème de développement, créer un produit brouillon, changer une configuration non publiée, pousser une branche Git.

Avant action : état initial, cible exacte, sauvegarde/rollback et validation attendue.

### C — Action commerciale, externe ou difficilement réversible

Autorisation explicite requise : publier, modifier une boutique live, connecter ou soumettre GMC, demander un examen, modifier mapping/prix DSers, passer une commande, lancer/augmenter une campagne, dépenser, envoyer un message externe, supprimer des données, changer un domaine ou moyen de paiement.

## Fiche d'action

```yaml
action: ""
class: A|B|C
target: ""
requested_by: ""
authorized_scope: ""
pre_state_evidence: ""
rollback: ""
executor: human|codex|other
completion_evidence: ""
result: planned|done|failed|blocked
```

## Énoncé honnête

Utiliser :

- `[FAIT]` pour l'état vérifié ;
- `[HYPOTHESE]` pour une explication non démontrée ;
- `[MANQUANT]` pour une preuve absente.

Nommer l'exécuteur réel. Un fichier préparé par Codex ne signifie pas qu'une campagne a été lancée ou qu'un produit a été publié.
