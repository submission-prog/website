# Pestimesh website

Static site: plain HTML, CSS and JavaScript. No build tools or hosting requirements beyond a static web server (Netlify, Vercel, GitHub Pages, cPanel, S3, etc.). Upload the contents of this `site/` folder as-is.

## Pages (20)

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About Us |
| `services.html` | Services overview (both groups) |
| `mosquitoes.html`, `cockroaches.html`, `bedbugs.html`, `rodents.html`, `termites.html`, `bee-treatment.html`, `bird-spike.html` | Pest Control services |
| `ipm.html`, `mosquito-mesh.html`, `termite-protection.html`, `disinfection.html` | Treatment & Protection services (the woven stainless-steel barrier now lives on `termite-protection.html`; `/mesh.html` redirects there via `vercel.json`) |
| `projects.html` | Projects |
| `certifications.html` | Certifications & Compliance |
| `sustainability.html` | Sustainability & ESG |
| `technology.html` | Technology & Innovation |
| `news.html` | News & Community |
| `contact.html` | Contact Us |

Service page wording is the client's "Pestimesh Writeup_Services.pdf" (Sep 2026), held verbatim in
`site-src/services.py`. The services menu groups live in `SERVICE_GROUPS` in `site-src/common.py`.

The enquiry form appears on the Contact page only; every other page's quote buttons link to it.

`bee-treatment.html` and `bird-spike.html` carry DRAFT wording (not from the client's write-up) marked as such in `site-src/services.py`; replace once the client supplies copy.

## Editing content

The HTML is generated from `../site-src/` (Python 3, no dependencies):

- `common.py` — contact details, nav, footer, enquiry form, icons, shared components
- `services.py` — all ten service pages (exact client wording) and the page builder
- `pages.py` — home, about, overview, projects, certifications, ESG, technology, news, contact, plus the **PROJECTS**, **CERTS** and **NEWS** lists
- `build.py` — run `python3 site-src/build.py` from the project root to regenerate all pages

If you prefer, you can also edit the generated `.html` files directly.

## Things to fill in

- Project statuses: set `status="Ongoing"` or `status="Completed"` on each entry in `PROJECTS` (`site-src/pages.py`). Each card then shows a badge, and once every project has a status the Ongoing / Completed statistics bar appears above the grid automatically.
- Hotel Indigo building photo: no accurate photo exists that can be used without a credit line; the card keeps a Pestimesh site photo until the client supplies one.
- Blog / insights articles ("to be updated in the future" in the sitemap) — the News page has placeholder cards.
- Form submission: the form currently opens the visitor's email client (pre-filled) or WhatsApp (pre-filled message). To store submissions, connect the `<form>` to a service such as Formspree, Netlify Forms or Web3Forms.

## Preloader

The home page opens on a dark green screen with the logo, then two panels split apart to reveal the
page. It shows for about 0.55 seconds once the page is parsed (it does not wait for the hero video),
and plays **once per browser session**: a flag in `sessionStorage` (`pl`) makes later visits to the
home page skip it, via a tiny inline script in the `<head>` that adds `pl-skip` to the `<html>`
element before anything paints. Reduced-motion visitors get a quick fade.

Timing is `MIN` in the preloader block of `js/main.js`; the markup and the inline script are in
`page()` in `site-src/common.py`.

## Home hero video

The home hero is a muted, looping background video (`assets/video/hero.mp4`, 1920px, with
`hero-m.mp4` for phones and `assets/img/hero-poster.jpg` as the first frame). The headline and
buttons show immediately over a flat 58% tint. Source clip: `Brand/hero-loop-source.mp4`.

## Client logos (home and About pages)

Under the heading "Projects We Have Done", two marquees scroll in opposite directions carrying
the 22 client logos in `assets/logos/clients/` (`logo_rows()` in `site-src/pages.py`, used on the home page and the About page). They are shown unboxed on the page background,
always in full colour, lifting slightly on hover. White backgrounds were keyed out of the supplied files by flood-filling
from the border, so white *inside* a mark is preserved.

Rows are `CLIENT_LOGOS_ROW1` (landmark facilities) and `CLIENT_LOGOS_ROW2` (construction
partners) in `site-src/pages.py`. Accreditation and membership logos are **not** shown on the
home page; they live on the Certifications page.

## Google reviews (home page)

The home page shows the company's five-star Google reviews that have written text, copied from the
Google listing on 11 Oct 2026 into `REVIEWS` in `site-src/pages.py`, with the overall rating and
rating in `GOOGLE_RATING`. The cards sit in a one-at-a-time slider that auto-advances every 5 seconds and loops (`[data-revslider]` in `js/main.js`). "Write a review" opens Google's review form for the
listing and "Read all reviews" opens the listing. Google has no free public API for reviews, so
refresh the list by hand when new five-star reviews arrive.

## Phone numbers

WhatsApp buttons and the enquiry form's WhatsApp option go to Winnie (`WA` in `site-src/common.py`, and `WA` in `js/main.js`). The Contact page also lists Vincent's number and the office line.

## Social links

`FACEBOOK`, `INSTAGRAM` and `LINKEDIN` in `site-src/common.py` feed the footer, the mobile menu and
the News page follow buttons.

## Cache busting

`css/style.css` and `js/main.js` are linked with a `?v=` build stamp, so visitors always get the current files instead of a stale cached copy. The stamp is regenerated on every build.

## Service hero photos

Mosquito, Bed Bug, Cockroach, Rodent and Termite Control use dedicated wide hero photos
(`assets/img/hero-mosquito.jpg`, `hero-bedbug`, `hero-cockroach`, `hero-rodent`, `hero-termite-svc`).
Any service whose `hero` starts with `hero-` gets the brighter "photo" hero style; originals are in `Service Photos/`.

## Solution card photos

Cards on the service pages can carry a photo behind a heavy flat tint. The mapping is `CARD_PHOTOS`
in `site-src/services.py` (page → card title → image). Cards with no accurate photo are left plain
on purpose. Only client-supplied photos are used; no stock or Creative Commons images, so no
credit lines appear anywhere on the site.

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

## Fogging photos

Fogging and misting photos appear only on the Mosquito page, where thermal fogging is offered.
Elsewhere the site uses inspection, mesh and team photos instead.
