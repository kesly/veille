# AI Watch — 2026-11-12 Matin

> Collecte : treg 4/4 sources, 15 recherches extended, GitHub Trending ok, 4 pages lues (Google blog, TechCrunch, GitHub n8n/nod, 9to5Mac), 6 items confirmés par une deuxième source.

## 🔥 Breaking

### Anthropic lance son IPO roadshow ($70–78/action)
- **Quoi** : Anthropic ouvre le roadshow de son introduction en bourse (Nasdaq « ANT »), 825 M d'actions Class A, jusqu'à ~64,4 Md$ levés ; pricing prévu le 18/11, cotation le 19/11.
- **Date** : 2026-11-10
- **Lien** : https://www.anthropic.com/news/roadshow-launch ; https://fortune.com/2026/11/10/anthropic-ipo-price-range-ai-stock-sell-off/
- **Pourquoi c'est important** : plus grosse IPO IA à ce jour ; valorisation citée jusqu'à 1,4 T$ (base diluée, méthodes divergentes selon les sources).
- **Testable** : Non

### Google Gemini Decisions API (modèle Gemini Decision 1)
- **Quoi** : endpoint qui ne génère pas de texte mais évalue jusqu'à 1 000 questions fermées (oui/non, choix, rubrique) en une passe sur texte, image, audio, vidéo, PDF ; ~0,10 $/M tokens en entrée, sortie gratuite (chiffres de la presse, à vérifier dans la doc).
- **Date** : 2026-11-11
- **Lien** : https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
- **Pourquoi c'est important** : routage, modération, évaluation (LLM-judge) à coût très bas ; nouveau type d'API. Payant (très bas prix).
- **Testable** : Oui — clé API dans Google AI Studio.

### Google Gemini 4 Carbon en disponibilité générale
- **Quoi** : Gemini 4 Carbon ouvert aux développeurs/entreprises/grand public ; 2 $/M entrée, 10 $/M sortie jusqu'au 30/11 (puis ~4 $ d'après un média).
- **Date** : 2026-11-10
- **Lien** : https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
- **Pourquoi c'est important** : concurrent direct de Claude Fable 5.2 / Opus 5.5 avec un prix d'appel agressif.
- **Testable** : Oui — AI Studio, Antigravity, app Gemini (Ultra).

### Anthropic : Claude Meetings, Whiteboards, Sheets
- **Quoi** : Claude rejoint les visioconférences (Google Meet au lancement) et rédige plans/timelines en direct ; bêta Team et Enterprise.
- **Date** : 2026-11-10
- **Lien** : https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/
- **Pourquoi c'est important** : course aux « suites bureautiques IA » (OpenAI, Meta, Anthropic) contre Microsoft/Google. Payant.
- **Testable** : Oui sur plans Team/Enterprise.

## 🆕 Nouveaux Outils & Produits

### Nod par n8n Labs
- **Quoi** : agent personnel open source (Apache 2.0) avec son propre ordinateur/navigateur, local, demande avant d'agir ; macOS 14+, Windows 11 en preview ; modèle au choix.
- **Date** : 2026-11-10
- **Lien** : https://github.com/n8n-io/nod
- **Pourquoi c'est important** : agent « computer-use » local, gratuit, 259 votes PH. Recherche preview, partage de données d'usage activé par défaut.
- **Testable** : Oui — DMG sur GitHub.

### ElevenLabs Scribe v3 / v3 Live (Voice AI)
- **Quoi** : STT avec 27 % d'erreurs en moins (WER 16,94 → 12,38 % sur FLEURS selon ElevenLabs), diarisation jusqu'à 32 locuteurs ; v3 Live ~150 ms de latence.
- **Date** : 2026-11-10
- **Lien** : https://elevenlabs.io/blog/scribe-v3
- **Pourquoi c'est important** : nouvelle référence STT revendiquée (benchmarks du vendeur). Payant.
- **Testable** : Oui — API/app ElevenLabs.

### Earlybird (open source STT, 29M paramètres)
- **Quoi** : STT streaming minuscule qui émet les mots avant la fin de leur prononciation.
- **Date** : 2026-11-11 (Product Hunt)
- **Lien** : https://www.producthunt.com/products/earlybird-5
- **Pourquoi c'est important** : voix on-device très faible latence. Non confirmé par seconde source.
- **Testable** : Oui (voir PH).

