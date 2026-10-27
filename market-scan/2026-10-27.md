# 🔥 Market Scan — 2026-10-27

## 📊 Résumé Exécutif
- Apps analysées en profondeur : 0 (aucune ne passe le filtre : 3+ critères de buzz, <6 mois, hors big-tech)
- Top potentiel : aucun BUILD NOW cette semaine
- Opportunités immédiates (BUILD NOW) : 0
- Limites de la collecte : Product Hunt et Hacker News inaccessibles depuis l'environnement (DNS bloqué). Reddit/X non couverts par la recherche. Données GitHub Trending récupérées, le reste vient de recherches web partielles. Aucun chiffre n'est inventé.

## ❌ Candidats écartés (honnêteté > remplissage)

| Candidat | Signal | Raison d'exclusion | Source |
|---|---|---|---|
| Meta Muse (agent grand public) | #1 App Store US, ~730K-900K DL en 5-6 jours (sept. 2026) | Big-tech, non réplicable, lancé il y a ~7 semaines mais sans angle indie | [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-21/meta-s-new-muse-ai-app-tops-charts-draws-strong-early-reviews), [Fox Business](https://www.foxbusiness.com/technology/metas-muse-becomes-app-stores-hottest-download) |
| Orca (stablyai) | Workspace open-source multi-agents de code, ~9K stars/semaine, ~10-12K stars total, GitHub Trending | Open-source daté du 17 mars 2026 (>6 mois), outil dev, vendu via YC W22 | [Dealroom](https://app.dealroom.co/companies/stably_ai_orca), [AItoolly](https://aitoolly.com/ai-news/article/2026-10-19-orca-emerges-as-a-collaborative-multi-agent-workspace-for-running-coding-agents-across-desktop-mobil) |
| Graphify (Graphify-Labs, YC S26) | Graphe de connaissance de code pour agents, ~97K stars fin juillet, 7K stars/semaine | Lancé le 5 avril 2026 (>6 mois) | [YC](https://www.ycombinator.com/companies/graphify-labs), [Augment](https://www.augmentcode.com/learn/graphify-v0928-strict-mode-apache-relicense) |
| Fish Audio (voix IA) | Seed 50 M$, 21 M$ ARR, 8M+ users | Lancé en 2025, date de levée non confirmée | [NewsBytes](https://www.newsbytesapp.com/news/business/palo-altos-fish-audio-raises-50-million-seed-reports-21-million-arr/tldr) |

## 📈 Tendances Émergentes (signaux faibles)
1. **Skills / plugins pour agents de code** : GitHub Trending hebdo dominé par des repos "skill" (cloudflare/security-audit-skill ~16,6K stars/semaine, anthropics/knowledge-work-plugins, android/skills, un CLAUDE.md "Karpathy"). Le format skill devient un canal de distribution en soi. Source : [GitHub Trending](https://github.com/trending?since=weekly).
2. **Orchestration de flottes d'agents** (Orca, ruflo, opencode) et **mémoire longue pour agents** (ai-memory, Graphify) : la couche "outils autour des agents" explose, mais elle est open-source et saturée.
3. **Voix IA = capital massif** : Gradium (France, seed >100 M$ après extension Nvidia de 30 M$, juil. 2026), Fish Audio (50 M$ seed). Peu de place pour un acteur infra, plus pour des verticaux applicatifs. Sources : [Dealroom](https://dealroom.co/news/137701-gradium-adds-30m-from-nvidia-pushing-seed-round-past-100m/).
4. **Benchmark indie** : passer 10K MRR place dans le top ~15% des indie hackers (stat secondaire, [mean.ceo](https://blog.mean.ceo/?p=11175)).
5. Méfiance : les stars GitHub peuvent refléter des campagnes token (cas CloddsBot), [Towards AI](https://pub.towardsai.net/i-scanned-283-github-repos-the-1-repo-was-a-trap-5445feaa9c3c).

## 💡 Insights Actionnables
- **Pour Kyle (voix AI + SaaS)** : ne pas concurrencer Gradium/Fish Audio sur l'infra. Viser des agents vocaux verticaux (prise de RDV, relance, support FR/EU) en s'appuyant sur ces APIs.
- **Distribution** : publier un "skill" ou plugin open-source (ex. skill voix/telephonie pour agents de code) est un canal d'acquisition gratuit et prouvé par le Trending du moment, à tester en weekend.
- **Prochain scan** : corriger l'accès à Product Hunt/HN (proxy) ou ajouter une source alternative (API Algolia HN, flux RSS PH) pour une vraie détection.
