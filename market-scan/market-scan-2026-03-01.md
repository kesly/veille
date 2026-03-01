# 🔥 Market Scan — 2026-03-01

## 📊 Résumé Exécutif
- **Apps scannées** : 15+ (Product Hunt trending, HN Show HN, Reddit r/SaaS + r/SideProject)
- **Apps à fort potentiel** : 5
- **Opportunités immédiates** : 2 (Flowglad, Friendware)

### Tendance dominante
L'écosystème se cristallise autour de **l'AI-native infrastructure** : les outils qui permettent aux développeurs de shipper plus vite avec des agents IA (billing MCP-ready, scaling Postgres sans migration, demos automatisées). Les apps "AI as a feature" saturent ; ce qui gagne = **AI as infrastructure**.

---

## 🏆 TOP APP #1 : Flowglad 🔥

### 1️⃣ IDENTIFICATION
| Champ | Détail |
|-------|--------|
| **Nom** | Flowglad |
| **URL** | https://flowglad.com |
| **GitHub** | https://github.com/flowglad/flowglad |
| **Lancement** | ~Décembre 2025 |
| **Fondateurs** | RISD/YC alum, ex-founding designer Imgur (330M MAU) |
| **Catégorie** | Dev Tool / Billing Infrastructure |
| **Métriques buzz** | Featured PH Vibe Coding, YC-backed, open-source, HN mentions |

**Critères de buzz** : ✅ Croissance (PH featured) · ✅ Traction (YC) · ✅ Communauté (GitHub OSS) · ✅ Médias (PH categories) · ✅ Engagement (dev discussions)

### 2️⃣ PROPOSITION DE VALEUR
- **Problème** : Intégrer les paiements/billing dans une app SaaS = 2-4 semaines de webhooks, sync d'entitlements, code glue. Les agents IA ne peuvent pas le faire seuls.
- **Solution** : Zero-webhook billing. Real-time entitlements via SDK. MCP server pour que les coding agents (Cursor, Claude Code) intègrent les paiements en UNE commande.
- **USP** : Premier billing provider **MCP-native** — un agent IA peut one-shot l'intégration paiement complète.
- **Target** : Développeurs indie, SaaS early-stage, équipes AI-first
- **Pricing** : $1K/mois gratuit, puis 0.65% du revenue (+ Stripe 2.9%+30¢)

### 3️⃣ STACK TECHNIQUE
- **Open source** : Monorepo TypeScript
- **Backend** : Node.js, Stripe sous le capot
- **SDK** : React Hooks + backend functions
- **Infra** : Webhook-free architecture (polling/real-time sync)
- **Intégrations** : MCP server, Stripe

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] **Simplicité** : "One-shot billing" = message puissant
- [x] **ROI immédiat** : Économise 2-4 semaines de dev
- [x] **Communauté** : Open source = confiance
- [x] **Statut** : YC badge + "AI-first" positioning

**JTBD** : Quand je lance un SaaS et que je dois ajouter le billing, je veux que mon agent IA le fasse en une commande, pour shipper le même jour.

**Aha moment** : L'agent IA génère tout le code billing en 30 secondes via MCP.

### 5️⃣ GO-TO-MARKET
- **Acquisition** : Product Hunt + YC network + GitHub SEO + Dev Twitter
- **Stratégie** : Open source → adoption gratuite → upsell sur volume
- **Viral loop** : Chaque app qui utilise Flowglad montre le modèle MCP → autres devs adoptent

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité** : 7/10 (nécessite expertise billing + MCP)
- **Verticaux adjacents** : Auth-as-MCP, Analytics-as-MCP, Email-as-MCP
- **Quick wins** : Tout service SaaS boring qui peut être "MCP-ified" pour agents
- **Notre angle** : Créer un "MCP toolkit" pour les services SaaS courants
- **Estimation** : 4-6 semaines pour un MVP vertical

**🎯 Verdict** : ⭐⭐⭐⭐⭐ (5/5)
**⏱️ Time-to-replicate** : 5 semaines (vertical adjacent)
**💡 Action** : **BUILD ADJACENT** — L'idée de MCP-ifier les services dev est le vrai pattern

---

## 🏆 TOP APP #2 : Karumi

### 1️⃣ IDENTIFICATION
| Champ | Détail |
|-------|--------|
| **Nom** | Karumi |
| **URL** | https://karumi.ai |
| **Lancement** | Novembre 2025 |
| **Fondateurs** | YC batch |
| **Catégorie** | AI Sales Tool / SaaS |
| **Métriques buzz** | YC launch, PH featured, AI sales trending category |

