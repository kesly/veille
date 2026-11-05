# AI Watch — 2026-11-05 Matin

> Collecte : 20 recherches extended, GitHub Trending ok, 7 items confirmés par une deuxième source.

## 🔥 Breaking

### ChatGPT Images 2.6 + GPT-Image-2.6 Flare / Sunburst
- **Quoi** : OpenAI ajoute création de GIF animés et images de référence réutilisables dans ChatGPT/Codex, plus deux modèles API (Flare = rapide, ~6 s ; Sunburst = qualité, cohérence d'édition, export SVG). ~50 % plus rapide.
- **Date** : 2026-11-04
- **Lien** : https://openai.com/index/introducing-images-2-6/
- **Pourquoi c'est important** : saut de vitesse et édition/SVG en API ; OpenAI revendique >4 Md d'images/semaine (chiffre secondaire). Prix : sources contradictoires (non divulgués vs identiques à 2.5).
- **Testable** : Oui — ChatGPT (web/desktop/mobile) et API payante.

### Kimi K3.1 Pro — poids ouverts publiés
- **Quoi** : Moonshot publie sur Hugging Face les poids de Kimi K3.1 Pro (MoE 2,8T total / 104B actifs, contexte 1M, multimodal), lancé en API le 23 oct.
- **Date** : 2026-11-04
- **Lien** : https://x.com/Kimi_Moonshot/status/2118010528123773297
- **Pourquoi c'est important** : plus gros modèle open-weight de classe frontière ; Moonshot annonce 65,7 % sur Terminal-Bench 4.0 (vs 66,4 % pour Opus 5.5) — chiffres constructeur. Licence non confirmée (voir model card).
- **Testable** : Oui via API/Ollama ; en local il faut ~8 GPU B300 (~1,56 To).

### Meta rachète Conductor
- **Quoi** : Meta acquiert Conductor (app Mac pour exécuter plusieurs agents de code en parallèle) ; l'équipe rejoint Meta Superintelligence Labs.
- **Date** : 2026-11-04
- **Lien** : https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/
- **Pourquoi c'est important** : consolidation des outils d'orchestration d'agents de code. Conductor Cloud passe en lecture seule le 13/11, fermeture le 20/11.
- **Testable** : Oui, jusqu'au 20/11 (produit existant).

### OpenAI rachète Pierre Computer (Code Storage)
- **Quoi** : OpenAI va acquérir Pierre, éditeur de Code Storage (hébergement Git pour agents) et des libs open source Trees/Diffs déjà dans Codex.
- **Date** : 2026-11-04
- **Lien** : https://aiweekly.co/ai-news-today/openai-news
- **Pourquoi c'est important** : backend Git natif pour Codex ; deal pas encore clos, prix non divulgué, libs censées rester open source.
- **Testable** : Non (Trees/Diffs open source déjà utilisables).

## 🆕 Nouveaux Outils & Produits

### Cognition SWE-2 Flash
- **Quoi** : modèle de code MoE 276B/12B actifs (post-entraîné depuis Inkling-Small), 3× plus rapide et 5× moins cher que SWE-2.
- **Date** : 2026-11-04
- **Lien** : https://cognition.com/blog/swe-2-flash
- **Pourquoi c'est important** : modèle de code agentique bon marché ; chiffres de Cognition non vérifiés, poids non publiés.
- **Testable** : Oui — Devin Desktop et Devin CLI, gratuit jusqu'au 30/11 (selon une source secondaire).

### VS Code 1.145
- **Quoi** : agents distants (preview), automations avec expressions cron (locales), sessions mêlant Claude/Codex/Copilot, contrôles de verbosité.
- **Date** : 2026-11-04
- **Lien** : https://visualstudiomagazine.com/articles/2026/11/04/vs-code-1-145-expands-remote-agent-workflows-adds-cron-automations.aspx
- **Pourquoi c'est important** : l'IDE devient un orchestrateur multi-agents planifiable. Gratuit, open source.
- **Testable** : Oui — mise à jour VS Code stable.

### Xcode 27.3 beta 1
- **Quoi** : GitHub Copilot ajouté à l'assistant de code intégré ; Siri AI ouvert aux développeurs en preview.
- **Date** : 2026-11-03
- **Lien** : https://9to5mac.com/2026/11/03/xcode-27-3-adds-github-copilot-to-its-built-in-coding-assistant/
- **Pourquoi c'est important** : Apple s'ouvre aux assistants tiers. Le volet Siri vient d'un seul digest.
- **Testable** : Oui, compte développeur Apple (beta).

## 🧠 Mises à jour de Modèles
- Kimi K3.1 Pro et SWE-2 Flash : voir ci-dessus.
- Mistral Large 4 (1T paramètres, poids ouverts le 29/10) : hors fenêtre 72 h, voir « À surveiller ».
- Google, Meta, DeepSeek : sorties « attendues » citées par un blog peu fiable, non confirmées.

## 🔬 Research

### Anthropic FlashProve (inférence prouvable)
- **Quoi** : prototype open source (Apache 2.0, zkSNARK) prouvant cryptographiquement qu'une réponse vient d'un modèle donné ; démontré sur Llama 4 Maverick (400B MoE). Avec EPFL, MIT, StarkWare.
- **Date** : 2026-11-04 (TechCrunch le 11-03)
- **Lien** : https://www.anthropic.com/research/provable-inference
- **Pourquoi c'est important** : base pour vérifier l'identité d'un modèle (anti-substitution). Surcoût élevé (~70-95× selon sources secondaires) ; aucun déploiement prévu.
- **Testable** : Oui sur GPU (repo GitHub, poids Llama à récupérer soi-même).

### Décodage spéculatif et distribution des sorties
- **Quoi** : papier (MIT, Princeton, Northeastern…) montrant que le décodage spéculatif décale la distribution de sortie des modèles open-weight sur tâches agentiques longues.
- **Date** : ~2026-11-04
- **Lien** : https://aiweekly.co/ai-news-today
- **Pourquoi c'est important** : à vérifier, une seule source agrégateur.
- **Testable** : Non.

## 📝 À surveiller
- **Mistral Large 4** (poids ouverts 29/10, 1T params, collaboration NVIDIA annoncée le 4/11) : https://en.cryptonomist.ch/2026/11/03/mistral-large-4-ai-model/
- **Anthropic IPO** : S-1 déposé le 26/10, introduction attendue ce mois-ci (CNN) ; nouvelle règle d'usage contre les abus envers Claude.
- **Google** : les modèles Pro quittent le forfait AI Plus (4,99 $) le 13/11 ; Search des écoles K-12 conditionné aux outils IA de Google (rapporté).
- **Financements** : Fal 1,3 Md$ (valo 16 Md$), Instinct 1 Md$ Série C (10 Md$), Nooks 500 M$, EliseAI 350 M$ ; Isomorphic Labs en discussion pour ~5 Md$. Rapportés par un agrégateur.
- **AMD–Meta** (jusqu'à 60 Md$ de puces sur 5 ans) et rachat de Taalas par AMD (~2,9 Md$) : non confirmés par source primaire.
- **Sécurité des agents** : CrowdStrike « kill switch » pour agents, Apple restreint l'accès disque complet.
- **Noms douteux** (GPT-6.1 Terra, Gemini 4 Carbon, « GPT-6 Astra conçoit un appareil ») : non corroborés, ignorés.
- **Voix** : rien de neuf confirmé (Convoso agent vocal no-code GA le 2/11 ; ElevenLabs v4 et Deepgram Flux TTS sont plus anciens). Vidéo/image hors OpenAI : RAS daté du jour (VideoGen Model 1 du 20/10, Gemini Omni sans date).

## 📊 Résumé
- **Top 3 du jour** : 1) Kimi K3.1 Pro en open weights ; 2) ChatGPT Images 2.6 + modèles API Flare/Sunburst ; 3) vague de rachats d'outils d'agents de code (Meta–Conductor, OpenAI–Pierre).
- **À tester en priorité** : VS Code 1.145 (agents distants, cron) ; SWE-2 Flash dans Devin CLI (gratuit jusqu'au 30/11) ; Images 2.6 dans ChatGPT ; Conductor avant sa fermeture du 20/11.

### GitHub Trending (jour)
- NVIDIA/auto-ontology (Python, +2 050) — couche de raisonnement sémantique en graphe pour agents.
- vercel-labs/agent-desktop (Rust, +2 470) — CLI pour que des agents pilotent un ordinateur.
- thedotmack/claude-mem (TS, +1 172) — mémoire persistante pour agents de code.
- mattpocock/skills (Shell, +1 379) — collection de skills d'agents.
- max-sixty/worktrunk (Rust, +531) — gestion de Git worktrees pour agents parallèles.
- garrytan/gstack (TS, +290), github/spec-kit (Python, +808), FareedKhan-dev/kimi-k3-in-c (C, +351 — inférence Kimi en C99 sur CPU).
