# AI Watch — 2026-11-23 Matin

> Collecte : treg 4/4 sources, 17 recherches extended, GitHub Trending ok, 4 pages lues, 5 items confirmés par une deuxième source.

## 🔥 Breaking

### Preuve de l'hypothèse de Riemann assistée par Claude (Levent Alpöge, Anthropic), certifiée en Lean
- **Quoi** : Alpöge (Anthropic) publie le 20/11 une note de 4 pages et une bibliothèque Lean de ~17 M de lignes, trouvée avec Claude en ~41 jours. Le 21/11, Lean FRO et Mathlib Initiative certifient dans un communiqué commun que l'énoncé est bien celui de Mathlib et que la preuve compile (plusieurs vérificateurs indépendants, comparator et con-leche).
- **Date** : 20-21 novembre 2026
- **Lien** : https://www.quantamagazine.org/updates/transformation/ · https://officechai.com/ai/lean-community-certifies-levent-alpoges-claude-assisted-proof-of-the-riemann-hypothesis-as-correct/ · https://cryptoslate.com/claude-assisted-proof-of-riemann-hypothesis-validated-by-independent-checkers/
- **Pourquoi c'est important** : si les idées mathématiques se confirment, c'est le premier problème du Millénaire résolu avec une IA. Réserves : la certification porte sur le code formel, pas sur la compréhension humaine de la preuve. Clay n'a pas encore statué (le prix reste « ouvert » au moment des articles). Un chiffre « 41,6 % → 67,2 % » circule, non confirmé. Une preuve humaine concurrente (Masullo, GRH) existe, non formalisée ; des doutes ont été signalés sur son théorème 12.5.1.1.
- **Testable** : Oui — dépôts Lean de formalisation de Masullo : https://github.com/mccorvie/riemann-masullo (en cours). Treemap de la preuve : https://pengowray.github.io/riemann-zeta-proof-visualizer/

### OpenAI — « Perplexity and Intelligence » (Jakub Pachocki)
- **Quoi** : essai du chef scientist d'OpenAI proposant la perplexité (cross-entropy) comme métrique commune entre développeurs et base de standards de sécurité partagés ; OpenAI publie ses mesures internes de pretraining depuis GPT-3.5.
- **Date** : 22 novembre 2026
- **Lien** : https://openai.com/index/perplexity-and-intelligence/ (521 pts HN) · https://cryptobriefing.com/openai-pachocki-perplexity-ai-benchmark/
- **Pourquoi c'est important** : OpenAI s'expose à ses concurrents pour appuyer l'idée de limites de développement partagées liées à des jalons de compréhension. Un article d'Emergent.sh parle d'un « framework » outillé : non confirmé, il s'agit d'un essai.
- **Testable** : Non (publication de recherche/politique).

