# Writes PUSH_TODAY.md: ready-to-paste OneSignal push drafts for the newest khabar posts.
# Run from repo root: python3 tools/push_draft.py
import sys, io, contextlib
sys.path.insert(0, ".")
import news
def cut(s, n):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n-1].rsplit(" ", 1)[0] + "…"
items = sorted(news.NEWS, key=lambda n: n["date"], reverse=True)
latest = items[0]["date"]
out = [f"# Push drafts (khabar dated {latest})", "",
       "OneSignal dashboard > Messages > Push > New push > Audience: Subscribed Users. Max 1-2 pushes per day.", ""]
for n in [x for x in items if x["date"] == latest][:2]:
    h = n["hi"]
    out += [f"## {n['icon']} {n['slug']}", f"- Title: {cut(h['title'], 60)}", f"- Message: {cut(h['summary'], 110)}",
            f"- Launch URL: https://ashayojana.com/khabar/{n['slug']}.html", ""]
open("PUSH_TODAY.md", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out))
