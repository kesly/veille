# 🔥 Market Scan — 2026-07-04

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : Glaze by Raycast
- Opportunités immédiates (BUILD NOW) : 1 (Tabstack vertical)

## 🏆 TOP APP #1 : Acti
### 1. Identification
- **URL** : acti.app | **Lancé** : Juillet 2026 | **Catégorie** : Mobile AI / Keyboard AI Agent
- **Métriques buzz** : #1 Product Hunt juillet 2026 (552 231 votes) — record du mois
- **Fondateurs** : Non divulgués publiquement | **Statut** : Gratuit (iOS + Android)

### 2. Proposition de valeur
- **Problème** : Chaque app mobile est un silo — copier/coller entre apps est lent et cassant
- **Solution** : Clavier IA agentique qui agit directement depuis le champ de saisie, sans quitter l'app
- **USP** : "Hold spacebar → intent → result/action" — zéro friction, universel sur toutes apps
- **Target** : Power users mobile, professionnels nomades, early adopters IA
- **Pricing** : Gratuit (monétisation future non annoncée — probablement freemium)

### 3. Stack technique (estimé)
- **Frontend** : SDK clavier natif iOS (Custom Keyboard Extension) + Android IME
- **Backend** : API agents propriétaire + intégrations OAuth (Google Calendar, Notion, LinkedIn)
- **Infra** : Cloud (AWS/GCP), streaming LLM responses
- **APIs** : Connecteurs custom par skill (Notion, Google, LinkedIn, etc.)

