# Pestimesh website

Static site: plain HTML, CSS and JavaScript. No build tools or hosting requirements beyond a static web server (Netlify, Vercel, GitHub Pages, cPanel, S3, etc.). Upload the contents of this `site/` folder as-is.

## Pages (19)

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About Us |
| `services.html` | Services overview |
| `ipm.html` | Integrated Pest Management |
| `termites.html`, `mosquitoes.html`, `bedbugs.html`, `cockroaches.html`, `rodents.html` | Pest control pages |
| `disinfection.html` | Disinfection & Hygiene |
| `mesh.html` | Stainless-Steel Mesh Protection |
| `termite-baiting.html` | Termite Baiting |
| `projects.html` | Projects |
| `certifications.html` | Certifications & Compliance (click any certificate to view it full-size / open the PDF) |
| `sustainability.html` | Sustainability & ESG |
| `technology.html` | Technology & Innovation |
| `news.html` | News & Community |
| `contact.html` | Contact Us |
| `faq.html` | All FAQs |

Every page ends with the enquiry form (per the sitemap) and the footer.

## Editing content

The HTML is generated from `../site-src/` (Python 3, no dependencies):

- `common.py` — contact details, nav, footer, enquiry form, icons, shared components
- `pests.py` — copy for the five pest pages
- `pages.py` — all other pages, plus the **PROJECTS**, **CERTS** and **NEWS** lists at the top
- `build.py` — run `python3 site-src/build.py` from the project root to regenerate all pages

If you prefer, you can also edit the generated `.html` files directly.

## Things to fill in

- Instagram profile URL: `INSTAGRAM` in `site-src/common.py` (currently `#`).
- Project write-ups in `pages.py` → `PROJECTS` are short placeholders based on the ESG report; replace with real scope descriptions and photos when available.
- Blog / insights articles ("to be updated in the future" in the sitemap) — the News page has placeholder cards.
- Form submission: the form currently opens the visitor's email client (pre-filled) or WhatsApp (pre-filled message). To store submissions, connect the `<form>` to a service such as Formspree, Netlify Forms or Web3Forms.

## Home hero sequence

The home page opens on a termite-tunnel scene with its own headline. The page is held there; the first scroll, swipe, arrow key or tap on the cue plays a 121-frame sequence once (tunnel, smoke, technician) over 3 seconds, then reveals the main hero copy and buttons and releases the page. It never replays on scrolling back up. Visitors arriving with a `#link`, or with reduced motion enabled, go straight to the end scene.

- Frames live in `assets/heroseq/`: `f_001…121.jpg` (1600px, desktop) and `m_001…121.jpg` (900px, phones). They were extracted from the source MP4 with ffmpeg.
- Intro wording is in the `seq-intro` block of `home()` in `site-src/pages.py`. Speed is `DURATION` in the hero sequence block of `js/main.js`.

## Logo sliders (home page)

- **Accreditations & memberships** slider uses real logos extracted from the certificates: `assets/logos/` (NEA, bizSAFE Star, WSH Council, SBF, SPMA, Tchoukball Singapore) plus ISO text badges.
- **Trusted by** client slider currently shows client names as text. To show logos, drop PNG files into `assets/logos/clients/` and set the file name in `CLIENT_LOGOS` in `site-src/pages.py`, e.g. `("psa", "PSA")` for `assets/logos/clients/psa.png`.

## Cache busting

`css/style.css` and `js/main.js` are linked with a `?v=` build stamp, so visitors always get the current files instead of a stale cached copy. The stamp is regenerated on every build.

## Assets

- `assets/img/` — photos (web-optimised JPG, max 1600 px)
- `assets/certs/` — certificate previews (JPG) and `assets/certs/pdf/` originals
- `assets/sdg/` — UN SDG icons used on the ESG page
- `assets/logo.png`, `assets/logo-light.png`, `assets/favicon.png`

## Local preview

```bash
python3 -m http.server 8791 --directory site
```

Then open http://localhost:8791
