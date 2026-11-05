# 🔥 Market Scan — 2026-11-05

> Collecte : 16 recherches extended, GitHub Trending ok (14 repos), 4 candidats creusés (Subvocal écarté : hardware). Réseau limité : PH/HN lus via extraits de recherche. Reddit/X/Indie Hackers : peu de signal frais (index faible).

## 📊 Résumé Exécutif
- Apps analysées : 3 (beacon.sh, HackerBooks, Cedric AI for Meetings) — **filtre partiel** pour les 3 (voir détails)
- Top potentiel : beacon.sh (mémoire open-source pour agents de code) 
- Opportunités immédiates (BUILD NOW) : 0 (1 BUILD ADJACENT probable)

## 🏆 TOP APP #1 : beacon.sh (Asymptote Labs)
**Filtre buzz : partiel (4/6 : traction/levée, croissance PH, engagement, communauté/GitHub ; manque viralité 10K+ mentions et médias).**

### 1. Identification
- Nom : beacon.sh — agent-beacon · [beacon.sh](https://beacon.sh/) · [GitHub](https://github.com/Asymptote-Labs/agent-beacon) · [Product Hunt](https://www.producthunt.com/products/asymptotelabs?launch=beacon-sh)
- Lancement : 20 oct. 2026 (levée + open-source), PH le 2 nov. 2026
- Fondateurs : Asymptote Labs (noms non vérifiés)
- Catégorie : dev tools / mémoire d'agents IA
- Buzz : #1 PH du 2 nov. (439 pts, 83 commentaires), seed 5,5 M$ (Tower Research Ventures) selon [ByteIota](https://byteiota.com/beacon-sh-agent-memory-that-survives-switching-coding-tools/), ~2,3k stars GitHub au 21 oct. (non revérifié)

### 2. Proposition de valeur
- Problème : chaque outil de code IA (Claude Code, Cursor, Codex…) oublie ; les leçons ne sont pas portables.
- Solution : enregistre les sessions de 20+ agents, extrait des « findings » et skills réutilisables.
- USP : cross-harness + auto-amélioration ; lessons validées par l'humain avant réinjection.
- Cible : devs et équipes qui utilisent plusieurs agents.
- Pricing : open-source MIT gratuit ; Cloud 0 $ (50 findings), Pro 20 $/mois, Enterprise sur devis ([source](https://eraofminds.com/blog/beacon-memory-coding-agents/), à confirmer).

### 3. Stack technique
Non publié en détail. Capture locale + dashboard local, couche cloud pour findings d'équipe. Intégrations par hooks des harness. (estimation)

### 4. Psychologie
- Triggers : douleur universelle (« l'agent a oublié »), autorité (seed + MIT), gratuité.
- JTBD : « arrêter de ré-expliquer mon projet à chaque session ».
- Aha moment : première skill générée automatiquement à partir d'une session passée.

### 5. Go-to-market
- Open-source d'abord, PH 2 semaines après, Discord communautaire. Même tendance sur GitHub Trending : claude-mem (8,8k stars/sem.), superpowers, skills.
- Boucle virale : skills/mémoires partageables entre équipes.

### 6. Réplication
- Complexité : 6/10. Temps : 2-3 mois pour un MVP crédible.
- Verticaux adjacents : mémoire pour agents vocaux (appels, CRM), mémoire pour agents support.
- Angle Kyle : « mémoire/learning loop pour agents voice AI » (transcripts d'appels → skills/prompts améliorés).
- Risque : marché encombré (claude-mem etc.), plateformes (Anthropic/Cursor) peuvent l'internaliser.

## 🏆 TOP APP #2 : HackerBooks
**Filtre buzz : partiel (3/6 : viralité, engagement, communauté ; manque traction revenus et croissance durable).**

### 1. Identification
- Nom : HackerBooks · [Show HN](https://news.ycombinator.com/item?id=50326821) · auteur roansh · lancé ~1er nov. 2026 · catégorie : agrégateur de contenu / curation
- Buzz : 1 771–1 852 pts, ~300 commentaires, réponse de Karpathy ([Best of Show HN](https://bestofshowhn.com/2026), [GIGAZINE](https://gigazine.net/gsc_news/en/20261102-hackerbooks-mentioned-books-hacker-news/))

### 2. Proposition de valeur
- Problème : trouver les livres réellement recommandés par une communauté experte.
- Solution : ~16,5k livres cités par au moins 2 commentateurs HN distincts, liens vers les commentaires.
- Pricing : gratuit ; monétisation via liens affiliés Bookshop/Amazon (divulgués).

### 3. Stack technique
JS vanille + JSON statique sur Cloudflare ; pipeline écrit presque entièrement par Claude Opus 5.5 ([DEV](https://dev.to/puneet_nanda_dc25d8b489ad/hacker-news-has-a-bookshelf-the-ranking-is-the-hard-part-ige)). Open Library pour les couvertures (qualité critiquée).

### 4. Psychologie
- Triggers : preuve sociale (HN), curiosité, nostalgie communautaire, autorité (Karpathy).
- JTBD : « quel livre lire ensuite, validé par des pairs ».
- Aha : voir le top 10 classé et cliquer sur les commentaires d'origine.

### 5. Go-to-market
- Show HN pur, copie d'un format viral (HackerTube de Karpathy). Clones immédiats (HackerShelf).
- Un commentateur note que le trafic tombe à zéro après la sortie de la front page.

### 6. Réplication
- Complexité : 2/10. Temps : un week-end. Aucune barrière : pas de moat.
- Verticaux : « livres/outils/podcasts cités par la communauté X » (r/SaaS, X, YC founders, voice AI).
- Angle Kyle : annuaire des outils voice AI cités par devs, avec affiliation/leads sponsorisés. Revenu faible, utile comme canal d'acquisition.

## 🏆 TOP APP #3 : Cedric AI for Meetings
**Filtre buzz : partiel (2-3/6 : croissance PH, engagement modeste, communauté PH ; manque levée publique, revenus, médias).**

### 1. Identification
- Nom : Cedric AI for Meetings · [meet-cedric.com](https://meet-cedric.com/use-cases/ai-meeting-assistant) · [Product Hunt](https://producthunt.com/products/cedric) · PH le 2 nov. 2026 (Launch of the Day, ~238 votes, 34 commentaires) ; produit Cedric lancé 15 oct.
- Fondateurs : Benjamin Ben Hattar (co-fondateur/CTO, [LinkedIn](https://www.linkedin.com/in/benhattar/)) ; Zurich, SFF Studio. Aucune levée trouvée.
- Catégorie : assistant de réunion IA / voice-adjacent

### 2. Proposition de valeur
- Problème : les note-takers ne font que résumer.
- Solution : agent qui rejoint Meet/Zoom/Teams, présente des slides, répond aux questions, attend à la place de l'utilisateur.
- Pricing : freemium (100k crédits ≈ 50 $), Team dès 19 $/mois (source vendeur, à confirmer). Payant, propriétaire.

### 3. Stack technique
Non publié. Probablement bot de réunion + STT/TTS + LLM + intégrations Slack/Telegram/Discord (estimation).

### 4. Psychologie
- Triggers : gain de temps, FOMO (« envoyer son clone »), code promo PH.
- JTBD : « ne plus assister aux réunions inutiles ».
- Aha : l'agent répond en direct à une question en réunion.

### 5. Go-to-market
PH (code PRODUCTHUNT2026), SEO de pages use-cases/blog, LinkedIn fondateurs. Positionnement élargi « AI teammate for startups » (aggregateur agentic.ai : score 11/36).

### 6. Réplication
- Complexité : 6/10 (latence voix, bots de réunion). Temps : 6-8 semaines.
- Verticaux : réunions commerciales FR, webinaires, comités médicaux/juridiques (hors régulation lourde : éviter).
- Angle Kyle : expert voice AI, agent de réunion francophone avec présentation + réponses, sur-mesure pour ventes/CS. Marché très concurrentiel (Fireflies, Otter, Read, etc.).

## 💰 Unit Economics Deep Dive — beacon.sh
Tout chiffre ci-dessous est une `estimation` (aucune donnée de revenu publique ; seed 5,5 M$ cité par ByteIota).

| Métrique | Estimation |
|---|---|
| Users | ~5-15k installs actifs (2,3k stars) `estimation` |
| Conversion payant | 2-3 % `estimation` |
| ARPU payant | 20 $/mois (Pro) |
| ARR | ~30-90 k$ `estimation` (démarrage) |
| CAC | ~0-30 $ (organique OSS) `estimation` |
| LTV | ~240 $ (12 mois, churn dev tools élevé) `estimation` |
| LTV/CAC | >8 si organique `estimation` |
| Payback | <2 mois `estimation` |
| Burn | ~150-250 k$/mois (équipe 8-12) `estimation` |
| Runway | ~22-35 mois sur 5,5 M$ `estimation` |
| Rev/employé | ~5-10 k$ `estimation` |
| Rule of 40 | non pertinent (pré-revenu) |

**Verdict : 🟡** — financé, distribution OSS efficace, mais monétisation non prouvée et risque d'absorption par les plateformes.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | beacon.sh | HackerBooks | Cedric Meetings |
|---|---|---|---|
| 📊 Market Size (20%) | 7 | 3 | 8 |
| ⚙️ Complexity inversé (15%) | 5 | 9 | 5 |
| ⏱️ Time-to-Market (15%) | 5 | 10 | 6 |
| 🏟️ Competition inversé (15%) | 3 | 6 | 2 |
| 💰 Revenue Potential (20%) | 6 | 2 | 6 |
| 🧑‍💻 Founder-Fit Kyle (15%) | 5 | 4 | 8 |
| **Score pondéré** | **5.3** | **5.4** | **5.9** |
| Verdict | 🟠 WATCH | 🟠 WATCH | 🟠 WATCH |

Calcul Cedric : 8×.2+5×.15+6×.15+2×.15+6×.2+8×.15 = 1.6+.75+.9+.3+1.2+1.2 = 5.95 → **5.9-6.0**, à la frontière 🟡 BUILD ADJACENT si angle francophone/vertical précis. beacon.sh : 1.4+.75+.75+.45+1.2+.75 = 5.3. HackerBooks : .6+1.35+1.5+.9+.4+.6 = 5.35 (arrondi 5.4, 🟠).

Scores honnêtes : aucun BUILD NOW ce jour.

## 📈 Tendances Émergentes
1. **Mémoire/skills pour agents de code** : GitHub Trending dominé par claude-mem (8,8k stars/sem.), superpowers, anthropics/skills, worktrunk, hallmark, impeccable ([GitHub Trending](https://github.com/trending?since=weekly)). Le « skills layer » est le nouveau plugin.
2. **Clones viraux en 24h via IA** : HackerTube (Karpathy) → HackerBooks → HackerShelf ; copie de Subvocal en un jour. Le moat se déplace vers distribution/données.
3. **Voice/silent interfaces** : Subvocal (YC F26, 1,3 M$ pré-seed, précommandes 499 $, 7,3M vues X) ; hardware donc exclu ([Show HN](https://news.ycombinator.com/item?id=50340088), [Dealroom](https://app.dealroom.co/news/note/subvocal-raises-1-3m-pre-seed-to-turn-silent-speech-into-computer-commands)). Voice AI financé : Gradium 100 M$ seed (Paris), Fish Audio 52 M$, Modulate 25 M$, Vapi 50 M$ Series B.
4. **Seeds verticaux IA** : Clark (audit, 11 M$), Archiboost (construction, 6,2 M$) — agents spécialisés par métier.
5. **Réserve** : Product Hunt dominé par boîtes financées ; peu de signal indie frais (Reddit/X/IH non indexés).

## 💡 Insights Actionnables
1. **Testeur rapide (week-end)** : annuaire « outils voice AI cités par devs/fondateurs » façon HackerBooks, pour capter du trafic SEO FR/EN et des leads vers ton expertise. Faible revenu direct, bon canal.
2. **Piste principale (6-8 semaines)** : agent de réunion/appel vocal francophone vertical (ventes, recrutement) ; différenciateur = latence + français. Valider avec 5 prospects avant de coder.
3. **Idée adjacente** : boucle d'apprentissage pour agents voice (transcripts → findings → prompts), inspirée de beacon.sh. Monter un prototype open-source et regarder les stars.
4. **Distribution** : open-source d'abord, PH ensuite (beacon.sh) ; Show HN avec un format copiable (HackerBooks).
5. **À surveiller** : Subvocal (expédition T1 2027), évolution des stars de beacon.sh, saturation des mémoires d'agents.
