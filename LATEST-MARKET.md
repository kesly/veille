# 🔥 Market Scan — 2026-07-06

## 📊 Résumé Exécutif
- Apps analysées : 6 (Glaze, Humalike, Context.dev, Tabstack, Acti, OpenClaw)
- Top potentiel : Humalike (#1), Glaze (#2), Context.dev (#3)
- Opportunités immédiates (BUILD NOW) : 0 · BUILD ADJACENT : 1 (Humalike)

## 🏆 TOP APP #1 : Humalike
### 1. Identification
- **Nom** : Humalike · **URL** : humalike.ai
- **Launch** : 1er juillet 2026 (PH #2 du jour, 162 upvotes, 449 pts)
- **Fondateurs** : non publics · **Investisseurs** : premiers LPs d'ElevenLabs et Revolut
- **Catégorie** : Infrastructure comportementale pour agents IA
- **Buzz** : Top PH July 2026, Nature article sur "AI societies", trending #buildinpublic

### 2. Proposition de Valeur
- **Problème** : Les agents IA sont techniquement compétents mais socialement désastreux en groupe (parlent trop, coupent la parole, ne savent pas quand se taire)
- **Solution** : Suite d'APIs comportementales (turn-taking, theory of mind, norms, persona, social memory)
- **USP** : API "Turn-Taking" flagship — le seul produit qui dit à un agent *quand* parler basé sur des recherches in-house (LoSoNA benchmark, modèle HUMA)
- **Target** : Builders d'agents vocaux, compagnons IA, NPCs, tuteurs, humanoides
- **Pricing** : $20 free tokens à l'inscription · Usage-based ensuite · Enterprise non communiqué

### 3. Stack Technique
- APIs REST spécialisées par comportement · Recherche in-house (LoSoNA, HUMA) · Probablement fine-tuning LLM + règles pragmatiques · Infrastructure cloud

### 4. Psychologie & JTBD
- **JTBD** : "Je veux que mon agent vocal ne soit pas perçu comme un bot en conversation de groupe"
- **Aha moment** : Premier appel où l'agent ne coupe plus la parole → ressenti immédiat
- **Triggers** : Autorité (recherche publiée), social proof (ElevenLabs investors), urgence (early API access)

### 5. Go-to-Market
- **Canal principal** : Product Hunt + communauté voice AI builders
- **Viral loop** : Les apps construites avec Humalike démontrent la valeur → les builders adoptent
- **Distribution** : Partenariats avec plateformes voice AI (Vapi, Retell, Bland) plausibles

### 6. Réplication
- **Complexité** : 7/10 (recherche ML + fine-tuning + infra temps réel)
- **Verticaux adjacents** : Réunions IA, gaming NPC, plateformes RH, téléphonie
- **Angle Kyle** : Intégrer cette couche comportementale DANS ses produits voice AI existants ou white-label turn-taking pour ses clients
- **Temps dev** : 6-12 mois pour un MVP crédible

## 🏆 TOP APP #2 : Glaze by Raycast
### 1. Identification
- **Nom** : Glaze by Raycast · **URL** : glaze.app
- **Launch** : Beta privée mars 2026 → Public juillet 2026 (PH top mensuel juillet)
- **Fondateurs** : Équipe Raycast (Thomas Paul Mann, Petr Rajtsev)
- **Catégorie** : Vibe-coding platform + App Store desktop
- **Buzz** : Top PH juillet 2026, couverts par The Verge, AlternativeTo, HN thread 200+ comments

### 2. Proposition de Valeur
- **Problème** : Créer une app Mac utile nécessite des mois de développement ou un dev freelance
- **Solution** : Décrire l'app en langage naturel → app Mac native générée, publiable dans un store
- **USP** : L'app tourne EN LOCAL (accès fichiers, menu bar, raccourcis clavier, mode offline) + store communautaire pour découvrir/forker les apps des autres
- **Target** : Professionnels non-dev, power users Mac, équipes sans ressources dev
- **Pricing** : Tier gratuit (crédits journaliers) + plans payants $20-30/mo · Requiert macOS Tahoe + Apple Silicon

### 3. Stack Technique
- **Frontend** : Raycast native Mac framework · **IA** : Claude Code + OpenAI Codex en backend
- **Distribution** : Intégré dans Raycast launcher (100K+ users) + store séparé glaze.app

### 4. Psychologie & JTBD
- **JTBD** : "Je veux une micro-app pour mon workflow exact sans attendre un dev"
- **Aha moment** : Premier app fonctionnelle en 2 minutes depuis un prompt → effet waouh garanti
- **Triggers** : Social proof (Cursor, Linear, Vercel l'utilisent), ownership (ton app, dans ton dock), communauté (voir les apps des autres → inspiration → création)

### 5. Go-to-Market
- **Distribution existante** : 100K+ utilisateurs Raycast quotidiens = cold start évité
- **Viral loop** : Créer une app → la partager → d'autres la fork → créateur visible dans le store
- **Médias** : Launch coordonné blog + X + PH + partenariats presse tech

### 6. Réplication
- **Complexité** : 9/10 (distribution Raycast = fossé infranchissable, infra LLM + sandbox natif Mac)
- **Verticaux adjacents** : Version web (moins fort), version VS Code extension, version mobile
- **Angle Kyle** : Construire des Glaze apps pour automatiser ses workflows voice AI · PAS de réplication directe
- **Temps dev** : Impossible à répliquer (moat = distribution Raycast)

## 🏆 TOP APP #3 : Context.dev
### 1. Identification
- **Nom** : Context.dev · **URL** : context.dev
- **Launch** : Fondé 2025 · PH launch mars 2026 (2ème launch) · YC-backed
- **Fondateur** : Yahia Bakour (solo) — ex Principal SWE Amazon, co-fondateur StockAlarm.io (225K+ users)
- **Catégorie** : API web scraping + enrichissement de données pour agents IA
- **Buzz** : PH top developer tools 2026, 5 000+ businesses utilisatrices, Mintlify + Daily.dev comme références

### 2. Proposition de Valeur
- **Problème** : Les modèles IA sont puissants mais aveugles au web en temps réel — les agents hallucinent sur des données obsolètes
- **Solution** : Une seule API pour scraper, enrichir et comprendre le web : markdown propre, brand data (logos/couleurs), crawl, screenshots, research agents
- **USP** : Agent-native design — coller une ligne dans son coding agent et il s'inscrit, récupère la clé API et câble lui-même l'intégration. SDK TypeScript/Python/Ruby inclus.
- **Target** : Développeurs d'agents IA, startups SaaS, équipes data
- **Pricing** : Hobby $25/mo · Starter $49 · Pro $149 · Growth $299 · Scale $499-$949 · Enterprise custom · Pas facturé si bloqué/erreur

### 3. Stack Technique
- API REST + SDKs · Backend cloud scalable · Accessibilité DOM (comme Tabstack) pour réduction coûts LLM
- YC infrastructure probable (AWS/GCP) · Solo founder (90% du code écrit par Yahia)

### 4. Psychologie & JTBD
- **JTBD** : "Je veux que mon agent IA ait accès au web live sans construire et maintenir un scraper"
- **Aha moment** : Agent qui cite une source live à jour → confiance utilisateur multipliée
- **Triggers** : Autorité (YC-backed), simplicité (une ligne d'intégration), preuve sociale (5K+ businesses)

### 5. Go-to-Market
- **Canal** : PH + X + communauté YC · SEO "web scraping API" très fort
- **Viral loop** : Les agents construits avec Context.dev génèrent du bouche-à-oreille quand ils "savent" des infos récentes
- **Moat** : Qualité des données + fiabilité + DX irréprochable

### 6. Réplication
- **Complexité** : 5/10 (infra scraping robuste est difficile mais faisable en 2-4 mois avec les bons outils)
- **Verticaux adjacents** : API spécialisée par secteur (finance, e-commerce, B2B SaaS)
- **Angle Kyle** : Utiliser Context.dev comme brique pour enrichir ses agents voice AI (research avant appel, fiche client live) · Pas de réplication directe
- **Temps dev** : 3-6 mois pour un vertical spécialisé

## 💰 Unit Economics Deep Dive — Humalike
> ⚠️ Humalike vient de lancer (1er juillet 2026) — pas de chiffres publics. Estimation raisonnée basée sur benchmarks sectoriels API comportementale/voice AI.

| Métrique | Estimation | Source/Méthode |
|---|---|---|
| **ARR** | $120K–$500K | Early-stage API tool, pricing usage-based |
| **Users (payants)** | 50–300 builders | Comparaison Hume AI early stage |
| **ARPU** | $200–$1 500/mo | Mix dev indé + startups + early enterprise |
| **CAC** | $50–$200 | PH launch + organique (early leverage) |
| **LTV** | $2 000–$18 000 | Churn ~3-5%/mo estimé early API startup |
| **LTV/CAC** | 10–90x | Favorable si rétention tient |
| **Payback** | 1–3 mois | Usage-based = cash positif rapide |
| **Burn** | $20K–$80K/mo | 2-5 personnes, recherche ML |
| **Runway** | 18–36 mois | Seed + revenus (investisseurs ElevenLabs/Revolut) |
| **Rev/Employee** | $24K–$100K ARR/emp | Très early, à surveiller |
| **Rule of 40** | ~40–60 (estimé) | Croissance forte > burn modéré |

**Verdict santé : 🟡 Trop tôt pour juger — signaux positifs mais pas de données**
- ✅ Backing qualité (ElevenLabs investors)
- ✅ Marché en croissance ($2.4B → $47.5B voice AI d'ici 2034)
- ✅ Problem-solution fit évident pour tout builder voice AI
- ⚠️ Traction réelle inconnue · Risque churn fort si pas de stickiness API
- ⚠️ Pas de pricing publié complet → difficulty d'estimer ARR avec précision

## 🎯 Opportunity Scorecard — Top 3
| Dimension (Poids) | 🥇 Humalike | 🥈 Glaze/Raycast | 🥉 Context.dev |
|---|---|---|---|
| 📊 Market Size (20%) | 7 — $2.4B→$47B voice AI | 6 — no-code $13B 2026 | 6 — web scraping $3-5B |
| ⚙️ Complexité inv. (15%) | 4 — ML + infra temps réel | 2 — moat Raycast imbattable | 5 — API + scraping faisable |
| ⏱️ Time-to-Market (15%) | 4 — 6-12 mois MVP | 2 — impossible répliquer | 6 — 3-6 mois vertical |
| 🏟️ Concurrence inv. (15%) | 8 — blue ocean behavioral | 5 — compétition vibe-coding | 5 — Firecrawl/Apify existent |
| 💰 Revenue Potential (20%) | 7 — enterprise API stickiness | 6 — distribution forte mais Mac-only | 6 — pricing clair, 5K clients |
| 🧑‍💻 Fit Kyle (15%) | **9** — voice AI = cœur de métier | 3 — pas son marché | 3 — brique outil pas verticale |
| **Score Pondéré** | **6.55** | **4.10** | **5.35** |
| **Verdict** | 🟡 BUILD ADJACENT | 🔴 SKIP (répliquer) | 🟠 WATCH |

**Calculs détaillés :**
- Humalike : 7×0.20 + 4×0.15 + 4×0.15 + 8×0.15 + 7×0.20 + 9×0.15 = 1.40+0.60+0.60+1.20+1.40+1.35 = **6.55**
- Glaze : 6×0.20 + 2×0.15 + 2×0.15 + 5×0.15 + 6×0.20 + 3×0.15 = 1.20+0.30+0.30+0.75+1.20+0.45 = **4.20**
- Context.dev : 6×0.20 + 5×0.15 + 6×0.15 + 5×0.15 + 6×0.20 + 3×0.15 = 1.20+0.75+0.90+0.75+1.20+0.45 = **5.25**

## 📈 Tendances Émergentes
### 1. 🎭 Behavioral Layer = le nouveau "missing piece" des agents IA
Les agents sont désormais techniquement capables — le gap est comportemental. Humalike, Hume AI, et plusieurs startups stealth ciblent turn-taking, emotion detection, social norms. La prochaine guerre: qui standardise cette couche ?

### 2. 🏗️ "Vibe Coding" → App Stores personnels
Glaze n'est pas une anomalie. Replit, v0, Lovable, Bolt, Cursor — tous poussent vers l'app en 5 minutes. La tendance de fond : chaque power user aura son app store personnel de micro-outils générés. Le moat se déplace vers la distribution (Raycast) et le store network effects.

### 3. 🤖 Agent-Native = nouveau "mobile-first"
Context.dev, Tabstack, Firecrawl — toutes ces APIs se positionnent "agent-native" comme on disait "mobile-first" en 2012. Les prochains 18 mois : chaque API existante sera refactorisée pour être consommée par des agents, pas des humains.

### 4. 🌐 Local-First AI reprend du terrain
OpenClaw (210K+ étoiles GitHub, 2M users semaine 1) a montré que la confidentialité locale crée une demande massive. Glaze tourne en local. La tendance : "your AI, your machine, your data" devient un argument commercial fort vs cloud.

### 5. 🧩 MCP comme infrastructure de distribution
Tous les outils mentionnés (Context.dev, Tabstack, Glaze) peuvent exposer des MCP servers. MCP (Model Context Protocol d'Anthropic) est en train de devenir le "npm" des agents IA — une explosion de serveurs MCP spécialisés à anticiper.

## 💡 Insights Actionnables pour Kyle
### 🔥 Action #1 — Tester Humalike maintenant (gratuit, $20 tokens offerts)
Kyle est expert voice AI → les APIs turn-taking et social memory de Humalike peuvent directement améliorer ses produits existants. Créer un compte, tester l'API turn-taking sur un use case client réel. Si le résultat est convaincant → USP différenciante à communiquer aux clients.
**Action concrète** : Créer compte sur humalike.ai · Tester turn-taking sur un agent vocal existant · Mesurer l'impact sur le ressenti utilisateur.

### 🔥 Action #2 — Construire une Glaze app "voice AI workflow"
Raycast + Glaze = 100K+ dev power users. Créer une app Glaze pour un workflow vocal (ex. transcription → action → CRM) et la publier sur le store. C'est de la visibilité gratuite auprès d'une audience de builders.
**Action concrète** : Installer Glaze (nécessite Mac + Apple Silicon) · Builder une app utile pour workflows voice AI · Publier sur le store public.

### 🔥 Action #3 — Positionner comme "la couche comportementale" avant que ce soit mainstream
La behavioral layer pour agents IA est en train d'émerger. Kyle peut devenir une référence sur ce sujet (newsletters, posts X, conférences) AVANT que le marché soit saturé. C'est le moment d'écrire sur "pourquoi votre voice AI agent échoue en conversation de groupe".
**Action concrète** : Thread X sur la "behavioral layer gap" des agents vocaux · Citer Humalike + ses propres observations clients · Établir thought leadership.

### ⚠️ Signal d'alarme — MCP Server Distribution
Si Kyle n'a pas encore exposé ses produits voice AI via MCP, c'est une priorité. La distribution via MCP servers devient un canal d'acquisition émergent (Claude Desktop, Cursor, Glaze). Un MCP server bien conçu = présence dans les environments de travail de milliers de devs.

### 📌 À surveiller dans 30 jours
- Humalike : premiers retours publics sur la qualité du turn-taking API
- Glaze app store : combien d'apps publiées ? Network effects en construction ?
- Nouveaux entrants behavioral layer : Hume AI (concurrent direct Humalike), ElevenLabs (déjà dans la voix)
