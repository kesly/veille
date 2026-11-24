# AI Watch — 2026-11-24 Matin

> Collecte : treg 4/4 sources (X : 0 post après filtre), 15 recherches extended, GitHub Trending ok, 3 pages lues, 5 items confirmés par une deuxième source.

## 🔥 Breaking

### GLM-5.4 (Z.ai), premier flagship « Loop Transformer »
- **Quoi** : modèle d'environ 750B (taille non confirmée par Z.ai) qui repasse deux fois sur un bloc de 28 couches partagées. Vision, contexte 1M tokens, +50 % de quota hebdo sur le Coding Plan.
- **Date** : 2026-11-23
- **Lien** : https://z.ai/blog/glm-5.4 — https://www.marktechpost.com/2026/11/23/zai-glm-5-4-loop-transformer/
- **Pourquoi c'est important** : Z.ai annonce un niveau comparable à des modèles de 2 à 3T de paramètres sans ajouter de paramètres. Aucun benchmark chiffré publié. Reddit r/LocalLLaMA juge le modèle excellent en code mais faible en écriture. Z.ai reconnaît des boucles de « marathon thinking » trop longues.
- **Testable** : Oui, via Z.ai Chat, ZCode et GLM Coding Plan (payant). API et poids ouverts : pas de date, après évaluation de sécurité.

### Anthropic : preuve annoncée de VP ≠ VNP, non vérifiée
- **Quoi** : papier de 70 pages attribué à Claude seul, avec une formalisation Lean 4 (324 fichiers). Il affirme des bornes inférieures superpolynomiales pour le polynôme du cycle hamiltonien sur tout corps, et pour le permanent hors caractéristique 2. Anthropic précise que cela ne résout pas P vs NP.
- **Date** : 2026-11-23 (environ 20h UTC)
- **Lien** : https://github.com/anthropics/formal-math/tree/main/vp-vnp — https://interestingengineering.com/ai-robotics/claude-proves-vp-not-vnp-valiant-conjecture
- **Pourquoi c'est important** : si le résultat tient, c'est un jalon majeur pour l'IA en mathématiques. Aucun mathématicien humain n'a vérifié. Lean valide les étapes, mais l'adéquation de l'énoncé formalisé à la conjecture n'a été jugée que par des IA. À traiter comme une revendication, pas comme un résultat établi.
- **Testable** : Oui, le dépôt est public (vérification Lean possible).

### OpenAI + Cisco : Shirudo (runtime open source eBPF)
- **Quoi** : « boucliers » eBPF générés par des agents (Codex) pour bloquer une faille sur un Linux en cours d'exécution, sans redémarrage. Démo : exploit Java4Shell bloqué sur un Elasticsearch.
- **Date** : 2026-11-23
- **Lien** : https://openai.com/index/introducing-shirudo/ — https://isovalent.com/blog/post/cisco-openai-shirudo
- **Pourquoi c'est important** : patcher prend des jours ou des semaines. Un correctif temporaire agentique réduit la fenêtre d'exposition. Le projet est pré-release et issu de Tetragon.
- **Testable** : Oui, open source sur GitHub (pré-release).

## 🆕 Nouveaux Outils & Produits

### Replit Missions
- **Quoi** : essaim d'agents IA qui travaille sous budget plafonné et règles d'approbation, avec un relecteur IA indépendant en fin de mission. Replit a aussi ouvert le code de DataCat, construit avec Missions.
- **Date** : 2026-11-17 (hors fenêtre 72 h, repris par Product Hunt le 23/11, 85 votes)
- **Lien** : https://www.producthunt.com/products/replit — https://www.technobezz.com/news/replit-missions-budgets-ai-agent-swarms
- **Pourquoi c'est important** : le modèle « objectif + budget » plutôt que « tâche ». Les accélérations annoncées (jusqu'à 19× avec 32 agents sur 13 tâches NumPy) viennent de Replit. Prix non communiqué.
- **Testable** : Oui (payant, enterprise sur contact).

### Perplexity Monitor API
- **Quoi** : surveillance planifiée du web pour agents, avec webhook uniquement quand un changement est pertinent. 1 $ pour 1 000 exécutions.
- **Date** : 2026-11-16 (hors fenêtre 72 h, repris le 23/11)
- **Lien** : https://www.perplexity.ai/hub/blog/introducing-perplexitys-monitor-api
- **Pourquoi c'est important** : brique de base pour des agents toujours actifs. Performances revendiquées par Perplexity uniquement.
- **Testable** : Oui, API payante.

### Product Hunt, outils agents à noter
- Polylane Swarms (129 votes, agents sur incidents de prod), Mobile Agent Testers (78 votes, open source, agents qui testent des apps mobiles), Plango (88 votes, agents qui tournent la nuit), Hydrilla (113 votes, assets 3D générés). Non vérifiés par une deuxième source.
- **Lien** : https://www.producthunt.com/products/polylane — https://www.producthunt.com/products/mobile-agent-testers
- **Testable** : Oui, voir les fiches.

