import glob, json, os, re, subprocess, sys, time, urllib.parse
from collections import Counter
from datetime import datetime, timedelta, timezone

TOKEN = os.environ.get("TREG_TOKEN", "")
NOW = datetime.now(timezone.utc)
CHART_POST = "dataforseo.x.app-data-apple-app-list-task-post"
CHART_GET = "dataforseo.x.app-data-apple-app-list-task-get-advanced"
APP_DETAIL = "crawl4ai.app-store.app.detail"
APP_REVIEWS = "litescrape.app_store.reviews"
META_ADS = "crawl4ai.meta-ads.library.advertiser"
META_SEARCH = "scrapecreators.x.v1-facebook-adlibrary-search-companies"
CHARTS = ["", "productivity", "utilities", "lifestyle", "health_and_fitness", "education"]
NICHES = ["finance", "food_and_drink", "shopping", "medical", "business", "photo_and_video",
          "entertainment", "travel", "sports", "reference", "social_networking", "music"]
DEMAND = "dataforseo.google.keywords.volume"
STORE_SEARCH = "crawl4ai.app-store.search.apps"
TREG_FALLBACK_MAX = 8
fallbacks = [0]
DEMAND_CACHE = "market-scan/data/demand.tsv"
MODES = {
    "market": dict(days=7, likes=5,
        x=["launched my app MRR", "crossed MRR app revenue", "app hit $10k MRR", "buildinpublic revenue app", "my app makes per month subscribers"],
        reddit=["SideProject", "SaaS", "indiehackers", "microsaas"]),
    "ai": dict(days=3, likes=50,
        x=["new AI model released", "open source AI launch", "voice AI launch", "AI coding agent launch"],
        reddit=["LocalLLaMA", "ClaudeAI", "OpenAI", "MachineLearning"]),
}


def call(endpoint, body=None, query=None):
    url = "https://treg.to/call/" + endpoint
    if query:
        url += "?" + urllib.parse.urlencode(query)
    cmd = ["curl", "-sS", "-m", "90", "-w", "\n%{http_code}"]
    if TOKEN:
        cmd += ["-H", "X-Treg-Token: " + TOKEN]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    done = subprocess.run(cmd + [url], capture_output=True, text=True)
    text, _, status = done.stdout.rpartition("\n")
    if done.returncode or status != "200":
        raise RuntimeError(f"{endpoint}: HTTP {status or '000'} {done.stderr.strip()[:120]}")
    return json.loads(text)


def apple(url):
    done = subprocess.run(["curl", "-sS", "-m", "30", "-A", "Mozilla/5.0", "-w", "\n%{http_code}", url], capture_output=True, text=True)
    text, _, status = done.stdout.rpartition("\n")
    if done.returncode or status != "200":
        raise RuntimeError(f"apple: HTTP {status or '000'} {done.stderr.strip()[:80]}")
    return json.loads(text)


def store_search(term, country):
    try:
        rows = apple("https://itunes.apple.com/search?" + urllib.parse.urlencode(
            {"term": term, "entity": "software", "country": country, "limit": 10}))["results"]
        time.sleep(1)
        return "apple", [dict(app_id=str(r["trackId"]), name=r["trackName"], rating_count=r.get("userRatingCount") or 0,
                              rating=r.get("averageUserRating") or 0, released_at=r.get("releaseDate"),
                              version_released_at=r.get("currentVersionReleaseDate"),
                              url=(r.get("trackViewUrl") or "").split("?")[0]) for r in rows]
    except Exception as error:
        if fallbacks[0] >= TREG_FALLBACK_MAX:
            raise RuntimeError(f"Apple injoignable ({str(error)[:60]}), secours treg épuisé")
        fallbacks[0] += 1
        rows = call(STORE_SEARCH, {"query": term, "country": country, "limit": 10}).get("rows") or []
        return "treg", [dict(app_id=str(r["app_id"]), name=r["name"], rating_count=r.get("rating_count") or 0,
                             rating=r.get("rating") or 0, released_at=r.get("released_at"),
                             version_released_at=r.get("version_released_at"), url=r.get("url")) for r in rows]


