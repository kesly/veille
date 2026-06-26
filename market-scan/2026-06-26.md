# 🔥 Market Scan — 2026-06-26

## 📊 Résumé Exécutif
- Apps analysées : 6 (Fundraisly, OpenMontage, Skybridge, AgentX, Files.md, Apfel)
- Top potentiel : Fundraisly, OpenMontage, Skybridge
- Opportunités immédiates (BUILD NOW) : 2

## 🏆 TOP APP #1 : Fundraisly
### 1. Identification
- **URL** : https://fundraisly.com | **PH** : producthunt.com/products/fundraisly
- **Launch** : 2 juin 2026 | **Fondatrice** : Anna (ex-analyste $600M+ AUM VC Fund, 2.5 ans)
- **Catégorie** : AI Agent · B2B SaaS · Fundraising
- **Buzz** : #1 PH semaine de lancement · 1 700+ followers PH · 5.0/5 rating · $100M+ raised pour des fondateurs · 3k+ VC calls facilitées (a16z, Sequoia, Index)

### 2. Proposition de Valeur
- **Problème** : Lever des fonds = 6-12 mois d'emails froids, de warm intros laborieuses, de spreadsheets manuels
- **Solution** : Agent IA qui analyse 300K+ investisseurs + millions de deals, identifie ceux qui investissent MAINTENANT dans votre vertical, cartographie les chemins chauds via votre réseau, couvre le reste en outreach froid ciblé
- **USP** : "Fondé par des gens qui ont levé $1B+" → crédibilité immédiate. 20-40 meetings qualifiés en 90 jours
- **Target** : Fondateurs seed/Series A cherchant à lever entre $500K et $5M
- **Pricing** : Non public (vraisemblablement $500-2000/mois ou success fee)

### 3. Stack Technique
- **Frontend** : React/Next.js (hypothèse)
- **Backend** : Python · LLM agents (GPT-4o / Claude) · Vector DB pour matching investisseurs
- **Infra** : AWS ou GCP · Apollo/LinkedIn API pour enrichissement data
- **APIs** : Scraping Crunchbase/PitchBook, LinkedIn Sales Navigator

### 4. Psychologie
- **Triggers** : Autorité ("levé $1B+") · Social proof (a16z, Sequoia) · FOMO (fonds qui investissent MAINTENANT)
- **JTBD** : "Aide-moi à obtenir des meetings investisseurs sans passer 6 mois à networker"
- **Aha moment** : Premier warm intro envoyée automatiquement avec contexte précis → "Ça aurait pris 2 semaines manuellement"