### Open source / GitHub Trending (non vérifié ailleurs)
- Claude-BugHunter (+2 029 étoiles/jour, skills Claude Code pour le bug hunting), firecrawl (+924), obra/superpowers (+840), last30days-skill (+797), CLI-Anything (+790), minimind (+828, LLM 64M en 2 h).
- **Lien** : https://github.com/trending?since=daily
- **Testable** : Oui, tous open source.

## 🧠 Mises à jour de Modèles

### Inkling 2 Mini (Thinking Machines)
- **Quoi** : MoE bouclé de 26,4B (3,4B actifs), poids Apache 2.0, contexte 1M, tourne sur un Mac 32 Go.
- **Date** : 2026-11-20
- **Lien** : https://www.marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer/ — https://ollama.com/library/inkling-2-mini
- **Pourquoi c'est important** : tendance « looped » confirmée (GLM-5.4 trois jours plus tard). Scores maison élevés (SWE-bench Verified 79,2 %). L'évaluation indépendante d'Artificial Analysis est plus modeste (20 sur l'Intelligence Index).
- **Testable** : Oui, `ollama` / Hugging Face (open weights, gratuit).

### NariQ : Qwen3.8-27B niveau BF16 en 10 Go
- **Quoi** : GGUF quantifié de Qwen3.8-27B. Source unique (Hacker News, 139 pts).
- **Lien** : https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- **Testable** : Oui (open weights).

## 🔬 Research
- VP ≠ VNP : voir Breaking. Latent Introspection (les LLM détectent des concepts injectés) : https://arxiv.org/abs/2602.20031, source unique, 41 pts HN.

## 📝 À surveiller
- **Nvidia** : Jensen Huang est réinstallé PDG le 23/11 après sa démission du 12/11. Confirmé par le communiqué Nvidia (https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director), Bloomberg et CNN. Le contexte politique pèse (pression de l'administration Trump selon NBC/Bloomberg). L'action aurait gagné plus de 30 % sur la journée selon CNN. Hors cœur IA, mais impact majeur sur le secteur (2 270 pts HN).
- **Débat sur l'open source** : le post de Yann LeCun reprochant à Dario Amodei d'exagérer les dangers pour rendre les modèles open source illégaux fait 1 338 pts sur HN.
- **Financement** : Deutsche Telekom engage 100 M€ dans Mistral AI. AMD et HUMAIN annoncent un partenariat jusqu'à 10 Md$ (500 MW). Des banques syndiquent 63 Md$ liés au bail de puces Google d'Anthropic. Source : agrégateurs, non vérifié directement.
- **Claude Duet** (agent proactif d'Anthropic, preview le 21/10, aujourd'hui ouvert aux abonnés US Pro/Max/Ultra de la liste d'attente) : les résumés du 23/11 parlent d'un agent « nouveau », mais il s'agit probablement de re-couverture.
- **Gemini 4 Neon** (Google, environ 18/11) et **Kimi K3.1 Pro Prime** (20/11) : dates issues d'agrégateurs, non confirmées par les éditeurs.
- **Google** : abonnements Gemini AI Pro et Plus à moitié prix pour le Black Friday ; rétention des chats Gemini portée à 2 mois (17/11).
- **Sécurité** : Zero Data Retention avec Enterprise Frontier Safeguards en beta chez Anthropic (source unique, 3 pts HN). Outils d'audit de skills et de serveurs MCP (mcpseal, toolfence-scan) : très petits, sources uniques.
- **Voix** : rien de nouveau dans les 72 h. Derniers lancements notables (AssemblyAI TTS 27/10, ElevenLabs Scribe v3, Rime Prism, Liquid LFM3-Audio) sont plus anciens. FireVoice (Show HN, voice studio open source local) : source unique.
- **Image/vidéo** : RAS dans les 72 h confirmés (Kling 4.0 en octobre, LongCat Video Avatar 1.6 le 13/11).
- **Meta / Mistral** : RAS confirmé dans la fenêtre, hors le financement Deutsche Telekom.

## 📊 Résumé
- **Top 3 du jour** : 1) GLM-5.4, premier flagship Loop Transformer (avec Inkling 2 Mini, la tendance « looped »). 2) Revendication VP ≠ VNP par Claude, à vérifier. 3) Shirudo (OpenAI/Cisco), agents de sécurité Linux open source.
- **À tester en priorité** : Inkling 2 Mini via Ollama (gratuit, local) ; GLM-5.4 via Z.ai Chat ; le dépôt Lean de vp-vnp ; Shirudo sur GitHub ; Perplexity Monitor API.
