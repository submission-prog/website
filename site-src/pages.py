# All non-pest pages for the Pestimesh site.
from common import *
import re

# ---------------------------------------------------------------- data
# status: "Ongoing" or "Completed" once the client confirms it. None = no badge, and the
# statistics bar on the Projects page only appears once every project has a status.
PROJECTS = [
    dict(name="Project Legend at Clarke Quay", sector="", img="tp-building", status=None),
    dict(name="ICA Service Centre", sector="Government", img="proj-ica", status=None),
    dict(name="Banyan Tree Mandai Rainforest Resort", sector="Hospitality", img="proj-banyan", status=None),
    dict(name="PUB Tuas Water Reclamation Plant", sector="Public infrastructure", img="proj-pub", status=None),
    dict(name="Family Justice Courts", sector="Government", img="proj-fjc", status=None),
    dict(name="Singapore Zoo", sector="Attractions", img="training-group-1", status=None),
    dict(name="PSA", sector="Port & logistics", img="tp-misting", status=None),
    dict(name="Indigo Hotel", sector="Hospitality", img="tech-bedbug", status=None),
    dict(name="Singapore Aviation Academy", sector="Education & aviation", img="team-site", status=None),
    dict(name="Bedok Market 216", sector="Community", img="bedok-wide", status=None),
]

CERTS_UPDATED = "September 2026"   # shown on the certifications page; refresh when credentials change

CERTS = {
    "Management systems": [
        ("iso9001", "ISO 9001:2015", "Quality Management System — provision of pest control services & anti-termite woven stainless-steel mesh", False),
        ("iso14001", "ISO 14001:2015", "Environmental Management System", False),
        ("iso45001", "ISO 45001:2018", "Occupational Health & Safety Management System", False),
        ("bizsafe-star", "bizSAFE Star", "Workplace Safety and Health Council — valid till 03.07.2027", False),
    ],
    "Awards & recognition": [
        ("es-award-2024", "Environmental Services Achievement Award 2024", "Presented by the National Environment Agency, Environmental Services Industry", False),
        ("sbea-appreciation", "SBEA Certificate of Appreciation", "Brands Entrepreneurs Alliance (Singapore), 2024", False),
    ],
    "Memberships": [
        ("sbf-membership", "Singapore Business Federation", "Statutory member — apex business chamber of Singapore", False),
        ("spma-membership", "Singapore Pest Management Association", "Ordinary membership 2025–2026", False),
        ("smm-membership", "Society of Modern Management", "Permanent member since June 2025", True),
        ("amk-cma", "Ang Mo Kio Constituency Merchant Association", "21st Term Committee (2024–2027)", True),
        ("fma", "Federation of Merchants' Associations, Singapore", "Honorary appointment, 2024–2026", False),
    ],
    "Letters of appreciation": [
        ("tbas-letter", "Tchoukball Association of Singapore", "Letter of appreciation for sponsorship and support", False),
        ("ectc-letter", "East Coast Town Council", "Letter of appreciation — Bedok Market 216 disinfection works", False),
        ("gcte-fund", "Goh Chok Tong Enable Fund", "Certificate of appreciation for community support", False),
    ],
    "Training & competence": [
        ("wsq-hazardous", "WSQ Hazardous Substances Management", "Statement of Attainment — technician certification, 2026", False),
    ],
}

NEWS = [
    dict(kind="Company news", title="Singapore Heartland Enterprise Star Award 2025", img="award-heartland", text="Pestimesh was recognised at the Singapore Heartland Enterprise Star Award 2025 ceremony on 17 December 2025, celebrating heartland enterprises that give back to their communities."),
    dict(kind="In the press", title="Bedok Market 216 reopens after large-scale disinfection", img="bedok-wide", text="Our disinfection and environmental hygiene works at Bedok Market 216 were featured in The Straits Times and Lianhe Zaobao, supporting a cleaner, safer public environment for market operators and visitors."),
    dict(kind="Community", title="Dengue awareness talk for site workers", img="dengue-1", text="Pestimesh conducted a dengue awareness talk sharing practical knowledge on identifying breeding habitats, preventive measures and proactive mosquito control."),
    dict(kind="Community", title="Supporting the Tchoukball Association of Singapore", img="tchoukball-6", text="As a founding benefactor and sponsor of TBAS, Pestimesh supports youth participation and the growth of community sport in Singapore."),
    dict(kind="Community", title="Career sharing with Bendemeer Secondary School", img="bendemeer-1", text="Students visited our office to learn about careers in pest management, safety practices and the technology behind modern pest control."),
    dict(kind="Team", title="Celebrating our people", img="birthday-1", text="Birthday celebrations, staff gatherings and team dinners help us recognise milestones and build a positive workplace culture."),
]


