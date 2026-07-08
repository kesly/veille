# 🔥 Market Scan — 2026-07-08

## 📊 Résumé Exécutif
- Apps analysées : 8
- Top potentiel : Acti, Glaze by Raycast, Humalike
- Opportunités immédiates (BUILD NOW) : 1

## 🏆 TOP APP #1 : Acti
### 1. Identification
- **URL** : https://acti.so | **Launch** : 30 juin 2026 | **PH #1** : 1er juillet 2026
- **Fondateurs** : Young Wang (CEO), Mike Sun (CTO, ex-Baidu Yike Album 10M DAU), Junbo Yang (CSO, ex-HashKey)
- **HQ** : Singapour | **Catégorie** : AI Mobile Productivity
- **Buzz** : #1 PH (231 upvotes, 549 comments), TechCrunch, Unite.AI, 10+ médias internationaux, $5.3M seed annoncé simultanément

### 2. Proposition de Valeur
- **Problème** : jongler entre 10 apps pour obtenir de l'aide IA = friction massive sur mobile
- **Solution** : clavier iOS/Android qui intègre des agents IA directement dans TOUTES les apps
- **USP** : contexte cross-app appartenant à l'utilisateur, pas à la plateforme
- **Target** : power users mobiles, early adopters IA, professionnels nomades
- **Pricing** : freemium → subscription (premium models + usage illimitée, prix non encore public)

### 3. Stack Technique
- **Frontend** : iOS/Android natif | **Backend** : cloud + local-first (données perso on-device)
- **LLM** : Google Gemini (choix pour vitesse, fiabilité, multilangue)
- **Système** : "Skills" — workflows no-code créés par les utilisateurs (1,000+ déjà buildés en beta)

### 4. Psychologie
- **Triggers** : curiosité (premier clavier agentique), utilité immédiate, social proof (TechCrunch day-one)
- **JTBD** : "Je veux faire des recherches / booking / traductions sans quitter ma conversation"
- **Aha moment** : premier restaurant trouvé depuis son clavier iMessage sans ouvrir Maps

### 5. Go-to-Market
- **Canaux** : Product Hunt (viral), TechCrunch coverage, communauté dev Skills, App Store
- **Launch strategy** : funding annonce + PH + médias le même jour (trifecta)
- **Viral loop** : utilisateurs partagent leurs Skills → ecosystem s'auto-alimente

### 6. Réplication pour Kyle
- **Complexité** : 8/10 (LLM integration + clavier system extension iOS = hardu)
- **Verticaux adjacents** : clavier vocal (dicter des actions), clavier B2B (Salesforce, CRM depuis clavier)
- **Angle Kyle** : **version voice** — même concept mais commandes vocales intégrées dans le clavier
- **Temps de dev** : 4-6 mois MVP (iOS keyboard extension + voice API + 1 modèle LLM)

## 🏆 TOP APP #2 : Glaze by Raycast
### 1. Identification
- **URL** : https://glaze.app | **Launch** : 1er juillet 2026 (GA après beta privée mars 2026)
- **Fondateurs** : Équipe Raycast (Thomas Paul Mann, Raycast CEO)
- **Catégorie** : No-code AI App Builder (Desktop)
- **Buzz** : 368 votes PH, couverture AlternativeTo, TechBuzz, 01Webmasters, utilisé par Cursor/Linear/Vercel

### 2. Proposition de Valeur
- **Problème** : créer une app desktop custom = engager un dev. Les outils internes restent des Google Sheets bricolés.
- **Solution** : décris l'app en chat → Glaze génère une vraie app native Mac qui tourne en local
- **USP** : app native (pas web-app), fonctionne hors ligne, s'installe dans le Dock, partage public/privé
- **Target** : équipes ops, solopreneurs, power users Mac, devs qui veulent prototyper vite
- **Pricing** : Gratuit → $20/mois (paid plan)

### 3. Stack Technique
- **Runtime** : apps natives macOS (Swift/SwiftUI sous le capot, généré par IA)
- **Backend** : Raycast Cloud + modèles LLM internes
- **Distribution** : via Raycast App Store interne (100K+ daily users captifs)

