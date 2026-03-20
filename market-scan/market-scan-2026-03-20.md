# 🔥 Market Scan — 20 mars 2026

## 📊 Résumé Exécutif
- **Apps scannées :** 12+
- **Apps à fort potentiel :** 4
- **Opportunités immédiates :** 2
- **Sources :** Product Hunt, Hacker News (Show HN), Indie Hackers, Reddit, Twitter/X

### 🔑 Signal du jour
La vague **"agentic dev tools"** continue d'exploser — tmux-IDE, Google Antigravity, et Flowglad illustrent la même tendance : l'outillage pour développeurs qui travaillent avec des agents IA. La niche **"TTS ultra-léger pour edge"** (KittenTTS) est un signal fort pour l'embarqué/IoT.

---

## 🏆 TOP APP #1 : KittenTTS
**🎯 Score : 8.5/10**

### 1️⃣ IDENTIFICATION
- **Nom :** KittenTTS
- **URL :** https://github.com/KittenML/KittenTTS
- **Date de lancement :** v0.8 — mars 2026 (projet démarré ~fin 2025)
- **Fondateurs :** Rohan Joshi + équipe KittenML
- **Catégorie :** Dev Tool / AI Infrastructure / Edge AI
- **Métriques de buzz :**
  - 🔥 Show HN : **370 upvotes, 146 commentaires** (front page)
  - ⭐ GitHub : croissance rapide
  - HuggingFace : demo live + 4 modèles hébergés
  - Discord actif

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Les modèles TTS existants (ElevenLabs, OpenAI) nécessitent cloud + GPU + API payante. Impossible pour edge/embarqué/offline.
- **Solution :** TTS open-source de 25MB à 80MB, CPU-only, ONNX. 8 voix, 24kHz, preprocessing intégré.
- **USP :** Le plus petit modèle TTS de qualité au monde. 14M paramètres = 25MB. Tourne sur un Raspberry Pi.
- **Target :** Devs IoT, apps offline-first, assistants vocaux embarqués, accessibilité
- **Pricing :** Open-source (licence permissive) + commercial support payant

