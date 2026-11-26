# AI Watch — 2026-11-26 Matin

> Collecte : treg 4/4 sources, 13 recherches extended, GitHub Trending ok, 3 pages lues, 4 items confirmés par une deuxième source.

## 🔥 Breaking

### Google Workspace : serveurs MCP et CLI en disponibilité générale
- **Quoi** : Google rend GA ses serveurs MCP hébergés (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat, Tasks) et un CLI Workspace officiel. Les agents IA devront passer par MCP et non plus par REST à partir du 1er février 2027.
- **Date** : 2026-11-24
- **Lien** : https://developers.google.com/workspace/guides/configure-mcp-servers (guide) ; https://workspace.google.com/blog/product-announcements/built-for-trust-and-control-new-ai-agent-protections-and-developer-tools-in-google-workspace
- **Pourquoi c'est important** : MCP devient la voie obligatoire pour les agents sur les données Workspace. Un palier gratuit existe, un palier payant démarre le 1er avril 2027 (le plafond gratuit de 5 000 requêtes/jour n'est cité que par un média, non confirmé).
- **Testable** : Oui, pour les clients Workspace. Déploiement progressif sur 2 semaines, contrôles admin dans la console (API Controls).
- **Confirmation** : plusieurs médias (Dataconomy, UC Today, Sulat, etc.) ; blog Google vu en résultat de recherche, non lu directement.

### Anthropic : Skills over MCP (bêta publique) et MCP Tasks/Elicitation GA
- **Quoi** : les serveurs MCP peuvent livrer des instructions de workflow (skills) avec leurs outils ; MCP Tasks et Elicitation passent GA dans Claude.
- **Date** : 2026-11-24
- **Lien** : https://venturebeat.com/technology/mcp-servers-can-now-deliver-ai-agent-skills-changing-what-companies-approve-when-they-connect-one ; https://grafy.ai/news/anthropic-introduces-skills-over-mcp-to-automate-ai-workflows
- **Pourquoi c'est important** : la spec signale elle-même un risque d'injection de prompt via les instructions fournies par le serveur. Ce qu'une entreprise approuve en connectant un serveur change.
- **Testable** : Oui, en bêta dans Claude et Claude Code.
- **Confirmation** : VentureBeat + Grafy.

### Google « Cogentic » : 6 papiers de maths générés par agents (factorisation, log discret)
- **Quoi** : Google Research publie dans son dépôt des papiers produits par l'agent Cogentic, dont une factorisation d'entiers « inconditionnelle » en L_N[1/3] et un log discret. Les autres couvrent équilibres de Nash approchés, reconstruction de graphes et conjecture log-rank.
- **Date** : 2026-11-25
- **Lien** : https://github.com/google-research/google-research/tree/master/cogentic_research_papers ; https://www.rdworldonline.com/google-cogentic-ai-integer-factoring-bounds-lean-proofs/
- **Pourquoi c'est important** : si c'est valide, c'est un résultat algorithmique majeur sur la factorisation. La borne est sous-exponentielle, pas polynomiale : ça ne casse pas RSA en pratique.
- **Testable** : Non (papiers). Rien n'est relu par des pairs ; les sources se contredisent sur la vérification Lean 4.
- **Confirmation** : HN (461 pts), dépôt GitHub lu, plusieurs médias.

### OpenAI : lot de preprints maths (ω = 9/4, conjecture de Hirsch polynomiale fausse, FFT)
- **Quoi** : OpenAI a posté ~9 manuscrits le 24 novembre, dont ω = 9/4 pour la multiplication matricielle (borne inférieure), un contre-exemple à la conjecture de Hirsch polynomiale et la complexité de la FFT en N(log N)^(1/2+o(1)). Scott Aaronson les évoque, avec des preuves VP ≠ VNP d'OpenAI et d'Anthropic et une preuve de l'hypothèse de Riemann (Alpöge/Anthropic) citées dans son billet. Je n'ai pas vérifié ces dernières.
- **Date** : 2026-11-24
- **Lien** : https://scottaaronson.blog/?p=10379 ; https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf
- **Pourquoi c'est important** : si ça tient, l'IA produit des résultats de premier plan en théorie de la complexité. Un autre claim d'OpenAI (conjecture de Connes) est déjà contesté par un mathématicien.
- **Testable** : Non. Aucun de ces résultats n'est vérifié de façon indépendante. À traiter comme des allégations.
- **Confirmation** : blog Aaronson lu, Snape Report, HN.

## 🆕 Nouveaux Outils & Produits

### Canva MCP
- **Quoi** : serveur MCP Canva pour agents (160 votes PH). **Date** : 2026-11-25. **Lien** : https://www.producthunt.com/products/canva
- **Pourquoi c'est important** : suit la tendance MCP chez les éditeurs grand public. **Testable** : Oui.

