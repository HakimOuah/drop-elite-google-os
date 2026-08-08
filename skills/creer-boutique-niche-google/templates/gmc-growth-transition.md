# Transition boutique — `GMC_READY` → `GROWTH_MARKETING`

## Identification

- Projet/boutique :
- Domaine :
- Entreprise :
- Marché :
- État initial : `GMC_READY` / `GROWTH_MARKETING` / autre
- État cible : `GMC_READY` / `GROWTH_MARKETING`
- Mode : `BUILD_GMC_READY` / `BUILD_GROWTH_MARKETING` / `TRANSITION_GMC_TO_GROWTH`
- Thème/version initiale :
- Thème/version cible :
- Date :
- Responsable :

## Preuve Merchant Center

- Compte concerné :
- Statut observé :
- Date/heure d'observation :
- Produits approuvés/refusés :
- Source/capture :
- Demande d'examen autorisée : oui/non/hors périmètre

## Contrat d'invariants

| Invariant | Avant | Après | Source de vérité | Contrôle | Verdict |
|---|---|---|---|---|---|
| entreprise/contact |  |  |  |  |  |
| domaine/vendeur |  |  |  |  |  |
| produit/variante |  |  |  |  |  |
| prix/devise |  |  |  |  |  |
| stock/disponibilité |  |  |  |  |  |
| livraison/frais |  |  |  |  |  |
| retours/remboursement |  |  |  |  |  |
| feed/schema/checkout |  |  |  |  |  |
| achat/tracking |  |  |  |  |  |
| consentement |  |  |  |  |  |

## Modules marketing

| Module | État avant | État après | Claim/offre | Preuve | Risque | Rollback |
|---|---|---|---|---|---|---|
| hero/proposition de valeur |  |  |  |  |  |  |
| promotions/prix barrés |  |  |  |  |  |  |
| urgence/compte à rebours |  |  |  |  |  |  |
| preuve sociale/UGC |  |  |  |  |  |  |
| bundles/upsells |  |  |  |  |  |  |
| seuil livraison |  |  |  |  |  |  |
| popup/email |  |  |  |  |  |  |
| contenu SEO |  |  |  |  |  |  |
| autre |  |  |  |  |  |  |

## QA avant publication

- [ ] même état servi à tous les visiteurs et robots ;
- [ ] mobile étroit et bureau contrôlés ;
- [ ] navigation, recherche et collections fonctionnelles ;
- [ ] variantes, prix, stock et images cohérents ;
- [ ] panier et checkout testés jusqu'à l'étape autorisée ;
- [ ] frais et délais visibles et identiques aux politiques/feed ;
- [ ] contact et liens de politiques testés ;
- [ ] promotions réelles et reliées au backend ;
- [ ] prix barrés et urgence justifiables ;
- [ ] avis/UGC réels et attribuables ;
- [ ] feed et données structurées contrôlés ;
- [ ] achat test avec valeur/devise/transaction ID ;
- [ ] consentement et tags contrôlés ;
- [ ] captures et rapport datés enregistrés.

## Autorisation et publication

- Classe d'action : B/C
- Périmètre autorisé :
- Autorisé par/date :
- Exécuteur réel :
- Sauvegarde/baseline :
- Procédure de rollback :
- Date/heure de publication :
- Version réellement publiée :

## Observation après publication

- Storefront rendu :
- Diagnostics GMC :
- Produits refusés ou alertes :
- Tracking/commandes :
- Incidents clients :
- Décision : `CONSERVER` / `CORRIGER` / `ROLLBACK`
- Prochaine revue :
