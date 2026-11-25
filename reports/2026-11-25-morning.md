# AI Watch — 2026-11-25 Matin

> Collecte : treg 4/4 sources (X : 3 posts après filtre, peu exploitables), 17 recherches extended, GitHub Trending ok, 4 pages lues (1 PDF illisible, 1 page GitHub sans contenu utile), 6 items confirmés par une deuxième source.

## 🔥 Breaking

### OpenAI : « GPT-6 as a Universal Foundation Model for Protein Biology » (preprint)
- **Quoi** : la famille GPT-6 conçoit des structures et séquences de protéines par raisonnement et code généraliste, sans appeler de modèle biologique spécialisé. Tests en laboratoire avec Onava : liaison observée sur 5 cibles avec des protéines issues de GPT-6.2 ; des anticorps redessinés gardent leur liaison.
- **Date** : 2026-11-24
- **Lien** : https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/ — https://www.unite.ai/openai-reports-gpt-6-designs-proteins-with-reasoning-and-code/
- **Pourquoi c'est important** : un modèle généraliste rivalise avec des outils dédiés (selon la presse secondaire : 43,7 % vs 27,8 % pour RFdiffusion sur 30 défis de motif-scaffolding ; 35 protéines sur 322 synthétisées se lient à leur cible). Réserves : le modèle interne n'est pas celui qu'on peut utiliser, des modèles spécialisés ont aidé à sélectionner les candidats, et c'est un preprint non relu.
- **Testable** : Non (pas d'endpoint dédié ; preprint lisible).

### OpenAI : preprint « The matrix multiplication exponent is nine fourths »
- **Quoi** : OpenAI affirme que l'exposant de la multiplication de matrices carrées vaut exactement 9/4 sur tout corps. La borne supérieure 9/4 vient d'un preprint d'octobre ; la nouveauté serait la borne inférieure correspondante (pour les circuits arithmétiques formels, d'après un seul résumé).
- **Date** : 2026-11-24
- **Lien** : https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf — https://aiweekly.co/alerts/openai-claims-matrix-multiplication-exponent-is-exactly-94 — https://eccc.weizmann.ac.il/report/2026/281/
- **Pourquoi c'est important** : le meilleur exposant connu était d'environ 2,371. Si la borne inférieure tient, c'est un résultat théorique majeur. Aucune vérification indépendante de l'argument inférieur n'a été trouvée, et aucun impact pratique sur les GPU n'est attendu. Je n'ai pas pu lire le PDF (extraction vide) : revendication à traiter avec prudence.
- **Testable** : Non (papier ; le dépôt openai/math est public).

### Anthropic : Claude Ship (Code Review, PR Steward, Claude Approvals)
- **Quoi** : agents qui relisent les pull requests GitHub, proposent des correctifs et approuvent les changements routiniers selon un fichier de politique écrit par l'équipe. Code Review est disponible ; PR Steward et Claude Approvals sont en bêta. Anthropic recommande de démarrer en mode observation seule et reconnaît que l'outil peut rater des bugs ou failles.
- **Date** : 2026-11-23
- **Lien** : https://marktechpost.com/2026/11/23/anthropic-claude-ship-pull-request-agents — https://www.itpro.com/software-engineering/anthropics-new-claude-ship-service-hands-the-reins-to-agents-to-fix-and-review-code-changes-but-the-company-warns-it-may-miss-bugs-security-vulnerabilities-or-other-issues
- **Pourquoi c'est important** : passe du relecteur assistant à l'agent qui approuve. Chiffres cités (PR fusionnées x2 de juin à septembre, annulations -40 %) : internes à Anthropic. Aussi n°6 de Product Hunt (137 votes).
- **Testable** : Oui, abonnés Claude Team/Enterprise avec GitHub (payant).

## 🆕 Nouveaux Outils & Produits

