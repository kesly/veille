# AI Watch — 2026-11-11 Matin

> Collecte : treg 4/4 sources, 15 recherches extended, GitHub Trending ok, 4 pages lues, 4 items confirmés par une deuxième source.

## 🔥 Breaking

### AlphaProof Code (Google DeepMind)
- **Quoi** : framework agentique multi-LLM qui vérifie formellement du vrai code. Il a prouvé en Lean des propriétés de sécurité clés du code du protocole Signal (libsignal). Plus de 6 M de lignes de Lean, générées par des agents Gemini Carbon, et seulement ~1 % du code signalé pour relecture humaine.
- **Date** : 2026-11-10
- **Lien** : https://deepmind.google/blog/introducing-alphaproof-code/
- **Pourquoi c'est important** : première vérification formelle de l'implémentation d'un protocole de chiffrement largement déployé à cette profondeur. Les agents ont retrouvé d'anciens bugs Signal déjà corrigés mais n'ont trouvé aucune nouvelle faille. Un chercheur DeepMind juge que le passage à tout le logiciel reste lointain. Papier technique publié, artefacts de vérification annoncés en open source.
- **Testable** : Non (artefacts et papier à consulter ; pas d'outil public)

### MiniMax H3-Image (poids ouverts)
- **Quoi** : modèle d'image open-weight (DiT 33B, 6 steps) en 4K (4096×4096) en moins de 10 s, jusqu'à 16 images de référence, édition incluse.
- **Date** : 2026-11-10
- **Lien** : https://www.minimax.io/blog/minimax-h3-image (poids : https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)
- **Pourquoi c'est important** : 4K rapide en local avec support ComfyUI dès le lancement. Les chiffres de vitesse sont des revendications du constructeur, sans benchmark indépendant. Licence communautaire MiniMax, pas une licence open source standard, et US/UK/UE/Corée du Sud exclus de la zone autorisée. Encodeur texte Qwen3-VL-32B requis, téléchargement de 70 à 135 Go selon les sources.
- **Testable** : Oui — poids sur Hugging Face + ComfyUI, ou API MiniMax (si région autorisée). Gratuit en local, API payante.

## 🆕 Nouveaux Outils & Produits

### Render Sandboxes
- **Quoi** : un « ordinateur par agent » : sandboxes pour exécuter du code non fiable, inactives = gratuites.
- **Date** : 2026-11-10 (Product Hunt, 262 votes)
- **Lien** : https://www.producthunt.com/products/render
- **Pourquoi c'est important** : brique d'infrastructure pour agents de code. Source unique (Product Hunt).
- **Testable** : Oui — payant à l'usage.

### Framer AI Agents
- **Quoi** : agents IA pour concevoir et publier des sites.
- **Date** : 2026-11-10 (Product Hunt, 970 votes, le plus voté du jour)
- **Lien** : https://www.producthunt.com/products/framer
- **Pourquoi c'est important** : fort signal d'adoption côté design/web. Source unique.
- **Testable** : Oui — freemium.

### Ember (Slack open source), Co-Review, Almanzor (MCP docs)
- **Quoi** : Ember = Slack open source auto-hébergé sur Cloudflare en un clic (104 votes) ; Co-Review = lire un dépôt entier avec l'agent qui l'a construit (100 votes) ; Almanzor = « Ask AI » + serveur MCP pour documentation, réponses citées (78 votes).
- **Date** : 2026-11-10
- **Lien** : https://www.producthunt.com/products/ember-117 · https://www.producthunt.com/products/co-review · https://www.producthunt.com/products/almanzor
- **Pourquoi c'est important** : outils de niche, intéressants pour les devs. Sources uniques.
- **Testable** : Oui.

### Repos GitHub Trending (jour)
- **Quoi** : anthropics/skills (+1 679 étoiles), mattpocock/skills (+1 225), vercel-labs/agent-browser (CLI de navigation pour agents, +780), homeassistant-ai/ha-mcp (+790), addyosmani/agent-skills (+465), meta/astryx (design system pensé pour agents, +3 108), billion-context (compression de contexte, +375).
- **Date** : 2026-11-11
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : les « Agent Skills » dominent le trending open source.
- **Testable** : Oui — open source, gratuit.

### GoogleChrome/modern-web-guidance
- **Quoi** : guide pour sortir les agents de code du JavaScript ~2019 vers les primitives web modernes (Show HN, 300 pts).
- **Date** : 2026-11-10
- **Lien** : https://github.com/GoogleChrome/modern-web-guidance
- **Pourquoi c'est important** : améliore la qualité du code généré par agents. Source unique (HN).
- **Testable** : Oui — open source.

## 🧠 Mises à jour de Modèles

### Meta Muse Ember 1.0
- **Quoi** : plus petit et moins cher modèle Meta, pour les tâches répétitives d'agents (appels d'outils, sous-tâches de code, extraction). Contexte 1 M tokens, entrées texte/image/audio/vidéo. $0,10 / $0,50 par million de tokens (entrée/sortie).
- **Date** : 2026-11-09 (certaines sources disent le 10)
- **Lien** : https://research.meta.ai/blog/muse-ember · https://thenextweb.com/news/meta-muse-ember-small-ai-model-haiku-luna
- **Pourquoi c'est important** : Meta revendique le niveau de Claude Haiku 5.5 sur l'Intelligence Index d'Artificial Analysis (36) à un tiers du coût par tâche. Haiku garde l'avantage sur FrontierCode 2.0 (34,9 % contre 27,2 %). Plusieurs résultats viennent de tests internes Meta.
- **Testable** : Oui — API Meta Model et Muse Code (payant).