### 3️⃣ STACK TECHNIQUE
- **Core :** ONNX Runtime (CPU optimized)
- **Modèles :** 4 tailles (nano 15M int8→25MB, nano 15M→56MB, micro 40M→41MB, mini 80M→80MB)
- **Distribution :** pip/npm, HuggingFace Hub
- **Langues :** Anglais (pour l'instant)

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Simplicité — `pip install kittentts` et c'est parti
- [x] Communauté — Discord + HN + open-source
- [x] ROI immédiat — gratuit vs ElevenLabs $5-99/mois
- [x] Statut — "look how small my model is"
- **JTBD :** Quand je build une app qui parle, je veux du TTS qui tourne sans API cloud, pour garder le contrôle et réduire les coûts.
- **Aha moment :** Première synthèse vocale de qualité en <1 seconde, offline, sur CPU

### 5️⃣ GO-TO-MARKET
- **Canal primaire :** Hacker News + GitHub organic
- **Canal secondaire :** HuggingFace ecosystem, Twitter dev community
- **Stratégie :** Open-source → adoption → commercial support/custom voices
- **Viral loop :** Devs partagent des démos audio sur Twitter/HN

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité :** 9/10 (ML research nécessaire)
- **Verticaux adjacents :** TTS français léger (aucun concurrent!), TTS pour assistants domotiques, TTS pour jeux mobiles
- **Quick wins :** Wrapper SaaS autour de KittenTTS (API hébergée low-cost)
- **Notre angle :** API TTS française ultra-rapide basée sur KittenTTS → marché FR sous-servi
- **Estimation :** 2-4 semaines pour un wrapper API, 3-6 mois pour fine-tune FR

**💡 Action : WATCH** — Trop ML-heavy pour build from scratch, mais surveiller pour intégration dans nos projets (RestoAI voice agent?)

---

## 🏆 TOP APP #2 : Tmux-IDE
**🎯 Score : 7.5/10**

### 1️⃣ IDENTIFICATION
- **Nom :** tmux-IDE
- **URL :** https://tmux.thijsverreck.com
- **Date de lancement :** Mars 2026
- **Fondateurs :** Thijs Verreck (indie dev)
- **Catégorie :** Dev Tool / AI Agent Infrastructure
- **Métriques de buzz :**
  - Show HN : **86 upvotes, 37 commentaires**
  - npm package disponible (`npx tmux-ide`)
  - Claude Code skill intégré

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Configurer un workspace multi-agent Claude Code est fastidieux — split tmux manuellement, lancer les agents, coordonner.
- **Solution :** Un CLI qui génère des layouts tmux avec lead + teammate agents, dev servers, et shells. Config YAML déclarative.
- **USP :** Premier outil dédié aux "agent teams" dans le terminal. Self-organizing via prompts.
- **Target :** Devs utilisant Claude Code en multi-agent (niche mais en forte croissance)
- **Pricing :** Gratuit/open-source

### 3️⃣ STACK TECHNIQUE
- Node.js CLI, tmux, YAML config
- Auto-détection de stack (Next.js, Vite, Python, Go)
- Claude Code skill built-in

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Simplicité — `npx tmux-ide` et le layout est prêt
- [x] Communauté — écosystème Claude Code
- [x] ROI immédiat — gain de temps setup
- **JTBD :** Quand je veux faire travailler plusieurs agents Claude en parallèle, je veux un layout prêt en une commande, pour me concentrer sur le prompting pas la config.

### 5️⃣ GO-TO-MARKET
- Hacker News + npm organic
- Claude Code ecosystem (skills marketplace)
- Twitter #buildinpublic

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité :** 3/10 (c'est principalement du scripting tmux)
- **Verticaux adjacents :** Extension VS Code équivalente, version pour Cursor multi-agent
- **Quick wins :** Templates de workflows pré-configurés (full-stack, data pipeline, etc.)
- **Notre angle :** Intégrer dans dotclaud comme skill premium
- **Estimation :** 1 semaine pour une version comparable

**💡 Action : BUILD ADJACENT** — Intégrer le concept dans dotclaud (Kyle a déjà un multi-agent fleet!)

---

## 🏆 TOP APP #3 : Flowglad
**🎯 Score : 8/10**

### 1️⃣ IDENTIFICATION
- **Nom :** Flowglad
- **URL :** https://github.com/flowglad/flowglad
- **Date de lancement :** Décembre 2025 (PH), actif mars 2026
- **Catégorie :** Dev Tool / Payments / Open-source
- **Métriques de buzz :**
  - Product Hunt : Featured
  - GitHub : open-source, croissance active
  - Mentionné dans PH "Best Vibe Coding Tools 2026"
  - Community buzz sur Reddit/Twitter

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Intégrer Stripe nécessite des webhooks, du glue code, et de la synchronisation DB. C'est un cauchemar pour les vibe coders et les agents IA.
- **Solution :** Payment provider sans webhooks. L'API te dit directement le statut. MCP hooks pour one-shot payment setup par un agent IA.
- **USP :** "Zero webhooks" + "AI can one-shot it" = parfait pour la vague vibe coding
- **Target :** Indie devs, vibe coders, équipes utilisant des agents IA pour builder
- **Pricing :** Open-source + hosted (freemium probable)

### 3️⃣ STACK TECHNIQUE
- Open-source, self-hostable
- API-first, webhook-free architecture
- MCP (Model Context Protocol) hooks
- Real-time entitlements

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Simplicité — pas de webhooks = moins de code
- [x] ROI immédiat — setup en minutes vs heures avec Stripe
- [x] Communauté — open-source
- **JTBD :** Quand je build un SaaS avec un agent IA, je veux ajouter les paiements en une commande, sans écrire de webhook handlers.

### 5️⃣ GO-TO-MARKET
- Open-source + Product Hunt launch
- Écosystème vibe coding (Lovable, Cursor, Claude Code)
- Developer advocacy

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité :** 7/10 (payments = complexe, compliance)
- **Verticaux adjacents :** Billing spécialisé par niche (restaurants, comptables)
- **Quick wins :** Plugin Flowglad pour nos projets
- **Notre angle :** Utiliser Flowglad dans ClientFlow/dotclaud au lieu de Stripe
- **Estimation :** N/A (mieux d'utiliser que de répliquer)

**💡 Action : WATCH + USE** — Évaluer pour nos propres projets SaaS

---

## 🏆 TOP APP #4 : Flux (iMessage AI Agents)
**🎯 Score : 7/10**

### 1️⃣ IDENTIFICATION
- **Nom :** Flux
- **URL :** Product Hunt Featured (Jan 2026)
- **Date de lancement :** 2025, featured janvier 2026
- **Catégorie :** No-code / AI Agents / Messaging
- **Métriques de buzz :**
  - Product Hunt : Top Products Jan 2026
  - Listé dans "40 Leading SaaS Startups 2026"
  - Mentionné dans PH "Best No-Code Platforms 2026"

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Créer un agent IA conversationnel nécessite du code, un serveur, une intégration messaging.
- **Solution :** Build & deploy des agents IA custom directement dans iMessage/WhatsApp. No-code.
- **USP :** Agent IA dans l'app de messaging que les gens utilisent déjà. Pas d'app à installer.
- **Target :** PMEs, éducateurs, support client, solopreneurs
- **Pricing :** Freemium (bootstrapped/early stage)

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Simplicité — no-code
- [x] ROI immédiat — agent opérationnel en minutes
- [x] Social proof — listé partout
- **JTBD :** Quand je veux automatiser mon support/tutoring, je veux un agent dans WhatsApp/iMessage, sans coder ni gérer de serveur.

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité :** 5/10
- **Verticaux adjacents :** Agent WhatsApp pour restaurants (→ RestoAI!)
- **Notre angle :** Exactement le concept de RestoAI mais vertical resto
- **Estimation :** RestoAI est déjà en cours

**💡 Action : WATCH** — Valide la thèse RestoAI. Flux prouve que "agent dans messaging" a de la traction.

---

## 📈 Tendances Émergentes

### 1. 🤖 Agentic Dev Tools Explosion
Google Antigravity (free agent-first IDE, 5 agents parallèles, Claude Opus + Gemini), tmux-IDE, Claude Code skills ecosystem — tout converge vers le dev assisté par des équipes d'agents. **C'est le moment de vendre des outils pour cette vague** → dotclaud bien positionné.

### 2. 🔊 Edge AI / Tiny Models
KittenTTS (25MB TTS), LLM circuit finder (duplicate 3 layers = massive improvement) — la course au "smallest model that actually works". Applications : IoT, mobile, offline, privacy-first.

### 3. 💳 Vibe Coding Infrastructure
Flowglad (payments), Lovable (full-stack gen), NativeBridge (mobile QA) — tout l'écosystème autour du "build entire apps with AI" se structure. Les outils d'infrastructure pour vibe coders = niche en or.

### 4. 🏢 Micro-SaaS Acquisition
Indie Hackers post sur $120K MRR via acquisition de micro-SaaS (Mava, Evalart, Sendtric). Le modèle "buy, don't build" gagne du terrain pour les solopreneurs.

---

## 💡 Insights Actionnables

1. **dotclaud :** Ajouter un skill "multi-agent tmux layout" inspiré de tmux-IDE. C'est un quick win qui ajoute de la valeur au pack Pro. **Temps : 1 semaine.**

2. **RestoAI :** Flux valide le modèle "agent dans messaging". Accélérer le développement de l'agent WhatsApp pour restos. Le timing est parfait.

3. **Flowglad :** Évaluer comme alternative à Stripe pour les prochains projets. Le "zero webhook" simplifie massivement le dev.

4. **KittenTTS :** Garder en radar pour le voice agent RestoAI. Un TTS léger en local = moins de coûts, plus de rapidité.

---

## 🚀 Idées de Produits Émergées

| Idée | Source | Complexité | Potentiel |
|------|--------|:----------:|:---------:|
| API TTS française (wrapper KittenTTS) | KittenTTS | 6/10 | 🟡 Niche |
| Skill dotclaud "multi-agent layout" | tmux-IDE | 3/10 | 🟢 Quick win |
| Agent WhatsApp vertical (resto, comptable) | Flux | 5/10 | 🟢 RestoAI |
| SaaS "payments pour vibe coders" français | Flowglad | 8/10 | 🟡 Crowded |

---

## 💰 Unit Economics Deep Dive — KittenTTS (Top App)

### Revenue Estimation
- **ARR déclaré/estimé :** $0 (open-source, pre-revenue)
- **Méthode :** Pas encore de revenus. Modèle = OSS → Commercial support
- **Revenue potentiel :** Custom voices ($5K-50K/deal enterprise), hosted API ($29-199/mois), licensing
- **Comparable :** Coqui TTS (acquis), Bark (open-source, pas monétisé), ElevenLabs ($330M ARR estimé)

### Unit Economics (Estimations)
- **CAC estimé :** ~$0 (organic HN/GitHub/Twitter)
- **LTV estimé :** TBD (pas encore de clients payants)
- **Churn estimé :** N/A

### Benchmarks
- **Revenue per employee :** N/A (early stage)
- **Funding :** Non déclaré (bootstrapped probable)

### Vulnérabilités identifiées
- Anglais seulement → gap multilingue
- Qualité vs ElevenLabs/OpenAI TTS encore inférieure
- Pas de clonage de voix (encore)
- Modèle commercial flou

### Leçons pour Kyle
- L'open-source sur HN/GitHub = acquisition gratuite massive
- Le positionnement "tiny/edge" est un moat technique réel
- Un wrapper API payant autour d'un OSS = business model validé (cf. Supabase/Postgres)

---

## 🎯 Opportunity Scorecard — Top 3 du Jour

| Critère (poids) | tmux-IDE skill (dotclaud) | Agent WhatsApp Resto | API TTS FR |
|-----------------|:-------------------------:|:--------------------:|:----------:|
| 📊 Market Size (20%) | 5/10 | 7/10 | 4/10 |
| ⚙️ Complexity (15%) | 9/10 | 6/10 | 5/10 |
| ⏱️ Time-to-Market (15%) | 9/10 | 7/10 | 6/10 |
| 🏟️ Competition (15%) | 8/10 | 7/10 | 9/10 |
| 💰 Revenue Potential (20%) | 6/10 | 8/10 | 5/10 |
| 🧑‍💻 Founder Fit (15%) | 9/10 | 7/10 | 4/10 |
| **TOTAL** | **7.3/10** | **7.1/10** | **5.4/10** |
| **Verdict** | **BUILD** | **BUILD** (RestoAI) | **WATCH** |

---

## 📊 Cumulative Tracker
→ Voir fichier global : `veille/market-scan/TRACKER.md`
- Opportunités totales trackées : +4 aujourd'hui
- BUILD NOW actifs : 2 (tmux-IDE skill, RestoAI acceleration)
- WATCH en observation : 2 (KittenTTS, Flowglad)
- Nouveaux ajouts aujourd'hui : 4
