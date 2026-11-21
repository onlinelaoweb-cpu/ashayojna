# Auto real photos for khabar posts that have none yet. Runs in GitHub Actions (needs UNSPLASH_KEY; the dev sandbox cannot reach Unsplash).
# For every news item without photos/<slug>.jpg: search Unsplash (landscape, India-flavoured query), download, record credit in photos/credits.json.
# Then tools/apply_photos.py crops all photos/*.jpg to img/news-<slug>-{hi,en}.jpg. No photo found -> the emoji scene image stays (safe fallback).
import os, re, json, sys, urllib.request, urllib.parse
sys.path.insert(0, os.getcwd())
KEY = os.environ.get("UNSPLASH_KEY", "")
# topic words (in the English title/summary/related slug) -> search phrase. First match wins; always suffixed with "india".
TOPICS = [
 (r"pension|elderly|senior|jeevan pramaan|life certificate", "elderly indian man village"),
 (r"farm|kisan|crop|pmfby|fasal|paddy|wheat|rabi|kharif", "indian farmer field"),
 (r"solar|surya|rooftop|electricity|power", "solar panels rooftop india"),
 (r"hospital|health|ayushman|pm-jay|medical", "indian hospital patient"),
 (r"scholarship|student|school|education|exam", "indian school students"),
 (r"loan|mudra|stand-up|startup|msme|business|entrepreneur", "indian small business owner"),
 (r"women|mahila|ladli|girl|beti|matru|maternity", "indian woman village"),
 (r"ration|food|anna|nfsa|gas|lpg|ujjwala", "indian ration shop"),
 (r"housing|awas|house|gramin", "indian village house"),
 (r"bank|aadhaar|dbt|kyc|ekyc|account|upi", "indian woman smartphone bank"),
 (r"job|employment|rozgar|skill|training|mgnrega|nrega", "indian workers"),
]
def query_for(n):
    text = " ".join([n.get("slug", ""), n.get("related", ""), n["en"]["title"], n["en"].get("summary", "")]).lower()
    for pat, q in TOPICS:
        if re.search(pat, text): return q + " india" if "india" not in q else q
    return "india village people"
def api(path, **params):
    params["client_id"] = KEY
    req = urllib.request.Request("https://api.unsplash.com" + path + "?" + urllib.parse.urlencode(params), headers={"Accept-Version": "v1"})
    return json.load(urllib.request.urlopen(req, timeout=30))
def pick(results):
    for r in results:
        if r.get("width", 0) >= 2000 and r["width"] > r["height"] * 1.3:
            if r.get("premium") or r.get("plus"): continue
            return r
def fetch(n):
    q = query_for(n)
    res = api("/search/photos", query=q, orientation="landscape", per_page=15, content_filter="high").get("results", [])
    r = pick(res)
    if not r: return None
    url = r["urls"]["raw"] + ("&" if "?" in r["urls"]["raw"] else "?") + "w=1800&fit=max&q=80&fm=jpg"
    data = urllib.request.urlopen(urllib.request.Request(url), timeout=60).read()
    try: api(urllib.parse.urlparse(r["links"]["download_location"]).path)  # required by Unsplash API terms: count the download
    except Exception: pass
    open(f"photos/{n['slug']}.jpg", "wb").write(data)
    return {"name": r["user"]["name"], "link": r["user"]["links"]["html"], "id": r["id"], "query": q}
def main():
    if not KEY: print("UNSPLASH_KEY missing"); return 0
    import news
    cp = "photos/credits.json"
    cred = json.load(open(cp, encoding="utf-8")) if os.path.exists(cp) else {}
    os.makedirs("photos", exist_ok=True); got = 0
    for n in news.NEWS:
        if os.path.exists(f"photos/{n['slug']}.jpg"): continue
        try: c = fetch(n)
        except Exception as ex: print("FAIL", n["slug"], ex); continue
        if c: cred[n["slug"]] = c; got += 1; print("OK", n["slug"], "<-", c["query"], c["name"])
        else: print("no photo", n["slug"])
    json.dump(cred, open(cp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("new photos:", got)
if __name__ == "__main__": main()
