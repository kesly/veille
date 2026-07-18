# 🔥 Market Scan — 2026-07-18

## 📊 Résumé Exécutif
- Apps analysées : 10+ (Product Hunt, HN, GitHub Trending, Reddit)
- Top potentiel : River (voice AI × B2B sales)
- Opportunités immédiates (BUILD NOW) : 0 — 1 BUILD ADJACENT fort (River vertical)

## 🏆 TOP APP #1 : River
### 1. Identification
- **URL** : rivereditor.com (launch Vercel Day, 16 juillet 2026)
- **Fondateurs** : Équipe xAI alumni, backée par fondateurs de Ramp, Kalshi, Lean
- **Catégorie** : Sales AI / Voice AI / Audio
- **Buzz** : #1 Product Hunt 17 juillet 2026 (Vercel Day contest) · mentions presse Yahoo Finance, Bloomberg

### 2. Proposition de valeur
- **Problème** : Les leads B2B attendent 48h+ le calendrier d'un AE. Taux de no-show : 30-50%.
- **Solution** : Un AI Account Executive rejoint le call en live dès qu'un lead envoie un message — démo, gestion d'objections, close. Zéro attente.
- **USP** : "Never let a lead wait for a rep's calendar"
- **Cible** : PME/ETI B2B, équipes sales 5-50 personnes, SaaS mid-market
- **Pricing** : Non public (early access). Modèle probable : per seat ($500-1500/mo) ou success fee sur deals closés.

### 3. Stack technique
- **Frontend** : Vercel (lancé Vercel Day), Next.js probable
- **Voice AI** : LLM + TTS/STT temps réel (type ElevenLabs / Deepgram)
- **Orchestration** : Agents LLM avec mémoire de session, CRM sync (Salesforce/HubSpot)
- **Infra** : Vercel Edge pour faible latence call

### 4. Psychologie & JTBD
- **Trigger principal** : Urgence + Social Proof (backed by Ramp founders = crédibilité B2B)
- **JTBD** : "Quand un lead arrive, close-le maintenant, pas dans 3 jours"
- **Aha moment** : Premier call fermé sans intervention humaine
- **Biais** : FOMO concurrentiel (si mon concurrent a River, il répond 24/7)

