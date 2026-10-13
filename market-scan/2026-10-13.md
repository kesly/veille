# 🔥 Market Scan — 2026-10-13

> ⚠️ Limites de la collecte : Product Hunt et Hacker News inaccessibles depuis l'environnement (DNS bloqué). Seul GitHub Trending (hebdo) a été exploitable ; les recherches web n'ont rien remonté de daté octobre 2026. Les chiffres de stars divergent entre pages (voir notes). Scores = estimations honnêtes, non vérifiées par des revenus publics.

## 📊 Résumé Exécutif
- Apps analysées : 3 (sources : GitHub Trending hebdo + pages repos)
- Top potentiel : tester-army/e2e (TesterArmy) — SaaS B2B dev-tool adjacent
- Opportunités immédiates (BUILD NOW) : 0 (1-2 en BUILD ADJACENT)

## 🏆 TOP APP #1 : tester-army/e2e (TesterArmy)
**1. Identification**
- Repo : [tester-army/e2e](https://github.com/tester-army/e2e) — open-source (Apache-2.0), plateforme hébergée TesterArmy (e2e.tester.army)
- Launch : date non affichée ; 751 commits, « en route vers 1.0 » (probablement <6 mois, non confirmé)
- Fondateurs : non identifiés
- Catégorie : testing E2E piloté par agents IA (web + mobile)
- Buzz : +5 582 stars sur la semaine (GitHub Trending), ~9,7k stars, 462 forks, 68 PR ouvertes → 2 critères (viralité GitHub, communauté active) ; pas de traction revenus publique

**2. Proposition de valeur**
- Problème : les tests E2E sont fragiles et coûteux à maintenir
- Solution : étapes en langage naturel (`agent.act`, `agent.assert`) enregistrées puis rejouées sans appel modèle tant que l'app ne change pas
- USP : coût LLM ≈ 0 en régime stable, BYO clé/abonnement/modèle local, web + iOS/Android
- Target : équipes produit/dev, startups avec CI GitHub
- Pricing : framework gratuit ; plateforme TesterArmy (prix non listé)

**3. Stack** : TypeScript, monorepo pnpm, Playwright, agent-device (simulateurs), intégrations Kernel / smol / Limrun / EAS ; reporter GitHub PR ; télémétrie anonyme.

**4. Psychologie** : trigger = douleur récurrente (tests flaky) ; autorité via Playwright ; aha moment = `npx e2e init` puis un test en une phrase ; JTBD = « arrêter de maintenir des sélecteurs ».

**5. Go-to-market** : open-source bottom-up → upsell plateforme hébergée ; commentaires de résultats directement dans les PR (boucle virale interne à l'équipe) ; docs + exemples par framework.

**6. Réplication** : complexité 6/10 ; verticaux : QA voix (tester des agents vocaux par appels simulés), QA d'agents conversationnels ; angle Kyle : « E2E pour voice agents » ; temps de dev MVP : 6-8 semaines.

## 🏆 TOP APP #2 : HyperFrames (HeyGen)
**1. Identification**
- Repo : [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — open-source (Apache-2.0), par HeyGen (société établie)
- Launch : date non affichée ; ~62k stars, 5,6k forks, +4 482 stars sur la semaine
- Catégorie : génération vidéo programmatique « pour agents »
- Buzz : viralité GitHub, communauté (Discord), usage en production chez HeyGen → 3 critères ; biais : marque HeyGen préexistante

**2. Proposition de valeur**
- Problème : produire de la vidéo de façon déterministe et pilotable par des agents IA
- Solution : écrire du HTML/CSS/GSAP, rendu image par image dans Chrome headless + FFmpeg → MP4 identique à chaque run
- USP : HTML simple vs React (Remotion), 21 skills d'agents, rendu AWS Lambda optionnel
- Target : devs, créateurs de contenu automatisé, outils hébergés
- Pricing : gratuit (OSS) ; monétisation indirecte via HeyGen

**3. Stack** : TypeScript, Bun/Node 22+, Puppeteer, FFmpeg, adaptateurs GSAP / Lottie / Three.js / Anime.js / WAAPI, Studio navigateur.

**4. Psychologie** : autorité (marque HeyGen), comparaison explicite à Remotion, aha moment = un agent produit une vidéo depuis un prompt ; JTBD = « automatiser la vidéo sans éditeur ».

**5. Go-to-market** : OSS adossé à une marque + skills pour agents (distribution via Claude Code / Cursor) ; catalogue de blocs réutilisables.

**6. Réplication** : complexité 7/10 ; verticaux : vidéos voix + sous-titres générées automatiquement, rapports vidéo d'appels ; angle Kyle : couche voix (TTS/sync labiale) au-dessus du moteur ; dev 2-3 mois. Concurrence forte (HeyGen, Remotion).

## 🏆 TOP APP #3 : openGym
**1. Identification**
- Repo : [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) — AGPL-3.0, gratuit, auto-hébergé
- Launch : date non affichée ; 1 804 commits, releases toutes les ~2 semaines ; ~10,7k stars, +6 621 sur la semaine
- Fondateur : développeur indépendant (développé avec Claude Code)
- Catégorie : fitness / suivi d'entraînement, self-hosted
- Buzz : viralité GitHub, forte communauté, import Strong/Hevy/FitNotes → 2-3 critères

**2. Proposition de valeur**
- Problème : apps de fitness avec abonnement, pubs, données captives
- Solution : tracker que l'on possède (`docker compose up`), 5 600+ exercices, passkeys, sync, MCP lecture seule, coach IA optionnel (BYOK)
- USP : zéro compte, zéro abonnement, zéro télémétrie, 19 langues
- Target : lifters tech-savvy, communauté self-hosting
- Pricing : gratuit (attention : médias d'exercices sous licence restreinte)

**3. Stack** : React 19 + Vite + Zustand, API Node `node:http`, stockage JSON, nginx, Docker Compose, Capacitor (APK), PWA iOS.

**4. Psychologie** : trigger = rejet de l'abonnement/de la surveillance ; propriété des données ; aha moment = import de l'historique Strong/Hevy en un clic.

**5. Go-to-market** : communauté self-hosted (Reddit, HN), migration facilitée depuis les concurrents, cadence de releases visible.

**6. Réplication** : complexité 3/10 (clone) ; mais pas de modèle économique évident. Angle Kyle : version « hébergée managée » payante (5-8 €/mois) pour ceux qui ne veulent pas self-hoster, ou carnet d'entraînement vocal (logger ses séries à la voix). Dev : 3-4 semaines.

## 💰 Unit Economics Deep Dive — tester-army/e2e (TesterArmy)
⚠️ Aucune donnée financière publique trouvée (Crunchbase/Tracxn/SimilarWeb non consultés). Tout ce qui suit est une **estimation de modélisation**, pas un fait.

| Métrique | Estimation |
|---|---|
| ARR | < 0,5 M€ (probablement pré-revenu / early) |
| ARPU | ~40-100 €/équipe/mois (hypothèse) |
| Users | ~10k stars → quelques centaines d'équipes actives |
| CAC | ~0-50 € (acquisition organique OSS) |
| LTV | ~1 000-2 000 € (churn 3 %/mois, hypothèse) |
| LTV/CAC | > 20 (biaisé par l'organique) |
| Payback | < 1 mois |
| Burn / Runway | inconnu |
| Rev/Employee | inconnu |
| Rule of 40 | non calculable |

**Verdict : 🟡** — traction d'adoption excellente, monétisation non démontrée. Risque : le coût d'inférence est évité par le replay, mais le framework gratuit peut suffire à la plupart des équipes.

## 🎯 Opportunity Scorecard — Top 3
| App | Market (20%) | Complexité inv. (15%) | TTM (15%) | Concurrence inv. (15%) | Revenue (20%) | Fit Kyle (15%) | **Score** | Verdict |
|---|---|---|---|---|---|---|---|---|
| tester-army/e2e | 7 | 4 | 5 | 4 | 6 | 6 | **5.5** | 🟠 WATCH |
| HyperFrames | 7 | 3 | 4 | 3 | 5 | 4 | **4.5** | 🟠 WATCH |
| openGym | 5 | 8 | 8 | 3 | 4 | 3 | **5.1** | 🟠 WATCH |

Variante pour Kyle (non scorée sur les repos eux-mêmes) : « QA/monitoring d'agents vocaux » inspirée d'e2e ≈ 6.8 → 🟡 BUILD ADJACENT (marché en croissance, fit fort, concurrence encore moyenne).

## 📈 Tendances Émergentes
- **Outils « pour agents »** dominent GitHub Trending : [claude-mem](https://github.com/thedotmack/claude-mem) (+3 762), [mattpocock/skills](https://github.com/mattpocock/skills) (+11 139), [openrig](https://github.com/mvschwarz/openrig), [text-to-cad](https://github.com/earthtojake/text-to-cad), [cursor/plugins](https://github.com/cursor/plugins).
- **Skills / MCP comme canal de distribution** : le repo livre des skills pour Claude Code/Cursor (hyperframes, openGym MCP, REA).
- **Self-hosted anti-abonnement** (openGym) soutenu par le coding assisté par IA.
- **Signal faible** : [morluto/rea](https://github.com/morluto/rea) (reverse engineering par agents, MIT, ~169k stars, chiffres incohérents — à traiter avec prudence, risque de manipulation de stars) et AnyPS5 (jeu/hardware, exclu).
- Voix : [BoldVoice](https://yespress.io/boldvoice.md) (5M+ downloads, Série A 21 M$), Sesame (app iOS), ElevenLabs vers l'éducation.

## 💡 Insights Actionnables
1. **Replay sans LLM** (tester-army) : enregistrer les décisions de l'agent et rejouer sans inférence est un pattern à copier pour les agents vocaux (réduire coût/latence).
2. **Idée à valider** : QA automatisée pour voice agents (appels simulés, assertions sur transcript/latence) — fit direct avec l'expertise de Kyle. Valider avec 5 entretiens avant de coder.
3. **Distribuer via skills/MCP** : publier un skill Claude Code + serveur MCP pour tout futur produit.
4. **Migration en un clic** (imports Strong/Hevy) = levier d'acquisition simple.
5. **Hygiène de collecte** : réparer l'accès PH/HN (DNS bloqué) sinon ce scan reste biaisé GitHub ; revérifier les stars (incohérences).
