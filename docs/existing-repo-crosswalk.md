# Répartition entre les dépôts

| Dépôt | Rôle | Ce qui reste dedans | Ce qui va dans cet OS |
|---|---|---|---|
| `boutiques-drop` | hub, mémoire, agents et historique partagé | index des dépôts, conventions globales, sauvegarde du contexte | lien vers l'OS uniquement |
| `boutique-pipeline` | recherche produit active France | candidats, mesures SEMrush, fournisseurs, tickets et rapports de boutique | méthodes génériques seulement |
| `dropshipping-product-factory` | usine historique | archives et code historique | aucune nouvelle connaissance canonique |
| `drop-elite-google-os` | connaissance privée et skills | corpus autorisé, méthodes sourcées, politiques FR, installateurs | source de vérité de ce système |

## Règle anti-duplication

- Une donnée de campagne ou de boutique reste dans son dépôt opérationnel.
- Une méthode réutilisable et indépendante d'une boutique vit ici.
- Un résumé peut faire un lien vers l'autre dépôt, mais ne doit pas créer deux sources de vérité éditables.
- `chasse-clusters-codex` reste le moteur spécialisé de recherche produit France ; ce dépôt l'appelle comme dépendance lorsqu'il est installé.
