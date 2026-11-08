# AI Watch — 2026-11-08 Matin

> Collecte : treg 4/4 sources, 15 recherches extended, GitHub Trending ok, 4 pages lues, 5 items confirmés par une deuxième source.

## 🔥 Breaking

### OpenAI GPT-6 Cyber
- **Quoi** : Modèle orienté recherche en sécurité, classé « Critical » en cybersécurité dans le Preparedness Framework d'OpenAI ; 48,5 % sur ExploitGym (32,1 % pour GPT-5.6 Cyber) et 99,93 % de respect du périmètre (94,49 % avant).
- **Date** : 5-6 novembre 2026 (les sources divergent d'un jour)
- **Lien** : https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html (annonce : https://openai.com/index/introducing-gpt-6-cyber/)
- **Pourquoi c'est important** : OpenAI dit qu'il a servi à trouver 948 exploits d'élévation de privilèges Linux, 81 failles Firefox et une faille critique dans Brotli (CVE-2026-111497). Premier modèle qu'OpenAI classe « Critical » en cyber.
- **Testable** : Non. API et Codex réservés à des clients vérifiés « Daybreak Red ». Payant, fermé.

### Claude Code : « Yes, and don't ask again » enregistre des secrets en clair
- **Quoi** : Apiiro a trouvé 1 122 fichiers `.claude/settings.local.json` publics contenant un vrai secret sur 104 185 copies. Avec l'historique git, les settings partagés et les transcripts : 2 539 secrets dans 1 994 dépôts, 63 organisations.
- **Date** : 5 novembre 2026 (en tête de Hacker News le 7-8)
- **Lien** : https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again (relayé par https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)
- **Pourquoi c'est important** : L'option enregistre la commande exacte, mot de passe compris, dans un fichier non ignoré par git. Un correctif côté Anthropic est évoqué par une seule source secondaire, non vérifié.
- **Testable** : Oui. Chercher `.claude/settings.local.json` et `.claude/settings.json` dans vos dépôts et leur historique git. Si un secret y figure, le renouveler d'abord et nettoyer ensuite.

### Gemini Omni 1.2 Flash (Google)
- **Quoi** : Vidéo générée et éditée jusqu'à 15 s (10 s avant), édition conversationnelle sur toute la durée, environ 0,07 $/s en 720p (-30 %), meilleure cohérence visages et marques, SynthID.
- **Date** : 5 novembre 2026
- **Lien** : https://the-decoder.com/googles-gemini-omni-1-2-flash-stretches-ai-video-clips-to-15-seconds-and-cuts-pricing-by-30-percent/ ; https://workspaceupdates.googleblog.com/2026/11/gemini-omni-12-flash-now-in-vids-with-15second-generations-and-improved-quality.html
- **Pourquoi c'est important** : Baisse de prix et clips plus longs sur un modèle disponible partout (API, AI Studio, Vertex, Flow, Vids, Ads).
- **Testable** : Oui, via Gemini API / AI Studio. Payant, fermé.

## 🆕 Nouveaux Outils & Produits

### Meta Muse : voix temps réel et avatars (Muse Realtime Voice / Avatar)
- **Quoi** : Conversations vocales interruptibles et avatar animé, un seul système en streaming ; appels vidéo avec avatar. Un article rapporte un avatar distillé passant de 120 à 2 étapes de calcul, 12 sessions par GB200, ~870 ms jusqu'à la première image.
- **Date** : 5 novembre 2026
- **Lien** : https://www.unite.ai/meta-brings-real-time-voice-and-expressive-avatars-to-muse/
- **Pourquoi c'est important** : Voice AI vers l'agent-avatar grand public. Aucune info sur le prix, la rétention des données ou le contrôle parental.
- **Testable** : Oui, pour les utilisateurs US (mobile, web, Mac).

### ChatGPT Images 2.6 (GIFs, images de référence, API)
- **Quoi** : Création de GIF animés, images de référence réutilisables, deux nouveaux modèles API (GPT Image 2.6 Flare, vitesse, et Sunburst, qualité) annoncés 50 % plus rapides. 248 votes sur Product Hunt.
- **Date** : 4 novembre 2026
- **Lien** : https://community.openai.com/t/images-upgraded-introducing-chatgpt-images-2-6/1412901
- **Pourquoi c'est important** : Génération plus rapide côté API, et GIF natifs.
- **Testable** : Oui (ChatGPT et API). Payant.

### Qoduck, modèle « stealth » dans Alibaba Qoder
- **Quoi** : Modèle de code sans origine déclarée, gratuit dans un quota quotidien pour les comptes individuels, pour une durée limitée. La communauté pense à Qwen 4, **non confirmé** (Alibaba Cloud : « Don't ask where it came from »).
- **Date** : 7 novembre 2026
- **Lien** : https://x.com/alibaba_cloud/status/2118992047613080032 ; https://startupfortune.com/alibabas-qoder-makes-a-mystery-coding-model-called-qoduck-free-to-use/
- **Pourquoi c'est important** : Teaser Qwen « The becoming begins » la veille ; Qwen 4 serait en entraînement selon Alibaba (septembre).
- **Testable** : Oui, via le sélecteur de modèle de Qoder International. Gratuit (limité), IDE fermé.

### Mistral Studio : agents managés, apps, workflows + rachat de SkipLabs
- **Quoi** : Agents managés et apps en preview publique, workflows en GA sur Mistral Cloud, déploiement privé/on-prem fin novembre. Acquisition de SkipLabs (génération de code, prix non communiqué).
- **Date** : 5 novembre 2026
- **Lien** : https://fourweekmba.com/ai-mistral-adds-managed-agents-and-apps-to-its-studio-platform/ ; https://www.ventureatlas.org/news/2026-11-05-mistral-skiplabs
- **Pourquoi c'est important** : Mistral monte en gamme vers l'agentique d'entreprise. Sources secondaires uniquement.
- **Testable** : Oui (preview publique de Studio). Payant.

### Autres lancements du jour (Product Hunt)
- Exa Monitors v2 (recherche web planifiée qui déclenche un agent, 2 $ / 1 000 exécutions), LiveReview (revue de code gratuite avec auto-approbation des changements à faible risque), Framer AI Agents (966 votes). Liens : https://www.producthunt.com/products/exa-ai ; https://www.producthunt.com/products/livereview ; https://www.producthunt.com/products/framer

## 🧠 Mises à jour de Modèles
- Voir GPT-6 Cyber, Gemini Omni 1.2 Flash, Images 2.6 et Qoduck ci-dessus.
- Mistral Large 4 (1 000 Md de paramètres) : poids ouverts publiés le 29 octobre, hors fenêtre de 72 h, voir « À surveiller ».
- Le reste : RAS confirmé. Des trackers signalent DeepSeek v4-flash (5 nov), Tencent Hy4 (3 nov) et Kling VIDEO 4.0, mais sans confirmation fiable.

## 🔬 Research
- **Anthropic, « The Components of Agent Memory »** : le « dreaming » (réorganisation de la mémoire en temps mort, inspirée du sleep-time compute) et ses évaluations. 154 pts sur HN. https://www.anthropic.com/research/components-of-agent-memory — Testable : non (méthode).
- **METR / Anthropic** : METR estime que les progrès de benchmark d'Anthropic vont environ 1,9× plus vite qu'avant octobre 2025 ; Anthropic a masqué une partie des preuves du rapport. Source secondaire, à confirmer : https://the420.in/anthropic-metr-ai-research-acceleration-report-redactions
- **Fin du groupe AI Frontiers de Microsoft Research** : John Langford annonce la fin du groupe (~50 personnes, auteurs d'AutoGen et Fara) et son départ, après son rattachement à Microsoft AI. 423 pts sur HN. https://hunch.net/?p=13764006 — à noter pour qui dépend d'AutoGen.
- **MaxxBench** : critique de la fiabilité du score DeepSWE (229 pts HN). https://maxxbench.unlap.ai/research/why-maxxbench/ — non lu.

## 📝 À surveiller
- **Qwen 4** : probablement derrière Qoduck, aucune confirmation officielle ni poids publiés.
- **Introduction en bourse d'Anthropic** : dossier déposé, Nasdaq visé mi-novembre, valorisation évaluée entre 1 et 1,5 T$ selon les sources (informations contradictoires, sources secondaires).
- **Sécurité MCP** : des agents de code installent des serveurs MCP dépréciés qui ne seront jamais corrigés (Help Net Security, 3 nov). https://www.helpnetsecurity.com/2026/11/03/mcphantom-deprecated-mcp-servers/
- **Rumeurs de financement non confirmées** : Thinking Machines Lab (~5 Md$ à 40 Md$ pré-money), Traversal (120 M$), CrowdStrike (rachat de deux startups de sécurité IA, 495 M$ au total).
- **DeepMind** : un digest évoque une cryptanalyse assistée par IA rendant la falsification de signatures RSA-1024 environ 1 600× moins chère. Non vérifié, source unique.
- **Mistral Large 4** (poids ouverts, 29 oct) et **Meta Muse Video / Image** (annoncés, pas encore disponibles).

## 📊 Résumé
- **Top 3 du jour** : (1) fuite de secrets via « don't ask again » de Claude Code ; (2) GPT-6 Cyber classé « Critical » ; (3) Gemini Omni 1.2 Flash (vidéo 15 s à 0,07 $/s).
- **À tester en priorité** : auditer vos `.claude/settings*.json` ; Qoduck dans Qoder (gratuit) ; Gemini Omni 1.2 Flash via AI Studio ; Images 2.6 en API.

### GitHub Trending (open source)
- cloudflare/security-audit-skill (+2 085 aujourd'hui) : skill d'audit de sécurité multi-phases pour agents de code. https://github.com/cloudflare/security-audit-skill
- milind-soni/OpenMausBot (+1 955) : alternative open source à un bot Grok, avec VM. https://github.com/milind-soni/OpenMausBot
- mattpocock/skills (+1 100), google/skills (+443), anthropics/skills (+390) : les « skills » d'agents sont la tendance dominante.
- vercel-labs/agent-browser (+190, Rust) : CLI d'automatisation de navigateur pour agents. https://github.com/vercel-labs/agent-browser
- Communauté : agent local open source de surveillance par téléphone (r/LocalLLaMA, 293 pts).
