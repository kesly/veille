# 🔥 Market Scan — 2026-11-20

> Collecte : treg 4/5 sources (Product Hunt en 504, Reddit vide), 9 recherches extended, GitHub Trending ok, 1 page lue, 3 candidats creusés.

## 📊 Résumé Exécutif
- Apps au radar : 15 · creusées : 3
- Mon pari : Pari #1 Scanner de revente Vinted/Leboncoin sans piège d'essai (6.05/10, 🟡 BUILD ADJACENT)
- Opportunités immédiates (BUILD NOW) : 0
- Signal du jour : les apps qui encaissent (ThriftAI, TalkingParents, Double Holo) accumulent les 1★ sur le même thème, l'essai gratuit piégé ou le paywall qui s'est durci.

## 🧭 Où l'argent se déplace
| Niche (catégorie) | Mouvement | Demande Google US | Leaders et faiblesse | Part à prendre |
|---|---|---|---|---|
| Revente / thrift (shopping) | Thrifty AI nouveau→#36, Thrifted 73→#53, Thrift Hunt 85→#62, Inventory Bot nouveau→#65, AI Listing Assistant nouveau→#67 (9 j) | « reseller app » 2 900/mois, CPC 5.23 $, plat ; « thrift scanner app » 10→30 | ThriftAI 4.77★, 20 880 avis, MAJ il y a 25 j ; 29 avis sur 50 à 1★ (essai piégé, prix faux) | **oui** : leader mal vu, clones en nombre |
| Suivi de colis (shopping) | #3 My Package Tracker, #4 TrackPack 3.7★, #9 Parcels Hub 3.5★ | « amazon package tracker » 60 500, CPC 0.25 $ ; « package tracker app » 210, CPC 2.62 $ | Notes 3.5-3.7★ pour 2 sur 3 | à creuser : CPC bas |
| Co-parentalité (productivité) | TalkingParents #25, OurFamilyWizard #22 | « co-parenting app » 27 100, CPC 5.31 $, **en baisse** (49 500→8 100) | TalkingParents 4.38★, 41 avis sur 50 à 1★, gratuit supprimé en mars 2026 | **oui** côté plainte, à creuser côté demande |
| Alertes de restock (shopping) | Scout nouveau→#58, Outpost nouveau→#54, HotStock #5 | « restock alerts » 590, CPC 1.09 $, **260→2 400 en 12 mois** | HotStock 4.7★, 15 508 avis | **oui** : la demande monte plus vite que l'offre |
| Cartes à collectionner (sports/shopping) | SPcard nouveau→#89, Card Ladder #5, Double Holo #10 | « pokemon card scanner » 14 800, CPC 2.44 $, 8 100→18 100 ; « sports card scanner » 4 400 | Double Holo 4.77★, 22 avis sur 50 à 1★ (paywall, compte obligatoire) | à creuser : données de prix lourdes |
| Macros IA (santé) | FoodPilot nouveau→#99, MacrosFirst nouveau→#91, MacroFactor #12 | « ai calorie tracker » 1 000, CPC 4.41 $, en baisse | MacroFactor 4.8★ | non : leader solide |
| Anglais IA (éducation, vocal) | Loora nouveau→#84, LangLearn #8, YayTalk #29 | « language learning app » 27 100, 40 500→8 100 | Speak 4.8★, 67 368 avis | non : saturé, demande en baisse |

Source du bloc « Où l'argent bouge » : `/tmp/treg.md`, relevés du 11 au 20/11. Demande : `demand`, caches inclus.

