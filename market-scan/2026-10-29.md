# 🔥 Market Scan — 2026-10-29

> ⚠️ Limites de ce run : news.ycombinator.com et producthunt.com sont hors de la liste des domaines autorisés de la session (à ajouter dans les réglages réseau). Les données viennent de recherches web + GitHub Trending. Chiffres non vérifiés à la source primaire = marqués (?).

## 📊 Résumé Exécutif
- Apps analysées : 3 (signaux partiels, aucune ne passe le filtre 3+ critères avec certitude)
- Top potentiel : Instinct (agent iMessage) pour l'angle voice/agent de Kyle
- Opportunités immédiates (BUILD NOW) : 0

## 🏆 TOP APP #1 : Instinct (agent IA sur iMessage)
**Confiance : faible** — une seule source secondaire (rapport a16z Top 100 Gen AI Consumer Apps, 7e éd.) : [a16z](https://a16z.com/100-gen-ai-apps-7/)

1. **Identification** : agent IA lancé en août 2026 sur iMessage ; cité avec Tomo, Poke, Lindy, Town comme produits à « centaines de milliers d'users ». Fondateurs : non vérifiés. Catégorie : assistant/agent conversationnel. Buzz : mention a16z, croissance virale (?).
2. **Valeur** : agent accessible dans une app déjà installée (zéro install, zéro onboarding). Cible : grand public. Pricing : non vérifié (?).
3. **Stack** : probablement LLM frontier + orchestration d'outils + passerelle iMessage/SMS (?). Non confirmé.
4. **Psychologie** : friction nulle, effet « texto à un ami », Aha moment dès le 1er message ; social proof via partage de conversations.
5. **GTM** : viralité par le canal messagerie, bouche-à-oreille, presse a16z.
6. **Réplication** : complexité 5/10 (la difficulté = fiabilité des agents + conformité messagerie). Angle Kyle : agent **vocal** sur WhatsApp/téléphone (appel entrant) pour le marché FR/EU, là où iMessage est minoritaire. Dev : 4-8 semaines MVP.

## 🏆 TOP APP #2 : Muse (app IA grand public)
**Confiance : faible** — chiffres tirés d'une newsletter ([monthindigital](https://monthindigital.substack.com/p/october-2026-95-of-marketers-have)), non recoupés.

1. **Identification** : « Muse », app IA grand public ; 10 M de téléchargements US en 40 jours (?), mais seulement 23 % d'actifs à la semaine 2 (?).
2. **Valeur** : détails produit non vérifiés. Signal clé : acquisition massive, rétention médiocre.
3. **Stack** : inconnue.
4. **Psychologie** : curiosité/nouveauté, FOMO ; pas de boucle d'habitude visible (rétention 23 %).
5. **GTM** : probablement paid/viral social ; non confirmé.
6. **Réplication** : non évaluable. Leçon : ne pas copier le pic de téléchargements, viser la rétention. Complexité ?/10.

## 🏆 TOP APP #3 : cloudflare/security-audit-skill
Sources : [GitHub Trending](https://github.com/trending?since=weekly), [Korben](https://korben.info/en/cloudflare-launches-ai-security-audit-skill.html), [Fireup](https://fireup.pro/news/cloudflare-open-sources-its-ai-security-auditor-heres-why-it-matters)

1. **Identification** : skill open source (MIT, **gratuit**) de Cloudflare qui transforme un agent de code en auditeur sécurité. #1 GitHub Trending hebdo : +16 002 stars/semaine ; ~43 k stars au 24/10 selon un article (?). Catégorie : dev tools / sécurité.
2. **Valeur** : audit multi-phases avec sous-agents chasseurs + vérificateur indépendant qui tente de réfuter chaque faille. Cible : devs/équipes sécu. Pricing : gratuit (marque Cloudflare = lead-gen).
3. **Stack** : fichiers Markdown (un par famille d'attaque), schéma JSON de rapport, validateurs JS sans dépendances. Installation via `npx skills add`.
4. **Psychologie** : autorité (Cloudflare), peur (failles), gratuité, simplicité d'installation.
5. **GTM** : open-source par une marque établie, distribution via l'écosystème « skills » d'agents.
6. **Réplication** : complexité 2/10 techniquement ; l'autorité de marque, elle, n'est pas réplicable. Angle Kyle : skills/plugins verticaux (audit conformité RGPD, qualité d'agents vocaux). Dev : 1-2 semaines.

## 💰 Unit Economics Deep Dive — Instinct
**Données insuffisantes** pour estimer honnêtement les unit economics d'Instinct (pas de revenus, pricing ni équipe publics). Estimations indicatives, hypothèses seulement :

| Métrique | Estimation |
|---|---|
| Users | ~100-500 k (a16z) |
| ARPU | inconnu (?) |
| ARR / CAC / LTV / Burn / Runway / Rule of 40 | non estimables |

Verdict santé : 🟡 non évaluable. À revérifier via Crunchbase/Tracxn quand un tour de table sera publié.

## 🎯 Opportunity Scorecard — Top 3
Scores subjectifs, données partielles.

| Dimension | Poids | Instinct | Muse | CF skill |
|---|---|---|---|---|
| 📊 Market Size | 20% | 8 | 6 | 5 |
| ⚙️ Complexity inversé | 15% | 5 | 5 | 9 |
| ⏱️ Time-to-Market | 15% | 6 | 5 | 9 |
| 🏟️ Competition inversé | 15% | 3 | 3 | 4 |
| 💰 Revenue Potential | 20% | 6 | 4 | 3 |
| 🧑‍💻 Founder-Fit Kyle | 15% | 7 | 3 | 5 |
| **Total** | | **5.9** 🟠 WATCH | **4.3** 🔴 SKIP | **5.4** 🟠 WATCH |

## 📈 Tendances Émergentes
- **Skills pour agents de code** : 8 des 11 repos du GitHub Trending hebdo sont des skills/plugins/harness pour Claude Code & co (security-audit-skill, impeccable, taste-skill, claude-seo, graphify, knowledge-work-plugins). Nouvelle couche de distribution.
- **Agents dans les apps de messagerie** (iMessage, Poke, Tomo) : zéro friction d'install.
- **Acquisition ≠ rétention** : Muse (10 M DL, 23 % actifs S2) rappelle le piège des pics de téléchargement.
- **Show HN** : volume x6 depuis ChatGPT, mais les posts à 20+ points restent à peu près stables ([source](https://hub.causo.ai/guides/show-hn-launch-playbook-technical-founders-2026)).

## 💡 Insights Actionnables
1. **Publier des skills verticaux** (voice AI QA, audit RGPD agents vocaux, SEO FR) : effort 1-2 semaines, distribution gratuite via l'écosystème skills, bon moyen de générer du lead pour les offres voice de Kyle.
2. **Prototyper un agent vocal/WhatsApp** pour PME FR en s'inspirant du modèle « zéro install » d'Instinct.
3. **Mesurer la rétention J7/J14 avant toute copie** d'un produit à gros téléchargements.
4. **Débloquer les sources** : autoriser news.ycombinator.com et producthunt.com dans les réglages réseau de la session pour des scans plus fiables.
