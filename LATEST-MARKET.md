# 🔥 Market Scan — 2026-06-25

## 📊 Résumé Exécutif
- Apps analysées : 8
- Top potentiel : Palmier Pro, Skybridge, OpenMontage
- Opportunités immédiates (BUILD NOW) : 1 (Skybridge ecosystem)

## 🏆 TOP APP #1 : Palmier Pro
### 1. Identification
- **URL** : [palmier.io](https://www.palmier.io/) | GitHub : [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro)
- **Launch** : mi-juin 2026 (public) | Fondée 2024 (YC S24)
- **Fondateurs** : Équipe Palmier-io (YC batch)
- **Catégorie** : AI-native video editor, macOS
- **Buzz** : #1 GitHub Trending (22 juin 2026), 3 500+ stars, 291 forks, couverture AIToolly/AgentStack/explainx.ai

### 2. Proposition de valeur
- **Problème** : Les éditeurs vidéo (Premiere, Final Cut) ne sont pas conçus pour travailler avec des agents IA
- **Solution** : Éditeur macOS où l'IA (Claude, Codex, Cursor via MCP) lit et édite la timeline comme un humain
- **USP** : Open-source GPLv3 + génération payante (Seedance, Kling, Nano Banana Pro dans la timeline)
- **Target** : Créateurs de contenu tech-savvy, solo founders, agences IA
- **Pricing** : Éditeur gratuit (no login) · Pro $29/mo (5K crédits) · Max $69/mo (12K crédits)

### 3. Stack technique
- **Frontend/App** : Swift natif macOS (construit from scratch)
- **Génération** : Seedance, Kling, Nano Banana Pro (fermé, payant)
- **Intégration agents** : MCP server open-source (Claude, Codex, Cursor)
- **Backend** : Fermé (pipeline de génération propriétaire)

### 4. Psychologie
- **Aha moment** : Voir Claude éditer ta timeline vidéo sans quitter l'éditeur
- **JTBD** : "Je veux produire des vidéos AI-native sans jongler entre 5 outils"
- **Triggers** : Curiosité (#1 GitHub trending = effet FOMO), social proof YC, gratuité de l'entrée
- **Viral loop** : "Built with Palmier" watermark possible + MCP = distribution via Claude users

### 5. Go-to-market
- **Canal principal** : GitHub (trending organique), Twitter/X dev community, newsletter AI
- **Stratégie launch** : Open-source d'abord → YC network → Product Hunt à venir
- **Viral loop** : Forks massifs (291 en quelques jours), articles tiers spontanés (6+ médias IA)

### 6. Réplication pour Kyle
- **Complexité** : 8/10 (Swift natif macOS = niche technique forte)
- **Angle Kyle** : Vertical voice AI → éditeur de podcast/audio avec agent IA qui édite la timeline audio
- **Verticaux adjacents** : Éditeur de screencasts AI, éditeur de cours en ligne AI-native
- **Temps dev** : 4-6 mois pour un MVP audio (moins complexe que video)

## 🏆 TOP APP #2 : Skybridge
### 1. Identification
- **URL** : [skybridge.tech](https://www.skybridge.tech/) | GitHub : [alpic-ai/skybridge](https://github.com/alpic-ai/skybridge)
- **Launch** : juin 2026 (Product Hunt #16 mensuel) | Société : Alpic AI (Pre-Seed)
- **Fondateurs** : Harijoe, Fred Barthelet + équipe Alpic
- **Catégorie** : Framework TypeScript fullstack pour MCP Apps & ChatGPT Apps
- **Buzz** : 100K npm downloads/mois, 1K+ GitHub stars, recommandé dans la doc OpenAI, 10% des MCP apps Claude/ChatGPT

### 2. Proposition de valeur
- **Problème** : Construire des apps MCP (Model Context Protocol) est complexe et fragmenté
- **Solution** : Framework React type-safe, platform-agnostic pour shipper des MCP apps en one-click via Alpic cloud
- **USP** : Open-source + cloud propriétaire (Alpic) + présence dans les app stores Claude et ChatGPT
- **Target** : Développeurs TypeScript/React qui veulent distribuer des apps dans l'écosystème Claude/ChatGPT
- **Pricing** : OSS gratuit · Alpic cloud (tiered, non public)

### 3. Stack technique
- **Framework** : TypeScript, React, type-safe
- **Infra** : Alpic cloud (build, deploy, monitor, distribute)
- **Compatibilité** : Claude App Store, ChatGPT Plugin Store, MCP protocol
- **Modèle** : Open-core (framework OSS + cloud propriétaire)

### 4. Psychologie
- **Aha moment** : Shipper une MCP app dans Claude Store en une commande CLI
- **JTBD** : "Je veux distribuer mon app IA à des millions d'utilisateurs Claude/ChatGPT sans gérer l'infra"
- **Triggers** : Autorité (recommandé par OpenAI), réseau (10% des apps MCP = effet dominant), FOMO (early mover dans un store qui explose)
- **Viral loop** : Chaque app shippée = nouveau dev qui découvre le framework

### 5. Go-to-market
- **Canal principal** : Dev communities (npm, GitHub), doc OpenAI, Product Hunt, Alpic blog
- **Stratégie** : Infrastructure-first → capture le marché avant que les stacks MCP se standardisent
- **Network effect** : Plus d'apps dans le store → plus de visibilité → plus de devs → plus d'apps

### 6. Réplication pour Kyle
- **Complexité** : 6/10 (framework, pas un produit end-user)
- **Angle Kyle** : Construire une voice AI app MCP avec Skybridge → distribution immédiate à tous les users Claude
- **Verticaux adjacents** : MCP app de scheduling vocal, assistant de meeting voice-to-action
- **Temps dev** : 2-4 semaines pour une voice MCP app basique avec Skybridge

## 🏆 TOP APP #3 : OpenMontage
### 1. Identification
- **URL** : GitHub : [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)
- **Launch** : 22 juin 2026 | Créateur : calesthio (solo developer)
- **Catégorie** : Agentic video production system, open-source
- **Buzz** : #2 GitHub Trending, 8 600+ stars (3 000 en 1 seul jour), couverture Medium/nerdzap/AIToolly

### 2. Proposition de valeur
- **Problème** : Production vidéo = processus long, coûteux, multi-outils
- **Solution** : 12 pipelines + 52 outils + 500+ skills qui transforment Claude Code/Cursor/Codex en studio vidéo complet
- **USP** : Open-source, coût production ~$1.33 pour une vidéo 60s avec narration+musique+captions
- **Target** : Développeurs utilisant des agents IA (Claude Code, Cursor, Codex)
- **Pricing** : Gratuit (OSS) · Coûts API selon usage · Path zero-key (Piper TTS + Archive.org + FFmpeg local)

### 3. Stack technique
- **Orchestration** : Claude Code / Cursor / Codex (via MCP ou native)
- **Rendu** : FFmpeg, Remotion
- **TTS** : Piper TTS (local) ou API payantes
- **Assets** : Archive.org, NASA (zero-cost) ou APIs génération payantes
- **Format** : Markdown comme script de direction (le Markdown "fait" la réalisation)

### 4. Psychologie
- **Aha moment** : Écrire un script Markdown et voir ton agent produire une vidéo complète pour $1.33
- **JTBD** : "Je veux créer des vidéos de contenu sans toucher à Premiere ni payer une agence"
- **Triggers** : Curiosité extrême (concept inédit), chiffre choc ($1.33/vidéo), open-source = adoption sans friction
- **Viral loop** : Chaque vidéo produite = démonstration du tool → partage organique

### 5. Go-to-market
- **Canal principal** : GitHub trending (organique), Twitter dev community, newsletters IA
- **Stratégie** : Drop GitHub + vitesse de croissance stars = effet boule de neige médias
- **Moat** : Communauté contributors (déjà des forks multiples en 3 jours)

### 6. Réplication pour Kyle
- **Complexité** : 5/10 (assemblage d'outils existants, pas de code proprio)
- **Angle Kyle** : Version spécialisée "Podcast to Video" ou "Voice memo to short-form video"
- **Verticaux adjacents** : Newsletter → vidéo, blog post → Reel, rapport → présentation animée
- **Temps dev** : 3-6 semaines pour un vertical spécialisé monetisable (SaaS wrapper d'OpenMontage)

## 💰 Unit Economics Deep Dive — Palmier Pro
*Données : launch mi-juin 2026, YC S24, open-source + SaaS. Estimations basées sur GitHub stars, pricing public, taille marché.*

| Métrique | Estimation | Source / Hypothèse |
|---|---|---|
| **MRR estimé** | ~$15K–40K | Launch récent (~10 jours), early adopters YC network |
| **ARR projeté (12m)** | $500K–2M | Hypothèse : 5x MRR actuel × croissance organique |
| **Users actifs** | 2 000–5 000 | 3 500 stars → ~10–15% conversion download gratuit |
| **Paying users** | 300–800 | Freemium → ~10–15% conversion Pro/Max |
| **ARPU** | $35–45/mo | Mix Pro ($29) / Max ($69), moyenne pondérée |
| **CAC** | ~$0 | Distribution GitHub organique + YC network |
| **LTV (estimé)** | $420–720 | Churn ~5–8%/mo → LTV = ARPU × 1/churn |
| **LTV/CAC** | ∞ (CAC≈0) | Distribution organique → ratio exceptionnel |
| **Payback period** | <1 mois | CAC quasi nul |
| **Équipe** | 4–6 personnes | YC S24 standard team |
| **Rev/Employee** | $40K–80K ARR | Cohérent early-stage YC |
| **Rule of 40** | ~70+ | Croissance forte + marges élevées (SaaS) |

**Verdict santé : 🟢 SAIN** — CAC quasi nul grâce à GitHub + YC, LTV/CAC excellent, modèle freemium bien structuré (editor free → crédits payants). Seul risque : dépendance APIs génération tierces (marges variables). YC backing = runway assuré ~18 mois.

*Sources : [palmier.io/pricing](https://www.palmier.io/pricing), [GitHub repo](https://github.com/palmier-io/palmier-pro), [AIToolly launch article](https://aitoolly.com/ai-news/article/2026-06-21-palmier-pro-a-new-ai-native-video-editing-solution-specifically-designed-for-macos-users)*

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Palmier Pro | Skybridge | OpenMontage |
|---|---|---|---|
| 📊 Market Size (20%) | 7 — Marché vidéo AI €5B | 9 — Infra MCP = OS layer futur | 6 — Vidéo contenu AI €3B |
| ⚙️ Complexité inversée (15%) | 3 — Swift macOS natif, dur | 7 — TypeScript React, accessible | 8 — Assembly d'outils OSS |
| ⏱️ Time-to-Market (15%) | 4 — 4-6 mois minimum | 8 — 2-4 semaines (voice app) | 7 — 3-6 semaines (SaaS wrapper) |
| 🏟️ Compétition inversée (15%) | 6 — CapCut/Premiere = titans | 8 — Early mover MCP stores | 7 — Pas de concurrent direct OSS |
| 💰 Revenue Potential (20%) | 7 — $50-200K MRR à 12 mois | 8 — B2D + SaaS cloud, high ACV | 5 — OSS difficile à monétiser |
| 🧑‍💻 Founder-Fit Kyle (15%) | 5 — Voice adjacent, Swift = non | 9 — Voice MCP app = fit parfait | 6 — Intéressant mais pas core |
| **Score pondéré** | **5.6** | **8.3** | **6.4** |
| **Verdict** | 🟠 WATCH | 🟢 BUILD NOW | 🟡 BUILD ADJACENT |

### Détail calculs
- **Palmier Pro** : (7×0.20)+(3×0.15)+(4×0.15)+(6×0.15)+(7×0.20)+(5×0.15) = 1.4+0.45+0.6+0.9+1.4+0.75 = **5.50** → 🟠 WATCH
- **Skybridge** : (9×0.20)+(7×0.15)+(8×0.15)+(8×0.15)+(8×0.20)+(9×0.15) = 1.8+1.05+1.2+1.2+1.6+1.35 = **8.20** → 🟢 BUILD NOW
- **OpenMontage** : (6×0.20)+(8×0.15)+(7×0.15)+(7×0.15)+(5×0.20)+(6×0.15) = 1.2+1.2+1.05+1.05+1.0+0.9 = **6.40** → 🟡 BUILD ADJACENT

## 📈 Tendances Émergentes
### 1. MCP = nouveau App Store (signal fort 🔴)
Le Model Context Protocol s'impose comme la couche de distribution des apps IA. Claude et ChatGPT ont leurs "stores" d'apps MCP. Skybridge en est l'infrastructure. C'est l'équivalent de l'App Store iOS en 2008 — être early = avantage massif. La fenêtre d'opportunité est ouverte *maintenant*.

### 2. "AI-native" ≠ AI-assisted (signal fort 🔴)
Palmier Pro et OpenMontage représentent une nouvelle catégorie : des outils *conçus* pour être contrôlés par des agents, pas juste des outils avec un bouton IA. Les agents peuvent lire la timeline, écrire des scripts, orchestrer la production. Ce paradigme va s'étendre à l'audio, au code, à la data.

### 3. Open-source as go-to-market (signal récurrent 🟡)
OpenMontage et Palmier Pro utilisent GitHub trending comme canal d'acquisition primaire. 8K stars en 1 jour sans budget marketing. Le repo *est* le funnel. Pour les dev-tools, ce modèle supplante Product Hunt.

### 4. Agents IA + MCP + voice = convergence (signal pour Kyle 🎯)
Les trois tendances convergent vers un futur proche où un agent vocal contrôle des apps MCP en temps réel. Kyle est positionné à l'intersection exacte : voice AI (expertise) + MCP (distribution) + SaaS (monétisation). La fenêtre est de 6-12 mois avant que le marché se sature.

### 5. Coûts de production AI s'effondrent (signal économique 🟡)
OpenMontage le quantifie : $1.33 pour une vidéo 60s complète. Ce mouvement dévalue tous les services créatifs humains répétitifs (montage basique, voix off générique, sous-titrage). Les nouveaux gagnants sont ceux qui créent les *workflows* et les *distributions*, pas ceux qui exécutent.

## 💡 Insights Actionnables
### 🎯 Pour Kyle — Actions immédiates (72h)

**#1 — Construis une voice MCP app avec Skybridge [BUILD NOW]**
Le store MCP de Claude est ouvert. Skybridge réduit le time-to-ship à 2-4 semaines. Kyle peut construire une voice AI app (ex: "Vocal Meeting Assistant" — enregistre, transcrit, actionne via Claude) et la distribuer dans le Claude App Store. Premier entrant dans le vertical voice = position dominante.
→ Action : Fork skybridge, lire la doc Alpic, prototyper en 1 semaine.

**#2 — Ouvre un GitHub repo pour ton prochain projet voice AI [GRATUIT]**
La distribution par GitHub trending est réelle et gratuite. Un repo bien positionné ("Voice AI MCP App Starter" ou similaire) peut atteindre 1K+ stars en une semaine si le timing et le nom sont bons. Cela nourrit aussi le funnel Alpic/Skybridge.
→ Action : Créer repo public avec README soigné + demo GIF avant tout autre canal.

**#3 — Surveille Palmier Pro pour un partenariat audio [WATCH]**
Palmier Pro a l'infra (Swift macOS + MCP) mais pas d'expertise voice AI. Kyle pourrait proposer un partenariat : intégrer une couche de traitement vocal intelligente dans la timeline Palmier. YC networking = approche directe possible.
→ Action : Contacter l'équipe Palmier sur GitHub/Twitter dans 30 jours si le repo continue de croître.

**#4 — Ne pas builder OpenMontage, mais l'utiliser**
OpenMontage est OSS et mature pour wrapping. Kyle peut lancer un SaaS "PodcastToVideo.ai" basé sur OpenMontage en 4-6 semaines, avec pricing $19-49/mo pour automatiser la conversion podcast → short-form video (Reels, TikTok, YouTube Shorts). Niche claire, CAC potentiellement bas via créateurs.
→ Action : Valider la demande via un tweet / page landing avant de coder.

### 📌 Veille à maintenir
- [alpic.ai](https://alpic.ai/) — blog Skybridge skills (nouvelles capabilities MCP hebdomadaires)
- [trendshift.io](https://trendshift.io/) — GitHub trending daily (détecter le prochain OpenMontage)
- [producthunt.com/leaderboard/monthly/2026/6](https://www.producthunt.com/leaderboard/monthly/2026/6) — top mensuel PH
