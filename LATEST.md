# AI Watch — 2026-04-13 Soir

> Veille générée le 2026-04-13 à 16h08 UTC | Couvre les 12 dernières heures et l'actualité chaude de la semaine

---

## 🔥 Breaking

> Releases majeures, annonces qui changent la donne

### Claude Mythos Preview + Project Glasswing (Anthropic)
- **Quoi** : Anthropic publie son modèle le plus puissant à ce jour — mais ne le rend pas public, l'accès est réservé à un consortium de 40+ entreprises (Microsoft, Amazon, Apple, Google, NVIDIA, CrowdStrike, Palo Alto Networks, JPMorgan Chase…)
- **Lien** : https://www.anthropic.com/glasswing
- **Pourquoi c'est important** : Mythos atteint 93,9 % sur SWE-bench Verified et 94,6 % sur GPQA Diamond. Lors des tests internes, le modèle a découvert et exploité de façon autonome des zero-days dans **chaque** OS majeur et chaque navigateur. Bloomberg rapporte une réunion d'urgence convoquée par Bessent et Powell réunissant des PDG de grandes banques. Anthropic investit 100 M$ en crédits d'utilisation pour la détection et le patching de failles critiques. C'est la première fois qu'un modèle frontier est **volontairement retenu** pour risque systémique.
- **Testable** : Non — accès exclusif via Project Glasswing

### Stanford AI Index 2026 — Publié aujourd'hui
- **Quoi** : Le rapport annuel de référence du HAI Stanford vient de paraître (13 avril 2026)
- **Lien** : https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report
- **Pourquoi c'est important** : Conclusion-clé : les modèles de pointe continuent de progresser malgré les prédictions de plateau. Dans la course US vs Chine, **Anthropic mène**, suivi par xAI, Google et OpenAI. L'adoption IA dépasse déjà celle du PC et d'Internet à stade équivalent. 3/4 des gains économiques de l'IA sont captés par 20 % des entreprises (PwC).
- **Testable** : Oui — rapport librement téléchargeable

---

## 🆕 Nouveaux Outils & Produits

### Claw Code — Framework open-source de coding agent
- **Quoi** : Réécriture clean-room de l'architecture de Claude Code, en Python/Rust. 72 000+ étoiles GitHub en quelques jours (100 000 atteints, un record historique)
- **Lien** : https://github.com/ultraworkers/claw-code
- **Pourquoi c'est important** : Né accidentellement suite à la publication involontaire du code source de Claude Code sur npm (512 000 lignes de TypeScript, source map de 59,8 Mo dans le package v2.1.88). La communauté a immédiatement reconstruit un fork indépendant. Support multi-agents, tool-calling, orchestration autonome. **Open-source, gratuit.**
- **Testable** : Oui — `git clone` + Dockerfile disponible

### Microsoft Agent Framework 1.0
- **Quoi** : Lancement du framework d'orchestration multi-agents de Microsoft, avec support natif MCP et A2A 1.0
- **Lien** : https://learn.microsoft.com/en-us/agent-framework/agents/tools/local-mcp-tools
- **Pourquoi c'est important** : APIs stables, engagement LTS, interopérabilité cross-runtime entre agents hétérogènes. Soutien MCP (97 M+ téléchargements/mois) + A2A v1.0 imminent. Positionne Microsoft comme fournisseur d'infrastructure agent-native en entreprise. **Gratuit (open-source).**
- **Testable** : Oui — disponible sur NuGet/npm dès maintenant

### Google Colab MCP Server
- **Quoi** : Serveur MCP open-source permettant à tout agent IA de se connecter directement à Google Colab (exécution de code, notebooks, GPU cloud)
- **Lien** : https://developers.googleblog.com/announcing-the-colab-mcp-server-connect-any-ai-agent-to-google-colab/
- **Pourquoi c'est important** : Ouvre l'environnement d'exécution Colab (GPUs gratuits, bibliothèques préinstallées) aux workflows agentiques — un agent peut maintenant lancer et superviser du code Python dans le cloud sans action humaine. **Open-source, gratuit.**
- **Testable** : Oui — install via pip + config MCP

### Telnyx — LiveKit on Telnyx (Voice AI Platform)
- **Quoi** : Plateforme hébergée LiveKit sur infrastructure propre Telnyx, intégrant téléphonie enterprise + IA vocale (STT/TTS) en latence ultra-basse
- **Lien** : https://telecomreseller.com/2026/04/10/telnyx-launches-livekit-on-telnyx-for-deploying-voice-ai-agents-with-lower-cost-and-ultra-low-latency/
- **Pourquoi c'est important** : 50 % moins cher que LiveKit Cloud sur STT/TTS, round-trip <200 ms, audio qui ne quitte pas le réseau Telnyx. Les développeurs déploient leurs agents LiveKit existants sans modifier le code (juste un Dockerfile). **Bêta gratuite.**
- **Testable** : Oui — bêta ouverte

