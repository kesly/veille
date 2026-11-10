# AI Watch — 2026-11-10 Matin

> Collecte : treg 4/4 sources, 15 recherches extended, GitHub Trending ok, 4 pages lues (Anthropic, Meta, Google, repo Gemini), 4 items confirmés par une deuxième source (Fable 5.2, Muse Ember, TPU 8tx/8i Max, Opus 5.5 « nerf »).

## 🔥 Breaking

### Claude Fable 5.2 et Mythos 5.2 (Anthropic)
- **Quoi** : Mise à jour du duo Fable/Mythos (même modèle sous-jacent). Mieux en code, raisonnement et vision, sorties jusqu'à 30 % plus rapides que 5.1. Prix en baisse : 8 $/M tokens en entrée, 40 $/M en sortie. Mode « fast » optionnel jusqu'à 2,5x plus rapide (16 $/80 $). Anthropic annonce aussi une preuve formalisée du dernier théorème de Fermat en 30 h en test prérelease.
- **Date** : 2026-11-09
- **Lien** : https://www.anthropic.com/claude-fable-and-mythos-5-2 (confirmé par CNBC et MacRumors)
- **Pourquoi c'est important** : Fable 5.2 monte à 65 sur Artificial Analysis, le meilleur score à ce jour selon HN (https://artificialanalysis.ai/models/claude-fable-5-2). Sortie juste avant l'IPO attendue d'Anthropic. Fable est ouvert à tous, Mythos est réservé aux organisations vérifiées (programmes Cyber et Life Sciences). Payant.
- **Testable** : Oui — Fable 5.2 via API, Claude Code, Google Cloud, Microsoft Foundry.

### Meta Muse Ember
- **Quoi** : Le plus petit modèle de la gamme Muse, pensé pour les tâches répétitives d'agents (appels d'outils, routage, extraction). 0,10 $/M tokens en entrée, 0,50 $/M en sortie. Contexte 1M tokens, multimodal.
- **Date** : 2026-11-09
- **Lien** : https://research.meta.ai/blog/muse-ember (confirmé par TechCrunch, The Decoder, SiliconANGLE)
- **Pourquoi c'est important** : Meta dit égaler Claude Haiku 5.5 à environ un tiers du coût et battre GPT-6 Luna. Les benchmarks sont ceux de Meta. The Decoder note que Haiku reste devant sur les tâches de code réelles (34,9 % contre 27,2 %). Poids fermés.
- **Testable** : Oui — API Meta (`muse-ember-1.0`), Muse Code. Payant.

### Google TPU 8tx et TPU 8i Max
- **Quoi** : Deux nouveaux systèmes de la 8e génération de TPU. 8tx : inférence confidentielle avec sécurité matérielle. 8i Max : très longs contextes, deux fois le calcul, la SRAM et la HBM du 8i.
- **Date** : 2026-11-09
- **Lien** : https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/ (confirmé par SiliconANGLE)
- **Pourquoi c'est important** : Quatre systèmes TPU en un an, face à Nvidia. Pas de date de disponibilité officielle (Bloomberg parle de 2027 pour le 8i Max).
- **Testable** : Non.

## 🆕 Nouveaux Outils & Produits

### ChatGPT Work + app desktop (OpenAI)
- **Quoi** : Agent pour tâches longues multi-étapes, déploiement général avec nouvelle app desktop. Pro, Enterprise et Edu d'abord, Plus et Business dans les jours qui suivent.
- **Date** : semaine du 2026-11-09 (dates variables selon les sources agrégatrices)
- **Lien** : https://openai.com/news/
- **Pourquoi c'est important** : Concurrent direct des agents de Claude. Je n'ai pas lu la source primaire, donc à confirmer. Payant.
- **Testable** : Oui, si abonnement éligible.

