# AI Watch — 2026-11-15 Matin

> Collecte : treg 4/4 sources, 19 recherches extended, GitHub Trending ok, 2 pages lues, 6 items confirmés par une deuxième source.

## 🔥 Breaking

### Gemini 4 Hydrogen (Google)
- **Quoi** : Nouveau modèle rapide de la famille Gemini 4, pensé pour le code au quotidien et les workflows agentiques. Google annonce qu'il dépasse Argon sur l'Artificial Analysis Intelligence Index, avec 4 niveaux de réflexion configurables et une vitesse 2,5x supérieure à Gemini 3.8 Flash.
- **Date** : 12 novembre 2026 (certains sites indiquent le 13)
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
- **Pourquoi c'est important** : Le niveau « Flash » devient aussi bon que l'ancien haut de gamme. Il est déployé dans Search et l'app Gemini pour tous les utilisateurs, et dans l'API, AI Studio et Antigravity (option Orchestrator avec Carbon).
- **Testable** : Oui, via l'app Gemini, Google AI Studio ou l'API Gemini. Payant à l'usage (un site secondaire cite 1,50 $ par million de tokens en entrée, non confirmé).

### Jensen Huang quitte Nvidia
- **Quoi** : Jensen Huang démissionne de son poste de CEO et du conseil d'administration après 33 ans. La CFO Colette Kress est CEO par intérim. Nvidia ne donne pas de raison. La presse évoque des allégations personnelles et une enquête interne liée à une opération de renseignement étrangère. CNBC parle d'une éviction, d'après une source anonyme.
- **Date** : 11-12 novembre 2026
- **Lien** : https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html
- **Pourquoi c'est important** : Nvidia est au cœur de la chaîne de valeur de l'IA. Le sujet domine r/LocalLLaMA (3200 pts) et la succession peut peser sur la roadmap GPU et le marché.
- **Testable** : Non

### Anthropic : IPO prévue sur le Nasdaq (ticker ANT)
- **Quoi** : Fourchette de prix de 70 à 78 $ pour 825 M d'actions, soit jusqu'à environ 64 Md$ levés. Fixation du prix attendue le 18 novembre et début de la cotation le 19. Environ 20 % des titres sont réservés au retail.
- **Date** : fourchette annoncée le 10 novembre 2026
- **Lien** : https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html
- **Pourquoi c'est important** : C'est la plus grosse introduction en bourse d'un laboratoire d'IA. Elle sert de référence de valorisation pour tout le secteur. Les dates du 18 et du 19 viennent de la presse, pas du dépôt.
- **Testable** : Non

### Thinking Machines : poids ouverts d'Inkling 2 Small
- **Quoi** : MoE de 594 Md de paramètres au total (17 Md actifs), licence Apache 2.0, publié sur Hugging Face. Il est classé meilleur modèle open-weights hors Chine selon Artificial Analysis. Le checkpoint NVFP4 demande au moins 500 Go de VRAM.
- **Date** : 12 novembre 2026
- **Lien** : https://thinkingmachines.ai/model-card/inkling-2-small/
- **Pourquoi c'est important** : Gros modèle ouvert et permissif, compatible SGLang, vLLM et Unsloth. L'annonce de l'équipe vient d'un post X relayé par des blogs. Je n'ai pas lu la page officielle.
- **Testable** : Oui pour qui a du matériel multi-GPU (2x B300 ou 4x H200). Open source, gratuit. Sinon via Tinker, le service du laboratoire.

## 🆕 Nouveaux Outils & Produits

### Cloudflare Kitesurf (open source)
- **Quoi** : Moteur de navigateur léger pour agents IA, plus économe en CPU et mémoire que Chromium. Il est compatible Chrome DevTools Protocol, donc les scripts Puppeteer fonctionnent sans réécriture. Il est encore en développement actif.
- **Date** : 12-13 novembre 2026
- **Lien** : https://developers.cloudflare.com/changelog/post/2026-11-12-kitesurf-open-source/
- **Pourquoi c'est important** : Réduit le coût du browsing par agents à grande échelle. Le service hébergé Browser Run n'est pas inclus dans le dépôt.
- **Testable** : Oui, en auto-hébergement ou sur un compte Cloudflare. Apache 2.0.

### Render Sandboxes
- **Quoi** : Une machine isolée par agent, démarrage en moins d'une seconde. Product Hunt : 265 votes.
- **Date** : 14 novembre 2026 (lancement Product Hunt)
- **Lien** : https://www.producthunt.com/products/render
- **Pourquoi c'est important** : L'infrastructure de sandbox pour agents devient un segment à part entière (Nvidia donne OpenShell au CNCF dans le même mouvement). Seule la page Product Hunt a été consultée.
- **Testable** : Oui, payant.

### Gemini Robotics 2.5
- **Quoi** : Modèle robotique « le plus capable » de Google selon la fiche Product Hunt (147 votes).
- **Date** : 14 novembre 2026 (lancement Product Hunt)
- **Lien** : https://www.producthunt.com/products/gemini-robotics-2-5
- **Pourquoi c'est important** : Autre signal sur la robotique, alors que des sources non confirmées disent qu'OpenAI aurait dissous son équipe robotique. Pas de seconde source sur les détails.
- **Testable** : Non vérifié

