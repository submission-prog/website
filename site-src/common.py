# Shared layout, icons and helpers for the Pestimesh static site build.
from html import escape
import time

BUILD = str(int(time.time()))   # cache-buster appended to css/js so browsers never serve a stale copy

SITE = "Pestimesh Pte Ltd"
PHONE = "+65 8668 1988"
PHONE_TEL = "+6586681988"
WA = "https://wa.me/6586681988"
EMAIL = "enquiry@pestimesh.com.sg"
ADDRESS = ["80 Playfair Road, #04-05", "Kapo Factory Building", "Singapore 367998"]
LINKEDIN = "https://www.linkedin.com/company/pestimesh-pte-ltd"
INSTAGRAM = "#"  # TODO: add Instagram profile URL

I = {
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "arrowl": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.6a2 2 0 0 1-.5 2.1L8 9.7a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.8.3 1.7.5 2.6.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="m2 7 10 7 10-7"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5L9.1 6.9c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.5 9.4 8 11 4.5-1.6 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13c0-6 5-9 16-9-1 11-4 16-9 16z"/><path d="M4 21c4-6 8-9 12-12"/></svg>',
    "bug": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7a4 4 0 0 1 8 0v1H8z"/><path d="M6 12a6 6 0 0 0 12 0v-2a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2z"/><path d="M12 8v10M3 9l3 2M21 9l-3 2M3 17l3-2M21 17l-3-2M2 13h4M18 13h4"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 8 5-3 5 3-1.5-8"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    "zoom": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5M11 8v6M8 11h6"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-5-6.7"/></svg>',
    "zap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5M3 18l9 5 9-5"/></svg>',
    "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2M10 21v-3h4v3"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
    "radar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/><path d="M12 3v9l6-6"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>',
    "thermo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0z"/></svg>',
    "mesh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v18H3zM3 9h18M3 15h18M9 3v18M15 3v18"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 9-8 9 8v10a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/></svg>',
    "spray": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 9h6v13H7zM9 9V5h2v4M11 5h4M17 5l3-2M17 8h3M17 11l3 2"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-8-5.3-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.7-8 11-8 11z"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h8"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "refresh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.6-6.4M21 3v6h-6"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 2 20h20z"/><path d="M12 9v5M12 17h.01"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
    "in": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.4 2H3.6A1.6 1.6 0 0 0 2 3.6v16.8A1.6 1.6 0 0 0 3.6 22h16.8a1.6 1.6 0 0 0 1.6-1.6V3.6A1.6 1.6 0 0 0 20.4 2zM8 19H5V9h3zM6.5 7.7A1.8 1.8 0 1 1 8.3 6a1.8 1.8 0 0 1-1.8 1.7zM19 19h-3v-4.9c0-1.2 0-2.7-1.6-2.7s-1.9 1.3-1.9 2.6V19h-3V9h2.9v1.4a3.2 3.2 0 0 1 2.9-1.6c3.1 0 3.7 2 3.7 4.7z"/></svg>',
    "quote": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 7h4v4c0 3-2 5-4 5v-2c1 0 2-1 2-3H7zm8 0h4v4c0 3-2 5-4 5v-2c1 0 2-1 2-3h-2z"/></svg>',
}

SERVICES = [
    ("ipm.html", "Integrated Pest Management", "Prevention-led programmes for every property", "layers"),
    ("termites.html", "Termites Protection", "Soil treatment, corrective, baiting & mesh", "bug"),
    ("mosquitoes.html", "Mosquitoes & Dengue Prevention", "Misting, larviciding & thermal fogging", "drop"),
    ("bedbugs.html", "Bedbugs Control", "Targeted treatment for active infestations", "home"),
    ("cockroaches.html", "Cockroaches Control", "Gel baiting & targeted applications", "search"),
    ("rodents.html", "Rodents Management", "Control, monitoring & proofing", "target"),
    ("disinfection.html", "Disinfection & Hygiene", "Cleaner, more hygienic environments", "spray"),
    ("mesh.html", "Stainless-Steel Mesh Protection", "Physical, long-term termite barrier", "mesh"),
    ("termite-baiting.html", "Termite Baiting", "Colony management with monitoring", "radar"),
]

NAV = [
    ("index.html", "Home"), ("about.html", "About Us"), ("services.html", "Services"),
    ("projects.html", "Projects"), ("certifications.html", "Certifications"),
    ("sustainability.html", "Sustainability"), ("technology.html", "Technology"),
    ("news.html", "News"), ("contact.html", "Contact"),
]


