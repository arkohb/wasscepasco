# WASSCE Core Four

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

Content © 2026 Bismark Arko-Ofori. Build 2026.10.14.
