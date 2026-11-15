# -*- coding: utf-8 -*-
import os, json, html, shutil, datetime
import data10, data_daily, calcs2, calcdata, data9, tags, data4, data5, data6, data7, data8, en3, en4, en5, en6, static_hi, static_en
from data1 import Y, CATS
EN = en6.EN
CALC = calcdata.CALC

# ======= CONFIG: sirf ye 4 cheezein badalni hain =======
SITE_NAME   = "आशा योजना"
SITE_NAME_EN= "Asha Yojana"
SITE_URL    = "https://ashayojana.com"     # apna domain (bina / ke) - sitemap ke liye
ADSENSE_PUB = "ca-pub-5169642227203900"                            # e.g. "ca-pub-1234567890123456"  (approval ke baad)
CONTACT_EMAIL = "ashayojana.contact@gmail.com"                          # apna contact email
# ========================================================
PH = "YOUR-DOMAIN" in SITE_URL
LASTMOD = "2026-11-15"
OUT = "site"
e = html.escape
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
CSS = open("style.css", encoding="utf-8").read()
import hashlib
CSSV = hashlib.md5(CSS.encode()).hexdigest()[:8]
open(OUT+"/style.css","w",encoding="utf-8").write(CSS)

STATES = {"up": ("उत्तर प्रदेश","Uttar Pradesh"), "bihar": ("बिहार","Bihar"), "mp": ("मध्य प्रदेश","Madhya Pradesh"), "rajasthan": ("राजस्थान","Rajasthan"), "maharashtra": ("महाराष्ट्र","Maharashtra"), "gujarat": ("गुजरात","Gujarat"), "delhi": ("दिल्ली","Delhi"), "haryana": ("हरियाणा","Haryana"), "karnataka": ("कर्नाटक","Karnataka"), "westbengal": ("पश्चिम बंगाल","West Bengal"), "tamilnadu": ("तमिलनाडु","Tamil Nadu"), "ap": ("आंध्र प्रदेश","Andhra Pradesh"), "arunachal": ("अरुणाचल प्रदेश","Arunachal Pradesh"), "assam": ("असम","Assam"), "chhattisgarh": ("छत्तीसगढ़","Chhattisgarh"), "goa": ("गोवा","Goa"), "himachal": ("हिमाचल प्रदेश","Himachal Pradesh"), "jharkhand": ("झारखंड","Jharkhand"), "kerala": ("केरल","Kerala"), "manipur": ("मणिपुर","Manipur"), "meghalaya": ("मेघालय","Meghalaya"), "mizoram": ("मिज़ोरम","Mizoram"), "nagaland": ("नागालैंड","Nagaland"), "odisha": ("ओडिशा","Odisha"), "punjab": ("पंजाब","Punjab"), "sikkim": ("सिक्किम","Sikkim"), "telangana": ("तेलंगाना","Telangana"), "tripura": ("त्रिपुरा","Tripura"), "uttarakhand": ("उत्तराखंड","Uttarakhand")}
CATS_EN = {
 "kisan":("Farmer Schemes","Direct income support and cheap credit for farmers"),
 "swasthya":("Health Schemes","Free treatment and health insurance"),
 "mahila":("Women & Girl Schemes","Savings and support schemes for girls and women"),
 "rozgar":("Jobs & Loans","Loans and support to start your own work"),
 "bima":("Insurance & Pension","Low-premium protection and old-age pension"),
 "ghar":("Home, Ration & Energy","Housing, free ration, cooking gas and solar schemes"),
 "shiksha":("Education & Scholarships","Scholarships and education loans for studies"),
}
UPD = {"hi":"15 नवंबर 2026","en":"15 November 2026"}
T = {
 "hi": dict(lang="hi", loc="hi_IN", font="Noto+Sans+Devanagari", site=SITE_NAME, home="होम", other="English", otherlbl="Read in English",
   ded="माँ आशा जी को समर्पित", tagline="सरकारी योजनाओं की सरल हिंदी जानकारी। यह एक <b>निजी, गैर-सरकारी</b> सूचना वेबसाइट है और किसी सरकारी विभाग से संबद्ध नहीं है।",
   info="जानकारी", aboutl="हमारे बारे में", contactl="संपर्क करें", privl="गोपनीयता नीति", disl="अस्वीकरण", catl="श्रेणियाँ", statel="राज्य",
   copy="आवेदन से पहले हमेशा आधिकारिक वेबसाइट पर जानकारी की पुष्टि करें।", more="पूरी जानकारी →", ad="विज्ञापन",
   central="केंद्र सरकार", lastchk="अंतिम जाँच", what="योजना क्या है?", ben="मुख्य लाभ", elig="पात्रता – कौन आवेदन कर सकता है?", notelig="कौन पात्र नहीं है / ध्यान रखें",
   docs="ज़रूरी दस्तावेज़", steps="आवेदन कैसे करें? (स्टेप बाय स्टेप)", faq="अक्सर पूछे जाने वाले सवाल", also="इन्हें भी देखें",
   warn="<b>सावधान:</b> सरकारी योजना के आवेदन के नाम पर किसी एजेंट या वेबसाइट को पैसे न दें। आधिकारिक पोर्टल पर आवेदन आम तौर पर निःशुल्क होता है। OTP, PIN या बैंक की गोपनीय जानकारी किसी से साझा न करें।",
   ttl=" – पात्रता, लाभ, आवेदन", cattl=" – सरकारी योजनाएँ",
   h1="सरकारी योजनाओं की सही और आसान जानकारी", hp="पात्रता, लाभ, दस्तावेज़ और आवेदन का तरीका – सरल हिंदी में। हर पेज पर आधिकारिक पोर्टल का लिंक।",
   findl="योजना खोजक", findh="आपके लिए कौन-सी योजना?", findp="अपना राज्य चुनें और बताएँ कि आप कौन हैं। हम आपके लिए काम की योजनाएँ दिखाएँगे।", findst="आपका राज्य", findall="सभी राज्य", findwho="मैं हूँ… (एक या ज़्यादा चुनें)", findbtn="योजनाएँ दिखाएँ", findres="आपके लिए ये योजनाएँ मिलीं", findnote="यह सिर्फ़ सुझाव है, पात्रता की पक्की जाँच नहीं। हर योजना के पेज पर पात्रता पढ़ें और आधिकारिक पोर्टल से पुष्टि करें।", findnone="कुछ चुनकर बटन दबाएँ।", findgo="🔎 आपके लिए कौन-सी योजना? (योजना खोजक)",
   dedtop="🪔 माँ आशा जी को समर्पित · हर घर तक योजनाओं की रोशनी", ph="🔍 योजना खोजें… जैसे: किसान, बीमा, पेंशन, लोन",
   statesh="राज्यवार योजनाएँ", statesub="अपने राज्य की योजनाएँ देखें। केंद्र शासित प्रदेशों के लिए केंद्र सरकार की योजनाएँ देखें।", cnt="योजनाएँ", central_h="केंद्र सरकार की योजनाएँ (पूरे देश के लिए)",
   statenote="नीचे दी गई योजनाएँ सिर्फ़ इस राज्य के निवासियों के लिए हैं। केंद्र सरकार की योजनाएँ हर राज्य में लागू हैं।", seecentral="केंद्र सरकार की योजनाएँ देखें →", soon="जल्द आ रहा है: और राज्य",
   how="हम कैसे काम करते हैं", howl=["जानकारी आधिकारिक पोर्टल और विश्वसनीय स्रोतों से जाँचकर लिखी जाती है।","हर पेज पर अंतिम जाँच की तारीख़ दी जाती है।","बदलने वाली रकम/दरों के लिए आधिकारिक पोर्टल की पुष्टि की सलाह दी जाती है।","हम आवेदन के बदले कोई पैसा नहीं लेते और न किसी एजेंट से जुड़े हैं।"],
   nores="कोई योजना नहीं मिली। दूसरा शब्द आज़माएँ।", homettl=" – सरकारी योजनाओं की जानकारी हिंदी में (पात्रता, लाभ, आवेदन)",
   homedesc="पीएम किसान, आयुष्मान भारत, उज्ज्वला, सुकन्या समृद्धि, मुद्रा लोन और भारत के सभी राज्यों की मुख्य योजनाओं की सरल हिंदी जानकारी।"),
 "en": dict(lang="en", loc="en_IN", font="Noto+Sans", site=SITE_NAME_EN, home="Home", other="हिन्दी", otherlbl="हिंदी में पढ़ें",
   ded="Dedicated to my mother, Asha ji", tagline="Simple information on government schemes. This is a <b>private, non-government</b> information website and is not affiliated with any government department.",
   info="Information", aboutl="About us", contactl="Contact us", privl="Privacy Policy", disl="Disclaimer", catl="Categories", statel="States",
   copy="Always confirm the information on the official website before applying.", more="Full details →", ad="Advertisement",
   central="Central Government", lastchk="Last checked", what="What is the scheme?", ben="Key benefits", elig="Eligibility – who can apply", notelig="Who is not eligible / things to note",
   docs="Documents required", steps="How to apply (step by step)", faq="Frequently asked questions", also="Also see",
   warn="<b>Beware:</b> Do not pay any agent or website in the name of applying for a government scheme. Applying on the official portal is generally free. Do not share OTP, PIN or confidential bank details with anyone.",
   ttl=" – Eligibility & How to Apply", cattl=" – Government Schemes",
   h1="Accurate and easy information on government schemes", hp="Eligibility, benefits, documents and how to apply – in simple language. Every page links to the official portal.",
   findl="Scheme finder", findh="Which scheme is for you?", findp="Choose your state and tell us who you are. We will show schemes that may be useful for you.", findst="Your state", findall="All states", findwho="I am… (choose one or more)", findbtn="Show schemes", findres="Schemes that may suit you", findnote="This is only a suggestion, not a confirmation of eligibility. Read the eligibility on each scheme page and confirm on the official portal.", findnone="Pick something and press the button.", findgo="🔎 Which scheme is for you? (Scheme finder)",
   dedtop="🪔 Dedicated to my mother, Asha ji · Light of schemes for every home", ph="🔍 Search schemes… e.g. farmer, insurance, pension, loan",
   statesh="State-wise schemes", statesub="See schemes of your state. For Union Territories, see the Central Government schemes.", cnt="schemes", central_h="Central Government schemes (for all of India)",
   statenote="The schemes below are only for residents of this state. Central Government schemes apply in every state.", seecentral="See Central Government schemes →", soon="Coming soon: more states",
   how="How we work", howl=["Information is written after checking official portals and reliable sources.","The date of last check is shown on every page.","For amounts/rates that change, we advise confirming on the official portal.","We take no money for applications and are not tied to any agent."],
   nores="No scheme found. Try another word.", homettl=" – Government Schemes in Hindi & English",
   homedesc="Simple information on PM Kisan, Ayushman Bharat, Ujjwala, Sukanya Samriddhi, Mudra loan and state schemes of all states of India, in Hindi and English."),
}

