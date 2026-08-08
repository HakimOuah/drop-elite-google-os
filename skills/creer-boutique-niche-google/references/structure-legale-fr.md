# Structure légale et fiscale (France) — repères Kraken

**Statut : `ENSEIGNE_A_VERIFIER` — contenu daté (~2022-2025), antérieur à la réforme du seuil unique de franchise TVA.** Confirmer les seuils **2026** avant toute application. Ce document n'est pas un conseil juridique/fiscal : router vers un expert-comptable inscrit à l'Ordre et un avocat pour toute décision. Sources : module 11 (`vimeo-caption-1089473725`, `1089473739`, FAQ `1100102487`) et vidéos LegalPlace (`RRehUD4-C5k`, `_Jww5002w7M`, `9vcyc_XPqnk`, `ffuYF6q_-Pg`, `XhAJG6gopyM`).

## Choix du statut

- **Seul** : micro-entreprise, EURL, SASU. **Plusieurs** : SARL, SAS, SA (micro impossible à plusieurs).
- Micro : formalités simples mais **responsabilité illimitée**, plafonds de CA, imposition sur le CA (pas sur le bénéfice réel).
- EURL vs SASU (le vrai arbitrage = rémunération/couverture) : sur 1 000 € de salaire, EURL ≈ 450 € de cotisations (TNS ~45 %), SASU ≈ 750 € (assimilé salarié ~75 %). Dividendes : SASU ~30 % (flat tax), EURL ~45 %. **Revenu mensuel régulier → EURL ; sortie en dividendes de fin d'année → SASU** (recommandé ~80 % des cas).

## Montage type recommandé (`1089473725`)

**SAS/SASU (la boutique) + micro-entreprise en parallèle.** La micro ne peut pas exercer la même activité que la SAS ; elle encaisse les **revenus annexes** : cashback AliExpress, affiliation de logiciels, prestation de netlinking. Optimisations citées : dividendes plutôt que salaire, récupérer la TVA sur achats pro, aides ACRE (~11 % la 1re année) / chômage jusqu'à 2 ans.

## Bascule micro → société

- Le seuil légal micro est élevé (~188 k€ marchandises) mais le **vrai critère = l'imposition réelle** : si tu es en déficit (investissement marketing/sourcing), **quitte la micro pour la société** afin de capter le **déficit reportable** (perdu en micro). Faire un tableur CA − coûts.
- **Assujettissement TVA micro** ≈ 85 k€ an 1 / 93 k€ an 2 en glissement. La **franchise de TVA n'est cohérente que si on vend uniquement en France** (au-delà de 10 000 € de ventes UE → TVA du pays de destination ; le n° TVA intracommunautaire est exigé par Stripe/PayPal/Shopify/fournisseur).
- **Migration opérationnelle** : clôture micro concomitante à la création société (ex. 30/06 → 01/07) ; garder Stripe/PayPal/Shopify en réattribuant les moyens d'encaissement à la société (on ne peut pas changer le pays d'un compte Stripe, seulement l'intitulé).

## TVA dropshipping (`1100102487`)

- **AliExpress** : ne pas mettre son n° de TVA sur la plateforme ; **aucune TVA récupérable** (fournisseur hors UE) = charge pure. Préférer la facturation via succursale UE (Pays-Bas/Allemagne) pour une compta propre.
- **Auto-liquidation Google Ads (Irlande)** : écriture neutre (+20 %/−20 %), aucun impact réel — sert juste à mesurer les flux intra-UE.
- **IOSS** : avoir son propre numéro (société) pour l'importation ; ne jamais utiliser l'IOSS du fournisseur chinois. Produits < 150 € : en principe pas de frais de douane (à la charge du client sinon).
- **DOM-TOM** : spécificités TVA → comptable local obligatoire.

## Comptabilité

- Compte bancaire pro (obligatoire micro seulement si > 10 000 €/an sur 2 ans) ; e-commerce = compta soutenue, déclarations TVA souvent **mensuelles**. Le comptable qualifie les flux par géographie (France/UE/monde).
- Expert-comptable en ligne (Dougs, Clémentine, Pennylane…) : **20-30 €/mois** (EI) / 70-100 (libéral) / ≥150 (artisan-commerçant), −30 à −40 % vs cabinet. **Exiger un forfait « de A à Z »** (TVA + bilan + liasse + dépôt des comptes inclus) et vérifier l'inscription à l'Ordre.
- Comptable « câblé e-commerce » : comprend les frais Facebook/Google et les plateformes de vente, facture au forfait (pas à la ligne), outil de synchro banque + marketing.

## RH (repères de coût)

Stagiaire ~600 €/mois ; alternant net ~100-200 €/mois (aides) ; freelance FR ~2 000 €/mois. En scaling : chef de projet international ~4 000 € chargé, développeur ~5 000 € chargé.

## Expatriation (`1089473739`)

La légalité ne doit pas freiner le démarrage ; l'expatriation est un choix de vie, pas fiscal. Résidence fiscale (où on vit) ≠ siège société (où on vend). Attention : si le site entre dans l'actif de la société FR, sa sortie exige estimation + contrat de cession. D'abord un comptable, puis un avocat pour la TVA/le juridique.
