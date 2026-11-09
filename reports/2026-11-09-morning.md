# AI Watch — 2026-11-09 Matin

> Collecte : treg 4/4 sources, 17 recherches extended, GitHub Trending ok (9 repos seulement listés), 4 pages lues, 6 items confirmés par une deuxième source.

## 🔥 Breaking

### DeepSeek Harness : 1,54 M d'utilisateurs quotidiens
- **Quoi** : DeepSeek annonce que son app d'agent open source Harness atteint ~1,54 M d'utilisateurs/jour (271 k fin septembre), ~92 T tokens/jour, ~35 000 plugins tiers, marketplace de plugins prévue.
- **Date** : chiffres au 4 nov, relayés le 8-9 nov (post X de Cointelegraph, Seeking Alpha, Bloomberg)
- **Lien** : https://seekingalpha.com/news/4668771-deepseek-says-agent-app-tops-15m-daily-users-plans-plugin-marketplace
- **Pourquoi c'est important** : un agent open source chinois s'impose à grande échelle en moins de 3 mois ; chiffres auto-déclarés, non audités.
- **Testable** : Oui — app open source (lancée le 13 août).

### Nvidia : enquête indépendante du conseil sur Jensen Huang
- **Quoi** : le conseil d'administration ouvre une enquête après des informations selon lesquelles Jensen Huang aurait été la cible d'une opération de renseignement étrangère. Le conseil affirme n'avoir aucune raison de croire que des secrets aient été compromis.
- **Date** : 8 nov 2026
- **Lien** : https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors
- **Pourquoi c'est important** : gouvernance du principal fournisseur de GPU IA ; risque d'image et géopolitique.
- **Testable** : Non

### Anthropic : ~3,4 Md$ de générateurs gaz pour data centers
- **Quoi** : selon le FT (repris par Bloomberg), Anthropic s'engage sur 1,7 GW de générateurs gaz auprès d'OnePWR. Reuters n'a pas pu vérifier ; Anthropic n'a pas commenté.
- **Date** : 8 nov 2026
- **Lien** : https://www.bloomberg.com/news/articles/2026-11-08/anthropic-buys-power-for-ai-data-centres-in-3-4b-deal-ft-says
- **Pourquoi c'est important** : plus gros achat connu d'équipement électrique par un labo IA ; l'énergie devient le goulot d'étranglement.
- **Testable** : Non

## 🆕 Nouveaux Outils & Produits

### Vimoo 1.0 (vidéo, poids ouverts)
- **Quoi** : famille de modèles texte→vidéo et image→vidéo, Vimoo-1.0 (~12B) et Lite (~10B), variantes ComfyUI/MLX, licence Apache 2.0.
- **Date** : 8 nov 2026 (post X ; page Hugging Face mise à jour il y a ~2 jours)
- **Lien** : https://huggingface.co/Vimoo-AI
- **Pourquoi c'est important** : modèle vidéo open weights commercialisable. Sources surtout first-party, pas de benchmark indépendant vu.
- **Testable** : Oui — gratuit, open source, poids sur Hugging Face.

### llama-modchip (284B DeepSeek-V4-Flash sur 64 Go de RAM, sans GPU)
- **Quoi** : moteur d'inférence CPU qui fait tourner DeepSeek-V4-Flash (284B MoE, 13B actifs) en GGUF 1,71 bpw, ~57 Go de RAM à 256K de contexte ; 9-15 tok/s en génération, 44 tok/s en prefill (Ryzen 9 9955HX, AVX-512).
- **Date** : en tête de HN le 9 nov (v2.4.0)
- **Lien** : https://github.com/synchopate/llama-modchip
- **Pourquoi c'est important** : inférence locale de gros MoE sans GPU. Chiffres déclarés par l'auteur, aucune reproduction indépendante trouvée, marge mémoire très serrée.
- **Testable** : Oui — open source, nécessite 64 Go de RAM et AVX-512BW.

### Autres lancements Product Hunt / GitHub Trending (agents)
- NoMac (Mac cloud facturé à la minute pour agents IA, 128 votes), outages.live (flux d'incidents gratuit pour agents, 98 votes), Agent Clan (piloter Claude Code/Codex par gestes, 93 votes) : https://www.producthunt.com/products/nomac
- GitHub Trending : vercel-labs/agent-browser (CLI d'automatisation navigateur pour agents, Rust), anthropics/skills, ranxianglei/billion-context (compression de contexte).
- **Testable** : Oui pour tous.

## 🧠 Mises à jour de Modèles
RAS dans les dernières 72 h confirmé par une source primaire. Voir « À surveiller » pour Inkling 2 Small (5 nov), GPT Image 2.6 (4 nov) et Gemini Omni 1.2 Flash (5 nov).

## 🔬 Research
RAS confirmé. Un newsletter cite un audit METR sur l'accélération de la recherche d'Anthropic par l'IA, mais sans source primaire vérifiée.

## 📝 À surveiller
- **Inkling 2 Small (Thinking Machines)**, 5 nov : MoE 594B/17B actifs, contexte 1M, 0,30 $/1,00 $ par M de tokens sur Tinker ; poids Apache 2.0 promis ~1 semaine plus tard après tests de sécurité. https://www.marktechpost.com/2026/11/05/thinking-machines-inkling-2-small-release/
- **Goldman Sachs limite Claude Code/GitHub aux ingénieurs** (Bloomberg, début nov ; 660 pts sur HN). https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers
- **Sécurité Claude Code « Don't Ask Again »** (Apiiro, 5 nov) : 1 122 fichiers publics `.claude/settings.local.json` contenant de vrais secrets sur 104 185 copies. Vérifiez vos dépôts. https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again
- **Meta rachète Conductor** (4 nov) ; service cloud en lecture seule le 13 nov, arrêt le 20 nov. https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/
- **Anthropic** : IPO roadshow annoncé, incident d'accès tiers non autorisé aux systèmes internes signalé aux clients entreprise (source unique, agrégateur).
- **OpenAI** : ChatGPT Images 2.6 (Flare/Sunburst, 4 nov), partenariat Hacktron, 11 Md$ de financement rapportés (agrégateurs seulement).
- **Gemini Omni 1.2 Flash** GA le 5 nov ; **Gemini 4 Carbon** (28 oct) réservé aux défenseurs cyber.
- **Voix** : AssemblyAI-TTS-1, Cartesia Managed Agents (semaine du 26 oct-1 nov).
- **Starship Flight 15** prévu le 13 nov (hors IA).

## 📊 Résumé
- **Top 3 du jour** : 1) DeepSeek Harness à 1,54 M d'utilisateurs/jour ; 2) fuite de secrets via Claude Code « Don't Ask Again » ; 3) Anthropic ~3,4 Md$ de générateurs (à confirmer).
- **À tester en priorité** : Vimoo 1.0 (open weights Apache 2.0), llama-modchip (si 64 Go + AVX-512), vercel-labs/agent-browser ; auditez vos `.claude/settings.local.json`.
