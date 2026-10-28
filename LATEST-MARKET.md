# 🔥 Market Scan — 2026-10-28

> ⚠️ **Limites de la collecte** : Product Hunt et Hacker News inaccessibles (domaines hors allowlist réseau de la session). Web search sans résultats exploitables pour PH/HN/Twitter/Reddit. Seule source fiable : GitHub Trending hebdo. Dates de lancement non vérifiables (stars très élevées → projets probablement > 6 mois pour certains : filtre d'exclusion appliqué avec réserve). Rapport = signaux faibles + analyse prudente.

## 📊 Résumé Exécutif
- Apps analysées : 3 (toutes open-source, source GitHub Trending 7j)
- Top potentiel : Orca (stablyai) — orchestration d'agents de code
- Opportunités immédiates (BUILD NOW) : 0 (1 BUILD ADJACENT possible)

## 🏆 TOP APP #1 : Orca (stablyai/orca)
**1. Identification** — [github.com/stablyai/orca](https://github.com/stablyai/orca) · org `stablyai` (tag "yc-backed", fondateurs non nommés) · date de lancement non vérifiée · dev tools · **open-source MIT, gratuit** (les agents tournent sur les abonnements de l'utilisateur).
Buzz : ~108k stars, +8 802 stars cette semaine (#9 trending), 17k commits, 3,8k PR, 4,1k issues → communauté très active.

**2. Proposition de valeur** — Problème : gérer plusieurs agents de code (Claude Code, Codex, OpenCode…) en parallèle est chaotique. Solution : app desktop, 1 worktree git par agent, vue unifiée, ~34 agents supportés. USP : compagnon mobile iOS/Android (suivi + relances), Design Mode (clic sur élément UI → HTML/CSS/screenshot envoyé à l'agent), worktrees SSH, annotation de diffs. Cible : devs qui orchestrent des flottes d'agents. Pricing : 0 €.

**3. Stack** — Electron + Vite, TypeScript, pnpm workspaces, terminal GPU, relai cloud mobile↔desktop (`cloud/`), CLI, intégrations GitHub/Linear.

**4. Psychologie** — Triggers : FOMO (« tout le monde parallélise ses agents »), gain de productivité immédiat, social proof (stars). JTBD : « superviser N agents sans perdre le contrôle ». Aha moment : un prompt envoyé à plusieurs agents, comparaison, merge du meilleur.

**5. GTM** — Distribution via GitHub/communauté dev, neutralité vis-à-vis des vendors (agnostique), open-source comme moteur de confiance ; boucle virale : partage de workflows/CLI. Monétisation future probable : cloud/relai/équipes (hypothèse).

**6. Réplication** — Complexité 7/10 (Electron + mobile + relai), 4-6 mois pour un MVP crédible. Verticaux adjacents : orchestration d'agents voix/support, QA, data. Angle Kyle : tableau de bord de supervision d'agents **voix** (appels en parallèle, transcription live, reprise humaine) plutôt que concurrencer un outil gratuit MIT.

## 🏆 TOP APP #2 : Graphify (Graphify-Labs/graphify)
**1. Identification** — [github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) · Graphify Labs (auteur probable : safishamsi, non confirmé) · date non vérifiée · dev tools/knowledge graph · **open-source Apache-2.0/MIT** + offre payante *Graphify Cloud* (essai 14 j).
Buzz : ~137k stars, +7 268 cette semaine (#6 trending), 13k forks.

**2. Proposition de valeur** — Problème : les agents « grep » des repos entiers et brûlent des tokens. Solution : graphe de connaissances (code, docs, SQL, PDF, vidéo) interrogeable (`query`, `path`, `explain`), parsing local tree-sitter (~40 langages), 0 crédit LLM pour le code, rapport `GRAPH_REPORT.md`. Installable comme skill dans 20+ assistants. Cible : utilisateurs d'agents de code. Pricing : gratuit + cloud.

**3. Stack** — Python 3.10+, tree-sitter, Leiden/networkx, serveur MCP, export Neo4j/FalkorDB, faster-whisper, backends LLM multiples, Docker.

**4. Psychologie** — Triggers : économie de tokens (coût), autorité (benchmark LOCOMO 0,497 recall@10 — auto-déclaré). JTBD : « donner du contexte fiable à mon agent ». Aha : la carte des « god nodes » d'un repo.

**5. GTM** — Distribution comme skill multi-assistants (présent partout où sont les devs), open-source → cloud payant, sponsoring.

**6. Réplication** — Complexité 6/10, 2-3 mois. Adjacent : graphe de connaissances sur transcriptions d'appels/CRM. Angle Kyle : mémoire graphe pour agents voix (historique client interrogeable).

## 🏆 TOP APP #3 : security-audit-skill (Cloudflare)
**1. Identification** — [github.com/cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · Cloudflare · date non vérifiée · sécurité/agents · **open-source MIT, gratuit**.
Buzz : ~50,5k stars, **+16 388 cette semaine (#1 trending)**, adossé à une marque d'autorité.

**2. Proposition de valeur** — Transforme un agent de code en auditeur sécurité en 6 phases (recon, chasse guidée par ledger de couverture, validation adverse, findings JSON schématisés, vérification indépendante, rapport). USP : findings vérifiés et machine-readable, runs additifs. Cible : équipes sécu/devs. Pricing : gratuit (coût = tokens).

**3. Stack** — Prompts Markdown, JSON Schema, validateurs Node.js sans dépendance, installation via Skills CLI, sandbox OS requis.

**4. Psychologie** — Autorité (Cloudflare), peur (failles), réduction de faux positifs. Aha : un rapport avec findings confirmés vs rejetés.

**5. GTM** — Le « marketing » est la marque ; publication d'une méthodologie interne comme contenu viral. Format « skill » = zéro friction d'adoption.

**6. Réplication** — Complexité 3/10 (prompts + schémas), 2-4 semaines. Verticaux : audit conformité RGPD, audit de prompts/agents voix, revue qualité d'appels. Angle Kyle : skill d'audit de sécurité/conformité pour agents voix (injection, fuite PII). Attention : la distribution vient de la marque, non réplicable.

## 💰 Unit Economics Deep Dive — Orca
Produit 100 % gratuit/MIT : **aucune donnée financière publique** (non vérifiable sans Crunchbase/Tracxn/SimilarWeb, inaccessibles ici). Estimations très spéculatives :

| Métrique | Estimation |
|---|---|
| ARR | ~0 € (pas de tier payant visible) |
| Users | non publié (108k stars ≠ users actifs) |
| ARPU / CAC / LTV / LTV-CAC / Payback | N/A (CAC ≈ 0, organique) |
| Burn / Runway | inconnus ; équipe visiblement large (17k commits), financement YC supposé |
| Rev/Employee, Rule of 40 | N/A |

**Verdict santé : 🟡** — traction communautaire exceptionnelle, monétisation inexistante pour l'instant ; risque : les vendors (Anthropic, OpenAI) intègrent nativement l'orchestration.

## 🎯 Opportunity Scorecard — Top 3
| Dimension (poids) | Orca | Graphify | Security-audit-skill |
|---|---|---|---|
| 📊 Market Size (20%) | 7 | 6 | 6 |
| ⚙️ Complexité inversée (15%) | 4 | 6 | 8 |
| ⏱️ Time-to-Market (15%) | 4 | 6 | 8 |
| 🏟️ Competition inversée (15%) | 3 | 4 | 5 |
| 💰 Revenue Potential (20%) | 4 | 5 | 5 |
| 🧑‍💻 Founder-Fit Kyle (15%) | 4 | 5 | 5 |
| **Score pondéré** | **4,6 🟠 WATCH** | **5,4 🟠 WATCH** | **6,2 🟡 BUILD ADJACENT** |

Scores prudents : données financières et dates manquantes, concurrence open-source gratuite forte.

## 📈 Tendances Émergentes
- **Skills/plugins pour agents de code** dominent GitHub Trending (security-audit-skill, claude-seo, knowledge-work-plugins, android/skills, CLAUDE.md de Karpathy) : le « skill » devient un format de distribution.
- **Orchestration de flottes d'agents** : Orca, ruflo, opencode.
- **Mémoire/contexte pour agents** : Graphify, ai-memory (Rust).
- Sources : [GitHub Trending](https://github.com/trending?since=weekly). Show HN : volume ×6 depuis ChatGPT mais peu de posts percent ([zeli.app](https://zeli.app/es/story/49712005)).

## 💡 Insights Actionnables
1. Publier un **skill d'audit pour agents voix** (sécurité + conformité RGPD/PII) : coût faible, canal de distribution = Skills CLI, positionne Kyle comme autorité voice AI.
2. Ne pas concurrencer les outils MIT d'orchestration ; viser la **supervision d'agents voix** (angle vertical).
3. Débloquer l'accès réseau à Product Hunt, Hacker News (et Reddit/X) pour de vrais scans : cette session n'a vu que GitHub.
