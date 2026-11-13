# AI Watch — 2026-11-13 Matin

> Collecte : treg 4/4 sources (X : 0 post retenu), 14 recherches extended, GitHub Trending ok, 4 pages lues, 4 items confirmés par une deuxième source.

## 🔥 Breaking

### Gemini 4 Hydrogen (Google)
- **Quoi** : nouveau modèle rapide de la famille Gemini 4 (aux côtés de Carbon et Argon), pensé pour le code et les workflows agentiques ; remplace Gemini 3.8 Flash. Lancement d'« Orchestrator » dans Antigravity, qui bascule dynamiquement entre Carbon et Hydrogen dans une même session.
- **Date** : 12 nov. 2026
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
- **Pourquoi c'est important** : 2,5x plus rapide que 3.8 Flash, Terminal-Bench 4.1 57 % vs 18,2 %, indice Artificial Analysis 51 (54 en xhigh), contexte 1M tokens à 1,50 $/7,50 $ par M tokens. Devient le modèle par défaut d'AI Mode dans Search. Chiffres issus de Google (confirmés par plusieurs médias).
- **Testable** : Oui — Gemini API, AI Studio, app Gemini (sélection auto en gratuit), Antigravity (Pro/Ultra). Payant via API.

### Jensen Huang quitte la direction de Nvidia
- **Quoi** : Huang démissionne de son poste de CEO et du conseil ; la CFO Colette Kress devient CEO par intérim. Contexte de scandale (enquête interne, relations avec des employées ; certaines sources évoquent une tentative d'ingérence étrangère).
- **Date** : 12 nov. 2026 (conseil ayant accepté la démission le 11)
- **Lien** : https://techcrunch.com/2026/11/12/nvidias-jensen-huang-resigns-chipmaker-names-cfo-colette-kress-as-interim-ceo/
- **Pourquoi c'est important** : choc majeur pour le fournisseur central de l'infrastructure IA ; action en baisse d'environ 13 % à l'ouverture, recherche d'un successeur en cours. Les détails des allégations restent non vérifiés.
- **Testable** : Non

### Anthropic IPO : fourchette de prix et calendrier
- **Quoi** : introduction en bourse sur Nasdaq (ticker « ANT »), 825 M d'actions à 70–78 $, valorisation implicite ~1,4 T$. Fixation du prix le 18 nov., cotation le 19 nov. T3 2026 : 17,0 Md$ de revenus (>12x sur un an), perte nette 23,3 Md$ (dont 21,9 Md$ de charge non cash).
- **Date** : amendement du S-1 le 10 nov. ; roadshow en cours
- **Lien** : https://ipo.anthropic.com/us/ — https://techcrunch.com/2026/11/10/anthropic-sets-ipo-price-range-of-70-to-78-per-share-to-reach-an-implied-valuation-of-1-404-trillion/
- **Pourquoi c'est important** : plus grosse IPO IA à ce jour ; engagements de calcul d'environ 895 Md$ selon le dépôt. Carnet d'ordres décrit comme plusieurs fois sursouscrit (source secondaire).
- **Testable** : Non

## 🆕 Nouveaux Outils & Produits

### Edge0-145B / 120B (open source)
- **Quoi** : modèles open weights de 145B (MoE, 512 experts, 10 actifs, contexte 256K) exécutables en local ; framework d'inférence et app fournis. Annonce : 29 Go de mémoire pic, 80+ tokens/s en décodage sur laptop (chiffres du fournisseur, non indépendants).
- **Date** : 12 nov. 2026
- **Lien** : https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer — https://huggingface.co/Edge0/Edge0-145B-q3k
- **Pourquoi c'est important** : si confirmé, change la donne pour l'IA locale. Attention : exigences matérielles contradictoires selon les sources (MacBook vs GPU CUDA 16 Go) et licence à vérifier (mention de conditions Qwen).
- **Testable** : Oui — poids sur Hugging Face, repo GitHub Edge0-AI/Edge0. Gratuit/open source.

### Anthropic : Claude for Manufacturing et Claude Meetings (bêta)
- **Quoi** : plugin de 17 skills pour l'industrie ; Claude Meetings (participant dans les appels Google Meet) avec Whiteboards et Sheets.
- **Date** : 10–12 nov. 2026
- **Lien** : https://www.unite.ai/anthropic-launches-claude-meetings-beta-for-live-video-calls/
- **Pourquoi c'est important** : poussée vers la productivité en entreprise. Source secondaire uniquement.
- **Testable** : Oui — offres Team/Enterprise (payant).

### Product Hunt / HN : agents et outillage
- **Plurai Simulation** (366 votes, API : monde simulé pour améliorer un agent) — https://www.producthunt.com/products/plurai
- **Omnigraph** (233 votes, open source : base de graphes pour agents) — https://www.producthunt.com/products/omnigraph
- **Harness Memory** (126 votes, open source : mémoire long terme d'agents) — https://www.producthunt.com/products/epsilla
- **Spacefast by Automattic** (160 votes : environnement pour agents) — https://www.producthunt.com/products/spacefast-by-automattic
- **Gemini Decisions API** (112 votes : décisions multimodales calibrées) — https://www.producthunt.com/products/google
- **AgentRun** (Show HN, open source : agents managés auto-améliorants) — https://github.com/Parcha-ai/agentrun/blob/main/README.md
- **Pourquoi c'est important** : tendance nette vers simulation, mémoire et runtime pour agents. Un seul signal chacun, pas de seconde source.
- **Testable** : Oui (liens ci-dessus).

### GitHub Trending (open source)
- openai/codex-security (CLI/SDK sécurité, +643 étoiles/jour), addyosmani/agent-skills (+816), GoogleChrome/modern-web-guidance-src (+739), CopilotKit/OpenBot (+298), QwenLM/qwen-code (+151), ashhart/TensorFold (moteur d'inférence Zig). Source : https://github.com/trending?since=daily

## 🧠 Mises à jour de Modèles

- **Gemini 4 Hydrogen** : voir Breaking. Gemini 4 Carbon (2 $/10 $ par M tokens) cité par un digest du 12 nov. (non confirmé par source primaire).
- **Qwen4** (Alibaba, 11 nov.) : fenêtre 1M tokens, orienté code/agents ; la preview Max s'arrête le 25 nov. Source secondaire — https://xenospectrum.com/en/qwen4-max-preview-specs-limitations/
- **Voix** : Chariot (12 nov., 11 langues indiennes + anglais) et DeepL Aure (11 nov., traduction voix-à-voix) — secondaires.
- Grok 4.8, promis pour le 10 nov., n'est toujours pas sorti (digest, non confirmé).

## 🔬 Research

RAS de vérifiable sur les dernières 24 h. À noter : DeepMind AlphaGenome 2 et Gemini Robotics 2.5 mentionnés par un digest, sans source primaire lue.

## 📝 À surveiller

- **GPT-6 Cyber (OpenAI)** : annoncé vers le 5–6 nov. (hors fenêtre 72 h), ExploitGym 48,5 % selon OpenAI, classé Critical dans le Preparedness Framework, accès limité aux clients Daybreak Red. Un post Reddit du jour cite des chiffres différents (77 % vs 39,2 % pour Mythos 5.2) : incohérence à clarifier. Livestream « Cyber at the Frontier » prévu le 12 nov., contenu non trouvé. https://openai.com/index/introducing-gpt-6-cyber/
- **Cursor / SpaceX / OpenAI** : OpenAI a prolongé temporairement l'accès de Cursor à ses modèles au-delà du 12 nov. https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
- **Mistral Large 4 « Le Chonk »** : poids ouverts publiés début nov., Mistral Studio agents en preview, rachat de SkipLabs (sources secondaires).
- **Meta** : Muse Ember (9–10 nov.) et rachat de Conductor (Conductor « is back » sur HN).
- **Financement** : Fractile 720 M$ Série C (7 Md$), Mercor 750 M$ Série D (20 Md$), Databricks Genie.
- **Marché** : repli lié à l'IA évoqué (plus de 600 Md$ de capitalisation perdus cette semaine selon un digest) ; avertissement d'un responsable de la Fed.
- **Reddit** : r/ClaudeAI — un jeu retiré de sous-reddits gamedev pour usage d'IA (1269 pts) ; HN — Apple Foundation Models framework, tension autour des revues d'apps assistées par IA.

## 📊 Résumé
- **Top 3 du jour** : 1) Gemini 4 Hydrogen + Orchestrator (Google) ; 2) Démission de Jensen Huang chez Nvidia ; 3) Anthropic IPO (prix le 18, cotation le 19 nov.).
- **À tester en priorité** : Gemini 4 Hydrogen (API/AI Studio/Antigravity) ; Edge0-145B en local (vérifier le matériel requis) ; openai/codex-security et addyosmani/agent-skills (GitHub).
