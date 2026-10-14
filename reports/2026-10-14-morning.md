# AI Watch — 2026-10-14 Matin

> Note : la recherche web n'a remonté aucune annonce datée avec certitude des 12 dernières heures (sources majoritairement agrégateurs/blogs). Les items ci-dessous sont les plus récents trouvés (sept.–début oct. 2026), à vérifier sur les sources officielles.

## 🔥 Breaking

### Claude Opus 5.5 (Anthropic) — 22 sept.
- **Quoi** : Premier modèle de la famille 5.5 ; 1M tokens de contexte, 128k en sortie, $4/$20 par M tokens (vs $5/$25), +30% de vitesse, effort « medium » par défaut. Sonnet 5.5 et Haiku 5.5 annoncés « dans les prochaines semaines ».
- **Lien** : https://computingforgeeks.com/claude-opus-5-5-released-features-benchmarks/
- **Pourquoi c'est important** : 66,4% sur Terminal-Bench 4.0 (chiffres Anthropic) ; annoncé en tête de l'Artificial Analysis Intelligence Index (source secondaire). Moins cher que Opus 5.
- **Testable** : Oui — API / Claude Code (payant).

### GPT-6 Sol & Luna (OpenAI) — 22 sept.
- **Quoi** : Sol à $2/$10 et Luna à $0,10/$0,50 par M tokens (moitié du prix de la série 5.6) ; OpenAI annonce 2x moins d'erreurs factuelles pour Sol (éval interne).
- **Lien** : https://datanorth.ai/news/openai-launches-gpt-6-sol-and-luna
- **Pourquoi c'est important** : Guerre des prix ; sortis ~90 min après Opus 5.5. Benchmarks indépendants mitigés.
- **Testable** : Oui — API, Codex, ChatGPT Work (payant ; Luna partiellement gratuit selon une source).

### Gemini 4 Argon (Google) — 30 sept.
- **Quoi** : Modèle phare orienté code, travail de connaissance et cyberdéfense ; 1M tokens in/out ; accès limité à des partenaires cybersécurité, pas de date GA officielle.
- **Lien** : https://letsdatascience.com/news/google-introduces-gemini-4-argon-with-limited-cyber-defense-d3adff18
- **Pourquoi c'est important** : Concurrent direct d'Opus 5.5 / GPT-6 Astra ; classements variables selon la source.
- **Testable** : Non (accès restreint).

## 🆕 Nouveaux Outils & Produits

### Personal Agent Protocol (Meta + Sierra) — 6 oct.
- **Quoi** : Standard ouvert (basé OAuth) pour que des agents personnels s'authentifient auprès d'entreprises ; partenaires : Shopify, Stripe, Walmart, Genesys… Spec v0.1 prévue fin octobre.
- **Lien** : https://www.channelinsider.com/ai/news-meta-walmart-shopify-stripe-ai-agent-standard/
- **Pourquoi c'est important** : Standardisation du commerce agentique ; OpenAI et Anthropic non cités.
- **Testable** : Non (spec pas encore publiée).

### Meta Muse Code (août) / Z.ai ZCode
- **Quoi** : Muse Code (Meta, basé Muse Spark 1.2) ; ZCode, environnement de dev agentique gratuit de Z.ai pour GLM-5.2, BYOK, macOS/Windows/Linux.
- **Lien** : https://oodaloop.com/briefs/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding/
- **Pourquoi c'est important** : Pression sur Cursor / Claude Code / Copilot.
- **Testable** : Oui pour ZCode (gratuit).

### Voice AI : Mistral Voxtral TTS, Cartesia Sonic-3.6
- **Quoi** : Voxtral TTS (open source, 9 langues dont FR, tourne en local) ; Sonic-3.6 (44 langues, bêta). Dates non confirmées.
- **Lien** : https://oodaloop.com/briefs/technology/mistral-releases-a-new-open-source-model-for-speech-generation
- **Pourquoi c'est important** : TTS open source embarquable.
- **Testable** : Oui.

## 🧠 Mises à jour de Modèles
- Voir Breaking (Opus 5.5, GPT-6 Sol/Luna, Gemini 4 Argon).
- Google : accès aux modèles Gemini restreint par abonnement (effectif le 9 oct. pour les non-abonnés) — https://letsdatascience.com/news/google-limits-gemini-model-access-by-subscription-24b0d7ca
- Image : ChatGPT Images 2.5 (8 sept., source secondaire). Rien de nouveau en octobre trouvé.

## 🔬 Research
- Anthropic affirme que Claude mène ~26% de son travail de R&D IA (17 sept.) : https://technews.tw/2026/09/18/anthropic-says-claude-leads-26-percent-of-its-ai-rd-work/
- Sinon RAS.

## 📝 À surveiller
- Sonnet 5.5 / Haiku 5.5 (Anthropic) « dans les semaines à venir ».
- Spec v0.1 du Personal Agent Protocol (fin oct.).
- GA de Gemini 4 Argon (estimation tierce : nov.–déc.).
- Rumeurs non confirmées : Anthropic en discussions pour racheter Decart AI (~6 Md$) ; Mistral « Le Chonk 1T » avec poids ouverts.
- Spec MCP stateless (2026-07-28) désormais adoptée par plusieurs serveurs (GitHub MCP, JupiterOne).
- Financement : Instinct ($1Md) et FieldAI ($700M), Inworld rachète Ultravox (voice).

## 📊 Résumé
- **Top 3 du jour** : 1) Claude Opus 5.5 ; 2) GPT-6 Sol/Luna (baisse des prix) ; 3) Gemini 4 Argon (accès limité) — aucun n'est nouveau dans les 12 dernières heures.
- **À tester en priorité** : Opus 5.5 via API, GPT-6 Luna (bas coût), ZCode (gratuit), Voxtral TTS (open source).
