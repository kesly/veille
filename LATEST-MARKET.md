# 🔥 Market Scan — 2026-05-16

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : AgentPeek
- Opportunités immédiates (BUILD NOW) : 1 (AgentPeek)

## 🏆 TOP APP #1 : AgentPeek
### 1. Identification
- **URL** : [agentpeek.app](https://agentpeek.app)
- **Lancement** : Mai 2026
- **Catégorie** : Developer Tools / AI Tooling
- **Buzz** : Top Product Hunt mai 2026, trending sur X (#buildinpublic, #claudecode)
- **Open-source** : Partiel (hooks open source sur [GitHub/AppGram/agentnotch](https://github.com/AppGram/agentnotch))

### 2. Proposition de valeur
- **Problème** : Les devs qui font tourner Claude Code / OpenAI Codex doivent jongler entre terminaux pour voir les sessions actives, valider les permissions et suivre les tokens.
- **Solution** : App macOS native qui s'installe dans le notch du Mac. Toutes les infos AI en un coup d'œil sans quitter l'éditeur.
- **USP** : "Zero context-switch" — local-first, <1 Mo, s'installe en 2 min via hooks Claude/Codex.
- **Cible** : Développeurs Apple Silicon utilisant des agents IA quotidiennement.
- **Pricing** : $9 lifetime (2 jours gratuits, pas de CB). Modèle one-shot, friction quasi-nulle.

### 3. Stack technique
- **Frontend** : SwiftUI (macOS natif)
- **Backend** : Aucun serveur — lecture locale des fichiers de hooks (`~/.claude/settings.json`, `~/.codex/hooks.json`)
- **Infra** : Distribué en direct (pas App Store nécessaire pour v1)
- **APIs** : Aucune API externe — tout local

### 4. Psychologie
- **Triggers** : Urgence ("tes agents tournent sans que tu le saches"), social proof (viral X/HN), autorité (fondateur crédible du monde Apple dev)
- **JTBD** : "Quand je code avec Claude, je veux savoir exactement ce qu'il fait, sans interrompre mon flow."
- **Aha moment** : Voir en temps réel son agent IA penser dans le notch — effet "wow" immédiat.

### 5. Go-to-Market
- **Canaux** : X (#buildinpublic, #claudecode), Product Hunt, HN Show HN, bouche-à-oreille dev
- **Viral loop** : Chaque développeur qui screenshot le notch génère du UGC organique
- **Stratégie launch** : Démo vidéo courte + thread X → Product Hunt le même jour

### 6. Réplication
- **Complexité** : 2/10 — 1 dev Swift, 1-2 semaines max
- **Verticaux adjacents** : Version Windows (PowerToys), version Linux (waybar widget), version "multi-agent" pour équipes
- **Angle Kyle** : Adapter pour voice AI agents (Vapi, ElevenLabs) — widget notch qui monitore les sessions voice en cours, coûts, latences. Niche encore vierge.

## 🏆 TOP APP #2 : Steadwing
### 1. Identification
- **URL** : [steadwing.com](https://www.steadwing.com)
- **Lancement** : Mars 2026 (Show HN : 7 mars 2026)
- **Catégorie** : DevOps / AIOps / Autonomous Engineering
- **Buzz** : HN Show HN, intégrations Datadog + PagerDuty, free tier attractif

### 2. Proposition de valeur
- **Problème** : Les alertes on-call à 3h du matin coûtent cher en burn humain. Diagnostiquer un incident prend 20-60 min en moyenne.
- **Solution** : Agent IA autonome qui corrèle logs, métriques, traces → RCA en <5 min + proposition de fix avec ou sans approbation humaine.
- **USP** : Pas juste de l'alerte intelligente — exécution du correctif. "Your engineer, not your monitor."
- **Cible** : Startups et scale-ups avec infra cloud, 10-200 ingénieurs.
- **Pricing** : Freemium (connexion stack en 5 min, pas de CB) → tiers payants non publiés.

### 3. Stack technique
- **Intégrations** : Datadog, PagerDuty, Slack, GitHub, AWS/GCP
- **Core** : LLM orchestration + RAG sur runbooks d'incidents historiques
- **Infra** : Cloud-hosted SaaS (accès API aux stacks clients)

### 4. Psychologie
- **Triggers** : Peur (incident nocturne, perte de revenus), gain (ingénieurs libérés des gardes), social proof (intégrations tier-1)
- **JTBD** : "Quand une alerte tombe, je veux un diagnostic immédiat sans réveiller mon équipe."
- **Aha moment** : Premier incident résolu automatiquement pendant le sommeil du CTO.

### 5. Go-to-Market
- **Canaux** : HN, Slack communities DevOps, intégrations comme growth vector (Datadog Marketplace)
- **Viral loop** : L'équipe partage les "incidents auto-résolus" → crédibilité + FOMO
- **Stratégie** : Bottom-up (free tier dev), expansion vers l'enterprise

### 6. Réplication
- **Complexité** : 7/10 — intégrations multiples, confiance sécurité critique, 3-6 mois pour v1 robuste
- **Verticaux adjacents** : On-call pour systèmes voice AI (latence, erreurs TTS/STT, coûts API)
- **Angle Kyle** : "Steadwing for Voice AI" — monitorer et auto-diagnostiquer les incidents sur pipelines Vapi/ElevenLabs/Twilio. Niche sous-adressée, expertise directe.

## 🏆 TOP APP #3 : Thewebsite.app
### 1. Identification
- **URL** : [thewebsite.app](https://thewebsite.app)
- **Lancement** : Février-mars 2026
- **Catégorie** : Expérimentation / AI-native business / Build in Public
- **Buzz** : HN Show HN 111 points / 31 comments (6 mars 2026), concept viral sur X
- **Open-source** : Oui — code intégralement public

### 2. Proposition de valeur
- **Problème** : Peut-on déléguer la gestion d'un business réel à un agent IA et atteindre $80K/mois ?
- **Solution** : Le fondateur fixe la stratégie, l'agent IA code, déploie et opère. Transparence totale, tout public.
- **USP** : Pas un produit à vendre — un laboratoire vivant en public. La viralité EST le produit.
- **Cible** : Fondateurs tech curieux, investisseurs IA, communauté Build in Public
- **Pricing** : Gratuit (open source) — monétisation indirecte (audience, consulting, sponsoring)

### 3. Stack technique
- **Stack** : Non précisé, entièrement open source sur GitHub
- **Core** : Orchestration d'agents LLM pour décisions business opérationnelles
- **Infra** : Probablement Vercel + cloud standard

### 4. Psychologie
- **Triggers** : Curiosité (expérience unique), FOMO (suivre l'évolution en live), légitimité (code ouvert = transparence)
- **JTBD** : "Je veux voir si les agents IA peuvent vraiment gérer un business — pas un démo, un vrai."
- **Aha moment** : Voir une décision business prise et exécutée par l'agent en temps réel.

### 5. Go-to-Market
- **Canaux** : HN, X build-in-public, newsletters IA, YouTube explainers
- **Viral loop** : Chaque milestone ($1K → $5K MRR) génère du contenu organique naturel
- **Stratégie** : Audience first → produit/consulting ensuite

### 6. Réplication
- **Complexité** : 4/10 pour le concept (wrapper LLM + site vitrine), 9/10 pour l'exécution à l'échelle
- **Verticaux adjacents** : "AI-native agency" pour voice AI — un agent qui gère les campagnes clients
- **Angle Kyle** : Documentaire public "Voice AI business run by agents" → audience + crédibilité + leads entrants. Différenciation forte sur le marché francophone.

## 💰 Unit Economics Deep Dive — AgentPeek
**Note** : Données estimées — AgentPeek est un produit solo bootstrappé, aucune donnée publique officielle.

| Métrique | Estimation | Base |
|---|---|---|
| **Pricing** | $9 one-time | Confirmé |
| **Users (est.)** | 2 000 – 8 000 | PH + X traction |
| **ARR équivalent** | $18K – $72K (one-shot) | Conversion ~30-40% |
| **ARPU** | $9 (lifetime) | Confirmé |
| **CAC** | ~$0 | Distribution organique (X, HN, PH) |
| **LTV** | $9 (one-shot) | Pas d'abonnement |
| **LTV/CAC** | ∞ (CAC≈0) | Distribution gratuite |
| **Payback** | Immédiat | $9 direct |
| **Burn** | ~$0 / mois | 1 dev solo, infra nulle |
| **Runway** | Infini | Coûts quasi-nuls |
| **Rev/Employee** | $18K-$72K (1 personne) | Solo |
| **Rule of 40** | N/A (one-shot, pas SaaS récurrent) | — |

**Verdict santé** : 🟢

Modèle one-shot atypique : pas de récurrence, mais CAC=0 + marges=100% + zéro infrastructure.
Risque principal : plateau rapide si pas de v2 ou passage à l'abonnement.
Signal fort que le marché existe — à convertir en SaaS $X/mois pour LTV >$9.

*Sources : [Product Hunt AgentPeek](https://www.producthunt.com/products/agentpeek), [agentpeek.app](https://agentpeek.app), [GitHub AppGram](https://github.com/AppGram/agentnotch)*

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | AgentPeek | Steadwing | Thewebsite.app |
|---|---|---|---|
| 📊 Market Size (20%) | 6 — marché dev tools IA en croissance explosive | 8 — AIOps/DevOps $50B+ | 5 — niche expérimentale |
| ⚙️ Complexité inversée (15%) | 9 — 1-2 semaines Swift | 3 — 6+ mois, intégrations lourdes | 6 — concept simple, exécution dure |
| ⏱️ Time-to-Market (15%) | 9 — <1 mois | 3 — >6 mois | 7 — site + agent en 2-3 semaines |
| 🏟️ Compétition inversée (15%) | 7 — Agent Hub concurrent, mais niche encore jeune | 4 — Devin, incident.io, PagerDuty AI | 8 — concept unique, peu de concurrents directs |
| 💰 Revenue Potential (20%) | 5 — $9 one-shot, plateau rapide | 8 — ARR récurrent enterprise possible | 3 — monétisation indirecte lente |
| 🧑‍💻 Founder-Fit Kyle (15%) | 7 — dev tool, mais pas voice AI direct | 8 — voice AI ops = expertise directe | 7 — build in public + audience = atout |

| App | Score pondéré | Verdict |
|---|---|---|
| **AgentPeek** | **(6×0.20)+(9×0.15)+(9×0.15)+(7×0.15)+(5×0.20)+(7×0.15) = 7.15** | 🟡 BUILD ADJACENT |
| **Steadwing** | **(8×0.20)+(3×0.15)+(3×0.15)+(4×0.15)+(8×0.20)+(8×0.15) = 5.90** | 🟠 WATCH |
| **Thewebsite.app** | **(5×0.20)+(6×0.15)+(7×0.15)+(8×0.15)+(3×0.20)+(7×0.15) = 5.75** | 🟠 WATCH |

**Recommandation** : AgentPeek → construire la version "Voice AI notch monitor" pour Vapi/ElevenLabs. Score BUILD NOW potentiel si on cible le segment voice AI (Kyle = expert = Founder-Fit 10).

## 📈 Tendances Émergentes
1. **"Notch economy"** : Le notch Mac devient un espace UI premium pour les power users. AgentPeek, Notchmeister, et d'autres apps exploitent cette zone vierge. Tendance 6-12 mois.

2. **Agents IA en production ≠ monitoring standard** : Les outils classiques (Datadog, Sentry) ne sont pas faits pour observer des agents LLM. Nouveau segment : observability native pour AI agents. Marché naissant, peu de solutions robustes.

3. **Modèle one-shot lifetime en renaissance** : Après des années de SaaS pur, le $9-$49 lifetime revient fort pour les dev tools (AgentPeek, RayCast plugins, etc.). Acquisition ultra-rapide, CAC=0, mais LTV limitée.

4. **DevOps → AIOps → AgentOps** : La chaîne d'évolution est claire. Steadwing est positionné AIOps. La prochaine vague = AgentOps (monitoring d'agents autonomes multi-étapes). Encore très peu d'acteurs.

5. **Build in Public comme canal d'acquisition** : Thewebsite.app illustre une tendance : le projet EST le marketing. 2026 voit l'explosion des "founder-as-media" où la transparence radicale remplace les ads.

## 💡 Insights Actionnables
### 🎯 Pour Kyle (Voice AI + SaaS)

**Insight #1 — BUILD : "AgentPeek for Voice AI"**
Un widget macOS (ou menu bar) qui monitore en temps réel les sessions Vapi, ElevenLabs, Twilio Voice AI : coût/appel, latence TTS/STT, taux d'erreur, tokens. Pricing $12 lifetime ou $5/mois. Stack : SwiftUI + webhooks Vapi. Délai : 2-3 semaines. Founder-Fit = 10/10.

**Insight #2 — WATCH : "Steadwing pour Voice AI ops"**
Les équipes qui déploient des agents vocaux n'ont aucun outil de on-call dédié. Un Steadwing vertical = "quand ton agent vocal tombe à 3h, je te dis pourquoi et je le fix". Différenciation forte, mais complexité élevée. À surveiller sur 3-6 mois.

**Insight #3 — AUDIENCE : Documenter en public**
Thewebsite.app montre qu'un projet expérimental bien raconté génère plus de leads que de la pub. Kyle peut documenter la construction de son prochain produit voice AI en public (X, LinkedIn, YouTube FR) → audience francophone encore peu exploitée sur ce segment.

**Insight #4 — MONETISATION : Éviter le one-shot pur**
Le modèle $9 one-shot d'AgentPeek est bon pour l'acquisition, mais plafonne vite. Pour un produit équivalent, Kyle devrait cibler $9 trial → $8/mois après 30 jours, pour garder une LTV >$50.

**Insight #5 — SIGNAL FAIBLE : AgentOps comme catégorie**
Aucun acteur dominant sur le monitoring d'agents IA (voice ou texte) en 2026. Fenêtre de 6-12 mois avant consolidation. Opportunité de définir la catégorie et d'en devenir la référence francophone.