**Critères de buzz** : ✅ Traction (YC) · ✅ Croissance (PH AI Sales featured) · ✅ Engagement (discussion Reddit/HN) · ✅ Médias

### 2️⃣ PROPOSITION DE VALEUR
- **Problème** : Les prospects veulent une demo immédiatement, mais les sales teams sont en timezone limitée et bookent à J+3-7.
- **Solution** : Agent IA qui rejoint un appel vidéo live, délivre une demo personnalisée 24/7, dans n'importe quelle langue.
- **USP** : "Le Waymo des demos" — AI agent en LIVE VIDEO, pas un chatbot ou une vidéo pré-enregistrée
- **Target** : SaaS B2B avec sales-led motion, $50K+ ARR
- **Pricing** : Enterprise (probablement $500-2K/mois)

### 3️⃣ STACK TECHNIQUE
- Video call infrastructure (WebRTC probable)
- LLM multi-langue + screen sharing/control
- Intégration CRM

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] **Urgence** : Capture le prospect au pic d'intérêt
- [x] **ROI immédiat** : Réduit le cycle de vente de jours à minutes
- [x] **Autorité** : YC badge
- [x] **Social proof** : "Like Waymo" framing

**JTBD** : Quand un prospect arrive sur mon site à 2h du matin, je veux qu'un agent fasse la demo live, pour ne jamais perdre un lead chaud.

### 5️⃣ GO-TO-MARKET
- YC Launch → PH → Direct sales B2B SaaS
- Product-led : widget "Book instant demo" sur les sites clients

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité** : 8/10 (video AI en temps réel = hard)
- **Verticaux adjacents** : Onboarding agent, Support agent live, Training agent
- **Notre angle** : Version niche (ex: demos pour dev tools, ou demos e-commerce)
- **Estimation** : 8-12 semaines, besoin d'expertise video/AI

**🎯 Verdict** : ⭐⭐⭐⭐ (4/5)
**⏱️ Time-to-replicate** : 10 semaines
**💡 Action** : **WATCH** — Techniquement complexe mais le pattern "AI live agent" est puissant

---

## 🏆 TOP APP #3 : Friendware

### 1️⃣ IDENTIFICATION
| Champ | Détail |
|-------|--------|
| **Nom** | Friendware |
| **URL** | https://friendware.app (via PH) |
| **Lancement** | Décembre 2025 |
| **Fondateurs** | Indie maker |
| **Catégorie** | Productivité macOS / AI Tool |
| **Métriques buzz** | Featured PH Productivity 2026, newcomer highlight |

**Critères de buzz** : ✅ Croissance (PH featured newcomer) · ✅ Engagement (reviews positives) · ✅ Viralité (concept viral "Tab everywhere") · ✅ Communauté

### 2️⃣ PROPOSITION DE VALEUR
- **Problème** : Context-switching constant entre apps et ChatGPT/Claude. Copy-paste, ré-expliquer le contexte.
- **Solution** : AI proactive qui voit ton écran et propose des completions inline. Tab pour accepter. Partout sur macOS.
- **USP** : "GitHub Copilot mais pour TOUT" — pas juste le code, tout ce que tu fais sur ton Mac.
- **Target** : Knowledge workers macOS, freelances, devs
- **Pricing** : Freemium probable + abonnement

### 3️⃣ STACK TECHNIQUE
- macOS native (Swift probable)
- Screen reading / accessibility APIs
- LLM integration (multi-model)
- Inline overlay UI

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] **Simplicité** : Un seul geste = Tab
- [x] **ROI immédiat** : Gain de temps mesurable dès le premier usage
- [x] **Gamification** : Le "flow" de Tab-complete est addictif

**JTBD** : Quand j'écris un email/doc/message, je veux que l'AI complète ma pensée sans quitter mon app, pour rester dans le flow.

### 5️⃣ GO-TO-MARKET
- Product Hunt → Twitter indie makers → Word of mouth macOS
- Viral loop : Les gens voient Tab-complete en screen share → "c'est quoi ça ?"

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité** : 6/10 (macOS accessibility + LLM = faisable)
- **Verticaux adjacents** : Version Windows, version spécialisée (writers, sales, support)
- **Quick wins** : Version Windows (marché 10x plus grand, pas de concurrent direct)
- **Notre angle** : Clone Windows + spécialisation verticale (ex: "Friendware for Sales")
- **Estimation** : 3-4 semaines pour MVP Windows

