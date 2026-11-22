# 🔥 Market Scan — 2026-11-22

> Collecte : treg 5/5 sources, 16 tests App Store (source apple), 2 recherches extended (en dessous de l'objectif : la collecte treg a fourni l'essentiel), GitHub Trending ok, 0 page lue via `read`, 3 candidats creusés (3 fiches App Store, 1 appel `demand` de 30 mots-clés).

## 📊 Résumé Exécutif
- Apps au radar : 15 · creusées : 3
- Mon pari : Pari #1 Devis/factures pour artisans FR (6.9/10, 🟡 BUILD ADJACENT)
- Opportunités immédiates (BUILD NOW) : 0
- Signal du jour : 4 planificateurs de repas de moins de 6 mois (mise, TapCook, Whipp, NeatEat) sont dans le top 10 grossing Food & Drink US, et les leaders de la niche (Whipp, ATC) se font démolir en avis sur l'essai « gratuit » et le paywall d'entrée.

## 🧭 Où l'argent se déplace
| Niche (catégorie) | Mouvement | Demande Google US | Leaders et faiblesse | Part à prendre |
|---|---|---|---|---|
| Planification de repas sous budget (Food) | Feeding Littles nouveau→50, Sidekick 77→49, Paprika nouveau→7 (9 j) ; Whipp #3, TapCook #4, mise #6, NeatEat #8 | meal planner app 2 400/mois, CPC 5,38 $, stable ; budget meal plan 1 000, CPC 3,48 $ ; glp-1 meal plan 2 900, CPC 5,55 $, en hausse (1 900→3 600) | ReciMe #1 (341k avis). Whipp : 10 des 27 1-2★ pour l'essai facturé, 6 pour les prix faux | **Oui** en français : 7/10 places prenables, Jow seul gros acteur (49k avis) |
| Devis/factures indépendants (Business) | Invoice Maker & Estimate nouveau→90 ; Billdu 81→69 ; Invoice Fly #5, Invoice Simple #7 | invoice app 2 900, **CPC 42,60 $** ; estimate app 390, CPC 44,53 $, en hausse (260→590) | Invoice Simple 4.9★, MAJ il y a 3 j ; Devis facile sans MAJ depuis 1 298 j | **À creuser** : CPC très élevé, FR 6/10 prenables, mais leaders solides |
| Vol, turbulences, radio ATC (Travel) | Flightsy nouveau→49, Rift nouveau→42, AeroLOPA 59→37, AirNav 67→55 ; ATC #3 | turbulence forecast 49 500, CPC 0 $, stable ; flight tracker app 6 600, CPC 1,36 $ | Turbulence : 9/10 prenables, apps à 2-25 avis. ATC : 21 des 25 1-2★ sur le paywall | **Oui** turbulences ; ATC à creuser (concurrent gratuit LiveATC) |
| Scan de documents / imprimante (Business, Utilities) | Smart Printer iPrint 60→32, Scanner Pro 32→21, eSign nouveau→82 | scan to pdf 4 400, CPC 5,61 $, en hausse (3 600→6 600) | Marché saturé de clones | **Non** : demande qui monte mais trop d'offre |
| Apprentissage des langues (Éducation) | Parrot nouveau→84, EWA nouveau→95, Speak City nouveau→100 | learn french app 6 600, CPC 6,52 $ ; learn spanish 27 100, CPC 6,84 $ (volatil, 49 500→4 400) | Pimsleur #6, Speak #12 | **À creuser** : saisonnalité forte, peu de preuve de faille |
| Suivi GLP-1 / santé (Health) | MeAgain #38, Ash nouveau→92, Peptalk nouveau→76 | glp-1 tracker 480, CPC 3,44 $, en hausse | Niche déjà proposée 2 fois | **À creuser** : seulement avec un angle nouveau |
| Co-parentalité (Productivité) | TalkingParents #23, OurFamilyWizard #24 | co-parenting app 27 100, CPC 5,31 $, **en baisse** (49 500→8 100) | Deux leaders installés, 4.4-4.6★ | **Non** : demande qui s'effondre |
| Recherche de contacts / amitiés (Lifestyle, Social) | Joie nouveau→25, BeFriend nouveau→97, Meete #21 | non testé | 3.9-4.4★ chez Once, Meete | **À creuser** : preuve d'argent, faible clarté du trou |