def grossing_index(folder, days=14):
    limit = str(NOW.date() - timedelta(days=days))
    best = {}
    for path in glob.glob(folder + "/*.tsv"):
        day = os.path.basename(path)[:10]
        if day < limit:
            continue
        for line in open(path):
            cat, rank, app, *_ = line.rstrip("\n").split("\t")
            if app not in best or int(rank) < best[app][0]:
                best[app] = (int(rank), cat, day)
    return best


def clip(text, size=260):
    return " ".join((text or "").split())[:size]


def days_since(stamp):
    return (NOW - datetime.fromisoformat(stamp.replace("Z", "+00:00"))).days


def age(stamp):
    return f"{stamp[:10]} ({days_since(stamp)} j)" if stamp else "?"


def app_detail(app_id):
    rows = call(APP_DETAIL, {"app": str(app_id), "country": "us"}).get("rows") or []
    return rows[0] if rows else {}


def hacker_news():
    print("\n## Hacker News, front page")
    for r in call("crawl4ai.hackernews.stories.front", {"limit": 60})["rows"][:40]:
        print(f"- {r.get('score')} pts, {r.get('comments')} comm. | {r.get('title')} | {r.get('url')}")


def product_hunt():
    print("\n## Product Hunt, lancements du jour")
    for r in call("crawl4ai.producthunt.launches.today", {"limit": 30})["rows"]:
        print(f"- {r.get('votes')} votes | {r.get('name')} ({r.get('topic')}) | {clip(r.get('tagline'), 120)} | {r.get('url')}")


def x_posts(queries, days, likes):
    print(f"\n## X, {days} derniers jours, {likes}+ likes")
    seen, kept = set(), []
    limit = (NOW - timedelta(days=days)).timestamp()
    for q in queries:
        for p in call("treg.x.search.posts", {"q": q})["output"]["posts"]:
            if p["id"] in seen or p.get("isReply") or p["createdUtc"] < limit or p["likeCount"] < likes:
                continue
            seen.add(p["id"])
            kept.append(p)
    for p in sorted(kept, key=lambda p: -p["likeCount"])[:25]:
        day = datetime.fromtimestamp(p["createdUtc"], timezone.utc).date()
        print(f"- {day} | {p['likeCount']} likes, {p['authorFollowers']} abonnés | {clip(p['text'])} | https://x.com/{p['authorUsername']}/status/{p['id']}")


