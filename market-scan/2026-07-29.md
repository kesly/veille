# 🔥 Market Scan — 2026-07-29

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : Glaze by Raycast
- Opportunités immédiates (BUILD NOW) : 1

## 🏆 TOP APP #1 : Glaze by Raycast
### 1. Identification
- **URL** : [raycast.com/glaze](https://www.raycast.com/blog/introducing-glaze)
- **Lancement** : Beta mars 2026 → Public **3 juillet 2026**
- **Fondateurs** : Petr Nikolaev & Thomas Paul Mann (Raycast, Berlin)
- **Catégorie** : No-code AI app builder (desktop natif macOS)
- **Métriques buzz** : #1 PH avec 574 upvotes · $47,8M levés (Atomico, Accel, Coatue)

### 2. Proposition de valeur
- **Problème** : Créer une app desktop native demande des mois de dev Swift/Electron
- **Solution** : Tu décris ton app en langage naturel → agent AI (Claude Code / Codex) génère une vraie app native qui vit dans le Dock, fonctionne offline, accède au système de fichiers
- **USP** : Apps 100% locales, pas un wrapper web — raccourcis clavier, menu bar, fichiers, processus background
- **Target** : Mac power users, solopreneurs, petites équipes tech
- **Pricing** : Free (120 crédits) · Pro $20/mois · Team $30/siège/mois

### 3. Stack technique
- **Frontend** : SwiftUI (macOS Tahoe, Apple Silicon only)
- **Backend** : Agent AI local (Claude Code ou OpenAI Codex sous le capot)
- **Distribution** : App store communautaire Glaze + partage privé équipe
- **Infra** : Pas de serveur pour les apps générées — 100% on-device

### 4. Psychologie & JTBD
- **Trigger** : Frustration du "ça prend 3 semaines juste pour avoir un script avec une UI"
- **JTBD** : "Quand j'ai une idée d'outil perso, je veux la builder en 10 min sans coder"
- **Aha moment** : Voir son app apparaître dans le Dock après 2 prompts
- **Social proof** : #1 PH, store communautaire (viral loop d'apps partagées)

### 5. Go-to-Market
- **Canal principal** : PH launch + X/Twitter (communauté Raycast existante ~500K users)
- **Viral loop** : App store public → chaque app partagée = pub gratuite pour Glaze
- **Stratégie** : Raycast avait déjà une base massive → lancement chaud garanti

### 6. Réplication pour Kyle
- **Complexité** : 7/10 — nécessite compétences Swift ou solide wrapper
- **Angle** : Builder le pendant **Windows/Linux** (Glaze = macOS seulement), ou vertical voice AI : app builder avec interface vocale
- **Verticaux adjacents** : Builder d'apps mobiles par prompt, builder d'outils internes no-code
- **Temps de dev estimé** : 4-8 mois (MVP) pour un équivalent cross-platform

## 🏆 TOP APP #2 : Superpowers
### 1. Identification
- **URL** : [github.com/obra/superpowers](https://github.com/obra/superpowers)
- **Lancement** : Octobre 2025 (open source)
- **Fondateur** : Jesse Vincent (aka obra) — vétéran open source (RT::Extension, keyboard.io)
- **Catégorie** : Agent skills framework (Claude Code, Cursor, Codex, Gemini CLI)
- **Métriques buzz** : **250 000 stars GitHub** (juillet 2026) · 7 000 stars/semaine au pic · 1 528 stars dans les 24h initiales

### 2. Proposition de valeur
- **Problème** : Les agents AI coding réinventent la roue à chaque session — pas de discipline TDD, pas de mémoire des bonnes pratiques
- **Solution** : Fichiers de skills Markdown auto-déclenchés par contexte, qui encodent la discipline d'ingénierie pro (TDD, revues, patterns) dans l'agent
- **USP** : Agnostique (Claude Code, Cursor, Codex, Gemini CLI) · Zero config · Open source
- **Target** : Développeurs utilisant des agents AI pour coder
- **Pricing** : 100% gratuit, open source (MIT)

### 3. Stack technique
- **Format** : Fichiers Markdown avec frontmatter YAML (triggers, contexte)
- **Intégration** : Hook natif dans Claude Code via `.claude/skills/`, Cursor via `.cursorrules`, etc.
- **Infra** : Aucune — pur côté client, zéro serveur
- **Monétisation** : Indirecte via notoriété / consulting (pas encore)

### 4. Psychologie & JTBD
- **Trigger** : L'agent qui fait une bêtise répétitive que tu aurais pu éviter
- **JTBD** : "Je veux que mon agent AI code comme un dev senior, pas comme un stagiaire"
- **Aha moment** : Premier test TDD que l'agent écrit tout seul sans qu'on lui demande
- **Viral loop** : Chaque dev qui partage son setup → bouche-à-oreille technique exponentiel

### 5. Go-to-Market
- **Canal principal** : HN Show HN + X/Twitter communauté Claude Code
- **Flywheel** : Open source → contribueurs → forks → ecosystem de skills communautaires
- **Momentum** : 250K stars = légitimité instantanée, top 5-6 repos GitHub de tous les temps

### 6. Réplication pour Kyle
- **Complexité** : 3/10 — créer une collection de skills voice AI spécialisés
- **Angle** : **Skills pack "Voice AI"** pour Claude Code (Vapi, Retell, ElevenLabs, Twilio) — Kyle est l'expert absolu
- **Verticaux adjacents** : Skills pack par secteur (legal, médical, e-commerce)
- **Temps de dev** : 2-4 semaines pour un MVP, potentiel monétisation via abonnement ou consulting

## 🏆 TOP APP #3 : Upstream
### 1. Identification
- **URL** : [upstream.email](https://upstream.email) (YC S26)
- **Lancement** : Juin-juillet 2026
- **Fondateurs** : Équipe YC Summer 2026
- **Catégorie** : Email client redesigné pour agents AI
- **Métriques buzz** : **876 upvotes PH** (meilleur score mensuel email) · YC-backed · $3M seed

### 2. Proposition de valeur
- **Problème** : Gmail/Outlook sont conçus pour des humains — les agents AI peinent à lire, trier, répondre efficacement aux emails
- **Solution** : Interface email native AI-first : les agents peuvent lire, trier, répondre, archiver avec des règles et déclencheurs structurés
- **USP** : Seul client email pensé pour collaboration humain + agent AI
- **Target** : Fondateurs, growth hackers, execs avec fort volume email
- **Pricing** : Non encore public (freemium probable) · $3M seed

### 3. Stack technique
- **Frontend** : Web app + API REST pour agents
- **Backend** : Intégration Gmail/Outlook IMAP · pipeline LLM pour classification
- **Infra** : Cloud (probablement AWS/GCP) · webhooks pour agents externes
- **APIs** : Compatible agents Claude, GPT, et outils no-code (Zapier, Make)

### 4. Psychologie & JTBD
- **Trigger** : L'email est le dernier bastion non-AI de la stack pro
- **JTBD** : "Je veux que mon agent AI gère mes emails comme je le ferais moi-même"
- **Aha moment** : Voir l'agent traiter 50 emails en 30 secondes avec zéro erreur
- **Social proof** : YC backing + 876 votes = crédibilité institutionnelle

### 5. Go-to-Market
- **Canal** : YC Demo Day · PH launch · réseaux fondateurs YC alumni
- **Viral loop** : Chaque user invite son équipe → adoption B2B organique
- **Timing** : Parfait — agents AI matures mais email client AI-native encore vierge

### 6. Réplication pour Kyle
- **Complexité** : 6/10 — intégrations email complexes mais patterns bien connus
- **Angle** : **Email agent vocal** — Upstream pour la voix : "dis-moi mes 5 emails importants" via voice AI
- **Verticaux adjacents** : Inbox AI pour Slack, WhatsApp Business, SMS
- **Temps de dev** : 2-3 mois pour MVP avec Vapi/ElevenLabs + IMAP

## 💰 Unit Economics Deep Dive — Glaze by Raycast
> ⚠️ Glaze a 4 semaines d'existence. Chiffres = estimations basées sur Raycast total + benchmarks no-code AI.

| Métrique | Estimation | Source / Note |
|---|---|---|
| **ARR Glaze** | ~$500K–$1,5M | Raycast $6,5M ARR total · Glaze = produit flagship |
| **Users payants** | ~3 000–7 500 | Taux conversion PH typique 2-5% · base Raycast 500K |
| **ARPU** | ~$240/an | Mix Free/Pro $20/mois / Team $30/siège |
| **CAC** | ~$15–30 | Communauté Raycast existante = CAC très bas |
| **LTV** | ~$480–720 | Rétention SaaS dev tools typique 24-36 mois |
| **LTV/CAC** | **16-48x** 🟢 | Excellent — base communautaire chauffe |
| **Payback period** | ~1-2 mois | CAC très faible, conversion rapide |
| **Burn mensuel** | ~$400–600K | Équipe Raycast ~40 personnes (Berlin) |
| **Runway** | ~7 ans | $47,8M levés, burn estimé |
| **Rev/Employee** | ~$162K | 40 employés · ARR total Raycast $6,5M |
| **Rule of 40** | ~50+ | Croissance forte post-launch + marges élevées SaaS |

**Verdict santé : 🟢 SAINE**
Raycast est une machine bien huilée. Glaze est un produit additionnel sur base installée massive. Le vrai risque : dépendance macOS/Apple Silicon (Windows exclu au lancement).

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Glaze | Superpowers | Upstream |
|---|:---:|:---:|:---:|
| 📊 Market Size (20%) | 7 | 8 | 8 |
| ⚙️ Complexity inversé (15%) | 3 | 9 | 5 |
| ⏱️ Time-to-Market (15%) | 2 | 9 | 5 |
| 🏟️ Competition inversé (15%) | 5 | 7 | 6 |
| 💰 Revenue Potential (20%) | 8 | 4 | 8 |
| 🧑‍💻 Founder-Fit Kyle (15%) | 5 | 9 | 8 |
| **Score pondéré** | **5,55** | **7,50** | **6,65** |
| **Verdict** | 🟠 WATCH | 🟢 BUILD NOW | 🟡 BUILD ADJACENT |

**Notes :**
- **Glaze** : Trop lié à macOS/Swift pour Kyle → difficile à répliquer sans équipe iOS. Compétition directe de Raycast (grosse boîte). Score honnête : 5,55 → 🟠 WATCH
- **Superpowers** : Kyle peut créer un skills pack "Voice AI" en 2-4 semaines. Huge credibility boost + monetization via abonnement. Score : 7,50 → 🟢 BUILD NOW
- **Upstream** : L'angle "email vocal" est pertinent pour Kyle. Marché large, mais intégrations email complexes. Score : 6,65 → 🟡 BUILD ADJACENT

## 📈 Tendances Émergentes
**1. L'ère du "Prompt-to-App" natif**
Glaze symbolise un shift : on passe de "vibe coding web" (Lovable, Bolt) à des apps desktop natives générées par AI. La prochaine étape sera mobile-native. Marché encore vierge.

**2. Frameworks d'agents > LLMs eux-mêmes**
Superpowers à 250K stars prouve que l'infrastructure autour des agents (skills, mémoire, discipline) est plus désirable que les modèles bruts. L'attention se déplace : moins "quel modèle" et plus "comment le cadrer".

**3. Stacks pro remodelées pour l'AI**
Upstream préfigure une vague de "X redesigned for AI agents" : email, calendrier, CRM, téléphonie. Les verticaux qui n'ont pas encore eu leur Upstream sont nombreux.

**4. Voice AI : de l'expérimentation à la production**
ElevenLabs à $500M ARR, Retell à $40M ARR, marché voice AI à $22,5B en 2026 (+34,8% CAGR). La maturité est là — c'est maintenant que les verticaux voice se construisent.

**5. Open Source comme moteur de distribution**
Les repos ultra-viraux (Superpowers 250K, d'autres à 100K+) prouvent que l'open source est devenu le meilleur canal d'acquisition B2B dev. La monétisation vient après la notoriété.

## 💡 Insights Actionnables
### 🟢 Action immédiate — Voice AI Skills Pack (Superpowers-style)

**Quoi** : Créer une collection open source de skills Claude Code spécialisés voice AI (Vapi, Retell, ElevenLabs, Deepgram, Twilio). Publier sur GitHub, lancer sur HN Show HN + X.

**Pourquoi maintenant** : Superpowers prouve que les skill packs viralisent. Le vertical voice AI n'a pas encore son "Superpowers". Kyle = l'expert idéal.

**Effort** : 2-4 semaines de contenu · zéro infra · open source

**Monétisation** : Notoriété → consulting, cours, abonnement premium skills, sponsors

---

### 🟡 À 3-6 mois — "Upstream for Voice" (inbox vocal)

**Quoi** : App qui lit, trie et répond aux emails via un agent vocal. "Dis-moi mes 3 emails urgents" → résumé vocal → réponse dictée.

**Angle Kyle** : Il maîtrise Vapi/Retell + SaaS → combinaison parfaite. Stack : Vapi + IMAP + Claude + ElevenLabs.

**Effort** : 2-3 mois MVP · $5-15K/mois potentiel à 6 mois

---

### 📌 Signal à surveiller — Glaze Windows/Linux

Glaze est macOS-only. Si Raycast annonce Windows support → confirme le marché. Si non → opportunité de builder l'équivalent cross-platform (Electron + Claude Code API).

---

### 💡 Méta-insight

Le marché en juillet 2026 récompense deux profils : (1) les **infra builders** (frameworks, skills, APIs) et (2) les **vertical AI apps** (email, voice, calendrier) sur une strate d'agents mûrs. Kyle est positionné sur les deux — il doit choisir où concentrer son energie cette semaine.
