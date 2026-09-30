# 🔥 Market Scan — 2026-09-30

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : MosMos (voice writing), Floot MCP (AI app builder), Whiteboard IDE (YC W26)
- Opportunités immédiates (BUILD NOW) : 1 (MosMos — angle Voice AI vertical)

## 🏆 TOP APP #1 : MosMos
### 1. Identification
- **Nom** : MosMos | **URL** : [producthunt.com/products/mosmos](https://www.producthunt.com/products/mosmos)
- **Launch** : Septembre 2026 | **Catégorie** : Voice AI / Productivité macOS
- **Métriques buzz** : #1 PH le 19/09/2026 avec 391 upvotes

### 2. Proposition de valeur
- **Problème** : Prise de notes/rédaction fragmentée avant, pendant et après les réunions
- **Solution** : Workspace vocal natif macOS — touche Fn n'importe où → texte poli, adapté au contexte de l'app active
- **USP** : Adaptation du style d'écriture selon l'application (Slack vs Notion vs email), mémoire de vocabulaire perso
- **Target** : PMs, devs, opérateurs — profils qui jonglent entre meetings et docs
- **Pricing** : Non public (freemium probable)

### 3. Stack technique
- **Frontend** : Native macOS (Swift/AppKit)
- **Backend** : STT propriétaire ou Whisper + LLM pour reformulation
- **Infra** : Local-first avec sync cloud probable

### 4. Psychologie
- **Triggers** : Habitude (raccourci clavier Fn = réflexe), réduction friction cognitive
- **JTBD** : "Je veux capturer mes idées sans interrompre mon flow"
- **Aha moment** : Premier Fn dans Slack → message poli généré en 3 sec

### 5. Go-to-market
- **Canaux** : Product Hunt (#1), bouche-à-oreille communauté dev/PM
- **Viral loop** : "Envoyé avec MosMos" dans les messages (signature implicite)

### 6. Réplication
- **Complexité** : 6/10 (STT + LLM context-aware)
- **Verticaux adjacents** : Voice-to-CRM, voice-to-ticket (Jira), voice-to-PR review
- **Angle Kyle** : Extension verticale Voice AI → **MosMos for Customer Support** (transcription + reformulation agents IA)
- **Temps de dev** : 6-8 semaines MVP

## 🏆 TOP APP #2 : Floot MCP
### 1. Identification
- **Nom** : Floot MCP | **URL** : [floot.com](https://floot.com) | [PH](https://www.producthunt.com/products/floot)
- **Launch** : Sept 24, 2026 (2e lancement) | YC S25 | **Catégorie** : Dev Tools / AI App Builder
- **Métriques** : $220K ARR estimé (2025), 600+ paying customers, YC W26 Demo Day

### 2. Proposition de valeur
- **Problème** : Construire une app full-stack depuis Claude/ChatGPT = setup DB/auth/hosting douloureux
- **Solution** : MCP server → Claude/ChatGPT provisionnent DB, auth, storage, email, hosting en 0 setup
- **USP** : Zéro token Floot facturé — tourne sur le plan Claude existant de l'utilisateur
- **Target** : Vibe coders, indie hackers, no-coders agentiques
- **Pricing** : Freemium + plans team

### 3. Stack technique
- **Frontend** : React + Next.js (web preview live)
- **Backend** : MCP server exposé à Claude/ChatGPT
- **Infra** : Floot gère DB, auth, storage, email, hosting (Vercel-like)

### 4. Psychologie
- **Triggers** : "Build inside Claude" = zéro friction de context-switching
- **JTBD** : "Je veux shipper une app sans quitter mon LLM"
- **Aha moment** : Première preview live générée par Claude en <2 min

### 5. Go-to-market
- **Canaux** : PH, communauté vibe-coding, YC network, guides SEO "how to build with Claude"
- **Viral loop** : Chaque app publiée = badge "Built with Floot"
- **Activation rate** : 3-4x vs SaaS comparable (pas de "cold start")

### 6. Réplication
- **Complexité** : 8/10 (infra MCP + orchestration multi-service)
- **Verticaux adjacents** : Floot for Voice Apps, Floot for n8n/Zapier agents
- **Angle Kyle** : Partenariat/intégration Floot pour déployer des voice agents en 1 prompt
- **Temps de dev** : 4-6 mois (infrastructure lourde)

## 🏆 TOP APP #3 : Whiteboard IDE
### 1. Identification
- **Nom** : Whiteboard IDE | **URL** : [github.com/fesoliveira014/whiteboard](https://github.com/fesoliveira014/whiteboard) | [HN](https://news.ycombinator.com/item?id=49833867)
- **Launch** : Sept 2026 | YC W26 | **Catégorie** : Dev Tools / AI-assisted Architecture
- **Métriques** : Multiple forks GitHub, buzz HN Show HN, YC-backed

### 2. Proposition de valeur
- **Problème** : Les devs sautent directement dans VS Code sans phase de conception — les agents IA aussi
- **Solution** : IDE canvas-first pour architecturer AVANT de coder; specs + diagrammes connectés au code
- **USP** : Diff AST-aware en Rust, traces d'agents inspectables, MIT open-source
- **Target** : Senior engineers, tech leads, équipes avec agents IA codeurs
- **Pricing** : Open-source gratuit + hosted pour équipes (prévu)

### 3. Stack technique
- **Frontend** : Basé sur CodeOSS (VS Code open source)
- **Backend** : Rust (diff viewer AST-aware)
- **Infra** : Local-first, self-hostable, hosted teams en roadmap

### 4. Psychologie
- **Triggers** : Autorité (YC W26), légitimité open-source (MIT)
- **JTBD** : "Je veux comprendre ce que mon agent IA a décidé et pourquoi"
- **Aha moment** : Jump diagram → code avec keybinding VSCode familier

### 5. Go-to-market
- **Canaux** : HN Show HN, GitHub stars, YC network, bouche-à-oreille devs
- **Viral loop** : Stars GitHub + forks (déjà multiple repos miroirs)

### 6. Réplication
- **Complexité** : 9/10 (fork CodeOSS + Rust AST diff + agent tracing)
- **Verticaux adjacents** : Whiteboard for voice app workflows, diagram-to-prompt
- **Angle Kyle** : Trop complexe à répliquer — opportunité de **plugin voice layer** sur Whiteboard
- **Temps de dev** : 6-12 mois (projet d'infrastructure)

## 💰 Unit Economics Deep Dive — MosMos
*Estimations basées sur comparables sectoriels Voice AI / macOS productivity (données publiques limitées pour MosMos — app récente)*

| Métrique | Estimation | Source / Base |
|---|---|---|
| ARR | ~$50-150K | Early-stage, PH #1, pas de pricing public |
| ARPU | ~$10-20/mois | Benchmarks productivity apps macOS |
| Users payants | ~500-2 000 | Ratio upvotes PH × conversion typical 2-5% |
| CAC | ~$5-15 | Distribution organique PH + bouche-à-oreille |
| LTV | ~$120-240 | 12 mois rétention moyenne (churn ~8%/mois) |
| LTV/CAC | ~10-20x | Excellent pour early-stage |
| Payback period | <1 mois | CAC très faible (viral/organique) |
| Burn estimé | ~$20-50K/mois | 2-4 fondateurs + infra cloud |
| Runway | Bootstrapped probable | Pas de levée annoncée |
| Rev/Employee | ~$25-50K ARR | 3-5 personnes estimées |
| Rule of 40 | 🟡 Incalculable (trop early) | Croissance forte mais burn inconnu |

**Verdict santé : 🟡 EARLY PROMISING**
> LTV/CAC exceptionnel grâce au distribution organique. Modèle sain si rétention tient >6 mois. Principal risque : Apple peut nativer la feature (Fn = déjà touche dictée système).

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | MosMos | Floot MCP | Whiteboard IDE |
|---|---|---|---|
| 📊 Market Size (20%) | 7 — $500M+ voice productivity | 9 — $2B+ AI dev tools | 6 — $200M enterprise IDE |
| ⚙️ Complexity inversé (15%) | 6 — STT+LLM+context | 3 — infra MCP lourde | 2 — fork CodeOSS+Rust |
| ⏱️ Time-to-Market (15%) | 7 — 6-8 semaines MVP vertical | 3 — 4-6 mois | 2 — 6-12 mois |
| 🏟️ Competition inversé (15%) | 6 — Whisper apps, Otter.ai | 5 — Bolt, Lovable, Cursor | 7 — niche peu saturée |
| 💰 Revenue Potential (20%) | 8 — B2B vertical = $50K+ MRR | 7 — freemium → teams | 5 — open-source + hosted |
| 🧑‍💻 Founder-Fit Kyle (15%) | **9** — Voice AI expert + SaaS | 5 — infra pas son coeur | 4 — IDE = autre monde |

**Score pondéré :**

| App | Score | Verdict |
|---|---|---|
| **MosMos (vertical angle)** | **7.35** | 🟢 **BUILD NOW** |
| **Floot MCP** | **5.30** | 🟠 **WATCH** |
| **Whiteboard IDE** | **4.60** | 🟠 **WATCH** |

## 📈 Tendances Émergentes
1. **Voice-as-Primary-Interface** : MosMos confirme le passage de "voice en option" à "voice par défaut". Les apps qui intègrent la voix comme geste principal (pas bouton audio) explosent.

2. **MCP = nouveau standard d'intégration AI** : Floot, tiun, NOAN — tout s'intègre en MCP. Le "MCP-first" devient le "mobile-first" de 2026 pour les dev tools.

3. **Canvas + Code = nouveau paradigme IDE** : Whiteboard, Reladraw — les devs veulent penser visuellement AVANT de coder, surtout avec des agents IA autonomes.

4. **YC W26 = batch AI infrastructure** : 14 startups à $1M+ ARR avant Demo Day — le signal le plus fort : les fondateurs YC shipper et monétisent avant même de pitcher.

5. **Local-first revival** : StemDeck, Whiteboard, NimbleGate — la communauté HN pousse fort le local-first comme réponse à la dépendance cloud/API.

## 💡 Insights Actionnables
### 🎯 Pour Kyle — Actions immédiates

**1. BUILD NOW : Voice-to-[Vertical] SaaS (inspiré MosMos)**
> MosMos prouve le product-market fit du "voice context-aware". Kyle peut construire la même chose mais verticalisée :
> - **Voice-to-CRM** : Fn après un appel → fiche contact/CRM mise à jour auto
> - **Voice-to-Support** : Agent call → ticket Zendesk structuré auto
> - **Voice-to-Onboarding** : Script vocal → documentation produit générée
> Stack : Whisper/AssemblyAI + Claude + intégration CRM → MVP en 6 semaines

**2. WATCH : Monitorer Floot MCP pour intégration**
> Dès que Floot ouvre son API partenaire, construire "Voice App on Floot" — un template deployable en 1 prompt Claude qui provisionne un voice agent fonctionnel avec backend.

**3. SIGNAL FAIBLE : Whiteboard IDE + Voice Layer**
> Plugin "voice architecture" pour Whiteboard — décrire un système à l'oral → générer les diagrammes/specs. Niche mais forte cohérence avec l'expertise Kyle.

**4. TACTIQUE IMMÉDIATE : Publier un Show HN**
> La communauté HN de septembre 2026 est réceptive aux projets voice+local+open-source. Un "Show HN: I built a voice-to-CRM agent in 6 weeks" peut générer 200-400 upvotes et des early adopters qualifiés.
