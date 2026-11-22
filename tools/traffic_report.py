# Weekly traffic report from Google Analytics 4 + Search Console, read-only, via a Google service account (backup to the Supermetrics connector).
# Needs env GCP_SA_KEY (service-account JSON). GA_PROPERTY_ID defaults to the ashayojana.com GA4 property. Writes TRAFFIC_REPORT.md.
import os, sys, json, datetime, urllib.parse
SITE = "sc-domain:ashayojana.com"
GA_PROP = os.environ.get("GA_PROPERTY_ID") or "564355542"
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly", "https://www.googleapis.com/auth/webmasters.readonly"]
def session():
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
    info = json.loads(os.environ["GCP_SA_KEY"])
    return AuthorizedSession(service_account.Credentials.from_service_account_info(info, scopes=SCOPES))
def ga(s, body):
    r = s.post(f"https://analyticsdata.googleapis.com/v1beta/properties/{GA_PROP}:runReport", json=body, timeout=60); r.raise_for_status(); return r.json()
def gsc(s, body):
    r = s.post("https://www.googleapis.com/webmasters/v3/sites/" + urllib.parse.quote(SITE, safe="") + "/searchAnalytics/query", json=body, timeout=60); r.raise_for_status(); return r.json().get("rows", [])
def rows(j, nd):  # GA4 response -> [(dims..., metrics...)]
    out = []
    for r in j.get("rows", []):
        out.append([d["value"] for d in r["dimensionValues"]] + [float(m["value"]) for m in r["metricValues"]])
    return out
def pct(a, b): return "n/a" if not b else f"{(a-b)/b*100:+.0f}%"
def build(s, today=None):
    t = today or datetime.date.today(); e = t - datetime.timedelta(days=1)   # yesterday = last full day
    d7 = (e - datetime.timedelta(days=6)).isoformat(); p7s = (e - datetime.timedelta(days=13)).isoformat(); p7e = (e - datetime.timedelta(days=7)).isoformat()
    E = e.isoformat(); L = []
    L += [f"# Asha Yojana traffic report ({d7} to {E})", "", f"_Auto-generated {t.isoformat()} by tools/traffic_report.py (GA4 property {GA_PROP}, Search Console {SITE})._", ""]
    # GA4 totals this week vs previous week
    tot = ga(s, {"dateRanges": [{"startDate": d7, "endDate": E, "name": "w"}, {"startDate": p7s, "endDate": p7e, "name": "p"}],
                 "metrics": [{"name": "sessions"}, {"name": "totalUsers"}, {"name": "screenPageViews"}]})
    cur = {"sessions": 0, "totalUsers": 0, "screenPageViews": 0}; prv = dict(cur)
    for r in tot.get("rows", []):
        which = r["dimensionValues"][0]["value"] if r.get("dimensionValues") else "w"
        vals = [float(m["value"]) for m in r["metricValues"]]
        tgt = prv if which in ("p", "date_range_1") else cur
        for k, v in zip(cur, vals): tgt[k] = v
    L += ["## Visitors (GA4)", "| | this week | prev week | change |", "|---|---|---|---|"]
    for k, name in (("sessions", "Sessions"), ("totalUsers", "Users"), ("screenPageViews", "Page views")):
        L.append(f"| {name} | {cur[k]:.0f} | {prv[k]:.0f} | {pct(cur[k], prv[k])} |")
    ch = rows(ga(s, {"dateRanges": [{"startDate": d7, "endDate": E}], "dimensions": [{"name": "sessionDefaultChannelGrouping"}], "metrics": [{"name": "sessions"}], "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]}), 1)
    L += ["", "### Channels", "| channel | sessions |", "|---|---|"] + [f"| {r[0]} | {r[1]:.0f} |" for r in ch]
    pg = rows(ga(s, {"dateRanges": [{"startDate": d7, "endDate": E}], "dimensions": [{"name": "pagePath"}], "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}], "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}], "limit": 10}), 1)
    L += ["", "### Top pages", "| page | views | sessions |", "|---|---|---|"] + [f"| {r[0]} | {r[1]:.0f} | {r[2]:.0f} |" for r in pg]
    # Search Console (data lags ~2 days)
    ge = (e - datetime.timedelta(days=2)); g7 = (ge - datetime.timedelta(days=6)); gp_s = (ge - datetime.timedelta(days=13)); gp_e = (ge - datetime.timedelta(days=7))
    def tot_gsc(a, b):
        r = gsc(s, {"startDate": a.isoformat(), "endDate": b.isoformat()})
        return (r[0]["clicks"], r[0]["impressions"], r[0]["position"]) if r else (0, 0, 0)
    c1, i1, p1 = tot_gsc(g7, ge); c0, i0, p0 = tot_gsc(gp_s, gp_e)
    L += ["", f"## Google search ({g7.isoformat()} to {ge.isoformat()}, Search Console lags ~2 days)", "| | this week | prev week | change |", "|---|---|---|---|",
          f"| Clicks | {c1:.0f} | {c0:.0f} | {pct(c1, c0)} |", f"| Impressions | {i1:.0f} | {i0:.0f} | {pct(i1, i0)} |", f"| Avg position | {p1:.1f} | {p0:.1f} | |"]
    q = gsc(s, {"startDate": g7.isoformat(), "endDate": ge.isoformat(), "dimensions": ["query", "page"], "rowLimit": 15})
    q.sort(key=lambda r: (-r["clicks"], -r["impressions"]))
    L += ["", "### Top queries", "| query | page | clicks | impressions | position |", "|---|---|---|---|---|"]
    L += [f"| {r['keys'][0]} | {r['keys'][1].replace('https://ashayojana.com','')} | {r['clicks']:.0f} | {r['impressions']:.0f} | {r['position']:.0f} |" for r in q[:10]]
    L += ["", "Indexed-page count is not in these APIs: check Search Console > Pages.", ""]
    return "\n".join(L)
def main():
    if not os.environ.get("GCP_SA_KEY"): print("GCP_SA_KEY missing, skipping"); return 0
    s = session(); txt = build(s); open("TRAFFIC_REPORT.md", "w", encoding="utf-8").write(txt); print(txt)
if __name__ == "__main__": main()
