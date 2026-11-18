# AI Watch — 2026-11-18 Matin

> Collecte : treg 4/4 sources, 16 recherches extended, GitHub Trending ok, 4 pages lues (2 exploitables : OpenAI, Microsoft AI ; Tencent en erreur, claude.dev lu), 5 items confirmés par une deuxième source.

## 🔥 Breaking

### GPT-6.2 Astra et Sol (OpenAI)
- **Quoi** : deux nouveaux modèles : Astra (frontier, travail pro/science/cyber) et Sol (efficace, usage quotidien et code). 1,05M tokens de contexte rapporté.
- **Date** : 2026-11-17
- **Lien** : https://openai.com/index/introducing-gpt-6-2-astra-sol/ (confirmé par The Decoder, 9to5Mac, TestingCatalog)
- **Pourquoi c'est important** : Astra annonce 5,5 pts d'avance sur Claude Fable 5.2 sur Agents' Last Exam à 5 % du coût (chiffres OpenAI). Prix API Astra : 8 $ / 40 $ par M tokens (−20 %), Sol inchangé à 2 $ / 10 $. Tests indépendants (Artificial Analysis) plus mitigés : Astra ≈ GPT-6 Astra, Sol −3 pts vs 6.1 Sol. Cadre sécurité durci (cyber).
- **Testable** : Oui — ChatGPT Work et Codex (Plus/Pro/Enterprise/Edu), API `gpt-6.2-astra` / `gpt-6.2-sol`. Payant.

### Devin Bots (Cognition)
- **Quoi** : agents « manager » persistants (mémoire, déclencheurs planifiés, VM isolée) qui découpent un projet et pilotent plusieurs instances Devin.
- **Date** : 2026-11-17
- **Lien** : https://fortune.com/2026/11/17/exclusive-cognition-bets-on-devin-bots-coding-agents-in-challenge-to-anthropics-duet-and-openais-dots/
- **Pourquoi c'est important** : riposte aux agents persistants OpenAI « Dots » et Anthropic « Duet » ; la course passe des agents à tâche aux agents à objectif. Chiffres (×30 PR hebdo, ×10 d'usage en 2 semaines) venant de Cognition uniquement. Prix non publié.
- **Testable** : Oui — accès via Devin (payant).

## 🆕 Nouveaux Outils & Produits

### MAI Code 2 et Code 2 Flash (Microsoft AI)
- **Quoi** : deux modèles de code pour tâches d'entreprise courantes. Code 2 = 98 % de GPT 6.1 Sol à 40 % du coût ; Flash = niveau Haiku 5.5 / GPT-6 Luna à 20 % / 65 % du coût (chiffres Microsoft, prix promo −50 %).
- **Date** : 2026-11-17 (Ignite)
- **Lien** : https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/
- **Pourquoi c'est important** : Microsoft réduit sa dépendance aux modèles tiers dans Copilot. Non conçus pour la recherche ni les très longs agents. Un article (PromptZone) évoque un modèle open-weights MIT de 1,5B : contredit les autres sources, ignoré.
- **Testable** : Oui — GitHub Copilot ; Flash en préview limitée sur Foundry. Payant.

### Pinecall (Product Hunt)
- **Quoi** : plateforme open source pour agents vocaux.
- **Date** : 2026-11-17
- **Lien** : https://www.producthunt.com/products/pinecall
- **Pourquoi c'est important** : 91 votes, seul lancement voice open source du jour ; non vérifié par une 2e source.
- **Testable** : Oui (open source).

### Blue TTS v3 (r/LocalLLaMA)
- **Quoi** : TTS open source, ~50x temps réel sur CPU.
- **Date** : ~2026-11-17
- **Lien** : https://www.reddit.com/r/LocalLLaMA/comments/1xytrz9/
- **Pourquoi c'est important** : 188 pts ; post Reddit seul → non confirmé.
- **Testable** : Oui (CPU).

### Repos GitHub Trending (open source)
- **Quoi** : thème dominant = skills/harnais pour agents de code : obra/superpowers (+1 917 ⭐/jour), univer (+1 774), ag-ui (+1 445), paper-orchestra (Google Research, +1 072), Claude-BugHunter (+1 005), open-code-review (Go, +763), LoopForge (+591), plannotator (+691).
- **Date** : 2026-11-18
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : l'écosystème se structure autour des skills et de l'orchestration de Claude Code / Codex / Cursor.
- **Testable** : Oui — tous open source.

