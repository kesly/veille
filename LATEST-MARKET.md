# 🔥 Market Scan — 2026-07-25

## 📊 Résumé Exécutif
- Apps analysées : 7
- Top potentiel : Screenpipe, Sim, PlugThis
- Opportunités immédiates (BUILD NOW) : 1 (Sim-adjacent)

## 🏆 TOP APP #1 : Screenpipe
**URL :** https://screenpipe.com | **Launch :** Juillet 2026 (YC S26) | **Catégorie :** Productivité / AI Agents
**Fondateurs :** Ansh Grover + équipe Mediar Inc. (SF, 6 personnes)
**Métriques buzz :** 20 000+ GitHub ⭐ · HN front page · viral X · YC S26 batch

### Proposition de valeur
- **Problème :** Les travailleurs répètent les mêmes tâches sans mémoire contextuelle entre sessions.
- **Solution :** Enregistre écran + audio 24/7 en local, construit une mémoire structurée, génère des agents IA (standups auto, tickets depuis meetings, SOPs).
- **USP :** 100 % local & privé (zéro cloud), cross-platform Mac/Win/Linux, hackable via "Pipes" (agents markdown).
- **Cible :** Devs, fondateurs, knowledge workers productivité-obsédés.
- **Pricing :** Gratuit (perso/éducation) · Pro $150/siège/mois (commercial) — pivot licence juin 2026.

### Stack technique
- **Backend :** Rust (performance + mémoire sûre)
- **Desktop :** Tauri v2 (cross-platform natif)
- **Frontend :** React / Next.js
- **Storage :** SQLite local + FTS5 full-text search
- **Plugins :** "Pipes" = agents schedulés en markdown · MCP server · 100+ connecteurs

### Psychologie & GTM
- **Triggers :** Privacy (vs Microsoft Recall) · Open-source trust · "vos habitudes de travail → agents"
- **JTBD :** "Je veux automatiser mes tâches répétitives sans uploader mes données."
- **Aha moment :** Premier standup généré automatiquement depuis les enregistrements.
- **GTM :** Dev-led open-source flywheel → stars GitHub → crédibilité YC → monétisation licence.
- **Viral loop :** OSS partageable + intégrations MCP = réseau d'effet croissant.

### Réplication pour Kyle
- **Complexité :** 7/10 (Rust + Tauri non-trivial, mais Pipes = MVP rapide)
- **Verticaux adjacents :** Voice AI memory layer · Sales call intelligence · Customer success automation
- **Angle Kyle :** Construire la couche "voice memory" pour ses clients voice AI → Screenpipe + LLM pour calls = produit différencié
- **Temps de dev (MVP vertical) :** 4-6 semaines avec Screenpipe comme base OSS

## 🏆 TOP APP #2 : Sim
**URL :** https://sim.ai | **Launch :** Juillet 2026 (YC X25) | **Catégorie :** AI Agent Orchestration
**Fondateurs :** Emir Karabeg (CEO) + Waleed Latif (CTO)
**Métriques buzz :** 28 400 GitHub ⭐ · 595 PH upvotes · $7M Series A · 100K+ builders

### Proposition de valeur
- **Problème :** Construire des workflows d'agents IA requiert du code complexe (LangGraph, n8n) avec UX développeur-only.
- **Solution :** Canvas visuel (Figma-like) pour créer, tester et déployer des agents IA multi-LLM avec 1 000+ outils intégrés.
- **USP :** Open-source + multi-LLM (OpenAI, Anthropic, Gemini, Groq, DeepSeek) + multiplayer + human-in-the-loop + env dev/qa/prod.
- **Cible :** Équipes tech et équipes business qui veulent des agents sans code bas-niveau.
- **Pricing :** Free (1K crédits/mois) · Pro $25/user/mo · Max $100/user/mo · Enterprise self-hosted.

### Stack technique
- **Frontend :** Next.js + Bun + Turborepo
- **Open-source :** 100 % sur GitHub
- **Intégrations :** 1 000+ outils, tous les LLM majeurs
- **Infra :** SOC2 compliant, env promotion (dev/qa/prod)

### Psychologie & GTM
- **Triggers :** Open-source trust · "10 minutes pour un agent" · FOMO enterprise (Rivian, Russell Investments).
- **JTBD :** "Je veux déployer des agents IA en production sans recruter des ingénieurs ML."
- **Aha moment :** Premier workflow déployé en < 10 minutes avec canvas drag-and-drop.
- **GTM :** OSS flywheel → YC réseau → HN/PH launch → enterprise upsell (self-hosted).
- **Funding :** $7M Series A · Standard Capital, Paul Graham, Perplexity, SV Angel.

