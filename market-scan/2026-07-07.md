# 🔥 Market Scan — 2026-07-07

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : Wispr Flow (Voice OS, $2B valuation, Founder-Fit 9/10 pour Kyle)
- Opportunités immédiates (BUILD NOW) : 0 direct — 1 BUILD ADJACENT fort (voice vertical)
- Signal fort : AI app builders + Voice OS explosent simultanément en juillet 2026

## 🏆 TOP APP #1 : Glaze by Raycast

### 1. Identification
- **URL** : raycast.com/glaze
- **Launch** : 1er juillet 2026 (public) — beta depuis mars 2026
- **Fondateurs** : Thomas Paul Mann (CEO), Petr Nikolaev (CTO) + équipe Raycast (45 personnes)
- **Catégorie** : AI App Builder / Devtools (Mac)
- **Buzz** : #1 Product Hunt (368 votes), Fast Company, AlternativeTo, 90K followers X Raycast

### 2. Proposition de valeur
- **Problème** : Construire une app Mac custom prend des semaines et nécessite un dev Swift
- **Solution** : Tu décris en langage naturel → Glaze génère une vraie app Mac native en <5 min
- **USP** : App NATIVE (pas un web wrapper), tourne offline, dock, store communautaire de partage
- **Target** : Dev + équipes tech Mac (Cursor, Linear, Vercel l'utilisent déjà)
- **Pricing** : Inclus dans Raycast Pro (~$8/mo) — pas de coût additionnel

### 3. Stack technique
- **LLM** : Claude Code (Anthropic) + OpenAI Codex pour génération du code
- **Runtime** : Swift natif Mac — apps réelles, pas Electron
- **Infra** : Raycast existante (500K users, extensions ecosystem)
- **Distribution** : Store intégré pour partager/installer les apps générées

### 4. Psychologie & JTBD
- **JTBD** : "Je veux un outil custom pour mon workflow sans embaucher un dev ni attendre 3 semaines"
- **Aha moment** : Première app fonctionnelle dans le Dock en <5 minutes
- **Triggers** : Social proof (Cursor, Linear l'utilisent) + autorité (marque Raycast) + FOMO (beta → open)
- **Viral loop** : créer une app → la partager dans le store → adoption par d'autres Raycast users

### 5. Go-to-Market
- **Distribution gratuite** : base Raycast existante 500K+ actifs (0 CAC pour warm leads)
- **Launch** : Product Hunt #1 + Fast Company + AlternativeTo = presse diversifiée
- **Communauté** : Discord Raycast, Twitter dev community (#buildinpublic)
- **B2B** : Cursor, Linear, Vercel comme case studies → crédibilité enterprise

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (Swift runtime + génération code + store infra = non trivial)
- **Temps de dev** : 4-6 mois MVP sérieux
- **Verticaux adjacents** : "Glaze for Windows", "Glaze for browser extensions", "Glaze for CLI tools"
- **Angle Kyle** : Construire "Glaze for Voice Agents" — décris ton workflow → génère un agent vocal custom
  → Exploite exactement l'expertise de Kyle (voice AI) + le même pattern de génération
- **Sources** : [Product Hunt](https://www.producthunt.com/products/glaze-4) · [Fast Company](https://www.fastcompany.com/91546499/glaze-turns-ai-prompts-into-custom-mac-apps-in-minutes) · [Raycast Blog](https://www.raycast.com/blog/introducing-glaze)

## 🏆 TOP APP #2 : Context.dev

### 1. Identification
- **URL** : context.dev
- **Launch** : 22 mars 2026
- **Fondateurs** : Équipe YC W26 (non publics)
- **Catégorie** : AI Infrastructure / Web Enrichment API
- **Buzz** : YC-backed, Product Hunt Awards winner, forte traction dev community

### 2. Proposition de valeur
- **Problème** : Chaque produit AI doit reconstruire la même infra de scraping (proxies, rendering, markdown, logos, enrichissement) — perte massive de temps
- **Solution** : Une seule API unifiée — scrape, enrichit, structure n'importe quelle page web pour tes agents AI
- **USP** : Tout-en-un (scraping + brand data + company enrichment + screenshots) vs solutions fragmentées (Apify + Clearbit + SerpAPI + ...)
- **Target** : Fondateurs AI, dev teams construisant des agents avec données web live
- **Pricing** : Free to start, no card required, puis pay-as-you-go

### 3. Stack technique
- **Infra** : Réseau de proxies rotatifs + browser headless rendering (Playwright/Puppeteer)
- **Pipeline** : HTML → Markdown clean + NLP enrichment + brand extraction
- **API** : REST + SDKs (Python, JS), compatible Claude/GPT function calling
- **Compliance** : Gestionnaire de rate-limiting + respect robots.txt

### 4. Psychologie & JTBD
- **JTBD** : "Je veux que mon agent AI sache ce qui se passe sur le web live sans que je gère l'infra"
- **Aha moment** : Premier appel API → URL rendue en markdown propre en <1s, prête pour LLM
- **Triggers** : Pain évident (chaque AI founder a souffert du scraping) + YC label = confiance immédiate
- **Hook developer** : Free tier généreux, intégration en <30 min, doc exhaustive

### 5. Go-to-Market
- **YC network** : réseau d'early adopters AI founders via YC batch W26
- **Developer-first** : doc excellente, SDKs, exemples LangChain/AutoGen
- **Product Hunt** : Awards winner = social proof dans l'écosystème indie hacker
- **Contenu** : "Why we built this" storytelling (every AI founder a ce pain)

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (infra proxy à scale = 6-12 mois sérieusement)
- **Temps de dev** : 6-8 mois pour infra robuste
- **Verticaux adjacents** : API enrichissement pour vertical spécifique (e-commerce, legal, real estate)
- **Angle Kyle** : Construire un "Context.dev for Voice Lead Enrichment" — API qui enrichit les leads AVANT
  qu'un agent vocal appelle : who is calling, what they want, best offer to pitch
- **Sources** : [Product Hunt](https://www.producthunt.com/products/context-dev) · [LinkedIn](https://www.linkedin.com/posts/saas-radar-news_most-10-impacting-producthunt-saas-news-activity-7441725650719105025-IXYA)

## 🏆 TOP APP #3 : Wispr Flow

> ⚠️ App lancée en 2024 (>6 mois) — incluse car **explosion massive en 2026** ($260M levé mai 2026 @ $2B valuation, 100x users YoY). Signal impossible à ignorer pour Kyle.

### 1. Identification
- **URL** : wisprflow.ai
- **Launch** : App iOS 2024 / Android fév. 2026 / $260M Series B mai 2026
- **Fondateurs** : Tanay Kothari (CEO)
- **Catégorie** : Voice AI / Productivity / Voice OS
- **Buzz** : $290M levé total, $2B valuation, 270 Fortune 500 clients (Nvidia, Amazon), 40% MoM growth, TechCrunch, Yahoo Finance, VentureBurn

### 2. Proposition de valeur
- **Problème** : Taper est 4x plus lent que parler ; la dictée classique produisait des erreurs et ignorait le contexte
- **Solution** : Dictée vocale AI qui écrit dans TON style, auto-corrige en temps réel, fonctionne dans TOUTES les apps (Mac + Android)
- **USP** : Traitement on-device (privacy totale, données jamais partagées), 100+ langues, adaptation au style de l'utilisateur
- **Target** : Knowledge workers, cadres Fortune 500, Mac + Android users
- **Pricing** : ~$12-15/mo estimé (non public)

### 3. Stack technique
- **ASR** : Modèle speech-to-text local (on-device, pas cloud)
- **LLM** : Fine-tuning sur le style d'écriture de l'utilisateur
- **Intégration** : SDK macOS accessibility layer → fonctionne dans toute app
- **Android** : Stack équivalente pour Android depuis fév. 2026

### 4. Psychologie & JTBD
- **JTBD** : "Je veux dicter aussi vite que je pense, dans mes propres mots, partout"
- **Aha moment** : Première phrase dictée, corrigée, dans son propre style — en 2 secondes
- **Triggers** : Privacy (pas de cloud) + vitesse démontrée (4x faster) + adoption Fortune 500
- **Retention driver** : Plus tu l'utilises, mieux il apprend ton style → switching cost élevé

### 5. Go-to-Market
- **Enterprise top-down** : 270 Fortune 500 = réputation + revenus stables
- **Funding PR** : $25M → $260M → couverture massive (Yahoo Finance, TechCrunch, VentureBurn)
- **Organic** : Bouche-à-oreille dans les équipes (privacy-first = IT friendly)
- **Plateformes** : Mac App Store + Google Play = distribution native

### 6. Réplication pour Kyle
- **Complexité** : 8/10 (ASR on-device + fine-tuning style = expertise ML pointue)
- **Temps de dev** : 8-12 mois pour un produit compétitif
- **Angle Kyle** : Ne pas reconstruire Wispr — mais créer "Wispr for [Vertical]"
  → Voice OS for Sales Reps : dictée + brief client automatique + objection handling en temps réel
  → Voice OS for Support Agents : dictée + résumé ticket + KB lookup vocal
  → Kyle a l'expertise voice AI + réseau pour recruter les early users B2B
- **Sources** : [Yahoo Finance](https://finance.yahoo.com/news/wispr-raises-25m-build-voice-160000047.html) · [VentureBurn](https://ventureburn.com/wispr-ai-raise-25m/) · [TechCrunch Android](https://techcrunch.com/2026/02/23/wispr-flow-launches-an-android-app-for-ai-powered-dictation/)

## 💰 Unit Economics Deep Dive — Raycast (Glaze)

> Glaze est une feature de Raycast Pro, pas un produit standalone. Les métriques reflètent Raycast au global.
> Sources : Tracxn, Latka, PitchBook, Raycast blog, estimations publiques.

| Métrique | Valeur | Source / Note |
|---|---|---|
| **ARR** | ~$5.2M | Latka + estimations (500K users × ~5% Pro × $8/mo × 12) |
| **ARPU** | ~$96/an | Raycast Pro à $8/mo |
| **Paying users** | ~54 000 | ARR / ARPU |
| **Total users** | 500 000+ | Blog Raycast (2024) |
| **CAC** | ~$25-50 | Organique (SEO + dev community), pas de paid |
| **LTV** | ~$400-500 | ARPU / churn estimé 20%/an = $96 × 5 |
| **LTV/CAC** | ~10-14x | Excellent (seuil sain = 3x) |
| **Payback** | ~3-6 mois | CAC ~$35 / MRR ~$8 |
| **Employees** | 45 | LinkedIn (mai 2026) |
| **Rev/Employee** | ~$115K | $5.2M / 45 |
| **Total raised** | $47.8M | Crunchbase (Series B $30M — Atomico, sept. 2024) |
| **Burn estimé** | Non public | Probablement rentable ou proche (rev/emp élevé) |
| **Rule of 40** | ~60-70% | Croissance CAGR ~90% (2021-2025) + marges SaaS |

### Verdict santé financière : 🟢 EXCELLENTE
- LTV/CAC de 10-14x = modèle économique très sain
- Rev/Employee $115K = productivité forte pour une équipe de 45
- Glaze comme feature Pro driver peut accélérer significativement la conversion free→paid
- Risque principal : dépendance Apple/Mac OS (plateforme unique)

## 🎯 Opportunity Scorecard — Top 3
| Dimension | Poids | Glaze (Raycast) | Context.dev | Wispr Flow |
|---|---|---|---|---|
| 📊 Market Size | 20% | 8 → **1.60** | 7 → **1.40** | 9 → **1.80** |
| ⚙️ Complexity inversé | 15% | 4 → **0.60** | 4 → **0.60** | 3 → **0.45** |
| ⏱️ Time-to-Market | 15% | 4 → **0.60** | 4 → **0.60** | 3 → **0.45** |
| 🏟️ Competition inversé | 15% | 7 → **1.05** | 5 → **0.75** | 5 → **0.75** |
| 💰 Revenue Potential | 20% | 7 → **1.40** | 7 → **1.40** | 9 → **1.80** |
| 🧑‍💻 Founder-Fit Kyle | 15% | 4 → **0.60** | 5 → **0.75** | 9 → **1.35** |
| **TOTAL** | | **5.85/10** | **5.50/10** | **6.60/10** |
| **Verdict** | | 🟠 WATCH | 🟠 WATCH | 🟡 BUILD ADJACENT |

### Rationale scores
- **Glaze** : pattern brillant mais Founder-Fit faible pour Kyle (pas son domaine Swift/Mac tooling)
- **Context.dev** : infra utile mais concurrence (Firecrawl, Apify) et Kyle pas expert scraping
- **Wispr Flow** : marché validé $2B, fit parfait pour Kyle — mais reconstruire Wispr est trop dur.
  **L'opportunité réelle = verticale voice AI spécialisée** (sales, support, médical) où Kyle a le réseau.

## 📈 Tendances Émergentes
### 1. AI App Builders : la prochaine vague no-code
Glaze, Framer 3.0 (juin 2026, AI agents sur canvas), Cursor-like tools → génération de vrais artefacts logiciels depuis le langage naturel. Pas des templates : du code réel. Barrière d'entrée dev en chute libre.

### 2. Voice OS : au-delà de la dictée
Wispr Flow à $2B valuation prouve que la voix n'est plus un gadget. Le marché converge vers des "Voice OS" qui capturent toutes les interactions clavier. Vapi + ElevenLabs + Retell = stack voice agent en pleine consolidation.

### 3. AI Infra as-a-Service (AiaS) en accélération
Context.dev, Firecrawl, n8n (51K GitHub stars) → les fondateurs AI délèguent l'infra et se concentrent sur l'application. Chaque couche du stack AI (scraping, orchestration, voice, auth) est en train d'être commoditisée en API.

### 4. Privacy-first AI comme différenciateur enterprise
Wispr (on-device), Quartz (email AI local) → les entreprises Fortune 500 exigent que les données ne quittent pas leur machine. On-device AI = moat enterprise en 2026.

### 5. Distribution via base existante (anti-PH syndrome)
Glaze n'a pas besoin de conquérir de nouveaux users — il convertit 500K users Raycast existants. Tendance forte : builders qui lancent des features dans une base établie plutôt que de construire from scratch.

## 💡 Insights Actionnables
### 🥇 Insight #1 — L'opportunité Kyle : Voice OS Vertical (6-8 semaines pour valider)
Wispr Flow prouve le marché ($2B). Kyle a l'expertise. La stratégie n'est pas de le cloner mais de prendre une **verticale B2B où il a déjà un réseau** (sales teams ? support centers ? médical ?) et de construire un voice OS hyperspecialisé :
→ Dictée + enrichissement contexte client + suggestions temps réel vocales
→ Pricing B2B €50-200/seat/mois = €100K MRR avec 1000 seats
→ **Action immédiate** : identifier 10 early adopters dans son réseau, valider la douleur en 2 semaines

### 🥈 Insight #2 — Le pattern Glaze est réplicable pour voice agents
Le modèle "décris → génère un vrai artefact qui tourne" est dupliquable pour des agents vocaux.
"Décris ton workflow d'appel → Glaze génère ton script + ton agent Vapi" = produit plausible à construire.
Stack : Claude Code API + Vapi + voix ElevenLabs + UI simple. Dev estimate : 6-8 semaines MVP.

### 🥉 Insight #3 — Context.dev révèle un gap : enrichissement pre-call pour agents voice
Avant chaque appel sortant, un agent voice a besoin de contexte (qui est la personne, quelle entreprise, quel historique). Context.dev le fait pour le web, mais pas pour le use case "pre-call intelligence voice AI".
→ API pré-appel : enrichit un numéro de téléphone → profil complet → briefing vocal automatique
→ Partenariats naturels : Vapi, Bland AI, Retell comme distribution

### ⚡ Signal à surveiller
- **OpenClaw** (210K stars GitHub, ex 9K → 60K en quelques jours) : vérifier si ce projet AI open-source peut être weaponisé pour un use case voice
- **Framer 3.0** (juin 2026, AI agents sur canvas) : watch si pattern "agents dans l'interface de design" arrive dans l'UI building pour voice flows