**🎯 Verdict** : ⭐⭐⭐⭐⭐ (5/5)
**⏱️ Time-to-replicate** : 4 semaines (Windows clone)
**💡 Action** : **BUILD NOW** — Marché Windows grand ouvert, concept prouvé

---

## 🏆 TOP APP #4 : PgDog

### 1️⃣ IDENTIFICATION
| Champ | Détail |
|-------|--------|
| **Nom** | PgDog |
| **URL** | https://pgdog.dev |
| **GitHub** | https://github.com/pgdogdev/pgdog |
| **Lancement** | 2025 |
| **Fondateurs** | Lev Kokotov — ex-co-founder PostgresML, ex-Instacart (100TB+ DBs) |
| **Catégorie** | Dev Tool / Database Infrastructure |
| **Métriques buzz** | HN front page, YC-backed, OSS |

**Critères de buzz** : ✅ Engagement (HN front page Feb 2026) · ✅ Traction (YC) · ✅ Communauté (GitHub OSS) · ✅ Autorité (founder pedigree)

### 2️⃣ PROPOSITION DE VALEUR
- **Problème** : Scaler PostgreSQL = migrations complexes, extensions, downtime
- **Solution** : Proxy transparent qui load-balance et sharde, zéro changement de code app
- **USP** : "Scale Postgres without changing the app" — drop-in proxy
- **Target** : Équipes backend avec Postgres en croissance

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité** : 9/10 (deep Postgres expertise requise)
- **Notre angle** : Trop technique à répliquer, mais indicateur de tendance "invisible infra"

**🎯 Verdict** : ⭐⭐⭐ (3/5)
**⏱️ Time-to-replicate** : N/A (trop spécialisé)
**💡 Action** : **WATCH** — Pattern intéressant (infra transparente) mais niche

---

## 🏆 TOP APP #5 : Dvina

### 1️⃣ IDENTIFICATION
| Champ | Détail |
|-------|--------|
| **Nom** | Dvina |
| **URL** | https://dvina.ai |
| **Lancement** | Novembre 2025 |
| **Catégorie** | AI Agent Platform / Enterprise |
| **Métriques buzz** | PH AI Agent featured, 120+ intégrations, press coverage |

**Critères de buzz** : ✅ Croissance (PH featured) · ✅ Traction (enterprise clients) · ✅ Médias (press release) · ✅ Engagement

### 2️⃣ PROPOSITION DE VALEUR
- **Problème** : Les entreprises utilisent 50-100+ apps. L'automatisation entre elles = fragile, custom, coûteux.
- **Solution** : AI agents gouvernés qui orchestrent des workflows à travers 120+ apps (Google, Notion, Jira, SAP, Salesforce)
- **USP** : "Governed multi-agent orchestration" — sécurité enterprise + breadth d'intégrations
- **Target** : Enterprise, mid-market IT/ops teams

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité** : 9/10 (120+ intégrations = moat massif)
- **Notre angle** : Version micro-SaaS ciblée (ex: "Dvina but just for dev teams" = Jira+GitHub+Slack+Linear)

**🎯 Verdict** : ⭐⭐⭐ (3/5)
**⏱️ Time-to-replicate** : N/A full, 4-6 semaines pour niche
**💡 Action** : **WATCH** — Le moat est dans le nombre d'intégrations

---

## 📈 Tendances Émergentes

1. **MCP-ification de tout** : Flowglad montre que les services dev qui deviennent "agent-programmable" via MCP gagnent. Tout service SaaS ennuyeux (billing, auth, email, analytics) peut être MCP-ifié.

2. **AI Tab-Complete beyond code** : Friendware étend le paradigme Copilot à tout le desktop. La productivité AI passe du code au knowledge work général.

3. **AI Live Agents** : Karumi pousse l'agent IA au-delà du chat vers la VIDEO live. Prochain front : agents qui font des appels, des demos, du support en temps réel.

4. **"Invisible infrastructure"** : PgDog, Flowglad = des outils qui font disparaître la complexité. Drop-in, zero-config, transparent.

5. **AI Organizations** : Reddit (r/Startup_Ideas) buzze sur "2026 = era of AI Organizations" — pas juste des agents, mais des systèmes d'agents coordonnés.

---

## 💡 Insights Actionnables

1. 🔥 **BUILD : Clone Windows de Friendware** — Le concept Tab-to-complete est prouvé sur macOS, marché Windows 10x plus grand, zéro concurrent direct. MVP en 3-4 semaines.

