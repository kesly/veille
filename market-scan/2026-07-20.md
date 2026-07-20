# 🔥 Market Scan — 2026-07-20

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : AgentKey
- Opportunités immédiates (BUILD NOW) : 1

## 🏆 TOP APP #1 : AgentKey
### 1. Identification
- **Nom** : AgentKey — [agentkey.app](https://agentkey.app)
- **Launch** : 13 juillet 2026 — #1 Product Hunt du jour
- **Fondateurs** : Chainbase Labs (blockchain data infra)
- **Catégorie** : AI Agent Infrastructure / Live Data Marketplace
- **Métriques buzz** : #1 PH jour, relayé KuCoin, GitHub open-source (agentkey-dev/agentkey)

### 2. Proposition de Valeur
- **Problème** : Les agents IA raisonnent bien mais sont aveugles au web en temps réel (pas d'accès live aux APIs sociales, financières, on-chain)
- **Solution** : Un plugin MCP unique (une install, une clé) qui expose ~1 800 outils en 8 catégories : web, réseaux sociaux, finance, e-commerce, crypto, business data
- **USP** : Zéro gestion d'APIs tierces, zéro multi-abonnements — un seul endpoint, coût à l'usage
- **Target** : Développeurs d'agents IA (Claude Code, Codex, OpenClaw, tout MCP-compatible)
- **Pricing** : Usage-based (fractions de centime/requête) + abonnement mensuel credit pool

### 3. Stack Technique
- **Frontend** : Web dashboard (React probable)
- **Backend** : Node.js/TypeScript, architecture MCP-server
- **Infra** : Chainbase (blockchain data), APIs agrégées, sandbox sécurisé
- **APIs** : X/Twitter, Reddit, YouTube, Binance, web search, data e-commerce…

### 4. Psychologie
- **Trigger principal** : Frustration (agents puissants mais borgnes) → soulagement immédiat
- **JTBD** : "Quand je code un agent, je veux qu'il voie le web comme moi"
- **Aha moment** : Première requête live qui retourne des données réelles en <500ms
- **Social proof** : #1 PH, +mentions Hacker News, adoption visible dans la communauté Claude Code

### 5. Go-to-Market
- **Canal principal** : Developer community (Product Hunt, HN, Discord Claude/Cursor)
- **Viral loop** : Chaque agent qui consomme AgentKey génère des logs publics → cas d'usage → nouveau dev
- **Stratégie** : Open-source core (governance) + SaaS monétisé (data credits)
- **Distribution** : Marketplace MCP Claude + Cursor extensions store

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (agrégation APIs = travail de sape, mais architecture MCP bien documentée)
- **Verticaux adjacents** : AgentKey Voice — données live pour agents vocaux (météo, stocks, agenda en temps réel)
- **Angle Kyle** : Construire un "AgentKey vertical Voice AI" : 50-100 sources spécialisées call center/CRM/agenda — niche précise, moins de concurrence
- **Temps de dev** : 3-4 mois MVP (2 devs)

## 🏆 TOP APP #2 : JustVibe
### 1. Identification
- **Nom** : JustVibe — [justvibe.com](https://justvibe.com)
- **Launch** : Juillet 2026 — #1 PH du jour (462 upvotes), #8 leaderboard semaine 28
- **Fondateurs** : Lianghao Chen (ex-ML Lead Pinterest & The Yes)
- **Catégorie** : AI Search / No-Code App Generation
- **Métriques buzz** : 462 upvotes PH, #8 semaine, articles Daily AI World, Dynamic Business

### 2. Proposition de Valeur
- **Problème** : La recherche web retourne des liens — pas des outils. Planifier un voyage = 12 onglets ouverts.
- **Solution** : Saisissez une requête → JustVibe génère une app interactive fonctionnelle directement dans le navigateur (trip planner, scheduler, simulateur…)
- **USP** : Gratuit, sans compte, apps persistantes ("forever yours"), 12 catégories, live data (prix hôtels, cours boursiers)
- **Target** : Grand public non-technique, early adopters "vibe coders"
- **Pricing** : 100% gratuit (modèle freemium futur supposé, monétisation via Gemini API cost + ads éventuels)

### 3. Stack Technique
- **Frontend** : Sandbox navigateur (iframe sécurisé), React probable
- **Backend** : Google Gemini (génération code/UI), sandboxed execution
- **Infra** : Google Cloud (partenariat Gemini implicite)
- **APIs** : Live data fetching pour prix/stocks/météo en temps réel

### 4. Psychologie
- **Trigger** : Magie instantanée — voir une app naître en secondes depuis une phrase
- **JTBD** : "Quand j'ai besoin d'un outil spécifique, je veux le voir apparaître sans coder"
- **Aha moment** : Premier résultat interactif (trip planner Tokyo personnalisé en <10s)
- **Viral loop** : Partage de l'app générée = recrutement passif d'utilisateurs

### 5. Go-to-Market
- **Canal principal** : Product Hunt + Twitter viralité (demos visuelles)
- **Stratégie** : "Never click a link again" (newsletter PH) — message anti-Google percutant
- **Viral loop** : Chaque app partagée porte l'URL justvibe.com → new users
- **Différenciation** : Vs Perplexity (liens) / ChatGPT (texte) → JustVibe = expérience

### 6. Réplication pour Kyle
- **Complexité** : 8/10 (sandboxed execution + LLM fiable = difficile à parfaire)
- **Verticaux adjacents** : "VoiceVibe" — requête vocale → app interactive générée en temps réel
- **Angle Kyle** : Combiner voice AI + génération d'app : l'utilisateur parle, une app apparaît. Différenciateur fort vs interfaces texte.
- **Temps de dev** : 4-6 mois MVP (nécessite partenariat LLM solide)

## 🏆 TOP APP #3 : OpenKnowledge
### 1. Identification
- **Nom** : OpenKnowledge — [GitHub: open-knowledge](https://github.com/inkeep/open-knowledge)
- **Launch** : 27 juin 2026 (Show HN), article TechTimes 28 juin 2026
- **Fondateurs** : Inkeep (YC-backed, documentation AI startup)
- **Catégorie** : Knowledge Management / AI-First Editor
- **Métriques buzz** : ~1 856 GitHub stars au 5 juillet 2026, Show HN notable

### 2. Proposition de Valeur
- **Problème** : Obsidian manque d'un vrai WYSIWYG + intégration native Claude/Codex. Notion = propriétaire et cher.
- **Solution** : Éditeur markdown WYSIWYG local, GPL-3.0, avec Claude Code / Codex / Cursor intégrés nativement + CLI agents
- **USP** : 100% local first, open-source, synchronisation CRDT (yjs + ProseMirror), graph viewer, terminal UI intégré
- **Target** : Développeurs, solo founders, knowledge workers qui travaillent avec des agents IA
- **Pricing** : Gratuit (open-source GPL-3.0) — modèle de monétisation : Inkeep cloud hosting

### 3. Stack Technique
- **Frontend** : TypeScript, ProseMirror (WYSIWYG), yjs CRDT
- **Backend** : Local-first (filesystem), CLI, macOS app + web UI
- **IA intégrée** : Claude Code MCP, OpenAI Codex, Cursor — via plugin natif
- **Licence** : GPL-3.0

### 4. Psychologie
- **Trigger** : Frustration Obsidian (plugins bricolés) + ras-le-bol Notion (pricing, cloud)
- **JTBD** : "Quand je gère ma base de connaissances, je veux que mon agent IA puisse lire/écrire dedans directement"
- **Aha moment** : Premier agent qui écrit dans vos notes localement, en temps réel
- **Communauté** : HN + dev Twitter + r/Obsidian migration

### 5. Go-to-Market
- **Canal principal** : Show HN + GitHub stars organique + YC network (Inkeep)
- **Stratégie** : Open-source pour l'adoption, cloud Inkeep pour la monétisation
- **Viral loop** : Chaque template partagé = lien GitHub → étoile → visibility
- **Distribution** : Obsidian community, r/PKM, dev newsletters

### 6. Réplication pour Kyle
- **Complexité** : 6/10 (stack connue TS + ProseMirror, mais CRDT = complexité)
- **Verticaux adjacents** : Voice Knowledge Base — dicter ses notes, agent les structure automatiquement
- **Angle Kyle** : Intégrer voice AI dans OpenKnowledge ou fork — "parlez, votre second cerveau se met à jour"
- **Temps de dev** : 2-3 mois pour un fork vertical (déjà open-source)

## 💰 Unit Economics Deep Dive — AgentKey
*Sources : Blog Chainbase, agentkey.app/pricing, GitHub chainbase-labs/Agentkey, KuCoin article*
*Données publiques limitées (J+7 post-launch) — estimations fondées sur analogues MCP marketplace*

| Métrique | Estimation | Confiance |
|---|---|---|
| **ARR** | ~$120K–$360K (J+90 projeté) | 🟡 Faible |
| **ARPU** | ~$29–$99/mois (dev solo à équipe) | 🟡 Moyen |
| **Users actifs** | ~500–2 000 devs (J+7) | 🟡 Faible |
| **CAC** | ~$0 (PH viral, dev word-of-mouth) | 🟢 Élevé |
| **LTV** | ~$350–$1 200 (12-24 mois rétention dev) | 🟡 Moyen |
| **LTV/CAC** | >10x estimé (CAC proche de zéro) | 🟢 Excellent |
| **Payback** | <1 mois | 🟢 Excellent |
| **Burn** | Non public (Chainbase Labs financement crypto) | ⚫ Inconnu |
| **Runway** | Couvert par Chainbase (levée crypto antérieure) | 🟡 Moyen |
| **Rev/Employee** | Non calculable (équipe non divulguée) | ⚫ Inconnu |
| **Rule of 40** | Non applicable (trop tôt) | ⚫ — |

**⚠️ Biais crypto** : AgentKey est porté par Chainbase (data blockchain). Le modèle économique est hybride : revenus SaaS dev + potentiel token économie. Surveiller si un token est introduit (dégrade la thèse SaaS pure).

**Verdict santé : 🟡 TROP TÔT** — métriques insuffisantes à J+7. Recheck dans 60 jours.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | AgentKey | JustVibe | OpenKnowledge |
|---|---|---|---|
| 📊 Market Size (20%) | 8 — marché AI infra >$10B | 9 — search = marché massif | 6 — PKM niché mais croissant |
| ⚙️ Complexité inv. (15%) | 4 — 1 800 APIs à agréger | 3 — sandbox + LLM fiable dur | 6 — fork open-source possible |
| ⏱️ Time-to-Market (15%) | 5 — 3-4 mois MVP | 4 — 4-6 mois, dépend LLM | 7 — 2-3 mois (fork) |
| 🏟️ Compétition inv. (15%) | 6 — quelques concurrents (Composio, Zapier AI) | 5 — Perplexity, ChatGPT, Google | 7 — Obsidian / Notion ne bougent pas vite |
| 💰 Rev. Potential (20%) | 8 — $50-100K MRR réaliste à 12 mois | 5 — gratuit → monétisation floue | 6 — open-source = rev. indirecte |
| 🧑‍💻 Founder-Fit Kyle (15%) | 9 — voice AI agents + données live = fit parfait | 7 — voice query + app gen = innovation | 6 — knowledge mgmt utile mais périphérique |
| **Score pondéré** | **6.75** | **5.50** | **6.30** |
| **Verdict** | 🟡 BUILD ADJACENT | 🟠 WATCH | 🟡 BUILD ADJACENT |

### Recommandation
**AgentKey** est l'opportunité la plus solide pour Kyle : construire un MCP marketplace vertical "Voice AI Data" (CRM, agenda, real-time call data) répond à un besoin existant dans l'écosystème vocal qu'AgentKey ne couvre pas encore spécifiquement.

**OpenKnowledge** offre un chemin plus rapide (fork) vers une niche voice-first knowledge base.

**JustVibe** est à surveiller : si leur modèle de monétisation émerge, la verticale "voice → app" devient très attractive.

## 📈 Tendances Émergentes
1. **MCP devient le standard d'interopérabilité agents** : AgentKey, Grok Build, OpenKnowledge — tous s'appuient sur MCP. Le protocole Anthropic s'impose comme le "USB des agents IA". Implication : construire MCP-first = distribution gratuite.

2. **Shift de la recherche vers l'action** : JustVibe incarne le passage de "lire des résultats" à "interagir avec des outils". Google est challengé non par un meilleur moteur de recherche mais par une interface radicalement différente.

3. **Agents verticaux > agents généralistes** : GitHub Trending montre Strix (pentest), Vibe-Trading (finance), et AgentKey (data). Les agents spécialisés captent de la traction là où les généralistes saturent.

4. **Open-source comme acquisition channel** : OpenKnowledge (GPL-3), AgentKey (core open-source), Strix — tous parient sur GitHub stars → communauté → SaaS premium. C'est le nouveau PLG (Product-Led Growth).

5. **Voice AI + Action** : L'écosystème voice AI est mûr pour la jonction avec les agents actifs. Les pièces existent (voice recognition, LLM, MCP) mais personne n'a encore packagé "je parle → l'agent agit dans mes outils". Fenêtre d'opportunité ouverte ~12 mois.

## 💡 Insights Actionnables
### Pour Kyle — Actions classées par urgence

**🔴 Cette semaine**
- Tester AgentKey (install MCP dans Claude Code) : comprendre le DX, identifier les gaps voice AI
- Star + fork OpenKnowledge : évaluer si un fork "voice-first" est réalisable en sprint

**🟡 Ce mois**
- Sketcher "AgentKey Voice" : un MCP vertical avec 30-50 sources critiques pour agents vocaux (Calendly, HubSpot, Twilio, météo, agenda) — valider la demande en 3 tweets #buildinpublic
- Mapper les intégrations JustVibe manquantes pour le marché voice : si leur API devient publique, pivoter dessus

**🟢 Dans 60-90 jours**
- MVP "Voice Data Connector" : un MCP server qui donne aux agents vocaux accès au CRM + agenda + call logs en temps réel — pricing $29-99/mois
- Recheck AgentKey métriques (users, MRR public, GitHub stars) : décision BUILD ou WATCH

### Signal à surveiller
- AgentKey lève des fonds ou dépasse 5K GitHub stars → accélération de la catégorie = fenêtre se ferme
- JustVibe annonce une API ou monétisation → opportunité voice query + instant app
- Google ou Anthropic lance une fonctionnalité similaire à JustVibe nativement → category killer
