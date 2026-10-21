# AI Watch — 2026-10-21 Matin

> ⚠️ Note de fiabilité : le moteur de recherche renvoie peu de contenu daté des 12 dernières heures. Les items ci-dessous sont les plus récents trouvés (dernières ~2 semaines), à recouper avec les sources officielles. Rien de vérifié comme « nouveau cette nuit ».

## 🔥 Breaking
RAS (aucune annonce majeure vérifiée sur les 12 dernières heures).

## 🆕 Nouveaux Outils & Produits

### Grok Voice 3.0 (xAI) — 14 oct.
- **Quoi** : modèle speech-to-speech temps réel pour agents vocaux, remplace Grok Voice 2.0 (alias `grok-voice-latest`).
- **Lien** : https://www.devx.com/artificial-intelligence-ai/what-is-grok-voice-3-0-xai-speech-to-speech-model/
- **Pourquoi c'est important** : 0,08 $/min, latence < 1 s, gestion des interruptions ; cible centres d'appels. Classement #1 Artificial Analysis (86,9) contesté selon les sources (chiffres xAI vs indépendants).
- **Testable** : Oui — Voice Agent API xAI, model ID `grok-voice-3.0` (payant).

### ZCode (Z.ai) — date non confirmée
- **Quoi** : environnement de dev agentique desktop gratuit, bâti autour de GLM-5.2, BYOK pour modèles tiers (macOS/Windows/Linux).
- **Lien** : https://oodaloop.com/briefs/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding/
- **Pourquoi c'est important** : concurrent gratuit de Cursor / Claude Code / Copilot.
- **Testable** : Oui — app gratuite.

## 🧠 Mises à jour de Modèles

### Claude Haiku 5.5 (Anthropic) — 7 oct. (statut à confirmer, un tracker le dit « annoncé » seulement)
- **Quoi** : petit modèle rapide de la famille 5.5, contexte 1M, sortie 128K.
- **Lien** : https://computingforgeeks.com/claude-haiku-5-5-released-features-benchmarks/
- **Pourquoi c'est important** : ~0,10 $/M tokens en entrée, 0,50 $/M en sortie (≈75 % moins cher que Haiku 4.5 selon gori.me) ; 72,4 % OSWorld 2.1 (chiffres Anthropic). Vals AI : #16/45.
- **Testable** : Oui — API Anthropic (payant).

### Autres sorties d'octobre (BenchLM : 20 modèles / 16 fournisseurs)
- NVIDIA Nemotron 3.5 Super VL 120B A12B, Liquid AI LFM2.5-24B-A2B, Jais 3 (IFM, 15 oct.). Détails non vérifiés.
- **Lien** : https://af.net/realtime/confirmed-ai-model-releases-for-october-2026/
- **Testable** : Probablement (open-weights) — à vérifier sur Hugging Face.

### Gemini 4 — rumeur contradictoire
- Un registre liste « Gemini 4 Argon » en octobre ; un autre dit seulement post-training, sortie avant fin 2026. Non confirmé.

## 🔬 Research
RAS (non couvert de façon fiable par la recherche).

## 📝 À surveiller
- **Anthropic** : CA T3 2026 à 16,8 Md$ et rentable (FT/Reuters, 14 oct.) ; IPO évoquée en août (source unique) ; litige juridique avec le Pentagone en cours. https://www.thestar.com.my/tech/tech-news/2026/10/15/anthropic-revenue-jumps-to-168-billion-in-third-quarter-ft-reports
- **OpenAI** : GPT-6 Astra lancé le 3 sept. (rollout progressif, 10 $/50 $ par M tokens). Rumeur d'un « GPT-6.1 Astra » annulé pour raisons de sécurité : non retrouvée dans mes recherches, à traiter comme non confirmée.
- **ByteDance Seedance 2.5** : vidéo 30 s, jusqu'à 4K, API ouverte en juillet (benchmarks indépendants attendus).
- **Meta** : Muse Spark (avril), Muse Code (août) ; la date « 15 oct. » citée par un agrégateur n'a pas été retrouvée.
- **xAI/SpaceX–Cursor** : option d'achat à 60 Md$ (avril).

## 📊 Résumé
- **Top 3 du jour** : 1) Grok Voice 3.0 (voice agents à 0,08 $/min) ; 2) Claude Haiku 5.5 (petit modèle bon marché, contexte 1M) ; 3) Anthropic T3 à 16,8 Md$ et rentable.
- **À tester en priorité** : Grok Voice 3.0 via Voice Agent API ; ZCode (gratuit) ; Haiku 5.5 pour tâches agentiques à bas coût.
