# Daily content routine for ashayojana.com (Asha Yojana)

Owner: Prabhash (replies in Hinglish, wants short practical reports). The site is a bilingual (Hindi + English) static
guide to Indian government schemes, built by `build.py` from the data files. Live at https://ashayojana.com
(repo `onlinelaoweb-cpu/ashayojna`, GitHub Pages serves branch `main`). This branch (`source`) holds the generator.

## Goal each day
Add **5 to 10 new, genuinely useful scheme pages** (state or central), both languages, then publish.
Quality beats quantity: if you cannot find 5 schemes you can verify properly, add fewer and say so. Never pad.
Why: the site is new and goes for AdSense; thin or copied pages can get it marked as low-value/scaled content.

## What to add (priority order)
1. Real, currently running schemes with high search demand and payment/eligibility questions (pension, women cash
   benefit, farmer aid, scholarship, health cover, free power, gas cylinder, housing, ration, marriage aid, etc.).
2. States that have only 1-2 schemes (see "N योजनाएँ" counts on the home page) before big states.
3. Central schemes not yet on the site.
Skip anything already present (check `DAILY_LOG.md` and `grep -h 'slug=' data*.py` / `B("` lines) and anything
discontinued, renamed, or that you cannot confirm exists today.

## How to research (mandatory)
- Use WebSearch (and WebFetch where allowed). Government portals often block fetches; then rely on 2+ independent
  reputable sources (Vikaspedia, PIB, myScheme, state dept pages, major newspapers). Today's date is available from the
  `current_time` tool - do not trust old numbers; amounts and rules change.
- Write only facts you found. If unsure, hedge in the text ("रिपोर्टों के अनुसार" / "as per reports") and keep the
  generic warning NOTE. Never invent amounts, helpline numbers, URLs, dates, or eligibility rules.
- Official link: use a domain you saw in the sources. If unsure of the exact page, link the main official domain.
- Do not copy source text; write original, simple Hindi and clear English. Both languages must say the same thing.
- Each page should answer: what is it, benefits, who is eligible/not eligible, documents, step-by-step apply, FAQ,
  and a useful warning (e.g. "beware of agents asking money").

## How to add a page
Append a `B(...)` call to `data_daily.py` (full signature and many examples in `data8.py`; bilingual tuples are
`(hindi, english)`; list lengths are automatically kept equal). Then register tags:
`tags.TAGS["<slug>"] = "w d f e s b h g wid dis"` (space separated audience codes; see tags.py).
Slug convention: `<state-key>-<scheme-name>` (state keys are in `STATES` in build.py, e.g. up, bihar, mp). For central
schemes pass `None` as the state argument (central entries have `state=None`) and a slug like `central-<name>` or the official short name.
Category keys: kisan, swasthya, mahila, rozgar, bima, ghar (see CATS in data1.py).
Optional extras: `data9.EXTRA` / `data10.py` hold "how to check status" and "payment not received" sections - only add
those if you verified the steps.

