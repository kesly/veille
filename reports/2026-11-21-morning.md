# AI Watch — 2026-11-21 Matin

> Collecte : treg 3/4 sources (Product Hunt en 504), 15 recherches extended, GitHub Trending ok, 4 pages lues, 5 items confirmés par une deuxième source.

## 🔥 Breaking

### Preuve revendiquée de l'hypothèse de Riemann généralisée (GRH) avec Claude
- **Quoi** : Levent Alpöge (Anthropic), avec un modèle interne, publie une preuve Lean-only de la GRH (~17,4 M de lignes de Lean selon Aaronson). Même jour : preuves assistées par IA de blow-up en temps fini pour Euler 3D (version lisible) et Navier-Stokes 3D (Alpöge, Buckmaster, Coiculescu).
- **Date** : 2026-11-20
- **Lien** : https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/ ; https://scottaaronson.blog/?p=10344 ; https://alpo.ge/remark.pdf
- **Pourquoi c'est important** : si la vérification tient, c'est le résultat mathématique le plus marquant jamais obtenu avec une IA. Statut : NON vérifié. Pas de version lisible pour la GRH, vérification en cours (fil Lean Zulip). À traiter avec prudence.
- **Testable** : Non (preuve Lean à vérifier par la communauté)

### Anthropic entre au Nasdaq (ANT)
- **Quoi** : IPO à 83 $/action, ~81,3 Md$ levés (record), ouverture à 111,50 $, clôture ~97 $ le premier jour.
- **Date** : 2026-11-19
- **Lien** : https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html
- **Pourquoi c'est important** : plus grosse IPO de l'histoire ; valorisation 1,3 à 2 T$ selon le moment. Chiffres variables selon les sources.
- **Testable** : Non

### Inkling 2 Mini (Thinking Machines) — open weights, looped transformer
- **Quoi** : MoE 26,4B (3,4B actifs), couches centrales exécutées 3 fois par token, Apache 2.0, 1M de contexte, texte+image. 48,2 % DeepSWE v1.1, meilleur modèle open <100B selon le labo.
- **Date** : 2026-11-20
- **Lien** : https://thinkingmachines.ai/news/inkling-2-mini/
- **Pourquoi c'est important** : architecture bouclée qui raisonne plus avec moins de tokens ; tourne en local (Mac 32 Go via Ollama, DGX Spark, ~200 tok/s sur RTX 4090 avec vLLM selon Reddit).
- **Testable** : Oui — open source, Ollama, Hugging Face, Tinker, OpenRouter.

## 🆕 Nouveaux Outils & Produits

### Gemini : computer use sur Mac
- **Quoi** : l'app Gemini pour macOS pilote apps natives et sites en arrière-plan, avec validation des actions.
- **Date** : 2026-11-19
- **Lien** : https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/
- **Pourquoi c'est important** : agent desktop grand public chez Google.
- **Testable** : Oui — abonnement Google AI Plus/Pro/Ultra (payant).

### DreamCoder (harness/IDE de code)
- **Quoi** : harness de codage et IDE par l'auteur de Mastering Emacs.
- **Date** : 2026-11-20 (HN, 142 pts)
- **Lien** : https://www.masteringemacs.org/article/announcing-dreamcoder
- **Pourquoi c'est important** : nouvel entrant côté éditeurs/agents ; source unique, à surveiller.
- **Testable** : Oui — voir la page.

### OpenComputer (alternative open source à Devin)
- **Quoi** : agent de dev open source (Show HN).
- **Date** : 2026-11-20
- **Lien** : https://github.com/diggerhq/opencomputer
- **Pourquoi c'est important** : agent autonome auto-hébergeable.
- **Testable** : Oui — open source.

### ChatGPT : Live Dictation et GPT-Live-1.1 (API)
- **Quoi** : dictée en direct sans limite de 10 min ; GPT-Live-1.1 pour agents vocaux multilingues.
- **Date** : 2026-11-20 (sources secondaires + forum OpenAI)
- **Lien** : https://community.openai.com/c/announcements/6
- **Pourquoi c'est important** : voice AI.
- **Testable** : Oui — ChatGPT / API (payant).

