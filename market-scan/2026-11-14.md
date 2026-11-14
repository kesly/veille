# 🔥 Market Scan — 2026-11-14

> Collecte : treg 5/5 sources, 11 recherches extended, GitHub Trending ok, 2 pages lues, 3 candidats creusés (fiches App Store + avis).

## 📊 Résumé Exécutif
- Apps au radar : 15 · creusées : 3
- Mon pari : Pari #1 Co-parentalité à prix plat (6.4/10, 🟡 BUILD ADJACENT)
- Opportunités immédiates (BUILD NOW) : 0 (aucun pari ≥ 7.5)
- Fil rouge du jour : les leaders payants de 3 niches (suivi colis, co-parentalité, nettoyeurs) se font massacrer en avis 1★ pour leur paywall. Le trou est le même partout : l'abonnement perçu comme un piège.

## 🧭 Où l'argent se déplace
Demande : volume Google US/mois, CPC, tendance 12 mois (source `demand`, 14 nov.).

| Niche (catégorie) | Mouvement | Demande | Leaders et faiblesse | Part à prendre |
|---|---|---|---|---|
| Suivi de colis (shopping) | #3 My Package Delivery Tracker, #4 TrackPack, #11 Parcels Hub, nouveau #100 Package Tracker (29 j) | « parcel tracking app » 720, CPC 3,13 $, plat ; « package tracker app » 210 | 4,4★/11k avis ; 31 avis 1★ sur 50 contre l'abo forcé ; MAJ 51 j | **oui** : abonnement perçu comme arnaque, 4 apps dans le top 11 |
| Co-parentalité (productivité) | #23 OurFamilyWizard, #24 TalkingParents, AppClose 50→29 en 7 j | « co-parenting app » 27 100, CPC 5,31 $, en baisse (49 500→8 100) | TalkingParents 4,4★ mais 41/50 avis 1★ ; fin du plan gratuit mars 2026 (tiers) | **oui** : prix et support ; pas de version FR (non vérifié) |
| Nettoyage du téléphone (utilitaires) | Content Manager 50→14 en 1 j, SmartClean 75→55, CleanNova nouveau→79, AI Security nouveau→72 (7 j) | « phone cleaner app » 4 400, CPC 4,18 $ ; « duplicate photo cleaner » 1 300, CPC 5,52 $ | 26/50 avis 1★ : faux « gratuit », annulation impossible | **à creuser** : demande réelle, mais saturé et Apple surveille les abos |
| Scanners de revente et cartes (shopping/sports) | Thrifted 73→58, Thrift Hunt nouveau→68, Sports Card Scanner Spoly 90→73, Cardstock 83→72 | « sports card scanner » 4 400, CPC 2,84 $, +50 % sur 12 mois ; « reseller app » 2 900, CPC 5,23 $ ; « thrift scanner app » 10 | Un test tiers trouve ThriftAI juste 1 fois sur 11 (Android) | **à creuser** : déjà vu 3 fois, aucun nouvel élément fort |
| Permis et examens (éducation) | DMV Practice Test nouveau→91, CDL Prep nouveau→99 | « dmv practice test » 110 000, CPC 0,32 $ ; « cdl practice test » 33 100, CPC 1,44 $ | Revenus estimés tiers seulement (Android 90 K$/mois, non vérifié) | **à creuser** : demande énorme mais CPC bas, marché US par État |
| Langue des signes (éducation) | Ziggy nouveau→53 | « learn asl » 14 800, CPC 2,83 $, pic 27 100 | 4,8★/7k avis | **à creuser** : déjà vu, version LSF à valider |
| Alertes de réassort (shopping) | Snag nouveau→90, Outpost 0 avis→83 | « in stock alerts » 390 (880 récents), CPC 1,36 $ | Apps jeunes, quasi sans avis | **non** pour l'instant : volume trop faible |
| Wallet / cartes (shopping) | Pass2U 74→53, Walletsmith 75→57 | « apple wallet pass » 320, CPC 8,34 $ | Petites apps, peu d'avis | **à creuser** : CPC élevé, niche B2B |

Aucune niche vocale ce jour.

