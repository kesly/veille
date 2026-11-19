# AI Watch — 2026-11-19 Matin

> Collecte : treg 4/4 sources, 16 recherches extended, GitHub Trending ok, 2 pages lues (Gemini 4 Neon, Energy-Based Reasoners), 8 items confirmés par une deuxième source.

## 🔥 Breaking

### Gemini 4 Neon (Google)
- **Quoi** : nouveau modèle de la famille Gemini 4 (entre Hydrogen et Carbon), contexte 1M tokens, 4 niveaux de réflexion, orienté coding, travail de bureau et science.
- **Date** : 2026-11-18
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ (confirmé par 9to5Google, VentureBeat, TestingCatalog)
- **Pourquoi c'est important** : #3 sur l'Artificial Analysis Intelligence Index (61, niveau xhigh) et #2 sur le Vals Index (70,9 %) selon Google ; décrit comme niveau Opus 5.5 en coding. API à 3 $ / 15 $ par M tokens (tarif de lancement, 4 $ / 20 $ ensuite selon un média). Classements cités par Google lui-même, à nuancer.
- **Testable** : Oui — API Gemini (AI Studio, payant), app Gemini (Pro/Ultra), Antigravity.

### Anthropic fixe le prix de son IPO
- **Quoi** : introduction en bourse à 83 $/action (fourchette initiale 70-78 $), valorisation d'environ 1 500 Md$, cotation prévue le 19 nov au Nasdaq, ticker « ANT ».
- **Date** : 2026-11-18
- **Lien** : https://www.anthropic.com/news/anthropic-prices-initial-public-offering (Washington Post, CNBC, Bloomberg)
- **Pourquoi c'est important** : plus grosse IPO IA à ce jour ; référence de valorisation pour tout le secteur. Taille finale de l'offre et valorisation exacte non confirmées officiellement dans les recherches.
- **Testable** : Non.

### Genie 4 / Project Genie (Google DeepMind)
- **Quoi** : modèle de monde temps réel : édition de l'environnement en session par texte, audio et dialogues natifs ; agent Project Genie pour co-créer des mondes ; galerie communautaire.
- **Date** : 2026-11-18
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/
- **Pourquoi c'est important** : premier modèle de monde interactif grand public avec audio ; pas d'API pour l'instant (partenaires précoces annoncés, sans date).
- **Testable** : Oui — abonnés Google AI Ultra ; liste d'attente pour Pro. Payant.

## 🆕 Nouveaux Outils & Produits

### Sept modèles MAI (Microsoft, Ignite)
- **Quoi** : MAI Code 2 / Code 2 Flash, MAI Cyber 2 Flash, MAI Image 2.7, MAI Realtime 1 (speech-to-speech, dès 0,01 $/min audio), transcription Dragon/MAI, Decision 1.1 ; licences « MAI Licensed Weights » pour personnaliser sur Azure.
- **Date** : 2026-11-17 (la liste exacte varie selon les médias)
- **Lien** : https://microsoft.ai/news/microsoft-ignite-2026/ (TestingCatalog, Neowin)
- **Pourquoi c'est important** : Microsoft pousse ses propres modèles bon marché face à OpenAI/Anthropic. Chiffres de performance fournis par Microsoft uniquement.
- **Testable** : Oui — Code 2 dans GitHub Copilot, Image 2.7 en préview sur Foundry. Payant.

### Mistral Vibe Desktop
- **Quoi** : app desktop macOS/Windows pour lancer plusieurs agents de code en parallèle (git worktrees), local ou sandbox cloud, revue de code et suivi de PR.
- **Date** : ~2026-11-17
- **Lien** : https://docs.mistral.ai/vibe/code/desktop/overview (The Decoder, TestingCatalog)
- **Pourquoi c'est important** : Mistral rattrape Codex/Claude Code côté desktop ; Linux prévu. Offre Pro gratuite en Europe selon un média.
- **Testable** : Oui — téléchargement Mistral Vibe.

