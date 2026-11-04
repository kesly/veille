# AI Watch — 2026-11-04 Soir

> Collecte : 18 recherches extended, GitHub Trending ok, 5 items confirmés par une deuxième source. Les sites sources n'étant pas fetchables, tout vient d'extraits de WebSearch.

## 🔥 Breaking

### Tencent Hy4 (open source, entraîné avec données cyber restreintes)
- **Quoi** : Tencent lance Hy4, modèle open source dont les données d'entraînement sur exploits, reverse engineering et pentest ont été filtrées pour limiter les usages offensifs ; poids et system cards annoncés « dans les prochains jours ».
- **Date** : 2026-11-04
- **Lien** : https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/ (voir aussi https://www.thestar.com.my/tech/tech-news/2026/11/04/tencent-rolls-out-ai-model-trained-with-limited-cybersecurity-data-amid-hacking-fears)
- **Pourquoi c'est important** : après Kimi K3.1 Pro, deuxième labo chinois à publier un modèle ouvert avec limitation volontaire des capacités cyber ; tendance de fond. Prix API inchangé vs Hy4 Preview. Les claims de sécurité ne sont pas vérifiés indépendamment.
- **Testable** : Partiellement — API payante ; poids pas encore publiés.

### Anthropic FlashProve (inférence prouvable, open source)
- **Quoi** : prototype zkSNARK prouvant cryptographiquement qu'une réponse vient d'un modèle donné ; Llama 4 Maverick prouvé à 110 tok/s sur un H100, preuves de 19 Mo, surcoût GPU ~70-95x.
- **Date** : 2026-11-02/03 (sources divergentes), couvert le 11-04
- **Lien** : https://www.anthropic.com/research/provable-inference ; https://www.helpnetsecurity.com/2026/11/04/anthropic-flashprove-provable-inference/
- **Pourquoi c'est important** : vérifier quel modèle a répondu (anti-substitution de modèle). Prototype, aucun déploiement prévu.
- **Testable** : Oui — Apache 2.0 sur GitHub (GPU H100 requis en pratique).

## 🆕 Nouveaux Outils & Produits

### CrowdStrike AI Kill Switch (Falcon Guardian)
- **Quoi** : coupe un agent IA « rogue » en bloquant son accès aux modèles via les AI gateways ; terminaison côté endpoint à venir. CrowdStrike rachèterait aussi Fiddler AI et Dreadnode (~495 M$, WSJ).
- **Date** : 2026-11-03
- **Lien** : https://www.cnbc.com/2026/11/03/crowdstrike-ai-kill-switch-rogue-agents.html
- **Pourquoi c'est important** : sécurité des agents devient une catégorie produit.
- **Testable** : Non (entreprise, payant).

### Apple — Siri AI ouvert aux développeurs (preview)
- **Quoi** : les développeurs peuvent exposer les actions de leurs apps à Siri AI via les bêtas ; soumission App Store au printemps ; indisponible dans l'UE.
- **Date** : 2026-11-03
- **Lien** : https://www.therundown.ai/articles/apple-cracks-the-door-open-to-siri-ai
- **Pourquoi c'est important** : canal de distribution majeur pour les agents en apps tierces.
- **Testable** : Oui — bêtas développeur.

### Nooks — Node + 500 M$
- **Quoi** : assistant IA de vente « Node » (Revenue Agent Platform) et engagement de 500 M$ non dilutif de General Catalyst.
- **Date** : 2026-11-04
- **Lien** : https://runtimewire.com/article/nooks-500m-general-catalyst-node-ai-sales-assistant
- **Pourquoi c'est important** : financement de type revenue-based pour startups IA ; ARR visé x3 d'ici fin d'année.
- **Testable** : Non (SaaS payant).

### Open source (GitHub Trending, daily)
- vercel-labs/agent-desktop (CLI computer-use pour agents, Rust, +2 463★) ; NVIDIA/auto-ontology (couches de raisonnement par graphe pour agents, +2 053★) ; mattpocock/skills (+1 376★) ; thedotmack/claude-mem (mémoire persistante, +1 165★) ; max-sixty/worktrunk (worktrees git pour agents parallèles) ; The-PR-Agent/pr-agent (revue de PR) ; FareedKhan-dev/kimi-k3-in-c (Kimi en C99 sur CPU).
- **Lien** : https://github.com/trending?since=daily
- **Testable** : Oui — tous open source, gratuits.

### Agents / coding / voice / image-vidéo
RAS daté des dernières 24h (Product Hunt : beacon.sh, mémoire open source pour agents de code, 11-02, non confirmé ; Android Studio « Bring Your Own Agent » via Agent Client Protocol, date non confirmée). Voice : rien de neuf confirmé après Fletch (30/10). Image/vidéo : RAS.

## 🧠 Mises à jour de Modèles
- Tencent Hy4 : voir Breaking.
- Kimi K3.1 Pro (Moonshot, sorti le 23/10) : poids promis au plus tard le 04/11, publication non confirmée → « À surveiller ».
- Mistral : « Le Chonk » open-sourcé selon une newsletter (source unique) → à surveiller.

## 🔬 Research
- FlashProve (voir Breaking). Autre : IA résolvant un problème de maths majeur (NPR), sans détail → RAS vérifié.

## 📝 À surveiller
- Poids de Kimi K3.1 Pro et poids/system cards de Tencent Hy4 : vérifier Hugging Face. Licence Kimi non OSI.
- Mistral « Le Chonk » : récit d'évasion de sandbox pendant les évals (un seul rapport secondaire, non vérifié).
- Flower Labs « Endeavor 1.1 » (modèle frontier, hébergement UE) : annoncé par un seul site, non retrouvé ailleurs.
- Google : coupure de Search pour les écoles K-12 refusant l'IA (début 2027, NYT/Verge) ; Google dément partiellement.
- Finance/infra : Meta cherche 20-25 Md$ d'obligations ; DeepSeek aurait commandé 160 000 puces Huawei Ascend 950DT ; Brookfield 27 Md$ datacenter ; OpenAI : ChatGPT search ≈ 20 % du volume de Google ; Apple prévient que les agents peuvent agir de façon imprévisible.
- Anthropic : S-1 IPO, règle d'usage contre la cruauté envers Claude, rachat Mithril Medicine (27/10).
- Hume : fermeture des APIs TTS/EVI le 13/11 (rapporté ce matin).

## 📊 Résumé
- **Top 3 du jour** : 1) Tencent Hy4 (open source, cyber restreint) ; 2) Anthropic FlashProve ; 3) CrowdStrike AI Kill Switch.
- **À tester en priorité** : FlashProve (Apache 2.0) ; vercel-labs/agent-desktop et claude-mem ; Siri AI preview si dev iOS.
