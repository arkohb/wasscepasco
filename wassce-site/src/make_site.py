"""Turn the built app files into a complete static site for Netlify / GitHub."""
import os, re, shutil, json, time
from PIL import Image, ImageDraw, ImageFont

SITE = "site"
BRAND = {"paper": "#EEF1EC", "ink": "#141C24", "dark": "#11161A",
         "maths": "#D14A76", "english": "#5A67D8", "science": "#1AA189", "social": "#C08028"}

PAGES = [
    ("wassce-core-four.html", "index.html", "WASSCE Core Four",
     "Free WASSCE practice for all four core subjects — Core Maths, English, Integrated Science and "
     "Social Studies. 886 questions with worked solutions, plain-English notes, diagrams and timed mock papers."),
    ("index.html", "maths.html", "WASSCE Core Maths Drill",
     "WASSCE Core Mathematics practice: 244 questions with full working, 64 worked examples, diagrams, "
     "the complete syllabus and a timed mock Paper 1."),
    ("english.html", "english.html", "WASSCE English Drill",
     "WASSCE English Language practice: 204 questions with model answers, comprehension passages, summary "
     "and essay guides, oral English and a timed mock Paper 1."),
    ("science.html", "science.html", "WASSCE Science Drill",
     "WASSCE Integrated Science practice: 228 questions with explanations, 76 worked examples, labelled "
     "diagrams, the complete syllabus and a timed mock Paper 1."),
    ("social.html", "social.html", "WASSCE Social Studies Drill",
     "WASSCE Social Studies practice: 210 questions with essay answer guides, 70 worked examples, the "
     "complete syllabus and a timed mock Paper 1."),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="{paper}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{dark}" media="(prefers-color-scheme: dark)">
<meta name="author" content="Bismark Arko-Ofori">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="share.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<style>
html{{color-scheme:light dark}}
:root{{padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px)}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
.sitefoot{{max-width:1080px; margin:0 auto; padding:28px 16px 40px; font-size:13px; color:var(--ink-2);
  display:flex; flex-wrap:wrap; gap:6px 16px; align-items:center; border-top:1px solid var(--rule)}}
.sitefoot a{{color:var(--accent); font-weight:600; text-decoration:none}}
.sitefoot a:hover{{text-decoration:underline}}
.sitefoot .sep{{opacity:.5}}
</style>
"""

FOOT_HUB = """<footer class="sitefoot">
  <a href="./">All four subjects</a><span class="sep">·</span>
  <a href="maths.html">Core Maths</a><span class="sep">·</span>
  <a href="english.html">English</a><span class="sep">·</span>
  <a href="science.html">Integrated Science</a><span class="sep">·</span>
  <a href="social.html">Social Studies</a>
  <span style="flex:1 1 100%">Original practice questions written to the WAEC syllabus — not reproductions of
  past WASSCE papers. Your progress is stored only in this browser.</span>
</footer>
"""
FOOT_SUB = """<footer class="sitefoot">
  <a href="./">&larr; All four subjects in one app</a>
  <span style="flex:1 1 100%">Original practice questions written to the WAEC syllabus — not reproductions of
  past WASSCE papers. Your progress is stored only in this browser.</span>
</footer>
"""

SW_REG = """<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('sw.js').catch(function(){});
  });
}
</script>
"""


def build_pages():
    for src, out, title, desc in PAGES:
        html = open(src, encoding="utf-8").read()
        cut = html.index("<header")
        head_part, body_part = html[:cut], html[cut:]
        doc = (HEAD.format(desc=desc, title=title, paper=BRAND["paper"], dark=BRAND["dark"])
               + head_part.strip() + "\n</head>\n<body>\n"
               + body_part.rstrip() + "\n"
               + (FOOT_HUB if out == "index.html" else FOOT_SUB)
               + SW_REG + "</body>\n</html>\n")
        open(os.path.join(SITE, out), "w", encoding="utf-8").write(doc)
        print(f"  {out:14s} {len(doc)//1024:4d} KB   {title}")


def icons():
    os.makedirs(f"{SITE}/icons", exist_ok=True)
    dots = [BRAND["maths"], BRAND["english"], BRAND["science"], BRAND["social"]]
    for size in (180, 192, 512):
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        r = size * 0.22
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=BRAND["ink"])
        pad, gap = size * 0.22, size * 0.12
        dr = (size - 2 * pad - gap) / 2
        for i, c in enumerate(dots):
            cx = pad + (i % 2) * (dr + gap)
            cy = pad + (i // 2) * (dr + gap)
            d.ellipse([cx, cy, cx + dr, cy + dr], fill=c)
        img.save(f"{SITE}/icons/icon-{size}.png")
    # maskable version: same art on a full-bleed background with extra padding
    size = 512
    img = Image.new("RGBA", (size, size), BRAND["ink"])
    d = ImageDraw.Draw(img)
    pad, gap = size * 0.30, size * 0.10
    dr = (size - 2 * pad - gap) / 2
    for i, c in enumerate(dots):
        cx = pad + (i % 2) * (dr + gap)
        cy = pad + (i // 2) * (dr + gap)
        d.ellipse([cx, cy, cx + dr, cy + dr], fill=c)
    img.save(f"{SITE}/icons/icon-maskable-512.png")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="WASSCE Core Four">
<rect width="64" height="64" rx="14" fill="{BRAND['ink']}"/>
<circle cx="24" cy="24" r="9" fill="{BRAND['maths']}"/>
<circle cx="40" cy="24" r="9" fill="{BRAND['english']}"/>
<circle cx="24" cy="40" r="9" fill="{BRAND['science']}"/>
<circle cx="40" cy="40" r="9" fill="{BRAND['social']}"/>
</svg>
'''
    open(f"{SITE}/favicon.svg", "w").write(svg)
    print("  icons/        4 PNG icons + favicon.svg")


def share_image():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BRAND["paper"])
    d = ImageDraw.Draw(img)
    for x in range(0, W, 40):
        d.line([(x, 0), (x, H)], fill="#E3EAE3")
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill="#E3EAE3")

    def font(sz, bold=False):
        for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSerif%s.ttf" % ("-Bold" if bold else ""),
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")):
            if os.path.exists(p):
                return ImageFont.truetype(p, sz)
        return ImageFont.load_default()

    d.text((80, 150), "WASSCE Core Four", font=font(86, True), fill=BRAND["ink"])
    d.text((80, 270), "886 practice questions · 258 worked examples", font=font(40), fill="#4F6069")
    d.text((80, 330), "Core Maths · English · Integrated Science · Social Studies",
           font=font(34), fill="#4F6069")
    for i, c in enumerate([BRAND["maths"], BRAND["english"], BRAND["science"], BRAND["social"]]):
        d.ellipse([80 + i * 54, 440, 80 + i * 54 + 36, 476], fill=c)
    d.text((80, 520), "Original practice written to the WAEC syllabus — not past papers",
           font=font(28), fill="#4F6069")
    img.save(f"{SITE}/share.png")
    print("  share.png     social preview card")


def support_files(version):
    manifest = {
        "name": "WASSCE Core Four", "short_name": "Core Four",
        "description": "WASSCE practice for Core Maths, English, Integrated Science and Social Studies.",
        "start_url": "./", "scope": "./", "display": "standalone",
        "background_color": BRAND["paper"], "theme_color": BRAND["paper"], "orientation": "portrait-primary",
        "icons": [
            {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
        "shortcuts": [
            {"name": "Core Maths", "url": "maths.html"},
            {"name": "English", "url": "english.html"},
            {"name": "Integrated Science", "url": "science.html"},
            {"name": "Social Studies", "url": "social.html"},
        ],
    }
    open(f"{SITE}/manifest.webmanifest", "w").write(json.dumps(manifest, indent=2))

    open(f"{SITE}/sw.js", "w").write('''/* WASSCE Core Four - offline support.
   HTML is network-first (so updates arrive), everything else cache-first. */
const VERSION = '%s';
const CACHE = 'wassce-' + VERSION;
const ASSETS = ['./', './index.html', './maths.html', './english.html', './science.html', './social.html',
  './manifest.webmanifest', './favicon.svg', './icons/icon-192.png', './icons/icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()).catch(() => {}));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;            // fonts etc. - leave to the browser

  const isPage = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  if (isPage) {
    e.respondWith(fetch(req)
      .then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then(r => r || caches.match('./index.html'))));
  } else {
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {
      const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res;
    })));
  }
});
''' % version)

    open(f"{SITE}/netlify.toml", "w").write('''# Netlify configuration - static site, no build step.

[build]
  publish = "."
  command = ""

# Pretty URLs: /maths instead of /maths.html
[[redirects]]
  from = "/maths"
  to = "/maths.html"
  status = 200
[[redirects]]
  from = "/english"
  to = "/english.html"
  status = 200
[[redirects]]
  from = "/science"
  to = "/science.html"
  status = 200
[[redirects]]
  from = "/social"
  to = "/social.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "geolocation=(), microphone=(), camera=()"

# HTML: always revalidate, so students get updates as soon as you redeploy
[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"

[[headers]]
  for = "/sw.js"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"

# Icons and the share image rarely change
[[headers]]
  for = "/icons/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
''')

    open(f"{SITE}/robots.txt", "w").write("User-agent: *\nAllow: /\n\nSitemap: /sitemap.xml\n")
    pages = ["", "maths.html", "english.html", "science.html", "social.html"]
    today = time.strftime("%Y-%m-%d")
    urls = "".join(f"  <url><loc>https://REPLACE-WITH-YOUR-DOMAIN/{p}</loc><lastmod>{today}</lastmod></url>\n"
                   for p in pages)
    open(f"{SITE}/sitemap.xml", "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "</urlset>\n")

    open(f"{SITE}/404.html", "w").write(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found &middot; WASSCE Core Four</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<style>
  body{{margin:0; min-height:100vh; display:grid; place-items:center; background:{BRAND['paper']};
    color:{BRAND['ink']}; font-family:system-ui,-apple-system,Segoe UI,sans-serif; text-align:center; padding:24px}}
  h1{{font-size:28px; margin:0 0 8px}}
  p{{color:#4F6069; margin:0 0 20px}}
  a{{display:inline-block; background:{BRAND['ink']}; color:{BRAND['paper']}; text-decoration:none;
    padding:10px 22px; border-radius:999px; font-weight:600}}
  @media (prefers-color-scheme: dark){{
    body{{background:{BRAND['dark']}; color:#E7ECE8}} a{{background:#E7ECE8; color:{BRAND['dark']}}}
  }}
</style></head>
<body><main>
  <h1>That page is not here</h1>
  <p>The link may be old or mistyped.</p>
  <a href="/">Go to the practice app</a>
</main></body></html>
''')
    print("  manifest, sw.js, netlify.toml, robots.txt, sitemap.xml, 404.html")


def repo_files(version):
    open(f"{SITE}/.gitignore", "w").write(
        "__pycache__/\n*.pyc\n.DS_Store\n.netlify/\nnode_modules/\n*.zip\nsrc/bank_*.json\n")

    open(f"{SITE}/README.md", "w").write(f'''# WASSCE Core Four

Free practice for the four WASSCE core subjects, as plain static HTML — no build step, no server,
no database, no sign-in.

| Subject | Topics | Questions |
|---|---|---|
| Core Mathematics | 32 | 244 |
| English Language | 24 | 204 |
| Integrated Science | 38 | 228 |
| Social Studies | 35 | 210 |
| **Total** | **129** | **886** |

Each subject carries plain-English topic notes, key facts, 258 worked examples in all, 60 diagrams,
the complete WAEC syllabus mapped to the topics, a timed mock Paper 1, and per-topic progress.
Progress is kept in the student's own browser (localStorage) — nothing is uploaded anywhere.

## Files

```
index.html      all four subjects in one app  (the home page)
maths.html      Core Mathematics only
english.html    English Language only
science.html    Integrated Science only
social.html     Social Studies only
404.html        not-found page
sw.js           service worker: the app works offline after the first visit
manifest.webmanifest + icons/   installable on a phone's home screen
netlify.toml    Netlify settings (publish ".", pretty URLs, cache headers)
sitemap.xml     edit REPLACE-WITH-YOUR-DOMAIN once you have your domain
src/            the Python source that generates the question banks (optional)
```

## Deploy on Netlify

**Option 1 — drag and drop (fastest).**
Open <https://app.netlify.com/drop> and drag this whole folder onto the page. It is live in seconds.

**Option 2 — from GitHub (recommended, so every push redeploys).**

1. Create a repository on GitHub and push this folder:
   ```bash
   git init
   git add .
   git commit -m "WASSCE Core Four practice apps"
   git branch -M main
   git remote add origin https://github.com/arkohb/YOUR-REPO.git
   git push -u origin main
   ```
2. In Netlify: **Add new site → Import an existing project → GitHub**, choose the repo.
3. Build settings — Netlify reads `netlify.toml`, so just confirm:
   - Build command: *(empty)*
   - Publish directory: `.`
4. Deploy. Every later `git push` redeploys automatically.

### Custom domain
Netlify → **Domain settings → Add a domain**. Point your domain's DNS to Netlify's name servers,
then edit `sitemap.xml` and replace `REPLACE-WITH-YOUR-DOMAIN`.

## Deploy on GitHub Pages instead

Settings → Pages → Source: *Deploy from a branch* → `main` / root. All paths in the site are
relative, so it also works from a project sub-path such as `https://arkohb.github.io/wassce/`.
(`netlify.toml` is simply ignored there.)

## Updating the content

The HTML files are generated. To change questions, edit the Python in `src/` and rebuild:

```bash
cd src
pip install -r requirements.txt
./build.sh            # rebuilds the five HTML files into the site folder
```

`src/` carries one module per block of content (`part*.py` maths, `eng*.py` English, `sci*.py`
science, `sst*.py` social studies, `ext*` the plain-English notes and worked examples),
`syllabus.py` (the syllabus map) and `draw.py` (the SVG diagram library). The build fails loudly if
a maths or science answer does not check out, if a syllabus item points at a missing topic, or if a
topic is missing from the syllabus.

## About the questions

These are **original** practice questions written to the WAEC syllabus and to the format of the
papers. They are **not** reproductions of past WASSCE papers. For the real papers, use WAEC's own
e-learning portal and the past-question booklets sold by WAEC Ghana.

Content © {time.strftime("%Y")} Bismark Arko-Ofori. Build {version}.
''')

    os.makedirs(f"{SITE}/src", exist_ok=True)
    for f in ("core.py", "draw.py", "syllabus.py", "build_subject.py", "build_hub.py", "dump.py",
              "make_site.py", "part1.py", "part2.py", "part3.py", "ext_maths.py", "ext2_maths.py",
              "eng1.py", "eng2.py", "eng3.py", "ext_eng.py", "ext2_eng.py",
              "sci1.py", "sci2.py", "sci3.py", "ext_sci.py", "ext2_sci.py",
              "sst1.py", "sst2.py", "sst3.py", "ext_sst.py", "ext2_sst.py",
              "template.html", "hub.html"):
        if os.path.exists(f):
            shutil.copy(f, f"{SITE}/src/{f}")
    open(f"{SITE}/src/requirements.txt", "w").write("sympy>=1.12\npillow>=10.0\n")
    open(f"{SITE}/src/build.sh", "w").write('''#!/usr/bin/env bash
# Rebuild every app and refresh the site folder.
set -e
cd "$(dirname "$0")"
python3 dump.py maths   part1,part2,part3,ext_maths,ext2_maths
python3 dump.py english eng1,eng2,eng3,ext_eng,ext2_eng
python3 dump.py science sci1,sci2,sci3,ext_sci,ext2_sci
python3 dump.py social  sst1,sst2,sst3,ext_sst,ext2_sst
for s in maths english science social; do python3 build_subject.py $s; done
python3 build_hub.py
python3 make_site.py
echo "Done. Commit and push, or drag the site folder to Netlify."
''')
    os.chmod(f"{SITE}/src/build.sh", 0o755)
    print("  README.md, .gitignore, src/ (python source + build.sh)")


if __name__ == "__main__":
    version = time.strftime("%Y.%m.%d")
    os.makedirs(SITE, exist_ok=True)
    print("Building site/ …")
    build_pages()
    icons()
    share_image()
    support_files(version)
    repo_files(version)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(SITE) for f in fs)
    print(f"site/ ready — {total/1024/1024:.1f} MB in total")
