# Run after `python3 build.py`. Checks internal links, canonical domain and basic page structure.
import re, glob, os, sys
bad = 0
pages = glob.glob('site/**/*.html', recursive=True)
for f in pages:
    s = open(f, encoding='utf-8').read(); d = os.path.dirname(f)
    if 'YOUR-DOMAIN' in s: print('placeholder domain in', f); bad += 1
    for h in re.findall(r'href="([^"#?]+)"', s):
        if h.startswith(('http', 'mailto', 'data:', '//', "'+")): continue
        if not os.path.exists(os.path.normpath(os.path.join(d, h))): print('BROKEN', f, h); bad += 1
    if '/yojana/' in f and '<h1>' not in s: print('no h1', f); bad += 1
sm = open('site/sitemap.xml', encoding='utf-8').read()
print('pages', len(pages), 'sitemap urls', sm.count('<loc>'), 'CNAME', open('site/CNAME').read().strip())
print('PROBLEMS:', bad); sys.exit(1 if bad else 0)