GA_SNIPPET = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-MGNDZDNDG8"></script>
<script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-MGNDZDNDG8');</script>"""
def adscript():
    return f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUB}" crossorigin="anonymous"></script>' if ADSENSE_PUB else ""
def adslot(t):
    # Auto ads (enabled in AdSense) place ads by themselves; manual slots need a data-ad-slot id, so none for now.
    return ""

T["hi"].update(statush="स्थिति (Status) कैसे जाँचें?", issuesh="पैसा नहीं आया? ये वजहें हो सकती हैं", calcgo="🧮 सुकन्या समृद्धि कैलकुलेटर", calcl="सुकन्या समृद्धि कैलकुलेटर", calcall="🧮 सभी कैलकुलेटर")
T["en"].update(statush="How to check your status", issuesh="Payment not received? Possible reasons", calcgo="🧮 Sukanya Samriddhi calculator", calcl="Sukanya Samriddhi calculator", calcall="🧮 All calculators")
BKHOSTS = "7nishchay-yojana.bihar aarogyasri.telangana agriculture.telangana ayushmanuttarakhand cg.gov.in dwcd.goa himachalservices jeevandayee kmut.tn kviconline medhasoft merayuva myscheme.gov.in/schemes/mkky orunodoi pmayg.nic pmjay.gov.in pmsvanidhi sarvajanpension socialjustice.mp sspy-up wcdcommpune".split()
T["hi"]["bk"] = "आधिकारिक साइट कभी-कभी धीमी या बंद रहती है। न खुले तो बाद में फिर कोशिश करें, या योजना का नाम यहाँ खोजें:"
T["en"]["bk"] = "Official sites are sometimes slow or down. If it doesn't open, try again later, or search the scheme name here:"
def view(y, lang):
    if lang == "hi":
        d = dict(y); d["url"], d["linklabel"] = y["link"]; return d
    x = EN[y["slug"]]; d = dict(y); d.update(x); d["url"] = y["link"][0]; d["linklabel"] = x["link_label"]; return d