# Client logos for the home-page marquee. Files live in assets/logos/clients/.
# Row one carries the landmark facilities, row two the construction partners.
CLIENT_LOGOS_ROW1 = [
    ("changi-airport-group", "Changi Airport Group"), ("pub", "PUB, Singapore's National Water Agency"),
    ("singapore-zoo", "Mandai Singapore Zoo"), ("banyan-tree", "Mandai Rainforest Resort by Banyan Tree"),
    ("family-justice-courts", "Family Justice Courts"), ("hotel-indigo", "Hotel Indigo"),
    ("singapore-aviation-academy", "Singapore Aviation Academy"), ("obayashi", "Obayashi Corporation"),
    ("lum-chang", "Lum Chang Holdings"), ("soil-build", "Soilbuild Construction Group"),
    ("china-construction", "China State Construction"),
]
CLIENT_LOGOS_ROW2 = [
    ("bhcc", "BHCC Construction"), ("chiu-teng", "Chiu Teng Construction"), ("forsea", "Forsea"),
    ("hitek", "Hi-Tek Construction"), ("kwan-yong", "Kwan Yong Construction"), ("lbd", "LBD Construction Group"),
    ("lc-t-builder", "LC&T Builder"), ("lim-wen-heng", "Lim Wen Heng Construction"),
    ("pal-link", "PAL-Link Construction"), ("qing-feng", "Qingfeng Construction"), ("sanwah", "Sanwah"),
]

# ---------------------------------------------------------------- helpers

def logo_rows():
    """'Projects We Have Done': two client-logo marquees running in opposite directions."""
    item = lambda f, n: f'<span class="item logo"><img src="assets/logos/clients/{f}.png" alt="{n}" title="{n}" loading="lazy"></span>'
    row1 = "".join(item(f, n) for f, n in CLIENT_LOGOS_ROW1)
    row2 = "".join(item(f, n) for f, n in CLIENT_LOGOS_ROW2)
    return (f'<section class="section tight white" id="clients"><div class="container"><h2 class="h2 center logos-head">Projects We Have Done</h2></div>'
            f'<div class="marquee logos"><div class="track">{row1}</div></div>'
            f'<div class="marquee logos rev"><div class="track">{row2}</div></div></section>')


# Google reviews, copied from the company's Google listing on 11 Oct 2026. Five-star reviews with text only.
GOOGLE_RATING = "4.5"
GOOGLE_REVIEW_COUNT = 8
REVIEWS = [
    ("레아", "10 months ago", "Had a case of bed bugs and contacted this company to help with pest control. Service was good and everything got settled quickly, thank you 👍🏻"),
    ("Dato Siva", "10 months ago", "We had a Rodent problem in our garden and immediately decided to call Pestimesh as it has been highly recommended by my friends.They came down and within a week solved my rat infestation problem.Highly recommended"),
    ("Ming hao", "10 months ago", "Highly recommended for people who is in need of quick pest control services as they can get the job done quickly"),
    ("Leonard", "10 months ago", "Very good service. Recommend of you need any pest control services."),
    ("Andrea Lim", "10 months ago", "Very efficient, fuss free and workers know their stuff well"),
]


def reviews_section():
    stars = I["star"] * 5
    cards = "".join(
        f'<div class="review"><div class="stars">{stars}</div><p>{escape(text)}</p>'
        f'<div class="who"><span class="avatar">{escape(name[0].upper())}</span><div><b>{escape(name)}</b><span>{escape(date)} · Google</span></div></div></div>'
        for name, date, text in REVIEWS)
    return (f'<section class="section" id="reviews"><div class="container reviews-split">'
            f'<div class="reveal"><h2 class="h2">Google Reviews</h2>'
            f'<div class="rating"><b>{GOOGLE_RATING}</b><span class="stars">{stars}</span><span class="muted">Reviews on Google</span></div>'
            f'<div class="btn-row mt-4">'
            f'<a class="btn btn-lime" href="{GOOGLE_WRITE_REVIEW}" target="_blank" rel="noopener">Write a review {I["star"]}</a>'
            f'<a class="btn btn-outline" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Read all reviews {I["arrow"]}</a></div></div>'
            f'<div class="rev-slider reveal" data-revslider><div class="rev-track">{cards}</div>'
            f'<div class="rev-nav"><button type="button" data-dir="prev" aria-label="Previous review">{I["arrow"]}</button><div class="rev-dots"></div><button type="button" data-dir="next" aria-label="Next review">{I["arrow"]}</button></div></div>'
            f'</div></section>')


def slant_wall():
    """Columns of certificates for the slanted wall (home section and certifications hero)."""
    bykey = {c[0]: c for v in CERTS.values() for c in v}
    SLANT_COLUMNS = [
        ["fma", "ectc-letter", "gcte-fund"],                      # behind the headline
        ["smm-membership", "amk-cma", "tbas-letter"],
        ["spma-membership", "sbea-appreciation", "wsq-hazardous"],
        ["iso14001", "bizsafe-star", "sbf-membership"],           # clear band starts here
        ["iso9001", "iso45001", "es-award-2024"],                 # most visible column
        ["bizsafe-star", "iso9001", "spma-membership"],           # partly clipped at the edge
    ]
    def slant_card(c):
        k, n, d, land = c
        return f'''<div class="slant-card" data-lightbox="home-certs" data-full="assets/certs/{k}.jpg" data-title="{escape(n)}" data-pdf="assets/certs/pdf/{k}.pdf"><img src="assets/certs/{k}.jpg" alt="{escape(n)}" loading="lazy"><span>{escape(n)}</span></div>'''
    cols = []
    for i, keys in enumerate(SLANT_COLUMNS):
        items = [bykey[k] for k in keys]
        while len(items) < 6: items = items + [bykey[k] for k in keys]
        col_cards = "".join(slant_card(c) for c in items)   # NB: distinct name; `cards` holds the pest panels
        cols.append(f'<div class="slant-col" data-dir="{1 if i % 2 == 0 else -1}"><div class="slant-inner">{col_cards}{col_cards}</div></div>')
    return "".join(cols)

