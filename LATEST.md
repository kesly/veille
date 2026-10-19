# AI Watch — 2026-10-19 Matin

> Note : la recherche web n'a remonté presque aucune actualité datée des 12 dernières heures (04h UTC, lundi). Le rapport couvre donc les développements récents (≈ 2 semaines) encore actifs, signalés comme tels. Plusieurs sources sont des agrégateurs : à vérifier sur les sites officiels.

## 🔥 Breaking
RAS sur les dernières 12 h (aucune annonce majeure confirmée).

## 🆕 Nouveaux Outils & Produits

### Personal Agent Protocol (PAP) — Meta × Sierra
- **Quoi** : standard ouvert pour que des agents IA personnels interagissent avec des entreprises (vérification d'identité de l'agent, limites d'actions, sessions OAuth invité/connecté). Partenaires : Walmart, Shopify, Stripe, etc. Annoncé le 6 oct.
- **Lien** : https://www.channelinsider.com/ai/news-meta-walmart-shopify-stripe-ai-agent-standard/
- **Pourquoi c'est important** : s'ajoute aux protocoles concurrents (Universal Commerce Protocol côté Google, Agentic Commerce Protocol Stripe/OpenAI) — la bataille des standards du commerce agentique se précise.
- **Testable** : Non — spec v0.1 annoncée par Sierra « fin octobre » ; paiements encore en roadmap.

### Cartesia Sonic-3.6 (TTS)
- **Quoi** : modèle text-to-speech, 44 langues, en beta ; revendique la 1re place sur les classements Artificial Analysis (dire du vendeur). Payant (API).
- **Lien** : https://menastartupdigest.com/?p=49615
- **Pourquoi c'est important** : cadence rapide (3 mois après Sonic-3.5) sur la voix temps réel multilingue.
- **Testable** : Oui — API Cartesia (beta). Date exacte non confirmée.

### Mistral Voxtral TTS
- **Quoi** : modèle de synthèse vocale open source, 9 langues, assez léger pour l'edge (téléphone, laptop).
- **Lien** : https://oodaloop.com/briefs/technology/mistral-releases-a-new-open-source-model-for-speech-generation
- **Pourquoi c'est important** : alternative locale/open aux TTS propriétaires.
- **Testable** : Oui (open source) — date de sortie non confirmée dans les sources.

## 🧠 Mises à jour de Modèles

### Mistral Large 4 « Le Chonk » (~1T paramètres)
- **Quoi** : modèle multimodal ~1,05T de paramètres en preview publique ; poids ouverts annoncés pour ~27 oct. (licence non confirmée). TechCrunch : pas encore open-weight.
- **Lien** : https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/
- **Pourquoi c'est important** : si les poids sortent, plus gros modèle ouvert européen. Un site (CryptoBriefing) doute de l'existence du modèle — TechCrunch le confirme toutefois.
- **Testable** : Partiellement — endpoint preview ; poids attendus fin octobre.

### Claude Haiku 5.5 (Anthropic) — sorti le 7 oct.
- **Quoi** : petit modèle bas coût, 1M tokens de contexte, 128K en sortie, niveaux d'effort ; 0,10 $/0,50 $ par M tokens (≤100K). OSWorld 2.1 (sous-ensemble offline) 72,4 % vs 15,7 % pour Haiku 4.5 (chiffres Anthropic).
- **Lien** : https://letsdatascience.com/news/anthropic-releases-claude-haiku-55-with-lower-prices-and-eff-f698c663
- **Pourquoi c'est important** : sous-agents et usage navigateur à très bas coût.
- **Testable** : Oui — API Anthropic (payant).

### Claude Opus 5.5 vs GPT-6 Sol / Luna — 22 sept. (rappel)
- **Quoi** : Opus 5.5 (4 $/20 $) et GPT-6 Sol (2 $/10 $) et Luna (0,10 $/0,50 $) sortis à 90 min d'intervalle.
- **Lien** : https://decrypt.co/378986/openai-launches-gpt-6-sol-luna-anthropic-claude-opus-5-5
- **Pourquoi c'est important** : guerre des prix ; les benchmarks fournis par les labs sont à prendre avec prudence.
- **Testable** : Oui (APIs).

### xAI Grok Voice 3.0 (14 oct.), Meta Muse Spark (15 oct.)
- **Quoi** : listés par BenchLM parmi 20 sorties d'octobre ; Muse Spark est un modèle fermé (Meta AI). Aucun détail confirmé retrouvé.
- **Lien** : https://michaelparekh.substack.com/p/ai-metas-closed-muse-spark-enters
- **Pourquoi c'est important** : Meta passe à un modèle fermé pour son produit grand public.
- **Testable** : Non vérifié.

## 🔬 Research
- Anthropic affirme que Claude « mène » ~26 % de son R&D IA et publie une nouvelle mesure de vitesse de progrès (17 sept.) — https://technews.tw/2026/09/18/anthropic-says-claude-leads-26-percent-of-its-ai-rd-work/ (source secondaire, à vérifier).

## 📝 À surveiller
- Poids ouverts de Mistral Large 4 vers le 27 oct. et licence associée.
- Spec v0.1 du Personal Agent Protocol (fin octobre).
- Gemini 4 : rumeur (post-training, avant fin 2026), source unique, non confirmée.
- Siri IA multilingue avec iOS 27.2.

## 📊 Résumé
- **Top 3 du jour** : 1) Mistral Large 4 1T (poids ouverts à venir) ; 2) Personal Agent Protocol Meta/Sierra ; 3) Claude Haiku 5.5 (prix bas + computer use).
- **À tester en priorité** : Claude Haiku 5.5 (API), Cartesia Sonic-3.6 (beta), Mistral Voxtral TTS (open source).
