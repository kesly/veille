# 🔥 Market Scan — 2026-10-31

> ⚠️ Couverture partielle : Product Hunt et Hacker News inaccessibles depuis la session (domaines non autorisés), Reddit/X non scannés. Sources effectives : GitHub Trending hebdo + recherches web. Les chiffres d'ARR/CAC sont des estimations. Le thème dominant est « agent skills », donc des repos open-source plus que des apps classiques.

## 📊 Résumé Exécutif
- Apps analysées : 3 (tous open-source, écosystème « agent skills »)
- Top potentiel : Impeccable (design pour agents de code) — angle monétisable le plus clair
- Opportunités immédiates (BUILD NOW) : 0 (1 BUILD ADJACENT possible, voir scorecard)

## 🏆 TOP APP #1 : Impeccable
**1. Identification**
- Nom : Impeccable, par Paul Bakaus ([repo](https://github.com/pbakaus/impeccable)), Apache 2.0, gratuit
- Catégorie : skill de design pour agents de code (Claude Code, Cursor, etc.)
- Lancement : dérivé du skill « frontend-design » d'Anthropic. Date exacte non vérifiée.
- Buzz : ~11 300 étoiles cette semaine (#2 GitHub Trending hebdo) ; interview [Latent Space](https://latent.space/p/skill-engineering-design)

**2. Proposition de valeur**
- Problème : le design généré par IA est générique (« AI slop »).
- Solution : 1 skill, 23 commandes (audit, polish, critique, shape), ~60 règles de détection déterministes, itération live dans le navigateur.
- USP : un vocabulaire de design pour piloter l'agent, pas du one-shot.
- Cible : devs et fondateurs qui codent avec des agents. Prix : gratuit (`npx impeccable install`).

**3. Stack** : CLI Node, fichiers Markdown de skill, détecteurs de règles (le repo est indexé Rust), intégration navigateur. Pas de backend SaaS apparent.

**4. Psychologie**
- Triggers : autorité (créateur ex-Google/Chrome), aversion à la honte (« mon UI fait IA »), social proof via les étoiles.
- JTBD : « rendre mon app présentable sans designer ».
- Aha moment : `/impeccable audit` sort une liste précise de défauts sur son propre UI.

**5. Go-to-market** : distribution par le repo, install en une commande, podcast, effet de mode « skills » ; boucle virale : les devs partagent des avant/après.

**6. Réplication**
- Complexité 3/10 pour le skill ; 6/10 pour un produit hébergé.
- Verticaux adjacents : skills pour email, slides, accessibilité, copywriting FR.
- Angle Kyle : skill « voice UX » (design de parcours vocaux, audits de prompts d'agent vocal) ou audit UI SaaS en français.
- Temps de dev : 2-3 semaines pour un skill ; 2-3 mois pour un SaaS.

## 🏆 TOP APP #2 : Cloudflare security-audit-skill
**1. Identification**
- Nom : security-audit-skill, par Cloudflare ([repo](https://github.com/cloudflare/security-audit-skill)), MIT, gratuit
- Catégorie : sécurité / skill d'audit pour agents de code
- Buzz : ~12 800 étoiles cette semaine (#1 GitHub Trending) ; les agrégateurs donnent 33-43K étoiles au total (chiffres divergents). Couvert par plusieurs blogs ([exemple](https://fireup.pro/news/cloudflare-open-sources-its-ai-security-auditor-heres-why-it-matters)).

**2. Proposition de valeur**
- Problème : les audits par LLM confirment presque tout (faux positifs).
- Solution : audit en 6 phases (carte d'architecture, agents isolés par zone, agent « réfutateur » frais, vérification indépendante, rapport).
- USP : l'agent qui vérifie n'est jamais celui qui a trouvé.
- Cible : équipes dev avec agents de code. Gratuit. Prérequis : sandbox OS, Node.js.

**3. Stack** : Markdown de skill + validateurs Node.js, sous-agents parallèles, rapports JSON lisibles par machine.

**4. Psychologie**
- Triggers : autorité (marque Cloudflare), peur (faille de sécurité), nouveauté.
- JTBD : « savoir si mon code est exploitable sans payer un pentest ».
- Aha moment : un finding vérifié avec preuve, pas une liste de 200 alertes.

**5. Go-to-market** : open-source par une marque établie, distribution via Skills CLI, relais par les blogs. Pas de viral loop propre.

**6. Réplication**
- Complexité 4/10 pour copier le pattern ; la crédibilité Cloudflare n'est pas réplicable.
- Verticaux : audit RGPD/conformité, audit de prompts et d'agents vocaux (injection, fuite de PII).
- Angle Kyle : audit de sécurité des agents voice AI (le pattern « réfutateur » s'applique aux prompts).
- Temps de dev : 3-4 semaines (MVP).
- Note : le skill public est un point de départ, pas le système interne complet de Cloudflare.

## 🏆 TOP APP #3 : claude-seo
**1. Identification**
- Nom : claude-seo, par AgriciDaniel ([repo](https://github.com/AgriciDaniel/claude-seo)), MIT, gratuit (extensions DataForSEO, Firecrawl payantes)
- Catégorie : SEO / GEO (optimisation pour moteurs IA)
- Buzz : ~4 500 étoiles cette semaine, 8-12K au total selon les agrégateurs ([présentation](https://pasqualepillitteri.it/en/news/5860/claude-seo-claude-blog-open-source-skills)).
- ⚠️ Probablement lancé il y a plus de 6 mois : retenu pour la traction actuelle, hors filtre d'âge strict. Date non vérifiée.

**2. Proposition de valeur**
- Problème : audits SEO chers et fragmentés, nouveau besoin GEO/AEO.
- Solution : 19-21 sous-skills et 12-15 sous-agents (technique, on-page, E-E-A-T, schema, sitemap, GEO). Exemple : `/seo audit https://example.com`.
- Cible : freelances SEO, agences, fondateurs. Prix : gratuit.

**3. Stack** : plugin Claude Code, Python, intégrations DataForSEO / Firecrawl / génération d'images.

**4. Psychologie**
- Triggers : peur de disparaître des réponses IA, gain de temps, FOMO sur le GEO.
- JTBD : « apparaître dans ChatGPT/Perplexity et Google ».
- Aha moment : audit complet du site en une commande.

**5. Go-to-market** : repo open-source, plugin marketplace, articles SEO sur le repo lui-même, extensions payantes en upsell indirect.

**6. Réplication**
- Complexité 3/10.
- Verticaux : SEO local FR, GEO pour e-commerce, SEO d'agents vocaux/appels.
- Angle Kyle : audit GEO packagé en SaaS pour PME françaises, avec rapport en français.
- Temps de dev : 3-5 semaines.

## 💰 Unit Economics Deep Dive — Impeccable
⚠️ Impeccable est un projet open-source gratuit sans revenus publics. Tout ce qui suit est une **estimation** pour un hypothétique produit commercial dérivé, pas des données réelles.

| Métrique | Estimation |
|---|---|
| ARR actuel | ~0 € (OSS) |
| Users | probablement 10-50K installs (déduit des étoiles ; non vérifié) |
| ARPU (hypothétique version Pro) | ~15 €/mois |
| CAC | ~0-20 € (organique) |
| LTV | ~180 € (12 mois de rétention) |
| LTV/CAC | >9 si organique |
| Payback | <2 mois |
| Burn / Runway | ~0 (solo/side project) |
| Rev/Employee | n/a |
| Rule of 40 | n/a |

Scénario : 2 % de conversion sur 30K users × 15 €/mois ≈ 108K €/an ARR.

**Verdict : 🟡** Traction forte, modèle économique non prouvé. Sources : GitHub, [Latent Space](https://latent.space/p/skill-engineering-design). Pas de données Crunchbase/Tracxn.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Impeccable | security-audit | claude-seo |
|---|---|---|---|
| 📊 Market Size (20%) | 6 | 7 | 7 |
| ⚙️ Complexity inversé (15%) | 7 | 6 | 7 |
| ⏱️ Time-to-Market (15%) | 7 | 6 | 7 |
| 🏟️ Competition inversé (15%) | 3 | 4 | 3 |
| 💰 Revenue Potential (20%) | 4 | 6 | 5 |
| 🧑‍💻 Founder-Fit Kyle (15%) | 4 | 6 | 3 |
| **Score pondéré** | **5.0** 🟠 WATCH | **5.9** 🟠 WATCH | **5.1** 🟠 WATCH |

Calcul (ex. security-audit) : 7×.20 + 6×.15 + 6×.15 + 4×.15 + 6×.20 + 6×.15 = 5.9.

Honnêteté : produits gratuits, concurrence OSS énorme, monétisation floue. L'angle le plus proche de Kyle (audit d'agents voice AI) vaut un test rapide, pas un BUILD NOW.

## 📈 Tendances Émergentes
- **« Agent skills » = nouvelle catégorie virale** : 8 des 13 repos du trending hebdo sont des skills ou frameworks de skills pour agents de code ([GitHub Trending](https://github.com/trending?since=weekly)), dont obra/superpowers, anthropics/skills, taste-skill.
- **Skills verticaux** : design (impeccable, taste-skill), sécurité (Cloudflare), SEO/GEO (claude-seo). Chaque métier cherche son skill.
- **Vérification adversariale** entre agents (réfutateur indépendant) : un pattern qui se généralise.
- **Fichiers de comportement** type CLAUDE.md partagés comme produits (multica-ai/andrej-karpathy-skills, 4K étoiles/semaine).
- **GEO/AEO** : l'optimisation pour moteurs IA remplace progressivement le SEO classique.
- Signal faible : plugins pour « knowledge workers » (anthropics/knowledge-work-plugins).

## 💡 Insights Actionnables
1. **Tester un skill « voice agent audit »** (open-source) : prompts, injection, PII, latence, conformité. Distribution via GitHub, upsell vers un audit payant. MVP en 2-3 semaines.
2. **Copier le pattern d'ADN, pas le produit** : repo gratuit d'une personne crédible + install en une commande + démo avant/après.
3. **Monétiser autour du skill** : rapport hébergé, CI, dashboard d'équipe, version en français. Le skill lui-même reste gratuit.
4. **GEO pour PME françaises** : marché peu servi en français ; claude-seo prouve la demande.
5. **Corriger la veille** : autoriser `producthunt.com` et `news.ycombinator.com` dans les paramètres réseau de l'environnement pour couvrir PH/HN au prochain scan. Sans ça, le scan reste biaisé vers GitHub.
