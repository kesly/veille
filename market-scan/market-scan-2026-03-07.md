# 🔥 Market Scan — 7 mars 2026

## 📊 Résumé Exécutif
- **Apps scannées :** 12+
- **Apps à fort potentiel :** 4
- **Opportunités immédiates :** 2
- **Tendance macro :** 🔥 Le "SaaSpocalypse" — les SaaS traditionnels perdent 30% en bourse, l'ère "build vs buy" bascule vers "build" grâce aux coding agents

---

## 🏆 TOP APP #1 : CollectivIQ
**🎯 Score : 8/10**

### 1️⃣ IDENTIFICATION
- **Nom :** CollectivIQ
- **URL :** collectiviq.com
- **Date de lancement :** Mars 2026 (sortie de stealth)
- **Fondateurs :** John Davie (CEO Buyers Edge Platform, hospitality procurement)
- **Catégorie :** SaaS B2B — AI Aggregation / Enterprise AI
- **Métriques de buzz :**
  - ✅ Couverture TechCrunch (article dédié 4 mars)
  - ✅ Repris par 4+ médias tech
  - ✅ Traction interne validée (déployé chez Buyers Edge avant public launch)

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Les réponses d'un seul LLM sont souvent inexactes/hallucinées
- **Solution :** Query simultané de 10+ modèles (ChatGPT, Gemini, Claude, Grok...) puis fusion des réponses convergentes
- **USP :** "Crowdsourcing des chatbots" — consensus multi-modèles = plus fiable qu'un seul
- **Target :** Entreprises B2B (d'abord hospitality/procurement, puis horizontal)
- **Pricing :** Usage-based

### 3️⃣ STACK TECHNIQUE
- Multi-model orchestration layer
- APIs : OpenAI, Anthropic, Google, xAI (10+ providers)
- Probablement : Node/Python backend, routing & consensus algorithm

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Social proof (TechCrunch, validated internally)
- [x] ROI immédiat (meilleure accuracy = moins d'erreurs)
- [x] Autorité (fondateur CEO d'une entreprise établie)
- **JTBD :** Quand je pose une question critique à l'IA, je veux être sûr que la réponse est fiable, pour éviter des erreurs coûteuses.

### 5️⃣ GO-TO-MARKET
- Incubé dans une entreprise existante → validation interne d'abord
- PR via TechCrunch → crédibilité immédiate
- Usage-based pricing → faible friction d'adoption

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score complexité :** 5/10 (l'orchestration multi-modèles est relativement simple)
- **Verticaux adjacents :** Legal, médical, finance (domaines où l'accuracy est critique)
- **Quick wins :** Ajouter scoring de confiance, explainability, audit trail
- **Notre angle :** Version spécialisée pour un vertical (ex: comptabilité FR → lien avec ClientFlow)
- **Time-to-replicate :** 3-4 semaines MVP
- **⚡ Verdict : WATCH** — intéressant mais pas de moat fort, le marché va se commoditiser vite

---

## 🏆 TOP APP #2 : Claude-Replay
**🎯 Score : 7/10**

### 1️⃣ IDENTIFICATION
- **Nom :** Claude-Replay
- **URL :** github.com/es617/claude-replay
- **Date de lancement :** 6 mars 2026
- **Catégorie :** Dev Tool / Open Source
- **Métriques de buzz :**
  - ✅ 79 points + 28 comments sur HN Show (en 14h)
  - ✅ Engagement élevé (ratio comments/points fort)

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Les sessions Claude Code sont des logs texte difficiles à revoir
- **Solution :** Player vidéo-like pour revoir les sessions Claude Code step-by-step
- **USP :** Seul outil qui transforme des sessions CLI en replay visuel navigable
- **Target :** Développeurs utilisant Claude Code (marché en explosion)

### 3️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Communauté (dev tools, open source)
- [x] ROI immédiat (comprendre ce que l'agent a fait)
- [x] Simplicité (concept clair, usage immédiat)
- **JTBD :** Quand Claude Code termine un long task, je veux comprendre ce qu'il a fait exactement, pour valider et apprendre.

### 6️⃣ OPPORTUNITÉS
- **Angle Kyle :** Directement lié à dotclaud ! Intégrer un replay viewer dans le toolkit
- **Complexité :** 3/10
- **⚡ Verdict : WATCH** — pertinent pour dotclaud, à monitorer

---

## 🏆 TOP APP #3 : Graph-Oriented Generation (GOG)
**🎯 Score : 7.5/10**

### 1️⃣ IDENTIFICATION
- **Nom :** Graph-Oriented Generation
- **URL :** github.com/dchisholm125/graph-oriented-generation
- **Date de lancement :** ~Mars 2026
- **Catégorie :** Dev Tool / AI Infrastructure
- **Métriques de buzz :**
  - ✅ Sur HN Show (early traction)
  - ✅ Claim bold : "Beating RAG for codebases by 89%"

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** RAG classique est médiocre pour naviguer du code (perd le contexte structurel)
- **Solution :** Utilise la structure de graphe du code (imports, dépendances, call graphs) pour une retrieval + génération supérieure
- **USP :** 89% meilleur que RAG standard sur les codebases
- **Target :** Dev teams, AI coding tools, code review platforms

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] ROI immédiat (meilleur code understanding)
- [x] Autorité (benchmarks chiffrés)
- **JTBD :** Quand je veux qu'un LLM comprenne mon codebase, je veux une retrieval qui respecte la structure du code, pour des réponses précises.

### 6️⃣ OPPORTUNITÉS
- **Angle Kyle :** Intégrable dans les outils de dev (dotclaud, code-scanner)
- **Complexité :** 7/10
- **⚡ Verdict : WATCH** — technologie prometteuse, pas encore un produit

---

## 🏆 TOP APP #4 : WebBridge (MCP)
**🎯 Score : 6.5/10**

### 1️⃣ IDENTIFICATION
- **Nom :** WebBridge
- **URL :** github.com/jalabulajunx/WebBridge
- **Date de lancement :** 7 mars 2026
- **Catégorie :** Dev Tool / AI Infrastructure
- **Claim :** "Turns any website into MCP tools by recording browser traffic"

### 2️⃣ PROPOSITION DE VALEUR
- **Problème :** Créer des MCP tools pour chaque API/website est laborieux
- **Solution :** Enregistre le trafic browser → génère automatiquement des MCP tools
- **Target :** Développeurs MCP, AI agents builders

### 6️⃣ OPPORTUNITÉS
- **⚡ Verdict : WATCH** — early stage, mais le concept est puissant pour l'écosystème MCP

---

## 📈 Tendances Émergentes

### 🔥 1. Le SaaSpocalypse (TENDANCE MACRO MAJEURE)
- **Quoi :** ETFs software -30% depuis début 2026. Salesforce, Adobe, Intuit, ServiceNow tous -25-30%
- **Pourquoi :** "Build vs Buy" bascule vers "Build" grâce aux coding agents (Claude Code, Codex)
- **Analyse a16z :** "AI won't kill software — it'll make it bigger" mais les incumbents sans vrai moat vont souffrir
- **Impact Kyle :** 
  - ✅ Les outils qui AIDENT à "build" (dotclaud, code tools) sont dans le bon sens du vent
  - ✅ Les SaaS verticaux avec vrais moats (data, network effects) survivent
  - ⚠️ Les SaaS "commodity" (CRM basique, portails simples) sont les plus menacés

### 2. L'écosystème MCP explose
- WebBridge, Cross-Claude MCP sur HN
- MCP devient le "USB-C des AI agents"
- **Opportunité :** Outils/marketplace autour de MCP

### 3. Dev Tools pour AI Agents
- Claude-Replay, GOG, coding agent platforms
- Les devs ont besoin d'outils pour OBSERVER et DEBUGGER leurs agents
- **Opportunité :** Observability pour AI agents (logs, replay, monitoring)

### 4. Multi-Model Orchestration
- CollectivIQ, consensus-based AI
- Pas un seul modèle mais le meilleur de chaque
- **Opportunité :** Routing intelligent de requêtes vers le meilleur modèle par tâche

---

## 💡 Insights Actionnables pour Kyle

1. **dotclaud est BIEN positionné** — dans la vague "build not buy", les dev tools pour coding agents sont en plein boom
2. **Idée feature dotclaud :** Intégrer un session replay (comme claude-replay) dans le toolkit
3. **ClientFlow reste pertinent** — les SaaS verticaux avec workflow spécifique (relances comptables) ont un moat que le vibe coding ne peut pas remplacer
4. **Surveiller MCP** — l'écosystème MCP tools va exploser, possible opportunité de marketplace

---

## 💰 Unit Economics Deep Dive — CollectivIQ

### Revenue Estimation
- **ARR estimé :** Pré-revenue (vient de sortir de stealth)
- **Pricing :** Usage-based (pas de prix public)
- **Users estimés :** ~500 (Buyers Edge internal + early external)
- **Funding :** Non disclosed (incubé par Buyers Edge Platform)

### Unit Economics
- **CAC estimé :** Faible (PR-driven + incubation)
- **LTV estimé :** Variable (usage-based)
- **Gross Margin :** ~40-50% (coût des API multi-modèles élevé)

### Vulnérabilités
- **Margin squeezée** par les coûts API (10+ providers)
- **Pas de moat technique** — l'orchestration multi-modèles est reproductible
- **Risque plateforme** — dépendant des pricing des LLM providers

### Leçons pour Kyle
- Le modèle usage-based fonctionne pour l'enterprise AI
- L'incubation dans une entreprise existante = validation gratuite
- ⚠️ Attention aux produits avec margins comprimées par les API costs

---

## 🎯 Opportunity Scorecard — Top 3

| Critère (poids) | CollectivIQ | Claude-Replay/Observability | MCP Tools Marketplace |
|-----------------|:-----------:|:---------------------------:|:---------------------:|
| 📊 Market Size (20%) | 7/10 | 6/10 | 8/10 |
| ⚙️ Complexity (15%) | 5/10 | 8/10 | 6/10 |
| ⏱️ Time-to-Market (15%) | 7/10 | 9/10 | 5/10 |
| 🏟️ Competition (15%) | 4/10 | 8/10 | 7/10 |
| 💰 Revenue Potential (20%) | 6/10 | 5/10 | 7/10 |
| 🧑‍💻 Founder Fit (15%) | 5/10 | 9/10 | 7/10 |
| **TOTAL** | **5.7/10** | **7.3/10** | **6.8/10** |
| **Verdict** | SKIP | WATCH | WATCH |

---

## 🚀 Idées de Produits Émergées

1. **Agent Observability Platform** — replay, logs, debugging pour AI coding agents. Marché naissant, forte demande dev. Complexité modérée. → WATCH
2. **MCP Tool Generator** — comme WebBridge mais en SaaS hosted, UI no-code pour créer des MCP tools. → WATCH  
3. **AI Model Router SaaS** — routing intelligent vers le meilleur LLM par type de requête (pas consensus, mais routing optimal). → WATCH

---

*Scanné le 7 mars 2026 à 06:00 UTC*
*Sources : Product Hunt, Hacker News (Show HN), TechCrunch, a16z, Reddit, Brave Search*