### Airbot et MyClaw 3.0
- **Quoi** : Airbot est un « chief of staff » IA qui écrit en premier (259 votes) ; MyClaw 3.0 propose une équipe d'agents toujours active avec mémoire partagée (290 votes). **Date** : 2026-11-25. **Lien** : https://www.producthunt.com/products/airbots ; https://www.producthunt.com/products/myclaw-3-0
- **Pourquoi c'est important** : agents persistants grand public, tendance forte. **Testable** : Oui (tarifs non vérifiés).

### MAGI-2 (Sand AI) — vidéo
- **Quoi** : modèle de génération vidéo de 480B paramètres (87 votes). **Date** : 2026-11-25. **Lien** : https://www.producthunt.com/products/magi-1
- **Pourquoi c'est important** : gros modèle vidéo annoncé ; licence et accès non vérifiés. **Testable** : à vérifier.

### Apple FastFrames — vidéo
- **Quoi** : deux modèles de diffusion vidéo autorégressifs (1,3B et 14B), 480p, environ 35 ms de latence pour le petit. **Date** : 2026-11-25. **Lien** : https://hn.today/s/fastframes-video-generation-at-interactive-latency
- **Pourquoi c'est important** : vidéo à latence interactive. **Testable** : à vérifier (source unique, agrégateur).

### Open source trending (GitHub)
- **minimind** (https://github.com/jingyaogong/minimind) : LLM de 64M paramètres entraîné en ~2 h. Open source. Testable.
- **firecrawl** (https://github.com/firecrawl/firecrawl) : recherche/scraping pour agents, 550+ fournisseurs de données. Open source avec offre cloud payante.
- **HKUDS/CLI-Anything** (https://github.com/HKUDS/CLI-Anything) : rend tout logiciel utilisable par agents via CLI.
- **obra/superpowers** (https://github.com/obra/superpowers) : framework de skills pour agents de code.
- **last30days-skill** (https://github.com/mvanhorn/last30days-skill) : skill de recherche multi-sources.
- Note : Claude-BugHunter (1 652 étoiles/jour) est un bundle de skills de red team, à utiliser seulement sur des cibles autorisées.

## 🧠 Mises à jour de Modèles
- RAS de confirmé pour le 25 novembre. Rappels hors fenêtre de 72 h, issus de trackers incohérents entre eux : GPT-6.2 Astra/Sol (17/11), Gemini 4 Neon (18/11), Claude Fable 5.2 / Mythos 5.2 (9/11). Un benchmark HN (284 pts) montre GPT-6.2 Astra battant les records de code golf de Googlers : https://bjin.github.io/go-codegolf-benchmark/ (page lue, auteur individuel).
- Reddit r/ClaudeAI : un post à 284 pts demande s'il a été routé vers « Opus 5.6 ». Rumeur non confirmée.

## 🔬 Research
- Voir Cogentic et preprints OpenAI ci-dessus (non vérifiés).
- Reddit r/MachineLearning : « Research agents set 50 packing problem records » et LoomFormer (attention par tête). Faible traction (30 pts environ), source unique.
- Anthropic « Siren » : test honeypot pré-release pour agents qui dérivent (source : agrégateur aiweekly, non confirmée).

## 📝 À surveiller
- **ElevenLabs** : rachat de Kotoba (~100 M$, Nikkei) et levée en cours à 33 Md$ (Bloomberg via SiliconANGLE). Reste à confirmer.
- **Marché** : un agrégateur évoque une baisse du Nasdaq de ~4 % liée à l'IA, et l'IPO Anthropic (83 $/action) passée sous son prix d'introduction. Source unique, non vérifié.
- **Sécurité** : OX Security (MCP : près d'un tiers des serveurs sans propriétaire traçable) ; 1Password et Defang ont publié des incidents de sécurité (HN, hors IA) ; un contenu rapporte une intrusion à Treasury/CIA avec un outil IA défensif détourné (source unique, non confirmée).
- **Reddit** : post à 717 pts « Anthropic Ex-Employee: Claude sabotages research work » : allégation non vérifiée.
- **Voix** : Together AI Qwen3 TTS (20 $/M caractères, 20/11), AssemblyAI-TTS-1 (27/10), Microsoft MAI Voice 2, Gradium Phonon (TTS on-device open source). Pas de lancement majeur du jour.
- **Annonces rapportées** : Genesis AI (500 M$ Series A), Nvidia en discussion pour Inception (500 M$+), Meta Muse dans les DMs Instagram avec Walmart Agent Gateway.
- Le NYT déconseille aux photographes de mettre à jour Photoshop à cause des fonctions IA (HN 257 pts) : https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features

## 📊 Résumé
- **Top 3 du jour** : 1) Google Workspace MCP GA et obligation MCP au 1er février 2027 ; 2) Cogentic de Google et preprints maths d'OpenAI (résultats spectaculaires, non vérifiés) ; 3) Anthropic Skills over MCP, avec son risque d'injection.
- **À tester en priorité** : serveurs MCP Workspace et CLI (gratuit) ; Skills over MCP dans Claude Code (bêta) ; minimind (open source) ; firecrawl.