def cname(k, lang): return CATS[k][0] if lang=="hi" else CATS_EN[k][0]
def cdesc(k, lang): return CATS[k][2] if lang=="hi" else CATS_EN[k][1]
def sname(k, lang): return STATES[k][0] if lang=="hi" else STATES[k][1]

def page(lang, path, title, desc, body, base="", ld=None, noindex=False, alt=True):
    t = T[lang]; pfx = "" if lang=="hi" else "en/"
    nav = f'<a href="{base}find.html">🔎 {e(t["findl"])}</a>' + "".join(f'<a href="{base}category/{k}.html">{v[1]} {e(cname(k,lang))}</a>' for k,v in CATS.items())
    nav += "".join(f'<a href="{base}state/{k}.html">📍 {e(sname(k,lang))}</a>' for k in STATES)
    ldj = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ""
    url = f"{SITE_URL}/{pfx}{path}"
    sw = f"{base}en/{path}" if lang=="hi" else f"{base}../{path}"
    hre = ""
    if alt and not PH:
        hre = f'<link rel="alternate" hreflang="hi" href="{SITE_URL}/{path}"><link rel="alternate" hreflang="en" href="{SITE_URL}/en/{path}"><link rel="alternate" hreflang="x-default" href="{SITE_URL}/{path}">'
    ol = "en" if lang=="hi" else "hi"
    swlink = f'<a class="lang" href="{sw}" hreflang="{ol}" lang="{ol}" title="{e(t["otherlbl"])}">🌐 {t["other"]}</a>' if alt else ""
    canon = "" if (PH or noindex) else f'<link rel="canonical" href="{url}">'
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    css = (f"{base}style.css" if lang=="hi" else f"{base}../style.css") + "?v=" + CSSV
    sn = e(t["site"])
    statelinks = "".join(f'<a href="{base}state/{k}.html">{e(sname(k,lang))}</a>' for k in STATES)
    catlinks = "".join(f'<a href="{base}category/{k}.html">{e(cname(k,lang))}</a>' for k in CATS)
    h = f"""<!doctype html><html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
{canon}{hre}{robots}
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="article"><meta property="og:locale" content="{t['loc']}"><meta property="og:site_name" content="{sn}">
<meta name="theme-color" content="#0f5a4a">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 100 100%27%3E%3Ctext y=%27.9em%27 font-size=%2790%27%3E%F0%9F%AA%94%3C/text%3E%3C/svg%3E"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={t['font']}:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">{ldj}{GA_SNIPPET}{adscript()}</head><body>
<header class="hd"><div class="w hdr"><a class="logo" href="{base}index.html"><span class="lg">🪔</span>{sn}</a>{swlink}
</div>
<nav class="w nav">{nav}</nav></header>
<main class="w">{body}</main>
<footer class="ft"><div class="w"><div class="fgrid"><div><b>{sn}</b><p>🪔 <i>{t['ded']}</i></p><p>{t['tagline']}</p></div>
<div><b>{t['info']}</b><a href="{base}about.html">{t['aboutl']}</a><a href="{base}contact.html">{t['contactl']}</a><a href="{base}privacy-policy.html">{t['privl']}</a><a href="{base}disclaimer.html">{t['disl']}</a></div>
<div><b>{t['statel']}</b>{statelinks}</div>
<div><b>{t['catl']}</b>{catlinks}</div></div>
<p class="cp">© {datetime.date.today().year} {sn} · {t['copy']}</p></div></footer>
</body></html>"""
    full = os.path.join(OUT, pfx+path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    open(full, "w", encoding="utf-8").write(h)

def card(y, base, lang):
    v = view(y, lang); t = T[lang]
    return f'<a class="card" href="{base}yojana/{y["slug"]}.html"><span class="ic">{y["icon"]}</span><span class="tg">{e(v["tag"])}</span><h3>{e(v["name"])}</h3><p>{e(v["short"])}</p><span class="more">{t["more"]}</span></a>'

URLS = []
def build(lang):
    t = T[lang]; pfx = "" if lang=="hi" else "en/"; SN = t["site"]
    def reg(p): URLS.append(pfx+p)
    ul = lambda a: "<ul>"+"".join(f"<li>{e(i)}</li>" for i in a)+"</ul>"
    ol = lambda a: "<ol class='steps'>"+"".join(f"<li>{e(i)}</li>" for i in a)+"</ol>"
    # ---------- Yojana pages ----------
    for y0 in Y:
        y = view(y0, lang)
        facts = "".join(f"<div><span>{e(k)}</span><b>{e(v)}</b></div>" for k,v in y["facts"])
        faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in y["faq"])
        ex = data9.EXTRA.get(y0["slug"]); xsec = ""; xtool = ""
        if ex and ex.get(lang):
            xs = ex[lang]
            xsec = f'<h2>{t["statush"]}</h2>{ol(xs["status"])}<h2>{t["issuesh"]}</h2>{ul(xs["issues"])}'
            y = dict(y); y["faq"] = list(y["faq"]) + [(t["statush"], " ".join(f"{i+1}. {x}" for i,x in enumerate(xs["status"])))]
            faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in y["faq"])
        xbk = ""
        if any(b in y["url"] for b in BKHOSTS):
            xbk = f'<p class="note" style="margin-top:12px">{t["bk"]} <a href="https://www.myscheme.gov.in/" target="_blank" rel="noopener nofollow">myScheme.gov.in ↗</a></p>'
        for cc in calcs2.CALCS:
            if cc["scheme"] == y0["slug"]:
                xtool += f'<p style="margin-top:12px"><a class="btn" href="../{cc["slug"]}.html">{cc["icon"]} {e(cc[lang]["h1"])}</a></p>'
        if ex and ex.get("tool"): xtool += f'<p style="margin-top:12px"><a class="btn" href="../ssy-calculator.html">{t["calcgo"]}</a></p>'
        rel = [x for x in Y if x["cat"]==y0["cat"] and x["slug"]!=y0["slug"]] or [x for x in Y if x["slug"]!=y0["slug"]]
        rel = rel[:3]
        hl = f'<p class="hl">📞 {e(y["helpline"])}</p>' if y["helpline"] else ""
        st = y0.get("state")
        where = f'📍 {e(sname(st,lang))}' if st else f'🏛️ {t["central"]}'
        crumb = f'<a href="../index.html">{t["home"]}</a> › ' + (f'<a href="../state/{st}.html">{e(sname(st,lang))}</a> › ' if st else '') + f'<a href="../category/{y0["cat"]}.html">{e(cname(y0["cat"],lang))}</a> › {e(y["tag"])}'
        relcards = "".join(card(x,"../",lang) for x in rel)
        body = f"""<nav class="bc">{crumb}</nav>
<article><h1>{e(y["name"])}</h1>
<p class="meta">{y0["icon"]} {where} · {e(y["ministry"])} · {t["lastchk"]}: {UPD[lang]}</p>
<div class="facts">{facts}</div>
<div class="note">⚠️ {e(y["note"])}</div>
{adslot(t)}
<h2>{t["what"]}</h2><p>{e(y["about"])}</p>
<h2>{t["ben"]}</h2>{ul(y["benefits"])}
<h2>{t["elig"]}</h2>{ul(y["elig"])}
<h2>{t["notelig"]}</h2>{ul(y["notelig"])}
<h2>{t["docs"]}</h2>{ul(y["docs"])}
<h2>{t["steps"]}</h2>{ol(y["steps"])}
{xsec}<a class="btn" href="{y["url"]}" target="_blank" rel="noopener nofollow">{e(y["linklabel"])} ↗</a>{hl}{xtool}{xbk}
{adslot(t)}
<h2>{t["faq"]}</h2>{faq}
<div class="warn">{t["warn"]}</div>
</article>
<h2>{t["also"]}</h2><div class="grid">{relcards}</div>"""
        ld = [{"@context":"https://schema.org","@type":"Article","headline":y["name"],"description":y["short"],"inLanguage":t["lang"],"dateModified":LASTMOD,"author":{"@type":"Organization","name":SN},"publisher":{"@type":"Organization","name":SN}},
              {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in y["faq"]]}]
        p = f"yojana/{y0['slug']}.html"; reg(p)
        page(lang, p, f'{y["name"]}{t["ttl"]} | {SN}', y["short"], body, "../", ld)

    # ---------- Category pages ----------
    for k,(nm0,ic,ds0) in CATS.items():
        items = [y for y in Y if y["cat"]==k]
        nm, ds = cname(k,lang), cdesc(k,lang)
        cards = "".join(card(y,"../",lang) for y in items)
        body = f'<nav class="bc"><a href="../index.html">{t["home"]}</a> › {e(nm)}</nav><h1>{ic} {e(nm)}</h1><p class="lead">{e(ds)}</p>{adslot(t)}<div class="grid">{cards}</div>'
        p = f"category/{k}.html"; reg(p)
        page(lang, p, f"{nm}{t['cattl']} | {SN}", ds, body, "../")

    # ---------- State pages ----------
    for k in STATES:
        items = [y for y in Y if y.get("state")==k]
        nm = sname(k,lang)
        h1 = f"{nm} की सरकारी योजनाएँ" if lang=="hi" else f"Government schemes of {nm}"
        cards = "".join(card(y,"../",lang) for y in items)
        body = f'<nav class="bc"><a href="../index.html">{t["home"]}</a> › {e(nm)}</nav><h1>📍 {e(h1)}</h1><p class="lead">{t["statenote"]}</p>{adslot(t)}<div class="grid">{cards}</div><p style="margin-top:18px"><a class="btn" href="../index.html#central">{t["seecentral"]}</a></p>'
        p = f"state/{k}.html"; reg(p)
        desc = (f"{nm} की पेंशन, बेटियों, किसान, स्वास्थ्य और रोज़गार से जुड़ी सरकारी योजनाओं की सरल जानकारी।" if lang=="hi" else f"Simple information on {nm} government schemes for pension, girls, farmers, health and jobs.")
        page(lang, p, f"{h1} | {SN}", desc, body, "../")

    # ---------- Home ----------
    chips = "".join(f'<a class="chip" href="category/{k}.html">{v[1]} {e(cname(k,lang))}</a>' for k,v in CATS.items())
    central = [y for y in Y if not y.get("state")]
    schips = "".join(f'<a class="card statecard" href="state/{k}.html"><span class="ic">📍</span><h3>{e(sname(k,lang))}</h3><p>{sum(1 for y in Y if y.get("state")==k)} {t["cnt"]}</p><span class="more">{t["more"]}</span></a>' for k in STATES)
    ccards = "".join(card(y,"",lang) for y in central)
    sj = []
    for y0 in Y:
        v = view(y0, lang); st = y0.get("state")
        sj.append({"t":v["name"],"s":v["short"],"u":f'yojana/{y0["slug"]}.html',"k":v["tag"]+" "+y0["slug"]+" "+(sname(st,"hi")+" "+sname(st,"en") if st else "")})
    sjson = json.dumps(sj, ensure_ascii=False)
    body = f"""<section class="hero"><p style="margin:0 0 4px;font-size:15px;opacity:.9">{t["dedtop"]}</p><h1>{t["h1"]}</h1>
<p>{t["hp"]}</p>
<p style="margin:0 0 10px"><a class="btn" href="find.html">{t["findgo"]}</a> <a class="btn" href="calculators.html">{t["calcall"]}</a></p><input id="q" class="search" type="search" placeholder="{t["ph"]}" autocomplete="off"><div id="res" class="grid"></div></section>
<div id="all">
<h2>{t["statesh"]}</h2><p class="lead">{t["statesub"]}</p><div class="grid sgrid">{schips}</div>
<div class="chips">{chips}</div>{adslot(t)}
<h2 id="central">{t["central_h"]}</h2><div class="grid">{ccards}</div></div>
<section class="trust"><h2>{t["how"]}</h2><ul>{"".join(f"<li>{x}</li>" for x in t["howl"])}</ul></section>
<script>const D={sjson};const q=document.getElementById('q'),r=document.getElementById('res'),a=document.getElementById('all');
q.addEventListener('input',()=>{{const v=q.value.trim().toLowerCase();if(!v){{r.innerHTML='';a.style.display='';return}}
const m=D.filter(d=>(d.t+' '+d.s+' '+d.k).toLowerCase().includes(v));a.style.display='none';
r.innerHTML=m.length?m.map(d=>'<a class="card" href="'+d.u+'"><h3>'+d.t+'</h3><p>'+d.s+'</p><span class="more">{t["more"]}</span></a>').join(''):'<p>{t["nores"]}</p>'}});</script>"""
    ld = {"@context":"https://schema.org","@type":"WebSite","name":SN,"url":SITE_URL+"/"+pfx,"inLanguage":t["lang"]}
    reg("index.html")
    page(lang, "index.html", f"{SN}{t['homettl']}", t["homedesc"], body, "", ld)

    # ---------- Scheme finder ----------
    fidx = 0 if lang=="hi" else 1
    opts = f'<option value="">{t["findall"]}</option>' + "".join(f'<option value="{k}">{e(sname(k,lang))}</option>' for k in STATES)
    boxes = "".join(f'<label class="aud"><input type="checkbox" value="{k}"> {e(v[fidx])}</label>' for k,v in tags.AUD.items())
    fj = json.dumps([{"t":view(y0,lang)["name"],"s":view(y0,lang)["short"],"u":f'yojana/{y0["slug"]}.html',"st":y0.get("state",""),"a":tags.TAGS.get(y0["slug"],"").split(),"c":sname(y0["state"],lang) if y0.get("state") else t["central"]} for y0 in Y], ensure_ascii=False)
    fbody = ('<nav class="bc"><a href="index.html">'+t["home"]+'</a> › '+e(t["findl"])+'</nav><h1>🔎 '+e(t["findh"])+'</h1><p class="lead">'+t["findp"]+'</p>'
      '<div class="finder"><label><b>'+t["findst"]+'</b><br><select id="fs" class="search" style="max-width:340px">'+opts+'</select></label>'
      '<p><b>'+t["findwho"]+'</b></p><div class="auds">'+boxes+'</div><button id="fb" class="btn" type="button">'+t["findbtn"]+'</button></div>'
      '<p class="note">⚠️ '+t["findnote"]+'</p><h2 id="fh" style="display:none">'+t["findres"]+'</h2><div id="fr" class="grid"><p>'+t["findnone"]+'</p></div>'
      '<script>const F='+fj+';const fr=document.getElementById("fr"),fh=document.getElementById("fh");'
      'document.getElementById("fb").addEventListener("click",()=>{const st=document.getElementById("fs").value;'
      'const w=[...document.querySelectorAll(".aud input:checked")].map(x=>x.value);'
      'if(!w.length){fr.innerHTML="<p>'+t["findnone"]+'</p>";fh.style.display="none";return}'
      'let m=F.filter(d=>(st===""||d.st===""||d.st===st)&&d.a.some(x=>w.includes(x)));'
      'm.sort((a,b)=>(a.st===""?1:0)-(b.st===""?1:0));fh.style.display="";'
      'fr.innerHTML=m.length?m.map(d=>\'<a class="card" href="\'+d.u+\'"><span class="tg">\'+d.c+\'</span><h3>\'+d.t+\'</h3><p>\'+d.s+\'</p><span class="more">'+t["more"]+'</span></a>\').join(""):"<p>'+t["nores"]+'</p>"});</script>')
    reg("find.html")
    page(lang, "find.html", f'{t["findh"]} | {SN}', t["findp"], fbody, "")


    # ---------- SSY calculator ----------
    C = CALC[lang]
    cb = (f'<nav class="bc"><a href="index.html">{t["home"]}</a> › {e(t["calcl"])}</nav><h1>🧮 {e(C["h1"])}</h1><p class="lead">{C["lead"]}</p>'
      f'<div class="finder"><p><label><b>{C["amt"]}</b><br><input id="am" class="search" type="number" min="0" value="1000" style="max-width:240px"></label></p>'
      f'<p><label><b>{C["fr"]}</b><br><select id="fq" class="search" style="max-width:240px"><option value="m">{C["pm"]}</option><option value="y">{C["py"]}</option></select></label></p>'
      f'<p><label><b>{C["rt"]}</b><br><input id="rt" class="search" type="number" step="0.1" min="0" value="8.2" style="max-width:240px"></label><br><small>{C["rtn"]}</small></p>'
      f'<button id="go" class="btn" type="button">{C["btn"]}</button></div><div id="out"></div>'
      f'<p class="note">⚠️ {C["note"]}</p>{adslot(t)}<h2>{C["rh"]}</h2>{ul(C["rules"])}'
      f'<p><a class="btn" href="yojana/sukanya-samriddhi-yojana.html">{C["see"]}</a></p>'
      '<script>const L='+json.dumps(C["js"],ensure_ascii=False)+';const $=i=>document.getElementById(i);'
      'const fm=n=>"₹"+Math.round(n).toLocaleString("en-IN");'
      '$("go").addEventListener("click",()=>{let a=+$("am").value,m=$("fq").value,r=+$("rt").value/100,o=$("out");'
      'const max=m==="m"?12500:150000;if(!(a>=250)){o.innerHTML="<p class=note>"+L.min+"</p>";return}if(a>max){o.innerHTML="<p class=note>"+L.max+" "+fm(max)+"</p>";return}'
      'let bal=0,dep=0,rows="";for(let y=1;y<=21;y++){let it=0,d=0;if(y<=15){if(m==="m"){for(let i=0;i<12;i++)it+=(bal+a*(i+1))*r/12;d=a*12}else{it=(bal+a)*r;d=a}}else it=bal*r;'
      'dep+=d;bal+=d+it;rows+="<tr><td>"+y+"</td><td>"+fm(d)+"</td><td>"+fm(it)+"</td><td>"+fm(bal)+"</td></tr>"}'
      'o.innerHTML="<div class=facts><div><span>"+L.mat+"</span><b>"+fm(bal)+"</b></div><div><span>"+L.dep+"</span><b>"+fm(dep)+"</b></div><div><span>"+L.int+"</span><b>"+fm(bal-dep)+"</b></div></div>'
      '<details><summary>"+L.tab+"</summary><div style=\'overflow-x:auto\'><table class=ssyt><tr><th>"+L.yr+"</th><th>"+L.d+"</th><th>"+L.i+"</th><th>"+L.b+"</th></tr>"+rows+"</table></div></details>"});</script>')
    reg("ssy-calculator.html")
    page(lang, "ssy-calculator.html", f'{C["h1"]} | {SN}', C["desc"], cb, "")


    # ---------- more calculators + hub ----------
    for cc in calcs2.CALCS:
        D = cc[lang]; fl = []
        for i, f in enumerate(cc["fields"]):
            lab = D["labels"][i]
            if f["kind"] == "num":
                inp = f'<input id="{f["id"]}" class="search" type="number" min="{f["mn"]}" step="{f["step"] or 1}" value="{f["val"]}" style="max-width:240px">'
            else:
                inp = f'<select id="{f["id"]}" class="search" style="max-width:420px">' + "".join(f'<option value="{k}">{e(vv)}</option>' for k, vv in D["opts"][i-sum(1 for g in cc["fields"][:i] if g["kind"]=="num")]) + '</select>'
            hint = (D.get("hint") or [None]*9)[i] if f["kind"]=="num" else None
            fl.append(f'<p><label><b>{e(lab)}</b><br>{inp}</label>' + (f'<br><small>{e(hint)}</small>' if hint else '') + '</p>')
        ids = json.dumps([[f["id"], f["kind"]] for f in cc["fields"]])
        body = (f'<nav class="bc"><a href="index.html">{t["home"]}</a> › <a href="calculators.html">{e(calcs2.HUB[lang]["crumb"])}</a> › {e(D["h1"])}</nav><h1>{cc["icon"]} {e(D["h1"])}</h1><p class="lead">{e(D["lead"])}</p>'
          f'<div class="finder">{"".join(fl)}<button id="go" class="btn" type="button">{e(D["btn"])}</button></div><div id="out"></div>'
          f'<p class="note">⚠️ {e(D["note"])}</p>{adslot(t)}<h2>{e(D["rh"])}</h2>{ul(D["rules"])}'
          f'<p><a class="btn" href="yojana/{cc["scheme"]}.html">{e(D["see"])}</a></p>'
          '<script>const L=' + json.dumps(D["js"], ensure_ascii=False) + ';const IDS=' + ids + ';const $=i=>document.getElementById(i);'
          'const fm=n=>"₹"+Math.round(n).toLocaleString("en-IN");'
          'function f(v){' + cc["js"] + '}'
          '$("go").addEventListener("click",()=>{const v={};IDS.forEach(p=>{v[p[0]]=p[1]=="num"?+$(p[0]).value:$(p[0]).value});$("out").innerHTML=f(v)});</script>')
        reg(cc["slug"] + ".html")
        page(lang, cc["slug"] + ".html", f'{D["h1"]} | {SN}', D["desc"], body, "")
    H = calcs2.HUB[lang]
    cards = f'<a class="card" href="ssy-calculator.html"><span class="ic">👧</span><h3>{e(CALC[lang]["h1"])}</h3><p>{e(H["ssy"])}</p><span class="more">{t["more"]}</span></a>'
    for cc in calcs2.CALCS:
        D = cc[lang]
        cards += f'<a class="card" href="{cc["slug"]}.html"><span class="ic">{cc["icon"]}</span><h3>{e(D["h1"])}</h3><p>{e(D["desc"])}</p><span class="more">{t["more"]}</span></a>'
    hb = f'<nav class="bc"><a href="index.html">{t["home"]}</a> › {e(H["crumb"])}</nav><h1>🧮 {e(H["h1"])}</h1><p class="lead">{e(H["lead"])}</p><div class="grid">{cards}</div>{adslot(t)}'
    reg("calculators.html")
    page(lang, "calculators.html", f'{H["h1"]} | {SN}', H["desc"], hb, "")

    # ---------- Static pages ----------
    mod = static_hi if lang=="hi" else static_en
    for k,(tt,b) in mod.get(SN, UPD[lang], CONTACT_EMAIL, e).items():
        reg(f"{k}.html")
        page(lang, f"{k}.html", f"{tt} | {SN}", f"{tt} – {SN}", f'<article class="static">{b}</article>', "")

