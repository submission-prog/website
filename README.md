# Pestimesh website

Static marketing site for **Pestimesh Pte Ltd** (NEA-registered pest management and termite
protection, Singapore). Plain HTML, CSS and JavaScript — no framework, no build step required
to deploy.

## Layout

| Path | What it is |
|---|---|
| `site/` | **The website.** Deploy this folder as-is. See [`site/README.md`](site/README.md) for page list, assets and editing notes. |
| `site-src/` | Python templates that generate `site/*.html`. |
| `Certifications/` | Original certificate PDFs (source for `site/assets/certs/`). |
| `Website Photos/`, `Treatment Photos/` | Original photography (source for `site/assets/img/`). |
| `*.mp4` | Source video for the home-page hero frame sequence. |

## Editing content

Copy lives in the Python templates, not the generated HTML:

- `site-src/common.py` — contact details, navigation, footer, enquiry form, icons
- `site-src/pests.py` — the five pest pages
- `site-src/pages.py` — every other page, plus the project, certificate and news lists
- `site-src/build.py` — regenerates all 18 pages

```bash
python3 site-src/build.py
```

Requires Python 3 only (no packages). Regenerating **image assets** from the originals also
needs `pymupdf`, `Pillow` and `ffmpeg`, but that is a one-off — the generated assets are
committed.

## Local preview

```bash
python3 -m http.server 8791 --directory site
```

Then open http://localhost:8791

## Deploying

`vercel.json` points Vercel at the `site/` folder. In the Vercel project settings use
**Framework Preset: Other** and leave the build command empty. Any static host works the same
way: publish the contents of `site/`.

## Still to fill in

- Instagram profile URL (`INSTAGRAM` in `site-src/common.py`)
- Real project write-ups (`PROJECTS` in `site-src/pages.py`)
- Blog / insights articles
- A form backend if enquiries should be stored rather than emailed