### Ternary Bonsai 2.5 27B (PrismML)
- **Quoi** : modèle ternaire de 27B basé sur Qwen3.8, 5,9 Go en mémoire, orienté code agentique et usage d'outils en local. Selon PrismML : SWE-bench Verified 75,6 (Qwen3.8 27B pleine précision : 80,6 ; Bonsai 2 : 60,8), Terminal-Bench 2.1 60,1, τ³-Bench 73,9. Tourne via llama.cpp (NVIDIA/Intel) et MLX (Apple).
- **Date** : 2026-11-24
- **Lien** : https://prismml.com/news/bonsai-2-5-27b — https://github.com/PrismML-Eng/Bonsai-demo
- **Pourquoi c'est important** : très près du modèle de base pour un quart de l'empreinte mémoire. Benchmarks fournis par l'éditeur. 375 pts sur Hacker News.
- **Testable** : Oui, open weights Apache 2.0, gratuit (`./setup.sh` du dépôt demo ; vérifier le nom exact du modèle sur Hugging Face).

### Google Workspace MCP servers + Workspace CLI en GA
- **Quoi** : serveurs MCP et CLI pour Gmail, Drive, Docs, Sheets, Calendar. Un compte rendu indique que les agents devront passer par MCP plutôt que l'API directe à partir du 1er février 2027 (non confirmé ailleurs).
- **Date** : 2026-11-24
- **Lien** : https://adaptd.ai/updates/google-workspace-mcp-servers-agent-controls/
- **Pourquoi c'est important** : standardise l'accès des agents aux données Workspace. Source unique agrégatrice, à vérifier sur le blog Google.
- **Testable** : Oui (selon la source, services Workspace).

### Canva MCP server en disponibilité générale
- **Quoi** : serveur MCP Canva ouvert sans liste d'attente, avec de nouvelles API pour intégrer Canva dans d'autres logiciels.
- **Date** : ~2026-11-24
- **Lien** : https://thenextweb.com/news/canva-mcp-ai-agents-developers
- **Pourquoi c'est important** : design pilotable par agent. Une seule source.
- **Testable** : Oui.

### Songe (sous-labs) et autres projets du jour
- **Quoi** : « A training engine for your local model, using your idle compute » (HN 197 pts). Je n'ai pas pu lire le README, donc je ne peux pas décrire le fonctionnement. Product Hunt : Render Sandboxes (281 votes, bacs à sable pour agents), Fleetify (open source, centre de contrôle d'agents de code, 86 votes), Granular.Build (201 votes), Clam AI (170 votes).
- **Date** : 2026-11-24
- **Lien** : https://github.com/sous-labs/songe — https://www.producthunt.com/products/render — https://www.producthunt.com/products/fleetify
- **Pourquoi c'est important** : signaux de popularité uniquement, pas de revue de fond.
- **Testable** : Oui (Songe et Fleetify sont open source ; Render est payant).

### GitHub Trending (open source)
- Skills et outils pour agents dominent : obra/superpowers (framework de skills, +1 003 étoiles), firecrawl/firecrawl (API de scraping pour agents, +991), HKUDS/CLI-Anything (rendre les logiciels utilisables par agents via CLI, +1 074), elementalsouls/Claude-BugHunter (skills Claude Code pour chasse aux bugs, +1 826), jingyaogong/minimind (LLM de 64M entraîné de zéro, +727), google-labs-code/stitch-skills (+403).
- **Lien** : https://github.com/trending?since=daily

## 🧠 Mises à jour de Modèles

### GPT-6.2 Sol dans l'onglet Chat de ChatGPT
- **Quoi** : version de GPT-6.2 Sol adaptée à la conversation, déployée à partir du 23 novembre pour Plus, Pro, Business, Enterprise (pas Free ni Go). Le modèle lui-même est sorti le 17 novembre. Une source mentionne un retrait de l'ancien modèle le 23 décembre (source unique).
- **Date** : 2026-11-23
- **Lien** : https://www.macrumors.com/2026/11/23/openai-gpt-6-2-sol-chatgpt/ — https://www.notebookcheck.net/GPT-6-2-comes-to-ChatGPT-s-Chat-tab-but-only-for-paid-plans.1458765.0.html
- **Pourquoi c'est important** : mise à jour de produit plus que nouveau modèle.
- **Testable** : Oui, abonnement payant.