## 🎯 Quoi builder
### Pari #1 : Devis et factures pour artisans FR
- **L'idée** : devis et factures conformes au droit français pour artisans et auto-entrepreneurs, à 7 €/mois. Twist sur Invoice Maker (Tofu) : nouveau marché (France) et conformité locale.
- **Les 3 tests** : « facture auto-entrepreneur » (FR) : Demande ✅, Classable ✅ (6/10 prenables), Argent ✅ (Invoice Simple #7, Billdu #62 business), BUILD. « estimate maker » (US) : BUILD.
- **Preuve d'argent** : [Invoice Fly](https://apps.apple.com/us/app/invoice-maker-invoice-fly/id1606911248) #5 business ; [Invoice Simple](https://apps.apple.com/us/app/invoice-simple-invoice-maker/id694831622) #7 business. Demande : invoice app 2 900/mois, CPC 42,60 $ ; estimate app CPC 44,53 $ et en hausse.
- **Le trou** : [Devis facile](https://apps.apple.com/fr/app/devis-facile/id1586993321) sans MAJ depuis 1 298 j ; les gagnants FR sont des traductions d'apps US (résultats du test FR). Aucune plainte comptée sur la conformité : à vérifier en interrogeant des artisans.
- **Pourquoi Kyle** : SaaS full-stack francophone, produit sans IA ni voix, vendable par SEO et par bouche-à-oreille sur un marché qu'il connaît.
- **MVP** : devis en 1 minute, transformation devis→facture avec mentions légales françaises, lien de paiement Stripe. 6 à 8 semaines.
- **Argent** : paywall au moment d'envoyer le 4e document ; 7 €/mois, 59 €/an.
- **Acquisition** : SEO et groupes d'artisans. Accroche à tester : « Ton devis envoyé avant de quitter le chantier ».
- **Test en 48 h** : landing + post dans 3 groupes d'artisans ; go à 30 inscrits sur liste d'attente, stop sous 10.

### Pari #2 : Prévisions de turbulences pour voyageurs anxieux
- **L'idée** : « Vais-je être secoué sur mon vol ? », carte et score de turbulences par numéro de vol, pour les passagers qui ont peur, à 4 €/mois. Twist sur Flighty : niche plus étroite.
- **Les 3 tests** : « turbulence forecast » : Demande ✅ (49 500/mois), Classable ✅ (9/10 prenables), Argent ✅ (Turby #98 travel, Flightradar24 #3), BUILD. « turbulences avion » (FR) : À CREUSER.
- **Preuve d'argent** : [Turby](https://apps.apple.com/us/app/turby-turbulence-forecasts/id6761875552) #98 travel (10 avis) ; [Sky Guru Peur de l'avion](https://apps.apple.com/fr/app/sky-guru-peur-de-lavion/id1382240614) #81 travel FR. Le rang ne prouve pas un revenu.
- **Le trou** : les 9 concurrents remontés ont 2 à 838 notes ; CPC à 0 $ (pas d'annonceurs, argent à confirmer). Source : test App Store.
- **Pourquoi Kyle** : produit de données et de carte, sans équipement, lançable seul.
- **MVP** : score par vol, carte, alerte à l'embarquement. 3 semaines.
- **Argent** : paywall au détail du score de turbulences ; 4 €/mois.
- **Acquisition** : TikTok « peur en avion ». Accroche : « Ton vol sera-t-il agité ? Réponse en 5 secondes ».
- **Test en 48 h** : landing + 2 vidéos TikTok ; go à 40 inscrits, stop sous 15.

### Pari #3 : Plan repas budget aux prix des supermarchés FR (déjà vu 1 fois)
- **L'idée** : planificateur hebdomadaire sous budget avec prix de supermarchés français, 6 €/mois. Twist sur Whipp : nouveau marché et plainte n°1 corrigée (essai honnête, prix réels). Nouveau depuis le dernier rapport : 4 jeunes apps US dans le top 8 grossing.
- **Les 3 tests** : « planificateur de repas » (FR) : Demande ✅, Classable ✅ (7/10), Argent ✅ (Eatr #64), BUILD. « budget meal plan » (US) : ÉCARTÉ (2/10).
- **Preuve d'argent** : [TapCook](https://apps.apple.com/us/app/tapcook-budget-meal-plans/id6769601354) #4 food ; [Whipp](https://apps.apple.com/us/app/whipp-meal-planner-recipes/id6778126199) #3 food. Demande : meal planner app 2 400/mois, CPC 5,38 $.
- **Le trou** : 41 % des 1-2★ de Whipp visent les recettes IA, 22 % les prix faux (fiche App Store).
- **Pourquoi Kyle** : produit SaaS simple, marché francophone, sans voix.
- **MVP** : budget → semaine de dîners, liste de courses chiffrée, export. 4 à 6 semaines.
- **Argent** : paywall après le premier plan, essai de 3 jours avec rappel.
- **Acquisition** : TikTok cuisine budget. Accroche : « Ta semaine de repas à 50 € ».
- **Test en 48 h** : landing + vidéo ; go à 50 inscrits, stop sous 20.

**Mon pari : #1 — Devis et factures pour artisans FR** : meilleur score pondéré, CPC 42 $ qui prouve la valeur du client, et le seul des trois que Kyle vend facilement seul. Kyle décide.

## 🧮 Scorecard des paris
| Pari | 📊 Marché | ⚙️ Complexité | ⏱️ Mise sur le marché | 🏟️ Concurrence | 💰 Revenu | 🧑‍💻 Fit Kyle | **Score** | Verdict | 3 traits |
|---|---|---|---|---|---|---|---|---|---|
| #1 Devis/factures artisans FR | 7 | 6 | 5 | 6 | 8 | 9 | **6.9** | 🟡 BUILD ADJACENT | 2 |
| #2 Turbulences voyageurs anxieux | 6 | 7 | 7 | 8 | 4 | 7 | **6.35** | 🟡 BUILD ADJACENT | 2 |
| #3 Plan repas budget FR | 7 | 5 | 6 | 6 | 6 | 7 | **6.2** | 🟡 BUILD ADJACENT | 1 |

Scores estimés, pas mesurés. Revenu du #2 bas : CPC de 0 $, une seule app avec rang et 10 avis. Concurrence du #1 : 6/10 places prenables en FR mais des leaders solides.

## 💰 Unit Economics — Pari #1 : Devis/factures pour artisans FR
Comparables : Invoice Simple (#7 business), Invoice Fly (#5), Tofu (1,9 M d'entreprises déclarées). Aucun chiffre de revenu direct trouvé : tout ce qui suit est une **estimation**.

| Métrique | Estimation (an 1, solo) |
|---|---|
| Users payants | 500 |
| ARPU | 59 €/an |
| ARR | ~30 k€ |
| CAC | 15 € (SEO, groupes) |
| LTV | ~120 € (rétention 2 ans) |
| LTV/CAC | 8 |
| Payback | 3 mois |
| Burn | ~1 k€/mois (hébergement, Stripe, outils) |
| Runway | long si Kyle ne se paie pas |
| Rev/Employee | ~30 k€ (1 personne) |
| Rule of 40 | non pertinent à ce stade |

**Verdict 🟡** : économie saine sur le papier, mais acquisition non prouvée ; à valider par le test en 48 h avant tout développement.

## 🔭 Radar — 15 apps
| App | Signal | Âge | Ce qu'elle vend | Piste |
|---|---|---|---|---|
| [mise](https://apps.apple.com/us/app/mise-meal-planner/id6777471316) | #6 food (#4 le 13/11) | 164 j | Planificateur de repas (abo) | Pas de version FR |
| [TapCook](https://apps.apple.com/us/app/tapcook-budget-meal-plans/id6769601354) | #4 food, 8 479 avis | 127 j | Plans de repas petit budget | Prix US seulement |
| [Whipp](https://apps.apple.com/us/app/whipp-meal-planner-recipes/id6778126199) | #3 food, 1 059 avis | 162 j | Plan sous budget + courses chiffrées | Essai piégeux, prix faux |
| [ATC Live Air Traffic Radio](https://apps.apple.com/us/app/atc-live-air-traffic-radio/id6755132266) | #3 travel | 313 j | Radio ATC + carte, 70 $/an | Paywall d'entrée détesté |
| [Turby](https://apps.apple.com/us/app/turby-turbulence-forecasts/id6761875552) | #98 travel, 10 avis | 222 j | Prévisions de turbulences | 49 500 recherches/mois |
| [Invoice Fly](https://apps.apple.com/us/app/invoice-maker-invoice-fly/id1606911248) | #5 business, 111 960 avis | 1 745 j | Factures et devis | Pas de vrai FR local |
| [Invoice Simple](https://apps.apple.com/us/app/invoice-simple-invoice-maker/id694831622) | #7 business | 4 812 j | Factures, version FR traduite | Conformité FR absente |
| [Invoice Maker (Tofu)](https://apps.apple.com/us/app/invoice-maker-estimate-app/id1314873764) | #13 business, entré #90 | 3 271 j | Devis, factures, paiement en ligne | Doublon de facture demandé |
| [Flighty](https://apps.apple.com/us/app/flighty-live-flight-tracker/id1358823008) | #1 travel (16/11) | 2 651 j | Suivi de vol premium | Pas d'angle FR |
| Eatr: IA Plan repas | #64 food (FR), 2 892 avis | — | Plan repas IA en français | Seul gagnant FR visible |
| [MeAgain GLP-1](https://apps.apple.com/us/app/meagain-glp-1-tracker-app/id6744178534) | #38 health, 41 551 avis | — | Suivi GLP-1 | Déjà vu 2 fois |
| [Wispr Flow](https://apps.apple.com/us/app/wispr-flow/id6497229487) | #31 productivité (voix) | — | Dictée vocale | Non (gros acteur) |
| [ScribeKit](https://x.com/truly_offline/status/2122993424723026229) | 30 $ MRR déclaré | 5 sem. | Outil mobile, 100 % App Store search | — |
| [CFO Lens](https://x.com/arsyadharmaa/status/2123250350933373015) | 3 500 $ MRR déclaré | 6 mois | SaaS pour directions financières | — |
| [Petites apps mono-usage](https://x.com/vovalukashov/status/2123721509566824778) | 508 $ MRR déclaré | 17 sem. | Portefeuille iOS + web | Test rapide par niche |

Catégories : food, travel, business, health, productivité, finance. Une app vocale seulement (Wispr Flow). Lien Eatr non vérifié (id non relevé) : chercher « Eatr » sur le Store FR.

## 💸 Apps qui font du cash
**Revenus déclarés** (déclaré, non vérifié)
- ScribeKit : 30 $ MRR, 206 $ de revenu en 5 semaines, 23 payants, 0 $ de pub, tout vient de la recherche App Store. 2026-11-18. [post](https://x.com/truly_offline/status/2122993424723026229)
- CFO Lens (SaaS) : 3 500 $ MRR, clients à Londres, Hong Kong, US. 2026-11-19. [post](https://x.com/arsyadharmaa/status/2123250350933373015)
- Portefeuille de petites apps mono-usage (iOS + web) : 508 $ MRR, 87 abonnements, 757 $ sur 28 jours (App Store : 281 $ MRR). 2026-11-20. [post](https://x.com/vovalukashov/status/2123721509566824778)
- App Android (nom non cité) : 32 $ le premier mois, 16 $ le mois en cours. 2026-11-16. [post](https://x.com/engwaliullah/status/2122325193775546500)
- Écartés : un post à 3 100 $ MRR via TikTok organique et un post à 1 100 $ sur 28 jours, sans nom de produit ; l'app « appeler le Père Noël » qui « paie l'hypothèque » ([Reddit](https://www.reddit.com/r/microsaas/comments/1y29de6/)), sans montant.

**App Store US, top grossing, moins de 100k avis, hors jeux** (un rang n'est pas un revenu)
- #3 Food : [Whipp](https://apps.apple.com/us/app/whipp-meal-planner-recipes/id6778126199), 1 059 avis, plan de repas sous budget + liste de courses chiffrée.
- #4 Food : [TapCook](https://apps.apple.com/us/app/tapcook-budget-meal-plans/id6769601354), 8 479 avis, plans de repas à petit budget.
- #6 Food : [mise](https://apps.apple.com/us/app/mise-meal-planner/id6777471316), 5 255 avis, planificateur de repas.
- #8 Food : [NeatEat](https://apps.apple.com/us/app/neateat-meal-planner/id6783742855), 1 506 avis, planificateur de repas.
- #3 Travel : [ATC](https://apps.apple.com/us/app/atc-live-air-traffic-radio/id6755132266), 4 584 avis, radio de contrôle aérien en direct + carte, 70 $/an.
- #8 Travel : [Airclub](https://apps.apple.com/us/app/airclub-flight-deals/id6740247064), 19 294 avis, bons plans vols.
- #14 Business : [Joist](https://apps.apple.com/us/app/joist-estimate-invoice-maker/id592163563), 14 585 avis, devis et factures.
- #12 Business : [SimplyWise](https://apps.apple.com/us/app/simplywise-cost-estimator/id6670619664), 43 047 avis, estimation de coûts.
- Mouvements food (9 j) : Sidekick 77→49, Daily Bite 69→53, Plan to Eat 100→76 ; business : Invoice Maker & Estimate nouveau→90.

**Jeunes apps qui gagnent déjà** (moins de 365 j)
- mise (164 j, #6 food), TapCook (127 j, #4 food), Whipp (162 j, #3 food), NeatEat (127 j, #8 food) : planification de repas.
- ATC (313 j, #3 travel) : radio ATC en direct. Turby (222 j, #98 travel, 10 avis) : prévisions de turbulences.
- Reel Craft Pass (76 j, #65 food, 3 avis), GoFoodie (124 j, #88 food), Roam packing lists (98 j, #74 travel, 14 avis), Trekly (27 j, #97 travel).
- **Leaders sans MAJ depuis plus de 180 j (places à prendre)** : [LiveATC Air Radio](https://apps.apple.com/us/app/liveatc-air-radio/id317809458) (300 j, 3.6★, #46 travel), [Flightview](https://apps.apple.com/us/app/flightview-flight-tracker/id399057337) (304 j, 3.6★, #54 travel), Windrock Park (264 j, 2.44★, #67 travel), Soluna (383 j, #92 social).

## 🔬 App creusée #1 : ATC - Live Air Traffic Radio
1. **Identification** : [ATC](https://apps.apple.com/us/app/atc-live-air-traffic-radio/id6755132266), Travel, sortie App Store 2026-01-12 (313 j), MAJ 2026-11-20. Éditeur et fondateurs non trouvés. 4,7★ sur 4 584 notes, #3 travel US le 22/11. Payant (70 $/an ou 6 $/semaine).
2. **Proposition** : écouter en direct les échanges pilotes-contrôleurs de 2 000+ aéroports US, avec carte, transcription IA et alertes d'urgence. Cible : passionnés d'aviation, proches de voyageurs.
3. **Les 3 décisions qui font l'argent** : onboarding long (extrait audio, questionnaire, animations) avant le prix ; paywall dur dès l'ouverture, sans version gratuite, essai uniquement sur l'abonnement annuel ; retour par les alertes d'urgence et le replay (estimation, d'après les avis et la description).
4. **Test des 3 traits** : ✅ émotion (la tension d'une urgence en direct) ; ✅ résultat visible en secondes (on entend un avion sur la carte) ; ❌ pas de partage intégré relevé.
5. **Ce qui manque** (25 des 50 derniers avis sont à 1-2★) : 84 % (21/25) paywall ou prix (« Free to download, pay to use ») ; 20 % (5/25) onboarding interminable ; aéroports manquants et pas d'iPad. Citations : « Liveatc.net is free » ; « Cash grab!!!! ». App mise à jour il y a 1 j, donc pas de trou de maintenance. Source : fiche App Store.
6. **Acquisition** : pubs Meta non trouvées (la page remontée, « ATCO », n'est pas celle de l'app). Autres canaux : non trouvés ; l'acquisition semble passer par la recherche App Store (« live atc »).
7. **Stack** : estimation, app native iOS, récepteurs radio propriétaires (cité dans un avis), transcription IA, flux ADS-B.
8. **Réplication** : complexité 7/10 (flux audio et récepteurs). Niche : LiveATC (300 j sans MAJ, 3,6★, #46 travel) est le seul concurrent direct, et il est gratuit sur le web. Angle pour Kyle : ne pas copier l'audio, partir de la recherche « turbulence forecast » (Pari #2). Temps de dev : 3 mois pour une copie, 3 semaines pour l'angle turbulence.

## 🔬 App creusée #2 : Whipp: Meal Planner & Recipes
1. **Identification** : [Whipp](https://apps.apple.com/us/app/whipp-meal-planner-recipes/id6778126199), éditeur EVOY LTD, Food & Drink, sortie 2026-06-12 (162 j), MAJ 2026-11-17. 4,68★ sur 1 059 notes, #3 food US le 22/11. Gratuit à télécharger, abonnement.
2. **Proposition** : on donne un budget hebdomadaire et ses goûts, l'app planifie les dîners de la semaine et sort une liste de courses classée par rayon, avec total estimé. Cible : foyers qui veulent contrôler leurs courses.
3. **Les 3 décisions qui font l'argent** : onboarding de personnalisation (budget, magasin, goûts) ; paywall d'entrée avec essai de 3 à 7 jours, carte demandée tout de suite ; retour hebdomadaire par le nouveau plan et la liste de courses (estimation, d'après la description et les avis).
4. **Test des 3 traits** : ❌ émotion faible (un budget) ; ✅ résultat visible en moins d'une minute (« la semaine en moins d'une minute ») ; ❌ aucun partage intégré.
5. **Ce qui manque** (27 des 50 derniers avis sont à 1-2★) : 41 % (11/27) recettes « IA » non testées et instructions qui ne se mettent pas à l'échelle ; 37 % (10/27) essai « gratuit » facturé, annulation ignorée ; 22 % (6/27) prix du magasin faux (« 45 $ annoncés, 70 $ payés »). Citation : « The ingredient pricing does not match actual store pricing. » Les thèmes se recoupent. MAJ récente, pas de trou de maintenance.
6. **Acquisition** : 0 pub Meta active, 0 lancée depuis 7 jours (page à vérifier). Autres canaux : TikTok, selon un article sur les planificateurs de repas (non vérifié). Pas de PH.
7. **Stack** : estimation, app iOS native ou React Native, génération de recettes par LLM, base de prix de magasins.
8. **Réplication** : complexité 6/10. Niche : les quatre jeunes apps (mise, TapCook, Whipp, NeatEat) sont toutes US ; en français, la recherche « planificateur de repas » a 7/10 places prenables et Jow seul au-dessus de 1 000 notes. Angle : prix de supermarchés français réels, essai honnête. Temps de dev : 4 à 6 semaines.

## 🔬 App creusée #3 : Invoice Maker ▸ Estimate App (Tofu)
1. **Identification** : [Invoice Maker ▸ Estimate App](https://apps.apple.com/us/app/invoice-maker-estimate-app/id1314873764) (« by Tofu »), éditeur GetPaid Inc., Business, sortie 2017-12-08, MAJ 2026-11-16. 4,83★ sur 37 231 notes, #13 business le 10/11, revendique 1,9 M d'entreprises (déclaré par l'éditeur).
2. **Proposition** : devis et factures en quelques minutes, paiement en ligne par lien ou QR code, relances automatiques. Cible : freelances, artisans, petites entreprises. Prix : abonnement (un avis parle de 8 $/semaine).
3. **Les 3 décisions qui font l'argent** : onboarding rapide pour émettre un premier document ; paywall au moment d'envoyer ou de se faire payer (estimation) ; retour par les relances et les paiements encaissés (estimation, d'après la description).
4. **Test des 3 traits** : ❌ émotion faible, sauf être payé ; ✅ résultat visible en moins d'une minute (« less than a min ») ; ✅ distribution intégrée (le client reçoit un lien de paiement).
5. **Ce qui manque** (4 des 50 derniers avis sont à 1-3★, 2 à 1★) : 2 avis sur 2 à 1★ portent sur des prélèvements après suppression (« charging me 8 dollars a week ») ; un avis à 3★ demande de dupliquer une facture ; un autre des acomptes numériques. Échantillon trop mince pour des parts fiables. Pas de trou de maintenance.
6. **Acquisition** : pubs Meta non trouvées (3 pages écartées, aucune n'est sûre). Autres canaux : non trouvés.
7. **Stack** : estimation, app native iOS, Stripe pour les paiements (cité dans un avis).
8. **Réplication** : complexité 6/10. Niche : en français, « facture auto-entrepreneur » a 6/10 places prenables ; les gagnants sont Invoice Simple (#7 business) et Billdu (#62). Devis facile (1 143 notes) n'a pas été mis à jour depuis 1 298 j. Angle pour Kyle : devis/factures conformes au droit français, pensés pour les artisans. Temps de dev : 6 à 8 semaines.

## 📈 Tendances Émergentes
- **Accroches publicitaires** : aucune accroche exploitable ce jour. Les pubs de la page remontée pour ATC appartiennent à un autre annonceur (ATCO), Whipp n'a aucune pub Meta active, et aucune page sûre n'a été trouvée pour Invoice Maker.
- **Le paywall d'entrée déçoit partout** : 84 % des avis négatifs d'ATC (21 sur 25) et 37 % de ceux de Whipp (10 sur 27) visent l'essai « gratuit » ou le paywall qui bloque l'app. Un essai honnête est un argument de vente.
- **Vague de planificateurs de repas jeunes** : quatre apps de moins de 6 mois dans le top 8 food US, toutes en anglais.
- **Les posts X sur l'argent restent petits** : 30 $ à 3 500 $ de MRR, acquisition par TikTok organique ou recherche App Store, aucun montant vérifié.
- **GitHub Trending** : agents de code et skills (plannotator, stitch-skills, last30days-skill), plus [we-promise/sure](https://github.com/we-promise/sure), finance perso open source (2 041 étoiles cette semaine).
- **Hacker News** : dominé par la démonstration de l'hypothèse de Riemann généralisée et Inkling 2 Mini ; rien d'exploitable pour un produit grand public.