### GitHub Trending (open source)
- Claude-BugHunter (skills Claude Code, +1622★), obra/superpowers, firecrawl/firecrawl (API web pour agents), HKUDS/CLI-Anything, minimind (LLM 64M en 2h), last30days-skill, opensre, autoclip. Tendance : écosystème de « skills » pour agents de code. Lien : https://github.com/trending?since=daily

## 🧠 Mises à jour de Modèles

### Gemini 4 Neon (Google)
- **Quoi** : modèle entre Hydrogen et Carbon, 1M de contexte, ~3 $/15 $ par M tokens (une source), benchmarks Google : Terminal-Bench Science 70,5 %, HLE-Diamond 71,3 %.
- **Date** : 2026-11-18
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
- **Pourquoi c'est important** : 4e modèle Gemini en un mois (cadence rapide). Benchmarks non indépendants.
- **Testable** : Oui — AI Studio, app Gemini Pro/Ultra, Antigravity.

### Tencent Hy4 flash
- **Quoi** : MoE ~224B (~12B actifs), multimodal, 1M contexte, open weights, ~0,07 $/M tokens en entrée ; Tencent le dit proche de Claude Haiku 5.5 à 1/18 du coût (chiffres internes).
- **Date** : 2026-11-16 (poids ouverts ~17)
- **Lien** : https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows/
- **Pourquoi c'est important** : pression sur les prix des petits modèles. AMA Reddit r/LocalLLaMA (270 pts).
- **Testable** : Oui — Hugging Face, TokenHub (−50 % jusqu'au 30/11).

### Hors fenêtre 72 h : Microsoft MAI Code 2 (17/11, Ignite) — voir À surveiller.

## 🔬 Research

### Language Models Can Rewrite Their Own Weights
- **Quoi** : un modèle open 27B réécrit ses propres poids sans gradient (+6,6 pts sur problèmes inédits, amélioration sur 8 sessions), capacité émergente avec l'échelle.
- **Date** : arXiv 2026-11-16 (v2 le 18)
- **Lien** : https://arxiv.org/abs/2611.21885
- **Pourquoi c'est important** : pas vers l'auto-amélioration récursive ; résultat d'un seul papier, non répliqué.
- **Testable** : Non

### Show HN : audio-to-MIDI 60x plus efficace (Dettato)
- **Lien** : https://kobi.music/research/dettato — 254 pts HN, source unique.

## 📝 À surveiller
- **Vérification de la GRH** : suivre le fil Lean Zulip et les réactions d'experts. Anthropic aurait dit ne pas s'attendre à ce que ces techniques mènent à une preuve complète (source secondaire).
- **Signal : restriction des agents IA sur les OS mobiles** (Signal, 527 pts HN) : https://signal.org/blog/protecting-your-privacy/
- **Microsoft MAI Code 2 / MAI Cyber 2 Flash** (Ignite, 17/11), cyber en déploiement en décembre.
- **Rumeurs/infos à source unique** : fuite de données de l'agent Meta Muse ; Apple développe un agent contrôlant l'ordinateur ; Nvidia stoppe les livraisons de puces vers la Chine ; enquête SEC sur Nvidia (comptabilité, HN 258 pts).
- **Mistral** : Deutsche Telekom T.Capital investit 100 M€ (20/11) ; Large 4 aux poids ouverts (digest du 9/11, à vérifier).
- **Zyphra ZONOS3-Mini** : TTS open-weight avec clonage de voix (12/11, source unique).
- **OpenAI** : GPT-6.2 Astra/Sol (17/11, source Newegg unique), objectif d'un chercheur automatisé d'ici mars 2028, Performance Factory (Codex).
- **ICLR 2027** : suppression de reviews générées par IA et desk rejections (Reddit).
- **CodeRabbit Verify** en bêta publique (18/11).

## 📊 Résumé
- **Top 3 du jour** : 1) Preuve GRH revendiquée avec Claude (à vérifier), 2) IPO Anthropic au Nasdaq, 3) Inkling 2 Mini open weights.
- **À tester en priorité** : Inkling 2 Mini (Ollama/HF, Apache 2.0), Hy4 flash (open weights), Gemini 4 Neon (AI Studio), OpenComputer (open source).