def project_card(p, cls=""):
    """Project tile: photo, name and (when known) an Ongoing / Completed badge. Not a link."""
    badge = f'<span class="pstatus {p["status"].lower()}">{p["status"]}</span>' if p.get("status") else ""
    return f'''<div class="card-img still {cls}"><img src="assets/img/{p["img"]}.jpg" alt="{escape(p["name"])}" loading="lazy">{badge}<div class="cap"><div><b>{p["name"]}</b></div></div></div>'''


def project_stats():
    """Ongoing / Completed counts. Hidden until every project has a confirmed status."""
    if not all(p.get("status") for p in PROJECTS):
        return ""
    ongoing = sum(p["status"] == "Ongoing" for p in PROJECTS)
    done = sum(p["status"] == "Completed" for p in PROJECTS)
    return (f'<div class="pstats reveal"><div><b data-count="{ongoing}">{ongoing}</b><span>Ongoing projects</span></div>'
            f'<div><b data-count="{done}">{done}</b><span>Completed projects</span></div></div>')


def news_card(n):
    return f'<article class="news-card"><div class="img"><img src="assets/img/{n["img"]}.jpg" alt="{escape(n["title"])}" loading="lazy"></div><div class="body"><span class="kind">{n["kind"]}</span><h4>{escape(n["title"])}</h4><p>{n["text"]}</p></div></article>'


def cert_card(key, name, desc, land):
    return f'''<div class="cert" data-lightbox="certs" data-full="assets/certs/{key}.jpg" data-title="{escape(name)}" data-pdf="assets/certs/pdf/{key}.pdf"><div class="thumb {'land' if land else ''}"><img src="assets/certs/{key}.jpg" alt="{escape(name)}" loading="lazy"></div><span class="zoom">{I["zoom"]}</span><div class="meta"><b>{escape(name)}</b><span>{escape(desc)}</span></div></div>'''


def gallery(items, group):
    return '<div class="masonry">' + "".join(f'<a href="#" data-lightbox="{group}" data-full="assets/img/{img}.jpg" data-title="{escape(lbl)}"><img src="assets/img/{img}.jpg" alt="{escape(lbl)}" loading="lazy"><span class="lbl">{escape(lbl)}</span></a>' for img, lbl in items) + '</div>'


# ---------------------------------------------------------------- HOME

