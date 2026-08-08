# Audit des lacunes du corpus de La Méthode Kraken

**Date de relecture :** 2026-08-08
**Périmètre :** 48 VTT + 1 transcription pilote canonique, soit 49 contenus parlés et 124 489 mots dérivés. Les quatre PDF et le gist Shopify ont également été confrontés aux leçons.

## Verdict

Le corpus permet déjà de répondre avec beaucoup de contexte sur la **sélection de niche**, l'**architecture catalogue/SEO**, l'**intégration produit**, Merchant Center, le **lancement Shopping**, l'optimisation et une forme de scaling par marge. Il ne contient toutefois pas toute la formation annoncée et ne suffit pas, seul, à coacher de manière fiable sur l'ensemble d'une entreprise e-commerce.

La frontière honnête est la suivante :

- **fortement couvert** : niche, catégories, SEO on-site, contenu, flux/GMC, Shopping standard, lecture des KPI et optimisation produit/requête ;
- **partiellement couvert** : sourcing, offre/CRO, mesure, retargeting, automatisation produit, économie et scaling ;
- **absent ou trop superficiel** : customer research, branding complet, email, SEO off-site opérationnel, affiliation, délégation d'entreprise, fiscalité, droit français détaillé, sécurité produit et pilotage SAV/retours.

`corpus/derived/coach-source-index.md` conserve le résumé source par source. Le présent document décrit tout ce qui manque, se contredit ou demande un encadrement opérationnel.

## 1. Limites matérielles du lot

| Lacune | Preuve | Conséquence |
|---|---|---|
| Les 48 VTT restent automatiques | `corpus/manifest.json` : `AUTOMATIQUE_NON_RELUE` | un mot, un nombre ou un nom d'outil peut être faux ; réécouter le média quand la précision est déterminante |
| Les vidéos Vimeo ne sont pas présentes | seules les pistes VTT ont été fournies | impossible de relire les écrans, réglages, feuilles de calcul et gestes montrés |
| Titres et ordre pédagogique Vimeo absents | IDs de captions seulement | intitulés reconstruits et ordre du curriculum incertain |
| Démonstration rideaux très pauvre textuellement | `vimeo-caption-234180398` : dernier timecode ~76 min, ~2 500 mots | grande partie de l'information probablement visuelle ou silencieuse |
| Pas de preuve que le lot contient tout Skool | plusieurs modules et pièces jointes sont annoncés mais absents | répondre `MANQUANT_MODULE` au lieu de supposer la suite |
| Pas de date fiable par leçon | certaines paroles citent juin 2025 ou des interfaces précises, sans métadonnée éditoriale complète | revalider chaque fonctionnalité, règle et écran avant application |

La mention `ASSIMILE_TEXTE` signifie donc « lu et compris depuis le texte », jamais « certifié mot à mot par écoute ».

## 2. Modules annoncés mais non fournis

Le pilote annonce une stratégie plus large que le lot actuel :

| Module annoncé | Repère | Couverture actuelle | Statut |
|---|---|---|---|
| Branding et identité de marque | séquence générale du pilote | quelques principes de différenciation et le skill `brandkit`, mais pas le module Kraken complet | `MANQUANT_MODULE` |
| Email marketing | `de-6417462fa6547-strategie-muse` [10:25–10:32] | capture email évoquée dans le blog, aucune stratégie de flows/campagnes | `MANQUANT_MODULE` |
| SEO off-site / backlinks | pilote [06:31–07:16] et [10:33–10:36] | principe annoncé, aucune procédure complète d'outreach, sélection, budget ou mesure | `MANQUANT_MODULE` |
| Affiliation | pilote [07:25–08:08] | principe et cibles évoqués, aucun recrutement, contrat, tracking, commission ou anti-fraude | `MANQUANT_MODULE` |
| Retargeting Meta | pilote [08:14–08:39] | une mise en place Google Display/Demand Gen est présente ; pas de méthode Meta complète | `PARTIEL` |
| Délégation et automatisation globales | pilote et Q&A `262936735` [04:50–04:53] | uniquement intégration produit assistée par IA et allusions aux process | `MANQUANT_MODULE` |
| Vente/valorisation de boutique | `vimeo-caption-262936735` [02:20–02:40] mentionne le module 13 | aucune leçon dédiée ni calculateur | `MANQUANT_MODULE` |