### Krach IA sur les marchés : Nasdaq −10 % sur la semaine, Nvidia ~−23 %, Anthropic −8,5 % le lendemain de son IPO
- **Quoi** : pire semaine du Nasdaq depuis 2020 sur fond de doutes sur le financement et le rythme des investissements datacenters ; Nvidia perd ~2,6 Md$ de capitalisation malgré des résultats record. Anthropic a fixé son IPO à 83 $ (valorisation d'au moins 1 500 Md$ selon les sources) puis a reculé de 8,5 % vendredi.
- **Date** : 16-21 novembre 2026
- **Lien** : https://tastylive.substack.com/p/the-weekly-recap-the-ai-rout-went · https://www.npr.org/2026/11/21/nx-s1-6048678/anthropic-ipo-mission-ai-safety
- **Pourquoi c'est important** : change le contexte de financement des labs et startups IA. Les chiffres exacts varient selon les indices et les sources.
- **Testable** : Non.

## 🆕 Nouveaux Outils & Produits

### Localcode
- **Quoi** : agent de code open source qui tourne en local sur Mac « en une commande ».
- **Date** : 22-23 novembre 2026 (Show HN, 37 pts)
- **Lien** : https://github.com/mjwsolo/localcode
- **Pourquoi c'est important** : alternative locale aux agents cloud, dans un contexte de coûts et de limites d'usage. Peu de signal pour l'instant (une seule source).
- **Testable** : Oui — open source, installation en une commande.

### Omi CLI, TeaserKit, Ulika, Webless Agents (Product Hunt)
- **Quoi** : Omi CLI (agents de code qui travaillent en votre absence, 93 votes) ; TeaserKit (votre agent de code réalise votre vidéo de lancement, 75) ; Ulika (éditeur visuel pour sites générés avec Claude/Cursor/Codex, 90) ; Webless Agents (agents face client, 112). Tines (401 votes) positionne une plateforme sécurisée pour agents, apps et automatisations.
- **Date** : 23 novembre 2026
- **Lien** : https://www.producthunt.com/products/omi-cli · https://www.producthunt.com/products/teaserkit · https://www.producthunt.com/products/ulika · https://www.producthunt.com/products/tines
- **Pourquoi c'est important** : confirme la tendance « agents autonomes + outillage autour de Claude Code/Codex ». Descriptions non vérifiées au-delà de la fiche PH ; modèles tarifaires non relevés.
- **Testable** : Oui — via les pages Product Hunt.

### Open source trending GitHub (agents, skills)
- **Quoi** : obra/superpowers (framework de skills, ~788 ★/jour), HKUDS/CLI-Anything (rendre les logiciels pilotables par agents, ~699), firecrawl/firecrawl (API recherche/scrape pour agents, ~915), mvanhorn/last30days-skill (~668), google-labs-code/stitch-skills (~494), cursor/plugins (~294), Tracer-Cloud/opensre (agent fiabilité CI/CD), minimind (LLM 64M entraîné en ~2 h, ~473). Le premier du jour, elementalsouls/Claude-BugHunter (~1 716 ★), est un bundle de skills Claude Code pour chasse aux bugs/red team : à manipuler avec prudence.
- **Date** : 23 novembre 2026 (GitHub Trending daily)
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : les « agent skills » sont le motif dominant du trending.
- **Testable** : Oui — open source (licences non vérifiées).

## 🧠 Mises à jour de Modèles

### Gemini 4 Neon (Google)
- **Quoi** : modèle intermédiaire de la famille Gemini 4, 1 M de contexte, ~3 $/15 $ par M de tokens ; score Artificial Analysis Index 61 contre 59 (Claude Opus 5.5) et 57 (GPT-6.2 Sol) selon les chiffres de lancement. Modèle par défaut dans Gemini (AI Pro/Ultra/Enterprise).
- **Date** : 18-19 novembre 2026 (les sources divergent d'un jour) — hors fenêtre 72 h strict, gardé car confirmé par deux sources
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ · https://www.analyticsvidhya.com/blog/2026/11/gemini-4-neon-review/
- **Pourquoi c'est important** : Google revendique la tête sur l'indice, mais les benchmarks sont surtout internes et les résultats de coding varient selon le harnais.
- **Testable** : Oui — payant (API et abonnements).

### Gemini : contrôle du Mac (computer use)
- **Quoi** : l'app Gemini pour macOS peut piloter des apps natives et naviguer en arrière-plan ; États-Unis, anglais, abonnés AI Plus/Pro/Ultra.
- **Date** : 19 novembre 2026
- **Lien** : https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/
- **Pourquoi c'est important** : rejoint les agents « computer use » concurrents. Source unique (TechCrunch).
- **Testable** : Oui — payant, US.

### Qwen3 TTS sur Together AI ; Google AI Edge Gallery (ASR/TTS hors ligne)
- **Quoi** : Qwen3 TTS (open-weight) en serverless, 9 voix, 10 langues, ~97 ms de latence au premier audio, 20 $/M de caractères. Google ajoute ASR et TTS embarqués hors ligne à AI Edge Gallery.
- **Date** : 20 novembre 2026
- **Lien** : https://futurumgroup.com/insights/together-ai-brings-real-time-voice-to-its-open-inference-stack/ · https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/
- **Pourquoi c'est important** : voix temps réel bon marché et locale. Chiffres issus des annonces.
- **Testable** : Oui — Together (payant), Qwen3 TTS open-weight.

### Image / vidéo
RAS dans la fenêtre 72 h (dernières sorties : GPT Image 2.6 le 4/11, Seedream 5.5 le 9/11, MiniMax-H3-Image le 11/11 — hors fenêtre).

## 🔬 Research

### Harvard CS 2881R — AI Safety / agent swarm sur P vs NP
- **Quoi** : séminaire de théorie ML en libre accès (55 pts HN) ; un « agent swarm » qui tente P vs NP (pequalnp.com, 128 pts) est surtout un projet de démonstration. Un jeu Show HN où l'on joue le sous-agent d'un LLM (286 pts).
- **Date** : 22-23 novembre 2026
- **Lien** : https://boazbk.github.io/mltheoryseminar/ · https://pequalnp.com/ · https://github.com/gulivan/worker755
- **Pourquoi c'est important** : faible, signal de culture plus que de résultats.
- **Testable** : Oui — pages en ligne.

## 📝 À surveiller
- **Amazon / Decart (~7,5 Md$)** : le FT (21/11) rapporte des discussions avancées, pas de deal annoncé ; Decart optimise l'exécution des modèles sur Trainium. Annonce possible cette semaine ou la suivante. https://www.pymnts.com/news/artificial-intelligence/2026/amazon-nears-7-5-billion-purchase-of-ai-startup-decart/
- **Cognition (Devin Bots), Replit Missions, OpenCode Browse** (≈17/11) : agents persistants et essaims à budget fixe ; sources agrégateurs uniquement. https://aiagentstore.ai/ai-agent-news/this-week
- **Modèles « récents » cités par les trackers mais non recoupés** : GPT-6.2 Sol/Astra (17/11), Kimi K3.1 Pro Prime (20/11, date et nom non confirmés ; les poids de K3.1 Pro ont été publiés ~4/11, 2,8 T de paramètres, licence propre non Apache). https://www.morphllm.com/kimi-k3-1
- **Sécurité** : rapport d'un acteur lié à la Chine utilisant des agents autonomes sur une 0-day dans MONAI Label (root en ~11 min) ; source de type digest, non vérifiée. https://riorundown.substack.com/p/ai-news-nov-22-2026-autonomous-systems
- **Anthropic** : évaluation METR (capacités ×2 en vitesse) et résultats de test de Claude Opus 5.5 sur un scénario de ciblage ; relayé par des newsletters uniquement.
- **Local AI** : guide Unsloth + Qwen/Inkling (326 pts HN) ; thread Reddit LocalLLaMA demandant d'indiquer le quant utilisé quand on annonce des perfs. https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth
- **X** : les posts viraux « fabrique à Shorts avec Opus 5.5 » ou « 12 repos pour agence IA » relèvent du marketing, ignorés.

## 📊 Résumé
- **Top 3 du jour** : 1) Preuve de Riemann assistée par Claude, certifiée en Lean (vérification formelle faite, compréhension mathématique à venir) ; 2) Essai de Pachocki (OpenAI) pour une métrique et des limites partagées ; 3) Rout boursier de l'IA (Nasdaq −10 %, Nvidia −23 %, Anthropic −8,5 %).
- **À tester en priorité** : Gemini 4 Neon (API/app), Localcode (open source, Mac), Qwen3 TTS (Together AI), repos trending obra/superpowers et firecrawl.
