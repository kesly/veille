# 🔥 Market Scan — 2026-10-22

> ⚠️ Limites : Product Hunt, HN Algolia inaccessibles (réseau) ; seule la page GitHub Trending a été lue en direct. Les autres chiffres viennent d'agrégateurs (aitoolly.com, blogs) et sont **auto-déclarés / non vérifiés**.

## 📊 Résumé Exécutif
- Apps analysées : 3 (toutes open-source, signal GitHub Trending)
- Top potentiel : VoiceStudio (voice AI local, aligné Kyle)
- Opportunités immédiates (BUILD NOW) : 0 (1 BUILD ADJACENT voice)

## 🏆 TOP APP #1 : VoiceStudio (ex-OmniVoice Studio)
**1. Identification**
- [github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) · dev solo Palash Debnath · lancé 2026 (couverture sept-oct) · catégorie : voice AI desktop
- Buzz : +15K stars/semaine sur [GitHub Trending](https://github.com/trending?since=weekly) ; >50K stars total et 646 langues (auto-déclaré, [aitoolly](https://aitoolly.com/ai-news/article/2026-10-01-voicestudio-emerges-as-an-open-source-local-elevenlabs-alternative-supporting-646-languages)) ; ~1,6K forks ; v0.5.2 ([release](https://newreleases.io/project/github/debpalash/VoiceStudio/release/v0.5.2))
- Critères buzz : viralité ✅, croissance ✅, communauté ✅ (forks), médias ⚠️ (agrégateurs seulement)

**2. Proposition de valeur**
- Problème : ElevenLabs & co = payant, cloud, vie privée, quotas
- Solution : clonage de voix (~3 s d'audio), voice design, doublage vidéo, dictée, transcription, audiobooks, 100 % local
- USP : « alternative locale à ElevenLabs », sans compte ni clé API ni limite
- Cible : créateurs, traducteurs/doubleurs, devs privacy-first
- Pricing : **gratuit, open-source AGPL-3.0**

**3. Stack** : Python (moteurs TTS/ASR locaux), app desktop, backends CPU + Apple Silicon + GPU, pas d'infra serveur.

**4. Psychologie** : trigger = « gratuit vs abonnement » + chiffre choc (646 langues) ; JTBD = « doubler/cloner une voix sans payer ni envoyer mes données » ; Aha = voix clonée en 3 s, localement.

**5. GTM** : GitHub Trending + agrégateurs d'actualités IA qui répètent le pitch ; positionnement anti-incumbent ; AGPL = boucle communautaire (forks, contributions).

**6. Réplication** : complexité 5/10 (assemblage de modèles open-source), 2-3 mois pour un MVP. Verticaux : doublage pour e-commerce FR, agents vocaux on-prem, dictée métier (médical/juridique). Angle Kyle : version **hébergée/entreprise RGPD** + voice agents FR, là où l'AGPL local bloque les entreprises.

## 🏆 TOP APP #2 : REA (morluto/rea)
**1. Identification**
- [github.com/morluto/rea](https://github.com/morluto/rea) · morluto · apparu sur GitHub Trending ~8-16 oct. 2026 ([aitoolly](https://aitoolly.com/ai-news/article/2026-10-14-morluto-releases-rea-an-open-source-framework-enabling-ai-agents-to-reverse-engineer-software-and-na)) · catégorie : outils agents / reverse engineering
- Buzz : #1 GitHub Trending hebdo, « 129K stars/semaine » affiché par la page trending — **chiffre suspect, à vérifier** (possible manipulation/bug). Peu de discussion indépendante → 2 critères seulement, borderline.

**2. Proposition de valeur** : CLI + serveur MCP permettant à des agents de coder de rétro-ingénierer apps et binaires natifs (analyse Hopper, dossiers de fonctions, preuves reproductibles « Evidence v2 », capture de process). Cible : chercheurs sécurité, devs. Pricing : open-source gratuit.

**3. Stack** : TypeScript, MCP, intégration Hopper (outil tiers payant), ~50-70 tools.

**4. Psychologie** : autorité (reverse engineering = expertise), curiosité ; JTBD = « comprendre une app sans les sources » ; Aha = l'agent produit un dossier de fonction.

**5. GTM** : écosystème MCP/skills (porté par la vague Claude Code), trending GitHub.

**6. Réplication** : complexité 8/10, 6+ mois ; niche dual-use, risque légal/éthique. Angle Kyle faible (hors voice/SaaS). À surveiller seulement.

## 🏆 TOP APP #3 : HyperFrames (HeyGen)
**1. Identification**
- [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) · HeyGen · open-sourcé avril-juin 2026 (dates divergentes : [noqta](https://www.noqta.tn/en/blog/heygen-hyperframes-html-to-mp4-ai-agent-video-2026), [aitoolly](https://aitoolly.com/ai-news/article/2026-06-24-heygen-launches-hyperframes-a-new-framework-to-write-html-and-render-video-built-specifically-for-ai)) → **~4-6 mois, limite du filtre**
- Buzz : +5,7K stars cette semaine (trending), soutenu par une entreprise financée ; communauté via hyperframes.dev.

**2. Proposition de valeur** : « vidéo as code » : l'agent écrit HTML/CSS/GSAP, la CLI rend un MP4. Cible : devs, marketeurs techniques, équipes de contenu automatisé. Pricing : Apache 2.0 gratuit (monétisation indirecte via HeyGen).

**3. Stack** : Node ≥22, Chrome headless + FFmpeg, skills pour Claude Code/Cursor/Codex.

**4. Psychologie** : « agents-native » (tendance), JTBD = « générer des vidéos de lancement par prompt » ; Aha = MP4 pixel-perfect depuis un prompt.

**5. GTM** : open-source comme top-of-funnel d'un SaaS existant, installation `npx skills add`, galerie communautaire de remix.

**6. Réplication** : complexité 6/10, 1-2 mois pour un wrapper SaaS. Verticaux : vidéos produit auto, reporting vidéo, sous-titrage/voix off. Angle Kyle : HyperFrames + voix IA FR = générateur de vidéos explicatives avec voix off automatique.

## 💰 Unit Economics Deep Dive — VoiceStudio
Projet open-source sans revenus publics : estimations **spéculatives**, non sourcées (pas de données Crunchbase/Tracxn).

| Métrique | Estimation |
|---|---|
| ARR | ~0 € (pas de monétisation) |
| ARPU | 0 € |
| Users | 50K+ stars ≈ dizaines de milliers d'installs (non vérifié) |
| CAC | ~0 € (organique) |
| LTV / LTV:CAC | n/a |
| Burn / Runway | quasi nul (dev solo) / illimité tant que bénévole |
| Rev/Employee | n/a |
| Rule of 40 | n/a |

**Verdict : 🟡** — traction exceptionnelle, modèle économique inexistant. La valeur est dans la monétisation que le projet laisse ouverte : hébergé, support entreprise, licence commerciale (l'AGPL oblige à acheter une licence ou à ouvrir son code). Benchmark : ElevenLabs facture des abonnements récurrents, preuve que la demande payante existe.

## 🎯 Opportunity Scorecard — Top 3
| App | Market (20%) | Complexité inv. (15%) | TTM (15%) | Compétition inv. (15%) | Revenue (20%) | Fit Kyle (15%) | **Total** | Verdict |
|---|---|---|---|---|---|---|---|---|
| VoiceStudio | 8 | 5 | 6 | 3 | 7 | 9 | **6.5** | 🟡 BUILD ADJACENT |
| REA | 4 | 3 | 3 | 6 | 4 | 2 | **3.8** | 🔴 SKIP |
| HyperFrames | 7 | 5 | 6 | 4 | 6 | 6 | **5.8** | 🟠 WATCH |

Notes : VoiceStudio — marché voice énorme mais ElevenLabs et autres saturent ; l'angle viable est B2B FR/RGPD. Scores prudents vu la qualité des données.

## 📈 Tendances Émergentes
- **Agents-native tooling** : skills, MCP, plugins dominent GitHub Trending (claude-plugins-official, scientific-agent-skills, android/skills, cursor/plugins, context-mode, ruflo) — [GitHub Trending](https://github.com/trending?since=weekly).
- **Local-first / privacy** : alternatives open-source locales aux SaaS IA payants (voix).
- **Open-source comme funnel** d'entreprises (HeyGen) plutôt que produit final.
- Signal faible : outils de réduction de contexte pour agents de code.

## 💡 Insights Actionnables
1. **Voix locale = trou B2B** : proposer une offre hébergée UE / on-prem (clonage + dictée + doublage) pour entreprises qui ne peuvent pas utiliser l'AGPL ni envoyer leurs audios aux US. Prototype d'abord sur doublage/voix off FR.
2. **Combo vidéo-as-code + voix IA** : un générateur de vidéos explicatives par prompt (HyperFrames + TTS) pour SaaS français — MVP en quelques semaines.
3. **Vérifier avant d'agir** : les stars de REA (129K/sem) et VoiceStudio (50K+) sont à contrôler sur GitHub ; le scan n'a pas pu couvrir Product Hunt, HN, Reddit, X.
4. Ne pas investir dans le reverse engineering (hors fit, risque légal).