## 3. Pièces jointes et outils mentionnés mais absents

1. **SOP d'intégration produit de 25–30 pages** et vidéos associées : `vimeo-caption-232117816` [07:04–07:07].
2. **Fichier de calcul de rentabilité/ROAS par produit** : `vimeo-caption-249178958` [05:06–05:36]. Les applications WooCommerce/Shopify sont citées, mais leur logique vérifiable et leur version ne sont pas fournies.
3. **Calculateur de profit moyen et calculateur de valorisation** : `vimeo-caption-262936735` [02:34–02:40].
4. **Feuilles d'architecture et exports finaux** créés pendant les démonstrations : on voit leur construction dans les paroles, pas les fichiers achevés.
5. **Vidéo de connexion de l'assistant à Shopify** citée dans `vimeo-caption-306109499` ; le gist produit est présent, mais pas cette ressource ni son contexte de sécurité.
6. **Données brutes des études de cas** : historique Ads complet, backend commandes, COGS, taxes, retours, remboursements et marge ne sont pas joints. Les récits ne permettent donc pas de recalculer leurs conclusions.

## 4. Méthodes insuffisamment couvertes

### Recherche de niche et demande

Le corpus explique bien comment trouver des idées et lire volume/KD/CPC, mais il manque :

- une méthode robuste de déduplication des requêtes par intention ;
- le nettoyage marque, informationnel, ambigu et international à l'échelle d'un cluster ;
- un protocole de saisonnalité, tendance, volatilité et taille de marché ;
- la recherche client brute : besoins, objections, alternatives, contexte d'usage et willingness to pay ;
- un score de droit de gagner fondé sur preuves et non sur l'esthétique d'un concurrent.

Ces lacunes sont compensées dans le système par `chasse-clusters-codex`, `customer-research` et `competitor-profiling`, mais ces ajouts ne viennent pas de la formation.

### Sourcing et vérité produit

AliExpress et la profondeur fournisseur sont souvent cités, mais la formation disponible ne fournit pas de procédure exhaustive pour :

- variante exacte, prix par palier, stock et route France ;
- coût livré, TVA/import, incoterm et délai observé ;
- conformité CE/GPSR, batteries, matériaux, notices et responsable UE ;
- échantillon, contrôle qualité, photos réelles et plan de secours fournisseur ;
- négociation, SLA, litiges, retours, adresse de retour et capacité à scaler ;
- synchronisation DSers/Shopify et gestion d'une rupture sans tromper le client.

### Économie unitaire et offre

Le ratio `prix / CPC` et les calculs de ROAS produit aident au tri, mais omettent ou simplifient souvent :

- coût fournisseur et livraison par variante ;
- TVA et fiscalité réellement applicables ;
- paiement, change, remises, apps variables ;
- taux de remboursement, retour, chargeback, colis perdu et réexpédition ;
- coût SAV, coût créatif et coût d'intégration ;
- panier multi-produit, repeat, LTV et besoin de trésorerie.

Le framework PDF appelle même `revenu - ad spend` un profit. Le système corrige cela par la **marge contributive après publicité** et refuse de scaler sans coûts complets.

### Storefront, offre et conversion

Les leçons traitent contenu produit et vitesse, mais pas suffisamment :

- hiérarchie de l'offre, bundles, garantie réelle et merchandising ;
- recherche utilisateur, tests d'utilisabilité et accessibilité ;
- confiance sans faux avis, preuve produit et réassurance par risque ;
- mobile par gabarit, compatibilité variantes, panier et checkout ;
- protocole expérimental CRO, échantillon, métrique primaire et causalité.