## 🎯 Quoi builder
### Pari #1 : Scanner de revente Vinted/Leboncoin, essai sans piège
- **L'idée** : pour les revendeurs et chineurs francophones, un scan photo qui estime le prix de revente et écrit l'annonce Vinted/Leboncoin, à 4.99 €/mois ou 29 €/an, essai sans carte. Déjà vu 1 fois (brocante FR) ; nouveau : le cluster shopping gagne 27 apps en 9 jours.
- **Preuve d'argent** : [ThriftAI](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278) #11 shopping (45-60 K$/mois, estimation de trackers) ; [Thrifty AI / Thrift Hunt](https://apps.apple.com/us/app/thrift-hunt-resale-scanner-ai/id6760717302) #36 et #62.
- **Le trou** : « Charged in full on the day the trial was supposed to end » (avis ThriftAI) ; prix faux sur les livres. Pas d'équivalent français trouvé, demande FR non mesurée.
- **Pourquoi Kyle** : mobile et SaaS seul, intégration d'API de prix, marché francophone sans leader local vu.
- **MVP** : scan photo avec estimation et fourchette ; annonce prête à coller ; historique d'achats et marge. 6 à 8 semaines.
- **Argent** : paywall après 5 scans gratuits sans carte, 4.99 €/mois.
- **Acquisition** : TikTok de revendeurs. Accroche : « Ton essai ne se transforme jamais en facture surprise. »
- **Test en 48 h** : landing + vidéo TikTok de scan. Go à 100 emails, stop sous 30.

### Pari #2 : Co-parentalité à prix plat (France)
- **L'idée** : pour parents séparés, messagerie, calendrier et frais partagés avec export PDF inclus, 5 €/mois par foyer. Déjà vu 1 fois ; nouveau : TalkingParents a supprimé son gratuit en mars 2026 et 41 avis sur 50 sont à 1★.
- **Preuve d'argent** : [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726) #25 productivité ; [OurFamilyWizard](https://apps.apple.com/us/app/ourfamilywizard-co-parent-app/id497405393) #22 (110-300 $/an par parent, estimation presse).
- **Le trou** : « Now it's 40 a month. » (avis) ; support absent ; pas de version FR vue.
- **Pourquoi Kyle** : produit CRUD + paiement, droit français à étudier, SEO francophone.
- **MVP** : fil de messages horodatés ; calendrier de garde ; export PDF. 8 semaines.
- **Argent** : paywall à l'invitation du second parent, 5 €/mois par foyer. La demande Google US (27 100, CPC 5.31 $) baisse.
- **Acquisition** : SEO et forums de parents séparés. Accroche : « Un seul prix pour deux parents. »
- **Test en 48 h** : landing + post sur un forum. Go à 50 inscrits, stop sous 15.

### Pari #3 : Scanner de cartes à collectionner sans compte
- **L'idée** : pour collectionneurs francophones, scan de cartes avec cote Cardmarket, sans compte obligatoire, 3.99 €/mois. Déjà vu 1 fois ; nouveau : « pokemon card scanner » passe de 8 100 à 18 100/mois.
- **Preuve d'argent** : [Double Holo](https://apps.apple.com/us/app/double-holo-card-scanner/id6759494054) #10 shopping (~250 K$ ARR déclaré) ; [Card Ladder](https://apps.apple.com/us/app/card-ladder/id1541535971) #5 sports.
- **Le trou** : « Account creation is atrocious. » (avis Double Holo).
- **Pourquoi Kyle** : il livre vite un scan simple, ses clients FR n'ont pas d'alternative évidente (non vérifié).
- **MVP** : scan et prix ; collection locale ; alertes de prix. 10 semaines.
- **Argent** : alertes et export derrière le paywall, 3.99 €/mois.
- **Acquisition** : TikTok d'ouvertures de boosters. Accroche : « Scanne sans créer de compte. »
- **Test en 48 h** : vidéo + landing. Go à 150 emails, stop sous 40.

**Mon pari : #1 — Scanner de revente Vinted/Leboncoin**, car c'est le score le plus haut et la plainte la plus nette (essai piégé), dans la niche où 27 apps entrent en 9 jours. Tu décides.

## 🧮 Scorecard des paris
| Pari | 📊 Marché 20 % | ⚙️ Complexité 15 % | ⏱️ Délai 15 % | 🏟️ Concurrence 15 % | 💰 Revenu 20 % | 🧑‍💻 Fit Kyle 15 % | **Score** | Verdict | 3 traits |
|---|---|---|---|---|---|---|---|---|---|
| #1 Scanner de revente FR | 6 | 6 | 6 | 4 | 7 | 7 | **6.05** | 🟡 BUILD ADJACENT | 2 |
| #2 Co-parentalité FR | 6 | 5 | 5 | 6 | 7 | 6 | **5.90** | 🟠 WATCH | 2 |
| #3 Scanner de cartes | 5 | 4 | 4 | 4 | 6 | 5 | **4.75** | 🟠 WATCH | 3 |