### Réplication pour Kyle
- **Complexité :** 8/10 (plateforme agent multi-LLM complète, concurrence forte)
- **Verticaux adjacents :** Agent vocal spécialisé (call center, support) · Vertical SaaS agents
- **Angle Kyle :** Utiliser Sim comme infra pour créer des workflows voice AI pour clients → partenariat/intégration plutôt que compétition
- **Temps de dev (vertical voice) :** 2-3 mois pour un cas d'usage voice précis sur Sim

## 🏆 TOP APP #3 : PlugThis
**URL :** https://plugthis.ai | **Launch :** 10 juillet 2026 | **Catégorie :** No-Code / Browser Tools
**Fondateurs :** Non divulgués publiquement
**Métriques buzz :** 515 PH upvotes · Trending r/SideProject · viral indie hackers

### Proposition de valeur
- **Problème :** Créer une extension Chrome requiert de maîtriser Manifest V3, les APIs de navigation, et JS/HTML.
- **Solution :** Décris en langage naturel l'extension souhaitée → code Manifest V3 production-ready + backend Supabase optionnel + export ZIP.
- **USP :** Code source appartient à l'utilisateur (pas de lock-in) · Free tier généreux · "Hire a Human" pour builds complexes.
- **Cible :** Créateurs no-code, solopreneurs, marketeurs, PMEs.
- **Pricing :** Free (1 projet) · ~$20/mois (3 projets + intégrations OpenAI/Gemini) · $25/module pour builds humains.

### Stack technique
- **Frontend :** Browser-based, zéro installation
- **Output :** Manifest V3 extensions + Supabase backend optionnel
- **Stack interne :** Non divulguée (probablement Next.js + LLM API)

### Psychologie & GTM
- **Triggers :** Urgence "je veux juste cette extension" · Ownership (code source = le vôtre) · Zero setup.
- **JTBD :** "Je veux automatiser mon workflow Chrome sans apprendre à coder."
- **Aha moment :** Extension fonctionnelle téléchargeable en < 5 minutes.
- **GTM :** SEO content strategy ("chrome extension builder 2026") · PH launch · Free tier viral · "Hire a Human" upsell organique.
- **Concurrent :** bolt.new, Plasmo, Manus, Kromio — mais PlugThis = le plus simple sur browser.

### Réplication pour Kyle
- **Complexité :** 3/10 (wrapper LLM → code template bien défini)
- **Verticaux adjacents :** Extension voice note → transcription · Extension CRM enrichment · Extension sales intelligence
- **Angle Kyle :** "PlugThis for voice" = génère des extensions qui capturent/transcrivent l'audio en 1 chat → vente aux équipes sales
- **Temps de dev MVP :** 1-2 semaines (LLM + template Manifest V3 voice API)

## 💰 Unit Economics Deep Dive — Screenpipe
**Source :** GitHub (20K ⭐), YC S26, licence commerciale juin 2026, équipe 6 personnes.
⚠️ *Pas de chiffres ARR publics — estimations conservatives basées sur pricing affiché et taille d'équipe.*

| Métrique | Estimation | Raisonnement |
|---|---|---|
| **Users total** | ~50 000 | 20K stars → ratio stars/users ~0.4 typique OSS |
| **Users payants** | ~300-500 | 1-3 % conversion free→paid typique OSS |
| **ARPU estimé** | ~$600/an | Mix $150/siège/mois × 1.2 sièges moyen + rabais early |
| **ARR estimé** | ~$200K-$300K | 350 clients × $700 ARPU moyen |
| **CAC** | ~$50-100 | Dev-led OSS = quasi-zéro media spend |
| **LTV** | ~$1 800 | Churn B2B ~30%/an → LTV = ARPU / 0.3 |
| **LTV/CAC** | **18-36x** | Excellent pour OSS commercial |
| **Payback** | < 2 mois | CAC très faible |
| **Burn estimé** | ~$80-100K/mois | 6 personnes SF + infra |
| **Runway** | 12-18 mois | Estimation YC standard deal $500K + revenus |
| **Rev/Employee** | ~$40-50K | Stade early, normal |
| **Rule of 40** | 🟡 ~55+ | Croissance rapide compense marge faible |

**Verdict santé : 🟢 SAIN**
LTV/CAC exceptionnel grâce au modèle OSS developer-led. Risque principal : complexité du pricing enterprise ($150/siège) à prouver vs alternatives open-source gratuites. Pivot licence = signal de monétisation sérieux post-YC.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Screenpipe | Sim | PlugThis |
|---|---|---|---|
| 📊 Market Size (20%) | 8 · €10B+ (AI productivity) | 9 · €50B+ (enterprise agents) | 6 · €2B (browser tools) |
| ⚙️ Complexité inversée (15%) | 3 · Rust+Tauri = 3-4 mois | 2 · Plateforme complète = 6+ mois | 8 · Template + LLM = 2 semaines |
| ⏱️ Time-to-Market (15%) | 4 · 2-3 mois vertical | 3 · 3-4 mois vertical | 9 · < 1 mois MVP |
| 🏟️ Compétition inversée (15%) | 6 · Microsoft Recall + LUCI | 4 · n8n, Langflow, Zapier | 7 · bolt.new mais UX différent |
| 💰 Revenue Potential (20%) | 8 · $150/siège prouvé | 9 · $25-100/user + enterprise | 6 · $20/mo mais ARPU faible |
| 🧑‍💻 Founder-Fit Kyle (15%) | 9 · Voice AI + local AI = natif | 7 · Agents = bon fit mais plateforme | 7 · Voice extension = angle rapide |