2. 🔥 **BUILD : MCP Toolkit** — Suite d'outils dev "agent-programmable" (auth, email, analytics via MCP). Flowglad prouve le modèle pour billing, étendre aux autres services.

3. 👀 **WATCH : AI Demo Agents** — Karumi montre la direction mais la tech video est complexe. Surveiller si le pattern se confirme.

4. 💡 **Insight Reddit** : L'analyse de 1.3M App Store reviews montre des apps "begging to be replaced" — Discogs identifiée comme "Apollo-for-Reddit opportunity of 2026" (43% de 1-star récentes).

---

## 🚀 Idées de Produits Émergées

| Idée | Source | Complexité | Potentiel |
|------|--------|:----------:|:---------:|
| Tab-to-complete Windows | Friendware clone | 6/10 | ⭐⭐⭐⭐⭐ |
| MCP Auth Provider | Pattern Flowglad | 5/10 | ⭐⭐⭐⭐ |
| MCP Analytics SDK | Pattern Flowglad | 5/10 | ⭐⭐⭐⭐ |
| AI agent memory for coding | Engram (HN Show) | 6/10 | ⭐⭐⭐ |
| Discogs alternative app | Reddit signal | 4/10 | ⭐⭐⭐ |
| Dev team mini-Dvina | Dvina niche | 7/10 | ⭐⭐⭐⭐ |

---

## 💰 Unit Economics Deep Dive — Flowglad

### Revenue Estimation
- **ARR estimé** : Pre-revenue / early ($0-500K) — YC-stage
- **Méthode** : Estimation via pricing model ($1K gratuit, 0.65% après)
- **Pricing moyen (ARPU)** : ~$50-200/mois par client actif
- **Nb users estimés** : 50-200 (early OSS adopters)

### Unit Economics
- **CAC estimé** : ~$0-50 (product-led, OSS, YC network = quasi gratuit)
- **LTV estimé** : $50/mois × 24 mois = $1,200
- **Ratio LTV/CAC** : >10x (acquisition quasi gratuite via OSS) 🟢
- **Payback Period** : <1 mois 🟢

### Burn Rate & Runway
- **Funding** : YC ($500K standard deal)
- **Burn rate estimé** : $15-25K/mois (petite équipe)
- **Nb employés** : 2-3
- **Runway estimé** : 20-33 mois

### Efficiency Metrics
- **Revenue per employee** : Early stage, N/A
- **Funding efficiency** : Pre-scale
- **Gross Margin estimé** : 85%+ (SaaS billing layer) 🟢

### Vulnérabilités identifiées
- Dépendance Stripe (pas de payment processor propre)
- Moat faible si un gros player (Stripe eux-mêmes) lance un MCP server
- Marché de niche — les devs AI-first sont nombreux mais le billing n'est fait qu'une fois

### Leçons pour Kyle
- Le **MCP-as-distribution** est un canal d'acquisition révolutionnaire : ton outil apparaît dans l'IDE de chaque dev
- L'**open source + free tier généreux** = flywheel d'adoption sans CAC
- Le **timing** est parfait : les agents IA deviennent mainstream, tout outil "agent-programmable" a un avantage

---

## 🎯 Opportunity Scorecard — Top 3 du Jour

| Critère (poids) | Tab-Complete Windows | MCP Auth Provider | Dev Team Mini-Dvina |
|-----------------|:--------------------:|:-----------------:|:-------------------:|
| 📊 Market Size (20%) | 9/10 | 7/10 | 6/10 |
| ⚙️ Complexity (15%) | 7/10 | 8/10 | 5/10 |
| ⏱️ Time-to-Market (15%) | 8/10 | 8/10 | 6/10 |
| 🏟️ Competition (15%) | 9/10 | 7/10 | 5/10 |
| 💰 Revenue Potential (20%) | 8/10 | 7/10 | 7/10 |
| 🧑‍💻 Founder Fit (15%) | 7/10 | 8/10 | 6/10 |
| **TOTAL** | **8.1/10** | **7.5/10** | **5.9/10** |
| **Verdict** | **🔥 BUILD NOW** | **BUILD** | **WATCH** |

---

## 📊 Cumulative Tracker
→ Voir fichier global : `veille/market-scan/TRACKER.md`
- Opportunités totales trackées : 6
- BUILD NOW actifs : 1 (Tab-Complete Windows)
- BUILD actifs : 1 (MCP Auth Provider)
- WATCH en observation : 4
- Nouveaux ajouts aujourd'hui : 6
