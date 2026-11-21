# Crops photos/<slug>.jpg (originals) to 1200x630 -> img/news-<slug>-{hi,en}.jpg. Run from repo root BEFORE build.py.
# CROPS: slug -> (x0 fraction, y0 fraction, width fraction); height follows the 1200:630 ratio. BLUR: fractional boxes (x0,y0,x1,y1).
import os, json
from PIL import Image, ImageFilter, ImageEnhance
CROPS = {
 "pm-jay-public-hospital-packages-proposal": (0, .45, 1.0),
 "jeevan-pramaan-life-certificate-30-november-2026": (0, .09, 1.0),
 "bihar-pmfby-rabi-2026-27-applications": (0, .12, 1.0),
 "karnataka-ration-card-ekyc-deadline-30-november": (.24, .452, .76),
 "stand-up-india-extended-2031": (0, .084, 1.0),
 "pm-surya-ghar-50-lakh-installations": (0, .20, 1.0),
}
BLUR = {"pm-jay-public-hospital-packages-proposal": [(.30, .735, .40, .775), (.67, .755, .77, .79)]}
BRIGHT = {"pm-jay-public-hospital-packages-proposal": 1.25}
def run():
    import glob
    slugs = [os.path.basename(f)[:-4] for f in sorted(glob.glob("photos/*.jpg"))]
    try: cred = json.load(open("photos/credits.json", encoding="utf-8"))
    except Exception: cred = {}
    for slug in slugs:
        x0f, y0f, wf = CROPS.get(slug, (0, None, 1.0))  # auto photos: full width, vertically a bit above centre (faces/subjects sit high)
        src = f"photos/{slug}.jpg"
        im = Image.open(src).convert("RGB"); W, H = im.size
        for (a, b, c, d) in BLUR.get(slug, []):
            box = (int(a*W), int(b*H), int(c*W), int(d*H))
            im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(25)), box)
        w = int(wf*W); h = int(w*630/1200); x0 = int(x0f*W); y0 = min(int((y0f if y0f is not None else max(0.0, (H-h)*0.4/H))*H), H-h)
        out = im.crop((x0, y0, x0+w, y0+h)).resize((1200, 630), Image.LANCZOS)
        if slug in BRIGHT: out = ImageEnhance.Brightness(out).enhance(BRIGHT[slug])
        pre = cred.get(slug, {}).get("out", "img/news-")  # news default; guides -> img/guide-, schemes -> img/
        for lang in ("hi", "en"): out.save(f"{pre}{slug}-{lang}.jpg", quality=86)
if __name__ == "__main__": run()