### OpenAI — Nouveau palier $100/mois ChatGPT Pro
- **Quoi** : Nouveau plan intermédiaire à 100 $/mois (entre le Plus à 20 $ et le Pro à 200 $), avec 5× le quota Codex du Plus (×10 en promo jusqu'au 31 mai 2026)
- **Lien** : https://thenextweb.com/news/openais-new-100-chatgpt-pro-plan-targets-claude-max-with-five-times-the-codex-access
- **Pourquoi c'est important** : Réponse directe au Claude Max d'Anthropic. Ajoute des sièges Codex-only en pay-as-you-go et baisse le tarif annuel Business. Signal d'une guerre des prix en cours sur le segment développeur. **Payant.**
- **Testable** : Oui — souscription sur chatgpt.com

### Google Vids + Veo 3.1 — Vidéo IA gratuite pour tous
- **Quoi** : Google upgrade sa suite Vids avec génération vidéo (Veo 3.1), musique (Lyria), et avatars IA directables — **offert sans frais à tous les comptes Google**
- **Lien** : https://autogpt.net/state-of-ai-video/
- **Pourquoi c'est important** : Production vidéo professionnelle accessible gratuitement à des milliards d'utilisateurs. Clips jusqu'à 2 minutes en passe unique. Concurrence directe à Runway, Sora, Kling. **Gratuit.**
- **Testable** : Oui — via Google Workspace / workspace.google.com

---

## 🧠 Mises à jour de Modèles

### Meta Muse Spark — Premier modèle des Meta Superintelligence Labs
- **Quoi** : Premier modèle issu de la nouvelle entité Meta Superintelligence Labs dirigée par Alexandr Wang (ex-Scale AI). Score 52 sur l'Artificial Analysis Intelligence Index (top 5 mondial)
- **Lien** : https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/
- **Pourquoi c'est important** : Meta abandonne son identité open-source avec ce modèle 100 % propriétaire. Pas de poids téléchargeables, pas de Llama ici. Architecture MoE, entraîné avec 10× moins de compute que Llama 4 Maverick comparable. Rupture stratégique majeure pour Meta. **Payant/API uniquement.**
- **Testable** : Accès limité — Meta AI app

### Google Gemma 4 — Open source Apache 2.0
- **Quoi** : Famille de modèles ouverts en 4 tailles (2B, 4B, 26B MoE, 31B Dense), nativement multimodaux, contexte 256K, 140+ langues
- **Lien** : https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html
- **Pourquoi c'est important** : Le 31B Dense est #3 mondial sur Arena AI parmi les modèles open source. Apache 2.0 = usage commercial sans restriction. Support audio, image, function calling natifs. **Gratuit, open-source.**
- **Testable** : Oui — Hugging Face + Google AI Studio

### Alibaba Wan 2.7 — Génération image/vidéo avec "Thinking Mode"
- **Quoi** : Suite vidéo MoE 27B (14B actifs) : text-to-video, image-to-video, reference-to-video, édition vidéo. 720p/1080p, 2 à 15 secondes. Pricing : 0,10 $/seconde de vidéo
- **Lien** : https://markets.financialcontent.com/stocks/article/abnewswire-2026-4-6-alibaba-launches-wan-27-breakthrough-ai-image-and-video-generation-model-with-thinking-mode
- **Pourquoi c'est important** : Le "Thinking Mode" (plan-puis-génère) réduit drastiquement les artefacts et améliore la cohérence narrative. Disponible sur Together AI. Architecture MoE plus économique que les modèles denses concurrents. **Payant à l'usage.**
- **Testable** : Oui — via Together AI API

### Mistral Small 4 — Modèle multimodal unifié ultra-bon marché
- **Quoi** : Fusion de Magistral (raisonnement), Pixtral (vision) et Devstral (coding) en un seul modèle à 0,15 $/M tokens en entrée
- **Lien** : https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide
- **Pourquoi c'est important** : 5× moins cher que GPT-5.4 Mini en entrée, 7,5× en sortie. Raisonnement + vision + code dans un seul appel API. Rapport qualité/prix imbattable pour les applications à fort volume. **Payant, très bon marché.**
- **Testable** : Oui — Mistral API + La Plateforme

### Alibaba HappyHorse-1.0 — #1 vidéo sur Artificial Analysis
- **Quoi** : Modèle de génération vidéo d'Alibaba (ATH AI Innovation Unit) apparu discrètement sur la plateforme Artificial Analysis, qui a grimpé au sommet des classements text-to-video et image-to-video en tests à l'aveugle
- **Lien** : https://www.cnbc.com/2026/04/10/alibaba-happyhorse-ai-video-model-benchmark-reveal.html
- **Pourquoi c'est important** : Révélé sur un compte X nouvellement créé, encore en développement. Alibaba domine désormais les deux premiers rangs vidéo (HappyHorse + Wan 2.7). Accélère la course chinoise sur la génération multimédia. **Pas encore public.**
- **Testable** : Non — en développement

### Zhipu GLM-5.1 — 744B MoE, licence MIT, bat GPT-5.4
- **Quoi** : Modèle mixture-of-experts de 744 B paramètres (40B actifs), contexte 200K, licence MIT — bat Claude Opus 4.6 et GPT-5.4 sur SWE-Bench Pro
- **Lien** : https://llm-stats.com/ai-news
- **Pourquoi c'est important** : Open source MIT avec des performances frontier sur le coding — combinaison rare. La Chine positionne un modèle compétitif directement utilisable en production sans restrictions de licence. **Gratuit, open-source.**
- **Testable** : Oui — Hugging Face

---

## 🔬 Research

### Tufts — VLA Neuro-Symbolique : ×100 sur l'efficacité énergétique
- **Quoi** : Système VLA (Visual-Language-Action) combinant réseaux de neurones et raisonnement symbolique pour la robotique, publié le 5 avril 2026
- **Lien** : https://www.sciencedaily.com/releases/2026/04/260405003952.htm
- **Pourquoi c'est important** : Réduit la consommation énergétique par un facteur 100 **tout en améliorant** la précision. Approche radicalement différente des VLAs purement connexionnistes. Potentiel majeur pour la robotique embarquée et les applications edge. **Open-access.**
- **Testable** : Code à venir — papier disponible

### xAI — Tous les 11 co-fondateurs ont quitté (crise structurelle)
- **Quoi** : Les 11 co-fondateurs originels d'xAI ont tous quitté l'entreprise au 27 mars 2026. Musk reconstruit "depuis les fondations". Nouvelles recrues : Andrew Milich, Jason Ginsberg, Devendra Chaplot (co-fondateur de Mistral AI)
- **Lien** : https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide
- **Pourquoi c'est important** : Rupture organisationnelle totale chez le concurrent direct d'OpenAI/Anthropic. Recrutement de talents Mistral suggère une réorientation technique. Impact incertain sur Grok et la roadmap modèles. **À surveiller.**
- **Testable** : N/A

### Google TurboQuant — Accélération KV cache (ICLR 2026)
- **Quoi** : Algorithme présenté à ICLR 2026 qui résout le goulot d'étranglement mémoire du KV cache dans les LLMs via quantification vectorielle optimisée
- **Lien** : https://www.devflokers.com/blog/new-ai-papers-arxiv-last-24-hours-april-2026
- **Pourquoi c'est important** : Accélère l'inférence à long contexte sans dégradation de qualité mesurable. Applicable à tout modèle transformer — potentiel d'adoption large dans les semaines à venir.
- **Testable** : Code bientôt sur GitHub (ICLR open-source policy)

---

## 📝 À surveiller

> Tendances émergentes, betas, rumeurs crédibles

- **GPT-5.5 "Spud"** : Pré-entraînement terminé chez OpenAI. Annonce imminente probable.
- **GPT Image 2** : Déploiement progressif en cours pour une sous-population d'utilisateurs ChatGPT.
- **Claude Mythos public ?** : La pression sur Anthropic pour une ouverture partielle est forte — Project Glasswing pourrait évoluer vers un accès API restreint d'ici l'été 2026.
- **Meta et l'open-source** : Des sources indiquent que Meta prépare un pivot retour vers l'open-source pour ses prochains modèles après l'échec d'engagement sur Muse Spark vs OpenAI/Google.
- **MCP v2.1 Server Cards** : Nouveau standard `.well-known/mcp.json` pour la découverte automatisée de serveurs MCP — à intégrer dès adoption.
- **Bulle VC IA ?** : 300 Mds$ investis en un seul trimestre (Q1 2026), dont 65 % dans 4 entreprises. Les indicateurs de valorisation sont au-delà de tout précédent historique.
- **MCP v2.1 + A2A 1.0** : La convergence des deux standards d'interopérabilité agents (Anthropic MCP + Google A2A) via Microsoft Agent Framework est le signal le plus important pour l'infrastructure IA 2026.

---

## 📊 Résumé

- **Top 3 du jour** :
  1. **Claude Mythos / Project Glasswing** — Anthropic retient son meilleur modèle pour raisons de sécurité nationale, fait appel à 40 entreprises tech pour patcher les OS/navigateurs. Rupture de paradigme dans la publication de modèles frontier.
  2. **Stanford AI Index 2026** — Référence mondiale publiée aujourd'hui : l'IA continue d'accélérer, l'adoption dépasse PC/Internet, Anthropic mène la course technique.
  3. **Microsoft Agent Framework 1.0 + MCP 97M installs** — L'infrastructure pour agents IA est maintenant mature et standardisée. Le pipeline MCP → Agent → A2A devient le pattern dominant en entreprise.

- **À tester en priorité** :
  - 🟢 **Google Gemma 4** (open-source, Apache 2.0, top 3 open models) → Hugging Face, dispo maintenant
  - 🟢 **Claw Code** (framework agent coding open-source viral) → GitHub, dispo maintenant
  - 🟢 **Telnyx LiveKit beta** (voice AI, -50% coût, <200ms) → bêta gratuite ouverte
  - 🟢 **Mistral Small 4** (reasoning + vision + code, le moins cher du marché) → Mistral API
  - 🟢 **Google Vids + Veo 3.1** (vidéo IA gratuite pour tous) → Google Workspace
  - 🟢 **Google Colab MCP Server** (agents IA + GPU cloud Colab) → pip install
