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
schemes use the state value as in existing central entries in data1/data2 (check how they set `state`).
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