def reddit(subs, days):
    print(f"\n## Reddit, {days} derniers jours")
    limit = NOW - timedelta(days=days)
    for sub in subs:
        rows = []
        for e in call("treg.reddit.subreddit.posts", {"subreddit": sub})["output"]["posts"]:
            node = e.get("node") or {}
            cells = {c.get("__typename"): c for c in node.get("cells") or []}
            meta, title, action = cells.get("MetadataCell"), cells.get("TitleCell"), cells.get("ActionCell")
            if not (meta and title and action and meta.get("createdAt")):
                continue
            if datetime.strptime(meta["createdAt"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc) < limit:
                continue
            rows.append((action.get("score") or 0, action.get("commentCount") or 0, title["title"], node["groupId"][3:]))
        print(f"### r/{sub}")
        for score, comments, title, post in sorted(rows, key=lambda r: -r[0])[:8]:
            print(f"- {score} pts, {comments} comm. | {clip(title, 140)} | https://www.reddit.com/r/{sub}/comments/{post}/")


def reference(days, min_age):
    limit = str(NOW.date() - timedelta(days=min_age))
    older = [d for d in sorted(days) if d <= limit]
    return older[-1] if older else (min(days) if days else None)


def stars(i):
    value = (i.get("rating") or {}).get("value")
    return f"{value:.1f}★" if value else "?★"


def charts(folder):
    cats = CHARTS + NICHES[NOW.toordinal() % 3::3]
    print("\n## App Store US, top grossing (un rang, pas un revenu)")
    print("Catégories du jour : " + ", ".join(c or "all" for c in cats) + ". Les niches tournent : chacune revient tous les 3 jours.")
    body = [dict({"app_collection": "top_grossing_ios", "location_code": 2840, "language_code": "en", "depth": 100},
                 **({"app_category": c} if c else {})) for c in cats]
    tasks = {}
    for cat, task in zip(cats, call(CHART_POST, body)["tasks"]):
        if task.get("status_code") == 20100:
            tasks[cat or "all"] = task["id"]
        else:
            print(f"### {cat}: refusé ({task.get('status_message')})")
    os.makedirs(folder, exist_ok=True)
    today = f"{folder}/{NOW.date()}.tsv"
    history, notes, current = {}, {}, {}
    for path in sorted(glob.glob(folder + "/*.tsv")):
        if path == today:
            continue
        for line in open(path):
            cat, rank, app, _title, count, *_ = line.rstrip("\n").split("\t")
            day = os.path.basename(path)[:10]
            history.setdefault(cat, {}).setdefault(day, {})[app] = int(rank)
            if count.isdigit():
                notes.setdefault(app, {})[day] = int(count)
    out, picks, momentum = [], [], []
    for cat, task in tasks.items():
        result = None
        for attempt in range(6):
            result = call(CHART_GET, query={"id": task})["tasks"][0].get("result")
            if result:
                break
            time.sleep(20)
        if not result:
            print(f"### {cat}: résultat non prêt")
            continue
        items = result[0]["items"]
        for i in items:
            if i.get("reviews_count") and str(i["app_id"]) not in current:
                current[str(i["app_id"])] = (i["title"], cat, i["rank_absolute"], i["reviews_count"])
            out.append(f"{cat}\t{i['rank_absolute']}\t{i['app_id']}\t{i['title']}\t{i.get('reviews_count')}\t{(i.get('rating') or {}).get('value')}")
        small = [i for i in items if (i.get("reviews_count") or 0) < 100000][:12]
        days = history.get(cat, {})
        last, week = reference(days, 1), reference(days, 7)
        moves = []
        if last:
            for i in items:
                before = days[last].get(str(i["app_id"]))
                if before is None or before - i["rank_absolute"] >= 10:
                    moves.append(f"{i['title']} ({'nouveau' if before is None else before}→{i['rank_absolute']})")
                    picks.append((0 if cat == "all" else 1, cat, i))
        if week and cat != "all":
            gained = [(days[week].get(str(i["app_id"])), i) for i in items]
            gained = [(b, i) for b, i in gained if b is None or b - i["rank_absolute"] >= 15]
            momentum.append((len(gained), cat, week, gained))
        if cat != "all":
            picks += [(2, cat, i) for i in small]
        print(f"### {cat}")
        print("Moins de 100k avis : " + "; ".join(f"#{i['rank_absolute']} {i['title']} ({i.get('reviews_count')} avis, {stars(i)}) {i.get('url')}" for i in small))
        print(f"Mouvements vs {last} : " + ("; ".join(moves[:15]) or "aucun") if last else "Premier relevé de cette catégorie : pas encore de comparaison.")
    with open(today, "w") as f:
        f.write("\n".join(out) + "\n")
    print("\n### Où l'argent bouge (entrées dans le top 100 et montées de 15 places ou plus, sur environ 7 jours)")
    for count, cat, week, gained in sorted(momentum, key=lambda m: -m[0]):
        shown = "; ".join(f"{i['title']} ({'nouveau' if b is None else b}→#{i['rank_absolute']}, {i.get('reviews_count')} avis, {stars(i)})"
                          for b, i in sorted(gained, key=lambda g: g[1]["rank_absolute"])[:8])
        print(f"- {cat} (vs {week}, {(NOW.date() - datetime.fromisoformat(week).date()).days} j) : {count} apps | {shown or '—'}")
    ref = reference({d for s in notes.values() for d in s}, 7)
    if ref:
        span = max(1, (NOW.date() - datetime.fromisoformat(ref).date()).days)
        speed = [((count - notes[app][ref]) / span, title, cat, rank, notes[app][ref], count)
                 for app, (title, cat, rank, count) in current.items()
                 if count < 100000 and notes.get(app, {}).get(ref) and count > notes[app][ref]]
        print(f"\n### Vitesse des notes vs {ref} ({span} j), apps à moins de 100k notes : beaucoup de notes par jour = beaucoup de nouveaux utilisateurs")
        for v, title, cat, rank, before, count in sorted(speed, reverse=True)[:12]:
            print(f"- {title} ({cat} #{rank}) : +{v:.0f} notes/j ({before}→{count})")
    print("\n### Âge des apps à surveiller (catégories de niche, les moins d'avis d'abord : bien classée avec peu d'avis = souvent jeune)")
    seen = set()
    picks = [p for p in picks if p[1] != "all" and (p[2].get("reviews_count") or 0) < 100000]
    for _, cat, i in sorted(picks, key=lambda p: (p[2].get("reviews_count") or 0, p[0])):
        if i["app_id"] in seen or len(seen) >= 8:
            continue
        seen.add(i["app_id"])
        try:
            d = app_detail(i["app_id"])
        except Exception as error:
            print(f"- {i['title']} : TREG_ERREUR {str(error)[:120]}")
            continue
        print(f"- #{i['rank_absolute']} {cat} | {i['title']} ({d.get('developer')}) | sortie {age(d.get('released_at'))} | dernière MAJ {age(d.get('version_released_at'))} | {d.get('rating')}★ sur {d.get('rating_count')} | {d.get('category')} | {i.get('url')}")


def meta_page(names):
    seen = []
    for name in names:
        found = call(META_SEARCH, query={"query": name}).get("searchResults") or []
        seen += [f"{p.get('name')} ({p.get('category')})" for p in found[:3]]
        apps = [p for p in found if re.search(r"\bApp\b|Software|Product/service", p.get("category") or "")
                and (p.get("name") or "").lower().startswith(name.lower()) and str(p.get("page_is_deleted")) != "True"]
        if apps:
            return max(apps, key=lambda p: int(p.get("likes") or 0)), seen
    return None, seen


def app_report(target):
    found = re.search(r"(\d{6,})", target)
    if not found:
        return print(f"APP_INTROUVABLE: donne une URL App Store ou un id numérique, pas « {target} »")
    app_id = found.group(1)
    d = app_detail(app_id)
    print(f"# {d.get('name')} ({d.get('developer')}) {d.get('url')}")
    print(f"Sortie {age(d.get('released_at'))} · dernière MAJ {age(d.get('version_released_at'))} · {d.get('rating')}★ sur {d.get('rating_count')} notes · prix {d.get('price')} {d.get('currency')} · {d.get('category')}")
    print("Notes de version : " + clip(d.get("release_notes"), 300))
    print("Description : " + clip(d.get("description"), 600))
    reviews = []
    try:
        for page in (1, 2, 3, 4):
            entries = apple(f"https://itunes.apple.com/us/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json")["feed"].get("entry") or []
            reviews += [dict(rating=int(e["im:rating"]["label"]), review_date=e.get("updated", {}).get("label", "")[:10],
                             title=e["title"]["label"], text=e["content"]["label"]) for e in entries if "im:rating" in e]
            if len(entries) < 50:
                break
    except Exception as error:
        print(f"AVIS_APPLE_INDISPONIBLE ({str(error)[:80]})")
    source = "apple"
    if not reviews:
        source = "litescrape (flux Apple vide)"
        for page in (1, 2, 3, 4):
            try:
                batch = call(APP_REVIEWS, query={"product_id": app_id, "country": "us", "page": page}).get("reviews") or []
            except Exception as error:
                print(f"AVIS_ERREUR: {str(error)[:150]}")
                break
            reviews += batch
            if len(batch) < 25:
                break
    notes = Counter(r.get("rating") for r in reviews)
    print(f"\n## {len(reviews)} avis US récents (source {source}), notes : " + ", ".join(f"{n}★ {notes[n]}" for n in (5, 4, 3, 2, 1)))
    for r in sorted(reviews, key=lambda r: r.get("rating") or 5)[:30]:
        print(f"- {r.get('rating')}★ {r.get('review_date')} | {clip(r.get('title'), 80)} : {clip(r.get('text'), 220)}")
    short = re.split(r"\s[-–|:]\s|:\s", d.get("name") or "")[0]
    page, seen = meta_page(dict.fromkeys(n for n in (short, d.get("name")) if n))
    if not page:
        return print("\n## Pubs Meta : aucune page d'app sûre trouvée, donc aucune pub comptée. Pages écartées : " + clip("; ".join(seen), 300))
    result = call(META_ADS, {"page": page["page_id"], "active_status": "active", "country": "ALL", "limit": 30})
    ads = result.get("rows") or []
    week = [a for a in ads if a.get("start_date") and days_since(a["start_date"]) <= 7]
    print(f"\n## Pubs Meta actives : {len(ads)} (plafond 30), dont {len(week)} lancées depuis 7 jours")
    print(f"Page : « {page.get('name')} » ({page.get('category')}, {page.get('likes')} likes, Instagram @{page.get('ig_username')}). Vérifie que c'est bien celle de l'app.")
    hooks = Counter(clip(a.get("body") or a.get("title"), 180) for a in ads)
    formats = Counter(a.get("display_format") for a in ads)
    print("Formats : " + ", ".join(f"{k} {v}" for k, v in formats.most_common()))
    for hook, count in hooks.most_common(5):
        print(f"- ×{count} | {hook}")


def demand_report(arg):
    words = list(dict.fromkeys(w.strip().lower() for w in arg.split(",") if w.strip()))[:60]
    cache = {}
    if os.path.exists(DEMAND_CACHE):
        for line in open(DEMAND_CACHE):
            word, day, *rest = line.rstrip("\n").split("\t")
            cache[word] = [day] + rest
    fresh = str(NOW.date() - timedelta(days=30))
    missing = [w for w in words if w not in cache or cache[w][0] < fresh]
    if missing:
        rows = call(DEMAND, [{"keywords": missing, "location_code": 2840, "language_code": "en"}])["tasks"][0].get("result") or []
        for r in rows:
            series = " ".join(str(m.get("search_volume") or 0) for m in reversed(r.get("monthly_searches") or []))
            cache[r["keyword"]] = [str(NOW.date()), str(r.get("search_volume") or 0), str(r.get("cpc") or 0), str(r.get("competition") or "?"), series]
        os.makedirs(os.path.dirname(DEMAND_CACHE), exist_ok=True)
        with open(DEMAND_CACHE, "w") as f:
            f.write("".join(f"{w}\t" + "\t".join(v) + "\n" for w, v in sorted(cache.items())))
    print(f"## Demande Google US ({len(missing)} mots-clés payés, {len(words) - len(missing)} repris du cache)")
    print("mot-clé | volume/mois | CPC $ | concurrence | 12 mois, du plus ancien au plus récent")
    for w in words:
        if w in cache:
            _, volume, cpc, competition, series = cache[w]
            print(f"- {w} | {volume} | {cpc} | {competition} | {series}")
        else:
            print(f"- {w} | pas de donnée")


def keywords_report(arg):
    terms = list(dict.fromkeys(t.strip().lower() for t in arg.split(",") if t.strip()))[:24]
    grossing = grossing_index("market-scan/data/top-grossing")
    volumes = {}
    if os.path.exists(DEMAND_CACHE):
        for line in open(DEMAND_CACHE):
            word, _day, volume, *_ = line.rstrip("\n").split("\t")
            volumes[word] = int(volume or 0)
    print("## Tests App Store : top 10 réel de chaque recherche")
    print("Prenable = moins de 1 000 notes ou pas de mise à jour depuis 180 j. Argent = une petite app (moins de 10 000 notes) vue dans le top grossing US des 14 derniers jours,"
          " ou seulement des gros acteurs si la recherche est facile (5 places prenables ou plus).")
    for term in terms:
        country, _, word = term.rpartition(":")
        country = country or "us"
        try:
            source, rows = store_search(word, country)
        except Exception as error:
            print(f"\n### « {word} » ({country}) : TREG_ERREUR {str(error)[:120]}")
            continue
        rows = rows[:10]
        open_slots, strong, earners, small = 10 - len(rows), 0, [], False
        print(f"\n### « {word} » ({country.upper()}, source {source})")
        for n, r in enumerate(rows, 1):
            upd = days_since(r["version_released_at"]) if r.get("version_released_at") else None
            weak = r["rating_count"] < 1000 or (upd or 0) > 180
            open_slots += weak
            strong += r["rating_count"] >= 1000
            g = grossing.get(r["app_id"])
            if g:
                is_small = r["rating_count"] < 10000
                small = small or is_small
                earners.append(f"{r['name'][:30]} (#{g[0]} {g[1]}, {r['rating_count']} notes, {'petite app' if is_small else 'gros acteur'})")
            print(f"{n}. {r['name'][:45]} | {r['rating_count']} notes, {r['rating']:.1f}★ | sortie {age(r.get('released_at'))} | MAJ il y a {upd} j | {r['url']}"
                  + (" | PRENABLE" if weak else "") + (f" | 💰 top grossing #{g[0]} {g[1]} le {g[2]}" if g else ""))
        volume = volumes.get(word) if country == "us" else None
        demand = volume >= 1000 if volume is not None else strong >= 3
        basis = f"{volume} recherches Google/mois" if volume is not None else f"{strong} apps à 1 000 notes ou plus"
        money = small or (bool(earners) and open_slots >= 5)
        tests = [demand, open_slots >= 3, money]
        verdict = {3: "BUILD", 2: "À CREUSER"}.get(sum(tests), "ÉCARTÉ")
        print(f"→ Demande {'✅' if tests[0] else '❌'} ({basis}) · Classable {'✅' if tests[1] else '❌'} ({open_slots}/10 prenables) · "
              f"Argent {'✅' if tests[2] else '❌'} ({'; '.join(earners) or 'aucune app du top grossing'}) · VERDICT {verdict}")


def read_page(url):
    pages = call("treg.web.extract", {"url": url})["output"]["pages"]
    print(clip(pages[0].get("markdown") or pages[0].get("content") or json.dumps(pages[0]), 6000) if pages else "PAGE_VIDE")


def main():
    mode = sys.argv[1]
    if mode in ("read", "app", "demand", "keywords"):
        try:
            return {"read": read_page, "app": app_report, "demand": demand_report, "keywords": keywords_report}[mode](sys.argv[2])
        except Exception as error:
            return print(f"TREG_ERREUR: {str(error)[:200]}")
    conf = MODES[mode]
    print(f"# Collecte treg ({mode}), {NOW.isoformat(timespec='minutes')}")
    steps = [hacker_news, product_hunt, lambda: x_posts(conf["x"], conf["days"], conf["likes"]), lambda: reddit(conf["reddit"], conf["days"])]
    if mode == "market":
        steps.append(lambda: charts(sys.argv[2]))
    failures = 0
    for step in steps:
        try:
            step()
        except Exception as error:
            failures += 1
            print(f"\nTREG_ERREUR: {str(error)[:200]}")
    print(f"\nTREG_BILAN: {len(steps) - failures}/{len(steps)} sources ok")


main()
