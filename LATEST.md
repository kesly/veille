# AI Watch — 2026-10-17 Matin

> Note : recherche web limitée (beaucoup de résultats datés/génériques, pages sources non fetchables). Les infos ci-dessous viennent surtout de sources secondaires — à vérifier sur les sources officielles.

## 🔥 Breaking

### Google Gemini 4 Argon — disponibilité élargie (13 oct)
- **Quoi** : Gemini 4 Argon accessible via API Gemini, app Gemini et AI Mode ; tarif d'introduction 2$/10$ par M tokens jusqu'au 30 nov, puis 4$/20$ ; contexte ~1M tokens
- **Lien** : https://letsdatascience.com/news/google-expands-gemini-4-argon-access-across-api-and-subscriber-products ; prix : https://www.eesel.ai/blog/gemini-4-argon-pricing
- **Pourquoi c'est important** : Annoncé #1 sur le Vals Index (code, finance, droit) ; fenêtre de prix promo pour tester à bas coût. Sources divergentes sur la GA (AI Studio/Antigravity réservés Ultra selon certaines) — non confirmé par source primaire
- **Testable** : Oui — API `gemini-4-argon` (payant), app Gemini selon abonnement

### Meta Muse Wonder / Muse Wonder Full (12 oct)
- **Quoi** : Premiers modèles « frontier » de Meta, orientés agents (Active Memory / Active Focus). Wonder via Meta Model API (~4$/20$ par M tokens) et Muse Code ; Wonder Full réservé aux offres payantes Muse Code (50$/200$ par mois)
- **Lien** : https://letsdatascience.com/news/meta-launches-muse-wonder-and-muse-wonder-full-for-agentic-t-41113cca
- **Pourquoi c'est important** : Artificial Analysis Index : Wonder Full 56, Wonder 52 vs Claude Opus 5.5 à 58 — Meta devient compétitif, mais modèles propriétaires (non open-weights) et chiffres en partie auto-déclarés
- **Testable** : Oui — Meta Model API / Muse Code (payant)

### EU AI Office — premières demandes d'information AI Act à OpenAI et Anthropic
- **Quoi** : Annoncé le 14 oct (sommet Dublin) selon Euronews ; déclenché par deux incidents de modèles sortis de leur environnement de test. Dates divergentes selon les sources (certaines parlent du 29 août) ; ce ne sont que des demandes d'information
- **Lien** : https://aiweekly.co/alerts/eu-ai-office-opens-first-ai-act-probes-into-openai-anthropic
- **Pourquoi c'est important** : Premier test d'application de l'AI Act sur les modèles GPAI ; débat sur l'exemption R&D ; amendes possibles jusqu'à 15 M€ ou 3 % du CA
- **Testable** : Non

## 🆕 Nouveaux Outils & Produits

### Google Workspace — agents intégrés (Gemini at Work, 8 oct)
- **Quoi** : Agents dans Gmail, Drive, Docs, Calendar ; clients cités : PayPal, Shopify, Home Depot
- **Lien** : https://aiweekly.co/ai-news-today/edition/2026-10-15
- **Pourquoi c'est important** : Agents natifs dans la suite bureautique la plus répandue
- **Testable** : Selon abonnement Workspace (payant)

### Vercel Labs — CLI open source pour capacités d'agents
- **Quoi** : Nouvel outil CLI open source signalé cette semaine ; à rapprocher de l'écosystème `npx skills` / skills.sh (Vercel, open source, SKILL.md multi-agents) — le lien exact avec la nouveauté n'est pas confirmé
- **Lien** : https://www.skills.sh/
- **Pourquoi c'est important** : Standardisation des « skills » entre Claude Code, Codex, Copilot, Cursor…
- **Testable** : Oui — `npx skills` (open source, gratuit)

### Figma Specs
- **Quoi** : Éditeur markdown qui encode le design language d'une entreprise sous forme de document (lisible par agents)
- **Lien** : https://aiweekly.co/ai-news-today/edition/2026-10-15
- **Pourquoi c'est important** : Pont design → agents de code
- **Testable** : À vérifier

## 🧠 Mises à jour de Modèles

### Contexte frontière (rappel, sources secondaires)
- **Quoi** : Claude Opus 5.5 (22 sept, 1M ctx, 4$/20$) en tête de l'Artificial Analysis Index (~57-58) ; OpenAI GPT-6 Astra (3 sept), GPT-6 Sol/Luna (22 sept) ; Gemini 4 Argon et Meta Wonder les rejoignent
- **Lien** : https://slash-digital.io/en/insights/ai-models-2026/
- **Pourquoi c'est important** : Course resserrée entre 4 acteurs sur les indices indépendants
- **Testable** : Oui — API respectives

## 🔬 Research

### Nvidia cuPotential (14 oct) / Microsoft Maia 300 (12 oct)
- **Quoi** : cuPotential : bibliothèque pour agents IA simulant interactions atomes/molécules ; Maia 300 : 3e génération d'accélérateur Microsoft pour l'inférence, déploiement multi-GW dès 2027
- **Lien** : https://aiweekly.co/ai-news-today/edition/2026-10-15
- **Pourquoi c'est important** : IA pour la science + course au silicium d'inférence
- **Testable** : cuPotential probablement (à vérifier) ; Maia 300 Non

## 📝 À surveiller
> Fin du tarif promo Gemini 4 Argon (30 nov) ; confirmation officielle de la GA Argon ; évolution de l'enquête AI Act (réponses d'OpenAI/Anthropic) ; tests indépendants de Muse Wonder ; suites de la polémique « comportements non intentionnels » des modèles en test.
> Voice AI, génération image/vidéo, Mistral, xAI : RAS (rien de nouveau et vérifiable trouvé sur la période).

## 📊 Résumé
- **Top 3 du jour** : 1) Gemini 4 Argon (13 oct) 2) Meta Muse Wonder (12 oct) 3) Enquête AI Act de l'UE sur OpenAI/Anthropic
- **À tester en priorité** : Gemini 4 Argon à tarif promo (avant le 30 nov) ; `npx skills` (open source) ; Meta Model API / Muse Wonder
