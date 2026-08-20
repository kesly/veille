# 🔥 Market Scan — 2026-08-20

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : ScrollToll (screen-time gym), Murmell (AI cloud canvas), CoachAI (form tracking)
- Opportunités immédiates (BUILD NOW) : 1 (ScrollToll-clone pour verticaux spécifiques)

## 🏆 TOP APP #1 : ScrollToll
### 1. Identification
- **URL** : [getscrolltoll.app](https://getscrolltoll.app) | [Product Hunt](https://www.producthunt.com/products/scrolltoll-2)
- **Launch** : Août 2026 (≈2 semaines)
- **Fondateur** : Chandan (solo dev, Inde)
- **Catégorie** : Productivité / Screen-time management
- **Métriques buzz** : 4.8★ / 2 000+ reviews iOS+Android, trending PH semaine 33/2026

### 2. Proposition de Valeur
- **Problème** : Addiction au scroll (Reels, Shorts, TikTok) impossible à briser avec de simples timers
- **Solution** : Compte chaque vidéo courte regardée → bloque le feed au-delà du quota → pour débloquer, tu dois faire des répétitions physiques (pompes, squats, etc.) validées en temps réel par l'IA caméra
- **USP** : Le sport comme "mot de passe" — on-device AI pose detection, aucun upload
- **Cible** : 18-35 ans, utilisateurs conscients de leur addiction, parents pour ados
- **Pricing** : Freemium + IAP (estimé $4.99-$9.99/mo pour quota illimité)

### 3. Stack Technique
- **Mobile** : Flutter (iOS + Android cross-platform)
- **AI** : On-device pose estimation (MediaPipe ou ML Kit)
- **Backend** : Firebase (auth, sync quotas)
- **Distribution** : App Store + Google Play

### 4. Psychologie
- **Triggers** : Aversion à la perte (bloquer = punir), social proof (2k reviews), gamification (streaks)
- **JTBD** : "Aide-moi à reprendre le contrôle sans willpower"
- **Aha moment** : Premier lockout + premier squat pour débloquer → effet "wow ça marche vraiment"

### 5. Go-to-Market
- **Canaux** : Viral organique TikTok/Reddit (ironie de bloquer TikTok avec une app), Product Hunt
- **Viral loop** : Les gens partagent leurs stats de sport involontaire → mème naturel
- **Stratégie** : Solo dev, zero paid acquisition, pure bouche-à-oreille

### 6. Réplication
- **Complexité** : 4/10 (Flutter + MediaPipe bien documentés)
- **Verticaux adjacents** : version pour adultes/travail (bloquer LinkedIn quand trop scrollé), version enfants avec contrôle parental, version B2B pour entreprises
- **Angle Kyle** : Intégrer voice AI comme coach vocal pendant l'exercice → "Allez, encore 3 squats !"
- **Temps de dev** : 4-6 semaines MVP

## 🏆 TOP APP #2 : Murmell
### 1. Identification
- **URL** : [murmell.com](https://murmell.com) | [Product Hunt](https://www.producthunt.com/products/murmell)
- **Launch** : Août 2026 (≈2 semaines)
- **Fondateurs** : Non publics (basé sur PH listing)
- **Catégorie** : Developer tools / AI collaboration
- **Métriques buzz** : Featured PH semaine 33/2026, mention sur Teahose, UIComet

### 2. Proposition de Valeur
- **Problème** : Les coding agents (Claude Code, Codex) tournent en silos — impossible de voir plusieurs agents en même temps ni de collaborer avec eux
- **Solution** : Canvas cloud partagé dans le browser où agents AI + humains travaillent sur le même repo, cloud machine, en temps réel
- **USP** : Agents "clament" des fichiers avant d'écrire (pas de conflits), iOS/Android simulators dans le canvas à venir
- **Cible** : Petites équipes dev + solo founders heavy AI users (Claude Code, Codex, Kimi)
- **Pricing** : Solo $39/mo · Pro $69/mo · Builder $149/mo + 2 semaines gratuites + $60 crédits Claude Code offerts

### 3. Stack Technique
- **Frontend** : Canvas WebGL/Canvas2D custom (browser-first)
- **Backend** : Cloud machines (probablement GCP/AWS) + WebSockets pour le real-time
- **Agents supportés** : Claude Code, Codex, Kimi, OpenCode (OpenClaw, Hermes en route)
- **Git integration** : Tout se sync via git, pas de lock-in

### 4. Psychologie
- **Triggers** : FOMO (les autres équipes ont des "super-pouvoirs" AI), autorité (intégration avec les LLMs leaders)
- **JTBD** : "Aide-moi à superviser plusieurs agents AI sans perdre le contrôle"
- **Aha moment** : Voir 3 agents travailler en parallèle sur le même repo sans conflits

### 5. Go-to-Market
- **Canaux** : Product Hunt, Twitter dev community, HN, bouche-à-oreille développeurs
- **Viral loop** : Partage de screenshots du canvas multi-agents → aspiration sociale
- **Offre d'entrée** : 2 semaines gratuites + $60 Claude Code crédits = très faible friction

### 6. Réplication
- **Complexité** : 8/10 (synchronisation multi-agents temps réel = ingénierie complexe)
- **Verticaux adjacents** : Version pour data scientists (notebooks partagés avec agents), pour designers (Figma-like avec AI agents)
- **Angle Kyle** : Trop complexe à répliquer, mais partenariat/intégration voice AI possible (agent vocal qui pilote le canvas)
- **Temps de dev** : 6-12 mois pour MVP robuste

## 🏆 TOP APP #3 : CoachAI
### 1. Identification
- **URL** : [coachai.tech](https://coachai.tech) | [Product Hunt](https://www.producthunt.com/products/coachai-fitness-coach)
- **Launch** : Août 2026 (≈2 semaines)
- **Fondateurs** : Équipe Dubaï (non publics)
- **Catégorie** : Health & Fitness / AI Coach
- **Métriques buzz** : Featured PH août 2026, App Store présent

### 2. Proposition de Valeur
- **Problème** : Les gens s'entraînent régulièrement mais se blessent ou stagnent faute de feedback sur leur forme
- **Solution** : Caméra iPhone = coach en temps réel — compte les répétitions, corrige la posture, adapte le programme selon ce que le corps vient de faire
- **USP** : On-device (rien uploadé), correction en temps réel, adaptation dynamique du prochain set
- **Cible** : 20-45 ans, pratiquants autonomes (home gym, salle sans coach perso)
- **Pricing** : Freemium + abonnement (estimé $9.99-$14.99/mo)

### 3. Stack Technique
- **Mobile** : Swift/iOS natif (performance maximale pour pose detection)
- **AI** : Vision framework Apple + modèle custom de pose estimation
- **Backend** : Minimal (on-device first), sync iCloud probable
- **APIs** : Apple HealthKit (intégration native)

### 4. Psychologie
- **Triggers** : Autorité (IA = expertise de coach), progression (stats de reps/form), peur de la blessure
- **JTBD** : "Entraîne-moi comme un coach perso, sans en payer un"
- **Aha moment** : Première correction en temps réel ("Ta hanche descend trop à gauche") → sentiment de coaching pro

### 5. Go-to-Market
- **Canaux** : Product Hunt, communautés fitness Reddit (r/fitness, r/bodyweightfitness), influenceurs fitness TikTok
- **Viral loop** : Partage de "mon coach AI m'a corrigé mes squats" → démonstration visuelle convaincante
- **Différenciation** : Pas de connexion internet requise → privacy selling point fort

### 6. Réplication
- **Complexité** : 6/10 (iOS natif + pose detection = expertise requise, mais frameworks bien documentés)
- **Verticaux adjacents** : Yoga (forme + respiration), physiothérapie rééducation, sport scolaire
- **Angle Kyle** : Version voice-first — coaching 100% vocal pendant l'exercice, les mains libres, yeux sur la forme. Son expertise voice AI est un avantage direct.
- **Temps de dev** : 3-5 mois MVP iOS

## 💰 Unit Economics Deep Dive — ScrollToll
### ScrollToll — Estimations (sources : App Store reviews, Product Hunt, patterns micro-SaaS similaires)

| Métrique | Estimation | Hypothèse |
|---|---|---|
| Users actifs | ~5 000–10 000 | 2k reviews = ~10-20% reviewers |
| Payants (conv. 5%) | ~300–500 | Freemium typique |
| ARPU mensuel | $7/mo | Milieu de gamme IAP |
| ARR estimé | ~$25K–$42K | 350 users × $7 × 12 |
| CAC | ~$0 | Acquisition 100% organique |
| LTV (12 mo, 70% rétention) | ~$84 | $7 × 12 mo |
| LTV/CAC | ∞ | CAC ≈ $0 |
| Payback Period | Jour 1 | Pas de paid acquisition |
| Burn | ~$200/mo | Firebase + App Store fees |
| Runway | Illimité | Solo dev, revenu > coûts |
| Rev/Employee | $25-42K/an | Solo fondateur |
| Rule of 40 | ~90+ | Croissance forte + marges >95% |

**⚠️ Limites** : Données estimées, pas de sources officielles disponibles. Les vraies métriques pourraient différer.

**Verdict santé** : 🟢 Excellent pour un solo-dev en phase early. CAC nul = unité économique parfaite. Risque : dépendance à App Store (30% cut) et viralité difficile à soutenir.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | ScrollToll | Murmell | CoachAI |
|---|---|---|---|
| 📊 Market Size (20%) | 7 — marché global $B | 8 — dev tools $10B+ | 7 — fitness $B |
| ⚙️ Complexité inversée (15%) | 8 — Flutter+MediaPipe | 3 — temps réel complexe | 5 — iOS natif moyen |
| ⏱️ Time-to-Market (15%) | 8 — 4-6 semaines | 3 — 6-12 mois | 5 — 3-5 mois |
| 🏟️ Compétition inversée (15%) | 7 — niche "sport-gate" | 6 — nouveaux entrants | 5 — marché fitness saturé |
| 💰 Revenue Potential (20%) | 6 — IAP + freemium | 8 — $39-149/mo B2B | 6 — B2C fitness |
| 🧑‍💻 Founder-Fit Kyle (15%) | 7 — voice AI comme diff. | 4 — pas son cœur | **9** — voice coaching direct |

**Scores pondérés :**

| App | Score | Verdict |
|---|---|---|
| **ScrollToll** | (7×0.20)+(8×0.15)+(8×0.15)+(7×0.15)+(6×0.20)+(7×0.15) = **7.10** | 🟡 BUILD ADJACENT |
| **Murmell** | (8×0.20)+(3×0.15)+(3×0.15)+(6×0.15)+(8×0.20)+(4×0.15) = **5.75** | 🟠 WATCH |
| **CoachAI** | (7×0.20)+(5×0.15)+(5×0.15)+(5×0.15)+(6×0.20)+(9×0.15) = **6.35** | 🟡 BUILD ADJACENT |

**Recommandation** : ScrollToll + angle voice AI (score potentiel →🟢) ou CoachAI voice-first (expertise directe Kyle)

## 📈 Tendances Émergentes
### 1. 🤖 AI On-Device comme standard (pas exception)
Les apps gagnantes d'août 2026 (ScrollToll, CoachAI) traitent TOUT localement. La privacy devient un argument marketing central, pas une contrainte. MediaPipe, Vision Framework, Core ML = commodités accessibles aux solos.

### 2. 💪 "Friction productive" — le retour du comportemental
ScrollToll inverse le modèle : au lieu de réduire la friction pour l'engagement, elle AJOUTE de la friction (sport obligatoire). Trend contre-courant : apps qui te veulent du bien en te résistant.

### 3. 🕹️ Multi-agents AI = nouveau paradigme dev
Murmell préfigure un marché où superviser des agents AI devient un métier à part. Le canvas partagé humain+agent est probablement le futur de tout IDE. Acteurs à surveiller : Claude Code + v0 + Lovable convergent vers ce modèle.

### 4. 📱 Solo dev → produits $1K-$50K MRR en 2026
L'écart coût/valeur s'est effondré. Un solo dev avec Claude + Flutter livre en 4 semaines ce qui prenait 6 mois en 2023. Micro-SaaS mobile = sweet spot 2026 : App Store discovery, viralité organique, marges >90%.

### 5. 🎙️ Voice AI cherche son killer use case consumer
Le voice AI est mature (ElevenLabs, Cartesia, etc.) mais les apps grand public sont rares. Fitness vocal, coaching mental vocal, language learning voice — les verticaux consumer voice AI sont encore largement libres.

## 💡 Insights Actionnables pour Kyle
### 🎯 Pour Kyle (voice AI + SaaS)

**Insight #1 — CoachAI Voice-First est ton meilleur angle**
CoachAI fait du coaching VISUEL. Personne ne fait encore de coaching VOCAL pendant l'exercice (mains libres, yeux sur la forme). Ton expertise ElevenLabs/Cartesia + Flutter = avantage compétitif direct. L'app parle pendant que tu fais tes reps. CAC potentiellement nul (même canal viral que CoachAI).

**Insight #2 — ScrollToll + Voice AI = différenciation immédiate**
Clone ScrollToll et ajoute un coach vocal qui parle pendant les exercices de déverrouillage. "Allez, 3 pompes, encore 2, bien !" → personne ne fait ça. Voice AI = la seule différenciation qui compte ici. Time-to-market : 5-7 semaines.

**Insight #3 — Le "sport-gate" est un mécanisme réplicable**
Le principe de ScrollToll (exercice physique comme accès) s'applique à d'autres verticaux :
- Email addiction → pompes pour lire les newsletters
- LinkedIn scroll → squats avant de voir le feed
- Jeux vidéo → étirements avant de lancer
Chaque vertical = app séparée, même code base.

**Insight #4 — Multi-agent canvas = SaaS B2B en 2027**
Ne pas construire Murmell. Mais surveiller : dans 6-12 mois, le marché sera établi. Opportunité d'intégrer un "voice agent controller" — parler pour diriger ses agents AI dans un canvas Murmell-like.

**Action immédiate recommandée** : Valider l'angle "voice fitness coach" en 48h. Créer un waitlist + vidéo démo quick (Loom). Cibler r/bodyweightfitness + TikTok fitness. Budget : $0.
