# AI Watch — 2026-11-14 Matin

> Collecte : treg 4/4 sources, 18 recherches extended, GitHub Trending ok, 4 pages lues, 7 items confirmés par une deuxième source.

## 🔥 Breaking

### llama.cpp et ggml v1.0.0
- **Quoi** : Les deux bibliothèques passent en v1.0.0 avec semver strict (majeur = rupture d'API/ABI C), 35 fonctions dépréciées supprimées, support FP8 pour le KV cache (selon la presse).
- **Date** : 2026-11-13
- **Lien** : https://huggingface.co/blog/ggml-org/llama-cpp-v1 (source principale lue) ; https://github.com/ggml-org/ggml/releases/tag/v1.0.0
- **Pourquoi c'est important** : Stabilité de l'API pour tout l'écosystème IA locale (Ollama, apps downstream). Post Reddit r/LocalLLaMA à 1477 pts.
- **Testable** : Oui — open source, gratuit. Compiler llama.cpp v1.0.0 ou télécharger l'app macOS native annoncée.

### Gemini 4 Hydrogen (Google)
- **Quoi** : Modèle « daily driver » agentique, déployé dans Gemini app, Google Search, AI Studio, API et Antigravity (Pro/Ultra). Google annonce 51 sur l'Artificial Analysis Intelligence Index (54 en xhigh), devant Gemini 4 Argon (50). Nouveau « Orchestrator » dans Antigravity qui bascule entre Carbon et Hydrogen.
- **Date** : 2026-11-12 (page mise à jour le 13)
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
- **Pourquoi c'est important** : Frontière 4e génération mise à disposition de tous, tarif plat 1,50 $/7,50 $ par M tokens sur 1M de contexte. Benchmarks = déclarations de Google, non indépendantes.
- **Testable** : Oui — payant (API) / gratuit dans l'app Gemini et AI Studio. 129 votes sur Product Hunt.

### Claude Meetings (Anthropic), bêta
- **Quoi** : Claude rejoint les appels vidéo comme participant visible, répond dans le chat, rédige docs/whiteboards en direct, produit notes et actions. Google Meet uniquement pour l'instant.
- **Date** : 2026-11-10 à 12 (sources divergentes)
- **Lien** : https://claude.com/resources/articles/claude-meetings (lu) ; https://www.axios.com/2026/11/10/anthropic-claude-meetings-knowledge-work
- **Pourquoi c'est important** : Concurrence directe d'Otter, Fireflies, Granola, avec exécution d'actions via outils connectés. Indisponible en ZDR, HIPAA, CMEK.
- **Testable** : Oui, si plan Team/Enterprise (payant, déploiement progressif).

### Démission de Jensen Huang de Nvidia
- **Quoi** : Huang quitte ses postes de CEO, président et administrateur ; la CFO Colette Kress devient CEO par intérim, Harvey C. Jones président du conseil. Le FT rapporte une approche de Rene Haas (Arm).
- **Date** : 2026-11-12
- **Lien** : https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/ ; https://techcrunch.com/2026/11/12/nvidias-jensen-huang-resigns-chipmaker-names-cfo-colette-kress-as-interim-ceo/
- **Pourquoi c'est important** : Changement de direction du principal fournisseur de GPU IA, action en baisse. Les causes officielles ne sont pas données par Nvidia ; la presse évoque une affaire personnelle.
- **Testable** : Non.

## 🆕 Nouveaux Outils & Produits

### Perplexity Decider v1.3 et Flash v1.3
- **Quoi** : Modèles de décision (classifieur généraliste texte+vision) retournant des probabilités ; nouvelle fonction « locate » (NER, PII, QA extractive).
- **Date** : 2026-11-12
- **Lien** : https://www.perplexity.ai/hub/blog/perplexity-decider (lu)
- **Pourquoi c'est important** : Alternative légère aux LLM pour routage, modération, reranking. Chiffres (91,6 % sur 63 tâches internes) auto-déclarés.
- **Testable** : Oui — open weights Apache sur Hugging Face, OpenRouter (version gratuite), API Decisions (~0,02 $/M tokens).

### Render Sandboxes
- **Quoi** : Une machine dédiée par agent, démarrage en moins d'une seconde.
- **Date** : 2026-11-13 (Product Hunt, 265 votes)
- **Lien** : https://www.producthunt.com/products/render
- **Pourquoi c'est important** : Infra d'exécution pour agents. Pas de seconde source, annonce vendeur.
- **Testable** : Oui — payant.

### Filament by Galaxy
- **Quoi** : Outil open source pour déplacer des données depuis le terminal ou un agent.
- **Date** : 2026-11-13 (Product Hunt, 274 votes)
- **Lien** : https://www.producthunt.com/products/galaxy
- **Pourquoi c'est important** : Brique CLI pour agents. Non vérifié ailleurs.
- **Testable** : Oui — open source.

### Daybreak Red Team / Defense Factory (OpenAI)
- **Quoi** : Outils de sécurité qui testent les applications et proposent des correctifs revus par des ingénieurs. Red Team en accès anticipé. À noter aussi : ChatGPT Enterprise sur AWS Marketplace.
- **Date** : ~2026-11-13
- **Lien** : https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-friday-november-13-2026/
- **Pourquoi c'est important** : OpenAI pousse vers la sécurité offensive/défensive automatisée. Source secondaire uniquement, non confirmé.
- **Testable** : Non — accès anticipé. Voir aussi le repo trending openai/codex-security (751 étoiles/jour).

### Muse (Meta) : appels téléphoniques
- **Quoi** : L'assistant peut passer des appels pour l'utilisateur, abonnés payants US.
- **Date** : 2026-11-12
- **Lien** : https://dexerto.com/entertainment/metas-ai-can-now-make-phone-calls-you-dont-want-to-make-3428077
- **Pourquoi c'est important** : Agent vocal grand public. Source unique.
- **Testable** : Oui, abonnés Muse payants aux US.

## 🧠 Mises à jour de Modèles

- **Qwen 4 Max Preview (Alibaba)** : aperçu du 11 au 25 novembre, positionné codage et agents. Source : https://www.yottalabs.ai/post/qwen-4-max-specs-benchmarks-pricing-how-to-access (secondaire, non confirmé).
- **Baidu ERNIE 5.0 Thinking Preview** : listé le 13 novembre par un tracker (https://opper.ai/model-releases), non confirmé.
- **IBM Granite 4.1 LLMON (3B et 8B, expérimental)** : délimiteurs réservés pour séparer instructions et données, contre l'injection de prompt. Source : https://samonai.substack.com/p/ai-brief-november-13-2026 (non confirmé).
- **Qwen3.8-27B quantifié par Unsloth (Dynamic v3.1)** : https://unsloth.ai/docs/models/qwen3.8 — modèle sorti en août, seule la quantification est nouvelle. Testable via llama.cpp, open source.

## 🔬 Research

### Claude et les carnets de Gödel
- **Quoi** : Jan von Plato a utilisé Claude pour déchiffrer 16 carnets sténographiés (1 009 pages) : 663 théorèmes ou ébauches, dont environ 400 validés sous Coq, environ 200 à reformuler, environ 50 faux (chiffres rapportés).
- **Date** : 2026-11-13
- **Lien** : https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths
- **Pourquoi c'est important** : Cas concret d'IA pour l'histoire des maths, avec vérification formelle. Je n'ai pas lu l'article du Guardian, seulement la couverture secondaire.
- **Testable** : Non.

### Autres
- « After 600 experiments, here's what I discovered about JEPA world models » (225 pts HN) : https://haddyalchaer.com/jepa — non vérifié.
- « Weight Space Misfolding » (136 pts HN) : https://www.alphaxiv.org/abs/2611.weight-space-misfolding — non vérifié.

## 📝 À surveiller

- **IPO Anthropic** : fourchette 70–78 $ par action, pricing attendu le 18 nov, cotation Nasdaq « ANT » le 19 nov (CNBC : https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html). Pas encore fixé.
- **Procès d'ONG** visant Anthropic, Google, Meta, OpenAI et la division IA de SpaceX pour geler les modèles frontière (source : digest Neuron, non confirmé).
- **Panne FAA nationale** : enquête sur une éventuelle contribution d'un nouveau système d'IA (https://www.click2houston.com/news/local/2026/11/13/faa-investigating-whether-new-ai-technology-contributed-to-nationwide-ground-stop/) — rien de confirmé.
- **Nvidia** : accusations de scarcité organisée via le financement de startups clientes (https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus), 11,4 M$ de matériel disparu en transit. Allégations seulement.
- **Claude Code Projects** : refonte avec coordinateur et sessions parallèles (bêta depuis le 17 septembre, plus ancien que 72 h), consomme vite les quotas.
- **Schwab** lance son serveur MCP (https://riabiz.com/a/2026/11/13/schwab-surprises-analysts-with-extra-rapid-launch-of-own-mcp-servers-also-leaping-from-read-only-to-agentic-get-stuff-done-ai-it-leaves-rias-out-for-now-and-makes-anthropics-days-numbered-as-schwabs-exclusive-llm).
- **Financements/rachats** : Mirendil 1 Md$ Série A, Fractile 720 M$, Salesforce–Cresta (2,7 Md$, 5 nov), Oura–Counsel Health (625 M$). Chiffres de trackers, non vérifiés.
- **GitHub Trending IA** : alibaba/open-code-review, GoogleChrome/modern-web-guidance-src (1 925 étoiles/jour), ChromeDevTools/chrome-devtools-mcp.

## 📊 Résumé

- **Top 3 du jour** : 1) llama.cpp et ggml v1.0.0 ; 2) Gemini 4 Hydrogen ; 3) Claude Meetings (avec, en toile de fond, la démission de Jensen Huang et l'IPO Anthropic du 18-19 nov).
- **À tester en priorité** : llama.cpp v1.0.0 (open source), Perplexity Decider v1.3 (Apache, OpenRouter gratuit), Gemini 4 Hydrogen dans AI Studio ou l'app Gemini.
