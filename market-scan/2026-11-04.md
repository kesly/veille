# 🔥 Market Scan — 2026-11-04

> Collecte : 22 recherches extended, GitHub Trending ok, 3 candidats creusés (Beacon, Guava, Hacker Times). Product Hunt/HN/BetaList lus via extraits WebSearch uniquement. Reddit/X/Indie Hackers : aucun signal frais exploitable.

## 📊 Résumé Exécutif
- Apps analysées : 3
- Top potentiel : Beacon (Asymptote Labs) — mémoire partagée open-source pour agents de code
- Opportunités immédiates (BUILD NOW) : 0 (voir scorecard)

## 🏆 TOP APP #1 : Beacon (beacon.sh)
**1. Identification**
- Nom : Beacon — [beacon.sh](https://beacon.sh/) · repo [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) · **open-source (MIT)**, cloud gratuit à ce jour
- Lancement PH : ~2 nov. 2026, #1 du jour (score 439, 83 commentaires) — [PH daily](https://www.producthunt.com/leaderboard/daily/2026/11/2). L'outil existait ~2 semaines avant (X/blog)
- Fondateurs : Justin D'Souza (CEO), Shukan Shah (CTO), ex-Doppel — [Tower Research](https://tower-research.com/asymptote-labs-the-system-of-record-for-agentic-work/)
- Catégorie : dev tools / mémoire et télémétrie pour agents de code
- Buzz : #1 PH, ~3 249 stars GitHub, 288 forks (source WebSearch), seed 5,5 M$ le 20 oct. ([TNW](https://thenextweb.com/news/asymptote-labs-5-5m-seed-ai-agent-security)), relais X (Akshay Pachaar) → 4 critères : viralité modérée, PH, traction/levée, communauté (Discord)

**2. Proposition de valeur**
- Problème : chaque agent (Claude Code, Cursor, Codex…) travaille en silo, les corrections ne se transmettent pas
- Solution : capture les sessions de 20+ harnesses, en tire des mémoires/skills réutilisables via MCP ou Agent Skills
- USP : cross-harness + local-only possible + open-source
- Cible : développeurs, puis équipes sécurité/entreprises
- Pricing : gratuit ; plateforme payante (blocage d'actions risquées, fuites de données) non tarifée publiquement

**3. Stack** : CLI installable via Homebrew, hooks par harness, MCP/Agent Skills, Beacon Cloud (sync). Détails infra non publiés.

**4. Psychologie**
- Triggers : douleur de re-expliquer au contexte, FOMO « agents qui apprennent », autorité (investisseurs Cursor/Vercel), gratuité
- JTBD : « que mes agents arrêtent de refaire les mêmes erreurs »
- Aha : une correction faite dans Cursor est appliquée par Claude Code

**5. Go-to-market**
- Open-source comme entonnoir (Tower a découvert la boîte via la traction OSS), lancement PH, créateurs X/newsletters ([Daily Dose of DS](https://blog.dailydoseofds.com/p/give-claude-code-codex-and-cursor)), forks communautaires
- Monétisation : OSS → plateforme sécurité entreprise

**6. Réplication**
- Complexité 6/10 (hooks multi-harness fragiles). Temps : MVP 4–6 semaines (estimation)
- Verticaux : mémoire d'agents voix/support, mémoire pour agents commerciaux
- Angle Kyle : mémoire cross-session pour agents voix (transcripts d'appels → corrections réutilisables) plutôt que concurrencer sur le code

## 🏆 TOP APP #2 : Guava (goguava.ai)
**1. Identification**
- Guava — [goguava.ai](https://goguava.ai) · **payant** (free tier dev), propriétaire
- Annonce : seed 12,5 M$ le 3 nov. 2026, mené par Acrew Capital ([FinSMEs](https://www.finsmes.com/2026/11/guava-raises-12-5m-in-seed-funding.html), [Pulse 2.0](https://pulse2.com/guava-raises-12-5-million-seed-round-led-by-acrew-capital-for-voice-ai-platform/))
- Fondateurs : Omri Dahan (CEO), Anthony Scodary, Nico Benitez (ex-Gridspace), Mike Piechna (CRO). Los Angeles
- Catégorie : plateforme développeur voice agents (santé, finance, assurance)
- Buzz : levée, modèle Daytona (sept. 2026) avec 12+ clients entreprise et des dizaines de milliers d'appels/jour (déclaratif), presse multiple. Filtre partiel : pas de viralité sociale, c'est un signal B2B/levée

**2. Proposition de valeur**
- Problème : les stacks voix assemblées (STT+LLM+TTS de vendeurs différents) sont fragiles en production réelle
- Solution : stack intégré propre (reconnaissance, LLM, synthèse), SDK Python/TypeScript/Claude Code
- USP : latence déclarée <1 s bout en bout, <200 ms prise de parole (chiffres société, via [CarrierX](https://app.dealroom.co/news/feed/guava-and-carrierx-deploy-16-khz-hd-voice-ai-agents-with-sub-1-second-latency-for-regulated-industries)) ; SOC 2 Type II, HITRUST i1, PCI DSS L1
- Cible : entreprises réglementées et BPO
- Pricing : non publié. Référence marché : Vapi ~0,05 $/min hébergement, ElevenLabs 0,08 $/min, Retell 0,07–0,31 $/min ([comparatif](https://www.stork.ai/blog/best-ai-voice-agent-platforms-2026))

**3. Stack** : modèles propriétaires ASR/LLM/TTS, téléphonie via partenaires (CarrierX), SDK dev.

**4. Psychologie** : autorité (certifs conformité), réassurance (« premier appel réglementé en 14 jours »), onboarding <5 min en gratuit. JTBD : mettre un agent voix en prod sans cauchemar de latence/conformité. Aha : agent fonctionnel en 5 min.

**5. Go-to-market** : product-led côté dev (free tier, SDK), sales entreprise/BPO financé par la levée, partenariats opérateurs.

**6. Réplication**
- Complexité 9/10 pour copier le stack ; 4/10 pour une couche verticale par-dessus. Temps : 2–3 mois pour un vertical (estimation)
- Angle Kyle : ne pas concurrencer l'infra, vendre un agent voix verticalisé (cabinets, cliniques, immobilier FR/EU) avec conformité RGPD/hébergement UE, point faible d'un acteur US

## 🏆 TOP APP #3 : Hacker Times (hackertimes.ca)
**1. Identification**
- Hacker Times — [hackertimes.ca](https://hackertimes.ca/) · Show HN [item 50346981](https://news.ycombinator.com/item?id=50346981) · gratuit, code source non confirmé
- Lancement : ~3 nov. 2026 ; créateur non identifié dans les sources
- Catégorie : lecteur Hacker News « journal papier », front page éditée par IA
- Buzz : ~450 points / 145 commentaires sur HN ([front 03-11](https://news.ycombinator.com/front)). **Filtre partiel** : un seul critère fort (engagement HN) ; pas de revenus ni de levée

**2. Proposition de valeur** : lisibilité éditoriale (plus de détail par histoire, moins de densité) pour un flux tech. Pas de monétisation visible. Cible : lecteurs HN. Concurrents/clones existants : [etnt/hacker-times](https://github.com/etnt/hacker-times), [terryds/hackernewstimes](https://github.com/terryds/hackernewstimes) (React 19, Vite, Tailwind, Cloudflare Workers/KV, Resend, newsletter hebdo).

**3. Stack** : inconnue pour le site ; les clones utilisent API HN, Jina Reader, Cloudflare.

**4. Psychologie** : nostalgie/familiarité (marque NYT détournée), jeu esthétique, curiosité. Aha : voir la page HN familière en une du journal. Risque : critique « un clone de plus » et question de droits de marque relevées dans le fil.

**5. Go-to-market** : Show HN seul, effet de communauté, zéro budget.

**6. Réplication**
- Complexité 2/10, 1 week-end. Zéro moat
- Angle Kyle : appliquer le format « journal éditorial » à un flux de niche (veille voice AI en français) avec newsletter payante — l'intérêt est le canal Show HN, pas le produit

## 💰 Unit Economics Deep Dive — Beacon / Asymptote Labs
Aucune donnée financière publique : tout ce qui suit est `estimation`. Seuls faits sourcés : seed 5,5 M$ (20 oct. 2026), fonds pour ingénierie/recrutement/ventes ([TNW](https://thenextweb.com/news/asymptote-labs-5-5m-seed-ai-agent-security)), outil OSS gratuit, plateforme payante sans grille publique.

| Métrique | Valeur |
|---|---|
| ARR | ~0 à <0,3 M$ `estimation` (produit payant pré-commercial) |
| ARPU | non applicable (gratuit) ; entreprise visée ~20–50 k$/an `estimation` |
| Users | milliers (3 249 stars GitHub, source WebSearch) ; payants inconnus |
| CAC | ~0 côté OSS/PH ; vente entreprise 15–30 k$ `estimation` |
| LTV | 60–150 k$ sur 3 ans `estimation` |
| LTV/CAC | ~3–5 `estimation`, non vérifiable |
| Payback | 9–15 mois `estimation` |
| Burn | ~250–350 k$/mois (équipe 10–15) `estimation` |
| Runway | ~16–22 mois `estimation` |
| Rev/employé | ~0 aujourd'hui |
| Rule of 40 | non calculable (pas de revenu) |

**Verdict : 🟡** — financé et traction OSS réelle, mais aucun revenu prouvé, et la monétisation dépend d'un pivot vers la sécurité entreprise. Risque : les éditeurs d'agents (Anthropic, Cursor) intègrent la mémoire nativement.

## 🎯 Opportunity Scorecard — Top 3
| App | 📊 Market (20%) | ⚙️ Complexité inv. (15%) | ⏱️ TTM (15%) | 🏟️ Compét. inv. (15%) | 💰 Revenu (20%) | 🧑‍💻 Fit Kyle (15%) | **Total** | Verdict |
|---|---|---|---|---|---|---|---|---|
| Beacon | 7 | 6 | 7 | 4 | 5 | 4 | **5,55** | 🟠 WATCH |
| Guava (infra voix) | 9 | 2 | 3 | 3 | 8 | 8 | **5,80** | 🟠 WATCH |
| Hacker Times | 2 | 10 | 10 | 2 | 2 | 3 | **4,55** | 🟠 WATCH |

Variante honnête : **agent voix verticalisé UE** inspiré de Guava (marché 8, complexité 6, TTM 6, compétition 5, revenu 7, fit 9) = **6,90 → 🟡 BUILD ADJACENT**. Scores = jugement subjectif, sans données de revenus vérifiées.

## 📈 Tendances Émergentes
- **Mémoire/contexte d'agents** : Beacon #1 PH, et GitHub Trending hebdo dominé par claude-mem (~8 k stars), superpowers, skills, taste-skill, hallmark, impeccable ([trending](https://github.com/trending?since=weekly)). Les « skills » pour agents de code sont la catégorie OSS la plus chaude.
- **Voice AI financée en B2B réglementé** : Guava 12,5 M$, Karta AI 3 M$ (banques), Modulate 25 M$ (sept.), Smallest.ai 13 M$ ([TechCrunch](https://techcrunch.com/2026/09/28/modulate-raises-25m-for-its-voice-models-and-analysis-suite/)).
- **Sécurité/gouvernance d'agents** : Asymptote, Klarent (8 M$) ; l'OSS sert d'entrée vers l'entreprise.
- **Show HN plus saturé** : part des posts à 10+ points passée de 14,5 % à 7,8 % ([DEV](https://dev.to/pennyforgehq/your-odds-of-getting-any-traction-on-show-hn-have-fallen-by-a-third-your-odds-of-getting-real-28eb)).
- Le Product Hunt hebdo est en partie du placement payant (« Promoted »).

## 💡 Insights Actionnables
1. **Playbook OSS → entreprise** (Beacon) : outil gratuit local-first, lancement PH, relais de créateurs X, puis couche payante sécurité. Reproductible pour un outil voix : open-sourcer un SDK d'évaluation/mémoire d'agents voix.
2. **Opportunité Kyle (BUILD ADJACENT)** : agent voix vertical pour PME européennes (RGPD, hébergement UE, français natif) bâti sur briques existantes (Vapi/Retell/ElevenLabs à 0,05–0,08 $/min), en s'appuyant sur le fait que les leaders sont US et ciblent les grands comptes.
3. **Test rapide (1 week-end)** : « mémoire des appels » — transcripts d'appels → corrections réutilisables par l'agent suivant, lancé en OSS sur Show HN/PH.
4. **À surveiller** : si Anthropic/Cursor sortent une mémoire cross-agent native, Beacon perd son USP ; suivre les stars du repo et la grille tarifaire de Beacon Cloud.
5. **Limites de ce scan** : Reddit, X, Indie Hackers n'ont rien renvoyé de frais ; aucun MRR public vérifié. Les fonds levés ne prouvent pas un revenu.
