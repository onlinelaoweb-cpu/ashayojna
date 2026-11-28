# -*- coding: utf-8 -*-
# Page-specific FAQ entries assembled ONLY from facts already on each scheme page (eligibility, exclusions, documents, steps, portal).
# Targets pages Google crawled but did not index. No new facts are introduced; every answer points back to the official portal.
SLUGS = """arunachal-cmaay assam-orunodoi ayushman-bharat-pmjay bihar-samajik-suraksha-pension-yojana central-nikshay-poshan-yojana
central-pre-matric-scholarship-disabilities central-stand-up-india chhattisgarh-krishak-unnati delhi-laxmi-yojana goa-griha-aadhar
himachal-apna-parivar-sukhi-parivar-yojana jk-ladli-beti karnataka-shakti-yojana kerala-sthree-suraksha-pension lakhpati-didi-yojana
manipur-cmht nps-vatsalya-yojana pm-kusum-yojana pmegp-yojana punjab-mawan-dhiyan-satkar-yojana rajasthan-450-gas-cylinder-yojana
rajasthan-rajshri-yojana telangana-rythu-bharosa westbengal-annapurna-bhandar-yojana""".split()

def _j(l, hi): return ("; " if hi else "; ").join(x.rstrip("।. ") for x in l)

def _mk(d, hi):
    n = d["name"]; out = []
    have = " ".join(q for q, _ in d["faq"]).lower()
    link = d.get("link")
    portal = link[0].replace("https://", "").replace("http://", "").rstrip("/") if link else ""
    if d.get("elig"):
        q = f"{n} के लिए कौन पात्र है?" if hi else f"Who is eligible for {n}?"
        a = (("इस पेज के अनुसार: " if hi else "As per this page: ") + _j(d["elig"], hi) + ("। अंतिम शर्तें आधिकारिक पोर्टल/विभाग से पक्की करें।" if hi else ". Confirm final conditions with the official portal or department."))
        out.append((q, a))
    if d.get("notelig"):
        q = f"{n} के लिए कौन पात्र नहीं है?" if hi else f"Who is not eligible for {n}?"
        a = (("इस पेज के अनुसार ये लोग पात्र नहीं माने जाते: " if hi else "As per this page, these people are generally not eligible: ") + _j(d["notelig"], hi) + ("।" if hi else "."))
        out.append((q, a))
    if d.get("docs"):
        q = f"{n} में कौन-से दस्तावेज़ लगते हैं?" if hi else f"Which documents are needed for {n}?"
        a = (("आमतौर पर: " if hi else "Usually: ") + _j(d["docs"], hi) + (("। सूची बदल सकती है, आवेदन से पहले " + (portal or "विभाग") + " पर जाँच लें।") if hi else (". The list can change; check " + (portal or "the department") + " before applying.")))
        out.append((q, a))
    if d.get("steps"):
        q = f"{n} में आवेदन कैसे करें?" if hi else f"How to apply for {n}?"
        a = ((" → ".join(f"{i+1}) {s.rstrip('।. ')}" for i, s in enumerate(d["steps"]))) + ((" आधिकारिक साइट: " + portal + "। किसी एजेंट को पैसे न दें।") if portal and hi else (" Official site: " + portal + ". Do not pay any agent.") if portal else ""))
        out.append((q, a))
    return out[:4]

def apply(Y, EN):
    by = {y["slug"]: y for y in Y}
    for s in SLUGS:
        if s not in by: print("seo_auto: unknown slug", s); continue
        for d, hi in ((by[s], True), (EN[s], False)):
            have = {q for q, _ in d["faq"]}
            d["faq"] = list(d["faq"]) + [x for x in _mk(d, hi) if x[0] not in have]
