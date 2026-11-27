# AI Watch — 2026-11-27 Matin

> Collecte : treg 4/4 sources, 16 recherches extended, GitHub Trending ok, 4 pages lues, 3 items confirmés par une deuxième source.

## 🔥 Breaking

### Google Workspace : serveurs MCP GA + obligation pour les agents IA
- **Quoi** : Google rend GA ses 8 serveurs MCP Workspace (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat, Tasks) et le CLI `gwscli`. Un nouvel addendum aux CGU impose aux outils « pilotés par un agent IA » de passer par ces MCP/CLI au lieu des API REST (application technique le 1er février 2027). Le serveur Gmail ne peut pas envoyer d'e-mail (accès partenaire requis). Tier gratuit plafonné à 5 000 requêtes/jour/projet/produit, facturation du tier payant à partir du 1er avril 2027 (chiffres de sources secondaires).
- **Date** : 24 novembre 2026 (discussion HN le 26-27)
- **Lien** : https://workspace.google.com/blog/product-announcements/built-for-trust-and-control-new-ai-agent-protections-and-developer-tools-in-google-workspace — analyse : https://techstackups.com/articles/google-workspace-ai-agents-mcp/
- **Pourquoi c'est important** : premier grand éditeur qui contraint contractuellement les agents à passer par MCP ; impact direct sur tout assistant e-mail/agent de code utilisant l'API Gmail/Drive, avec rétention des embeddings limitée à 30 jours et entraînement sur les données interdit.
- **Testable** : Oui — gratuit (tier Standard), serveurs MCP distants et CLI à brancher sur un agent.

## 🆕 Nouveaux Outils & Produits

### Hub (Product Hunt, 367 votes)
- **Quoi** : outil open source pour piloter une centaine de sessions Claude Code / Codex en parallèle.
- **Date** : 26-27 novembre 2026
- **Lien** : https://www.producthunt.com/products/hub-20
- **Pourquoi c'est important** : l'orchestration multi-agents de code devient une catégorie (voir aussi DeskFleet 88 votes, AgentDE 68 votes).
- **Testable** : Oui — open source.

### Pax by Pydantic (125 votes)
- **Quoi** : agent de code où « même le code est un plugin ».
- **Date** : 26-27 novembre 2026
- **Lien** : https://www.producthunt.com/products/pydantic
- **Pourquoi c'est important** : nouvel entrant de l'équipe Pydantic sur les agents de code extensibles.
- **Testable** : Oui (détails de licence/prix non vérifiés).

### QA.tech MCP (194 votes)
- **Quoi** : serveur MCP qui fait vérifier chaque changement depuis l'IDE par des agents QA.
- **Date** : 26-27 novembre 2026
- **Lien** : https://www.producthunt.com/products/qa-tech
- **Pourquoi c'est important** : boucle de vérification automatique pour les agents de code.
- **Testable** : Oui (prix non vérifié).

### GitHub Trending (open source)
- **Quoi** : dominé par l'écosystème « skills » d'agents : `elementalsouls/Claude-BugHunter` (+1 597 étoiles/jour), `obra/superpowers` (+854), `HKUDS/CLI-Anything` (+746, rendre tout logiciel pilotable par agent via CLI), `firecrawl/firecrawl` (+1 046), `cathrynlavery/diagram-design` (+955), `jingyaogong/minimind` (+702, entraîner un LLM ~64M de zéro).
- **Date** : 27 novembre 2026
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : la dynamique open source est aux skills/plugins d'agents plutôt qu'aux modèles.
- **Testable** : Oui — tous open source.

### AMD-specific fork de llama.cpp (HN 305 pts)
- **Quoi** : fork de llama.cpp optimisé pour GPU AMD.
- **Date** : 26-27 novembre 2026
- **Lien** : https://devnull.land/amd-specific-llama-cpp
- **Pourquoi c'est important** : inférence locale sur matériel AMD.
- **Testable** : Oui — open source.

## 🧠 Mises à jour de Modèles
- **OpenAI** : ChatGPT et Codex partageront un seul quota d'usage (Plus, Pro, Business) à partir de décembre ; Instant chat exempté (source : aide OpenAI via Android Authority, https://www.androidauthority.com/chatgpt-codex-shared-usage-limits-3739254/). Un billet d'analyse (https://micjm.com/blog/openai-is-in-cost-control-mode/, HN 301 pts) estime que Astra 6.2 et Sol 6.2 « sous-réfléchissent » par rapport à leurs prédécesseurs (réglage coût) ; une seule source, méthode non vérifiée.
- **Amazon Nova 2.0 Omni** : listé au 26 novembre par un tracker ; pas d'annonce éditeur vérifiée → à surveiller.
- **Mistral** : démo de Mistral Large 4 (zoom outil sur photo aérienne) le 26 novembre ; Mistral ouvre un siège APAC à Singapour (20 nov).
- Reste : RAS confirmé.

## 🔬 Research
- **DeepMind** : des agents IA contrôlent une partie du calcul des expériences pour le prochain Gemini (Koray Kavukcuoglu, podcast DeepMind) ; pas d'auto-amélioration récursive complète, humains en revue, pas de récompense sur la chaîne de pensée. Confirmé par plusieurs relais. https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/
- **Testable** : Non.
- Rumeurs HN/Reddit sur une preuve de factorisation d'entiers (Google Research) et une préimpression de gravité liée à OpenAI : non vérifiées, voir À surveiller.

## 📝 À surveiller
- **Claude Opus 5.6 (rumeur)** : des testeurs voient des sorties attribuées à un « Opus 5.6 » via une route « Opus 5.5 Extra » dans Claude Code/chat ; aucune annonce Anthropic, Opus 5.5 reste le dernier Opus (22 sept.). Dates de sortie spéculatives (fin décembre). https://www.testingcatalog.com/testers-share-early-results-possible-claude-opus-5-6/
- **OpenAI Private Inference / Chat+Work unifiés** : en test alpha selon des digests quotidiens ; non retrouvé dans une source primaire.
- **NYT / Photoshop** : le NYT déconseillerait aux photographes de mettre à jour Photoshop à cause de fonctions IA (HN 659 pts) — https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features (source unique, non confirmée).
- **Microsoft MAI Code 2 / Flash** (Ignite, ~19 nov), **Cognition Devin Bots** (17 nov), **Gemini 4** (variantes Argon/Hydrogen ; hausse de prix après le 30 nov, sources de blogs) : à confirmer.
- **Linger** (agent perso open source, ex-DeepSeek, 20 nov) et **Shirudo** (OpenAI + Cisco, runtime de protection Linux) : lancements récents open source.
- Rumeurs « P = NP résolu » et retrait d'un auteur de préimpression : non vérifiées, ignorer.
- Digests : FCC/SpaceX 1 M de satellites IA, ban des jouets IA à New York, arrêt d'expéditions de serveurs Nvidia (non confirmé).

## 📊 Résumé
- **Top 3 du jour** : 1) Google impose MCP/CLI aux agents Workspace (échéance 1er fév. 2027) ; 2) DeepMind confie une part de calcul à des agents pour Gemini ; 3) ChatGPT/Codex à quota unique en décembre + rumeur Opus 5.6.
- **À tester en priorité** : serveurs MCP Workspace / `gwscli` (gratuit), Hub (open source), `CLI-Anything` et `obra/superpowers` (open source).