def home():
    PANEL_FOCUS = {'tech-termite': '42%', 'tech-mosquito': '58%', 'tech-bedbug': '57%', 'tech-cockroach': '57%', 'tech-rodent': '42%'}   # technician's horizontal position per photo
    pests_cards = [
        ("termites.html", "tech-termite", "Termite", "Termite protection solutions, including chemical treatment and physical barrier solutions where appropriate.", ""),
        ("mosquitoes.html", "tech-mosquito", "Mosquito", "Targeted mosquito-control solutions designed to address both adult mosquitoes and potential breeding sources.", ""),
        ("bedbugs.html", "tech-bedbug", "Bedbug", "Targeted bedbug treatment designed to address active infestations and help prevent recurrence.", ""),
        ("cockroaches.html", "tech-cockroach", "Cockroach", "Effective cockroach treatment for homes and businesses, with solutions tailored to the level and location of infestation.", ""),
        ("rodents.html", "tech-rodent", "Rodent", "Rodent management solutions focused on controlling activity and identifying potential entry and harbourage points.", ""),
        ("disinfection.html", "bedok-1", "Disinfection", "Professional disinfection services designed to help reduce harmful microorganisms on surfaces and high-contact areas.", ""),
        ("bee-treatment.html", "pest-bee", "Bee Treatment", "Safe treatment and removal of bee and hornet nests by trained technicians.", ""),
        ("bird-spike.html", "pest-birdspike", "Bird Spike", "Humane physical deterrents that stop birds landing, roosting and nesting on exposed surfaces.", ""),
    ]
    cards = "".join(
        f'''<a class="panel{" on" if i == 0 else ""}" href="{h}" data-panel="{i}"><img src="assets/img/{im}.jpg" alt="{t}" loading="lazy" style="object-position:{PANEL_FOCUS.get(im, "50%")} center"><span class="veil"></span>
<span class="spine"><b>{t}</b></span>
<span class="open"><small>Pest control</small><b>{t}</b><span class="desc">{sub}</span><span class="go">Learn more {I["arrow"]}</span></span></a>'''
        for i, (h, im, t, sub, tag) in enumerate(pests_cards))
    proj = "".join(card_img("projects.html", p["img"], p["name"]) for p in PROJECTS)
    # Slanted certificate wall. Columns run left to right; the right-of-centre
    # columns sit in the clear part of the image, so the strongest credentials go there.
    # Columns 0-1 fall behind the headline veil, so they carry the supporting documents.
    slant_cols = slant_wall()
    body = f'''
<section class="hero hero-video">
<video class="hero-vid" autoplay muted loop playsinline preload="auto" poster="assets/img/hero-poster.jpg">
 <source src="assets/video/hero-m.mp4" type="video/mp4" media="(max-width: 760px)">
 <source src="assets/video/hero.mp4" type="video/mp4">
</video>
<div class="veil"></div>
<div class="container"><div class="hero-grid">
 <div><h1 class="display" data-split>Protecting People. Protecting Properties. Protecting Communities.</h1>
  <p class="lead">Professional pest management and termite protection built around prevention, precision, safety and responsible innovation.</p>
  <div class="btn-row">{btn("WhatsApp us", WA, "wa", "wa")}{btn("Call us now", "tel:"+PHONE_TEL, "ghost", "phone")}</div></div>
</div></div></section>
</div></div>
<section class="section"><div class="container">
 <div class="section-head center-head"><div class="reveal"><div class="eyebrow">Pests we treat</div><h2 class="h2 line-reveal">Pests We Treat</h2></div></div>
 <div class="elastic reveal" data-elastic>{cards}</div>
 <p class="muted mt-3 center">Once the plan is confirmed, our team will implement the recommended pest management measures, target the source of the infestation, treat affected areas, and arrange follow-up monitoring to help provide lasting protection.</p>
</div></section>

{logo_rows()}

<section class="section dark slant-section"><div class="slant-stage" data-slant><div class="slant-wall">{slant_cols}</div><div class="slant-veil"></div></div>
 <div class="container slant-copy"><div class="reveal left"><div class="eyebrow">Certifications &amp; compliance</div><h2 class="h2">Professional standards. Responsible practice.</h2><p class="lead mt-2">Our certifications, licences and compliance credentials are presented here for transparency. ISO 9001, 14001 and 45001 certified, bizSAFE Star and NEA-registered. Click any certificate to view it.</p><div class="btn-row mt-3">{btn("View all certifications", "certifications.html", "lime")}</div></div></div>
</section>


<section class="section white"><div class="container">
 <div class="stats words reveal-stagger">
  <div class="stat"><span class="ic">{I["clock"]}</span><div><b>Since 2011</b><span>Singapore Experience</span></div></div>
  <div class="stat"><span class="ic">{I["layers"]}</span><div><b>IPM</b><span>Prevention-led approach</span></div></div>
  <div class="stat"><span class="ic">{I["shield"]}</span><div><b>Safety First</b><span>People &amp; Site Protection</span></div></div>
  <div class="stat"><span class="ic">{I["leaf"]}</span><div><b>ESG</b><span>Responsible Growth</span></div></div>
 </div>
</div></section>

<section class="section"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Projects</div><h2 class="h2">Trusted by Singapore's landmark facilities</h2></div><div class="hs-nav reveal"><button data-dir="prev" aria-label="Previous">{I["arrowl"]}</button><button data-dir="next" aria-label="Next">{I["arrow"]}</button></div></div></div>
 <div class="auto-slider projects" data-autoscroll><div class="track">{proj}</div></div>
 <div class="container">{link_arrow("View all projects", "projects.html")}</div></section>



{reviews_section()}
<section class="section white"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">News &amp; community</div><h2 class="h2">What we're doing and contributing</h2></div>{link_arrow("All news & community", "news.html")}</div>
 <div class="grid grid-3 reveal-stagger">{"".join(news_card(n) for n in NEWS[:3])}</div>
</div></section>
'''
    body = body.replace('href="#enquiry"', 'href="contact.html#enquiry"')   # the form lives on the contact page
    return "index.html", page("index.html", "Pest Control & Termite Protection Singapore", "Pestimesh Pte Ltd — NEA-registered pest management and termite protection specialists in Singapore since 2011. IPM, stainless-steel mesh, mosquito, rodent, bedbug and cockroach control.", body, with_form=False)

# ---------------------------------------------------------------- ABOUT

def about():
    body = page_hero("About Us", "Built through experience in Singapore.", "Established in 2011, Pestimesh Pte Ltd has developed strong experience in Singapore's pest management and termite protection industry. Our work spans construction, commercial, residential and facilities-management environments.", "team-site", "About Pestimesh")
    body += f'''
<section class="section"><div class="container split">
 <div class="reveal left"><div class="eyebrow">Our Expertise</div><h2 class="h2">From homes to large-scale facilities</h2>
  <p class="lead mt-2">From homes and commercial properties to large-scale facilities, our team handles a wide range of pest problems, including termites, bedbugs, cockroaches, rodents and other common pests.</p><p class="muted mt-2">We take a practical and thorough approach to pest control — identifying the source of the problem, applying appropriate treatments and providing recommendations to help prevent future infestations.</p>
  <h3 class="h3 mt-4">Our Approach</h3><p class="mt-1">We believe effective pest control starts with understanding each property's specific needs. Our experienced team assesses the situation carefully and recommends a suitable treatment plan based on the type and extent of the infestation.</p><p class="mt-1">Our goal is to provide reliable, effective and professional pest control solutions while minimising disruption to our customers.</p></div>
 <div class="frame parallax reveal right"><img src="assets/img/tp-training.jpg" alt="Pestimesh technician on a construction site"><div class="badge"><b>2011</b><span>Established<br>in Singapore</span></div></div>
</div></section>
<section class="section"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Leadership</div><h2 class="h2">People behind the protection</h2></div></div>
 <div class="grid grid-2">
  <div class="quote reveal left"><p>“We believe the future of pest management is built on smarter, more sustainable solutions. Through Integrated Pest Management, we focus on prevention, precision and responsible pest control — protecting our communities, environments and future.”</p><footer><img src="assets/img/winnie.jpg" alt="Winnie Seng"><div><b>Winnie Seng</b><span>Managing Director, Pestimesh</span></div></footer></div>
  <div class="quote reveal right"><p>“Safety is the foundation of every project we deliver. Through prevention, precision, innovation and responsible pest management, we protect our people, customers, environment and communities while upholding quality and integrity.”</p><footer><img src="assets/img/vincent.jpg" alt="Vincent Tan"><div><b>Vincent Tan</b><span>Project Director, Pestimesh</span></div></footer></div>
 </div>
 <p class="muted mt-3 prose">Our Project Director strengthened his technical knowledge through specialised experience and learning from Australia, bringing practical expertise and international knowledge into termite protection projects in Singapore. We focus on prevention and long-term building protection rather than relying only on reactive treatment.</p>
</div></section>
<section class="section white"><div class="container split rev">
 <div class="frame reveal right"><img src="assets/img/training-group-2.jpg" alt="Pestimesh team on site"></div>
 <div class="reveal left"><div class="eyebrow">Why Choose Pestimesh?</div><h2 class="h2">Why Choose Pestimesh?</h2>
 {checks(["Established in 2011", "Extensive industry experience", "Residential and commercial pest control", "Experience with major facilities and organisations", "Pest and termite control solutions", "Professional and reliable service"])}
 <h3 class="h3 mt-3">Our Commitment</h3><p class="muted mt-1">At Pestimesh, we are committed to providing dependable pest control services that our customers can trust. Whether you are managing a home, office, hotel, industrial facility or large commercial property, our team is ready to help keep your environment pest-free.</p></div>
</div></section>
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Our people</div><h2 class="h2">A team that grows together</h2></div><p class="lead reveal">33 employees across six nationalities. Birthday celebrations, gatherings and hands-on training are part of how we build a safe, inclusive workplace.</p></div>
{gallery([("staff-1","Staff gathering"),("birthday-1","Birthday celebration"),("training-group-1","Site training"),("gathering-1","Team dinner"),("birthday-2","Celebrating milestones"),("staff-2","Team outing")], "team")}</div></section>
{logo_rows()}'''
    return "about.html", page("about.html", "About Us", "Established in 2011, Pestimesh Pte Ltd is an NEA-registered pest management and termite protection specialist in Singapore.", body)