### 5. Go-to-market
- **Canal principal** : Vercel Day (audience dev/founder captive) + LinkedIn (fondateurs credibles)
- **Viral loop** : Le prospect qui reçoit le call AI en est impressionné → en parle → inbound
- **Launch strategy** : Contest PH (#1), early access waitlist, démos live

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (voice AI temps réel + intégration CRM + gestion objections)
- **Angle Kyle** : Kyle est expert voice AI → il possède déjà la brique critique (le moteur vocal). Le différentiel : verticaliser par secteur (immo, finance, SaaS).
- **Verticaux adjacents** : Real estate AI agent, Insurance broker AI, Recrutement AI
- **Temps de dev** : 3-5 mois MVP (avec stack voice AI existante de Kyle → 2 mois)
- **Avantage concurrentiel** : Kyle peut builder 3× plus vite que quelqu'un qui part de zéro

## 🏆 TOP APP #2 : JustVibe
### 1. Identification
- **URL** : justvibe.com
- **Fondateurs** : Lianghao Chen — ex-ML Lead Pinterest & The Yes (acquis par Pinterest)
- **Date** : #1 Product Hunt 12 juillet 2026 — 563 upvotes, 88 comments · #8 Weekly Leaderboard W28
- **Catégorie** : AI Search / Generative Apps / No-code
- **Buzz** : Newsletter PH "Never click a link again", couverture DailyAIWorld, Dynamic Business

### 2. Proposition de valeur
- **Problème** : Google retourne des liens → l'utilisateur doit naviguer, compiler, calculer lui-même.
- **Solution** : Tapez "divise les frais du ski trip en 5" → JustVibe génère une app interactive fonctionnelle. Pas de liens, une app.
- **USP** : Search engine for *doing*, pas pour *lire*
- **Cible** : Grand public, early adopters, étudiants, travailleurs du savoir
- **Pricing** : 100% gratuit, sans compte. Modèle monétisation : inconnu (Google Gemini API en dessous).

### 3. Stack technique
- **LLM** : Google Gemini (modèles sous la surface)
- **Exécution** : Apps générées dans un environnement sandbox navigateur (iframe sécurisé)
- **Frontend** : UI minimaliste, zero-signup UX
- **GTM** : Programmatic SEO via Publer pour Pinterest/LinkedIn

### 4. Psychologie & JTBD
- **Trigger** : Frictionlessness (aucun compte, aucun click superflu)
- **JTBD** : "Aide-moi à *faire* quelque chose, pas à lire comment le faire"
- **Aha moment** : La première app générée en 30 secondes qui résout réellement votre problème
- **Biais** : Effet de surprise ("ça marche vraiment ?") → partage social immédiat

### 5. Go-to-market
- **Canal** : Product Hunt + bouche-à-oreille (shareable app outputs)
- **Viral loop** : L'app générée est partageable → "regarde ce que j'ai créé en 10 secondes"
- **Faiblesses** : Pas de monétisation visible → risque de shutdown si coût API explose

### 6. Réplication pour Kyle
- **Complexité** : 6/10 (LLM orchestration + sandbox sécurisé + UX)
- **Angle Kyle** : Vertical voice — "JustVibe mais vocal" : parlez votre besoin, obtenez un mini-outil
- **Verticaux adjacents** : Secteur juridique (gen contracts on-demand), RH (onboarding tools)
- **Temps de dev** : 2-3 mois MVP sans sandbox custom, 4-5 mois avec
- **Risque** : Monétisation floue, concurrence OpenAI / Perplexity imminente

## 🏆 TOP APP #3 : Miora
### 1. Identification
- **URL** : miora.design
- **Fondateurs** : Tencent AI (labo international) — Igor Babuschkin (xAI co-fondateur) mentionné séparément
- **Date** : #1 Product Hunt 12 juillet 2026 · #16 Monthly Leaderboard juillet 2026
- **Catégorie** : AI Creative Studio / Design Tools / Marketing AI
- **Buzz** : Tweet viral Tencent AI News · annonce beta internationale

### 2. Proposition de valeur
- **Problème** : Les créatifs switchent entre 6-10 outils (Figma, Midjourney, Runway, etc.). Contexte perdu à chaque switch.
- **Solution** : Un canvas unique où des agents IA spécialisés génèrent images, vidéo, UI/UX, 3D — tout au même endroit avec mémoire partagée.
- **USP** : "Memory-as-editable-rules" — la mémoire de marque est visible et modifiable (≠ black box)
- **Cible** : Agences créatives, marketers, studios de contenu
- **Pricing** : Beta gratuite (modèle freemium annoncé)

### 3. Stack technique
- **Multi-agents** : Orchestrateur LLM + agents spécialisés (image, video, 3D, UI/UX)
- **Canvas** : Interface collaborative type Figma + génération IA inline
- **Mémoire** : Système de règles éditables (brand memory → style consistency)
- **Infra** : Tencent Cloud (avantage coût GPU significatif)

### 4. Psychologie & JTBD
- **Trigger** : Unification (1 outil vs 6) + Autorité (Tencent derrière)
- **JTBD** : "Génère une campagne complète (script, storyboard, vidéo, 3D) en une session"
- **Aha moment** : La mémoire de marque appliquée automatiquement sur le prochain asset
- **Biais** : Effect Ikea (les règles mémoire éditables donnent sentiment de contrôle et ownership)

### 5. Go-to-market
- **Canal** : Product Hunt + Twitter/X (audience créatifs) + Tencent distribution Asia
- **Viral loop** : Assets de campagne partagés avec watermark Miora
- **Risque** : Tencent = friction perçue côté occidental (données, confidentialité)

### 6. Réplication pour Kyle
- **Complexité** : 9/10 (multi-agent orchestration multimodale = mois de R&D)
- **Angle Kyle** : Non recommandé à répliquer. Observer les patterns UX de memory-as-rules pour les réutiliser dans un product voice AI.
- **Temps de dev** : 12+ mois avec équipe senior
- **Verdict** : Surveiller, ne pas builder

## 💰 Unit Economics Deep Dive — River
> ⚠️ River vient de lancer (Vercel Day, 16 juillet 2026). Pas de métriques publiques. Estimations basées sur comparables du secteur (11x.ai, Artisan AI, AiSDR).

| Métrique | Estimation | Hypothèse |
|---|---|---|
| **ARR actuel** | ~€0 (pre-revenue / early access) | Launch < 72h |
| **ARPU cible** | €800-1500/mo par équipe | Benchmark 11x.ai ($1K/mo), Artisan ($1.5K/mo) |
| **Clients Y1 cible** | 50-200 teams | Typical B2B AI sales SaaS Y1 |
| **ARR Y1 projeté** | €480K-€3.6M | Fourchette large, dépend GTM |
| **CAC estimé** | €2K-5K | Sales-led B2B, faible self-serve attendu |
| **LTV estimé** | €14K-27K | ARPU × 18 mois churn moyen B2B AI |
| **LTV/CAC** | 5-7× | Sain si ≥3× |
| **Payback period** | 3-6 mois | Bon pour SaaS B2B |
| **Burn estimé** | ~€200-400K/mo | Petite équipe + voice AI infra coûteuse |
| **Runway** | 12-24 mois | Si seed $3-5M |
| **Rev/Employee** | N/A (trop tôt) | — |
| **Rule of 40** | N/A | — |

**Sources comparables** : 11x.ai (raised $24M), Artisan AI (raised $11M), AiSDR, Aire.
**Verdict santé** : 🟡 Trop tôt pour juger. Sains fondamentaux (LTV/CAC estimé correct) mais burn voice AI infra est élevé. Watch closely Q4 2026.

**Signaux d'alarme à surveiller** : Pricing public non annoncé (risque freemium trap), concurrence Salesforce Agentforce qui pousse sur le même marché.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | River /10 | JustVibe /10 | Miora /10 |
|---|---|---|---|
| 📊 Market Size (20%) | **8** (B2B sales >$50B) | **7** (AI search large) | **7** (creative tools) |
| ⚙️ Complexity inversé (15%) | **5** (voice AI complexe) | **6** (sandbox + LLM) | **2** (multi-agent multimodal) |
| ⏱️ Time-to-Market (15%) | **6** (2-3 mois si stack voice existante) | **5** (3-4 mois) | **2** (12+ mois) |
| 🏟️ Competition inversé (15%) | **5** (Artisan, 11x, Salesforce Agentforce) | **4** (OpenAI/Perplexity imminents) | **4** (Canva, Adobe) |
| 💰 Revenue Potential (20%) | **8** (B2B SaaS $1K+/mo) | **4** (gratuit, monétisation floue) | **7** (agences créatives) |
| 🧑‍💻 Founder-Fit Kyle (15%) | **9** (voice AI expert, réseau SaaS) | **5** (ML/search distant) | **3** (créatif, hors scope) |
| **Score pondéré** | **🟡 6.55** | **🟠 5.20** | **🔴 4.10** |
| **Verdict** | 🟡 BUILD ADJACENT | 🟠 WATCH | 🔴 SKIP |

**Calculs détaillés** :
- River : (8×.20)+(5×.15)+(6×.15)+(5×.15)+(8×.20)+(9×.15) = 1.6+0.75+0.9+0.75+1.6+1.35 = **6.95** → 🟡 BUILD ADJACENT
- JustVibe : (7×.20)+(6×.15)+(5×.15)+(4×.15)+(4×.20)+(5×.15) = 1.4+0.9+0.75+0.6+0.8+0.75 = **5.20** → 🟠 WATCH
- Miora : (7×.20)+(2×.15)+(2×.15)+(4×.15)+(7×.20)+(3×.15) = 1.4+0.3+0.3+0.6+1.4+0.45 = **4.45** → 🔴 SKIP

**Recommandation clé** : River à 6.95 est le seul candidate BUILD ADJACENT. L'angle pour Kyle : ne pas répliquer River, mais builder un **vertical voice AI sales agent ciblé** (ex: immo, fintech, santé) où River ne peut pas aller avec un produit généraliste.

## 📈 Tendances Émergentes
### 1. 🤖 L'agent prend le téléphone (Voice AI Sales)
River n'est pas isolé. 11x.ai, Artisan, AiSDR — tous convergent vers l'idée qu'un AE AI peut closer des deals. La semaine Vercel Day a boosté la catégorie "AI Audio/Sales" sur PH. Signal fort : Salesforce Agentforce devient grand public → le marché est validé, la niche reste à prendre.

### 2. 🔍 Search → Do (Zero-Click Apps)
JustVibe incarne un shift : les utilisateurs ne veulent plus de liens. Ils veulent de l'action. Perplexity a commencé, JustVibe va plus loin. OpenAI va certainement lancer quelque chose de similaire dans SearchGPT. Fenêtre courte pour les challengers.

### 3. 🎨 Canvas IA Unifié (Memory + Multimodal)
Miora (Tencent), mais aussi Figma AI, Framer Agents (lancé Vercel Day également) — tous poussent vers un canvas unique. La tendance "memory-as-editable-rules" de Miora est une UX breakthrough à surveiller pour tout produit AI.

### 4. ⚡ Vercel Day = Nouveau Product Hunt pour Dev Tools
Le contest Vercel Day a propulsé River, Framer AI, et Glaze by Raycast en tête de PH simultanément. Pattern à mémoriser : les "platform days" (Vercel Day, Stripe Sessions, GitHub Universe) sont désormais des launches events premium pour les startups AI. S'y plugger = distribution garantie.

### 5. 📦 GitHub Trending : Open-Source AI Agent Infra
Les repos les plus étoilés du moment : Orca/herdr (coordination agents), OpenClaw (AI personnel local), Langflow/Dify/Flowise (visual AI builder). Signal : l'infra pour builder des agents se commoditise rapidement → les moats seront sur la verticale et l'expérience utilisateur, pas la techno.

## 💡 Insights Actionnables
### 🎯 Pour Kyle — Actions concrètes cette semaine

**1. Analyse River en profondeur (priorité #1)**
- Teste River en tant que prospect fictif d'une démo
- Identifie les lacunes : gestion d'objections industrie-spécifiques ? Intégration CRM ? Latence voice ?
- Ces lacunes = ton opportunité de verticaliser

**2. Valide le marché vocal B2B en 48h**
- Poste sur LinkedIn/Twitter : "Votre équipe sales utilise un AI pour closer des deals ? Répondez"
- 5 appels discovery avec directeurs commerciaux PME (immo, fintech, SaaS)
- Question clé : "Combien paieriez-vous pour ne jamais perdre un lead faute de disponibilité ?"

**3. Benchmark concurrents directs de River**
- 11x.ai · Artisan AI · AiSDR · Aire · Regie.ai
- Matrice : pricing / démo quality / CRM integration / latence / verticaux couverts
- Trouve le gap non couvert → c'est ta beachhead

**4. JustVibe : surveiller, ne pas builder**
- Modèle gratuit sans monétisation = piège. Mais l'UX "zero-click search" va influencer tous les produits AI. Intégrer cette UX logic dans tes produits voice AI.

**5. Miora : pattern mémoire à voler**
- "Memory-as-editable-rules" est une UX brillante que tu peux adapter pour un voice AI agent : l'utilisateur voit et édite les règles de comportement de son agent → sentiment de contrôle → rétention.

**6. Participer à la prochaine plateforme event**
- GitHub Universe (oct 2026), Vercel Day suivant → prépare un launch timing autour de ces events pour maximiser la distribution organique.

### 📌 KPIs à suivre
| Signal | Outil | Fréquence |
|---|---|---|
| River levée de fonds | Crunchbase | Hebdo |
| 11x.ai / Artisan pricing change | Leurs sites | Bi-mensuel |
| JustVibe monétisation annonce | PH / Twitter | Alert |
| GitHub stars OpenClaw / Langflow | Star-history.com | Mensuel |
