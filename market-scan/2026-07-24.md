# 🔥 Market Scan — 2026-07-24

## 📊 Résumé Exécutif
- Apps analysées : 5 (PH Top, GitHub Trending, HN Show)
- Top potentiel : 3 retenues (CREATE OS Sandbox, Natively, TwelveLabs Jockey)
- Opportunités immédiates (BUILD NOW) : 1 (Natively-adjacent)

## 🏆 TOP APP #1 : CreateOS Sandbox
### 1. Identification
- **URL** : [createos.sh](https://createos.sh/products/sandbox)
- **Launch** : Juillet 2026 (PH #1 le 22/07/2026)
- **Fondateur** : Naman Kabra
- **Catégorie** : Infrastructure / Developer Tools / AI Agents
- **Buzz** : #1 Product Hunt 22/07/2026 · Trending HN July 2026

### 2. Proposition de valeur
- **Problème** : Exécuter du code non-fiable d'agents IA dans des envs partagées = risque sécurité majeur
- **Solution** : Sandbox isolée hardware (Firecracker micro-VM) qui démarren en 30ms (p90), se pause quand idle
- **USP** : Pause-to-zero (paiement à l'usage strict) + eBPF egress enforcement + fork natif pour agents multi-branches
- **Target** : Devs AI agents, startups SaaS IA, enterprise AI builders
- **Pricing** : Free tier sans CB · Pay-as-you-go (compute only, no egress fees)

### 3. Stack technique
- **Infra** : Firecracker micro-VMs (AWS Lambda tech), eBPF kernel-level networking
- **SDK** : CLI + SDK + 50+ exemples · Claude plugin intégré
- **Storage** : Compatible S3/MinIO/R2
- **Régions** : EU + US

### 4. Psychologie
- **JTBD** : "Je veux exécuter du code agent sans mettre ma prod en danger"
- **Triggers** : Sécurité (chaque agent a son kernel propre) + économies (pause idle) + rapidité (30ms)
- **Aha moment** : "Je lance un agent IA en sandbox sécurisée en 30ms sans config serveur"
- **Social proof** : Exemples Claude-managed agents, 51 real-world examples publiés

### 5. Go-to-market
- **Launch** : Product Hunt #1 · Blog technique détaillé · Claude plugin → distribution via Anthropic ecosystem
- **Canaux** : Dev Twitter/X · Hacker News · GitHub (exemples open-source) · MCP/Claude marketplace
- **Viral loop** : Chaque dev qui utilise le Claude plugin = publicité organique dans logs/screenshots

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (Firecracker est complexe, mais des abstractions existent)
- **Angle Kyle** : Sandbox vocal — execution isolée pour agents voice AI (tests de prompts, sécurité LLM)
- **Verticaux adjacents** : Voice agent sandboxes, testing harness SaaS pour agents téléphoniques
- **Temps dev** : 3-4 mois pour MVP voice-sandbox

## 🏆 TOP APP #2 : Natively
### 1. Identification
- **URL** : [github.com/Natively-AI-assistant](https://github.com/Natively-AI-assistant/natively-cluely-ai-assistant)
- **Launch** : 2026 · v2.8.0 en cours · GitHub Trending July 2026
- **Fondateurs** : Communauté open-source (irishavmishra + contributors)
- **Catégorie** : Voice AI / Productivity / Interview Copilot
- **Métriques buzz** : 2 000+ stars · 465 forks · 9 000+ users · 700 DAU · GitHub Trending

### 2. Proposition de valeur
- **Problème** : Cluely ($20/mo), Final Round AI ($149/mo), LockedIn AI ($55-70/mo) = coûteux + cloud lock-in + risques RGPD
- **Solution** : AI meeting copilot 100% local, gratuit, avec transcription temps-réel <500ms et RAG local
- **USP** : Stealth mode (invisible screen share) + offline + BYOK + 0$ abonnement
- **Target** : Candidats entretiens tech, commerciaux, étudiants, freelances
- **Pricing** : Open-source gratuit · BYOK pour les modèles cloud

### 3. Stack technique
- **Desktop** : Electron + React + Vite + TypeScript + TailwindCSS
- **Native** : Rust (capture audio zero-copy ABI)
- **STT** : Whisper local ou cloud (Google, Deepgram, Groq, Azure, ElevenLabs)
- **AI** : Gemini, GPT-5.4, Claude 4.6, Groq Llama, Ollama
- **Storage** : SQLite + sqlite-vec (vector search local)

### 4. Psychologie
- **JTBD** : "Je veux de l'aide en temps-réel pendant mes entretiens sans payer ni risquer mes données"
- **Triggers** : Gratuit + vie privée + stealth mode (FOMO de ne pas l'avoir en entretien)
- **Aha moment** : "Il transcrit et répond à la question de l'interviewer en <500ms, invisible"
- **Social proof** : Comparaisons tarifaires explicites vs concurrents · 9K users organiques

### 5. Go-to-market
- **Launch** : GitHub + Reddit (r/cscareerquestions, r/learnprogramming) + HN Show
- **Canaux** : Word-of-mouth viral (communautés candidates) · Star-forking GitHub · Anti-Cluely SEO
- **Viral loop** : Chaque candidat réussi = témoignage → nouveau star GitHub

### 6. Réplication pour Kyle
- **Complexité** : 4/10 (stack connue, Electron + Whisper + LLM)
- **Angle Kyle** : Version B2B — copilot de vente vocal en temps-réel (CRM-aware, training objections)
- **Verticaux** : Call center copilot · Sales coaching · Support tier-1 assistance
- **Temps dev** : 6-8 semaines MVP · SaaS payant avec team features (analytics appels, coaching)

## 🏆 TOP APP #3 : Jockey by TwelveLabs
### 1. Identification
- **URL** : [twelvelabs.io/jockey](https://www.twelvelabs.io/jockey)
- **Launch** : PH #2 le 22/07/2026 · Series B $100M annoncé 01/07/2026
- **Fondateurs** : Jae Lee, Miju Han (San Francisco) · 178 employés
- **Catégorie** : Video AI / Enterprise Intelligence / Developer API
- **Métriques buzz** : $100M levés · Investors : NEA, NAVER, Amazon, Index · PH #2

### 2. Proposition de valeur
- **Problème** : Les bibliothèques vidéo d'entreprise (media, sport, corporate) sont impossibles à chercher — millions de minutes non-indexées
- **Solution** : Agent IA conversationnel qui comprend l'intégralité d'une médiathèque (personnes, moments, contexte) via multimodal AI (visuel + mouvement + audio)
- **USP** : MCP natif (Claude/ChatGPT) + API custom + entity resolution sans facial recognition
- **Target** : Éditeurs médias, plateformes sport, entreprises avec gros volumes vidéo
- **Pricing** : API usage-based (estimé : $0.05-0.15/min vidéo)

### 3. Stack technique
- **Foundation models** : Propriétaire (Marengo + Pegasus, multimodal video-native)
- **Distribution** : MCP server (Claude/ChatGPT), REST API, SDK Python/JS
- **Infra** : Cloud scalable · EU + US · Knowledge stores configurables
- **Features** : Corpus digest, entity resolution, agentic search, structured references

### 4. Psychologie
- **JTBD** : "Je veux trouver n'importe quel moment dans mes 50 000h de vidéo en langage naturel"
- **Triggers** : Autorité ($100M + Amazon comme investor) + Urgence (fenêtre avant que Google/AWS ne copie)
- **Aha moment** : "Je demande 'montre-moi tous les moments où Mbappé dribble à gauche' et ça trouve en secondes"
- **Social proof** : Clients sport (Sport Video Group mention) · Partenariat Red Bull

### 5. Go-to-market
- **Launch** : PH #2 + annonce $100M même semaine = double coup médiatique
- **Canaux** : Enterprise sales (NY + London offices) · Developer API via MCP marketplace · Media/sport verticals
- **Viral loop** : Intégration Claude/ChatGPT → devs testent l'API → migration progressive

### 6. Réplication pour Kyle
- **Complexité** : 9/10 (modèles propriétaires video-multimodal = années de R&D)
- **Angle Kyle** : NON RÉPLICABLE directement · Signal marché : l'audio-search (voice) est le pendant de video-search
- **Opportunité dérivée** : "Jockey pour appels téléphoniques" — search conversationnel dans archives calls CRM
- **Temps dev** : 2-3 mois pour voice-search MVP avec Whisper + embedding search

## 💰 Unit Economics Deep Dive — CreateOS Sandbox
**Sujet** : CreateOS Sandbox · Sources : createos.sh, PH, SimilarWeb estimations

| Métrique | Estimation | Source / Méthode |
|---|---|---|
| **ARR** | ~$200K–500K | Early-stage, free tier dominant, conversion estimée 2-5% |
| **ARPU** | ~$50–150/mois | Usage-based, agents devs → faible au début |
| **Users actifs** | 2 000–8 000 devs | Post-PH spike, early adopter curve |
| **CAC** | ~$0–20 | PH launch organique + dev word-of-mouth |
| **LTV** | ~$600–1 800 | 12 mois × ARPU estimé (churn élevé dev tools) |
| **LTV/CAC** | >30x | Exceptionnel si CAC ≈ $0 (organique) |
| **Payback** | <1 mois | CAC quasi-nul = payback immédiat |
| **Burn estimé** | $80K–150K/mois | Petite équipe infra, pas de fundraise public |
| **Runway** | Inconnu | Bootstrapped ou pre-seed probable |
| **Rev/Employee** | ~$20K–50K ARR/emp | <10 employés estimés |
| **Rule of 40** | N/A (trop tôt) | ARR trop faible pour calcul fiable |

**⚠️ Limites** : Pas de metrics publiques. Estimations basées sur analogies E2B / Daytona au stade similaire.

**Verdict santé** : 🟡 **WATCH** — Unit economics potentiellement excellents (CAC ≈ 0, LTV/CAC >30x) mais ARR encore faible et marché concurrentiel (E2B, Daytona, Modal). La clé : accélération enterprise ou partnership Anthropic/Claude.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | CreateOS Sandbox | Natively | Jockey/TwelveLabs |
|---|:---:|:---:|:---:|
| 📊 Market Size (20%) | 7 | 8 | 10 |
| ⚙️ Complexité inversée (15%) | 4 | 7 | 1 |
| ⏱️ Time-to-Market (15%) | 4 | 8 | 1 |
| 🏟️ Compétition inversée (15%) | 5 | 6 | 3 |
| 💰 Revenue Potential (20%) | 7 | 8 | 9 |
| 🧑‍💻 Founder-Fit Kyle (15%) | 5 | 9 | 4 |
| **Score pondéré** | **5.7** | **7.7** | **4.8** |
| **Verdict** | 🟠 WATCH | 🟢 BUILD NOW | 🔴 SKIP |

**Notes :**
- **CreateOS Sandbox** (5.7) : Marché réel mais complexité technique élevée, concurrence E2B/Daytona. À monitorer.
- **Natively** (7.7) : Stack 100% dans les cordes de Kyle (voice, transcription, LLM). Opportunité B2B sales copilot non exploitée. BUILD NOW l'angle B2B.
- **Jockey/TwelveLabs** (4.8) : Marché énorme mais inaccessible sans $10M+ R&D. Signal stratégique uniquement.

## 📈 Tendances Émergentes
### 1. Infrastructure IA = Nouvelle couche critique
Les sandboxes, runtimes et execution layers pour agents explosent (CreateOS, E2B, Modal, Daytona). Les devs veulent du "AWS Lambda pour agents IA" — isolation, pay-as-you-go, MCP-native. Marché estimé à $500M+ d'ici 2028.

### 2. Anti-subscription / Local-first = Mouvement viral
Natively, OpenClaw (350K+ stars GitHub), et leurs pairs prouvent qu'un positionnement "gratuit + local + vie privée" génère une croissance organique 10-100x supérieure aux SaaS payants. La frustration contre les abonnements SaaS ($20-149/mo) est un moteur viral puissant.

### 3. MCP comme canal de distribution
Les launches réussies de juillet 2026 (CreateOS, Jockey) ont toutes un plugin Claude/MCP. Le Claude MCP Marketplace devient un App Store pour outils IA — distribution organique massive sans publicité payante.

### 4. Video/Audio Intelligence = Infrastructure de l'ère agents
TwelveLabs à $100M prouve que le marché enterprise pour "comprendre du contenu non-structuré" (vidéo, audio) est réel et massif. La même logique s'applique à l'audio : archives calls, podcasts, réunions.

### 5. Open-source comme Go-to-Market
Grok Build (xAI), OpenClaw, Natively, Strix (pentest) — les meilleurs lancements sont open-source d'abord, puis monétisés via cloud/enterprise. Le repo GitHub = la page de vente.

## 💡 Insights Actionnables pour Kyle
### 🎯 Pour Kyle (Voice AI + SaaS)

**1. BUILD NOW : Sales Copilot B2B vocal (Natively → B2B)**
L'angle consumer de Natively (entretiens candidats) est saturé. L'angle B2B ne l'est pas : un copilot vocal temps-réel pour commerciaux pendant leurs appels (objection handling, CRM lookup, suggestions produit). Stack : Electron/web + Whisper + LLM + CRM webhook. Prix cible : $49-99/siège/mois. TAM : marché sales enablement = $5B+.
→ **Différenciation Kyle** : expertise voice AI = avantage compétitif direct. MVP en 6-8 semaines.

**2. OPPORTUNITÉ : Voice Search Archive (Signal Jockey)**
Jockey prouve que les entreprises paient pour "trouver dans un catalogue non-structuré". Le pendant audio n'existe pas encore à l'échelle : chercher dans des milliers d'heures d'appels clients, podcasts, formations. Kyle peut construire "Jockey for Audio" avec Whisper + embeddings + RAG.
→ Marché cible : Call centers, Legal tech, Media. Prix : $200-500/mois.

**3. DISTRIBUTION : Publier un Claude MCP plugin dès le Day 1**
Les deux lancements PH #1 et #2 de juillet ont un plugin Claude. Ce n'est plus optionnel — c'est le canal de distribution principal pour les dev tools IA en 2026.

**4. VIGILANCE : OpenClaw (signal fort, hors scope analyse)**
OpenClaw (350K+ stars, créateur recruté par OpenAI) est le signal le plus fort de l'année : les gens veulent un agent IA personnel qui connecte tous leurs outils locaux. Ce marché va être dominé par OpenAI/Apple dans 12-18 mois. Fenêtre d'opportunité verticale : un "OpenClaw pour les équipes commerciales" ou "pour les recruteurs" — avant que la feature soit native dans ChatGPT.

**5. POSITIONNEMENT : "Local-first + RGPD-ready" = avantage en France/EU**
Le discours vie-privée + local résonne 3x plus fort en France/EU qu'aux USA. Kyle a un avantage géographique naturel pour les verticaux réglementés (santé, finance, RH).