## Build, check, publish
```
git clone <repo> && cd <repo>            # use add_repo with push access if the repo is not attached
git checkout source
python3 build.py && python3 check.py     # must print PROBLEMS: 0
# visual spot check (Playwright/chromium is preinstalled): open 2 new pages at 390px width, make sure nothing overflows
git worktree add ../pub main
cd ../pub && git rm -rq . && cp -a ../<repo>/site/. . && touch .nojekyll
git add -A && git commit -m "Daily: add N schemes (...)" && git push origin main
cd ../<repo> && update DAILY_LOG.md && git add -A && git commit -m "Log" && git push origin source
```
Set `LASTMOD` in build.py to today (sitemap). Leave `UPD` alone unless you re-verified existing pages.
After pushing, confirm the remote hash equals the local one (`git ls-remote origin main`).
Commit trailers: `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.

## Log and report
Append to `DAILY_LOG.md`: date, slugs added, 1-2 source URLs per slug, anything skipped and why.
Final message (Hinglish, short): how many pages added, their names, anything uncertain or worth Prabhash checking.
If a step fails (build error, push denied), fix it or report exactly what failed; never force-push.

## Update 2026-11-16: daily task is now two parts
- Part A: 3-5 new verified pages (as above).
- Part B: re-verify 3-4 OLDER pages per day (pages from before 2026-11-16, oldest/thinnest and high-traffic central schemes first). Fix outdated facts, replace vague "as per reports" with verified facts where possible, expand thin sections, note sources checked. Discontinued/renamed schemes: say so or remove, and log. Do not bump the global UPD date; log refreshed slugs and a "could not verify" list in DAILY_LOG.md.
- Keep og-image.png (copied by build.py) and see TRAFFIC_PLAN.md. AI-detection evasion is not a goal; accuracy, sources and dates are.

## Update 2026-11-18: Part C = 1-2 'Taaza Khabar' posts daily (Google Discover + RSS)
- Add 1-2 short, verified news-update posts per day to `news.py` (NEWS list; fields in the file header). Topic: a real, dated development on a scheme (extension, instalment released, amount/rule change, deadline) found in an official/major source from the last days. Both hi+en, 3-4 short paragraphs, say what was NOT confirmed, list 2-3 sources, link `related` = an existing yojana slug. date = today (ISO). Never invent.
- Then run `python3 tools/make_images.py` (makes img/<slug>-<lang>.jpg for schemes AND news-<slug>-<lang>.jpg; commit img/), `python3 build.py && python3 check.py`. Pages: /khabar/<slug>.html, /en/khabar/..., feeds /feed.xml and /en/feed.xml, section index /khabar/index.html. Publish the same way (site/ includes img/).
- Always run make_images.py after adding new schemes too, otherwise their og:image 404s.
- If there is no genuinely new verified development that day, post fewer (0 is fine); never pad.

## Guides, scholarships and trust pages (added 2026-11-20)
- `guides.py` holds evergreen how-to guides (hi+en, fields in the file header). Each daily run may add 1 new guide to
  `guides.GUIDES` if it can verify the steps with 2+ sources (backlog ideas: Jan Dhan account, PAN-Aadhaar link, Voter ID
  correction, birth certificate, Ayushman card download, e-Shram card, Digilocker, Udyam registration, bank KYC update).
  Keep state-specific facts hedged. Link related yojana slugs in `rel`.
- Scholarship schemes (state-wise, with last dates when official) are a priority for Part A; category `rozgar`/`kisan`
  etc. are fine, scholarships go under the education category used in data1 CATS.
- `/status.html` is built from `data9.EXTRA` (status sections); `/checklist.html` is built from every scheme's docs/steps.
  `/how-we-verify.html` describes our method - do not claim anything there that the routine does not actually do.
- Every yojana page links to guides, status hub, checklist and "report a mistake" (mailto). Do not remove these.

## Discover readiness (added 22 Nov 2026)
- Guides now get per-guide share/Discover images (`img/guide-<slug>-<lang>.jpg`, made by `tools/make_images.py`) plus Article+HowTo schema. After adding a guide or khabar post ALWAYS run `python3 tools/make_images.py` and commit `img/`.
- NewsArticle/Article schema uses the PUBLISHER object (name, url, logo) and full ISO timestamps. Keep featured images 1200px wide.
- Do not add spam tactics (mass AI posts, adding strangers to WhatsApp groups).

## Push notifications (OneSignal, 22 Nov 2026)
- OneSignal app "Asha Yojana" (App ID in build.py `ONESIGNAL_APP_ID`); worker file `OneSignalSDKWorker.js` is written to site root by build.py. Slidedown prompt shows after 25s + a scroll, or via the footer bell button. Do not make it more aggressive (AdSense/UX).

- Daily routine: after adding khabar posts run `python3 tools/push_draft.py` (writes PUSH_TODAY.md with title/message/launch URL for the owner to paste into OneSignal; max 1-2 pushes/day) and commit it with SHARE_TODAY.md.

## Khabar images (22 Nov 2026)
- Khabar cards and article pages now show `img/news-<slug>-<lang>.jpg`, a topic scene made by `tools/make_images.py` (emoji scene, no headline text). For EVERY new khabar post add a specific 3-emoji entry to `SCENES` in tools/make_images.py (centre emoji = main topic) before running it; the category default is only a fallback. Never use a scene that misrepresents the news.
- Real photos: if `photos/<slug>.jpg` exists (original from Pexels, owner-supplied) and has a CROPS entry in tools/apply_photos.py, make_images.py uses it instead of the emoji scene. Keep credits in photos/CREDITS.md. Never take photos from news sites or Google Images.

## Auto photos (GitHub Action)
`.github/workflows/auto-photos.yml` runs daily 13:00 IST (and on demand): `tools/auto_photos.py` finds Unsplash landscape photos (secret `UNSPLASH_KEY`) for khabar posts lacking `photos/<slug>.jpg`, saves credit in `photos/credits.json` (shown as "Photo: name / Unsplash" on the post), `tools/apply_photos.py` crops every `photos/*.jpg` (auto crop unless listed in CROPS), builds, checks, pushes `source` and publishes `main`. No photo found -> emoji scene stays. To pick a photo yourself, drop `photos/<slug>.jpg`; the Action skips slugs that already have one. Keep topic regexes in `TOPICS` updated.
Extra pages: the same Action also adds photos to guides and scheme pages, MAX_EXTRA=8 per run (random, seeded by date, no photo reused). Pages show a hero photo only when `photos/<slug>.jpg` exists; `photos/credits.json` `out` says where the cropped image goes (img/guide-, img/, img/news-).