# ---------------------------------------------------------------- SERVICES OVERVIEW

def services():
    from services import PAGES
    def first_sentence(t):
        m = re.match(r"(.+?[.!?])(\s|$)", t)
        return m.group(1) if m else t
    groups = ""
    for g, items in SERVICE_GROUPS:
        cards = "".join(card_img(h, PAGES[h]["card"], escape(n), first_sentence(PAGES[h]["lead"][0])) for h, n, _ in items)
        groups += f'<div class="mt-5"><h2 class="h2 mb-3">{escape(g)}</h2><div class="grid grid-3 reveal-stagger">{cards}</div></div>'
    body = page_hero("Services", "Pest control and protection, tailored to your property.", "From homes and commercial properties to construction sites and national facilities, every programme starts with an inspection and a plan built around prevention.", "training-group-2")
    body += f'''<section class="section" style="padding-top:20px"><div class="container">{groups}</div></section>'''
    return "services.html", page("services.html", "Services", "Pest control, termite control and protection, mosquito control, disinfection and stainless-steel mesh services in Singapore.", body)

def projects():
    tiles = "".join(project_card(p, "even") for p in PROJECTS)
    body = page_hero("Projects", "Trusted by Singapore's landmark facilities.", "Our portfolio includes pest control and termite-related projects for major facilities, and pest management programmes for developers and project teams throughout the construction phase of condominium and commercial developments.", "tp-building", "Projects")
    body += f'''
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Featured projects</div><h2 class="h2">Where we've worked</h2></div></div>
{project_stats()}<div class="grid grid-3 reveal-stagger">{tiles}</div></div></section>


<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">On site</div><h2 class="h2">Treatment in action</h2></div></div>
{gallery([("mesh-install","Stainless-steel mesh installation"),("tp-training-2","Mesh barrier works on site"),("tp-larviciding","Larviciding treatment"),("tp-misting","Water-based misting"),("tp-training","Site works"),("training-group-2","Pestimesh site team")], "site")}</div></section>'''
    return "projects.html", page("projects.html", "Projects", "Pestimesh projects: Project Legend at Clarke Quay, ICA, Singapore Zoo, Banyan Tree, Family Justice Courts, PUB Tuas, PSA, Indigo Hotel, Singapore Aviation Academy, Bedok Market 216.", body)

# ---------------------------------------------------------------- CERTIFICATIONS

