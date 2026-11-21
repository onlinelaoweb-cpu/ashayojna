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

# ---- topic scene images for Taaza Khabar (no headline text; the headline is on the page) ----
SCENE_BG = {"kisan":("#2f7d32","#9bcf53"),"swasthya":("#0d6e8c","#5ec8d8"),"mahila":("#a23b72","#f2a1c4"),"rozgar":("#c25e00","#f7b955"),
            "bima":("#2c4a8f","#7aa7e8"),"ghar":("#b8512a","#f4b183"),"shiksha":("#5b3fa0","#b9a2ee")}
SCENE_CAT = {"kisan":["🌾","🚜","👨‍🌾"],"swasthya":["🏥","🩺","💊"],"mahila":["👩","👧","🤱"],"rozgar":["💼","🏭","🤝"],
             "bima":["🛡️","📄","👴"],"ghar":["🏡","💡","🔑"],"shiksha":["🎓","📚","🏫"]}
# per-slug override: 3 emojis (centre first). Add new ones for each khabar post if the default is not specific enough.
SCENES = {"stand-up-india-extended-2031":["🏭","💼","👩‍💼"],"pm-surya-ghar-50-lakh-installations":["☀️","🏡","🔌"],
          "bihar-pmfby-rabi-2026-27-applications":["🌾","☔","📝"],"karnataka-ration-card-ekyc-deadline-30-november":["🪪","🍚","📱"],
          "pm-jay-public-hospital-packages-proposal":["🏥","🩺","💳"],"jeevan-pramaan-life-certificate-30-november-2026":["👴","📱","🪪"]}
def scene(em, cat, site, date):
    c1, c2 = SCENE_BG[cat]
    a, b2, c = (em + ["📄","📄"])[:3]
    return f"""<html><head><meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:630px;overflow:hidden;position:relative;background:linear-gradient(135deg,{c1},{c2});font-family:'Noto Color Emoji',sans-serif}}
.o{{position:absolute;border-radius:50%;background:rgba(255,255,255,.16)}}.e{{position:absolute;line-height:1;filter:drop-shadow(0 14px 18px rgba(0,0,0,.28))}}
.s{{position:absolute;left:36px;bottom:24px;font:700 28px sans-serif;color:#fff;opacity:.9;text-shadow:0 2px 6px rgba(0,0,0,.35)}}.d{{position:absolute;right:36px;bottom:24px;font:700 26px sans-serif;color:#fff;opacity:.85;text-shadow:0 2px 6px rgba(0,0,0,.35)}}</style></head><body>
<div class=o style="width:760px;height:760px;left:220px;top:-70px"></div><div class=o style="width:360px;height:360px;left:-80px;top:330px"></div><div class=o style="width:300px;height:300px;right:-60px;top:-60px"></div>
<div class=e style="font-size:330px;left:405px;top:130px">{a}</div><div class=e style="font-size:190px;left:150px;top:300px;transform:rotate(-8deg)">{b2}</div><div class=e style="font-size:190px;right:140px;top:90px;transform:rotate(8deg)">{c}</div>
<div class=s>ashayojana.com</div><div class=d>{date}</div></body></html>"""
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
            ycat = next(x for x in Y if x["slug"] == n["related"])["cat"]
            em = SCENES.get(n["slug"]) or SCENE_CAT[ycat]
            pg.set_content(scene(em, ycat, site, n["date"])); pg.wait_for_timeout(120)
            pg.screenshot(path=f"img/news-{n['slug']}-{lang}.jpg", type="jpeg", quality=86); n_ = 0
    import guides
    for g in guides.GUIDES:
        for lang in ("hi","en"):
            nm = g[lang]["title"]
            cat = "गाइड" if lang=="hi" else "Guide"
            site = "आशा योजना" if lang=="hi" else "Asha Yojana"
            fs = 64 if len(nm) < 45 else 52
            pg.set_content(card(g["icon"], nm, cat, site, "ashayojana.com", fs)); pg.wait_for_timeout(60)
            pg.screenshot(path=f"img/guide-{g['slug']}-{lang}.jpg", type="jpeg", quality=82)
    b.close()
sys.path.insert(0, "tools")
import apply_photos; apply_photos.run()   # real photos (photos/<slug>.jpg) override the scene images
print("images", n)
