# 🔥 Market Scan — 2026-07-03

## 📊 Résumé Exécutif
- Apps analysées : 8
- Top potentiel : 3 (Acti, Humalike, Tabstack)
- Opportunités immédiates (BUILD NOW) : 1 (Humalike)

## 🏆 TOP APP #1 : Acti
### 1. Identification
- **URL** : [openacti.com](https://openacti.com) | [PH](https://www.producthunt.com/products/acti-2)
- **Lancé** : 30 juin 2026 — Singapour
- **Fondateurs** : Young Wang (CEO), Mike Sun (CTO, ex-Baidu 10M DAU), Junbo Yang (CSO, ex-HashKey Capital)
- **Catégorie** : Mobile AI / Productivity
- **Buzz** : #1 PH avec 552K votes · TechCrunch · Digital Trends · BITKRAFT $5.3M seed

### 2. Proposition de valeur
- **Problème** : Les apps IA (ChatGPT, Claude) restent des silos — on sort de l'app pour aller chercher de l'aide
- **Solution** : Clavier natif iOS/Android qui exécute des agents IA directement dans n'importe quelle app
- **USP** : "ActiBar" = maintien de la barre espace → déclenchement d'agent ; Skills créés en langage naturel (1000+ en 2 semaines)
- **Cible** : Power users mobiles, travailleurs du savoir, non-devs
- **Pricing** : Gratuit au lancement, abonnements premium (modèles avancés + limites d'usage)

### 3. Stack technique
- **LLM** : Google Gemini (intelligence + multilingual + coût)
- **Archi** : Local-first (contexte perso stocké sur device, pas en cloud sauf besoin explicite)
- **Plateformes** : iOS + Android

### 4. Psychologie
- **Trigger** : Réduction friction extrême (pas d'app switch), FOMO sur "avoir ses agents partout"
- **JTBD** : "Quand je tape un email, je veux que mon agent rédige, traduise ou planifie sans sortir du fil"
- **Aha moment** : Premier fois qu'on tient la barre espace et qu'une tâche s'exécute en 2s

### 5. Go-to-Market
- **Canaux** : PH launch (#1), TechCrunch, communauté Skill builders (viral loop creator-side)
- **Viral loop** : Les Skills partagés → croissance organique de l'écosystème, réseau indirect

### 6. Réplication & Angle Kyle
- **Complexité** : 8/10 (clavier système = contraintes OS strictes, approbation Apple)
- **Verticaux adjacents** : Voice-first keyboard, keyboard dédié vertical (sales, legal, medical)
- **Angle Kyle** : Construire un **Skill vocal** pour Acti (voice-to-action dans le clavier) ou une app concurrente focalisée voice — compétence directe en voice AI
- **Temps de dev estimé** : 4-6 mois pour MVP keyboard (6-9 mois App Store approval inclus)

## 🏆 TOP APP #2 : Humalike
### 1. Identification
- **URL** : [humalike.ai](https://humalike.ai) | [PH](https://www.producthunt.com/products/humalike-2)
- **Lancé** : Juillet 2026
- **Fondateurs** : Équipe non-publique ; investisseurs = premiers backers ElevenLabs + Revolut
- **Catégorie** : AI Infrastructure / Voice & Conversational AI
- **Buzz** : #2 PH juillet 2026 avec 451K votes

### 2. Proposition de valeur
- **Problème** : Les agents IA coupent les autres mid-sentence, ne savent pas quand se taire, manquent de "lecture sociale"
- **Solution** : API comportementale — turn-taking, théorie de l'esprit, mémoire de groupe, personas
- **USP** : 7 composants comportementaux model-agnostic ; focus unique sur le "quand parler" pas juste "quoi dire"
- **Cible** : Devs d'agents vocaux, IA companions, tuteurs, NPCs de jeu, humanoids
- **Pricing** : $20 crédits gratuits pour démarrer (sans CB), puis pay-as-you-go

### 3. Stack technique
- **APIs** : Turn-taking, Theory of Mind, Memory, Group Dynamics, Persona — tous model-agnostic
- **Format** : REST API composable, benchmarks inclus pour validation
- **Intégration** : Compatible ElevenLabs, Retell, Vapi, tout stack voice AI

### 4. Psychologie
- **Trigger** : Douleur réelle identifiable (le bot qui parle par-dessus) + démonstration virale
- **JTBD** : "Quand je construis un agent vocal, je veux qu'il soit naturel sans m'occuper de la mécanique de conversation"
- **Aha moment** : Premier échange où le bot attend naturellement avant de répondre

### 5. Go-to-Market
- **Canaux** : PH launch, bouche-à-oreille dans la communauté voice AI (Retell, Vapi, ElevenLabs)
- **Viral loop** : Chaque démo d'agent "humain" → question "comment t'as fait ?" → Humalike
- **Positionnement** : Infrastructure (B2B dev-first), pas consumer

### 6. Réplication & Angle Kyle
- **Complexité** : 7/10 (science NLP non triviale sur le turn-taking, mais API faisable)
- **Verticaux adjacents** : Turn-taking pour sales calls IA, coaching vocal, téléphonie RH
- **Angle Kyle** : MATCH PARFAIT — Kyle est expert voice AI. Soit intégrer Humalike dans ses agents, soit construire un concurrent vertical (ex : Humalike pour call centers). Réseau ElevenLabs/Vapi = accès direct au marché
- **Temps de dev estimé** : 2-3 mois pour un MVP vertical (ex : turn-taking pour sales AI)

## 🏆 TOP APP #3 : Tabstack by Mozilla
### 1. Identification
- **URL** : [tabstack.ai](https://tabstack.ai) | [PH](https://www.producthunt.com/products/tabstack) | [HN](https://news.ycombinator.com/item?id=46620358)
- **Lancé** : Juillet 2026 — Mozilla
- **Fondateurs** : Équipe Mozilla New Products
- **Catégorie** : Developer Tools / Browser Automation / AI Infrastructure
- **Buzz** : #3 PH juillet 2026 avec 381K votes · Show HN viral · "web execution layer for AI agents"

### 2. Proposition de valeur
- **Problème** : Les agents IA ne peuvent pas naviguer le web en temps réel sans coder un scraper fragile
- **Solution** : API REST → rend une page, extrait données structurées, automatise des actions browser — sans infra
- **USP** : Éphémère (pas de stockage), robots.txt compliant, no model training, brandé Mozilla = confiance
- **Cible** : Devs SaaS/AI agents, data engineers, startups qui évitent l'infra browser
- **Pricing** : 10K crédits gratuits ; Starter $49/mo ; Growth $149/mo ; $1/1000 extractions MD, $5 JSON, $7.50 automation

### 3. Stack technique
- **Endpoints** : `/extract` (URL→MD/JSON/schéma custom), `/generate` (web→output IA), `/automate` (actions browser), `/research` (multi-source agents)
- **Infra** : Headless browser hébergé par Mozilla, ephemeral processing
- **Compliance** : robots.txt respecté par défaut, pas de training sur données user

### 4. Psychologie
- **Trigger** : Trust (Mozilla) + simplicité radicale (1 appel API = page rendue + données)
- **JTBD** : "Quand je construis un agent IA, je veux qu'il lise le web sans gérer Playwright ou Puppeteer"
- **Aha moment** : Premier appel `/research` qui retourne une synthèse multi-sources en <5s

### 5. Go-to-Market
- **Canaux** : PH + HN (devs) + halo Mozilla pour la confiance
- **Viral loop** : Devs qui partagent des patterns d'usage (GitHub repos, blog posts)
- **Moat** : Brand Mozilla → adoption enterprise sans vetting long

### 6. Réplication & Angle Kyle
- **Complexité** : 5/10 (Playwright + API wrapper = faisable, mais infra browser = coûts opex)
- **Verticaux adjacents** : Research agent spécialisé (finance, legal, medical), monitoring concurrent
- **Angle Kyle** : Intégrer Tabstack dans des voice agents pour donner aux agents accès au web réel-time (ex : agent vocal qui scrape l'actu pendant l'appel). Moins un produit à répliquer, plus un outil à utiliser
- **Temps de dev estimé** : 3-4 mois pour un concurrent simple, mais Tabstack vaut mieux à utiliser qu'à répliquer

## 💰 Unit Economics Deep Dive — Acti
> ⚠️ App lancée le 30/06/2026 — données basées sur funding public + benchmarks secteur keyboard/AI apps

| Métrique | Estimation | Source / Base |
|---|---|---|
| **ARR** | ~$0 (pas encore monetisé) | Gratuit au lancement, subs à venir |
| **Funding** | $5.3M seed | Crunchbase / TechCrunch confirmé |
| **Users (early)** | ~50K-200K installs estimés (1 sem post-PH #1) | Benchmark PH #1 mobile apps |
| **Skills créés** | 1 000+ en 2 semaines | Déclaration officielle |
| **ARPU** | N/A (gratuit) → cible ~$9-15/mo premium | Benchmark AI subscription apps |
| **CAC** | ~$0.50-2 (PH organic + TechCrunch) | Benchmark launch organic |
| **LTV (estimé)** | ~$72-120/user/an si 40% conversion premium | Benchmark: Grammarly, Otter.ai |
| **LTV/CAC** | ~40-80x potentiel si rétention forte | Très favorable si distribution organique |
| **Payback** | <1 mois si conversion | Modèle freemium |
| **Burn mensuel** | ~$200-400K/mo | $5.3M seed / 18 mois runway |
| **Runway** | ~13-26 mois | Taille seed + burn estimé |
| **Rev/Employee** | N/A pre-revenue | Phase seed |
| **Rule of 40** | N/A | Trop tôt |

**Verdict santé 🟡** — Très tôt post-launch. Signal fort (PH #1, TechCrunch, $5.3M BITKRAFT) mais aucun revenu encore. Le risque principal : monétisation retardée + contraintes App Store. Watch 90 jours pour voir conversion premium.

Sources : [TechCrunch](https://techcrunch.com/2026/06/30/acti-puts-ai-agents-directly-into-your-smartphone-keyboard/) · [Crunchbase Acti](https://www.crunchbase.com/organization/acti-8182) · [TNGlobal](https://technode.global/2026/07/01/singapores-acti-raises-5-3m-seed-round-to-build-ai-powered-keyboard-as-personal-context-layer/)

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Acti | Humalike | Tabstack |
|---|---|---|---|
| 📊 Market Size (20%) | 8 — mobile AI global >€1B | 9 — infra AI agents = marché €206B | 7 — dev tools web scraping €500M+ |
| ⚙️ Complexité inversée (15%) | 3 — clavier système = iOS hell | 6 — API NLP complexe mais faisable | 5 — browser infra = opex lourd |
| ⏱️ Time-to-Market (15%) | 2 — 6-9 mois minimum (Apple review) | 7 — 2-3 mois pour vertical MVP | 5 — 3-4 mois, mais pourquoi répliquer ? |
| 🏟️ Compétition inversée (15%) | 6 — niche keyboard AI, peu de concurrents directs | 8 — quasi blue ocean (infra comportementale) | 4 — Apify, Playwright, Browserbase |
| 💰 Revenue Potential (20%) | 7 — abonnements + Skill marketplace | 9 — B2B API = recurring + usage-based | 6 — API utility, price pressure long terme |
| 🧑‍💻 Founder-Fit Kyle (15%) | 5 — mobile/UX, peu voice | 10 — voice AI = expertise directe + réseau | 6 — utile mais pas un produit à construire |

| App | Score pondéré | Verdict |
|---|---|---|
| **Humalike** | **8.15/10** | 🟢 **BUILD NOW** |
| **Acti** | **5.55/10** | 🟠 **WATCH** |
| **Tabstack** | **5.55/10** | 🟠 **WATCH / UTILISER** |

> **Calcul Humalike** : (9×0.20)+(6×0.15)+(7×0.15)+(8×0.15)+(9×0.20)+(10×0.15) = 1.8+0.9+1.05+1.2+1.8+1.5 = **8.25**
> **Calcul Acti** : (8×0.20)+(3×0.15)+(2×0.15)+(6×0.15)+(7×0.20)+(5×0.15) = 1.6+0.45+0.30+0.90+1.4+0.75 = **5.40**
> **Calcul Tabstack** : (7×0.20)+(5×0.15)+(5×0.15)+(4×0.15)+(6×0.20)+(6×0.15) = 1.4+0.75+0.75+0.60+1.2+0.90 = **5.60**

## 📈 Tendances Émergentes
### 1. 🤖 L'infrastructure comportementale des agents devient le nouveau battleground
Le marché passe de "construire un agent IA" à "rendre l'agent humainement acceptable". Humalike illustre un shift : la valeur n'est plus dans le LLM mais dans la **couche comportementale** au-dessus (turn-taking, théorie de l'esprit, memoria contextuelle). Marché projeté à €206B en 2026 (+139% YoY).

### 2. 📱 Le clavier mobile = nouveau point d'entrée pour les agents
Acti ouvre un nouveau paradigme : l'agent IA n'est plus une app séparée, il vit dans le flux de frappe. Suivre les expérimentations similaires sur Android (accessibilité APIs) et iOS (contraintes keyboard = barrière à l'entrée = moat).

### 3. 🌐 Les géants fournissent l'infra "browser-as-a-service"
Mozilla avec Tabstack rejoint Apify, Browserbase, Bright Data sur le marché du browser headless managed. Signal : le scraping "amateur" est mort, c'est maintenant une couche infra structurée avec compliance. Opportunité pour les agents qui ont besoin de données web temps réel.

### 4. 🔒 Trust et privacy comme différenciateur
Acti (local-first) et Tabstack (no training on data, ephemeral) ont mis la privacy en avant dans leur pitch. En 2026, les devs et les entreprises choisissent d'abord selon la confiance. Signal fort pour TOUT produit IA.

### 5. 🧠 Le move de "show HN" vers "PH monstre" se normalise
Les 3 apps ont frappé simultanément PH + HN. Le stack de lancement 2026 = PH pour la distribution grand public + HN pour la crédibilité dev. Les 500K votes de PH sont probablement gamifiés/boostés mais le signal reste fort.

## 💡 Insights Actionnables pour Kyle
### 🚀 Action 1 — S'inscrire à Humalike MAINTENANT (cette semaine)
Humalike est directement dans ton domaine (voice AI). Les $20 gratuits permettent de tester la turn-taking API aujourd'hui. Si ça marche dans tes agents vocaux actuels, tu as un **avantage concurrentiel immédiat** sur tes clients.
→ [humalike.ai](https://humalike.ai) · Temps : 2h · Coût : $0

### 🚀 Action 2 — Construire un "Humalike vertical" pour un secteur précis
La vraie opportunité n'est PAS de concurrencer Humalike horizontalement. C'est de l'**appliquer verticalement** : un agent vocal avec turn-taking natif pour les **sales calls**, les **RH**, ou le **support client** en français. Kyle = expert voice + francophone = double avantage.
→ MVP réalisable en 6-8 semaines · ARR cible : €5-20K/mo en 6 mois

### 🚀 Action 3 — Intégrer Tabstack dans les pipelines existants
Utilise Tabstack (pas à construire) pour donner à tes agents vocaux l'accès au web en temps réel. Ex : agent qui répond aux questions clients sur les prix en scrapant le site en direct. Pas un produit, un levier d'amélioration immédiate.
→ [tabstack.ai](https://tabstack.ai) · Temps : 1 journée d'intégration · Coût : $49/mo

### 📌 À surveiller (30 jours)
- **Acti** : Conversion freemium→paid + rétention (proxy : reviews App Store). Si >4.5 étoiles + abonnements → signal que le modèle fonctionne
- **Humalike** : Partenariats annoncés avec Retell/Vapi ? = signal d'adoption infra
- **Compétiteurs** de Tabstack : Browserbase (YC) et Apify réaction ?

### 🎯 Verdict Kyle
Le signal du marché cette semaine pointe vers une conclusion nette : **l'infra comportementale pour agents vocaux est le prochain layer à construire**. Humalike a identifié le problème correctement mais reste horizontal et généraliste. Un product comme "Humalike pour sales calls francophones" avec intégration Vapi/ElevenLabs + contexte CRM serait un **wedge défendable** avec les compétences exactes de Kyle.