### Render Sandboxes, Framer pour agents, Loom + IA (Product Hunt)
- **Quoi** : sandboxes pour agents (271 votes), construction de sites Framer depuis Claude/Codex/Cursor (966), Loom « talk it through, ship with AI » (743).
- **Date** : 2026-11-17
- **Lien** : https://www.producthunt.com/products/render
- **Pourquoi c'est important** : infrastructure et intégration agents ; peu de détails vérifiés.
- **Testable** : Oui.

## 🧠 Mises à jour de Modèles

### Tencent Hy4 flash
- **Quoi** : 224B paramètres (12B actifs), multimodal, 1M contexte, >150 tok/s ; ~Claude Haiku 5.5 sur tâches bureautiques à ~18x moins cher (éval interne, 85 utilisateurs).
- **Date** : 2026-11-16
- **Lien** : https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows/
- **Pourquoi c'est important** : confirmé par plusieurs sources ; poids annoncés mais pas encore publiés, OpenRouter « bientôt ».
- **Testable** : Oui — Tencent Cloud TokenHub (−50 % jusqu'au 30/11), gratuit sur WorkBuddy jusqu'au 30/11.

## 🔬 Research

### Perplexity Frontier Research
- **Quoi** : programme visant un « scientifique automatisé » (>10 000 GPU), dirigé par Andrew Gordon Wilson ; publications, modèles et données promis en ouvert.
- **Date** : 2026-11-16
- **Lien** : https://www.perplexity.ai/hub/blog/introducing-perplexity-frontier-research
- **Pourquoi c'est important** : aucun résultat ni date de checkpoint ; annonce d'intention.
- **Testable** : Non.

### Vérification pour agents de code (Anthropic / Addy Osmani)
- **Quoi** : article sur les tests E2E, property et différentiels pour valider le travail des agents ; ~90 % du code de l'équipe Claude Code écrit/relu par Claude.
- **Date** : 2026-11-16
- **Lien** : https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
- **Pourquoi c'est important** : méthode directement applicable ; 275 pts sur HN. Complémentaire : étude Harvard « le goulot passe à la revue de code ».
- **Testable** : Oui (pratiques applicables).

## 📝 À surveiller
- **Cloudflare Kitesurf open source** (Apache 2.0, moteur de navigateur Rust/Wasm pour agents, CDP) : annoncé le 13/11 (>72 h), nécessite Workers Paid. https://blog.cloudflare.com/kitesurf-open-source
- **Anthropic** : Fable 5.2 / Mythos 5.2 (9/11), Claude Meetings, roadshow IPO (Nasdaq : ANT, 70–78 $) ; Managed Agents auto-hébergés (12/11). Rien de daté du 17/11.
- **Procès** : le procureur général de Californie poursuit OpenAI sur des incidents d'agents « rogue » (source agrégateur, non vérifiée).
- **Contrôles US** sur l'accès distant au calcul IA avancé (agrégateurs seulement).
- **Google** : conservation des chats Gemini portée à 2 mois (TechCrunch, 17/11) ; Gemini 4 Hydrogen par défaut dans AI Mode depuis le 12/11.
- **Financements** : Genesis AI 500 M$ à 3,5 Md$ ; Model ML 250 M$ à 1,5 Md$ ; AMD aurait finalisé l'acquisition de World Labs (non confirmé).
- **FBI / « Artex »** : outil open source de piratage par IA, source unique.
- **Mistral** : poids de Large 4 amélioré, rumeur d'IPO européenne.
- **Nvidia / Jensen Huang** : 1 685 pts sur r/LocalLLaMA, contenu non vérifié.
- **HN** : ONNX Runtime disparu de GitHub (178 pts) ; Twilio Conversation Relay / Agent Connect (voice, infra).
- Rien de nouveau trouvé sur Meta AI, image/vidéo (GPT Image 2.6 le 4/11, Kling 4.0 en octobre : hors fenêtre).

## 📊 Résumé
- **Top 3 du jour** : 1) GPT-6.2 Astra/Sol ; 2) Devin Bots ; 3) MAI Code 2 / Flash (avec Tencent Hy4 flash : course aux modèles bon marché).
- **À tester en priorité** : GPT-6.2 Sol dans Codex ; MAI Code 2 dans GitHub Copilot ; Hy4 flash (gratuit sur WorkBuddy jusqu'au 30/11) ; obra/superpowers et open-code-review (open source).
