# AI Watch — 2026-11-22 Matin

> Collecte : treg 4/4 sources, 14 recherches extended, GitHub Trending ok, 3 pages lues, 2 items confirmés par une deuxième source (Riemann/Lean, Inkling 2 Mini).

## 🔥 Breaking

### Preuve de l'hypothèse de Riemann (et GRH) par Levent Alpöge + Claude
- **Quoi** : Levent Alpöge (mathématicien chez Anthropic) publie, avec Claude, une preuve de l'hypothèse de Riemann et de la GRH, formalisée en Lean 4 (~17 M de lignes). La communauté Lean/Mathlib déclare « pleine confiance » dans sa correction après compilation indépendante et vérification par plusieurs checkers.
- **Date** : 20 nov. 2026 (certification Lean le 21 nov.)
- **Lien** : https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ — https://alpo.ge/remark.pdf — https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/
- **Pourquoi c'est important** : si confirmé, plus grand problème ouvert des mathématiques résolu avec une IA ; certification formelle = signal fort. À noter : un brouillon humain concurrent (Alessandro Masullo, Stanford) est sorti quelques heures plus tard, et l'examen par les pairs de l'argument mathématique n'est pas terminé. Le papier de Terry Tao du même jour (lien Euler/Navier-Stokes ↔ GRH) alimente le débat : https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/
- **Testable** : Oui — la bibliothèque Lean est publique, compilable avec Mathlib (gratuit, open source).

### Inkling 2 Mini (Thinking Machines) — modèle ouvert « looped transformer »
- **Quoi** : MoE 26,4B (3,4B actifs), couches centrales bouclées 3 fois ; tourne sur laptop (≈32 Go Mac / 5,4 Go en quant selon un repo HN). Revendique la tête des modèles ouverts <100B : DeepSWE v1.1 48,2 %, Vals Index v2.2 46,5 %. Une variante « variable-loop » sort pour la recherche.
- **Date** : 20 nov. 2026
- **Lien** : https://thinkingmachines.ai/news/inkling-2-mini/ — https://lmstudio.ai/models/inkling-2-mini
- **Pourquoi c'est important** : première architecture bouclée grand public en open weights, raisonne davantage avec moins de tokens ; étude de monitorabilité du CoT incluse. Benchmarks fournis par le labo (SWE-bench Verified 79,2 % cité par MarkTechPost, non confirmé ailleurs).
- **Testable** : Oui — Apache 2.0, poids sur Hugging Face, LM Studio, API Tinker.

## 🆕 Nouveaux Outils & Produits

### Claude Computer Use (bêta Team/Enterprise) + nouveau design mobile
- **Quoi** : Anthropic ajoute Computer Use en bêta aux plans Team/Enterprise et refond l'app mobile (source newsletter, non confirmée par seconde source).
- **Date** : ~21 nov. 2026
- **Lien** : https://riorundown.substack.com/p/ai-news-nov-21-2026-enterprise-infrastructure
- **Pourquoi c'est important** : agents desktop en entreprise.
- **Testable** : Oui si plan Team/Enterprise (payant).

### Gemini computer use sur Mac
- **Quoi** : Gemini pilote les apps Mac en arrière-plan (US, anglais, abonnés AI Plus/Pro/Ultra).
- **Date** : 19 nov. 2026
- **Lien** : https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/
- **Pourquoi c'est important** : course au computer use grand public.
- **Testable** : Oui (payant).

### Product Hunt : Exa Websets V2, Shipyard, AI Context Flow MCP, Stitch Loop
- **Quoi** : Exa Websets V2 (datasets web 4x plus rapides, 126 votes) ; Shipyard (MCP pour Claude/Cursor/Codex, 88) ; AI Context Flow MCP (mémoire partagée entre agents, 220) ; Stitch Loop (agent Google qui corrige et suit la métrique, 73).
- **Date** : 21-22 nov. 2026
- **Lien** : https://www.producthunt.com/products/exa-ai — https://www.producthunt.com/products/shipyard — https://www.producthunt.com/products/ai-context-flow — https://www.producthunt.com/products/stitch-loop
- **Pourquoi c'est important** : outillage MCP/agents en croissance continue.
- **Testable** : Oui (tarifs variables).

### GitHub Trending : outillage pour agents de code
- **Quoi** : obra/superpowers (+883 ★), HKUDS/CLI-Anything (+769), firecrawl/firecrawl (+1006), cathrynlavery/diagram-design (+583), mvanhorn/last30days-skill (+560), jingyaogong/minimind (+488), Claude-BugHunter (+1803, skill de bug hunting/red team). Open source.
- **Date** : 22 nov. 2026
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : les « skills » pour Claude Code/Cursor/Codex dominent le trending.
- **Testable** : Oui (open source, gratuit).

## 🧠 Mises à jour de Modèles

- **OpenAI GPT-6.2 Astra / Sol** (17 nov.) : API dès 2 $/10 $ (Sol) ; garde-fous cyber renforcés. https://casrai.org/news/openai-gpt-6-2-astra-sol-release-2026 (source unique, hors fenêtre 72 h)
- **Gemini 4 Neon** (18 nov.) : en tête d'un index d'agents de code selon un récap. Noms de modèles Google incohérents entre sources — à vérifier.
- **Kimi K3.1 Pro Prime** (Moonshot, 20 nov.) : listé par des trackers, non vérifié. https://llmgateway.io/timeline
- **Microsoft MAI Code 2 / Flash, MAI Realtime 1, MAI-Image-2.7-Flash** (17 nov.) : modèles de code moins chers, speech-to-speech et image. https://www.thedailystar.net/news/technology/news/microsoft-takes-openai-and-anthropic-cheaper-coding-ai-4327026

## 🔬 Research

- **Inkling 2 Mini variable-loop** : le no-CoT time horizon passe de 16 s à 37 s avec 3 boucles ; CoT plus court mais lisible. Voir lien ci-dessus.
- **« LLMs can read and write executables byte by byte from a hex dump »** (HN, 206 pts) : https://sgiannopoulos.github.io/blog/machine-code-programming/
- Sinon RAS.

## 📝 À surveiller

- **Vérification de Riemann** : revue par les pairs, comparaison avec le brouillon Masullo.
- **IPO Anthropic** : prix 83 $, ouverture ~111 $, clôture à 88,91 $ le 21 nov. selon la presse (chiffres divergents). https://www.japantimes.co.jp/business/2026/11/21/markets/anthropic-ai-stocks/
- **Sécurité** : chercheur Dragos — au moins 3 fournisseurs d'inférence IA compromis, prompts siphonnés (HN : OpenRouter « Data Processing Incidents on Inference Providers » https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) ; post Reddit sur un « agent swarm » ayant contourné la 2FA (non vérifié) ; RCE dans GnuPG (https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html).
- **Mistral** : Studio managed agents en preview, déploiement privé fin novembre.
- **Voice** : Zyphra ZONOS3-Mini TTS open-weight (12 nov.), ElevenLabs Scribe v3 Live (10 nov.) — hors fenêtre. Rien de neuf aujourd'hui.
- **Image/Vidéo** : roundup du 21 nov. : aucun nouveau modèle de base cette semaine.
- Pandex (droit européen via MCP) : https://www.pandex.io/

## 📊 Résumé
- **Top 3 du jour** : 1) Preuve Lean de Riemann par Alpöge + Claude ; 2) Inkling 2 Mini open weights bouclé ; 3) Computer use chez Google et Anthropic (Mac / Team-Enterprise).
- **À tester en priorité** : Inkling 2 Mini (LM Studio/HF), skills trending (superpowers, CLI-Anything), Exa Websets V2.