def certifications():
    cats = list(CERTS.keys())
    all_cards = "".join(cert_card(*c).replace('<div class="cert" ', f'<div class="cert" data-cat="{k}" ', 1) for k, v in CERTS.items() for c in v)
    total = sum(len(v) for v in CERTS.values())
    filters = f'<button class="on" data-filter="all">All certificates <span>{total}</span></button>' + "".join(f'<button data-filter="{k}">{k} <span>{len(v)}</span></button>' for k, v in CERTS.items())
    safety = ["People and occupants", "Site conditions", "Appropriate treatment methods", "Product and chemical handling", "Application requirements", "Follow-up and monitoring", "Minimising disruption to operations"]
    docs = ["Service records", "Inspection findings", "Treatment details", "Monitoring information", "Recommendations", "Follow-up requirements"]
    body = f'''<section class="page-hero cert-hero"><div class="slant-stage" data-slant><div class="slant-wall">{slant_wall()}</div></div><div class="veil"></div>
<div class="container"><h1 class="h1">Professional Standards. Responsible Practice.</h1><p class="lead">At Pestimesh, professional pest management means more than effective treatment. We believe responsible pest management requires appropriate training, regulatory compliance, safe working practices and proper handling of pest management products and equipment. Our commitment is to operate professionally and responsibly while protecting people, properties and the environments in which we work.</p></div></section>'''
    body += f'''
<section class="section" id="credentials"><div class="container">
 <div class="section-head center-head"><div class="reveal"><h2 class="h2">Our Certifications &amp; Credentials</h2><p class="lead mt-2">Our certifications, licences and compliance credentials are presented here for transparency. Click any certificate to view it in full or open the original PDF.</p></div></div>
 <div class="filters center reveal">{filters}</div>
 <div class="cert-grid reveal-stagger" id="certgrid">{all_cards}</div>
 <p class="center muted small mt-4" data-count-label>Showing all {total} credentials</p>
 <p class="center muted small" style="margin-top:6px">Credentials, licences and memberships last reviewed in {CERTS_UPDATED}.</p>
</div></section>
<section class="section dark" id="safety"><div class="container"><div class="grid" style="max-width:760px">
<div class="reveal"><div class="eyebrow">Documentation &amp; Service Records</div><h3 class="h3">Professional programmes, properly documented</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Depending on the scope of the programme, this may include:</p>{checks(docs)}<p class="small" style="color:rgba(255,255,255,.6)">These records can help customers understand the pest management programme and track ongoing activity.</p></div></div>
<div class="divider" style="background:rgba(255,255,255,.12)"></div>
<div class="reveal"><h3 class="h3">Our Commitment</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Pestimesh is committed to maintaining professional standards across our services while continuing to improve our knowledge, processes and practices.</p></div></div></section>'''
    return "certifications.html", page("certifications.html", "Certifications & Compliance", "Pestimesh certifications: ISO 9001, ISO 14001, ISO 45001, bizSAFE Star, NEA registration, awards, memberships and letters of appreciation.", body)

# ---------------------------------------------------------------- SUSTAINABILITY

