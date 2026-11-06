# 🔥 Market Scan — 2026-11-06

> Collecte : treg 0/5 sources (proxy 403), 15 recherches extended, GitHub Trending ok, 0 page lue (treg injoignable), 3 candidats creusés. Filtre partiel pour les 3 apps (voir chaque fiche).

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : Beacon (Asymptote Labs), score 5.5/10 (🟠 WATCH), talonné par Guava 5.45
- Opportunités immédiates (BUILD NOW) : 0 — semaine sans candidat ≥ 7.5, scores honnêtes

## 💸 Apps qui font du cash
**Données treg indisponibles (proxy 403) : classement App Store US et posts X/Reddit non collectés, rien d'inventé.**

**Revenus déclarés / estimés**
- **Scroll The Bible** (Gabriel Jacobson, JCBSN LLC) : « $2M MRR » en 10 mois, post X du 2026-10-27, `déclaré, non vérifié` (le fondateur n'a pas confirmé ; estimation tierce ScreensDesign ≈ $1,8M). App iOS lancée le 17/12/2025, feed vertical façon TikTok pour versets, ads Meta/Instagram depuis juillet 2026. Post : https://x.com/jacobrodri_/status/2115060267545731513 — hors Top 3 (>6 mois).
- **Solo AI tool à $69K/mois fin août 2026** : rapport secondaire, produit non identifié, `déclaré, non vérifié`, non retenu.
- **Habit Pixel** (habit tracker) : ≈ $1K MRR en janv. 2026, déclaré par le fondateur, https://www.indiehackers.com/post/from-0-to-1k-mrr-in-8-months-bootstrapping-habit-pixel-as-a-solo-dev-684b6c056d — `déclaré, non vérifié`.
- Benchmark : 28 produits IH vérifiés Stripe, 9 mois en moyenne pour $1K MRR (estimation d'un blog tiers).

**App Store US top grossing** (snapshots tiers, un rang n'est pas un revenu) : ChatGPT #1 (48e jour d'affilée au 1er nov.), Claude #8, Perplexity #72, Suno #99 — grandes marques, hors filtre. Aucune app <100k avis identifiée. Source : https://www.appstro.dev/top-grossing-apps

## 🏆 TOP APP #1 : Beacon (Asymptote Labs)
> Filtre partiel : critères remplis = média/PH (#1 Product of the Day 2 nov., 439 pts), traction (seed $5,5M), communauté (GitHub). Manquent : viralité 10K mentions, preuve de revenus. Âge : Beacon lancé en mai 2026 (~6 mois, limite) ; relancé sur PH le 2 nov.

**1. Identification** — Beacon, https://beacon.sh/ — Asymptote Labs ; CEO Justin D'Souza ; seed $5,5M (Tower Research Ventures, 20 oct.) — dev tools / sécurité agents IA. Repo : github.com/Asymptote-Labs/agent-beacon. Open source MIT. Sources : https://www.producthunt.com/products/asymptotelabs ; https://thenextweb.com/news/asymptote-labs-5-5m-seed-ai-agent-security

**2. Proposition de valeur** — Problème : les agents de code (Claude Code, Cursor, Codex) oublient tout d'une session à l'autre et les équipes sécurité ne voient pas ce qu'ils font. Solution : couche de télémétrie unifiée + mémoire réutilisable (MCP / Agent Skills), stockage local. USP : mémoire qui survit au changement d'outil. Pricing : gratuit en local ; Beacon Cloud / Pro $20/mois (source : agenttested.ai, à vérifier).

**3. Stack** — CLI local, format de trace normalisé, MCP + Agent Skills ; cloud optionnel. Détails internes non confirmés.

**4. Psychologie** — Triggers : peur de perdre le contexte, autorité (open source, seed), preuve sociale (#1 PH, +460 % d'étoiles en sept., déclaré). JTBD : « ne plus réexpliquer mon projet à l'agent ». Aha : l'agent réutilise une leçon validée.

**5. Go-to-market** — Open source bottom-up (GitHub), lancement PH, double positionnement : mémoire pour devs, télémétrie pour entreprises. Boucle virale : partage de skills/mémoire entre équipes.

**6. Réplication** — Complexité 5/10 ; 6–10 semaines pour un MVP. Verticaux : mémoire pour agents vocaux, audit d'appels. Angle Kyle : mémoire/traçabilité pour agents voice AI (transcripts → leçons). Risque : GitHub Trending montre claude-mem (+9 318 étoiles/sem.) déjà dominant sur ce créneau.

## 🏆 TOP APP #2 : Guava
> Filtre partiel : critères = traction (seed $12,5M, >12 clients entreprise), médias (Axios Pro, BusinessWire), communauté (partielle). Manquent : viralité, engagement discussion publique.

**1. Identification** — Guava, https://goguava.ai (domaine à vérifier) — Los Angeles, fondée 2026 par Omri Dahan, Anthony Scodary, Nico Benitez, Mike Piechna ; seed $12,5M annoncé le 3 nov. 2026 (Acrew Capital, Flourish, WillowTree, Clocktower, Commerce Ventures). Source : https://www.axios.com/pro/enterprise-software-deals/2026/11/03/voice-agents-guava-gridspace

**2. Proposition de valeur** — Problème : les voice agents en secteurs régulés (santé, finance, assurance) échouent en production. Solution : plateforme full-stack avec modèles propres (ASR, LLM, TTS), SDK Python/TypeScript/Claude Code, règles métier en code. Modèle Daytona (sept.), top 10 du benchmark Coval en WER (chiffres internes). Pricing : gratuit jusqu'à $499/mois selon Dealroom, non confirmé. Propriétaire, payant. Lien avec Gridspace non confirmé.

**3. Stack** — Modèles speech maison entraînés sur données d'appels régulés (10 Md de minutes revendiquées via Gridspace), SDK dev. Certifs SOC 2 II, HITRUST i1, PCI DSS 1.

**4. Psychologie** — Autorité (conformité), peur du risque réglementaire, social proof (dizaines de milliers d'appels/jour). JTBD : « déployer un agent vocal sans risque de non-conformité ». Aha : agent contrôlé par du code.

**5. Go-to-market** — Vente directe aux entreprises régulées + adoption développeurs via SDK et Claude Code.

**6. Réplication** — Complexité 9/10 pour la pile complète (modèles propres) ; 2/10 pour une couche verticale au-dessus de Vapi/Retell/Phonic. Angle Kyle : agent vocal vertical (cabinets, cliniques en France/UE, RGPD) plutôt que concurrencer l'infrastructure. Contexte : Phonic a levé $27,5M Series A (29 oct., First Round), signe d'un marché très financé.

## 🏆 TOP APP #3 : Glasshand
> Filtre partiel : critères = croissance PH (#1 du 5 nov., score 264), média/communauté légère. Manquent : revenus, viralité. Hardware-dependent (flotte d'iPhone/Mac) : exclusion à la limite, retenu faute de meilleur candidat.

**1. Identification** — Glasshand, https://glasshand.com/ — lancement PH le 5 nov. 2026, démo hackathon Vultr/Cerebral Valley le 26 sept. 2026. Fondateurs non identifiés. Catégorie : infra pour agents IA.

**2. Proposition de valeur** — Louer à un agent (Claude Code, Codex) de vrais iPhone et Mac dédiés, pas des émulateurs : test de login/paiement, installation d'apps, Xcode sur device physique, eSIM pour SMS de vérification, reset à la restitution. Pricing : iPhone $60/mois, Mac $90/mois, mensuel uniquement (https://glasshand.com/pricing/). Payant.

**3. Stack** — Parc de devices en datacenter, lecture d'écran et taps pilotés par agent. Détails non publiés.

**4. Psychologie** — Nouveauté, résolution d'une limite concrète des agents (apps mobiles vérifiées). Aha : une seule phrase au prompt et l'agent a un téléphone.

**5. Go-to-market** — Hackathon, puis Product Hunt ; cible les utilisateurs de coding agents.

**6. Réplication** — Complexité 7/10 (ops hardware, Apple, coûts fixes). Peu transposable pour Kyle ; idée adjacente : environnement de test téléphonique réel (appels, SIP) pour agents vocaux. Concurrent open source proche : Ghosthand (ghosthand.dev, $99/mois par Mac).

## 💰 Unit Economics Deep Dive — Beacon
Tout chiffre ci-dessous est une `estimation` sauf mention contraire ; aucun revenu public pour Beacon.

| Indicateur | Valeur |
|---|---|
| Financement | $5,5M seed (source : TNW) |
| ARR | < $200K (estimation, produit surtout gratuit/OSS) |
| ARPU | ~$20/mois côté Pro (prix non confirmé), ~$0 côté OSS |
| Users | milliers de devs OSS (estimation, étoiles non vérifiées) |
| CAC | ≈ $0 côté OSS, élevé côté vente entreprise (estimation) |
| LTV | ~$240–480 par Pro (12–24 mois, estimation) |
| LTV/CAC | non calculable fiablement |
| Payback | n/a |
| Burn / Runway | ~$150–250K/mois, 22–36 mois (estimation, équipe petite) |
| Rev/Employee | < $50K (estimation) |
| Rule of 40 | non applicable (pré-revenu) |

**Verdict santé : 🟡** — financé et bien lancé, mais monétisation non prouvée, positionnement flou (mémoire vs télémétrie) et concurrence open source forte.

## 🎯 Opportunity Scorecard — Top 3
| App | Market 20% | Complex. inv. 15% | TTM 15% | Compét. inv. 15% | Revenue 20% | Fit Kyle 15% | **Score** | Verdict |
|---|---|---|---|---|---|---|---|---|
| Beacon | 6 | 7 | 7 | 3 | 5 | 5 | **5.50** | 🟠 WATCH |
| Guava | 8 | 2 | 2 | 3 | 8 | 8 | **5.45** | 🟠 WATCH |
| Glasshand | 5 | 4 | 4 | 6 | 6 | 3 | **4.75** | 🟠 WATCH |

Beacon et Guava sont quasi à égalité ; pour Kyle, une couche verticale voice AI au-dessus de l'infra de Guava est plus pertinente que le clone direct.

## 📈 Tendances Émergentes
- **Infra pour agents de code** : mémoire, télémétrie, skills. GitHub Trending hebdo : t3code (+16 235 étoiles), claude-mem (+9 318), impeccable (+9 303), hallmark (+6 994), taste-skill (+5 426), superpowers, anthropics/skills. Les « skills de design » pour coding agents explosent. Source : https://github.com/trending?since=weekly
- **Voice AI très financée** : Guava $12,5M (3 nov.), Phonic $27,5M Series A (29 oct.), Fish Audio $52M seed (28 juil.), Karta AI $3M seed.
- **Agents qui sortent du navigateur** : Glasshand (devices réels), Product Hunt dominé par des outils d'agents (Click, UnleashX, Rerun).
- **Apps grand public à contenu simple** : Scroll The Bible illustre un feed vertical + pub Meta pour une niche religieuse (revenus non vérifiés).
- Note collecte : treg indisponible ce jour, donc pas de Hacker News, Reddit, X ni classement App Store.

## 💡 Insights Actionnables
1. **Voice AI vertical France/UE** : ne pas concurrencer Guava/Phonic sur les modèles ; viser un agent vocal métier (santé, assurance) conforme RGPD, avec règles métier en code. Effort : ~6–8 semaines pour un MVP sur briques existantes (estimation).
2. **Mémoire/traçabilité pour agents vocaux** : transposer l'idée de Beacon aux transcripts d'appels pour en extraire des leçons réutilisables. Marché à valider avant de coder.
3. **Test téléphonique réel pour voice agents** : équivalent de Glasshand côté SIP/PSTN, complexité moindre que du hardware.
4. **Pattern marketing** : Scroll The Bible montre qu'un format de feed simple + pub Meta peut scaler vite ; à tester sur un vertical éducatif avant d'y croire, les chiffres étant non vérifiés.
5. **À corriger côté outil** : le collecteur treg renvoie 403 (tunnel proxy) ; vérifier l'allowlist réseau de l'environnement pour avoir HN, Reddit, X et classement App Store au prochain run.
