# AI Watch — 2026-11-06 Matin

> Collecte : treg 0/4 sources (indisponible), 18 recherches extended, GitHub Trending ok, 0 pages lues (treg down), 4 items confirmés par une deuxième source.

## 🔥 Breaking

### OpenAI — ChatGPT Images 2.6 + GPT-Image-2.6 Flare / Sunburst
- **Quoi** : Nouvelle génération d'images ~50 % plus rapide, GIFs animés, images de référence persistantes ; deux modèles API : Flare (vitesse) et Sunburst (qualité, export SVG/markup).
- **Date** : 2026-11-04
- **Lien** : https://community.openai.com/t/images-upgraded-introducing-chatgpt-images-2-6/1412901 — https://x.com/OpenAI/status/2118124966055223755
- **Pourquoi c'est important** : Génération GIF native dans ChatGPT et Codex, API plus rapide à prix annoncé inchangé (sources divergentes sur le prix).
- **Testable** : Oui — ChatGPT/Codex (tous les tiers) ; API payante.

### OpenAI — Pipeline cyber autonome : 948 exploits Linux (modèle cyber non publié)
- **Quoi** : Run unique d'un futur modèle cyber : 1 724 vulnérabilités reproduites, 948 exploits d'escalade de privilèges locale générés/validés avec patches, ~1,2 M$ d'API (~1 279 $/faille).
- **Date** : 2026-11-04/05
- **Lien** : https://openai.com/index/a-thousand-fewer-paths-to-root/ — https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/
- **Pourquoi c'est important** : Démonstration d'échelle sur la découverte/exploitation offensive et le patching automatisés ; ~10 jours après, 61 bugs patchés en amont seulement. Modèle non nommé, pas de date de sortie.
- **Testable** : Non.

### Meta rachète Conductor (orchestration multi-agents de code)
- **Quoi** : Conductor (Claude Code, Codex, Cursor, OpenCode en parallèle) rejoint Meta ; montant non divulgué.
- **Date** : 2026-11-04
- **Lien** : https://www.infoworld.com/article/4245065/meta-acquires-conductor-as-ai-coding-shifts-toward-multi-agent-development.html
- **Pourquoi c'est important** : Consolidation des outils multi-agents de code ; Conductor Cloud read-only le 13/11, arrêt le 20/11 ; version locale maintenue jusqu'à début 2027.
- **Testable** : Oui, jusqu'au 20/11 (Conductor local).

## 🆕 Nouveaux Outils & Produits

### Anthropic FlashProve (open source, Apache 2.0)
- **Quoi** : Prototype de recherche pour prouver cryptographiquement (zkSNARK) quel modèle a produit une réponse, sans révéler les poids.
- **Date** : 2026-11-02/03
- **Lien** : https://thenextweb.com/news/anthropic-flashprove-provable-inference-ai-model-identity
- **Pourquoi c'est important** : Piste d'audit de l'identité des modèles ; limites fortes : preuve 70-95× le coût GPU, contexte 1 024 tokens, MoE uniquement, aucun déploiement prévu.
- **Testable** : Oui (open source, recherche).

### GitHub Trending (agents)
- NVIDIA/auto-ontology (+2 679 ⭐, raisonnement graphe pour agents), vercel-labs/agent-desktop (CLI computer-use, Rust), vercel-labs/agent-browser, max-sixty/worktrunk (worktrees pour agents parallèles), mattpocock/skills, garrytan/gstack, google/skills, microsoft/VibeVoice (voix open source), scenario-labs/skills.
- **Lien** : https://github.com/trending?since=daily
- **Pourquoi c'est important** : Thème dominant : infrastructure d'agents (computer-use, worktrees, skills).
- **Testable** : Oui — tous open source.

### Voice AI
- Convoso Voice AI Agent no-code (GA 2 nov, payant) ; AssemblyAI-TTS-1 (premier TTS d'AssemblyAI, fin oct.) ; Rime Prism et Gradium Phonon (TTS on-device open source), ElevenLabs Eleven Realtime — dates non vérifiées (voir À surveiller).

## 🧠 Mises à jour de Modèles
RAS confirmé sur 72 h hors images OpenAI. Mistral Large 4 (open weights, licence MIT modifiée) publié le 29/10, hors fenêtre. DeepSeek : le « v4-flash-0731 du 5/11 » d'un tracker est une erreur (V4.1 Flash 1017 est le plus récent) — ignoré.

## 🔬 Research
RAS (FlashProve ci-dessus). METR : l'accélération du développement chez Anthropic serait 2× celle de l'an dernier (une seule source, date incertaine).

## 📝 À surveiller
- OpenAI « National Community Compact » (4-5/11) : fin des NDA avec élus locaux, coûts électricité à charge, après des référendums locaux anti-data-centers ; le Nasdaq aurait chuté >5 % (chiffres divergents selon sources).
- Anthropic × AP : premier accord de licence avec un éditeur (Adweek, 4/11) ; partenariat Plaid (accès lecture seule) ; Cat Wu (Claude Code) passe chez OpenAI (Business Insider) ; S-1 IPO mentionné.
- Google : Gemini Omni 1.2 Flash dans Vids (5/11) ; Pro retiré du plan AI Plus le 13/11 ; modèles preview Gemini 3.x arrêtés le 17/11 ; contrôles des comptes élèves critiqués.
- OpenAI « Dots » (agent perso, 27/10) ; rachat Pierre Computer (rumeur) ; Gemini « 3.8 Live » non vérifié.
- Restrictions export : extension des contrôles aux data centers étrangers (non confirmé).
- Financements : Nooks 500 M$ (General Catalyst), Future Secure AI 80 M$, Mistral Série D 3 Md€ (date non précisée).
- MCP : Parallel MCP 2.0, Suno MCP (beta) — sans date vérifiée.

## 📊 Résumé
- **Top 3 du jour** : 1) OpenAI 948 exploits Linux par pipeline autonome ; 2) ChatGPT Images 2.6 / GPT-Image-2.6 ; 3) Meta rachète Conductor.
- **À tester en priorité** : Images 2.6 (ChatGPT/Codex, API), Conductor local avant le 20/11, agent-desktop / worktrunk (open source), FlashProve (recherche).