### Conformité, droit et sécurité produit

Les checklists GMC sont détaillées mais ne remplacent pas :

- une lecture actuelle des politiques Google ;
- les obligations françaises de consommation, rétractation, livraison, garanties légales et médiation ;
- RGPD, cookies/consentement, sous-traitants et transferts ;
- mentions société, facturation, TVA, EPR et obligations sectorielles ;
- sécurité des produits, rappels et claims santé ;
- validation juridique des modèles `policies-fr/`.

### Mesure, Ads et scaling

Les leçons couvrent la mécanique de compte, mais la méthode complète doit aussi préciser :

- transaction ID, valeur/devise dynamiques et test de déduplication ;
- rapprochement Google Ads ↔ analytics ↔ Shopify/backend ;
- consent mode et modélisation selon région ;
- latence, fenêtre de conversion et qualité de donnée ;
- plafond de perte, CAC de rupture et plan de test avant dépense ;
- incrémentalité de la marque, du retargeting et de PMax ;
- capacité fournisseur, trésorerie, SAV et rollback pendant le scaling.

## 5. Contradictions à conserver, pas à lisser

| Sujet | Enseignements présents | Règle coach |
|---|---|---|
| Taille catalogue | environ 50 parfois acceptable, abandon sous ~100, 200 minimum ailleurs, 500–1 000 sur des muses larges | citer le contexte ; en mode projet actuel, 200 distincts minimum, sans appeler cela une règle Google |
| Volume collection | >1 000 pour premiers termes et >150 longue traîne ; catégorie à 450 acceptée ; ~500 « en moyenne » ; refus d'un seuil universel | distinguer formation et décision Hakim : 1 000+ cœur, 500+ secondaire ±200, 30–40 k boutique nettoyés |
| Produits par collection | 5 minimum dans un PDF, 8/12 pour le rendu, 10–20 dans plusieurs leçons | dimensionner selon intention, assortiment vrai et UX ; aucun seuil GMC inventé |
| Passage au tROAS | 15 conversions dans plusieurs cas | seuil de cas/agence ; décider avec mesure propre, volume et recommandation actuelle de la plateforme |
| Taille d'un groupe de rentabilité | ~30 conversions/mois dans `249178958`, 15–20 dans `262936735` [02:09:38–02:09:40] | ne pas sur-segmenter ; consolider si le groupe n'apprend pas, sans transformer l'un des nombres en loi |
| Campagne de départ | Shopping standard au CPC dans la formation ; PMax « moteur central » dans le PDF 2026 | choisir selon hypothèse, contrôle, données et état actuel ; documenter le test |
| Livraison gratuite | parfois utilisée comme argument ; Q&A recommande des frais et un seuil gratuit | calculer impact AOV, CVR, marge et transparence ; tester honnêtement |
| Domaine expiré | présenté presque indispensable puis comme option | jamais un prérequis ; vérifier historique et choisir selon risque/valeur |
| SEO/Ads | la formation attribue un effet SEO direct au trafic Ads | ne pas affirmer de causalité ; mesurer séparément acquisition payante et organique |

## 6. Méthode GMC à conserver et exclusions résiduelles

### Progression conservée

Le coach doit savoir construire les deux états de boutique suivants :

- `GMC_READY` : commerce complet, achetable et sobre, avec identité, contact, produits, prix, livraison, retours, politiques, feed, schema, checkout et tracking cohérents ;
- `GROWTH_MARKETING` : même socle avec proposition de valeur, storytelling, merchandising, promotions réelles, bundles, preuves réelles, email et CRO enrichis.

