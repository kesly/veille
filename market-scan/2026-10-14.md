# 🔥 Market Scan — 2026-10-14

> ⚠️ Limites de cette session : Product Hunt et Hacker News inaccessibles (DNS bloqué), recherches web peu précises. Signal principal = GitHub Trending hebdo (données réelles) + pages repos. Dates de lancement non vérifiées → filtre « <6 mois » non confirmé. Scores à prendre avec prudence.

## 📊 Résumé Exécutif
- Apps analysées : 3 (toutes open-source, issues de GitHub Trending)
- Top potentiel : TesterArmy / e2e (test E2E par agents IA)
- Opportunités immédiates (BUILD NOW) : 0 (voir scorecard)

## 🏆 TOP APP #1 : TesterArmy — e2e
**1. Identification**
- URL : https://github.com/tester-army/e2e · site https://tester.army/e2e · docs https://e2e.tester.army/docs
- Lancement : non vérifié (© 2026, vers 1.0) · Fondateurs : org TesterArmy (non identifiés)
- Catégorie : dev tools / QA / agents IA · **Open-source Apache-2.0** + plateforme payante TesterArmy
- Buzz : +4 426 ⭐ cette semaine, 10,2k ⭐ total, 492 forks, 78 PR ouvertes ([GitHub Trending](https://github.com/trending?since=weekly)) → critères : croissance, communauté active, engagement

**2. Proposition de valeur**
- Problème : tests E2E fragiles et coûteux à maintenir.
- Solution : on décrit un objectif en langage naturel, un agent pilote l'app ; les étapes sont enregistrées puis rejouées sans appel LLM tant que l'app ne change pas.
- USP : record/replay (coût LLM ≈ 0 en régime stable), web + mobile (Playwright, simulateurs iOS/Android), BYO modèle/clé/local.
- Cible : équipes produit/dev. Pricing : framework gratuit ; plateforme hébergée (PR + cron) payante, tarifs non publics.

**3. Stack** : TypeScript, pnpm workspaces, Playwright, agent-device (mobile), reporter GitHub PR, providers hébergés (Limrun, EAS, Kernel).

**4. Psychologie**
- Triggers : douleur des tests flaky, autorité de l'open-source, FOMO « agents ».
- JTBD : « livrer sans casser la prod sans écrire de tests ».
- Aha : `npx e2e init` → premier test en langage naturel qui passe en minutes.

**5. Go-to-market** : OSS-led (CLI en une commande, exemples Vite/Next/Expo/Flutter...), reporter PR = boucle virale dans les repos, upsell vers cloud.

**6. Réplication**
- Complexité 7/10 (moteur agent + replay fiable). Temps : 3-5 mois pour un MVP crédible.
- Verticaux : QA voix/appels (tester des voice agents), conformité, e-commerce.
- Angle Kyle : **testeur automatisé d'agents vocaux** (scénarios en langage naturel, appels simulés, assertions sur transcript/latence) — niche où Kyle a l'expertise.

## 🏆 TOP APP #2 : HeyGen HyperFrames
**1. Identification**
- URL : https://github.com/heygen-com/hyperframes · https://hyperframes.dev · docs https://hyperframes.heygen.com
- Fondateur : HeyGen (scale-up vidéo IA) · Lancement non vérifié · Catégorie : vidéo programmatique pour agents
- **Open-source Apache-2.0**, sans frais par rendu
- Buzz : +4 732 ⭐/semaine, ~63k ⭐ total, 5,7k forks ; adopté en prod chez HeyGen ([source](https://github.com/heygen-com/hyperframes)) → croissance, communauté, traction corporate

**2. Proposition de valeur**
- Problème : générer des vidéos par code/agent sans timeline propriétaire ni React.
- Solution : compositions en HTML + attributs `data-*`, rendu déterministe MP4 (GSAP, Lottie, Three.js...).
- USP : conçu pour agents (21 skills Claude Code/Codex/Cursor), rendu AWS Lambda, Studio éditeur navigateur.
- Cible : devs, marketeurs, agents. Pricing : gratuit ; cloud render HeyGen (tarifs non publiés).

**3. Stack** : TypeScript, Bun, Node 22+, Puppeteer (headless Chrome), FFmpeg, AWS Lambda.

**4. Psychologie** : autorité (marque HeyGen), simplicité (« HTML → vidéo »), aha = un prompt à l'agent produit un MP4 en local.

**5. GTM** : OSS comme top-of-funnel pour la plateforme HeyGen, skills d'agents (distribution dans les écosystèmes Claude/Cursor), catalogue de blocs réutilisables, Discord.

**6. Réplication**
- Complexité 6/10 pour un clone minimal, 8/10 pour égaler. Temps : 2-3 mois (MVP).
- Verticaux : vidéos de démo produit, récaps data, contenu social automatisé.
- Angle Kyle : vidéos/avatars + voix IA (TTS/clone vocal) pilotés par agent, pour PME FR. Attention : l'OSS HeyGen est gratuit, la valeur est dans la vertical + voix.

## 🏆 TOP APP #3 : Diagram Design (Cathryn Lavery)
**1. Identification**
- URL : https://github.com/cathrynlavery/diagram-design · Auteure : Cathryn Lavery (LittleMight) · Lancement non vérifié
- Catégorie : skill d'agent (design/diagrammes). **Open-source MIT**, aucune monétisation visible
- Buzz : +9 867 ⭐/semaine, ~54k ⭐ total ([source](https://github.com/cathrynlavery/diagram-design)) → viralité forte, communauté ; traction revenus : aucune

**2. Proposition de valeur**
- Problème : diagrammes générés par IA moches (« Mermaid slop »).
- Solution : 44 types de diagrammes en HTML+SVG autonome, variantes light/dark/éditoriale, onboarding de marque, import draw.io/Mermaid/Excalidraw, export SVG/PNG.
- USP : sortie offline sans JS, contrôles CI (overlap, contraste), compatible Claude Code/Codex/Copilot/Kiro.
- Pricing : gratuit (bouton Sponsor).

**3. Stack** : HTML/SVG, Agent Skills (`npx skills add`), Playwright pour PNG, grille 4px.

**4. Psychologie** : goût/statut (« no shadows »), gain immédiat visuel, partage social des rendus ; aha = premier diagramme éditorial en une phrase.

**5. GTM** : distribution via marketplaces de plugins/skills, réseau personnel de l'auteure (newsletter, blog), screenshots partageables.

**6. Réplication**
- Complexité 3/10, 1-3 semaines. Verticaux : skills de design pour docs, slides, rapports.
- Angle Kyle : peu de lien direct ; transposable en « skills » vocaux (templates de scripts d'agents voix) comme lead magnet. Monétisation difficile (produit gratuit).

## 💰 Unit Economics Deep Dive — TesterArmy
⚠️ **Estimations très incertaines** : TesterArmy n'a aucun chiffre public trouvé (pas de Crunchbase/Tracxn/SimilarWeb consultés). Hypothèses de modèle, pas des faits.

| Métrique | Estimation |
|---|---|
| ARR | €0,3-1,5M (hypothèse : 100-400 équipes payantes) |
| ARPU | ~€250-400/mois/équipe |
| Users | 10k+ ⭐ ≈ quelques milliers d'utilisateurs OSS |
| CAC | ~€300-800 (OSS-led, faible) |
| LTV | ~€5-8k (churn annuel ~20%) |
| LTV/CAC | ~8-15x (théorique) |
| Payback | 2-4 mois |
| Burn / Runway | inconnu (équipe réduite supposée) |
| Rev/Employee | inconnu |
| Rule of 40 | non évaluable |

**Verdict santé : 🟡** — traction OSS réelle, monétisation non prouvée, coûts LLM à surveiller (atténués par le replay).

## 🎯 Opportunity Scorecard — Top 3
| App | 📊 Market (20%) | ⚙️ Complexité inv. (15%) | ⏱️ TTM (15%) | 🏟️ Compét. inv. (15%) | 💰 Revenu (20%) | 🧑‍💻 Fit Kyle (15%) | **Score** | Verdict |
|---|---|---|---|---|---|---|---|---|
| TesterArmy e2e | 8 | 4 | 4 | 3 | 7 | 4 | **5.25** | 🟠 WATCH |
| HyperFrames | 7 | 5 | 5 | 3 | 5 | 4 | **4.95** | 🟠 WATCH |
| Diagram Design | 3 | 8 | 9 | 4 | 2 | 3 | **4.60** | 🟠 WATCH |

Note : le fit Kyle de e2e monte à ~7 si l'angle « QA d'agents vocaux » est retenu (score ≈ 6.0 → 🟡 BUILD ADJACENT), à valider avec 5 entretiens clients.

## 📈 Tendances Émergentes
- **Skills/plugins d'agents comme canal de distribution** : mattpocock/skills (~290k ⭐), diagram-design, hyperframes (21 skills) — [GitHub Trending](https://github.com/trending?since=weekly).
- **Agents IA qui pilotent des apps** (test E2E, text-to-CAD +2 173 ⭐, claude-mem mémoire persistante +3 587 ⭐).
- **OSS gratuit → cloud payant** (modèle TesterArmy, HeyGen).
- Signal volume : les Show HN ont été multipliés ~6x depuis ChatGPT mais les posts à succès (20+ pts) peu ([source](https://zeli.app/es/story/49712005)) → la distribution prime sur le produit.
- Faible signal : modèle « SaaS + produit physique » à 10K MRR (podcast Indie Hacker, non vérifié).

## 💡 Insights Actionnables
1. **Valider l'angle « testeur d'agents vocaux »** : 5 appels clients (équipes voice AI) avant tout code ; s'inspirer du record/replay de e2e pour limiter le coût LLM.
2. **Publier un skill/plugin Claude Code voice AI** gratuit (lead magnet, 1-2 semaines) : la distribution par skills est le canal qui explose.
3. **Stratégie OSS-led** : cœur open-source + cloud payant, comme TesterArmy/HeyGen.
4. **Ne pas cloner** HyperFrames ni Diagram Design (gratuits, marques fortes) ; viser une verticale FR + voix.
5. **Corriger la veille** : Product Hunt/HN inaccessibles cette session — ajouter une source accessible (API HN Algolia, flux RSS) pour la prochaine exécution.