## 🎯 Quoi builder
### Pari #1 : Co-parentalité à prix plat
- **L'idée** : pour les parents séparés, une messagerie à registre inaltérable et export PDF, au prix d'un foyer (≈ 6 €/mois) et non par parent.
- **Preuve d'argent** : [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726) #24 productivité ; [OurFamilyWizard](https://apps.apple.com/us/app/ourfamilywizard-co-parent-app/id497405393) #23. Demande « co-parenting app » 27 100/mois, CPC 5,31 $, en baisse sur 12 mois.
- **Le trou** : 41/50 avis 1★ sur TalkingParents (fiche App Store) : « Now it's 40 a month ». Plan gratuit supprimé en mars 2026 (sources tierces). Version FR non vérifiée.
- **Pourquoi Kyle** : SaaS full-stack, marché francophone sous-servi (estimation), pas de voix requise.
- **MVP** : messagerie horodatée non modifiable ; calendrier de garde partagé ; export PDF. 6–8 semaines.
- **Argent** : paywall au 1er export PDF ou au-delà de 30 messages ; 5,99 €/mois par foyer.
- **Acquisition** : SEO et pub Reddit/Meta. Accroche : « Une preuve écrite, pas un abonnement par parent ».
- **Test en 48 h** : landing + 100 € de pub ; go à 30 e-mails, stop sous 10.

### Pari #2 : Suivi de colis sans piège
- **L'idée** : app gratuite pour suivre tous ses colis (Colissimo, Mondial Relay, Vinted Go) par transfert d'e-mail ; premium 2,99 €/mois.
- **Preuve d'argent** : [My Package Delivery Tracker](https://apps.apple.com/us/app/my-package-delivery-tracker/id6447516226) #3 shopping ; [TrackPack](https://apps.apple.com/us/app/package-tracker-trackpack/id6762376278) #4. « parcel tracking app » 720/mois, CPC 3,13 $.
- **Le trou** : « why do i have to pay a subscription just to track 1 package??? » (avis, 31/50 en 1★).
- **Pourquoi Kyle** : petit produit, API de transporteurs et parsing d'e-mails, dev solo.
- **MVP** : ajout par numéro ; import e-mail ; notifications. 3–4 semaines.
- **Argent** : suivi gratuit, alertes avancées payantes à 2,99 €/mois.
- **Acquisition** : ASO « suivi colis ». Accroche : « Suivre un colis ne devrait pas coûter d'abonnement ».
- **Test en 48 h** : landing + post r/vinted/r/france ; go à 40 inscrits, stop sous 15.

### Pari #3 : Nettoyeur de photos honnête
- **L'idée** : app iPhone à prix unique (≈ 14,99 €) qui supprime doublons et captures, sans essai piégé.
- **Preuve d'argent** : [Content Manager](https://apps.apple.com/us/app/content-manager-ai-%D1%81leaner/id1541639300) #14 (50→14 en 1 j) ; SmartClean AI #55 (75→55 en 7 j). « phone cleaner app » 4 400/mois, CPC 4,18 $.
- **Le trou** : « Says on ad "no subscriptions"… You do have subscriptions! » (avis).
- **Pourquoi Kyle** : produit simple, mais natif iOS ; moins adapté à son profil web (estimation).
- **MVP** : détection de doublons ; tri de captures ; aperçu des Go gagnés. 6–8 semaines.
- **Argent** : analyse gratuite, paywall au résultat (Go libérables) ; achat unique.
- **Acquisition** : vidéos TikTok avant/après. Accroche : « Un prix. Pas de piège. »
- **Test en 48 h** : vidéo TikTok + landing ; go à 100 liste d'attente, stop sous 30.

**Mon pari : #1 — Co-parentalité à prix plat**, car c'est le trou le plus net (41/50 avis 1★) avec le CPC le plus élevé (5,31 $) et un marché francophone probablement vierge.

