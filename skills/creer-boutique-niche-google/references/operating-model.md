# Modèle opératoire

## Un système de portes, pas une checklist linéaire

Une boutique peut revenir en arrière. Une incohérence de délai découverte pendant GMC renvoie à la vérité fournisseur ; un CPA trop élevé peut renvoyer à l'offre ou à l'intention de recherche ; un trafic SEO sans conversion renvoie au message ou à la page.

```text
0 Apprendre → 1 Prouver la demande → 2 Prouver l'économie
     ↑                                      ↓
8 Scaler ← 7 Optimiser ← 6 Tester ← 5 Conformité/mesure
                                      ↑
                         3 SEO → 4 Storefront
```

## Le dossier projet comme contrat de vérité

Chaque dossier conserve :

- `00-intake.md` : objectif, périmètre, autorisations, boutique et canaux ;
- `01-evidence-ledger.md` : faits et sources ;
- `02-gates.md` : verdicts et conditions ;
- `03-economics.md` : hypothèses et calculs ;
- `04-test-card.md` : test en cours ;
- `05-decisions.md` : décisions horodatées ;
- `06-postmortem.md` : résultats et apprentissages.

## Rythme de travail

- Avant une action : vérifier la porte, l'autorité et le rollback.
- Après une action : enregistrer l'état réellement observé, pas l'intention.
- Après un test : préserver la baseline et attribuer la décision à une métrique.
- Après une modification durable : valider, documenter, commit et push.

## Définition de « terminé »

Une tâche n'est pas terminée parce qu'un fichier a été écrit ou qu'une interface a affiché « succès ». Elle est terminée quand l'état final est vérifié par une preuve proportionnée : rendu mobile, événement de test, diagnostic GMC, diff Git, commit distant ou métrique de plateforme.