### Gemini 4 Carbon (Google)
- **Quoi** : annoncé le 28 octobre ; déploiement dans le mode IA de la recherche pour les abonnés Ultra le 10 novembre. Un seul site (benchlm.ai) cite un tarif API introductif de $2/$10 jusqu'au 30 novembre, puis $4/$20, calqué sur Argon. Non vérifié sur la page officielle.
- **Date** : 2026-11-10 (déploiement)
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- **Pourquoi c'est important** : c'est le modèle qui fait tourner AlphaProof Code. À noter : à partir du 13 novembre, la sélection des modèles Pro passe derrière l'abonnement AI Pro à 20 $/mois.
- **Testable** : Oui — API Gemini / abonnement Ultra (payant).

### Claude Fable 5.2 (Anthropic)
- **Quoi** : mentionné par un agrégateur et par des posts Reddit (r/ClaudeAI : 5 195 et 2 407 pts), mais je n'ai trouvé aucune annonce officielle ni seconde source.
- **Date** : 2026-11-09 (agrégateur)
- **Lien** : https://www.reddit.com/r/ClaudeAI/comments/1xstews/
- **Pourquoi c'est important** : voir « À surveiller ».
- **Testable** : Non confirmé.

### Autres
- GPT Image 2.6 (Flare / Sunburst) d'OpenAI : sorti le 4 novembre, donc hors fenêtre, mais discuté sur r/OpenAI.
- Gemini Omni 1.2 Flash (vidéo, clips de 15 s, 720p à $0,07/s) : 5 novembre, hors fenêtre.

## 🔬 Research

### Glasswing après 7 mois (VulnCheck)
- **Quoi** : VulnCheck suit 442 CVE attribuables à Anthropic (~0,5 % des CVE de l'année), dont 2 exploitées. Sur 37 966 findings déclarés, 7 349 sont publics et 217 marqués corrigés. Environ 1 654 doublons, soit près de 8 fois plus que de correctifs. curl a rejeté 19 des 34 rapports publiés.
- **Date** : 2026-11-09
- **Lien** : https://www.vulncheck.com/blog/anthropic-glasswing-november-update
- **Pourquoi c'est important** : critique chiffrée du coût de triage reporté sur les mainteneurs. Anthropic répond que le goulot d'étranglement est la capacité humaine de triage. Chiffres issus du suivi de VulnCheck, relayés par un digest de la Cloud Security Alliance. HN : 336 pts.
- **Testable** : Non

### The Surprising Effectiveness of Deleting Weights in LLM Post-Training
- **Quoi** : papier arXiv (2611.10866), très peu de signal pour l'instant (11 pts HN).
- **Date** : 2026-11-10
- **Lien** : https://arxiv.org/abs/2611.10866
- **Pourquoi c'est important** : non évalué, lu uniquement par son titre.
- **Testable** : Non

## 📝 À surveiller
- **Claude Fable 5.2** : buzz massif sur Reddit, mais aucune annonce officielle trouvée ; à confirmer.
- **Débat « code généré par IA »** : « AI usage generates a fragile codebase » (424 pts, 432 commentaires sur HN) — https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/
- **Val Town ferme** (329 pts HN) : https://blog.val.town/winding-down
- **Meta + Conductor** : rachat début novembre d'une startup qui orchestre plusieurs agents de code en parallèle ; interface prévue début 2027.
- **Microsoft MAI-Voice-2.1 / Flash** : annoncés dans un récap, sans date de sortie confirmée. Voix : AssemblyAI-TTS-1 sorti le 27 octobre ($15 / M caractères).
- **Fireworks AI** : cyberattaques divulguées, avec exposition de données clients et de parties de modèles non publiés (source unique).
- **Sécurité des agents** : Neo « Neoverse » (9 novembre), moteur gratuit d'analyse du risque des serveurs MCP et skills.
- **Australie** : projet de régulateur pour l'IA de pointe.

## 📊 Résumé
- **Top 3 du jour** : 1) AlphaProof Code vérifie formellement Signal ; 2) MiniMax H3-Image, 4K open-weight en moins de 10 s (licence restrictive) ; 3) Meta Muse Ember, petit modèle d'agents à $0,10/$0,50.
- **À tester en priorité** : H3-Image via ComfyUI (si région autorisée) ; Muse Ember via Meta Model API ; skills d'agents (anthropics/skills, mattpocock/skills) et vercel-labs/agent-browser.