### 4. Psychologie & Growth
- **Triggers** : Curiosité ("hold spacebar"), effet wow immédiat, social proof (#1 PH)
- **JTBD** : "Je veux exécuter des tâches complexes sans quitter ma conversation WhatsApp"
- **Aha moment** : Premier "hold spacebar" qui déclenche une action réelle en 1 seconde
- **Viral loop** : Partage de Skill Keys entre collègues → adoption organique en équipe

### 5. Go-to-Market
- **Canal principal** : Product Hunt (launch organique massif) + Twitter/X #buildinpublic
- **Stratégie** : Free-first pour maximiser adoption, marketplace de skills pour rétention
- **Distribution** : App Store (iOS) + Play Store — canal de découverte naturel

### 6. Réplication & Angle Kyle
- **Complexité** : 7/10 (SDK clavier natif = contrainte forte iOS/Android)
- **Verticaux adjacents** : Clavier IA médical, clavier IA CRM, clavier IA support client
- **Angle Kyle (voice AI)** : Version voice-first — "hold mic button → intent vocal → action" sur mobile
- **Temps de dev estimé** : 3-4 mois (clavier natif est complexe), mais le concept vocal = 6-8 semaines

## 🏆 TOP APP #2 : Glaze by Raycast
### 1. Identification
- **URL** : glaze.app | **Lancé** : Beta mars 2026, public juillet 2026 | **Catégorie** : No-Code AI App Builder (Mac)
- **Métriques buzz** : #1 PH 3 juillet 2026 | Adopté par équipes Cursor, Linear, Vercel
- **Fondateurs** : Équipe Raycast (Thomas Paul Mann, CEO) | **Statut** : Freemium

### 2. Proposition de valeur
- **Problème** : Les équipes paient des dizaines d'outils SaaS pour des besoins internes ultra-spécifiques
- **Solution** : Décrire en langage naturel → Glaze génère une vraie app Mac native, offline, avec accès filesystem
- **USP** : Apps vraiment natives (pas du web wrapé) — menu bar, raccourcis clavier, background tasks
- **Target** : Teams tech (Cursor, Linear, Vercel comme early adopters) + solopreneurs Mac
- **Pricing** : Gratuit pour démarrer, plan payant pour usage avancé (prix non publié)

### 3. Stack technique
- **Frontend** : Swift/SwiftUI (apps générées vraiment natives macOS)
- **Backend** : LLM propriétaire + Raycast infra existante
- **Distribution** : Glaze Store public + Team Store privé (viral B2B)
- **APIs** : Accès local filesystem, keyboard shortcuts, menu bar, background processes

### 4. Psychologie & Growth
- **Triggers** : Social proof fort (Cursor/Vercel l'utilisent), autorité Raycast (100k+ users base)
- **JTBD** : "Je veux un outil interne sur-mesure sans embaucher un dev"
- **Aha moment** : Voir son app apparaître dans le Dock en 60 secondes après une phrase
- **Viral loop** : Partage via Glaze Store → collègues installent → deviennent users Raycast

### 5. Go-to-Market
- **Canal principal** : Base Raycast existante (300k+ users) → adoption immédiate sans CAC
- **Stratégie** : Beta fermée (FOMO) → ouverture publique → intégration dans launcher Raycast
- **Distribution** : Raycast devient distribution channel unique — pas de SEO/ads nécessaire

### 6. Réplication & Angle Kyle
- **Complexité** : 8/10 (Swift natif + LLM codegen fiable = très dur à répliquer seul)
- **Verticaux adjacents** : Générateur d'apps Windows (PowerShell/WinUI), générateur Linux
- **Angle Kyle (voice AI)** : "Glaze by voice" — décrire oralement → app générée. Kyle = expert parfait
- **Temps de dev estimé** : 6-9 mois solo (base Raycast = avantage injuste non reproductible)

## 🏆 TOP APP #3 : Tabstack by Mozilla
### 1. Identification
- **URL** : tabstack.ai | **Lancé** : Juillet 2026 (PH) | **Catégorie** : Browser Automation API / AI Infrastructure
- **Métriques buzz** : #3 PH juillet 2026 (381k votes) | Backing Mozilla (crédibilité massive)
- **Fondateurs** : Équipe Mozilla | **Statut** : Payant (Starter $49/mo, Growth $149/mo)

### 2. Proposition de valeur
- **Problème** : Les AI agents ont besoin de données web live mais le scraping est illégal/fragile/cher
- **Solution** : API unique → extraction structurée, markdown, recherche multi-sources, automatisation browser
- **USP** : -60 à -80% tokens vs screenshot-based agents (accessibility tree) + privacy by design (Mozilla)
- **Target** : Développeurs AI, équipes agents, startups SaaS qui intègrent du web data
- **Pricing** : Starter $49/mo | Growth $149/mo | Pay-as-you-go | 10k crédits gratuits à l'essai

### 3. Stack technique
- **Frontend** : API REST + SDK
- **Backend** : Firefox engine (Mozilla) + infrastructure browser managée
- **Infra** : Traitement éphémère (pas de stockage), robots.txt compliance natif
- **APIs** : JSON extraction, Markdown conversion, multi-source research, browser automation

### 4. Psychologie & Growth
- **Triggers** : Autorité Mozilla (trust massif), économies concrètes (-60% tokens = $$ économisés)
- **JTBD** : "Je veux que mon agent AI accède au web live sans me soucier de la légalité ou des limites de tokens"
- **Aha moment** : Premier appel API qui retourne du JSON propre depuis n'importe quelle page en <2s
- **Viral loop** : Intégration dans des frameworks AI (LangChain, CrewAI) → adoption virale développeurs

### 5. Go-to-Market
- **Canal principal** : Communauté dev (HN, Reddit r/MachineLearning) + Mozilla brand
- **Stratégie** : Freemium généreux (10k crédits) → conversion sur volume, usage B2B
- **Distribution** : API marketplace (RapidAPI) + docs référencées dans frameworks AI open source

### 6. Réplication & Angle Kyle
- **Complexité** : 6/10 (wrapper autour d'APIs existantes + brave/puppeteer possible en vertical niche)
- **Verticaux adjacents** : Tabstack vocal (voice queries → web data → réponse audio), niches sectorielles
- **Angle Kyle (voice AI)** : "VoiceStack" — API qui reçoit une query vocale, scrape, résume en audio
- **Temps de dev estimé** : 4-6 semaines pour un MVP vertical (ex : veille concurrentielle audio)

## 💰 Unit Economics Deep Dive — Acti
> ⚠️ **Note** : Acti est actuellement gratuit — aucun revenu public déclaré. Estimations basées sur benchmarks sectoriels et métriques PH observées.

| Métrique | Valeur estimée | Source / Hypothèse |
|---|---|---|
| **Utilisateurs actifs** | ~150 000 (J+30) | Ratio historique PH top #1 → installs |
| **ARR actuel** | $0 (freemium pur) | App Store listing = free, 0 IAP déclaré |
| **ARR potentiel (12 mois)** | ~$1.5M–$3M | Si 2-3% conversion vers $9.99/mo pro |
| **ARPU cible** | $9.99/mois (Pro) | Benchmark clavier IA mobile (Gboard AI, etc.) |
| **CAC** | ~$0 (organique PH) | Launch 100% organique, 0 paid ads annoncé |
| **LTV estimée** | ~$60–$90 | Rétention 6-9 mois (clavier = haute sticky) |
| **LTV/CAC** | ∞ (CAC≈0) → réaliste 30–50x | Excellent si rétention tient |
| **Payback period** | < 1 mois | CAC quasi nul |
| **Burn estimé** | ~$50–80K/mois | Équipe 4-6 personnes + infra LLM |
| **Runway** | Inconnu (seed probable) | Non divulgué |
| **Rev/Employee** | N/A (pré-revenu) | — |
| **Rule of 40** | Non applicable (pré-revenu) | À réévaluer post-monétisation |

### Verdict santé 🟡
**Jaune** : Traction utilisateurs exceptionnelle (#1 PH all-time juillet) mais modèle monétisation encore absent. Le risque principal = délai monétisation. La stickiness du clavier (haute) et le CAC nul sont des atouts majeurs. À surveiller sur Q3 2026 pour annonce pricing.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Acti | Glaze/Raycast | Tabstack |
|---|---|---|---|
| 📊 Market Size (20%) | 8 — marché mobile AI global | 7 — Mac only, niche power users | 9 — toute startup AI a besoin de web data |
| ⚙️ Complexité inversée (15%) | 3 — SDK clavier natif très dur | 2 — Swift + LLM codegen fiable = très dur | 7 — API wrapper réalisable solo |
| ⏱️ Time-to-Market (15%) | 2 — 3-4 mois minimum | 2 — 6-9 mois | 7 — MVP 4-6 semaines |
| 🏟️ Competition inversée (15%) | 6 — peu de vrais concurrents | 5 — Cursor Tab, GitHub Copilot proxies | 5 — Apify, ScrapingBee, Browserless |
| 💰 Revenue Potential (20%) | 6 — gratuit pour l'instant, potentiel B2C | 7 — Raycast déjà rentable, modèle prouvé | 8 — $49-$149/mo, B2B récurrent |
| 🧑‍💻 Founder-Fit Kyle (15%) | 7 — voice AI → killer extension naturelle | 4 — Swift + MacOS hors expertise | 8 — API voice + web data = combo parfait Kyle |

| App | **Score pondéré** | **Verdict** |
|---|---|---|
| **Acti** | **(8×0.20)+(3×0.15)+(2×0.15)+(6×0.15)+(6×0.20)+(7×0.15) = 5.65** | 🟠 WATCH |
| **Glaze by Raycast** | **(7×0.20)+(2×0.15)+(2×0.15)+(5×0.15)+(7×0.20)+(4×0.15) = 4.90** | 🔴 SKIP (pour Kyle solo) |
| **Tabstack vertical** | **(9×0.20)+(7×0.15)+(7×0.15)+(5×0.15)+(8×0.20)+(8×0.15) = 7.55** | 🟢 BUILD NOW |

> 🟢 **Tabstack vertical (VoiceStack)** = score 7.55 → BUILD NOW pour Kyle

## 📈 Tendances Émergentes
1. **AI natif sur mobile** : Acti confirme que l'interface clavier mobile devient le nouveau battleground des agents IA. Les app stores deviennent secondaires — l'input layer est le vrai OS.

2. **No-code AI app builders** : Glaze, Cursor Notepads, Replit Deployments — génération d'apps par langage naturel passe du prototype à la production. Fenêtre de différenciation = 12-18 mois avant commoditisation.

3. **Infrastructure web pour agents AI** : Tabstack, Firecrawl, Spider.cloud — la bataille de l'accès au web live est le nouveau chokepoint de l'écosystème AI agent. Mozilla + Cloudflare + Anthropic se positionnent tous.

4. **Local-first AI** : GitHub trending = Ollama (165k⭐), llama.cpp, Open Interpreter. La souveraineté des données devient argument commercial premium, pas juste technique.

5. **Micro-SaaS AI vertical** : Solo founders atteignent $10k-$200k MRR grâce aux LLMs comme co-fondateur technique. Time-to-market réduit de 70% vs 2023. Niche + AI = nouvelle formule gagnante.

## 💡 Insights Actionnables pour Kyle
### 🎯 Action #1 — BUILD NOW : VoiceStack (dérivé Tabstack)
**Quoi** : API REST qui reçoit une requête vocale (audio ou texte) → scrape web live → retourne une réponse audio synthétisée.
**Pourquoi Kyle** : Expert voice AI + stack LLM = avantage injuste. Tabstack prouve la demande ($49-$149/mo marché validé), Mozilla n'ira pas sur le vertical vocal.
**Next step concret** : Prototype en 2 weekends — Whisper (STT) + Firecrawl API + TTS (ElevenLabs) + FastAPI. Lancer sur PH semaine 3.

### 🎯 Action #2 — WATCH : Clavier vocal agentique (dérivé Acti)
**Quoi** : Extension Acti-like mais avec "hold mic button → intent vocal → action" au lieu de texte.
**Pourquoi Kyle** : Acti valide la demande massive (#1 PH 552k votes). La version vocale n'existe pas encore.
**Blocage** : iOS Custom Keyboard API ne supporte pas le micro → il faut une app companion. Complexité 7/10. Watch Q3 2026.

### 🎯 Action #3 — Positionnement Kyle sur Product Hunt
Acti et Glaze montrent qu'un lancement PH bien préparé génère des centaines de milliers de votes. Investir dans la communauté PH (commenter, supporter) 4 semaines avant le prochain launch de Kyle.

### 📌 Signal faible à surveiller
**OpenClaw** (GitHub, 210k⭐ en 6 mois) → framework agent open-source qui peut devenir la base d'un produit SaaS. À étudier pour réduire le temps de dev VoiceStack.