### Autres lancements notables (PH / HN)
- **Skillbox** (bibliothèque de skills synchronisée entre agents), **CALL-E** et **Mitra MCP** (téléphonie pour agents), **Relay** : https://www.producthunt.com/products/skillbox-5
- **Pomerado** (YC F26, site web → MCP) : https://news.ycombinator.com/item?id=50455811
- **Yogurt** (alternative open source à Granola) : https://github.com/FrigadeHQ/yogurt
- **Atuin Threads** (sessions d'agents sur toutes les machines) : https://blog.atuin.sh/threads-agent-sessions/
- **Pourquoi c'est important** : l'écosystème « outillage d'agents » se densifie (téléphonie, skills, MCP). Testable : Oui (liens).

## 🧠 Mises à jour de Modèles

### Meta Muse Ember 1.0
- **Quoi** : plus petit modèle de la famille Muse, contexte 1M, multimodal ; 0,10 $/M entrée, 0,50 $/M sortie ; non open-weight (API Meta).
- **Date** : 2026-11-09/10 (sources divergentes)
- **Lien** : https://dev.meta.ai/docs/muse-ember
- **Pourquoi c'est important** : cible les tâches d'agents à gros volume ; Meta dit battre Claude Haiku 5.5 (benchmarks internes).
- **Testable** : Oui — Meta Model API.

### MiniMax H3-Image (open weights) et Seedream 5.5 (ByteDance)
- **Quoi** : H3-Image : 4K/16 MP en ~10–20 s, 16 images de référence ; poids sur Hugging Face, licence excluant US/UE/UK. Seedream 5.5 : édition 100 tours, décomposition en jusqu'à 99 calques.
- **Date** : 2026-11-10 (H3) / 2026-11-09 (Seedream)
- **Lien** : https://www.producthunt.com/products/minimax ; https://www.producthunt.com/products/seedream-4-0
- **Pourquoi c'est important** : génération d'images de haute résolution rapide, partiellement open source.
- **Testable** : Oui — API (≈0,02–0,07 $/image selon agrégateurs).

### Claude Fable 5.2 / Mythos 5.2 (Anthropic)
- **Quoi** : Fable 5.2 modèle par défaut de Claude Code ; Mythos 5.2 restreint aux organisations vérifiées.
- **Date** : 2026-11-09 (plus de 72 h pour certains détails, rappel contextuel)
- **Lien** : https://platform.claude.com/docs/en/release-notes/overview
- **Pourquoi c'est important** : r/ClaudeAI surveille déjà d'éventuels « nerfs ».
- **Testable** : Oui.

## 🔬 Research
- **Apple ML — Faster Retrieval for Better, More Efficient RAG** : https://machinelearning.apple.com/research/faster-retrieval (HN 174 pts). Non détaillé ici.
- RAS pour le reste de notable confirmé.

## 📝 À surveiller
- **Apple « Harbor »** : app Mac non sortie (fuite d'Aaron Perris) : serveur d'inférence privé, cluster de Macs en Thunderbolt 5. Calendrier incertain. https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/
- **United Airlines interdit les agents IA pour réserver des vols** (HN 454 pts) : https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/
- **Nvidia / Jensen Huang** : enquête rapportée (WSJ, NYT), non lié techniquement mais impact marché.
- **OpenAI** : chiffre d'affaires T3 ~10 Md$ (digests, source primaire non trouvée) ; ChatGPT Advanced/Standard Voice retirés le 11/12 au profit de GPT-Live ; rachat d'Odessia.
- **Huawei MACaQ** (quantizer local, open source) : https://github.com/huawei-csl/MACaQ
- **Open source self driving** (r/LocalLLaMA, 439 pts) : https://www.reddit.com/r/LocalLLaMA/comments/1xtmeif/
- **GitHub Trending** : meta/astryx, addyosmani/agent-skills, vercel-labs/agent-browser, shadcn/improve, homeassistant-ai/ha-mcp, openai/codex-security.

## 📊 Résumé
- **Top 3 du jour** : 1) Anthropic IPO roadshow ; 2) Gemini Decisions API + Gemini 4 Carbon GA ; 3) Nod (n8n) + Claude Meetings.
- **À tester en priorité** : Gemini Decisions API (AI Studio), Nod (open source), Scribe v3, MiniMax H3-Image, Muse Ember API.