## 🧮 Scorecard des paris
| Pari | 📊 Marché 20% | ⚙️ Complex. 15% | ⏱️ TTM 15% | 🏟️ Concur. 15% | 💰 Revenu 20% | 🧑‍💻 Fit 15% | **Score** | 3 traits | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| #1 Co-parentalité | 7 | 6 | 6 | 6 | 7 | 6 | **6.4** | 2 | 🟡 BUILD ADJACENT |
| #2 Suivi colis | 5 | 8 | 8 | 5 | 5 | 8 | **6.35** | 1 | 🟡 BUILD ADJACENT |
| #3 Nettoyeur photos | 7 | 5 | 6 | 3 | 7 | 5 | **5.65** | 2 | 🟠 WATCH |

Les notes sont des estimations, sans revenu vérifié. Les pondérations donnent un écart de 0,05 entre #1 et #2 : à ce niveau, c'est un ex æquo. Le #1 pèse davantage sur le CPC et le trou de prix.

## 💰 Unit Economics — Pari #1 : Co-parentalité à prix plat
Tout est `estimation` : aucune source directe pour les revenus des comparables (ni Crunchbase, ni SimilarWeb consultés).

| Indicateur | Estimation |
|---|---|
| Hypothèse | 6 €/mois par foyer, 12 mois, 3 000 foyers payants |
| ARR | ≈ 216 000 € (3 000 × 72 €) |
| ARPU | 72 €/an par foyer |
| Users | 3 000 payants (≈ 30 000 inscrits, 10 % de conversion) |
| CAC | 25 € (SEO + pub à petit budget) |
| LTV | ≈ 130 € (durée moyenne 22 mois, forte rotation après la procédure) |
| LTV/CAC | ≈ 5 |
| Payback | ≈ 5 mois |
| Burn | ≈ 2 000 €/mois (hébergement, vidéo, pub) |
| Runway | long : solo, financé par les revenus |
| Rev/Employee | ≈ 216 000 € (1 personne) |
| Rule of 40 | non pertinent à ce stade |

**Verdict 🟡** : l'économie unitaire est bonne sur le papier, mais l'hypothèse de 3 000 foyers en un an est ambitieuse. Risque principal : la valeur juridique d'un registre en France, à valider avant de construire.