### 4. Psychologie
- **Triggers** : possession (l'app est à vous, dans votre Dock), rapidité (moins de 2 min pour builder)
- **JTBD** : "Je veux un outil fait sur mesure sans attendre l'équipe dev"
- **Aha moment** : voir son app apparaître dans le Dock après 90 secondes de chat

### 5. Go-to-Market
- **Distribution** : audience captive Raycast (100K+ DAU) = distribution immédiate sans acquisition
- **Stratégie** : beta privée 4 mois → hype → GA avec couverture médias coordonnée
- **Viral loop** : apps Glaze partageables publiquement → showcase → nouveaux signups Raycast

### 6. Réplication pour Kyle
- **Complexité** : 9/10 (génération d'apps natives = infra très lourde)
- **Verticaux adjacents** : builder d'apps vocales (même concept mais pour voice flows), agent builder B2B
- **Angle Kyle** : créer un "Glaze for Voice" — describe ton assistant vocal → génère le flow Vapi/ElevenLabs
- **Temps de dev** : 3-4 mois MVP (wrapper over existing voice APIs + LLM orchestration)

## 🏆 TOP APP #3 : Humalike
### 1. Identification
- **URL** : https://humalike.ai | **Launch** : 1er juillet 2026 | **PH #2** : 162 upvotes, 449 comments
- **Fondateurs** : Martí (CEO), Mateusz Jacniacki (CTO, 2x médaille Olympiade Informatique Pologne)
- **Catégorie** : AI Infrastructure / Behavioral APIs
- **Buzz** : #2 PH July 1, produit "Jared" (AI employee) lancé mars 2026, couverture BuildMVPFast

### 2. Proposition de Valeur
- **Problème** : les agents IA sont "robotiques" — ils interrompent au mauvais moment, ignorent les signaux sociaux, manquent de tact
- **Solution** : APIs + modèles pour donner aux agents une intelligence sociale (turn-taking, empathie, mémoire sociale)
- **USP** : infrastructure comportementale — couche transversale compatible avec tous les agents
- **Target** : développeurs d'agents IA, entreprises déployant des assistants vocaux/chat
- **Pricing** : Free tier → $2,000/mois (enterprise)

### 3. Stack Technique
- **Produit** : APIs REST + modèles fine-tunés + benchmarks publics
- **Features** : Turn-Taking, Theory of Mind, Norms (ton du groupe), Social Memory, Social Signals
- **Modèle commercial** : B2B API (usage-based ou seat-based)

### 4. Psychologie
- **Triggers** : douleur universelle (tout le monde a vécu un agent mal calibré), FOMO (les concurrents vont l'intégrer)
- **JTBD** : "Je veux que mon agent vocal ne coupe pas les clients et sache quand se taire"
- **Aha moment** : tester l'API turn-taking et entendre un agent qui sait écouter pour la première fois

### 5. Go-to-Market
- **Canaux** : PH #2, communauté AI builder, Jared (AI employee) comme produit d'appel
- **Stratégie** : lancer un produit B2C (Jared) pour prouver la tech → vendre l'API aux builders
- **Viral loop** : benchmarks publics → cités par chercheurs → crédibilité → inbound B2B

### 6. Réplication pour Kyle
- **Complexité** : 7/10 (fine-tuning + datasets comportementaux = recherche réelle)
- **Verticaux adjacents** : intelligence sociale pour voice AI (cliniques, banques, e-commerce)
- **Angle Kyle** : intégrer Humalike dans un stack Vapi pour vendre des agents vocaux "premium" aux PME
- **Temps de dev** : 0 dev (API à intégrer) → 2-3 semaines pour un proof-of-concept vendable

## 💰 Unit Economics Deep Dive — Acti
**Données disponibles** : $5.3M seed (BITKRAFT Ventures, juillet 2026). Revenue = pré-monétisation (modèle subscription non encore lancé). Estimations basées sur benchmarks mobile AI freemium.

| Métrique | Estimation | Source / Hypothèse |
|---|---|---|
| ARR actuel | ~$0 (pre-revenue) | Subscription non lancé |
| Users bêta | ~5,000-15,000 | 1,000 Skills créés = proxy engagement |
| ARPU cible | $8-15/mois | Benchmark clavier premium (Gboard Pro-tier) |
| CAC estimé | $2-5 | App Store + viral PH/médias = faible |
| LTV cible (12 mois) | $96-180 | ARPU × 12 mois |
| LTV/CAC | 20-90x | Excellent si modèle freemium → conversion 3-5% |
| Payback | <1 mois | CAC très bas |
| Burn mensuel | ~$150K-250K | Seed $5.3M / 18-24 mois runway |
| Runway | 18-24 mois | Seed conservé |
| Rev/Employee | N/A | Pré-revenue |
| Rule of 40 | N/A | Trop tôt |

**Verdict santé : 🟡 TROP TÔT**
L'entreprise est clairement en phase build. Le seed est suffisant pour 18-24 mois. La thèse est solide (distribution via App Store, modèle freemium, LLM cost declining), mais sans revenue publique il est impossible de valider les unit economics. **Signal positif** : $5.3M seed + couverture TechCrunch day-one + CTO avec track record 10M DAU = équipe crédible.

Sources : TechCrunch (30/06/2026), Unite.AI (01/07/2026), TNGlobal (01/07/2026)

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Acti | Glaze by Raycast | Humalike |
|---|---|---|---|
| 📊 Market Size (20%) | 8 — clavier mobile = 4B users | 6 — Mac only = niche | 9 — infra AI agents = $10B+ |
| ⚙️ Complexité inversée (15%) | 3 — keyboard extension = dur | 2 — native app gen = très dur | 7 — API wrapper = faisable |
| ⏱️ Time-to-Market (15%) | 3 — 4-6 mois | 2 — 6-9 mois | 8 — 2-3 semaines (API exist) |
| 🏟️ Compétition inversée (15%) | 6 — Gboard/SwiftKey mais ≠ agentique | 5 — Cursor/bolt.new mais ≠ desktop natif | 5 — ElevenLabs/Vapi se rapprochent |
| 💰 Revenue Potential (20%) | 7 — freemium mobile à grande échelle | 6 — $20/mois mais petite base Mac | 8 — B2B API $2K/mois × 50 clients |
| 🧑‍💻 Founder-Fit Kyle (15%) | 7 — voice version = natif à Kyle | 5 — moins voice, plus UI | 9 — stack Vapi/voice = plug direct |

**Score pondéré :**
- **Acti** : (8×0.20)+(3×0.15)+(3×0.15)+(6×0.15)+(7×0.20)+(7×0.15) = **5.95** 🟠 WATCH
- **Glaze** : (6×0.20)+(2×0.15)+(2×0.15)+(5×0.15)+(6×0.20)+(5×0.15) = **4.55** 🟠 WATCH
- **Humalike** : (9×0.20)+(7×0.15)+(8×0.15)+(5×0.15)+(8×0.20)+(9×0.15) = **7.70** 🟢 **BUILD NOW**

> **Verdict** : Humalike est le winner pour Kyle. L'angle "social intelligence pour agents vocaux" est un différenciateur immédiat à intégrer dans ses stacks actuels, sans re-dev lourd. Acti mérite une veille (angle voice keyboard à 6 mois). Glaze : beau produit mais hors reach technique de Kyle seul.

## 📈 Tendances Émergentes
### 1. L'IA descend dans le clavier (Acti)
La prochaine bataille de distribution mobile se joue dans le clavier. Qui contrôle le clavier contrôle l'interaction cross-app. Acti en est le signal le plus clair.

### 2. L'infra comportementale pour agents = nouveau marché $1B+
Humalike et ses pairs (Sierra, Warmly) signalent que les entreprises ne veulent plus des agents génériques — elles veulent des agents avec des personnalités calibrées. La couche comportementale va devenir standard (comme les guardrails aujourd'hui).

### 3. Les app builders IA passent au natif
Glaze prouve que "générer une web-app" ne suffit plus. Les utilisateurs veulent des apps qui vivent dans leur OS. Prochaine étape : builders pour iOS natif, Windows natif.

### 4. Voice AI franchit le cap des $2B de valorisation (Wispr Flow, signal fort)
Wispr Flow en discussions pour $2B (ex-$700M il y a 6 mois). La dictée voix quitte le niche premium et devient infrastructure. Le marché valide que les utilisateurs paient pour la voix.

### 5. Reddit > Product Hunt pour la traction indie
Les indie hackers 2026 génèrent 3-8x plus de signups via r/SideProject que PH. La distribution organique Reddit est sous-exploitée par les fondateurs français.

## 💡 Insights Actionnables pour Kyle
### 🎯 Top 3 actions immédiates pour Kyle

**1. Tester Humalike API aujourd'hui (effort : 2h)**
Intégrer le module Turn-Taking dans un agent Vapi existant. Si le résultat est meilleur → slide "nos agents coupent 73% moins les clients" = argument de vente premium immédiat. Humalike a un free tier — zéro risque.

**2. Monitorer Acti pour angle Voice Keyboard (horizon : 6 mois)**
Si Acti ouvre une API Skills, Kyle peut builder un "Voice Skill" — commande vocale intégrée dans le clavier. Première movers advantage sur le segment voice-in-keyboard. Action : s'inscrire à leur developer newsletter.

**3. Repositionner les agents vocaux comme "social-aware" (effort : 1 semaine marketing)**
Wispr Flow à $2B prouve que les gens paient pour la voix. La différenciation de Kyle n'est pas "un agent vocal de plus" mais "un agent qui sait écouter, s'arrêter et s'adapter". Humalike donne la tech. Kyle apporte l'expertise verticale + la distribution francophone.

### ⚡ Signal à ne pas rater
Le marché Voice AI Agent pour PME est en train de se structurer : $3.5B de revenus cumulés pour 254 SaaS, mais **aucun player dominant francophone**. Fenêtre d'opportunité : 12-18 mois avant consolidation.