def sustainability():
    sdg = "".join(f'<img src="assets/sdg/sdg-{n}.jpg" alt="SDG {n}" title="{t}">' for n, t in [("3","Good health and well-being"),("6","Clean water and sanitation"),("8","Decent work and economic growth"),("9","Industry, innovation and infrastructure"),("11","Sustainable cities and communities"),("12","Responsible consumption and production"),("15","Life on land")])
    prio = [("Prevention", "Strengthen prevention-led pest management."), ("Physical protection", "Promote suitable exclusion and physical barrier solutions."), ("Responsible treatment", "Use appropriate and targeted intervention."), ("People & safety", "Maintain a strong focus on employee, customer and community safety."), ("Innovation", "Use technology and better methods to improve precision and effectiveness."), ("Continuous improvement", "Track progress and identify opportunities to improve environmental and social practices.")]
    body = page_hero("Sustainability &amp; ESG", "Responsible pest management for a more sustainable future.", "Responsible pest management is about more than controlling pests. It is about finding effective solutions that consider people, properties and the environment: prevention, precision and responsible intervention.", "mesh-install", "Sustainability & ESG")
    body += f'''
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Our ESG approach</div><h2 class="h2">Three areas. One commitment.</h2></div><p class="lead reveal">Our first sustainability report (FY2025) was prepared with reference to the GRI Standards, with carbon accounting aligned to the GHG Protocol. It sets the baseline against which we will measure future performance.</p></div>
<div class="pillars reveal-stagger">
<div class="pillar"><span class="big">E</span><h3 class="h3">Environment</h3><p>Reducing unnecessary intervention, encouraging prevention and using physical protection where appropriate.</p></div>
<div class="pillar"><span class="big">S</span><h3 class="h3">Social</h3><p>Protecting the health, safety and wellbeing of our employees, customers, occupants and communities.</p></div>
<div class="pillar"><span class="big">G</span><h3 class="h3">Governance</h3><p>Operating responsibly through professional standards, compliance, accountability and continuous improvement.</p></div></div></div></section>

<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">FY2025 baseline</div><h2 class="h2">Current progress</h2></div><p class="lead reveal">1 January – 31 December 2025. Our first year of tracking energy, water and emissions, and the reference point for future reduction targets.</p></div>
<div class="metric-tiles reveal-stagger">
<div class="tile"><b><span data-count="758.83">0</span><small>GJ</small></b><span>Total energy consumption (45% diesel, 45% petrol, 10% electricity)</span></div>
<div class="tile"><b><span data-count="54.93">0</span><small>tCO₂e</small></b><span>Total GHG emissions, Scope 1, 2 and 3 (46.45 / 8.32 / 0.15)</span></div>
<div class="tile"><b><span data-count="262.5">0</span><small>m³</small></b><span>Total water consumption, reduced through optimised anti-termite treatment</span></div>
<div class="tile"><b><span data-count="0">0</span></b><span>Recordable work-related injuries, fatalities and ill-health cases</span></div>
<div class="tile"><b><span data-count="33">0</span></b><span>Employees across six nationalities, 18% female</span></div>
<div class="tile"><b>24/7</b><span>Access to a whistleblowing channel for every employee</span></div>
<div class="tile"><b><span data-count="0">0</span></b><span>Incidents relating to corruption or bribery</span></div>
<div class="tile"><b>2<small>of 2</small></b><span>Board directors are women; one independent director</span></div></div></div></section>

<section class="section white"><div class="container split"><div class="reveal left"><div class="eyebrow">Environmental responsibility</div><h2 class="h2">Prevention before treatment</h2><p class="lead mt-2">A prevention-led approach reduces recurring pest activity and the need for repeated intervention. By identifying entry points, harbourage, food and water sources and other conducive conditions, we address the causes of pest activity.</p>
<h3 class="h3 mt-4">Physical pest protection</h3><p class="mt-1 muted">Stainless-steel mesh is our leading example of physical prevention. Installed as a barrier where buildings meet construction soil, it reduces reliance on chemical treatment and, in turn, lowers water and chemical consumption.</p>
<h3 class="h3 mt-4">Responsible treatment</h3><p class="mt-1 muted">Rather than a fixed volume per job, we calculate chemical and water quantities from the specific site area, minimising leftover chemicals and water waste. When treatment is required, IPM combines prevention, monitoring and targeted intervention.</p><div class="mt-3">{link_arrow("Explore stainless-steel mesh", "termite-protection.html")}</div></div>
<div class="frame parallax reveal right"><img src="assets/img/mesh-collar.jpg" alt="Stainless-steel mesh collar"><div class="badge"><b>Less</b><span>chemical, water<br>&amp; emissions</span></div></div></div></section>

<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Social</div><h2 class="h2">Safety first. People at the centre.</h2></div><p class="lead reveal">Our approach considers the safety of customers, employees, building occupants, site personnel, visitors and the wider community. Teams are supported through training, PPE, risk assessments, toolbox meetings and established safety procedures aligned with ISO 45001.</p></div>
<div class="grid grid-3 reveal-stagger">
<div class="card glow"><div class="ic">{I["shield"]}</div><h4>Occupational health &amp; safety</h4><p>Zero recordable injuries, fatalities and ill-health cases in FY2025. Incidents and near misses are investigated to strengthen procedures.</p></div>
<div class="card glow"><div class="ic">{I["users"]}</div><h4>Building skills &amp; knowledge</h4><p>Certification and licensing courses, hands-on training from Australian techniques, heat-stress and safety awareness, and mentorship.</p></div>
<div class="card glow"><div class="ic">{I["heart"]}</div><h4>Employee well-being</h4><p>Fair remuneration, medical benefits, insurance, PPE, paid leave, open communication, and gatherings that celebrate our people.</p></div></div></div></section>

<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Community</div><h2 class="h2">Protecting communities</h2></div><p class="lead reveal">Pest management contributes to healthier environments across homes, businesses, workplaces and public facilities. Beyond our services, we contribute through hygiene works, education and sport.</p></div>
<div class="grid grid-3 reveal-stagger">
{card_img("news.html", "bedok-wide", "Supporting public hygiene", "Disinfection and environmental hygiene at Bedok Market 216 for operators, workers and the public.", "Bedok Market 216")}
{card_img("news.html", "dengue-1", "Promoting dengue awareness", "Practical talks on identifying breeding habitats and adopting preventive measures.", "Education")}
{card_img("news.html", "tchoukball-2", "Supporting active communities", "Sponsor and founding benefactor of the Tchoukball Association of Singapore.", "Sport")}</div></div></section>

<section class="section dark"><div class="container split"><div class="reveal left"><div class="eyebrow">Governance</div><h2 class="h2">Responsible business</h2><p class="lead mt-2">Responsible growth requires more than delivering effective services. We maintain professional standards through:</p>{checks(["Regulatory compliance with Singapore and NEA requirements", "Appropriate training and safe work practices", "Responsible treatment practices and proper documentation", "Customer communication and continuous improvement", "Zero tolerance for bribery: no gifts, travel or entertainment to secure business", "24/7 whistleblowing access for every employee"])}</div>
<div class="reveal right"><div class="eyebrow">Commitment to UN SDGs</div><h3 class="h3">Our sustainable development goals</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">From the treatment methods we choose to the materials in our termite mesh installations, our work supports progress towards the UN Sustainable Development Goals.</p><div class="sdgs mt-3">{sdg}</div></div></div></section>

<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Looking ahead</div><h2 class="h2">Our sustainability priorities</h2></div></div>
<div class="grid grid-3 reveal-stagger">{"".join(f'<div class="card glow"><div class="num">0{i+1}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(prio))}</div>
<div class="quote mt-5 reveal"><p>“At Pestimesh, we believe that sustainability and business success go hand in hand. By working responsibly today, we can help build healthier, safer and more sustainable environments for future generations.”</p><footer><img src="assets/img/winnie.jpg" alt="Winnie Seng"><div><b>Winnie Seng</b><span>Managing Director</span></div></footer></div></div></section>'''
    return "sustainability.html", page("sustainability.html", "Sustainability & ESG", "Pestimesh's ESG approach: prevention-led pest management, stainless-steel mesh, safety-first culture, community initiatives and FY2025 GRI-referenced baseline.", body)

# ---------------------------------------------------------------- TECHNOLOGY

def technology():
    """Exactly the client's services write-up, page 14: Thermal Scanning & Inspection only."""
    body = page_hero("Technology", "Technology", [], "hero-termite")
    body += '''
<section class="section"><div class="container split"><div class="reveal left"><h2 class="h2">Thermal Scanning &amp; Inspection</h2><p class="lead mt-2">Thermal scanning technology helps identify potential termite activity, moisture issues, and concealed areas of concern without invasive investigation. Combined with professional inspections, it allows for more accurate assessment and treatment planning.</p></div>
<div class="frame reveal right"><img src="assets/img/pest-termite.jpg" alt="Termite inspection"></div></div></section>'''
    return "technology.html", page("technology.html", "Technology", "Thermal scanning and inspection at Pestimesh.", body)

