# 🔥 Market Scan — 2026-10-21

> ⚠️ Limites de la collecte : Product Hunt, Hacker News et Algolia étaient inaccessibles (réseau bloqué) ; la recherche web n'a renvoyé aucun classement d'octobre 2026. Seule source fiable : GitHub Trending (hebdo) + pages de repos. Dates de création non vérifiées. Les scores sont donc à prendre avec prudence.

## 📊 Résumé Exécutif
- Apps analysées : 3 (tous open-source, issus de GitHub Trending)
- Top potentiel : VoiceStudio (voice AI local, fit direct avec Kyle)
- Opportunités immédiates (BUILD NOW) : 0 (1 BUILD ADJACENT)

## 🏆 TOP APP #1 : VoiceStudio
**1. Identification** — [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) · open-source (AGPL-3.0) · catégorie voice AI · date de lancement non vérifiée · fondateur : debpalash (dev individuel/petite équipe). Buzz : 79,3k stars, 8,7k forks, ~17k stars sur la semaine dans [GitHub Trending](https://github.com/trending?since=weekly).

**2. Proposition de valeur** — Problème : cloner/doubler/transcrire des voix coûte cher en SaaS (ElevenLabs) et envoie les données dans le cloud. Solution : suite locale (clonage, voice design, doublage vidéo, dictée, transcription, audiobooks, 646 langues). USP : local-first + gratuit + API/MCP pour agents. Cible : créateurs, devs, studios. Pricing : gratuit (poids des modèles avec conditions propres).

**3. Stack** — Python/PyTorch (backend), Electron + Bun (desktop/web), CUDA/Metal/MLX, Docker, apps iOS/Android en preview. Moteur par défaut : k2-fsa/OmniVoice, moteurs interchangeables.

**4. Psychologie** — Triggers : gratuité vs abonnement, vie privée, "646 langues" (effet d'ampleur), FOMO sur la voix IA. JTBD : « doubler/cloner une voix sans payer ni envoyer mes données ». Aha moment : première voix clonée en local en une commande d'install.

**5. Go-to-market** — GitHub Trending + stars, install en une ligne, positionnement anti-SaaS, intégration MCP (surf sur la vague agents). Boucle virale : contenus générés partagés, forks.

**6. Réplication** — Complexité 6/10 (gros assemblage de modèles open-source, UX difficile à rendre propre). Verticaux adjacents : doublage pour e-learning, voicebots téléphoniques FR, accessibilité. Angle Kyle : version hébergée/managée orientée voice agents francophones (latence, RGPD, hébergement UE). Temps de dev MVP : 4–8 semaines.

## 🏆 TOP APP #2 : HyperFrames (HeyGen)
**1. Identification** — [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) · open-source (Apache 2.0) · vidéo programmatique pour agents · soutenu par HeyGen (société établie) · 68,6k stars, 6,2k forks, ~6k stars/semaine. Date de lancement non vérifiée.

**2. Proposition de valeur** — Problème : produire de la vidéo via code est lourd (Remotion = React + build). Solution : écrire du HTML/CSS avec attributs de timing, rendu MP4 déterministe. USP : « HTML-first », pensé pour que les agents (Claude Code, Codex, Cursor) génèrent la vidéo ; ~21 skills fournis. Cible : devs, marketeurs, agents. Pricing : gratuit ; monétisation probable via le cloud HeyGen.

**3. Stack** — TypeScript, Puppeteer/headless Chrome, FFmpeg, GSAP/Lottie/Three.js, rendu distribué AWS Lambda, Node 22+.

**4. Psychologie** — Triggers : autorité (marque HeyGen), tendance agents, simplicité (« pas de React »). JTBD : « faire une vidéo par prompt, reproductible ». Aha : un prompt à l'agent produit un MP4 propre.

**5. Go-to-market** — Distribution via l'écosystème de skills agents, comparaison directe avec Remotion, catalogue de blocs réutilisables, GitHub Trending.

**6. Réplication** — Complexité 5/10 pour un wrapper SaaS, 8/10 pour le moteur. Verticaux : vidéos de démo produit, reporting vidéo, shorts automatisés avec voix off. Angle Kyle : brancher voix IA + HyperFrames pour des vidéos narrées automatiquement (SaaS « vidéo de release notes »). Temps de dev : 3–6 semaines pour un wrapper.

## 🏆 TOP APP #3 : ai-job-search
**1. Identification** — [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) · open-source (MIT) · framework de recherche d'emploi sur Claude Code · 61,2k stars, 19k forks (ratio de forks très élevé), ~12,8k stars/semaine. Fondateur : Mads Lorentzen. Date de lancement non vérifiée.

**2. Proposition de valeur** — Problème : candidatures répétitives et peu personnalisées. Solution : commandes `/setup`, `/scrape`, `/rank`, `/apply` (CV + lettre LaTeX relus par un 2e agent), `/interview`, sync Gmail/Notion. USP : tout est local, forké dans un repo privé. Cible : candidats tech. Pricing : gratuit (coût = abonnement Claude de l'utilisateur).

**3. Stack** — Claude Code (commandes/skills), Python 3.10+, Bun, LaTeX, CLIs de portails d'emploi (Danemark au départ).

**4. Psychologie** — Triggers : anxiété de l'emploi, gain de temps, preuve sociale (forks). JTBD : « décrocher des entretiens sans y passer mes soirées ». Aha : un CV adapté à une annonce en quelques minutes.

**5. Go-to-market** — Contenu LinkedIn/X sur la recherche d'emploi, fork-and-run, partage de résultats. Le modèle « repo comme produit » se propage par forks.

**6. Réplication** — Complexité 3/10 (prompts + scripts). Verticaux : freelances (appels d'offres), immobilier, levée de fonds, marchés publics. Angle Kyle : version SaaS non-tech avec UI, sources FR (France Travail, Welcome to the Jungle), aucun terminal requis. Temps de dev : 2–4 semaines. Risque : scraping de portails, CGU.

## 💰 Unit Economics Deep Dive — VoiceStudio
VoiceStudio est un projet open-source sans entité commerciale identifiée : les unit economics sont **non applicables en l'état** ; ci-dessous, une estimation pour un SaaS qui monétiserait cette traction (hypothèses, aucune donnée publique).

| Métrique | Estimation |
|---|---|
| ARR | 0 € aujourd'hui (potentiel 300–600 k€ à 12 mois si hébergé) |
| ARPU | ~15 €/mois (créateurs) |
| Users | non publics (stars ≠ users) |
| CAC | ~0–10 € (acquisition organique GitHub) |
| LTV | ~150 € (churn ~10 %/mois) |
| LTV/CAC | >10 (si CAC organique tient) |
| Payback | <1 mois |
| Burn / Runway | inconnus (projet communautaire) |
| Rev/Employee | n/a |
| Rule of 40 | n/a |

Verdict : 🟡 — forte traction, aucun revenu vérifié ; risque : coût GPU d'une version hébergée, licence AGPL et conditions des poids de modèles. Sources : [GitHub](https://github.com/debpalash/VoiceStudio), estimations internes.

## 🎯 Opportunity Scorecard — Top 3
| App | Market (20%) | Complexité inv. (15%) | TTM (15%) | Concurrence inv. (15%) | Revenu (20%) | Fit Kyle (15%) | **Score** | Verdict |
|---|---|---|---|---|---|---|---|---|
| VoiceStudio | 8 | 4 | 5 | 3 | 6 | 9 | **5.9** | 🟠 WATCH |
| HyperFrames | 7 | 5 | 6 | 4 | 6 | 6 | **5.8** | 🟠 WATCH |
| ai-job-search | 6 | 8 | 8 | 4 | 5 | 4 | **5.8** | 🟠 WATCH |

Note : aucune des trois n'atteint 6,0. Le fit voix de Kyle fait de VoiceStudio la meilleure base, mais la concurrence (ElevenLabs, etc.) est très forte. Le « BUILD ADJACENT » viendrait d'un angle étroit (voicebots FR managés), pas du clone du produit.

## 📈 Tendances Émergentes
- **Skills/plugins pour agents comme canal de distribution** : HyperFrames (~21 skills), `anthropics/claude-plugins-official`, `scientific-agent-skills`, `context-mode`.
- **« Repo = produit »** : des workflows complets sur Claude Code (ai-job-search) forkés à grande échelle.
- **Voix IA locale et open-source** qui grignote les SaaS payants (VoiceStudio, 646 langues).
- **Vidéo générée par code/agents** (HyperFrames, artcraft).
- Signal faible : outils de reverse engineering pilotés par agents (morluto/rea en tête du trending, chiffres à prendre avec prudence).

## 💡 Insights Actionnables
1. **Tester un voicebot managé FR** (hébergement UE, latence, RGPD) en s'appuyant sur les moteurs open-source de VoiceStudio : validation en 1 semaine avec 5 prospects PME.
2. **Prototype « vidéo narrée automatique »** (HyperFrames + voix IA) pour release notes/démos SaaS : 2–3 semaines.
3. **Packager un workflow Claude Code vertical** (appels d'offres, recherche d'emploi FR) en SaaS no-code : le ratio forks/stars d'ai-job-search montre la demande.
4. **Publier des skills/MCP** pour l'écosystème agents comme canal d'acquisition à coût nul.
5. **Améliorer la veille** : prévoir un accès réseau à Product Hunt/HN, ce scan en manquait.