### GLM-5.4 (Z.ai)
- Déjà couvert dans le rapport d'hier. Toujours sans API ni poids ouverts d'après les digests du jour.

## 🔬 Research
- Voir les deux preprints OpenAI en Breaking (protéines, multiplication de matrices).
- Reddit r/LocalLLaMA : post à 646 pts sur la réduction de la mémoire pour 1M tokens de 130 To à 890 Mo (https://www.reddit.com/r/LocalLLaMA/comments/1y4kikk/). Je n'ai pas lu le contenu, donc je ne peux pas dire de quelle technique il s'agit.
- LessWrong : « Models Can Communicate via Inference Servers Despite Being Sandboxed » (https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being), non lu.

## 📝 À surveiller
- **Nvidia** : le conseil a réintégré Jensen Huang comme PDG le 23 novembre, onze jours après sa démission ; l'action a bondi de 31 % lundi puis reculé de 7 % mardi. Une enquête indépendante se poursuit. https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director
- **Amazon / Decart** : accord rapporté à 7,5 Md$ pour la technologie d'optimisation de Decart (Amazon confirme l'accord, pas le prix). https://techstartups.com/2026/11/23/amazon-acquires-decart-ais-technology-in-reported-7-5-billion-deal-to-boost-ai-chip-performance/
- **Palo Alto Networks / Applied Compute** : rachat rapporté à 4,5 Md$ ; **Sierra** lève 1,75 Md$ à 30 Md$ de valorisation (en cours). Sources secondaires.
- **Anthropic** : Artifacts installables en apps de bureau Mac/Windows (bêta, compte gratuit, https://the-decoder.com/anthropic-turns-claude-artifacts-into-standalone-desktop-apps-for-macos-and-windows/) ; skills via MCP en bêta publique et Tasks/Elicitation en GA (source secondaire, https://news.sulat.com/2026/11/25/claude-mcp-skills/). Des digests évoquent aussi une IPO à 81,3 Md$ et un accord Nscale d'environ 45 Md$ : non vérifiés, un seul digest.
- **Google Gemini 4 Neon** (18 novembre, 3 $/15 $ par M de tokens d'après une source) et Gemini API CLI, qui permet à Claude Code/Codex d'utiliser Gemini (post X, 109 likes). https://dev.to/jimmyliao/gemini-api-cli-official-guide-part-1-giving-your-ai-agent-a-stateless-multimodal-cli-toolbox-36p3
- **Notion MCP** : r/ClaudeAI (403 pts) accuse le MCP officiel de Notion d'injecter des messages commerciaux cachés dans Claude. Accusation Reddit non vérifiée.
- **Versine (YC F26)** : MCP pour envoyer et recevoir de l'argent, Launch HN 75 pts. https://news.ycombinator.com/item?id=50634426
- Voix : rien de neuf daté du 24. Dernier lancement notable : Qwen3 TTS sur Together AI (20 novembre). Image/vidéo : rien de daté du 24 (dernier : MiniMax H3, 21 novembre). Mistral : rien de neuf (Large 4 du 29 octobre).
- Tableaux de modèles « S1 Fast / S1 Pro / REAX 1 » : un seul agrégateur, aucune confirmation, ignorés.

## 📊 Résumé
- **Top 3 du jour** : 1) OpenAI : GPT-6 conçoit des protéines, avec liaison en laboratoire sur 5 cibles (preprint). 2) Anthropic : Claude Ship, des agents qui relisent et approuvent les PR. 3) PrismML : Ternary Bonsai 2.5 27B, modèle agentique local de 5,9 Go en open weights.
- **À tester en priorité** : Bonsai 2.5 27B en local (Apache 2.0) ; Claude Ship en mode observation seule sur un dépôt Team/Enterprise ; serveurs MCP Google Workspace et Canva une fois la GA vérifiée.