def btn(label, href, kind="lime", icon="arrow", extra=""):
    return f'<a class="btn btn-{kind} {extra}" href="{href}">{escape(label)}{I.get(icon,"")}</a>'


def link_arrow(label, href):
    return f'<a class="link-arrow" href="{href}">{escape(label)}<span class="ic">{I["arrow"]}</span></a>'


def checks(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f'<li><i>{I["check"]}</i><span>{x}</span></li>' for x in items) + "</ul>"


def faq(items, cls=""):
    out = [f'<div class="acc {cls}">']
    for q, a in items:
        out.append(f'<details><summary>{escape(q)}<span class="pm"></span></summary><div class="body"><p>{a}</p></div></details>')
    out.append("</div>")
    return "".join(out)


def mega():
    items = "".join(
        f'<a href="{h}"><span class="ico">{I[ic]}</span><span><b>{escape(n)}</b><span>{escape(d)}</span></span></a>'
        for h, n, d, ic in SERVICES)
    return f'<div class="mega"><div class="col-title">Pest Control</div><div class="col-title">Treatment &amp; Protection</div>{items}<a href="services.html" style="grid-column:1/-1;justify-content:center;font-weight:600;color:var(--teal-700)">View all services {I["arrow"]}</a></div>'


def nav(active):
    lis = []
    for h, n in NAV:
        if h == "services.html":
            lis.append(f'<li><a href="{h}">{n}{I["chev"]}</a>{mega()}</li>')
        else:
            lis.append(f'<li><a href="{h}">{n}</a></li>')
    mobile = "".join(f'<a href="{h}">{n}</a>' + (('<div class="sub">' + "".join(f'<a href="{sh}">{sn}</a>' for sh, sn, _, _ in SERVICES) + '</div>') if h == "services.html" else "") for h, n in NAV)
    return f'''<header class="nav"><div class="container">
  <a class="brand" href="index.html" aria-label="Pestimesh home"><img class="light" src="assets/logo-light.png" alt="Pestimesh — Integrated Pest Management"></a>
  <ul class="nav-links">{"".join(lis)}</ul>
  <div class="nav-cta">{btn("Book an inspection", "contact.html#enquiry", "lime")}<button class="burger" aria-label="Menu">{I["menu"]}</button></div>
</div></header>
<nav class="mobile-menu">{mobile}<div class="btn-row mt-3">{btn("WhatsApp us", WA, "wa", "wa")}{btn("Call now", "tel:"+PHONE_TEL, "ghost", "phone")}</div></nav>'''


def enquiry(title="Request a quote. Start with a site assessment.", sub="For project quotations and service enquiries, contact Pestimesh directly. Tell us a little about your property and the issue you are experiencing, and we will recommend the appropriate next step."):
    concerns = ["Termite", "Mosquito", "Bedbug", "Cockroach", "Rodent", "Disinfection", "Stainless-Steel Mesh", "Other / Not sure"]
    props = ["Residential", "Commercial", "Construction", "Facilities Management", "Other"]
    return f'''<section class="section enquiry" id="enquiry"><div class="container"><div class="split">
  <div class="reveal left">
    <div class="eyebrow light">Get in touch</div>
    <h2 class="h2">{escape(title)}</h2>
    <p class="lead light mt-2">{escape(sub)}</p>
    <div class="contact-list">
      <a href="{WA}" target="_blank" rel="noopener"><span class="ic">{I["wa"]}</span><span><b>WhatsApp Pestimesh</b><span>Fastest response for quick enquiries</span></span></a>
      <a href="tel:{PHONE_TEL}"><span class="ic">{I["phone"]}</span><span><b>{PHONE}</b><span>Call us now</span></span></a>
      <a href="mailto:{EMAIL}"><span class="ic">{I["mail"]}</span><span><b>{EMAIL}</b><span>Email for project quotations</span></span></a>
      <div><span class="ic">{I["pin"]}</span><span><b>{ADDRESS[0]}</b><span>{ADDRESS[1]}, {ADDRESS[2]}</span></span></div>
    </div>
  </div>
  <form class="form reveal right" novalidate>
    <div class="field"><label>Name</label><input name="name" required placeholder="Your name"></div>
    <div class="field"><label>Company</label><input name="company" placeholder="Optional"></div>
    <div class="field"><label>Phone number</label><input name="phone" type="tel" required placeholder="+65"></div>
    <div class="field"><label>Email</label><input name="email" type="email" required placeholder="you@company.com"></div>
    <div class="field"><label>Area of concern</label><select name="concern" required>{"".join(f'<option>{c}</option>' for c in concerns)}</select></div>
    <div class="field"><label>Property type</label><select name="property" required>{"".join(f'<option>{p}</option>' for p in props)}</select></div>
    <div class="field full"><label>Describe your concern</label><textarea name="message" placeholder="Pest issue, location, property size or anything else that helps us understand your requirements."></textarea></div>
    <div class="actions">
      <div class="btn-row"><button type="submit" class="btn btn-lime">Submit enquiry {I["arrow"]}</button><button type="button" class="btn btn-wa" data-wa-submit>Send via WhatsApp {I["wa"]}</button></div>
      <p class="note">Submitting opens your email client with the details pre-filled. Prefer WhatsApp? We pre-fill the message for you.</p>
    </div>
  </form>
</div></div></section>'''


