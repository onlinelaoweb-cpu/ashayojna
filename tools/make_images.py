# Generates 1200x630 share/Discover images: img/<slug>-<lang>.jpg (run from repo root: python3 tools/make_images.py)
import os, sys, html
sys.path.insert(0, ".")
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build
from data1 import Y, CATS
from en6 import EN
from playwright.sync_api import sync_playwright
os.makedirs("img", exist_ok=True)
F = os.path.abspath("fonts")
CSS = f"""@font-face{{font-family:N;font-weight:700;src:url(file://{F}/noto-sans-devanagari-devanagari-700-normal.woff2);unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}}
@font-face{{font-family:N;font-weight:700;src:url(file://{F}/noto-sans-devanagari-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122}}
*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:630px;background:linear-gradient(135deg,#0f5a4a,#17896f);font-family:N,'Noto Color Emoji',sans-serif;color:#fff;padding:60px 70px;display:flex;flex-direction:column;justify-content:space-between}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:34px}}.chip{{background:rgba(255,255,255,.18);padding:8px 24px;border-radius:40px}}
.ic{{font-size:110px;line-height:1}}h1{{font-size:{{fs}}px;line-height:1.25;font-weight:700}}
.bot{{display:flex;justify-content:space-between;font-size:34px;opacity:.95}}"""
def sp(t): return ''.join(f'<span style="margin-right:.25em;display:inline-block">{html.escape(w)}</span>' for w in t.split(' '))
def card(icon, name, cat, site, tag, fs):
    return f"<html><head><meta charset=utf-8><style>{CSS.replace('{fs}',str(fs))}</style></head><body><div class=top><span class=chip>{sp(cat)}</span><span class=ic>{icon}</span></div><h1>{sp(name)}</h1><div class=bot><span>{sp(site)}</span><span>{html.escape(tag)}</span></div></body></html>"
CATEN = build.CATS_EN
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1200,"height":630})
    n = 0
    for y in Y:
        for lang in ("hi","en"):
            name = y["name"] if lang=="hi" else EN[y["slug"]]["name"]
            cat = CATS[y["cat"]][0] if lang=="hi" else CATEN[y["cat"]][0]
            tag = "ashayojana.com"
            site = "आशा योजना" if lang=="hi" else "Asha Yojana"
            fs = 64 if len(name) < 45 else 52
            pg.set_content(card(y.get("icon","📄"), name, cat, site, tag, fs)); pg.wait_for_timeout(60)
            pg.screenshot(path=f"img/{y['slug']}-{lang}.jpg", type="jpeg", quality=82); n += 1
    import news
    for n in news.NEWS:
        for lang in ("hi","en"):
            d = n[lang]; nm = d["title"]
            cat = "ताज़ा खबर" if lang=="hi" else "Latest update"
            site = "आशा योजना" if lang=="hi" else "Asha Yojana"
            fs = 64 if len(nm) < 45 else 52
            pg.set_content(card(n["icon"], nm, cat, site, n["date"], fs)); pg.wait_for_timeout(60)
            pg.screenshot(path=f"img/news-{n['slug']}-{lang}.jpg", type="jpeg", quality=82); n_ = 0
    b.close()
print("images", n)
