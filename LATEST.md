# AI Watch — 2026-10-16 Matin

> ⚠️ Note de couverture : la recherche web n'a remonté aucun élément daté des 12 dernières heures. Les items ci-dessous datent de la dernière semaine à dix jours (6–7 octobre surtout) et sont les plus récents vérifiables. Beaucoup de sources sont secondaires (agrégateurs, blogs) : à recouper avec les sources primaires.

## 🔥 Breaking

### Claude Haiku 5.5 (Anthropic)
- **Quoi** : Petit modèle d'Anthropic sorti le 7 oct 2026 : 1M tokens de contexte, 128K de sortie, niveaux d'effort configurables (low → max).
- **Lien** : https://letsdatascience.com/news/anthropic-releases-claude-haiku-55-with-lower-prices-and-eff-f698c663
- **Pourquoi c'est important** : ~0,10 $/M tokens en entrée et 0,50 $/M en sortie (≤100K tokens) contre 1 $/5 $ pour Haiku 4.5. Anthropic annonce 72,4 % sur le sous-ensemble offline d'OSWorld 2.1 (vs 15,7 %) — chiffres éditeur. Cible : sous-agents, résumés, usage navigateur à gros volume.
- **Testable** : Oui — API Anthropic et AWS Bedrock (payant).

### OpenAI : 722 manuscrits de maths générés par un modèle non publié
- **Quoi** : Le 6 oct, OpenAI a publié 722 manuscrits (372 familles de résultats) sur GitHub (openai/math), produits par un modèle interne non sorti. 3 retirés et 14 révisés en moins de 24 h (erreur de signe) ; catalogue à 719.
- **Lien** : https://letsdatascience.com/blog/openai-posted-722-ai-written-math-papers-kept-the-prompts
- **Pourquoi c'est important** : Seuls 162 manuscrits ont un résultat principal formalisé en Lean. Parmi les affirmations : une preuve de la Unique Games Conjecture. Ni prompts, ni nom du modèle, ni compute publiés. Aucune relecture par les pairs ; des mathématiciens (Sutherland, Townsend) s'attendent à d'autres erreurs.
- **Testable** : Partiellement — le dépôt GitHub est consultable (gratuit), la vérification reste à faire par des experts.

### Mistral Large 4 (preview recherche)
- **Quoi** : Modèle de 1T de paramètres (49B actifs), sorti le 6 oct en Research Public Preview. Les poids doivent être publiés fin octobre.
- **Lien** : https://artificialanalysis.ai/articles/mistral-large-4-france-ai
- **Pourquoi c'est important** : Artificial Analysis : 38 à l'Intelligence Index, meilleur modèle hors USA/Chine sur cet indice, au niveau de GPT-6 Luna (max). API à 1,36 $/M entrée et 4,18 $/M sortie, -50 % pendant 2 semaines de lancement. Plus cher par tâche que des modèles open-weights comparables.
- **Testable** : Oui — API Mistral (payant, promo lancement). Poids ouverts attendus fin octobre.

## 🆕 Nouveaux Outils & Produits

### Personal Agent Protocol (Meta + Sierra)
- **Quoi** : Standard ouvert proposé pour que des agents personnels interagissent avec des entreprises (authentification, permissions via OAuth, accès lecture/écriture choisi par le client). Participants cités : Shopify, Stripe, Walmart, Genesys.
- **Lien** : https://letsdatascience.com/news/meta-and-sierra-introduce-personal-agent-protocol-for-busine-13aa4537
- **Pourquoi c'est important** : Concurrent/complément de l'Agentic Commerce Protocol Stripe–OpenAI. Spec v0.1 attendue fin octobre ; paiements et notifications en extensions futures. Adoption non prouvée.
- **Testable** : Non (spec pas encore publiée).

### Qoder 1.0
- **Quoi** : L'IDE IA devient un « Autonomous Development Desktop » (génération, vérification et livraison de code), Windows/macOS/Linux. Annonce de mai 2026, donc plus ancienne.
- **Lien** : https://ai-startups.dealroom.co/news/feed/qoder-1-0-launches-autonomous-development-desktop-with-ai-powered-code-generation-and-verification
- **Pourquoi c'est important** : Un de plus dans la course aux environnements de dev agentiques.
- **Testable** : Oui — téléchargement (tarification non vérifiée).

### mcp-use (Python, open source)
- **Quoi** : Framework open source sur le SDK MCP officiel avec inspector intégré et « Code Mode » (l'agent écrit du code au lieu d'appeler les outils). Revendique -98,7 % de contexte (chiffre éditeur) ; 8 000+ étoiles GitHub. Date de sortie non confirmée.
- **Lien** : https://mcp-use.com/python
- **Pourquoi c'est important** : Le Code Mode réduit la consommation de contexte des serveurs MCP.
- **Testable** : Oui — pip, open source.

## 🧠 Mises à jour de Modèles

- **GPT-6 Sol / Luna (OpenAI)** — sortis le 22 sept ; Sol à 2 $/10 $ par M tokens, Luna à 0,10 $/0,50 $ ; environ -50 % vs GPT-5.6. Un billet secondaire non confirmé mentionne GPT-6.1 Sol (29 sept) et Sol devenu modèle par défaut payant dans ChatGPT (7 oct). https://computingforgeeks.com/gpt-6-sol-luna-released-features-benchmarks/ — Testable : Oui (API `gpt-6-sol`, `gpt-6-luna`, Codex ; payant).
- **Claude Opus 5.5 (Anthropic)** — sorti le 22 sept (mentionné dans les recaps ; non re-vérifié ici). https://lumichats.com/blog/ai-news-recap-september-18-22-2026-three-new-models
- **Gemini 4 (Google)** — en post-training selon un preview, attendu avant fin 2026, pas de date officielle. https://www.thehansindia.com/tech/upcoming-ai-updates-in-october-2026-major-developments-to-watch-1127036
- Voir aussi Haiku 5.5 et Mistral Large 4 en Breaking.

## 🔬 Research

- Voir les manuscrits mathématiques OpenAI (Breaking). Autre : Anthropic indique que Claude mène plus d'un quart de la R&D sur ses futurs modèles, en collaboration humaine dans >90 % des cas (mesures d'août, via AFP) : https://www.techniques-ingenieur.fr/actualite/breves-afp/claude-dirige-plus-dun-quart-des-recherches-sur-les-futurs-modeles-danthropic-dit-la-firme-163844/
- Pas de paper influent supplémentaire vérifié.

## 📝 À surveiller

- Poids ouverts de Mistral Large 4 (fin octobre) et spec v0.1 du Personal Agent Protocol (fin octobre).
- Vérification/erreurs dans les manuscrits OpenAI (Lean, relecture experts) ; publication éventuelle du nom du modèle.
- Gemini 4 avant fin 2026 ; Siri IA multilingue dans iOS 27.2 (en test).
- Rapport TechRadar : Anthropic aurait assoupli sa politique de sécurité (fin du « pas de release tant que non sûr »), non vérifié en source primaire.
- Voix, génération image/vidéo, outils de code, open source/HN : RAS — les recherches n'ont rien remonté de récent et vérifiable.

## 📊 Résumé
- **Top 3 du jour** : 1) Claude Haiku 5.5 (prix ÷10, 1M de contexte) ; 2) 722 manuscrits de maths OpenAI et le débat de vérification ; 3) Mistral Large 4 (poids ouverts attendus fin octobre).
- **À tester en priorité** : Haiku 5.5 comme sous-agent bon marché ; Mistral Large 4 via API pendant la promo -50 % ; mcp-use (open source) pour le Code Mode MCP.