def footer():
    svc = "".join(f'<li><a href="{h}">{escape(n)}</a></li>' for h, n, _, _ in SERVICES)
    return f'''<footer class="footer"><div class="container">
  <div class="cols">
    <div><img src="assets/logo-light.png" alt="Pestimesh"><p>NEA-registered pest management and termite protection specialists. Protecting people, properties and communities across Singapore since 2011.</p>
      <div class="social"><a href="{INSTAGRAM}" aria-label="Instagram">{I["ig"]}</a><a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{I["in"]}</a></div></div>
    <div><h5>Services</h5><ul>{svc}</ul></div>
    <div><h5>Company</h5><ul><li><a href="about.html">About Us</a></li><li><a href="projects.html">Projects</a></li><li><a href="certifications.html">Certifications &amp; Compliance</a></li><li><a href="sustainability.html">Sustainability &amp; ESG</a></li><li><a href="technology.html">Technology &amp; Innovation</a></li><li><a href="news.html">News &amp; Community</a></li><li><a href="contact.html">Contact Us</a></li></ul></div>
    <div><h5>Contact</h5><ul><li>{ADDRESS[0]}<br>{ADDRESS[1]}<br>{ADDRESS[2]}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Co. Reg. No. 201114018K</li></ul></div>
  </div>
  <div class="bottom"><span>© <span data-year></span> {SITE}. All rights reserved.</span><span>Protecting People. Protecting Properties. Protecting Communities.</span></div>
</div></footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp Pestimesh">{I["wa"]}</a>'''


def page(file, title, desc, body, with_form=True):
    import re as _re
    html = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} | Pestimesh</title>
<meta name="description" content="{escape(desc)}">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v={BUILD}">
</head><body class="preloading">
<div id="preload" aria-hidden="true"><span class="pl-half t"></span><span class="pl-half b"></span><img src="assets/logo-light.png" alt=""></div>
{nav(file)}
<main>{body}{enquiry() if with_form else ""}</main>
{footer()}
<script src="js/main.js?v={BUILD}"></script>
</body></html>'''
    return _re.sub(r'<div class="eyebrow[^"]*">.*?</div>', '', html, flags=_re.S)   # no repeated dash labels above headings


def page_hero(crumb, title, lead, bg, eyebrow=None):
    return f'''<section class="page-hero"><div class="bg" style="background-image:url('assets/img/{bg}.jpg')"></div><div class="veil"></div><div class="grid-mesh"></div>
<div class="container"><div class="crumbs"><a href="index.html">Home</a><span>/</span>{crumb}</div>
{f'<div class="eyebrow light">{eyebrow}</div>' if eyebrow else ''}
<h1 class="h1">{title}</h1><p class="lead">{lead}</p></div></section>'''


def cta_band(title, text, bg="fogging-wide"):
    return f'''<section class="cta-band"><div class="bg" style="background-image:url('assets/img/{bg}.jpg')"></div><div class="veil"></div>
<div class="container center reveal"><h2 class="h2">{title}</h2><p class="lead light mt-2">{text}</p>
<div class="btn-row mt-3" style="justify-content:center">{btn("Get a free quote", "#enquiry", "lime")}{btn("WhatsApp us", WA, "wa", "wa")}{btn("Call now", "tel:"+PHONE_TEL, "ghost", "phone")}</div></div></section>'''


def card_img(href, img, title, sub="", tag="", cls=""):
    return f'''<a class="card-img {cls}" href="{href}"><img src="assets/img/{img}.jpg" alt="{escape(title)}" loading="lazy"><div class="cap"><div><b>{title}</b><small>{sub}</small></div><span class="ic">{I["arrow"]}</span></div></a>'''