### Inworld Voice Isolator (open source)
- **Quoi** : modèle de débruitage/isolation de voix 48 kHz, deux checkpoints (offline et temps réel, 20 ms de look-ahead), licence Apache 2.0.
- **Date** : ~2026-11-17/18
- **Lien** : https://huggingface.co/inworld/voice-isolator (blog Inworld ; 350 pts sur r/LocalLLaMA)
- **Pourquoi c'est important** : brique utile pour agents vocaux, gratuite.
- **Testable** : Oui — Hugging Face.

### Devin Bots, GPT-6.2 Astra/Sol, Qwen4-Max
- Déjà couverts hier (Devin Bots, GPT-6.2) ; Qwen4-Max (Alibaba, 16 nov, fermé, 2,4T MoE, 1M contexte, ~1,50 $ / 4,50 $ par M tokens) en seconde source MarkTechPost/DataCamp. Lien : https://www.marktechpost.com/2026/11/16/alibaba-qwen4-max-release/

## 🧠 Mises à jour de Modèles

### Tencent Hy4 flash
- **Quoi** : modèle multimodal MoE (~224B total, 12B actifs), contexte 1M, ~0,07 $/M tokens en entrée ; revendique le niveau de Claude Haiku 5.5 à bien moindre coût.
- **Date** : 2026-11-16
- **Lien** : https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows/
- **Pourquoi c'est important** : très bas prix ; statut open-weight contradictoire selon les sources (MLQ dit déjà sur Hugging Face, d'autres « prévu »). AMA r/LocalLLaMA vendredi 20 nov, 8-10h PST.
- **Testable** : Oui — Tencent Cloud TokenHub, OpenRouter bientôt. Payant, remise 50 %.

## 🔬 Research

### Energy-Based Reasoners (EBR)
- **Quoi** : modèles de raisonnement récurrents guidés par une énergie apprise ; 99,9 % sur Sudoku-Extreme avec 1,8M de paramètres.
- **Date** : arXiv 2611.08977, HN le 2026-11-18
- **Lien** : https://energy-based-reasoners.github.io/ (arXiv https://arxiv.org/abs/2611.08977)
- **Pourquoi c'est important** : le titre HN dit 385×, la page et l'abstract disent 345× moins de calcul que le meilleur modèle suivant : retenir 345×. Limité à des benchmarks algorithmiques, pas aux LLM généralistes.
- **Testable** : Non (code/papier uniquement).

## 📝 À surveiller
- **Palo Alto Networks rachète Applied Compute** (post-training/inférence de modèles open-weight), 4,5 Md$ en actions, annoncé le 18 nov, clôture prévue FQ3 2027 (SecurityWeek, Bloomberg).
- **Agent Arena Index** (Arena, 18 nov) : nouvel indice d'évaluation des agents, cité par Google pour Neon.
- **Rapport GAO** : des modèles (Claude, Grok, ChatGPT, Gemini) auraient aidé à planifier des attaques en moins de 12 h malgré les garde-fous (digest, source unique, non vérifié).
- **Genie 4 via API** et **open-weight Qwen4 plus petits** : annoncés sans date.
- Resserrement des contrôles d'export de puces IA (Singapour, Thaïlande, Malaisie) : source unique.
- Mistral : levée de 3 Md€ (Série D), valorisation > 21 Md€ : à confirmer.
- Reddit : « They're going to go after open weight models » (r/LocalLLaMA, 149 pts), débat réglementaire.

## 🆕 GitHub Trending (open source)
- google-research/paper-orchestra (multi-agent pour rédiger des papiers, +1 524 ★), affaan-m/ECC (harness agents), mvanhorn/last30days-skill, obra/superpowers, HKUDS/CLI-Anything, google-labs-code/stitch-skills, NVIDIA/SkillEvaluator, cursor/plugins.
- Product Hunt : S.Space (337 votes, espace de travail pour agents), Bluedot Phone Calls, Incredible Agents (voix IA), AssemblyAI-STT-3.7, uRun.

## 📊 Résumé
- **Top 3 du jour** : Gemini 4 Neon ; IPO Anthropic à 83 $ ; Genie 4 (avec les sept modèles MAI de Microsoft juste derrière).
- **À tester en priorité** : Gemini 4 Neon (API AI Studio), Mistral Vibe Desktop, Inworld Voice Isolator (Apache 2.0), Tencent Hy4 flash (TokenHub, remise 50 %).
