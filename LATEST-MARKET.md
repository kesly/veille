# 🔥 Market Scan — 2026-09-26

## 📊 Résumé Exécutif
- Apps analysées : 6 (filtrage → 3 retenues)
- Top potentiel : MosMos (Voice AI)
- Opportunités immédiates (BUILD NOW) : 2 (MosMos, Voiskey)

## 🏆 TOP APP #1 : MosMos
### 1. Identification
- **Nom** : MosMos | **URL** : [mosmos.io](https://mosmos.io/) | **Launch** : Sept 2026
- **Catégorie** : Voice AI / Productivity (macOS-native)
- **Buzz** : #1 Product Hunt du jour (391 upvotes), 4.7★ (78 reviews) · Windows + iOS annoncés
- **Sources** : [Product Hunt](https://www.producthunt.com/products/mosmos)

### 2. Proposition de Valeur
- **Problème** : La dictée classique est basique (pas de contexte, pas de réunions, pas de style)
- **Solution** : Espace de travail vocal natif macOS — `Fn` partout → texte poli selon l'app et le contexte
- **USP** : Multi-speakers meeting notes + personal glossary + web search intégré en vocal
- **Target** : Knowledge workers, executives, développeurs → power users Mac
- **Pricing** : Freemium (téléchargement gratuit), tier Pro estimé ~$12-20/mois

### 3. Stack Technique (estimé)
- **Frontend** : macOS native SwiftUI
- **Backend** : Node.js/Python + Whisper (OpenAI) ou modèle proprio
- **APIs** : Whisper, GPT-4o (polish), moteur web search
- **Infra** : Audio local par défaut → edge-first privacy

### 4. Psychologie & JTBD
- **Triggers** : Vitesse (5x vs typing), FOMO réunions, douleur transcription
- **JTBD** : "Quand je suis en réunion, je veux capturer sans perdre le fil"
- **Aha moment** : Première dictée en réunion multi-speakers → notes structurées automatiquement

### 5. Go-to-Market
- **Canaux** : Product Hunt (#1), bouche-à-oreille Mac community, Twitter/X voice AI niche
- **Viral loop** : Partage de notes de réunion → "Généré avec MosMos" watermark
- **Launch strategy** : macOS-first, Windows/iOS comme extensions

### 6. Réplication pour Kyle
- **Complexité** : 6/10 (whisper + LLM polish + native app)
- **Verticaux adjacents** : Sales calls, Customer success notes, Coaching sessions
- **Angle Kyle** : Expert voice AI → peut sur-performer sur la qualité de polish vocal
- **Temps de dev** : ~3-4 mois pour MVP (focus vertical plutôt que généraliste)

## 🏆 TOP APP #2 : Voiskey
### 1. Identification
- **Nom** : Voiskey | **URL** : [voiskey.com](https://voiskey.com) | **Launch** : 16 Sept 2026
- **Catégorie** : Voice AI / Input method cross-platform
- **Buzz** : #2 Product Hunt du jour (480+ upvotes) → #5 Weekly (525 upvotes), PR Newswire
- **Sources** : [PR Newswire](http://www.prnewswire.com/news-releases/voiskey-ranks-2-on-product-hunt-launching-enhanced-context-aware-polish-to-bridge-the-expression-gap-302880572.html) · [Launly](https://launly.com/products/voiskey)

### 2. Proposition de Valeur
- **Problème** : Le gap entre ce qu'on pense, ce qu'on dit, et ce qu'on veut écrire ("Expression Gap")
- **Solution** : IA vocale qui transcrit ET reformule selon contexte, audience, ton (formel/casual/tech)
- **USP** : "Expression Intelligence" — premier produit positionné explicitement sur l'intent vs la transcription
- **Target** : Professionnels multi-plateforme (iOS/macOS/Android/Windows), 100+ langues
- **Pricing** : Freemium supposé, tier Pro ~$10-15/mois

### 3. Stack Technique (estimé)
- **Frontend** : Cross-platform (React Native ou Flutter)
- **Backend** : Pipeline ASR + LLM context polish
- **Sécurité** : SOC 2 Type II + ISO 27001 → enterprise-ready, stockage local par défaut
- **Infra** : On-device audio + cloud polish optionnel

### 4. Psychologie & JTBD
- **Triggers** : Autorité (SOC2/ISO27001), speed (5x faster), universalité (100+ langues)
- **JTBD** : "Quand j'écris à un client pro, je veux que mon dictum soit déjà formaté correctement"
- **Aha moment** : Email professionnel dicté en 10 sec, déjà formaté pour le destinataire

### 5. Go-to-Market
- **Canaux** : Product Hunt (#2), PR Newswire (signal enterprise), App stores multi-plateforme
- **Viral loop** : Cross-platform = plus de surface de partage
- **Différenciation** : Enterprise trust (certifications) + multi-platform

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (multi-plateforme + certifications enterprise coûteux)
- **Verticaux adjacents** : Support client, Équipes commerciales, Recruteurs
- **Angle Kyle** : Niche verticale voix pour Sales (CRM-native) plutôt que généraliste
- **Temps de dev** : 4-6 mois (focus 1 plateforme puis expansion)

## 🏆 TOP APP #3 : MakersClaw 2.0
### 1. Identification
- **Nom** : MakersClaw 2.0 | **URL** : [makersclaw.com](https://makersclaw.com/) | **Launch** : 18 Sept 2026
- **Catégorie** : AI Agents / Business Operating System
- **Buzz** : Top Product Hunt (>200 upvotes estimés), launch day coverage, trending AI agents PH
- **Sources** : [Product Hunt](https://www.producthunt.com/categories/ai-agents) · [StarupCorners digest](https://startupcorners.com/digest/product-digest-2026-09-19)

### 2. Proposition de Valeur
- **Problème** : Gérer des opérations d'entreprise demande trop de coordination humaine
- **Solution** : OS d'entreprise piloté par agents IA spécialisés (research, GTM, content, ops) partageant un contexte commun
- **USP** : Agents persistent avec mémoire partagée → company knowledge qui s'améliore avec le temps
- **Target** : Startups / PME voulant automatiser sans embaucher
- **Pricing** : Free (3,000 crédits, sans CB) + Pro mensuel pour équipes

### 3. Stack Technique (estimé)
- **Frontend** : React/Next.js dashboard
- **Backend** : Orchestrateur multi-agents (LangGraph ou OpenAI Assistants)
- **Mémoire** : Vector DB (Pinecone/Weaviate) pour contexte partagé
- **Infra** : Cloud SaaS, API-based

### 4. Psychologie & JTBD
- **Triggers** : Aspirationnel ("company run by agents"), FOMO agentic AI wave, free trial sans friction
- **JTBD** : "Quand je dois scaler sans recruter, je veux que des agents gèrent mes opérations"
- **Aha moment** : Premier workflow complet exécuté sans intervention (research → GTM → content)

### 5. Go-to-Market
- **Canaux** : Product Hunt, Twitter/X AI founders, Indie Hackers
- **Viral loop** : Résultats d'agents partagés publiquement ("notre GTM plan généré par agents")
- **Launch strategy** : Free tier large pour adoption → conversion Pro sur volume

### 6. Réplication pour Kyle
- **Complexité** : 8/10 (orchestration multi-agents + mémoire partagée complexes)
- **Verticaux adjacents** : Agences marketing, Scale-ups SaaS, Cabinets de conseil
- **Angle Kyle** : Vertical voice-first agents (réunions → tâches automatiques)
- **Temps de dev** : 6-9 mois pour version robuste

## 💰 Unit Economics Deep Dive — MosMos
*Note : MosMos est en phase early (lancé sept 2026). Estimations prudentes basées sur proxies marché.*

| Métrique | Estimation | Hypothèses |
|---|---|---|
| **Users actifs** | ~5,000 | 391 PH upvotes × conversion ~12x |
| **ARPU mensuel** | ~$12 | Freemium ~20% conversion → $0.2 avg |
| **MRR** | ~$12,000 | 1,000 payants × $12 |
| **ARR run rate** | ~$144K | MRR × 12 |
| **CAC** | ~$8 | PH launch = coût quasi nul (organique) |
| **LTV (24 mois)** | ~$240 | ARPU × 20 mois rétention estimée |
| **LTV/CAC** | ~30x | Très sain pour early stage |
| **Payback period** | < 1 mois | CAC < 1 ARPU |
| **Burn mensuel** | ~$30-50K | 2-3 dev + infra |
| **Runway** | Inconnu | Pas de levée publique détectée = bootstrapped ou pre-seed |
| **Rev/Employee** | ~$36K/an | Estimé 4 personnes |
| **Rule of 40** | ~70+ | Croissance rapide, burn contenu |

**Verdict santé : 🟢 Très sain pour early stage**
- LTV/CAC exceptionnel grâce au canal PH/organique
- Modèle freemium avec conversion attendue
- Risque : scalabilité infra vocale + Windows/iOS = coûts à venir
- Opportunité : si conversion Pro >20%, ARR ×3 en 6 mois plausible

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | MosMos | Voiskey | MakersClaw 2.0 |
|---|---|---|---|
| 📊 Market Size (20%) | 8 — Voice productivity >€500M | 8 — Multi-platform input global | 9 — AI ops >€1B |
| ⚙️ Complexity inversé (15%) | 6 — ASR + LLM + native | 5 — Multi-platform + certs | 3 — Multi-agent orchestration |
| ⏱️ Time-to-Market (15%) | 7 — 3-4 mois MVP vertical | 6 — 4-6 mois | 4 — 6-9 mois |
| 🏟️ Competition inversé (15%) | 7 — Whisper apps présentes mais niches libres | 6 — Otter/Fireflies concurrents | 5 — CrewAI/n8n/Zapier |
| 💰 Revenue Potential (20%) | 8 — >€50K MRR avec Pro conversion | 8 — Enterprise path + scale | 7 — Enterprise lent mais €100K+ MRR |
| 🧑‍💻 Founder-Fit Kyle (15%) | **10** — Expert voice AI + SaaS | **9** — Voice + multi-platform | 6 — Agents tech sans voice edge |

**Scores pondérés :**

| App | Score | Verdict |
|---|---|---|
| **MosMos** | **(8×0.2)+(6×0.15)+(7×0.15)+(7×0.15)+(8×0.2)+(10×0.15) = 7.85** | 🟢 **BUILD NOW** |
| **Voiskey** | **(8×0.2)+(5×0.15)+(6×0.15)+(6×0.15)+(8×0.2)+(9×0.15) = 7.25** | 🟡 **BUILD ADJACENT** |
| **MakersClaw 2.0** | **(9×0.2)+(3×0.15)+(4×0.15)+(5×0.15)+(7×0.2)+(6×0.15) = 5.90** | 🟠 **WATCH** |

## 📈 Tendances Émergentes
1. **Voice AI : de la transcription à l'intention** — MosMos et Voiskey incarnent le shift : ce n'est plus "écrire ce que tu dis" mais "comprendre ce que tu voulais dire". L'Expression Gap devient une catégorie à part entière.

2. **Agentic infrastructure comme couche par défaut** — MakersClaw, Toone, ProductBridge : les nouveaux SaaS B2B embarquent des agents IA non comme feature mais comme architecture core. La question n'est plus "IA ou non" mais "combien d'agents et quelle mémoire".

3. **Privacy-first = avantage concurrentiel** — MosMos (audio local) et Voiskey (SOC2+ISO27001) montrent que dans le voice AI, la confiance > les features. Les certifications enterprise s'obtiennent tôt et créent des barriers to entry.

4. **macOS-first comme stratégie de niche rentable** — L'audience Mac est plus petite mais paie plus et adopte plus vite. MosMos et d'autres choisissent délibérément ce canal avant d'élargir.

5. **GitHub Trending : l'ère des CLAUDE.md & Agent Skills** — Karpathy Skills (207k stars) et Addy Osmani Agent Skills (90k stars) signalent que la meta-couche "comment se comporter" pour les agents IA est le prochain champ de bataille.

## 💡 Insights Actionnables
### Pour Kyle (Voice AI + SaaS)

**🚀 Action immédiate : Fork the MosMos playbook en vertical**
MosMos est généraliste (toutes apps macOS). Kyle peut aller plus vite en ciblant un vertical précis avec sa crédibilité :
- **"MosMos for Sales"** → dictée + CRM push automatique (Salesforce/HubSpot)
- **"MosMos for Customer Success"** → notes d'appels + tickets automatiques (Zendesk/Intercom)
- MVP réalisable en 6-8 semaines avec Whisper + GPT-4o + webhook CRM

**🎯 Différenciation gagnante vs MosMos/Voiskey :**
- Intégration native CRM (ils ne le font pas)
- "Voice-to-Action" pas juste "Voice-to-Text" → crée la catégorie
- Pricing enterprise ($50-100/siège/mois) vs B2C ($12-20/mois) = LTV 5-10x supérieur

**📌 Signal faible à surveiller :**
- L'émergence de "Voice Agent Skills" sur GitHub est un signe que la prochaine couche sera les comportements vocaux agents. Kyle pourrait positionner un produit open-source early pour construire la communauté (cf. Karpathy Skills playbook → 207k stars).

**⚠️ Risque principal :**
- Apple Intelligence (macOS) + Google Gemini Live vont pousser dans ce territoire. La fenêtre d'opportunité pour les indépendants est ~12-18 mois avant que les OS intègrent ces features nativement.
