# 🔥 Market Scan — 2026-07-27

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : Glaze by Raycast
- Opportunités immédiates (BUILD NOW) : 1 (Glaze → angle voice/SaaS)

## 🏆 TOP APP #1 : Glaze by Raycast
### 1. Identification
- **URL** : [raycast.com/glaze](https://www.raycast.com/glaze) | [PH](https://www.producthunt.com/products/glaze-4)
- **Launch** : Bêta privée mars 2026 → Public 3 juillet 2026
- **Fondateurs** : Thomas Paul Mann & Petr Nikolaev (Raycast, $47.8M levés)
- **Catégorie** : AI App Builder / No-code natif Mac
- **Buzz** : #1 Product Hunt 3 juillet (574 upvotes), utilisé par Cursor, Linear, Vercel

### 2. Proposition de valeur
- **Problème** : Créer une app Mac native demande des mois de dev Swift/Xcode
- **Solution** : Décrire l'app en langage naturel → AI (Claude Code / Codex) génère + compile une vraie app native Mac
- **USP** : Apps locales, offline, lancent instantanément, avec icône dock
- **Cible** : Solo devs, équipes produit, makers tech-savvy Mac
- **Pricing** : Free (120 crédits one-time) · Pro $20/mois (200 crédits) · Team $30/seat/mois

### 3. Stack Technique
- Frontend : SwiftUI (apps générées nativement)
- Backend : Claude Code + OpenAI Codex (dual AI backend)
- Infra : Raycast cloud + compilation locale
- APIs : Raycast Extensions API, MCP compatible

### 4. Psychologie
- **Triggers** : Autorité (Raycast = marque de confiance chez devs Mac), Social proof (Cursor/Linear/Vercel l'utilisent), Curiosité (voir son idée devenir app en 2min)
- **JTBD** : "Je veux un outil interne custom sans payer un dev"
- **Aha moment** : Première app qui s'ouvre dans le Dock 30s après la description

### 5. Go-to-Market
- Canaux : PH launch orchestré, Twitter/X devs Mac, Raycast community existante (1M+ users)
- Viral loop : Partage d'apps dans le store Glaze public → découverte organique
- Stratégie : Upsell naturel depuis Raycast Pro ($10/mois → Glaze $20/mois)

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (runtime AI → compilation Swift est le vrai challenge)
- **Verticaux adjacents** : Générateur d'agents voice AI (décris ton bot → déploie), Builder d'outils internes SaaS
- **Angle Kyle** : "Glaze for Voice Agents" — décris ton scénario conversationnel → app vAPI/Bland déployée
- **Temps dev** : ~3-4 mois (MVP web → compilateur agent, pas app native)

## 🏆 TOP APP #2 : superpowers (obra)
### 1. Identification
- **URL** : [github.com/obra/superpowers](https://github.com/obra/superpowers)
- **Launch** : Octobre 2025 → 250K+ stars juillet 2026
- **Fondateur** : Jesse Vincent (@obra) — ex-Keyboardio, ex-Perl 6, CEO Prime Radiant
- **Catégorie** : Open-source / AI Coding Framework / Skills pour agents
- **Buzz** : 250K GitHub stars (top 6 tous temps), accepté Anthropic Marketplace jan 2026

### 2. Proposition de valeur
- **Problème** : Les AI coding agents (Claude Code, Cursor…) produisent du code non testé et désorganisé
- **Solution** : 14 "skills" qui forcent l'agent à suivre clarify → design → plan → TDD → review
- **USP** : Framework open-source qui se branche sur 16 outils AI (Claude Code, Cursor, Windsurf, Kiro, Gemini CLI…)
- **Cible** : Développeurs seniors utilisant des AI coding agents
- **Pricing** : 100% gratuit / open-source (MIT)

### 3. Stack Technique
- Frontend : Markdown skills + YAML configs
- Backend : Hooks système dans les AI coding agents
- Infra : Zéro infra — runs localement
- APIs : Compatible Claude Code, Cursor, Windsurf, Gemini CLI, Kiro

### 4. Psychologie
- **Triggers** : Social proof (250K stars = validation ultime), FOMO ("ton agent code mieux que toi sans ça"), Autorité (Jesse Vincent = serial maker crédible)
- **JTBD** : "Je veux que mon AI coding agent produise du code prod-ready"
- **Aha moment** : Premier test TDD que l'agent écrit AVANT d'implémenter

### 5. Go-to-Market
- Canaux : GitHub viral organique, HN Show HN, Twitter devs, Anthropic Marketplace
- Viral loop : Devs partagent leurs "before/after" code quality → effet boule de neige
- Stratégie : Open-source → communauté → Prime Radiant (services/produits à venir)

### 6. Réplication pour Kyle
- **Complexité** : 2/10 (c'est du Markdown + YAML, zéro backend)
- **Verticaux adjacents** : "superpowers for Voice AI" — skills qui forcent la structure des prompts vAPI/Bland
- **Angle Kyle** : Créer un skill pack "Voice Agent Quality" pour Claude Code → monétiser via marketplace
- **Temps dev** : 1-2 semaines pour MVP de skills verticalisés voice AI

## 🏆 TOP APP #3 : Jockey by TwelveLabs
### 1. Identification
- **URL** : [twelvelabs.io/jockey](https://www.twelvelabs.io/jockey)
- **Launch** : Projet open-source antérieur → #2 PH 22 juillet 2026 · $100M Series B 1 juillet 2026
- **Fondateurs** : Jae Lee, Mihail Eric (TwelveLabs) — investisseurs : NEA, NAVER, Amazon, Index
- **Catégorie** : Video AI / Agentic Media Intelligence
- **Buzz** : #2 PH, $100M levés, partenariats Amazon + Index Ventures

### 2. Proposition de valeur
- **Problème** : Les bibliothèques vidéo/photo sont inparcourables — recherche par nom de fichier seulement
- **Solution** : Agent AI qui comprend le contenu vidéo/image (personnes, moments, contexte) et répond en langage naturel
- **USP** : "Retrouve le moment où on a failli rater l'avion" → recherche sémantique multi-modale
- **Cible** : Studios médias, équipes marketing, particuliers (mémoire photo/vidéo)
- **Pricing** : API pay-per-use + plans entreprise (non divulgués publiquement)

### 3. Stack Technique
- Frontend : API + MCP server (Claude/ChatGPT compatible)
- Backend : Marengo (embedding model vidéo) + Pegasus (video-language model)
- Infra : Cloud propriétaire TwelveLabs
- APIs : REST API, MCP pour Claude/ChatGPT, webhooks

### 4. Psychologie
- **Triggers** : Autorité ($100M + Amazon = validité massive), Social proof (PH #2), Magic demo (recherche émotionnelle dans ses propres vidéos)
- **JTBD** : "Je veux retrouver n'importe quel moment dans mes 10 ans de vidéos"
- **Aha moment** : Première recherche par émotion/contexte qui trouve exactement la bonne scène

### 5. Go-to-Market
- Canaux : Enterprise sales, API developer community, MCP ecosystem, PH launch orchestré
- Viral loop : Devs intègrent via MCP → leurs users découvrent TwelveLabs
- Stratégie : Land & expand B2B — API gratuite pour devs → upgrade enterprise

### 6. Réplication pour Kyle
- **Complexité** : 9/10 (ML propriétaire multi-modal, investissement R&D énorme)
- **Verticaux adjacents** : Indexation audio/voice pour call centers, analyse appels commerciaux
- **Angle Kyle** : Intégrer Jockey API pour indexer les conversations voice AI → insights clients
- **Temps dev** : 6-12 mois pour concurrent direct · 2-3 semaines pour intégration API

## 💰 Unit Economics Deep Dive — Glaze by Raycast
> ⚠️ Estimations basées sur données publiques (Raycast $47.8M levés, pricing Glaze, PH metrics). Aucun chiffre officiel Glaze disponible à ce jour.

| Métrique | Estimation | Source/Hypothèse |
|---|---|---|
| **ARR Glaze** | ~€1.5M-3M | Lancé il y a 3 sem. — extrapolé sur PH traction |
| **ARPU** | ~€22/mois (Pro) ou €30/seat (Team) | Pricing officiel |
| **Users payants estimés** | 5K-10K | PH #1 → 574 upvotes → ~2% conversion typique |
| **CAC** | ~€8-15 | Distribution via Raycast base (1M+ users) → CAC très bas |
| **LTV estimée** | ~€240 (Pro, 12 mois) à €720 (Team 2 ans) | Churn ~15%/an hypothèse SaaS devtools |
| **LTV/CAC** | 16x à 48x | Très fort grâce à distribution organique Raycast |
| **Payback period** | <1 mois | Distribution gratuite via base existante Raycast |
| **Funding Raycast** | $47.8M total | Données publiques Crunchbase |
| **Rev/Employee** | NC | ~50-100 pers. chez Raycast |
| **Rule of 40** | 🟢 Estimé >80 | Croissance explosive + marges SaaS |

**Verdict santé Glaze : 🟢 SAIN** — Distribution via Raycast = avantage stratégique majeur, CAC quasi nul, pricing cohérent. Risque : dépendance aux coûts AI (Claude Code/Codex) qui compressent les marges si usage explose.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Glaze (Raycast) | superpowers | Jockey (TwelveLabs) |
|---|---|---|---|
| 📊 Market Size (20%) | 7 — Marché devtools Mac ($2-5B) | 6 — Framework niche devs AI | 9 — Marché vidéo entreprise ($50B+) |
| ⚙️ Complexité inv. (15%) | 3 — Swift + AI runtime, dur | 9 — Markdown/YAML, très simple | 1 — ML multi-modal propriétaire |
| ⏱️ Time-to-Market (15%) | 4 — 3-4 mois pour adjacent | 9 — 1-2 semaines pour skills | 2 — 6-12 mois si concurrent |
| 🏟️ Compétition inv. (15%) | 5 — Lovable/Bolt sur web, Glaze sur native | 8 — Zéro concurrent direct skills AI | 4 — RunwayML, Twelve, Pika, etc. |
| 💰 Revenue Potential (20%) | 7 — €20-30/mois, bon ARPU | 4 — Open-source, montisation indirecte | 8 — Enterprise $$$, API pay-per-use |
| 🧑‍💻 Founder-Fit Kyle (15%) | 8 — SaaS + AI + Mac audience | 6 — Coding agent, pas voice | 7 — Voice AI intégrable via API |

| App | **Score pondéré** | **Verdict** |
|---|---|---|
| **Glaze (Raycast)** | **(7×.20)+(3×.15)+(4×.15)+(5×.15)+(7×.20)+(8×.15) = 5.85** | 🟠 WATCH |
| **superpowers** | **(6×.20)+(9×.15)+(9×.15)+(8×.15)+(4×.20)+(6×.15) = 6.65** | 🟡 BUILD ADJACENT |
| **Jockey (TwelveLabs)** | **(9×.20)+(1×.15)+(2×.15)+(4×.15)+(8×.20)+(7×.15) = 5.60** | 🟠 WATCH |

> **Calculs détaillés** : Glaze = 1.40+0.45+0.60+0.75+1.40+1.20 = **5.80** 🟠 | superpowers = 1.20+1.35+1.35+1.20+0.80+0.90 = **6.80** 🟡 | Jockey = 1.80+0.15+0.30+0.60+1.60+1.05 = **5.50** 🟠

## 📈 Tendances Émergentes
### 1. 🤖 L'ère des "AI App Builders" natifs
Glaze n'est pas seul. L'industrie pivote des web builders (Lovable, Bolt) vers des builders d'apps **natives desktop** (Mac d'abord, Windows à venir). La demande : apps offline, rapides, personnelles. Tendance : chaque plateforme majeure va lancer son propre générateur d'apps natif d'ici 12 mois.

### 2. 📏 La "Méthodologie comme Code" explose
superpowers illustre une tendance forte : encoder des best practices de dev dans des fichiers de config que les agents exécutent automatiquement. Ce pattern ("skills as code") va se reproduire pour chaque domaine : sales, design, legal, support.

### 3. 🎬 La compréhension vidéo devient infrastructure
Jockey + TwelveLabs ($100M) signalent que la vidéo n'est plus un fichier passif — c'est une base de données requêtable. Les entreprises qui ont des archives vidéo (médias, RH, support) sont les clients naturels. La course est lancée entre TwelveLabs, Runway, et les hyperscalers.

### 4. 🔌 MCP = le "USB-C" des agents AI
Les 3 apps analysées intègrent ou supportent MCP (Model Context Protocol). C'est devenu le standard de facto pour connecter les agents AI aux données. Toute nouvelle app qui veut être "agent-ready" doit exposer un MCP server.

### 5. 📈 Infrastructure race > Model race
GitHub trending confirme : les devs ne construisent plus des LLMs — ils construisent la **couche infrastructure** (agents, gateways, MCP servers, skill frameworks). C'est là où l'innovation se passe en juillet 2026.

## 💡 Insights Actionnables
### 💡 Top 3 actions immédiates (cette semaine)

**1. Crée un "superpowers for Voice AI" — 1-2 semaines**
Jesse Vincent a prouvé qu'un set de skills Markdown peut faire 250K stars. Le slot "Voice AI skills" (vAPI, Bland, Retell) est vide. Kyle a l'expertise ET le réseau. Publier sur GitHub + Anthropic Marketplace = distribution gratuite immédiate.
→ *Action : lister 5-6 best practices voice agent qu'on peut encoder en skills*

**2. Expose un MCP server sur ton produit voice AI**
MCP est devenu la norme. Les devs qui cherchent à intégrer du voice AI dans leurs agents vont chercher un MCP server. Être le premier à publier un MCP server "voice-agent-ready" sur Claude/Cursor = avantage early adopter.
→ *Action : identifier quelles données/actions de ton produit méritent un MCP endpoint*

**3. Surveille de près Glaze (Raycast) — signal fort pour ton pricing**
Le modèle Free → Pro $20/mois → Team $30/seat est très propre pour les dev tools AI. Si tu as un SaaS voice AI B2B, ce pricing tier est à copier. L'insight clé : la bêta privée crée de la rareté et de la désirabilité avant le launch public.
→ *Action : si tu vas lancer, structurer une liste d'attente bêta privée dès maintenant*

### ⚠️ Ce qu'il ne faut PAS faire
- **Ne PAS essayer de répliquer Jockey** (TwelveLabs) : $100M et 5 ans de R&D ML. C'est un outil à intégrer, pas à concurrencer.
- **Ne PAS attendre** sur le MCP : la fenêtre early mover se ferme rapidement.
- **Ne PAS ignorer le marché enterprise voice** : les 3 trends pointent vers le B2B — c'est là que l'argent est.