Scores honnêtes : aucune demande française n'a été mesurée, seulement la demande US, donc les notes de marché sont prudentes.

## 💰 Unit Economics — Pari #1 : Scanner de revente FR
Comparable : ThriftAI, 45-60 K$/mois selon des trackers (estimation). Tout est estimation.
- **ARR** : 150 K€ en 18 mois (hypothèse : ~3 000 abonnés payants).
- **ARPU** : 4 €/mois, 48 €/an. **Users** : 30 000 installs, 10 % de conversion.
- **CAC** : 6 € (TikTok organique + un peu de pub). **LTV** : 4 € × 10 mois = 40 €. **LTV/CAC** : 6.7. **Payback** : 1.5 mois.
- **Burn** : 800 €/mois (APIs de vision, hébergement). **Runway** : sans levée, jusqu'au seuil de rentabilité sur la trésorerie perso.
- **Rev/employé** : 150 K€ (1 personne). **Rule of 40** : non applicable, croissance non mesurée.
- **Verdict santé : 🟡**. L'économie est bonne si la rétention tient, mais le churn des apps de scan est haut (estimation) et la demande FR n'est pas prouvée.

## 🔭 Radar — 15 apps
| App | Signal | Âge | Ce qu'elle vend | Piste |
|---|---|---|---|---|
| [ThriftAI](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278) | #11 shopping, 20 880 avis | 532 j | Scan photo → prix de revente, essai 3 j puis 9.99 $/mois ou 20-50 $/an | Pièges d'essai, prix faux |
| [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726) | #25 productivité | 3 856 j | Messagerie co-parents certifiée tribunal, 7-32 $/mois par parent | Gratuit supprimé, support absent |
| [OurFamilyWizard](https://apps.apple.com/us/app/ourfamilywizard-co-parent-app/id497405393) | #22 productivité, 57 581 avis | ancien | Idem, 110-300 $/an par parent (estimation presse) | Prix, pas de version FR |
| [Double Holo](https://apps.apple.com/us/app/double-holo-card-scanner/id6759494054) | #10 shopping ; ~250 K$ ARR déclaré fondateur | 252 j | Scanner Pokémon + place de marché, 4.9 % de frais | Paywall vendeur durci |
| [Card Ladder](https://apps.apple.com/us/app/card-ladder/id1541535971) | #5 sports, 12 303 avis, 4.9★ | ancien | Valeur de cartes de sport | Pas creusée |
| [My Package Delivery Tracker](https://apps.apple.com/us/app/my-package-delivery-tracker/id6447516226) | #3 shopping | ancien | Suivi de colis | Demande 60 K/mois |
| [TrackPack](https://apps.apple.com/us/app/package-tracker-trackpack/id6762376278) | #4 shopping, 3.7★ | récent | Suivi de colis | Note faible |
| [Outpost Alerts](https://apps.apple.com/us/app/outpost-alerts/id6777955638) | #54 shopping | 50 j | Alertes de stock | Jeune, 0 avis |
| [MacroFactor](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471) | #12 health, 4.8★ | ancien | Suivi de macros adaptatif | Pas de FR |
| [Runna](https://apps.apple.com/us/app/runna-running-plans-coach/id1594204443) | #17 health | ancien | Plans de course | — |
| [LangLearn](https://apps.apple.com/us/app/langlearn-ai-english-tutor/id6744358897) | #8 éducation (vocal) | ancien | Tuteur d'anglais IA | — |
| [Wispr Flow](https://apps.apple.com/us/app/wispr-flow/id6497229487) | #33 productivité (vocal) | ancien | Dictée IA | — |
| App de [@julscales](https://x.com/julscales/status/2123064291305640065) | 3 100 $ MRR déclaré | ~1 mois | App iOS via TikTok organique | Canal TikTok |
| [CFO Lens](https://x.com/arsyadharmaa/status/2123250350933373015) | 3 500 $ MRR déclaré | 6 mois | Outil de pilotage financier | — |
| [HabitKit](https://www.buildmvpfast.com/blog/602k-revenue-solo-indie-hacker-app-portfolio-breakdown-2026) | 28 K$ MRR (déc. 2025, secondaire) | ~2 ans | Suivi d'habitudes à 1-2 $/mois | Prix très bas |

## 💸 Apps qui font du cash
**Revenus déclarés (déclaré, non vérifié)**
- App iOS de @julscales : 3 100 $ MRR, 3 800 $ en un mois, 7 000 téléchargements, TikTok organique, 18/11/2026. [post](https://x.com/julscales/status/2123064291305640065) (nom de l'app non donné)
- CFO Lens : 3 500 $ MRR, 19/11/2026, clients à Londres, Hong Kong, US. [post](https://x.com/arsyadharmaa/status/2123250350933373015)
- App de @zakisbuilding : 1 100 $ bruts sur 28 jours, 17/11/2026, pas du MRR. [post](https://x.com/zakisbuilding/status/2122823230540968335)
- Metrya (santé iOS) : 2 000 $ cumulés, 123 acheteurs, 14/11/2026. [post](https://x.com/rjozefowicz/status/2121589922611990926)
- ScribeKit : 30 $ MRR, 23 payants, 18/11/2026, tout vient de la recherche App Store. [post](https://x.com/truly_offline/status/2122993424723026229)
- HabitKit : 28 K$ MRR en déc. 2025, 25 100 abonnés à 1-2 $/mois, source secondaire. [article](https://www.buildmvpfast.com/blog/602k-revenue-solo-indie-hacker-app-portfolio-breakdown-2026)

**App Store US, top grossing, moins de 100k avis (un rang n'est pas un revenu)**
- #3 shopping, 11 377 avis : [My Package Delivery Tracker](https://apps.apple.com/us/app/my-package-delivery-tracker/id6447516226), suivi de colis.
- #4 shopping, 2 011 avis, 3.7★ : [Package Tracker TrackPack](https://apps.apple.com/us/app/package-tracker-trackpack/id6762376278), idem, app récente (id 676…).
- #5 sports, 12 303 avis : [Card Ladder](https://apps.apple.com/us/app/card-ladder/id1541535971), prix de cartes de sport.
- #11 shopping, 20 880 avis : [ThriftAI](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278), scanner de profit de revente.
- #12 health, 24 189 avis : [MacroFactor](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471), suivi de macros.
- #24 productivité, 24 522 avis : [Plaud](https://apps.apple.com/us/app/plaud-ai-work-companion/id6450364080), notes IA (matériel + app).
- #25 productivité, 28 756 avis : [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726), communication de co-parents.
- Mouvements : shopping a 27 apps qui entrent ou montent en 9 jours (Thrifty AI nouveau→#36, Thrift Hunt 85→#62, Scout nouveau→#58).

**Jeunes apps qui gagnent déjà (sorties il y a moins de 365 jours)**
- #54 shopping, [Outpost Alerts](https://apps.apple.com/us/app/outpost-alerts/id6777955638), 50 j, alertes de stock, aucun avis.
- #92 shopping, [FlipRaptor](https://apps.apple.com/us/app/flipraptor/id6807098970), 52 j, revente, 1 avis.
- #58 sports, [Captured Putting](https://apps.apple.com/us/app/captured-putting/id6820870213), 13 j, putting, 1.0★ sur 2 avis.
- #62 shopping, [Thrift Hunt](https://apps.apple.com/us/app/thrift-hunt-resale-scanner-ai/id6760717302), 239 j, scanner de revente, 5 avis.
- #99 shopping, [Thrifty Joe](https://apps.apple.com/us/app/thrifty-joe/id6762083255), 205 j, 4 avis.
- #10 shopping, [Double Holo](https://apps.apple.com/us/app/double-holo-card-scanner/id6759494054), 252 j, scanner Pokémon.
- Place à prendre : [QuickList](https://apps.apple.com/us/app/quicklist-ai-listing-tool/id6759634194) (#100, annonces IA) sans mise à jour depuis 251 jours.

## 🔬 App creusée #1 : ThriftAI (shopping)
**1. Identification** : [ThriftAI: Profit Identifier](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278), sortie App Store 2025-06-05, éditeur smallstack ApS (Danemark), fondateurs non trouvés. Shopping, #11 top grossing US, 20 880 avis, 4.77★. Revenu : 45 à 60 K$/mois selon des trackers tiers (estimation, non vérifié).
**2. Proposition** : photographier un objet de friperie, obtenir un prix de revente et une annonce eBay. Cible : revendeurs et chineurs. Prix : essai 3 jours, puis 9.99 $/mois ou 20-50 $/an, plus un module « sell-through » à 40 $ ([source](https://www.underpriced.app/blog/underpriced-vs-thrift-ai-2026)).
**3. Les 3 décisions qui font l'argent** (avis, estimation pour le reste)
- Onboarding : compte à rebours de 10 min dès l'installation avec offre d'essai (avis du 12/10).
- Paywall : avant la première valeur, au moment où la curiosité est la plus forte.
- Retour : l'utilisateur rescanne en magasin à chaque sortie, usage répété.
**4. Test des 3 traits**
- ✅ Une émotion pour une action : « combien vaut ce truc ? », l'envie de trouver une pépite.
- ✅ Résultat visible en quelques secondes : un prix, même si les avis disent que le traitement est lent (3 photos exigées).
- ❌ Distribution intégrée : pas de partage ni de code visible ; la croissance vient d'ailleurs.
**5. Ce qui manque** : la plainte n°1 est le piège d'essai et la facturation. « Charged in full on the day the trial was supposed to end. » Seconde plainte : prix faux (« Pricing $300 book at $20 »). MAJ il y a 25 jours, donc pas abandonnée. 29 avis sur 50 sont à 1★.
**6. Acquisition** : pubs Meta non trouvées (page « Thrift AI » ambiguë). Autres canaux : non relevés (estimation : TikTok de revendeurs).
**7. Stack** : estimation, app mobile native, vision par modèle multimodal, comparables de ventes eBay, abonnements via RevenueCat.
**8. Réplication** : complexité 6/10. Verticaux adjacents : livres, cartes, vinyles, brocante FR. Niche : un leader qui déçoit, sans vrai numéro 2 propre en français. Angle Kyle : même scan, prix fixe, essai sans carte, annonce Vinted/Leboncoin générée. Temps de dev : 6 à 8 semaines.

## 🔬 App creusée #2 : TalkingParents (productivité)
**1. Identification** : [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726), sortie 2016-04-29, éditeur Monitored Communications LLC, fondateurs non trouvés. Productivité, #25 top grossing, 28 756 avis, 4.38★. Revenu non déclaré, le rang est le seul signal.
**2. Proposition** : messagerie, appels et paiements entre parents séparés, conservés dans un registre recevable au tribunal. Prix : 7, 16 ou 32 $/mois par parent, essai 30 jours ([page](https://talkingparents.com/pricing)). Plan gratuit supprimé le 30/03/2026 selon des comparatifs.
**3. Les 3 décisions qui font l'argent**
- Onboarding : un tribunal ou un avocat impose souvent l'outil, donc l'autre parent s'inscrit de force (estimation).
- Paywall : après l'adoption obligatoire, l'enjeu émotionnel (voir ses enfants, preuve) rend la résiliation difficile.
- Retour : calendrier partagé, appels « accountable », exports PDF vendus à part.
**4. Test des 3 traits**
- ✅ Émotion : le conflit, « protect your peace ».
- ❌ Résultat en quelques secondes : le gain est un dossier, pas un résultat immédiat.
- ✅ Distribution intégrée : l'autre parent doit rejoindre, et les tribunaux prescrivent l'outil.
**5. Ce qui manque** : prix et support. « Just renewed my Subscription now it says They cannot find an active subscription. » « Now it's 40 a month. » 41 avis sur 50 sont à 1★. MAJ il y a 17 jours.
**6. Acquisition** : 30 pubs Meta actives, dont 2 lancées depuis 7 jours. Formats : dco 18, image 6, vidéo 4, carrousel 2. Accroches : « Gaslighting doesn't work when there's a transcript » ; « High conflict co-parenting takes a toll. Protect your peace with recorded interactions. » ; « Documentation matters too. »
**7. Stack** : estimation, app native iOS/Android, web, vidéo WebRTC, archivage horodaté, Stripe.
**8. Réplication** : complexité 5/10 (la recevabilité juridique est le vrai coût, pas le code). Adjacent : parents séparés, aidants, colocation. Niche : leader mal noté, concurrent OurFamilyWizard cher ; pas de version française vue. Angle Kyle : prix fixe par foyer, droit français (JAF). Temps de dev : 8 semaines.

## 🔬 App creusée #3 : Double Holo (cartes à collectionner)
Note : catégorie App Store Shopping, regroupée ici sous « cartes à collectionner ». Card Ladder (#5 sports) n'a pas été creusée, la limite de 3 fiches était atteinte.
**1. Identification** : [Double Holo: Card Scanner](https://apps.apple.com/us/app/double-holo-card-scanner/id6759494054), sortie 2026-03-12, éditeur Double Holo Inc., cofondateur Kacy Lombard. #10 shopping, 2 191 avis, 4.77★. Revenu : environ 250 K$ ARR, 40-50 K utilisateurs, dit par le cofondateur ([Teknovation](https://www.teknovation.biz/doubleholo-is-capitalizing-on-the-marketplace-for-collectibles/), date non précisée, déclaré, non vérifié).
**2. Proposition** : scanner une carte Pokémon, voir le prix du marché, puis la vendre depuis l'app. Gratuit pour scanner, premium pour alertes et ROI de grading, 4.9 % de frais vendeur, Vendor Hub (caisse de salon) payant.
**3. Les 3 décisions qui font l'argent**
- Onboarding : long, compte obligatoire (« about 50 pages to click through », avis).
- Paywall : le scan est gratuit ; l'argent vient des frais de vente, des alertes et de l'inventaire limité à 50 objets.
- Retour : alertes de prix, inventaire, boutique.
**4. Test des 3 traits**
- ✅ Émotion : la chasse à la carte valable.
- ✅ Résultat en secondes : prix en direct au scan.
- ✅ Distribution : place de marché, créateurs partenaires cités dans les avis.
**5. Ce qui manque** : paywall qui se durcit, compte obligatoire. « Now I have over 300 items in my inventory with now a sudden paywall. » « Account creation is atrocious. » MAJ il y a 47 jours.
**6. Acquisition** : pubs Meta non trouvées (pages « DoubleHolo » ambiguës). Autres canaux : créateurs de cartes cités dans les avis, SEO sur « pokemon card scanner ».
**7. Stack** : estimation, vision par ordinateur sur base de cartes, flux de prix, place de marché avec paiement.
**8. Réplication** : complexité 7/10 (base de cartes et prix). Adjacent : sports, Lorcana, monnaies. Niche : scanner francophone sans compte. Angle Kyle : scan hors ligne simple, cote Cardmarket. Temps de dev : 10 semaines.

## 📈 Tendances Émergentes
**Accroches qui reviennent** (une seule app avec pubs trouvées : TalkingParents)
- « La preuve te protège » : « Gaslighting doesn't work when there's a transcript », « Protect your peace with recorded interactions ».
- Pour les apps de revente, aucune accroche récupérée (pages Meta ambiguës) : à vérifier à la main dans la Meta Ad Library.

**Autres signaux**
- **Le piège d'essai tue la note** : ThriftAI (essai facturé en plein), TalkingParents (gratuit supprimé en mars 2026), Double Holo (paywall vendeur ajouté). Les trois ont des centaines de 1★ récents sur ce seul thème. Une promesse « sans piège » est une accroche vendable.
- **Shopping, 27 apps entrées ou montées en 9 jours** : revente par scan photo, alertes de stock, suivi de colis. Les entrants ont peu d'avis (Deals Soldier 7, Thrifted 23).
- **Alertes de restock** : la recherche Google passe de 260 à 2 400/mois en 12 mois, avec un CPC de 1.09 $.
- **Distribution TikTok organique** : une app iOS déclare 3 100 $ MRR en un mois sans pub ([post](https://x.com/julscales/status/2123064291305640065)).
- **Recherche App Store seule** : ScribeKit, 23 payants en 5 semaines ([post](https://x.com/truly_offline/status/2122993424723026229)).
- **GitHub Trending (semaine)** : outils pour agents de code (chrome-devtools-mcp, plannotator, ag-ui) et [sure](https://github.com/we-promise/sure), app de finance perso open source à 3 226 étoiles.
- **HN** : l'introduction en bourse d'Anthropic domine (1 012 pts), sans lien direct avec un produit à copier.