def news():
    body = page_hero("News &amp; Community", "Insights, updates &amp; our community.", "From practical pest prevention advice to company news, project updates and community initiatives, this is where we share what we are learning, doing and contributing.", "award-heartland", "News & Community")
    body += f'''
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Company news &amp; community</div><h2 class="h2">Latest from Pestimesh</h2></div></div>
<div class="grid grid-3 reveal-stagger">{"".join(news_card(n) for n in NEWS)}</div></div></section>
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">In the press</div><h2 class="h2">Bedok Market 216 in the news</h2></div><p class="lead reveal">Coverage of our large-scale disinfection works in The Straits Times and Lianhe Zaobao.</p></div>
{gallery([("news-1","The Straits Times"),("news-2","Lianhe Zaobao"),("news-3","Lianhe Zaobao"),("bedok-wide","On site"),("bedok-4","With community partners"),("bedok-3","Team on site")], "press")}</div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Giving back</div><h2 class="h2">Supporting Singapore's sporting community</h2></div><p class="lead reveal">Pestimesh is proud to support the Tchoukball Association of Singapore (TBAS). Through our sponsorship we support the development of sport, youth participation and opportunities for the local sporting community. Strong communities are built not only through the places we protect, but through the people, activities and organisations that bring them together.</p></div>
{gallery([("tchoukball-6","Founding Tchoukball Benefactors"),("tchoukball-1","With the national youth team"),("tchoukball-4","Team Singapore"),("tchoukball-2","Youth players"),("tchoukball-3","Match day"),("tchoukball-5","Post-match celebration")], "tbas")}</div></section>
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Education &amp; outreach</div><h2 class="h2">Dengue awareness &amp; career sharing</h2></div><p class="lead reveal">Sharing knowledge on dengue prevention with site workers, and opening our doors to students exploring careers in pest management.</p></div>
{gallery([("dengue-1","Dengue awareness talk"),("dengue-2","Site team briefing"),("bendemeer-1","Bendemeer Secondary School visit"),("bendemeer-2","Career sharing"),("bendemeer-3","Office tour"),("temple","Community event")], "outreach")}</div></section>
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Pest management insights</div><h2 class="h2">Practical guides, coming soon</h2></div><p class="lead reveal">Prevention tips, pest identification, seasonal pest issues and property protection guidance. In the meantime, each service page has detailed prevention advice.</p></div>
<div class="grid grid-4 reveal-stagger"><div class="card glow"><div class="ic">{I["shield"]}</div><h4>Pest prevention tips</h4><p>Simple property and hygiene measures that reduce pest risks.</p></div><div class="card glow"><div class="ic">{I["search"]}</div><h4>Pest identification</h4><p>Common signs of activity and when to call for an inspection.</p></div><div class="card glow"><div class="ic">{I["clock"]}</div><h4>Seasonal pest issues</h4><p>Pest risks that become more relevant at different times of year.</p></div><div class="card glow"><div class="ic">{I["building"]}</div><h4>Property protection</h4><p>Practical guidance for homes, businesses and facilities.</p></div></div>
<div class="btn-row mt-4"><a class="btn btn-outline" href="{FACEBOOK}" target="_blank" rel="noopener">Follow on Facebook {I["fb"]}</a><a class="btn btn-outline" href="{INSTAGRAM}" target="_blank" rel="noopener">Follow on Instagram {I["ig"]}</a><a class="btn btn-outline" href="{LINKEDIN}" target="_blank" rel="noopener">Follow on LinkedIn {I["in"]}</a></div></div></section>'''
    return "news.html", page("news.html", "News & Community", "Pestimesh company news, press coverage, community initiatives, tchoukball sponsorship and dengue awareness.", body)

# ---------------------------------------------------------------- CONTACT

def contact():
    """Contact details beside the form, with the map as a wide band underneath."""
    body = page_hero("Contact Us", "Let's talk about your pest management needs.", "Whether you are dealing with an active pest problem, looking for preventive protection or planning a pest management programme for your property, our team is ready to help.", "team-bedok", "Contact Pestimesh")
    body += enquiry()
    body += f'''
<section class="section"><div class="container">
 <div class="mapband reveal"><iframe title="Pestimesh office location" src="https://www.google.com/maps?q=80+Playfair+Road+Singapore+367998&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></div>
 <div class="mapfoot"><div><b>Pestimesh Pte Ltd</b><span>{ADDRESS[0]}, {ADDRESS[1]}, {ADDRESS[2]}</span><span>Company registration no. 201114018K · NEA Vector Control Operator NEA201114018K</span></div>
 <a class="btn btn-dark" href="https://www.google.com/maps/search/?api=1&query=80+Playfair+Road+Singapore+367998" target="_blank" rel="noopener">Open in Google Maps {I["pin"]}</a></div>
</div></section>'''
    return "contact.html", page("contact.html", "Contact Us", "Contact Pestimesh Pte Ltd — 80 Playfair Road #04-05 Kapo Factory Building Singapore 367998. Call +65 8668 1988 or WhatsApp +65 8913 9966.", body, with_form=False)


ALL = [home, about, services, projects, certifications, sustainability, technology, news, contact]
