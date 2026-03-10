# 🔥 Market Scan — 10 mars 2026

## 📊 Résumé Exécutif
- **Sources scannées:** Product Hunt (catégories trending), Hacker News (Show HN front page), Reddit (r/SaaS, r/startups), Twitter (#buildinpublic)
- **Apps identifiées:** 12
- **Apps analysées (3+ critères buzz):** 4
- **Opportunités immédiates:** 2

---

## 🏆 TOP APP #1 : VS Code Agent Kanban

### 1️⃣ IDENTIFICATION
- **Nom:** VS Code Agent Kanban
- **URL:** https://www.appsoftware.com/blog/introducing-vs-code-agent-kanban-task-management-for-the-ai-assisted-developer
- **GitHub:** https://github.com/appsoftwareltd/vscode-agent-kanban
- **Date de lancement:** ~mars 2026
- **Fondateurs:** AppSoftware Ltd (gbro3n sur HN)
- **Catégorie:** Extension VS Code / Dev Tool
- **Métriques de buzz:**
  - 90 points Hacker News, 43 commentaires
  - VS Code Marketplace featured
  - Discussion active sur HN (pain point universel)

### 2️⃣ PROPOSITION DE VALEUR
- **Problème résolu:** "Context rot" — quand tu utilises un AI coding agent (Copilot, Claude Code), le contexte se perd entre les sessions. Les décisions, plans et rationale disparaissent.
- **Solution:** Kanban board dans VS Code avec fichiers .md comme source de vérité. Chaque tâche = un fichier markdown avec frontmatter YAML + historique de conversation.
- **USP:** GitOps-friendly (tout est committable), pas de format propriétaire, workflow plan→todo→implement structuré
- **Target:** Devs qui utilisent AI coding agents quotidiennement (marché en explosion)
- **Pricing:** Extension gratuite (open source)

### 3️⃣ STACK TECHNIQUE
- **Frontend:** Extension VS Code (TypeScript)
- **Backend:** Local (fichiers .md, pas de serveur)
- **Infrastructure:** Dossier `.agentkanban/tasks/` dans le repo
- **Intégrations:** GitHub Copilot Chat, tout agent AI compatible VS Code

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Simplicité — "just markdown files"
- [x] ROI immédiat — résout un pain quotidien
- [x] Communauté — open source, GitOps
- [x] Autorité — résonne avec tous les devs AI
- **JTBD:** "Quand je reviens sur une feature après une semaine, je veux retrouver tout le contexte et les décisions, pour ne pas repartir de zéro avec mon agent AI"
- **Aha moment:** Premier task.md committé avec l'historique complet de la conversation AI

### 5️⃣ GO-TO-MARKET
- **Canal primaire:** Hacker News (90 pts = viral dans la communauté dev)
- **Canal secondaire:** VS Code Marketplace, GitHub
- **Stratégie:** Open source → adoption gratuite → potentiel freemium/pro plus tard
- **Viral loop:** Fichiers .agentkanban/ committés = exposition à toute l'équipe

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score de complexité:** 4/10 (extension VS Code + markdown)
- **Verticaux adjacents:** 
  - Plugin pour Cursor, Windsurf, autres IDE AI
  - SaaS web dashboard cross-IDE (pas juste VS Code)
  - Intégration native dans Claude Code CLI (notre stack!)
- **Quick wins:** Pas de analytics, pas de team dashboard web, pas de reporting
- **Notre angle:** Intégrer ce concept dans dotclaud — un skill `.agentkanban` pour Claude Code
- **Estimation:** 1-2 semaines pour un MVP

**🎯 Verdict:** ⭐⭐⭐⭐ (4/5)
**⏱️ Time-to-replicate:** 2 semaines
**💡 Action:** WATCH — Concept à intégrer dans dotclaud plutôt que répliquer

---

## 🏆 TOP APP #2 : DenchClaw (Local CRM on OpenClaw)

### 1️⃣ IDENTIFICATION
- **Nom:** DenchClaw
- **URL:** https://denchclaw.com
- **GitHub:** https://github.com/DenchHQ/DenchClaw
- **Date de lancement:** ~mars 2026
- **Fondateurs:** DenchHQ (kumar_abhirup)
- **Catégorie:** CRM / Productivity / AI Agent
- **Métriques de buzz:**
  - 110 points HN, 94 commentaires (fort engagement)
  - Skills Store (skills.sh) — marketplace
  - Discord community active

### 2️⃣ PROPOSITION DE VALEUR
- **Problème résolu:** CRM + automatisation trop fragmentés. Les solopreneurs/petites équipes jonglent entre 10 outils.
- **Solution:** CRM local-first construit sur OpenClaw avec agents AI pour outreach, automation
- **USP:** "The only local productivity tool you need" — local-first, extensible via skills
- **Target:** Solopreneurs, indie hackers, petites équipes
- **Pricing:** Open source (MIT)

### 3️⃣ STACK TECHNIQUE
- **Frontend:** Web UI (pnpm web:dev)
- **Backend:** Node.js, construit sur OpenClaw framework
- **Infrastructure:** Local (npx denchclaw)
- **Intégrations:** OpenClaw ecosystem, Skills Store

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Simplicité — `npx denchclaw` et c'est parti
- [x] Communauté — OpenClaw ecosystem, Discord
- [x] ROI immédiat — CRM + outreach agents
- **JTBD:** "Quand je fais du outreach commercial, je veux un CRM avec des agents AI intégrés, pour automatiser mes relances sans quitter mon environnement local"

### 5️⃣ GO-TO-MARKET
- **Canal primaire:** Hacker News, OpenClaw community
- **Canal secondaire:** GitHub, Discord
- **Viral loop:** Skills Store = contribution communautaire

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score de complexité:** 5/10
- **Notre angle:** On est DANS l'écosystème OpenClaw. On pourrait créer des skills spécialisés (CRM resto, CRM comptable) qui se vendent sur le Skills Store.
- **Estimation:** 2-3 semaines pour un skill CRM vertical

**🎯 Verdict:** ⭐⭐⭐⭐ (4/5)
**⏱️ Time-to-replicate:** 3 semaines
**💡 Action:** WATCH — Potentiel de créer des skills verticaux sur leur marketplace

---

## 🏆 TOP APP #3 : ShadowBroker (OSINT Dashboard)

### 1️⃣ IDENTIFICATION
- **Nom:** ShadowBroker
- **URL:** https://github.com/BigBodyCobain/Shadowbroker
- **Date de lancement:** ~mars 2026
- **Catégorie:** OSINT / Intelligence / Dev Tool
- **Métriques de buzz:**
  - 🔥 **300 points HN, 112 commentaires** — le #1 du jour
  - GitHub trending
  - Discussion massive (aviation, maritime, geopolitics)

### 2️⃣ PROPOSITION DE VALEUR
- **Problème:** Les données OSINT sont dispersées sur des dizaines de sources. Pas de vue unifiée.
- **Solution:** Dashboard temps réel agrégant 15+ feeds OSINT (aviation, maritime, satellites, séismes, conflits, GPS jamming)
- **USP:** "Single pane of glass" pour l'intelligence globale. Track jets privés, satellites, navires militaires.
- **Target:** Analystes, journalistes, chercheurs, passionnés géopolitique

### 3️⃣ STACK TECHNIQUE
- **Frontend:** Next.js + MapLibre GL
- **Backend:** FastAPI + Python
- **Infrastructure:** Docker/Podman
- **APIs:** OpenSky Network, AIS Stream, CelesTrak, GDELT, DeepState Map

### 4️⃣ PSYCHOLOGIE DU SUCCÈS
- [x] Viralité — le côté "spy tool" fascine
- [x] Communauté — open source, contributeurs actifs
- [x] Social proof — 300 pts HN en 24h
- **Aha moment:** Voir les jets privés de milliardaires en temps réel sur la carte

### 5️⃣ GO-TO-MARKET
- **Canal primaire:** Hacker News (viral organique)
- **Modèle:** Open source gratuit
- **Potentiel SaaS:** Hosted version, alertes personnalisées, API

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score de complexité:** 7/10 (beaucoup d'intégrations API)
- **Verticaux adjacents:** OSINT pour entreprises (concurrence intelligence), supply chain monitoring
- **Notre angle:** Pas directement aligné avec les projets de Kyle (B2B SaaS focus)
- **Estimation:** 4-6 semaines

**🎯 Verdict:** ⭐⭐⭐⭐⭐ (5/5) en buzz, mais PASS pour réplication
**⏱️ Time-to-replicate:** 6 semaines
**💡 Action:** PASS — Impressionnant mais hors scope (pas B2B SaaS, pas notre niche)

---

## 🏆 TOP APP #4 : Skir (Protocol Buffer Alternative)

### 1️⃣ IDENTIFICATION
- **Nom:** Skir
- **URL:** https://skir.build
- **GitHub:** https://github.com/gepheum/skir
- **Date de lancement:** v1.1, ~mars 2026
- **Catégorie:** Dev Tool / Infrastructure
- **Métriques de buzz:**
  - 107 points HN, 56 commentaires
  - VS Code extension publiée
  - npm package actif

### 2️⃣ PROPOSITION DE VALEUR
- **Problème:** Protocol Buffers (protobuf) est puissant mais complexe, verbose, et fragile pour l'évolution de schémas.
- **Solution:** Langage déclaratif moderne pour définir types, constantes et APIs. Génère du code idiomatique en TS, Python, Java, C++.
- **USP:** "Serialize now, deserialize in 100 years" — évolution de schéma safe avec checks intégrés. Built-in package manager (import depuis GitHub).
- **Target:** Devs backend, équipes microservices

### 6️⃣ OPPORTUNITÉS DE RÉPLICATION
- **Score de complexité:** 9/10 (langage + compilateur + multi-target codegen)
- **Notre angle:** Pas d'opportunité directe

**🎯 Verdict:** ⭐⭐⭐ (3/5)
**💡 Action:** PASS — Trop technique, marché niche, pas SaaS

---

## 📈 Tendances Émergentes

### 1. 🤖 AI Agent Tooling explose
- **DenchClaw** (CRM agents sur OpenClaw), **VS Code Agent Kanban** (task management pour AI devs), **Dvina** (orchestration 120+ apps) — tous lancés cette semaine
- Le tooling AUTOUR des agents AI est le nouveau gold rush
- **Signal:** Construire des outils pour les devs qui utilisent des agents AI, pas juste des agents AI eux-mêmes

### 2. 📂 Local-first & Open Source revival
- DenchClaw (local CRM), ShadowBroker (self-hosted OSINT), Agent Kanban (fichiers .md locaux)
- Les devs veulent posséder leurs données et ne pas dépendre de SaaS cloud
- **Signal:** Le local-first n'est pas mort, c'est un selling point

### 3. 🛠️ Developer Experience (DX) comme marché
- Skir (meilleur protobuf), Agent Kanban (meilleur workflow), ChurnGuard AI (churn prediction open source)
- Les devs paient pour des outils qui leur font gagner du temps
- **Signal:** Les extensions VS Code et les CLI tools sont des canaux de distribution puissants

---

## 💡 Insights Actionnables pour Kyle

1. **dotclaud opportunity:** Le concept Agent Kanban (persistent task context en .md) est EXACTEMENT ce que dotclaud pourrait intégrer comme skill. Un skill `agent-kanban` pour Claude Code serait killer.

2. **Skills Store (skills.sh):** DenchClaw a créé un marketplace de skills OpenClaw. Kyle pourrait vendre des skills dotclaud sur cette plateforme ou créer sa propre marketplace.

3. **CRM vertical sur OpenClaw:** DenchClaw prouve qu'un CRM local sur OpenClaw a de la traction. Notre projet RestoAI pourrait pivoter vers un "skill OpenClaw pour restaurants" plutôt qu'une landing page standalone.

---

## 🚀 Idées de Produits Émergées

| Idée | Source | Effort | Potentiel |
|------|--------|--------|-----------|
| Skill `agent-kanban` pour Claude Code | VS Code Agent Kanban | 1-2 sem | ⭐⭐⭐⭐ |
| Skills verticaux CRM sur Skills Store | DenchClaw | 2-3 sem | ⭐⭐⭐ |
| SaaS OSINT alertes (hosted ShadowBroker) | ShadowBroker | 4-6 sem | ⭐⭐ |

---

## 💰 Unit Economics Deep Dive — VS Code Agent Kanban

### Revenue Estimation
- **ARR déclaré/estimé:** €0 (open source, pas de monétisation actuelle)
- **Méthode d'estimation:** Gratuit — potentiel freemium non exploité
- **Pricing moyen (ARPU):** €0
- **Nb users estimés:** ~500-2000 (basé sur 90 pts HN + VS Code installs early)

### Unit Economics
- **CAC estimé:** ~€0 (croissance organique HN + VS Code Marketplace)
- **Canaux principaux:** HN, GitHub, bouche-à-oreille dev
- **LTV estimé:** €0 (pas encore monétisé)

### Benchmarks
- **Potentiel de monétisation:** Pro tier avec team features, analytics, cloud sync
- **Comparable:** Linear ($35M ARR), Shortcut — mais pour le workflow AI-specific

### Vulnérabilités identifiées
- Pas de monétisation = pas de moat business
- VS Code-only = pas cross-IDE
- Pas de team features (web dashboard, permissions)
- Dépendance à l'API Copilot Chat

### Leçons pour Kyle
- Les outils "boring tech" (markdown, fichiers locaux) résonnent fort avec les devs
- Open source → adoption → lock-in → monétisation (le playbook classique)
- Le marché "AI developer tooling" est en pleine explosion — timing parfait pour dotclaud

---

## 🎯 Opportunity Scorecard — Top 3 du Jour

| Critère (poids) | Agent Kanban Skill | CRM Skills Store | OSINT SaaS |
|-----------------|:------------------:|:----------------:|:----------:|
| 📊 Market Size (20%) | 7/10 | 6/10 | 5/10 |
| ⚙️ Complexity (15%) | 8/10 | 7/10 | 4/10 |
| ⏱️ Time-to-Market (15%) | 9/10 | 7/10 | 4/10 |
| 🏟️ Competition (15%) | 7/10 | 8/10 | 6/10 |
| 💰 Revenue Potential (20%) | 6/10 | 7/10 | 5/10 |
| 🧑‍💻 Founder Fit (15%) | 9/10 | 7/10 | 3/10 |
| **TOTAL** | **7.5/10** | **7.0/10** | **4.6/10** |
| **Verdict** | **BUILD** | **WATCH** | **SKIP** |

---

## 📊 Cumulative Tracker
→ Voir fichier global : `veille/market-scan/TRACKER.md`
- Opportunités totales trackées aujourd'hui : 4
- BUILD NOW actifs : 1 (Agent Kanban skill pour dotclaud)
- WATCH en observation : 2 (DenchClaw skills, Dvina)
- SKIP : 1 (ShadowBroker)