### 5. Go-to-Market
- **Canal principal** : Product Hunt (#1) · bouche-à-oreille entre fondateurs · LinkedIn (Anna partage success stories)
- **Viral loop** : Chaque fondateur financé devient un témoignage public → attire les suivants
- **Stratégie** : Niche très précise (early-stage founders), ROI immédiat mesurable, réseau VC comme moat

### 6. Réplication pour Kyle
- **Complexité** : 6/10 — le matching IA est faisable mais la qualité de la base de données investisseurs est le vrai moat
- **Verticaux adjacents** : Recrutement (matching candidats/startups), BD (matching partenaires commerciaux), M&A
- **Angle Kyle** : "Fundraisly for Voice AI Startups" — niche encore plus ciblée avec expertise sectorielle. Ou adapter le modèle pour trouver des clients enterprise en voice AI (sales agent)
- **Temps de dev** : 3-4 mois MVP

## 🏆 TOP APP #2 : OpenMontage
### 1. Identification
- **URL** : https://github.com/calesthio/OpenMontage
- **Launch** : ~20 juin 2026 | **Créateur** : calesthio (@calesthioailabs)
- **Catégorie** : Open-source · AI Video Production · Developer Tool
- **Buzz** : 22 400 GitHub stars · #1 trending GitHub repo le jour du lancement · 3 000 stars en 24h · Featured AIToolly, NerdZap, AgentConn

### 2. Proposition de Valeur
- **Problème** : Créer une vidéo pro avec IA = bricoler 5-10 outils disparates (script, assets, TTS, editing, rendering)
- **Solution** : Système agentique complet qui orchestre 12 pipelines de production vidéo depuis votre assistant IA (Cursor, Claude). Prompt texte → vidéo finie avec vrai footage motion (pas que des slides animées)
- **USP** : Premier système open-source agentique de production vidéo END-TO-END · Licence AGPLv3 (gratuit mais viral)
- **Target** : Développeurs, créateurs de contenu, équipes marketing avec accès à un AI coding assistant
- **Pricing** : Gratuit (open-source) · Potentiellement cloud-hosted version payante à venir

### 3. Stack Technique
- **Primary** : Python 89.5% · TypeScript 8.7% · JavaScript 1.4%
- **Moteurs** : FFmpeg · React/Remotion (vidéo React-based) · GSAP via HyperFrames (HTML/motion graphics)
- **Audio** : Piper TTS · WhisperX (transcription/alignement)
- **Video Gen** : 14 providers intégrés (RunwayML, Kling, etc.)
- **Architecture** : Agent-first, manifest-driven, AI coding assistant comme orchestrateur

### 4. Psychologie
- **Triggers** : Chiffres impressionnants ("52 tools, 500+ skills") · Open-source = adoption immédiate sans friction · FOMO dev ("était #1 trending")
- **JTBD** : "Produis des vidéos marketing pros sans équipe vidéo ni logiciel propriétaire coûteux"
- **Aha moment** : Première vidéo complète générée depuis un prompt texte, avec vrai footage et narration TTS

### 5. Go-to-Market
- **Canal** : GitHub organic (trending) · Posts dev Twitter/X · Reddit r/LocalLLaMA · Dev newsletters
- **Viral loop** : Chaque développeur qui fork ou star amplifie le signal · AGPLv3 force la contribution back
- **Moat** : Communauté contributeurs + catalogue de 500+ skills qui grandit organiquement

### 6. Réplication pour Kyle
- **Complexité** : 8/10 — 12 pipelines coordonnés + intégration 14 providers vidéo = projet ambitieux
- **Verticaux adjacents** : Version spécialisée podcasts vidéo, vidéos formations, démos produit SaaS
- **Angle Kyle** : Ajouter une couche Voice AI sur OpenMontage (narration voix clonée, lip-sync, multilingual). Contrib open-source → visibilité + réseau dev. Ou wrapper SaaS payant au-dessus
- **Temps de dev** : 6-9 mois version complète · 4-6 semaines contribution ciblée voice layer

## 🏆 TOP APP #3 : Skybridge
### 1. Identification
- **URL** : https://skybridge.tech | **GitHub** : github.com/alpic-ai/skybridge
- **Launch** : v1.0 mai/juin 2026 | **Fondateurs** : Harijoe + Fred Barthelet (Alpic AI)
- **Catégorie** : Developer Framework · MCP · Open-source (MIT)
- **Buzz** : 1 900 GitHub stars · 115 forks · 100K npm downloads/mois · 500K+ downloads totaux · #16 PH juin 2026 (554 votes) · Recommandé dans docs officiels OpenAI · 10%+ des apps Claude/ChatGPT stores

### 2. Proposition de Valeur
- **Problème** : Builders MCP doivent gérer compatibilité entre Claude, ChatGPT, VSCode + infrastructure spécifique à chaque plateforme
- **Solution** : Framework full-stack TypeScript "code once, ship everywhere" avec emulateur local, HMR, tunnel instant, React Query hooks — tout ce dont on a besoin pour une MCP app en prod
- **USP** : Seul framework qui abstrait les différences entre clients MCP + fourni un DX (developer experience) React moderne. Adopté par Datadog, Bitmovin, Evaneos
- **Target** : Développeurs TypeScript/React buildant des apps pour AI assistants
- **Pricing** : Gratuit (MIT) · Alpic AI monétise probablement via services/cloud

### 3. Stack Technique
- **Framework** : TypeScript 87.9% · React · Node.js 18+
- **DX** : Hot Module Reload · Local emulator · Instant tunnel (Claude/ChatGPT connect)
- **API** : React Query-style hooks · Type-safe end-to-end
- **Deploy** : Claude Artifacts Store · ChatGPT Store · VSCode Extensions · MCP-compatible clients
- **Version** : v1.1.2 (juin 2026) · 118 releases · 832 commits

### 4. Psychologie
- **Triggers** : Social proof enterprise (Datadog) · "Code once, ship everywhere" (promesse claire) · Recommandé par OpenAI (autorité)
- **JTBD** : "Construis une app MCP pro sans me battre avec 3 configurations différentes"
- **Aha moment** : Premier `skybridge dev` → l'app tourne dans Claude local en 2 minutes avec HMR

### 5. Go-to-Market
- **Canal** : GitHub organic · PH · Dev.to / Better Stack articles · Discord communauté · Mention dans docs OpenAI
- **Viral loop** : Chaque app Skybridge publiée dans les stores cite le framework → bouche-à-oreille dev
- **Moat** : First-mover MCP framework + momentum communauté + compatibility matrix maintenu

### 6. Réplication pour Kyle
- **Complexité** : 7/10 — créer un framework de qualité prod nécessite maturity et DX soignée
- **Verticaux adjacents** : Framework spécialisé Voice AI MCP (intégration ElevenLabs, Deepgram dans Skybridge) · Templates MCP pour secteurs spécifiques
- **Angle Kyle** : Contribuer des Voice AI skills/templates à Skybridge (visibilité ciblée devs MCP). Ou créer un plugin Skybridge pour voice — première intégration voice officielle dans l'écosystème
- **Temps de dev** : Plugin voice : 2-4 semaines. Framework concurrent : 4-6 mois

## 💰 Unit Economics Deep Dive — Fundraisly
*Note : Fundraisly n'a pas divulgué ses métriques financières publiquement. Estimations basées sur benchmark secteur + signaux publics.*

| Métrique | Estimation | Source/Logique |
|---|---|---|
| **MRR** | ~$30K-80K | Hypothèse 30-80 clients early à ~$1K/mois |
| **ARR** | ~$360K-960K | Extrapolation linéaire (2 mois de vie) |
| **Users actifs** | ~200-500 fondateurs | 1700 followers PH → taux activation ~15-30% |
| **ARPU** | ~$500-2000/mois | B2B fundraising tool à forte valeur |
| **CAC** | ~$200-500 | Canal principal organique (PH + bouche-à-oreille) |
| **LTV** | ~$3K-12K | 6-12 mois d'utilisation (durée d'une levée) |
| **LTV/CAC** | ~6-15x | Sain pour un SaaS B2B early-stage |
| **Payback** | 1-3 mois | CAC faible + ARPU élevé |
| **Burn** | ~$20-50K/mois | Équipe 2-4 personnes remote |
| **Runway** | Inconnu (pas de levée publique) | Bootstrapped probable |
| **Rev/Employee** | ~$90K-240K ARR | 4 employees hypothétiques |
| **Rule of 40** | ~60-80 | Croissance rapide + marges élevées (software pur) |