### Open source trending (GitHub)
- **Quoi** : GoogleChrome/modern-web-guidance-src (+1231 étoiles/jour, bonnes pratiques web pour agents de code), alibaba/open-code-review (+893, revue de code hybride règles et LLM), ChromeDevTools/chrome-devtools-mcp (+664), tradermonty/claude-trading-skills (+553), backnotprop/plannotator (+408), JuliusBrussee/caveman (+227, réduit la consommation de tokens d'environ 65 %, chiffre du dépôt), Tencent/LoopForge (orchestration d'agents de code avec validation humaine).
- **Date** : 15 novembre 2026
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : Les outils autour des agents de code (revue, contexte, MCP, économie de tokens) dominent le trending.
- **Testable** : Oui, tous open source.

## 🧠 Mises à jour de Modèles
- **Gemini 4 Hydrogen** : voir Breaking.
- **Inkling 2 Small** : voir Breaking.
- Sinon RAS de confirmé sur les dernières 24 h. Qwen4-Max-Preview (depuis le 11 novembre, selon un agrégateur) et MiniMax H3-Image (open-weight, environ 10-11 novembre) sont à vérifier. Voir « À surveiller ».

## 🔬 Research
### Google Research : Antigravity /teamwork
- **Quoi** : Système multi-agents s'appuyant sur Gemini 4 Argon, Carbon et Hydrogen. Il est appliqué à des problèmes ouverts en information theory, vérification formelle, chimie et optimisation de kernels, avec des experts humains. Le billet décrit des vérificateurs comme le prouveur Lean 4. Les outils sont ouverts via Antigravity.
- **Date** : 13 novembre 2026
- **Lien** : https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/
- **Pourquoi c'est important** : Source primaire lue. Il revendique des résultats concrets, non audités ici.
- **Testable** : Oui pour les abonnés Antigravity (Pro/Ultra) et via le programme d'accès chercheurs.

### Autres
- Show HN : DeepSeek V3 en environ 200 lignes de JAX (201 pts) : https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax. Utile pour apprendre, open source.
- Étude de l'université du Michigan : l'IA générative consomme plus d'énergie sur du texte non anglais (188 pts HN) : https://news.umich.edu/generative-ai-uses-more-energy-on-non-english-text/

## 📝 À surveiller
- **FBI FLASH sur ARTEX** (13 novembre) : framework open source de pentest piloté par LLM, détourné par des acteurs criminels et étatiques. Accès privilégié en moins de 3 h dans certains cas, plus de 1 600 consoles exposées. Il se branche sur Claude, GPT, DeepSeek et d'autres. Couvert par plusieurs sites de sécurité, je n'ai pas lu l'alerte elle-même (FLASH-20261113-001). À surveiller par toute équipe qui expose des clés d'API LLM.
- **Lovable** : une étude de 159 041 projets montre des données sensibles accessibles sans authentification (701 pts HN, page lue). La recherche date du 2 novembre, donc ancienne, mais le débat est actif.
- **Poursuite de 4 ONG contre OpenAI, Anthropic, Google, Meta et SpaceX** (San Francisco, déposée vers le 12 novembre) : demande d'injonction pour suspendre l'entraînement des nouveaux modèles. Plusieurs sources, détails à confirmer.
- **ChatGPT Wallet** (13 novembre selon un site) : paiements par agents avec jeton, d'abord pour les abonnés Pro aux États-Unis. Une seule famille de sources, aucune confirmation officielle vue. « Businesses in ChatGPT » : 183 votes sur Product Hunt.
- **Claude Fable 5.2 et Mythos 5.2** (9 novembre, au-delà des 72 h) : r/ClaudeAI très actif (7177 pts sur une démo Fable 5.2).
- **Claude Sheets/Whiteboards, mises à jour de Claude Code** : source unique, non confirmé.
- **llama.cpp v1.0.0** : cité par une seule newsletter.
- **Alibaba**, modèle vidéo annoncé pour novembre, sans nom.
- **Meta** : agent Chrome pour Muse et nom de modèle fuité, non confirmés.
- Autres signaux : amende de 887 M$ infligée à Meta par l'Italie (Reuters), des chercheurs affirment que des modèles chinois portent la trace de GPU soumis à contrôle d'export (392 pts HN, source unique).

## 📊 Résumé
- **Top 3 du jour** : 1) Départ de Jensen Huang de Nvidia. 2) IPO d'Anthropic, cotation attendue le 19 novembre. 3) Gemini 4 Hydrogen, avec Inkling 2 Small en open weights juste derrière.
- **À tester en priorité** : Gemini 4 Hydrogen (AI Studio), Cloudflare Kitesurf (open source), chrome-devtools-mcp et caveman (GitHub Trending). Pour la sécurité, vérifier les indicateurs de l'alerte FBI sur ARTEX.