### Product Hunt du jour
- **Quoi** : Render Sandboxes (une machine par agent, démarrage en moins d'une seconde, 262 votes), Product Hunt MCP (361 votes), MCP1 d'Appwrite (une URL pour tous les serveurs MCP, 130 votes), Arcjet AI security models (modèles de sécurité pour agents de code, 216 votes), ProtoMap (130+ votes, réduit les tokens gaspillés à redécouvrir les dépendances).
- **Date** : 2026-11-10
- **Lien** : https://www.producthunt.com/products/render ; https://www.producthunt.com/products/producthunt ; https://www.producthunt.com/products/appwrite
- **Pourquoi c'est important** : L'infrastructure pour agents (sandbox, MCP) reste le thème dominant.
- **Testable** : Oui (offres gratuites ou d'essai à vérifier).

### Higgsfield Miracle
- **Quoi** : Transforme une vidéo en calques éditables (recolorer, texte, fonds) sans régénérer. Bêta privée, bientôt dans Higgsfield MCP.
- **Date** : annoncé 2026-11-06, 133 votes sur Product Hunt le 10 novembre
- **Lien** : https://www.pixelsham.com/2026/11/06/introducing-higgsfield-miracle/
- **Pourquoi c'est important** : Édition vidéo locale, pas de génération. Prix et date de lancement inconnus.
- **Testable** : Non (bêta limitée).

## 🧠 Mises à jour de Modèles
- **Mistral Large 4 « Le Chonk »** : poids ouverts d'un modèle à 1 000 milliards de paramètres, licence MIT modifiée. Dates contradictoires selon les sources (29 octobre selon TechCrunch). Plus de 72 h, donc en contexte seulement. https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/
- **Gemini Omni 1.2 Flash** (vidéo, clips de 15 s, -30 % de prix) du 5 novembre et **GPT Image 2.6** du 4 novembre : hors fenêtre de 72 h, à titre de contexte.
- Reddit LocalLLaMA : débat sur un éventuel biais d'Artificial Analysis contre les modèles à poids ouverts (224 pts). Pas de nouvelle release Qwen confirmée.

## 🔬 Research
- RAS de confirmé. E-means (alternative à k-means, 305 pts sur HN) est une piste, non vérifiée : https://e-means.github.io/
- GitHub Trending : `anthropics/skills`, `meta/astryx` (design system « agent-ready »), `vercel-labs/agent-browser` (CLI de navigation pour agents), `anthropics/claude-quickstarts`, `homeassistant-ai/ha-mcp`. Tous open source. Source : https://github.com/trending?since=daily

## 📝 À surveiller
- **« Opus 5.5 est-il nerfé ? »** : 766 pts sur HN. Le changement du 3 novembre porterait sur les résumés de réflexion visibles. Aucune preuve publique d'une baisse de qualité des poids, et Anthropic n'a pas répondu. Opus 5.5 est par défaut en effort moyen.
- **Gemini et revue humaine des fichiers Drive/Gmail** : allégation d'un dépôt GitHub tiers (473 pts sur HN). La page d'aide Google serait modifiée depuis le 16 octobre. Je n'ai trouvé aucun démenti ni confirmation de Google, donc non vérifié. https://github.com/thisisme6598/gemini_files/
- **Fireworks AI** : intrusion du 24 octobre, avec accès aux données de facturation, communiquée aux clients le 9 novembre (une seule source).
- **Rumeur** : référence à « Claude Mythos 5.5 » sur la page Mythos (TestingCatalog, non confirmée).
- **Financement** : OpenAI aurait levé 11 Md$ à 1,25 T$ de valorisation (non confirmé). Shield AI rachète Echodyne pour 5,3 Md$. Le rendement obligataire de CoreWeave dépasse 16 % (stress de crédit IA).
- **OpenAI** retire Agent Builder le 30 novembre, au profit de l'Agents SDK.

## 📊 Résumé
- **Top 3 du jour** : 1) Claude Fable 5.2 / Mythos 5.2, 2) Meta Muse Ember (modèle d'agent à bas coût), 3) Google TPU 8tx / 8i Max.
- **À tester en priorité** : Fable 5.2 (et son mode fast) dans Claude Code, Muse Ember pour les sous-tâches d'agents, `vercel-labs/agent-browser` (open source), Render Sandboxes.