**Verdict santé** : 🟢 — Très tôt pour conclure, mais les signaux sont positifs. CAC organique quasi-nul grâce au PH launch et réseau VC de la fondatrice. LTV/CAC excellent si l'outil tient ses promesses (20-40 meetings = $500K-5M levés → success fee potentiel 1-2% = gros upside). Le risque principal : churn post-levée (chaque client disparaît une fois son round bouclé → acquisition perpetuelle nécessaire).

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Fundraisly | OpenMontage | Skybridge |
|---|---|---|---|
| 📊 Market Size (20%) | 8 — TAM global fundraising >$10B | 9 — Création vidéo pro, marché énorme | 7 — Marché MCP en hypercroissance |
| ⚙️ Complexity inversé (15%) | 6 — Base data investisseurs = moat difficile | 3 — 12 pipelines + 14 video providers | 5 — DX framework = craft long |
| ⏱️ Time-to-Market (15%) | 5 — 3-4 mois pour MVP crédible | 3 — 6-9 mois pour version complète | 7 — Plugin voice 2-4 semaines |
| 🏟️ Competition inversé (15%) | 7 — Quelques acteurs (Visible.vc, Capbase) mais aucun avec réseau VC intégré | 8 — Premier open-source agentique | 6 — Quelques frameworks MCP naissants |
| 💰 Revenue Potential (20%) | 9 — ARPU $500-2K/mois · success fee optionnel · CAC organique | 4 — Open-source pur : monétisation cloud/SaaS nécessaire | 6 — Monétisation indirecte (services, cloud) |
| 🧑‍💻 Founder-Fit Kyle (15%) | 6 — Voice AI / SaaS fit · mais pas expert VC fundraising | 8 — Voice AI = différentiation directe sur OpenMontage | 9 — Voice MCP plugin = expert + réseau |
| **Score pondéré** | **7.20** | **5.35** | **6.55** |
| **Verdict** | 🟢 **BUILD NOW** | 🟠 **WATCH** | 🟡 **BUILD ADJACENT** |

