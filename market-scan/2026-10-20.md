# 🔥 Market Scan — 2026-10-20

> ⚠️ Limites de ce run : Product Hunt et Hacker News inaccessibles (DNS bloqué), recherches web sans résultats datés d'octobre 2026. Seule source fiable : GitHub Trending (hebdo). Dates de création des repos non vérifiées (critère « <6 mois » non confirmé). Chiffres de stars à prendre avec prudence (valeurs divergentes entre la page Trending et les pages repo).

## 📊 Résumé Exécutif
- Apps analysées : 3 (toutes open-source, signal GitHub uniquement)
- Top potentiel : VoiceStudio (voice AI local, alignement direct avec Kyle)
- Opportunités immédiates (BUILD NOW) : 0 (1 BUILD ADJACENT probable, voir scorecard)

## 🏆 TOP APP #1 : VoiceStudio
**1. Identification**
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — open-source (AGPL-3.0), gratuit, voicestudio.sh
- Maintainer : debpalash (solo visible). Date de launch : non confirmée.
- Buzz : ~77,8k stars / 8,5k forks sur la page repo ; ~17k stars sur la semaine (GitHub Trending). 4 387 commits, 159 PR ouvertes → communauté très active.

**2. Proposition de valeur**
- Problème : le clonage vocal, le doublage et la dictée passent par des SaaS cloud payants (ElevenLabs, etc.).
- Solution : suite locale tout-en-un : clonage, design de voix, doublage vidéo, dictée (widget flottant), transcription, audiobooks, 646 langues.
- USP : local/privé, gratuit, API + serveur MCP pour agents.
- Cible : créateurs, podcasteurs, devs d'agents. Pricing : gratuit ; sponsoring et dons.

**3. Stack**
- Electron (Tauri abandonné), backend Python (uv, Alembic), Bun/Node 22, Rust. Moteur k2-fsa/OmniVoice, moteurs interchangeables. CUDA / MLX / CPU. Companion iOS/Android en preview.

**4. Psychologie**
- Triggers : gratuité vs abonnement, privacy, social proof (stars), FOMO « 646 langues ».
- JTBD : « cloner/doubler une voix sans payer ni envoyer mes données ».
- Aha : première voix clonée en local en quelques secondes.

**5. Go-to-market**
- Installeur one-liner, GitHub Trending, sponsoring payant visible, Discord. Boucle virale : contenus générés + stars. Intégration agents via MCP.

**6. Réplication**
- Complexité 5/10 pour un wrapper ; 8/10 pour égaler la qualité modèle. Dev : 2-3 mois pour un MVP vertical.
- Verticaux adjacents : doublage pour e-learning, voix-off pour agences, voice agents téléphoniques FR.
- Angle Kyle : ne pas concurrencer l'outil généraliste ; empaqueter le moteur open-source en SaaS vertical hébergé (conformité RGPD, voix FR/créole), là où l'installation locale freine les non-techniques.

## 🏆 TOP APP #2 : HyperFrames (HeyGen)
**1. Identification**
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — open-source (Apache 2.0), gratuit. Éditeur : HeyGen (société établie, pas un indie).
- Buzz : ~67,8k stars, 6,1k forks ; ~5,9k stars/semaine. Adopté par tldraw, TanStack. Date de launch non confirmée.

**2. Proposition de valeur**
- Problème : générer des vidéos par agent IA est fragile avec les timelines propriétaires.
- Solution : « Write HTML. Render video. » Compositions HTML + attributs de timing, rendu déterministe en MP4.
- USP : format ouvert que les LLM maîtrisent déjà (HTML/CSS), 21 skills d'agents (PR-to-video, captions, explainers).
- Cible : devs, marketing technique, agents de contenu. Pricing : gratuit ; sert de top-of-funnel à HeyGen.

**3. Stack**
- TypeScript, Bun, Node 22, FFmpeg, Puppeteer/headless Chrome, adaptateurs GSAP/Lottie/Three.js, rendu AWS Lambda.