build("hi"); build("en")
page("hi", "404.html", f"पेज नहीं मिला | {SITE_NAME}", "पेज नहीं मिला", '<article class="static"><h1>पेज नहीं मिला 🙏</h1><p>यह पेज मौजूद नहीं है। <a href="index.html">होम पेज</a> पर जाएँ।</p><p>Page not found. Go to the <a href="en/index.html">English home page</a>.</p></article>', noindex=True, alt=False)

# ---------- sitemap, robots, ads.txt ----------
if not PH:
    def alts(u):
        hi, en_ = (u[3:], u) if u.startswith("en/") else (u, "en/"+u)
        return f'<xhtml:link rel="alternate" hreflang="hi" href="{SITE_URL}/{hi}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/{en_}"/>'
    open(OUT+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+"".join(f"<url><loc>{SITE_URL}/{u}</loc><lastmod>{LASTMOD}</lastmod>{alts(u)}</url>" for u in URLS)+"</urlset>")
open(OUT+"/robots.txt","w").write("User-agent: *\nAllow: /\n"+("" if PH else f"Sitemap: {SITE_URL}/sitemap.xml\n"))
if ADSENSE_PUB: open(OUT+"/ads.txt","w").write(f"google.com, {ADSENSE_PUB.replace('ca-','')}, DIRECT, f08c47fec0942fa0\n")
open(OUT+"/.nojekyll","w").write("")
if not PH: open(OUT+"/CNAME","w").write(SITE_URL.replace("https://",""))
print("built", len(URLS), "pages")