## 🔭 Radar — 15 apps
| App | Signal | Âge | Ce qu'elle vend | Piste |
|---|---|---|---|---|
| [My Package Delivery Tracker](https://apps.apple.com/us/app/my-package-delivery-tracker/id6447516226) | #3 shopping, 11k avis | 1 200 j | Suivi de colis, essai 3 j puis abonnement hebdo (prix non relevé) | Suivi gratuit sans piège |
| [Package Tracker – TrackPack](https://apps.apple.com/us/app/package-tracker-trackpack/id6762376278) | #4 shopping, 3,7★ | jeune (estimation) | Suivi de colis | Même trou |
| [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726) | #24 productivité, 28k avis | 3 850 j | Messagerie co-parents, 7–32 $/mois/parent | Prix plat, version FR |
| [OurFamilyWizard](https://apps.apple.com/us/app/ourfamilywizard-co-parent-app/id497405393) | #23 productivité, 57k avis | ancien | Co-parentalité, 110–300 $/an/parent (estimation tiers) | Idem |
| [Content Manager](https://apps.apple.com/us/app/content-manager-ai-%D1%81leaner/id1541639300) | #14 utilitaires, 50→14 en 1 j | 2 137 j | Nettoyage photos, essai puis abo | Nettoyeur honnête |
| [ThriftAI](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278) | #8 shopping, 20k avis | récent | Scanner de revente, 9,99 $/mois (tiers) | Prix fiables, marché FR |
| [Snag: Restock Alerts](https://apps.apple.com/us/app/snag-restock-alerts/id6828241536) | #90 shopping | 8 j | Alertes de réassort | Test précoce |
| [Hudl](https://apps.apple.com/us/app/hudl/id412223222) | 65→15 sports en 3 j | ancien | Vidéo sportive d'équipes | Saisonnier, grand groupe |
| [CHANI](https://apps.apple.com/us/app/chani-your-astrology-guide/id1532791252) | #17 lifestyle, 4,9★ | ancien | Astrologie, abonnement | — |
| [MacroFactor](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471) | #12 santé, 4,8★ | ancien | Suivi de macros | Version FR |
| BoldVoice: Accent Training | nouveau→#95 éducation | ? | Coaching d'accent par IA (vocal) | Vocal, non retenu |
| Ziggy: Learn ASL | nouveau→#53 éducation | ? | Langue des signes, 7k avis | LSF (déjà vu) |
| [helumi](https://trustmrr.com/startup/helumi) | 916 $ MRR déclaré | ~1 mois | Stockage cloud dans le Finder Mac | — |
| MagicSlides & co (Sanskar) | 1 M$ cumulés déclaré | plusieurs années | PDF/vidéo vers présentations | — |
| [lightapaw](https://www.reddit.com/r/SideProject/comments/1xv6l3f/) | 106 pts Reddit, 25k pages | 8 j | Mémorial 3D d'animaux, extras payants | Émotion + partage, sans montant |

Catégories : shopping, productivité, utilitaires, sports, lifestyle, santé, éducation, web/Mac. Une seule app vocale (BoldVoice).

## 💸 Apps qui font du cash
**Revenus déclarés** (déclaré, non vérifié sauf mention)
- helumi (app Mac, stockage cloud dans le Finder) : 916 $ MRR, 9 nov. 2026 — [post](https://x.com/letcontactabhi/status/2119685259348635928). TrustMRR affiche 991 $ MRR et 1 569 $ sur 30 j (lecture des paiements, plus fiable) — [fiche](https://trustmrr.com/startup/helumi).
- Portefeuille de Sanskar (MagicSlides, Sheet AI à 2 000 $ MRR…) : plus de 1 M$ cumulés, ~1 000 clients payants/mois, 11 nov. 2026 — [post Starter Story](https://x.com/starter_story/status/2120311453987287229). Déclaré, non vérifié.
- App mobile de @celal_dev : de 0 à 8 K$ de revenu, 1,5–2 K$/mois, 100 % organique, 10 nov. 2026 — [post](https://x.com/celal_dev/status/2120217269934453145). Produit non identifié : à prendre avec prudence.
- Dosti Pro (appels vidéo Android, Inde) : 7 839 ₹ encaissés en un jour, 44 paiements, 10 nov. 2026 — [post](https://x.com/iamvenkatadri/status/2120165133259350431).
- App Android de @engwaliullah : 32 $ le premier mois, 11 nov. 2026 — [post](https://x.com/engwaliullah/status/2120555319864746128). Anecdote, très petit.
- lightapaw (mémorial 3D d'animaux, gratuit + extras payants) : traction (25 000 animaux, 657 000 bougies) mais aucun montant déclaré — [Reddit](https://www.reddit.com/r/SideProject/comments/1xv6l3f/).

**App Store US (top grossing, < 100k avis, hors jeux)** — un rang n'est pas un revenu
- #3 shopping, 11 276 avis : [My Package Delivery Tracker](https://apps.apple.com/us/app/my-package-delivery-tracker/id6447516226), suivi de colis, 1 300 transporteurs.
- #4 shopping, 1 896 avis : [Package Tracker – TrackPack](https://apps.apple.com/us/app/package-tracker-trackpack/id6762376278), même besoin, 3,7★.
- #14 utilitaires, 60 588 avis (50→14 en 1 j) : [Content Manager](https://apps.apple.com/us/app/content-manager-ai-%D1%81leaner/id1541639300), nettoyage photos/contacts.
- #24 productivité, 28 751 avis : [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726), messagerie de co-parents opposable au tribunal.
- #8 shopping, 20 853 avis : [ThriftAI](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278), scanner de prix de revente.
- #15 sports (65→15 en 3 j) : [Hudl](https://apps.apple.com/us/app/hudl/id412223222), vidéo et analyse sportive.
- #53 éducation, nouveau : Ziggy: Learn ASL (7 227 avis, 4,8★, lien non relevé par la collecte), langue des signes.

**Jeunes apps qui gagnent déjà** (liste « Âge »)
- #90 shopping, [Snag: Restock Alerts](https://apps.apple.com/us/app/snag-restock-alerts/id6828241536) : sortie il y a 8 j, 4 avis, alertes de réassort.
- #83 shopping, [Outpost Alerts](https://apps.apple.com/us/app/outpost-alerts/id6777955638) : sortie il y a 44 j, 0 avis, même niche.
- #100 shopping, [Package Tracker・Order Tracking](https://apps.apple.com/us/app/package-tracker-order-tracking/id6818790265) : 29 j, 6 avis.
- #71 shopping, [Thrifty Joe](https://apps.apple.com/us/app/thrifty-joe/id6762083255) : 199 j, 4 avis, scanner de revente.
- #68 shopping, [Thrift Hunt](https://apps.apple.com/us/app/thrift-hunt-resale-scanner-ai/id6760717302) : 233 j, 2 avis.
- Leader sans mise à jour > 180 j : aucun dans la liste (Patina, #80, est à 150 j).
- Constat : 5 apps de moins de 250 jours classées top 100 shopping avec moins de 10 avis. Elles encaissent sans base d'avis, signe d'acquisition payante (estimation).

## 🔬 App creusée #1 : TalkingParents (productivité / co-parentalité)
1. **Identification** : [TalkingParents](https://apps.apple.com/us/app/talkingparents-co-parent-app/id1092220726), Monitored Communications LLC, sortie App Store 2016-04-29, productivité, #24 top grossing US, 28 751 avis (4,4★), MAJ il y a 11 j. Fondateurs non relevés.
2. **Valeur** : parents séparés, messagerie et appels qui laissent un registre inaltérable, recevable en justice. Prix par parent : 7 / 16 / 32 $ par mois (sources tierces, à vérifier). Plan gratuit supprimé le 30 mars 2026 (tiers).
3. **Les 3 décisions** (estimation, d'après fiche et avis) : onboarding par Apple ID ; paywall au moment où le parent a besoin du registre ou des appels vidéo, donc sous stress ; retour par l'obligation judiciaire de communiquer par l'app.
4. **3 traits** : émotion ✅ (conflit, peur de « ne pas être cru ») ; résultat visible en quelques secondes ❌ ; distribution intégrée ✅ (l'autre parent doit s'inscrire, effet réseau forcé).
5. **Ce qui manque** : 41 avis 1★ sur 50. Plaintes : prix après fin du gratuit, support injoignable, abonnement impossible à confirmer via Apple ID. « Now it's 40 a month » ; « Over priced. No customer service. Glitches. » App mise à jour : pas de trou de MAJ.
6. **Acquisition** : 30 pubs Meta actives, 3 lancées depuis 7 j ; formats DCO 19, image 6, vidéo 3, carrousel 2. Accroches : « Gaslighting doesn't work when there's a transcript » ; « High conflict co-parenting takes a toll. Protect your peace with recorded interactions » ; formules de pension par État. Page de 26 584 likes. Autre canal : prescription par avocats et juges (estimation).
7. **Stack** (estimation) : mobile natif + web, messagerie horodatée, vidéo WebRTC, export PDF.
8. **Réplication** : 6/10 (messagerie sûre et export opposable : surtout de la confiance). Verticaux voisins : tutelle de proches, colocation, familles recomposées. Niche : un « TalkingParents » à prix plat sans fiche tarifaire par parent. Angle Kyle : version FR (convention parentale, pension). Dev : 6–8 semaines.

## 🔬 App creusée #2 : My Package Delivery Tracker (shopping)
1. **Identification** : [My Package Delivery Tracker](https://apps.apple.com/us/app/my-package-delivery-tracker/id6447516226), MultiApp Dynamics OU, sortie 2023-08-01, shopping, #3 top grossing US, 11 276 avis (4,4★), MAJ il y a 51 j (« bugs corrigés »). Gratuit à l'installation.
2. **Valeur** : tous les colis dans une app, 1 300 transporteurs. Prix exact non relevé : abonnement hebdomadaire après essai de 3 jours (cité dans les avis).
3. **Les 3 décisions** (d'après avis) : onboarding court menant à un numéro de suivi ; paywall immédiat, avant le premier résultat utile (l'utilisateur est inquiet pour son colis) ; retour par les notifications de livraison.
4. **3 traits** : émotion ✅ (« où est mon colis ») ; résultat en quelques secondes ❌ (bloqué par le paywall) ; distribution intégrée ❌.
5. **Ce qui manque** : 31 avis 1★ sur 50, quasi tous contre le paywall. « why do i have to pay a subscription just to track 1 package??? » ; « You have to pay weekly… tracking a package should be free ». Annulation après essai jugée trompeuse.
6. **Acquisition** : `pubs Meta non trouvées` (aucune page d'app sûre). Canal probable : ASO sur « package tracker » (estimation).
7. **Stack** (estimation) : agrégateur d'API de transporteurs, notifications push.
8. **Réplication** : 4/10 (agrégation d'API déjà vendue, plus parsing d'e-mails). Verticaux : réassort, retours, billets. Niche : leader qui déçoit, 4 apps dans le top 11 shopping, nouvelle entrante à 29 j. Angle Kyle : transporteurs FR (Colissimo, Mondial Relay, Chronopost, Vinted Go), suivi gratuit, monétisation sur alertes avancées. Dev : 3–4 semaines.

## 🔬 App creusée #3 : Content Manager: AI Cleaner (utilitaires)
1. **Identification** : [Content Manager: AI Cleaner](https://apps.apple.com/us/app/content-manager-ai-%D1%81leaner/id1541639300), DevMeApp, sortie 2021-01-06, utilitaires, #14 (50→14 en 1 jour), 60 589 avis (4,4★), MAJ il y a 2 j.
2. **Valeur** : trie photos, vidéos, doublons et contacts pour libérer du stockage. Année gratuite pour étudiants. Prix : non relevé (un avis cite 50 $ en attente).
3. **Les 3 décisions** (estimation, d'après avis) : onboarding qui lance une analyse ; paywall au moment où l'utilisateur voit son espace récupérable ; retour par rappels de nettoyage.
4. **3 traits** : émotion ✅ (soulagement, téléphone plein) ; résultat visible en quelques secondes ✅ (Go libérés) ; distribution intégrée ❌.
5. **Ce qui manque** : 26/50 avis 1★ : faux « gratuit », essai impossible à annuler. « Says on ad "no subscriptions"… You do have subscriptions! » ; « Impossible to cancel without being charged. » Pas de trou de MAJ.
6. **Acquisition** : `pubs Meta non trouvées` (pages homonymes écartées). Les avis évoquent des pubs intrusives dans d'autres apps (estimation : achat média).
7. **Stack** (estimation) : iOS natif, Photos framework, détection de doublons par hash et vision locale.
8. **Réplication** : 6/10 (API Photos, performances, validation App Review). Verticaux : nettoyage de contacts, de mails. Niche : leader qui déçoit, mais marché saturé. Angle Kyle : prix unique sans essai piégé, en français. Dev : 6–8 semaines en natif. Demande : « phone cleaner app » 4 400/mois, CPC 4,18 $.

## 📈 Tendances Émergentes
**Accroches publicitaires** (seule app avec pubs trouvées : TalkingParents ; les deux autres sans page Meta sûre)
- Preuve par la trace écrite : « Gaslighting doesn't work when there's a transcript », « recorded interactions ».
- Éducation avant la vente : formules de pension par État (contenu SEO en pub).
- Promesse de « gratuit » ou « sans abonnement » dans les pubs de nettoyeurs, contredite à l'ouverture de l'app (avis Content Manager).

**Autres signaux**
- Le paywall perçu comme piège est la première cause d'avis 1★ de la journée (colis 31/50, co-parentalité 41/50, nettoyeur 26/50). Un « prix honnête » est un angle de produit.
- Réassort, scan de revente et cartes à collectionner : beaucoup de petites apps jeunes dans le top 100 shopping (mouvements sur 3 j).
- Dev/IA : Claude Meetings (268 votes PH), skills d'agents en tête de GitHub Trending, « computer-use » et sandboxes pour agents. Rien de directement copiable en app grand public.
- Bruit : panne FAA nationale (1 436 pts HN), sans lien avec le marché des apps.
- Repères tiers (non vérifiés) : médiane de 143 $ MRR pour 305 apps mobiles (TrustMRR, oct. 2026).