**4. Psychologie**
- Triggers : autorité (marque HeyGen), simplicité (« c'est juste du HTML »), tendance agents.
- JTBD : « automatiser des vidéos produit sans éditeur vidéo ».
- Aha : un prompt à l'agent donne un MP4 propre.

**5. Go-to-market**
- Marque établie, skills installables dans les agents de code, catalogue de blocs réutilisables, adoption par projets connus (social proof).

**6. Réplication**
- Complexité 6/10 (rendu déterministe, perf). Dev : 6-10 semaines pour un clone minimal.
- Verticaux : vidéos de démos auto, rapports vidéo, shorts immobilier.
- Angle Kyle : couche SaaS « vidéo + voix off IA » au-dessus de HyperFrames et d'un TTS, pour PME francophones.

## 🏆 TOP APP #3 : AI Job Search (Claude Code)
**1. Identification**
- [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) — open-source (MIT), gratuit (nécessite abonnement/API Claude).
- Fondateur : Mads Lorentzen, géophysicien licencié en 2025, recasé en AI engineer (juin 2026). Date de launch non confirmée.
- Buzz : ~57,9k stars, 18,3k forks (ratio de forks très élevé = usage réel) ; ~9k stars/semaine.

**2. Proposition de valeur**
- Problème : candidatures répétitives, CV non adaptés, suivi chaotique.
- Solution : commandes /setup, /scrape, /rank, /apply, /interview : scoring d'offres, CV et lettre LaTeX, relecture par agent critique, check ATS, sync Gmail/Notion.
- USP : workflow complet dans Claude Code, story fondateur authentique. Cible : chercheurs d'emploi tech. Pricing : gratuit.

**3. Stack**
- Claude Code (runtime agent), Python, Bun, LaTeX, MCP Notion, connecteur Gmail.

**4. Psychologie**
- Triggers : peur (marché de l'emploi), preuve sociale personnelle (« j'ai décroché un poste avec »), contrôle.
- JTBD : « obtenir plus d'entretiens avec moins d'effort ». Aha : CV adapté + PDF validé en une commande.

**5. Go-to-market**
- Histoire fondateur partagée, viralité via forks, niche saturée de douleur. Pas de monétisation.

**6. Réplication**
- Complexité 3/10 : un pack de prompts/skills. Dev : 1-2 semaines.
- Verticaux : candidature en français (France Travail, APEC), freelances (missions), reconversions.
- Angle Kyle : SaaS grand public avec UI (la cible non-dev ne lance pas Claude Code) ; version vocale pour préparation d'entretien (mock interview voix).

## 💰 Unit Economics Deep Dive — VoiceStudio
⚠️ VoiceStudio est un projet open-source sans produit payant identifié : aucune donnée financière publique (Crunchbase/Tracxn/SimilarWeb non consultés). Les chiffres ci-dessous sont des **estimations de scénario**, pas des faits.

| Métrique | Estimation |
|---|---|
| ARR | ~0 à 50 K€ (sponsoring, dons) |
| Users | non mesurable ; installs probables en dizaines de milliers |
| ARPU | ~0 € (gratuit) |
| CAC | ~0 € (organique GitHub) |
| LTV, LTV/CAC, Payback | non applicables |
| Burn / Runway | quasi nul / illimité (solo, pas de salaires visibles) |
| Rev/Employee | non applicable |
| Rule of 40 | non applicable |

**Verdict santé : 🟡** — traction communautaire exceptionnelle, mais zéro monétisation démontrée. Risque : licence AGPL + poids de modèles sous licences séparées (usage commercial à vérifier) ; dépendance à un moteur tiers (OmniVoice).

**Lecture pour Kyle** : l'opportunité est le trou de monétisation. Un SaaS hébergé vertical, à ~29-99 €/mois, a un CAC faible si on s'appuie sur la notoriété du projet open-source. Vérifier la licence avant toute offre hébergée.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | VoiceStudio | HyperFrames | AI Job Search |
|---|---|---|---|
| 📊 Market Size (20%) | 8 | 7 | 7 |
| ⚙️ Complexité inversée (15%) | 5 | 5 | 8 |
| ⏱️ Time-to-Market (15%) | 5 | 5 | 8 |
| 🏟️ Compétition inversée (15%) | 3 | 5 | 4 |
| 💰 Revenue Potential (20%) | 7 | 6 | 5 |
| 🧑‍💻 Founder-Fit Kyle (15%) | 9 | 5 | 5 |
| **Score pondéré** | **6,3** | **5,6** | **6,1** |
| **Verdict** | 🟡 BUILD ADJACENT | 🟠 WATCH | 🟡 BUILD ADJACENT |

Calcul VoiceStudio : 1,6+0,75+0,75+0,45+1,4+1,35 = 6,3. HyperFrames : 1,4+0,75+0,75+0,75+1,2+0,75 = 5,6 (WATCH). AI Job Search : 1,4+1,2+1,2+0,6+1,0+0,75 = 6,15.
Scores honnêtes : la compétition voix est saturée (ElevenLabs, etc.) et la valeur repose sur l'angle vertical, pas sur le produit lui-même.

## 📈 Tendances Émergentes
- **Agents-first tooling** : MCP, skills et plugins dominent GitHub Trending ([claude-plugins-official](https://github.com/anthropics/claude-plugins-official), [cursor/plugins](https://github.com/cursor/plugins), [context-mode](https://github.com/mksglu/context-mode), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)).
- **Voix locale open-source** qui remplace les SaaS cloud (VoiceStudio).
- **Vidéo programmable pour agents** (HyperFrames, [artcraft](https://github.com/storytold/artcraft)).
- **Workflows verticaux packagés en skills** (job search, science) : une personne + Claude Code = produit viral.
- **Signal faible à surveiller** : [morluto/rea](https://github.com/morluto/rea) affiche ~201k stars sur la semaine, chiffre anormal (possible gonflage ou erreur de scrape) ; ne pas s'y fier sans vérification.

## 💡 Insights Actionnables
1. **Vérifier la licence de VoiceStudio/OmniVoice** (AGPL + poids séparés) avant tout SaaS hébergé ; si OK, prototyper un « doublage/voix-off FR » vertical en 2-3 semaines.
2. **Le goulot est l'installation locale** : le marché non technique paie pour du « ça marche dans le navigateur ».
3. **Packager un workflow en skills Claude Code** coûte 1-2 semaines et peut devenir viral (cas Job Search) ; idée : kit « voice agent » pour PME.
4. **Fiabiliser la veille** : PH/HN inaccessibles ce run ; prévoir une source alternative (flux RSS/API accessibles) pour couvrir les lancements SaaS non-open-source.
5. Aucun BUILD NOW cette semaine ; deux BUILD ADJACENT à approfondir.
