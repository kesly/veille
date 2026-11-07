# AI Watch — 2026-11-07 Matin

> Collecte : treg 0/4 sources (indisponible), 16 recherches extended, GitHub Trending ok, 0 page lue (lecture treg en échec), 4 items confirmés par une deuxième source.

## 🔥 Breaking

### OpenAI GPT-6 Cyber
- **Quoi** : Modèle spécialisé cybersécurité (détection de failles, exploits, vérification de correctifs). 48,5 % sur ExploitGym contre 32,1 % pour GPT-5.6 Cyber (chiffres constructeur). OpenAI cite 81 failles Firefox inconnues trouvées ; classé « Critical » dans son Preparedness Framework.
- **Date** : 5 novembre 2026
- **Lien** : https://thenextweb.com/news/openai-gpt-6-cyber-launch-firefox-linux-daybreak-red ; https://www.securityweek.com/openai-says-new-gpt-6-cyber-model-hunts-flaws-without-crossing-the-line/
- **Pourquoi c'est important** : Premier modèle OpenAI classé Critical ; accès restreint, signe d'une gouvernance par paliers des capacités offensives.
- **Testable** : Non — réservé à des clients Daybreak Red approuvés (API et Codex), payant, sans prix public.

### Meta rachète Conductor
- **Quoi** : Meta acquiert Conductor (orchestration de plusieurs agents de code en parallèle : Claude Code, Codex, Cursor). Équipe intégrée à Meta Superintelligence Labs.
- **Date** : 4 novembre 2026
- **Lien** : https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/ ; https://siliconangle.com/2026/11/04/meta-acquires-ai-coding-startup-conductor-whose-app-runs-several-coding-agents-at-once/
- **Pourquoi c'est important** : Consolidation sur la couche d'orchestration multi-agents de code ; le service cloud ferme le 20 novembre.
- **Testable** : Oui, jusqu'au 20 nov. (service cloud de Conductor).

## 🆕 Nouveaux Outils & Produits

### Perplexity Teammates
- **Quoi** : Agents persistants qui prennent en charge un projet dans la durée (basés sur Perplexity Computer, intégration Slack).
- **Date** : 4-5 novembre 2026
- **Lien** : https://mlq.ai/news/perplexitys-teammates-put-always-on-ai-agents-behind-a-200-monthly-paywall/
- **Pourquoi c'est important** : Concurrence directe des agents de travail OpenAI/Anthropic.
- **Testable** : Oui — preview web, abonnés Max (~200 $/mois, payant).

### OpenAI ChatGPT Images 2.6 (GPT-Image-2.6 Flare / Sunburst)
- **Quoi** : Génération d'images 50 % plus rapide, GIF à partir de prompts/photos/croquis ; arrivée dans l'API.
- **Date** : ~4 novembre 2026
- **Lien** : https://community.openai.com/c/announcements/6
- **Pourquoi c'est important** : Gain de vitesse et nouveau format animé. Source unique côté officiel (forum) + trackers.
- **Testable** : Oui — ChatGPT / API (payant).

### Gemini Omni 1.2 Flash (vidéo)
- **Quoi** : Génération/édition vidéo GA, clips jusqu'à 15 s, prix 720p −30 % (0,07 $/s), cohérence de personnages.
- **Date** : 5 novembre 2026
- **Lien** : https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available
- **Pourquoi c'est important** : Vidéo pro à coût réduit ; dispo dans Google Vids et l'app Gemini (Pro/Ultra).
- **Testable** : Oui — Gemini API, Vertex, Google Vids (payant).

### Voix : Gemini 3.8 Flash TTS (voice remixing), Gradium Phonon, AssemblyAI-TTS-1
- **Quoi** : Google ajoute le « remix » de voix par prompt (AI Studio / API, 4 nov.) ; Gradium ouvre Phonon, un TTS on-device (5 nov.) ; AssemblyAI sort son premier TTS pour agents vocaux (sem. du 26 oct.-1 nov.).
- **Lien** : https://cryptobriefing.com/google-launches-voice-remixing-for-gemini-38-flash-tts-in-ai-studio ; https://www.assemblyai.com/blog/voice-ai-in-2026-series-1
- **Pourquoi c'est important** : Le TTS se banalise chez les fournisseurs STT ; option open source locale avec Phonon.
- **Testable** : Oui — AI Studio (Gemini) ; Phonon open source (Hugging Face).

## 🧠 Mises à jour de Modèles

- **DeepSeek deepseek-v4-flash-0731** : listé le 5 nov. par des trackers (source unique, à vérifier). https://llmgateway.io/timeline
- **Tencent Hy4** (3 nov.) et **NVIDIA Nemotron 3.5 Transcribe** (STT open source) cités sur Product Hunt via un digest tiers. https://github.com/HuggerHustle/ai-radar/issues/172

## 🔬 Research
RAS (rien de vérifié sur la période). Note : METR estime que les modèles Anthropic progressent ~2× plus vite qu'il y a un an (rapporté par des digests).

## 📝 À surveiller
- **Mistral Large 4 en open weights** (1T paramètres MoE, ~50B actifs, licence Mistral Ecosystem Open-Weight, vLLM day-0) : poids publiés le 29 oct., plus de 72 h, mais couvert dans les digests du 6 nov. https://mistral.ai/news/mistral-large-4-oss/
- **Marchés / IPO Anthropic** : forte baisse des valeurs IA (Nasdaq −5,5 % jeudi selon un digest), valorisation d'IPO Anthropic révisée à ~1,1-1,3 T$ (Bloomberg, 6 nov.) ; marketing d'IPO prévu la semaine prochaine, report possible. https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout
- **Sécurité** : bug signalé dans Claude Code exposant l'e-mail du compte dans le User-Agent des recherches web (source unique, à confirmer) ; campagne attribuée à un groupe lié à la Chine utilisant l'outil « Artex » (source unique).
- **Dropbox** rachète Tigris Data (350 M$) pour les builders d'agents (source unique).
- **Gemini** : dès le 13 nov., les modèles Pro réservés aux abonnés AI Pro+ ; arrêt de plusieurs modèles preview Gemini 3 (TTS, Live) le 17 nov. https://ai.google.dev/gemini-api/docs/deprecations
- **Kling VIDEO 4.0** (clips jusqu'à 30 s) : dates contradictoires selon les sources.
- **Open source GitHub Trending** : NVIDIA/auto-ontology (framework de couches de raisonnement graphe pour agents, +2 015 ★), cloudflare/security-audit-skill (+2 548 ★), mattpocock/skills (+2 070 ★), google/skills (+534 ★).

## 📊 Résumé
- **Top 3 du jour** : 1) GPT-6 Cyber (premier « Critical » d'OpenAI) ; 2) Meta rachète Conductor (orchestration d'agents de code) ; 3) Gemini Omni 1.2 Flash GA (vidéo 15 s, −30 %).
- **À tester en priorité** : Gemini Omni 1.2 Flash, voice remixing Gemini 3.8 TTS, Phonon (open source), skills Cloudflare/Google/mattpocock pour agents de code, Conductor avant le 20 nov.