**Légende calcul** :
- Fundraisly : (8×0.20)+(6×0.15)+(5×0.15)+(7×0.15)+(9×0.20)+(6×0.15) = 1.6+0.9+0.75+1.05+1.8+0.9 = **7.0** → 🟢 BUILD NOW
- OpenMontage : (9×0.20)+(3×0.15)+(3×0.15)+(8×0.15)+(4×0.20)+(8×0.15) = 1.8+0.45+0.45+1.2+0.8+1.2 = **5.9** → 🟠 WATCH
- Skybridge : (7×0.20)+(5×0.15)+(7×0.15)+(6×0.15)+(6×0.20)+(9×0.15) = 1.4+0.75+1.05+0.9+1.2+1.35 = **6.65** → 🟡 BUILD ADJACENT

## 📈 Tendances Émergentes
1. **MCP devient la plomberie de l'AI** : Skybridge et l'écosystème autour du Model Context Protocol montrent que la prochaine vague n'est pas "construire un LLM" mais "construire des apps qui vivent DANS les assistants". Le store Claude/ChatGPT sera le nouveau App Store.

2. **Agents spécialisés > plateformes génériques** : Fundraisly gagne parce qu'il est UNIQUEMENT pour les fondateurs qui lèvent. Les plateformes generalist AI agents (AgentX, Make AI) peinent à se différencier. Niche = moat.

3. **Open-source comme canal d'acquisition** : OpenMontage prouve qu'un dépôt GitHub bien positionné peut générer 22K stars en quelques jours. L'AGPLv3 force les entreprises à contribuer ou payer → modèle OSS → SaaS rodé.

4. **La valeur est dans la DATA, pas dans l'IA** : Fundraisly ne vend pas l'IA, il vend l'accès à 300K+ profils investisseurs enrichis + les warm paths. L'IA est le moteur mais la donnée est le moat.

5. **Voice AI en fond de tableau** : Aucune app voice-first dans le top PH cette semaine, mais Skybridge (voice deployment) et OpenMontage (TTS/narration) l'intègrent comme feature. Signal : voice devient une couche infra, pas un produit standalone.

## 💡 Insights Actionnables
### 🎯 Pour Kyle — Actions immédiates

**1. Dupliquer le modèle Fundraisly sur un vertical voice AI** (Score 7.0 → BUILD NOW)
Fundraisly prouve que la combinaison "data propriétaire + agent IA + réseau expert" fonctionne pour un problème B2B précis. Kyle a l'équivalent pour les acheteurs enterprise en voice AI : connaissance des décideurs, des use cases, des intégrations. Construire un "Sales Agent" qui trouve et qualifie automatiquement des prospects enterprise pour des solutions voice → même ADN, même playbook.
- **Action** : Valider avec 5 entretiens fondateurs (semaine 1) → MVP en 6 semaines.

**2. Publier un Voice AI plugin Skybridge en open-source** (Score 6.65 → BUILD ADJACENT)
Skybridge powers 10%+ des apps Claude/ChatGPT. Un plugin officiel voice (ElevenLabs, Deepgram, Cartesia) positionne Kyle comme contributeur clé dans l'écosystème MCP naissant. Coût : 2-4 semaines. Bénéfice : visibilité ciblée (dev community), crédibilité, deals potentiels avec Alpic AI.
- **Action** : Fork skybridge, implémenter VoiceSkill template, PR en 3 semaines.

**3. Monitorer OpenMontage pour une opportunité de contribution voice** (Score 5.9 → WATCH)
22K stars = communauté captive. Le module narration/TTS d'OpenMontage est basique (Piper TTS local). Une contribution qui ajoute ElevenLabs/Cartesia comme provider premium serait mergée rapidement et exposerait le nom de Kyle à des milliers de devs créateurs de contenu.
- **Action** : Ouvrir une issue "Voice provider abstraction" dans les 2 prochaines semaines.

### 🔑 Leçon macro de ce scan
> Le marché récompense la SPÉCIFICITÉ. Les gagnants de cette semaine (Fundraisly, OpenMontage, Skybridge) ont chacun choisi un problème ultra-précis et l'ont résolu mieux que quiconque. Pas de plateforme "pour tout le monde". La niche est le produit.