| App | Score pondéré | Verdict |
|---|---|---|
| **Screenpipe** | **(8×0.20)+(3×0.15)+(4×0.15)+(6×0.15)+(8×0.20)+(9×0.15)** = **6.5** | 🟡 BUILD ADJACENT |
| **Sim** | **(9×0.20)+(2×0.15)+(3×0.15)+(4×0.15)+(9×0.20)+(7×0.15)** = **6.2** | 🟡 BUILD ADJACENT |
| **PlugThis** | **(6×0.20)+(8×0.15)+(9×0.15)+(7×0.15)+(6×0.20)+(7×0.15)** = **7.0** | 🟡 BUILD ADJACENT → quasi 🟢 |

**Recommandation :** PlugThis est le plus rapide à répliquer (< 1 mois MVP), avec un angle voice unique pour Kyle. Screenpipe offre le meilleur fit expertise mais demande plus d'effort. Sim = meilleur potentiel marché mais compétition établie.

## 📈 Tendances Émergentes
### 1. 🤖 Agents passifs > Agents actifs
Le shift dominant de juillet 2026 : les meilleurs produits (Screenpipe, Sim) ne demandent plus à l'utilisateur d'initier. Ils capturent passivement le contexte et génèrent des livrables automatiquement. L'interface devient invisible.

### 2. 🔒 Local-first comme avantage concurrentiel
Screenpipe, Colibri (744B MoE sur 25 Go RAM) : la privacy et le contrôle des données sont devenus un USP, pas une contrainte. Post-Meta/Limitless acquisition, les utilisateurs fuient vers le local. Opportunité pour tout SaaS "sensitive data".

### 3. 🔧 No-code → "Chat-to-X"
PlugThis, Glaze by Raycast : le paradigme évolue de drag-and-drop vers chat naturel pour générer des outils complets (extensions, apps, workflows). La courbe d'apprentissage s'efface.

### 4. 📦 OSS + licence commerciale = modèle SaaS hybride
Screenpipe, Sim : open-source pour la croissance organique, licence commerciale ou self-hosted payant pour la monétisation. Le VC comprend maintenant ce modèle mieux que le SaaS pur. Frein à l'entrée : 20K+ stars = fossé réputationnel.

### 5. 🎙️ Voice AI infrastructure en dessous du radar
Contexte.dev (#1 PH juillet avec 1 186 upvotes) = "One API to scrape, enrich, and extract". Signal : les développeurs veulent des APIs robustes pour enrichir et structurer des données non-structurées — dont l'audio/voix. La couche infrastructure voice est sous-construite.

## 💡 Insights Actionnables
### 🎯 Pour Kyle (Voice AI + SaaS)

**1. Forker Screenpipe pour le vertical voice** *(semaines 1-4)*
Screenpipe capture déjà l'audio. Kyle peut construire un "Screenpipe for Sales Teams" : capture des calls, mémoire structurée, agents post-call (CRM update, follow-up email, coaching). Complexité : modéré. Différenciation : clair.

**2. PlugThis Voice Extension** *(1-2 semaines)*
Créer un concurrent PlugThis mais spécialisé : génère des extensions Chrome pour capturer/transcrire l'audio du navigateur (meet, zoom, loom). Cible : solopreneurs, équipes sales. Monétisation : freemium $15/mois. Temps de dev : < 2 semaines. Test de marché rapide.

**3. Positionner son offre voice comme "agent passif"**
Le messaging qui marche en juillet 2026 : "vos appels → agents automatiques". Kyle devrait pivoter son pitch de "voice AI" vers "votre équipe sales parle, les agents s'occupent du reste" — en ligne avec le paradigme Screenpipe/Sim.

**4. Surveiller Context.dev** *(signal fort)*
#1 PH mensuel avec 1 186 upvotes : "One API to scrape, enrich, and extract the internet". Potentiellement un partenaire infrastructure pour enrichir les transcriptions voice avec données web en temps réel.

**5. À éviter cette semaine**
- Ne pas rebuild une plateforme agent (Sim a levé $7M avec Paul Graham → impossible à concurrencer frontalement)
- Ne pas lancer dans le local-AI hardware (Colibri = trop technique, trop bas-niveau)

**📌 Prochaine veille :** Surveiller le OpenAI Day PH (26 juillet) — 401 launches en attente. Fort risque d'un breakthrough voice ou agent tool qui change la donne.