La séquence est enseignée dans `vimeo-caption-240313004` [00:19:10–00:21:15] et renforcée dans `vimeo-caption-262936735` [01:44:56–01:46:38]. Hakim l'adopte comme `DECISION_PROJET`. La même version doit être visible par tous au même moment et les ajouts marketing doivent rester factuels et cohérents. La procédure détaillée se trouve dans `skills/creer-boutique-niche-google/references/store-states-gmc-growth.md`.

### Exclusions résiduelles

Ces comportements restent archivés mais ne doivent ni être recommandés ni exécutés :

- servir une version différente selon user-agent, IP, provenance ou identité supposée du contrôleur ;
- restaurer sciemment un claim trompeur, interdit ou impossible à prouver après l'approbation ;
- présenter un CSS comme solution « anti-ban » ou déplacer un compte suspendu sans traiter la cause : `vimeo-caption-239791167` ;
- proxy/anti-detect et identités multi-boutiques artificiellement isolées : `Fast-Track GMC Approval Framework`, p. 6–8 ;
- séparer artificiellement société/carte/adresse pour apparaître comme plusieurs annonceurs : `vimeo-caption-262936735` [02:20:03–02:20:19] ;
- retirer des coordonnées après approbation, minorer un délai réel ou créer une incohérence volontaire ;
- réécrire mécaniquement du contenu avec un spinner : `43kJQkuviKY` [03:28–03:32] ;
- envoyer une valeur achat statique de panier moyen quand la valeur réelle échoue ; l'erreur doit être visible et corrigée.

La progression autorisée reste : identité vraie, socle `GMC_READY` stable, ajout marketing conforme, dossier de preuve, QA et rollback. Une cause réelle de refus doit être corrigée avant réexamen.

## 7. File de vérification actuelle

Avant toute réponse qui devient une décision ou une mutation live, vérifier dans les sources primaires datées :

1. politiques Merchant Center, misrepresentation, review et spécification du feed ;
2. capacités/écrans Google Ads, PMax, Shopping standard, stratégies d'enchères et audiences ;
3. mesure achat, conversions améliorées, transaction ID et consentement ;
4. règles Search antispam, données structurées et indexation ;
5. droit français, CNIL, garanties, livraison et rétractation ;
6. exigences produit propres à la niche.

Le point de départ est `docs/official-source-register.md`, à rouvrir et dater lors d'une décision sensible.

## 8. Questions auxquelles le coach peut répondre maintenant

Le corpus est suffisant pour expliquer et adapter, avec réserves :

- comment chercher et préqualifier une niche catalogue-volume ;
- comment transformer un cluster en catégories/produits et maillage ;
- comment organiser un catalogue de lancement et ses briefs ;
- comment préparer une fiche produit SEO/Shopping sans inventer ;
- comment auditer cohérence site/feed/GMC ;
- comment construire une boutique `GMC_READY`, une boutique `GROWTH_MARKETING` ou la transition contrôlée entre les deux ;
- comment vérifier la mesure achat avant Ads ;
- comment lire requêtes, produits, devices, CPC, CTR, CVR, CPA et ROAS ;
- quand exclure, corriger le site, consolider ou segmenter ;
- comment distinguer CA, ROAS et marge contributive.

Il doit répondre `MANQUANT_MODULE` ou faire appel à une compétence complémentaire pour email, affiliation, backlinks, branding complet, customer research, sourcing réglementaire, juridique/fiscal ou délégation générale.

## 9. Prochaines acquisitions prioritaires

Pour approcher réellement le contexte d'un coach de la formation, demander en priorité :

1. les modules email, off-site/backlinks, affiliation, branding et délégation ;
2. le SOP produit 25–30 pages et ses annexes ;
3. le calculateur de rentabilité par produit et le module 13 profit/valorisation ;
4. les vidéos ou captures des démonstrations très visuelles ;
5. l'ordre/titre officiel des leçons ;
6. un export des mises à jour, FAQ et corrections publiées après les vidéos.

Chaque nouvel élément doit être ingéré avec provenance, hash, statut de transcription et fiche sémantique avant d'être déclaré assimilé.
