# All non-pest pages for the Pestimesh site.
from common import *
from pests import PESTS

# ---------------------------------------------------------------- data
PROJECTS = [
    dict(name="Changi Airport Terminal 2", sector="Aviation", img="tp-building", blurb="Pest management support for one of Singapore's busiest transport hubs, where continuity of operations and safety are paramount."),
    dict(name="ICA Service Centre", sector="Government", img="proj-ica", blurb="Pest control and termite protection works for a high-traffic public service facility."),
    dict(name="Banyan Tree Mandai Rainforest Resort", sector="Hospitality", img="proj-banyan", blurb="Prevention-led pest management for a nature-integrated resort, balancing guest experience with sensitivity to the surrounding ecosystem."),
    dict(name="PUB Tuas Water Reclamation Plant", sector="Public infrastructure", img="proj-pub", blurb="Pest management programme for critical national water infrastructure."),
    dict(name="Family Justice Courts", sector="Government", img="proj-fjc", blurb="Pest control and termite-related works for an institutional facility where hygiene and discretion matter."),
    dict(name="Singapore Zoo", sector="Attractions", img="fogging-close", blurb="Pest management in a wildlife environment, using approaches that limit harm to animals and the surrounding ecosystem."),
    dict(name="PSA", sector="Port & logistics", img="tp-misting", blurb="Pest management support across large-scale port and logistics operations."),
    dict(name="Indigo Hotel", sector="Hospitality", img="tp-fogging-2", blurb="Discreet, hospitality-grade pest management with minimal disruption to guests."),
    dict(name="Singapore Aviation Academy", sector="Education & aviation", img="team-site", blurb="Structured pest management programme for a training campus environment."),
    dict(name="Bedok Market 216", sector="Community", img="bedok-wide", blurb="Large-scale disinfection and environmental hygiene works at a hawker centre and market, supporting a cleaner, safer public space."),
]

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

def news_card(n):
    return f'<article class="news-card"><div class="img"><img src="assets/img/{n["img"]}.jpg" alt="{escape(n["title"])}" loading="lazy"></div><div class="body"><span class="kind">{n["kind"]}</span><h4>{escape(n["title"])}</h4><p>{n["text"]}</p></div></article>'


def cert_card(key, name, desc, land):
    return f'''<div class="cert" data-lightbox="certs" data-full="assets/certs/{key}.jpg" data-title="{escape(name)}" data-pdf="assets/certs/pdf/{key}.pdf"><div class="thumb {'land' if land else ''}"><img src="assets/certs/{key}.jpg" alt="{escape(name)}" loading="lazy"></div><span class="zoom">{I["zoom"]}</span><div class="meta"><b>{escape(name)}</b><span>{escape(desc)}</span></div></div>'''


def gallery(items, group):
    return '<div class="masonry">' + "".join(f'<a href="#" data-lightbox="{group}" data-full="assets/img/{img}.jpg" data-title="{escape(lbl)}"><img src="assets/img/{img}.jpg" alt="{escape(lbl)}" loading="lazy"><span class="lbl">{escape(lbl)}</span></a>' for img, lbl in items) + '</div>'


HOME_FAQ = [
    ("How much does pest control cost?", "The cost depends on factors such as the pest involved, property size, infestation severity, treatment method and whether follow-up treatments are required."),
    ("How long does a treatment take?", "Treatment duration depends on the pest, property and treatment approach. We can provide a more accurate estimate after understanding your requirements."),
    ("Do I need to leave my home during treatment?", "Requirements vary depending on the treatment method and area being treated. We will advise you on any necessary preparation and re-entry requirements."),
    ("How often should pest control be carried out?", "This depends on the pest and situation. Some problems may require a one-time treatment, while others may benefit from a scheduled programme."),
    ("Can you treat commercial premises?", "Yes. We provide pest-control solutions for various commercial environments, including F&B, construction, educational and other business premises."),
    ("I'm not sure what pest I have. Can you help?", "Yes. You can contact us or use our pest-identification feature to provide a photo and details of the problem."),
]

# ---------------------------------------------------------------- HOME

def home():
    pests_cards = [
        ("termites.html", "pest-termite", "Termite", "Termite protection solutions, including chemical treatment and physical barrier solutions where appropriate.", ""),
        ("mosquitoes.html", "pest-mosquito", "Mosquito", "Targeted mosquito-control solutions designed to address both adult mosquitoes and potential breeding sources.", ""),
        ("bedbugs.html", "pest-bedbug", "Bedbug", "Targeted bedbug treatment designed to address active infestations and help prevent recurrence.", ""),
        ("cockroaches.html", "pest-cockroach", "Cockroach", "Effective cockroach treatment for homes and businesses, with solutions tailored to the level and location of infestation.", ""),
        ("rodents.html", "pest-rodent", "Rodent", "Rodent management solutions focused on controlling activity and identifying potential entry and harbourage points.", ""),
        ("disinfection.html", "bedok-1", "Disinfection", "Professional disinfection services designed to help reduce harmful microorganisms on surfaces and high-contact areas.", ""),
    ]
    cards = "".join(
        f'''<a class="panel{" on" if i == 0 else ""}" href="{h}" data-panel="{i}"><img src="assets/img/{im}.jpg" alt="{t}" loading="lazy"><span class="veil"></span>
<span class="spine"><b>{t}</b></span>
<span class="open"><small>Pest control</small><b>{t}</b><span class="desc">{sub}</span><span class="go">Explore {t.lower()} control {I["arrow"]}</span></span></a>'''
        for i, (h, im, t, sub, tag) in enumerate(pests_cards))
    steps = [("Inspect & identify", "Understand the property, pest activity, harbourage, entry points and conducive conditions."), ("Prevent", "Address the conditions that allow pests to enter, survive and reproduce."), ("Monitor", "Track activity over time to understand infestation levels, movement and behaviour."), ("Targeted treatment", "The right solution to the right problem, at the right location: physical, exclusion, baiting or targeted chemical."), ("Evaluate & improve", "Review effectiveness and adapt: from reactive treatment towards long-term prevention.")]
    steps_html = "".join(f'<div class="step"><h4>{t}</h4><p>{d}</p></div>' for t, d in steps)
    proj = "".join(card_img("projects.html", p["img"], p["name"], p["blurb"], p["sector"]) for p in PROJECTS)
    # Slanted certificate wall. Columns run left to right; the right-of-centre
    # columns sit in the clear part of the image, so the strongest credentials go there.
    # Columns 0-1 fall behind the headline veil, so they carry the supporting documents.
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
    slant_cols = "".join(cols)
    logo_item = lambda f, n: f'<span class="item logo"><img src="assets/logos/clients/{f}.png" alt="{n}" title="{n}" loading="lazy"></span>'
    row1 = "".join(logo_item(f, n) for f, n in CLIENT_LOGOS_ROW1)
    row2 = "".join(logo_item(f, n) for f, n in CLIENT_LOGOS_ROW2)
    body = f'''
<section class="hero hero-seq" data-heroseq data-frames="121">
<canvas class="seq-canvas" aria-hidden="true"></canvas>
<div class="bg" style="background-image:url('assets/img/hero-home.jpg')"></div><div class="veil"></div>
<div class="seq-intro"><div class="container">
 <h1 class="display">What you can't see can cost you the most.</h1>
 <p class="lead">Termites work silently inside walls, floors and foundations, long before the damage shows.</p>
</div></div>
<div class="container seq-end"><div class="hero-grid">
 <div><h2 class="display" data-split>Protecting People. Protecting Properties. Protecting Communities.</h2>
  <p class="lead">Professional pest management and termite protection built around prevention, precision, safety and responsible innovation.</p>
  <div class="btn-row">{btn("WhatsApp us", WA, "wa", "wa")}{btn("Call us now", "tel:"+PHONE_TEL, "ghost", "phone")}{btn("Contact for quotation", "#enquiry", "lime")}</div></div>
</div></div></section>
</div></div>
<section class="section tight white" id="clients"><div class="container"><h2 class="h2 center logos-head">Projects We Have Done</h2></div>
<div class="marquee logos"><div class="track">{row1}</div></div>
<div class="marquee logos rev"><div class="track">{row2}</div></div></section>

<section class="section"><div class="container">
 <div class="section-head center-head"><div class="reveal"><div class="eyebrow">Pests we treat</div><h2 class="h2 line-reveal">Pests We Treat</h2></div></div>
 <div class="elastic reveal" data-elastic>{cards}</div>
 <p class="muted mt-3 center">Once the plan is confirmed, our team will implement the recommended pest management measures, target the source of the infestation, treat affected areas, and arrange follow-up monitoring to help provide lasting protection.</p>
</div></section>

<section class="section white"><div class="container split">
 <div class="frame parallax reveal left"><img src="assets/img/tp-training-2.jpg" alt="Pestimesh technician installing stainless-steel termite mesh"><div class="badge"><b>15<small>+</small></b><span>years protecting<br>Singapore properties</span></div></div>
 <div class="reveal right"><div class="eyebrow">Why Choose Pestimesh?</div><h2 class="h2">Trusted Pest Control Since 2011</h2>
  <p class="lead mt-2">With over a decade of experience, Pestimesh provides professional pest control solutions for homes, businesses and large-scale facilities across Singapore. We combine proven expertise with modern technology and responsible pest management practices to deliver effective, tailored solutions.</p>
  {checks(["<b>Established in 2011</b> — Over a decade of industry experience", "<b>Proven Track Record</b> — Experience serving major facilities and organisations", "<b>Professional &amp; Sustainable</b> — Effective solutions with a focus on responsible pest management"])}
  {link_arrow("Learn More About Us", "about.html")}</div>
</div></section>

<section class="section"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Our approach</div><h2 class="h2">Smarter pest management starts with prevention</h2></div><p class="lead reveal">Our Integrated Pest Management approach combines inspection, prevention, monitoring, targeted treatment and ongoing evaluation, prioritising the safety of people, properties and the environment.</p></div>
 <div class="steps reveal-stagger">{steps_html}</div>
 <div class="mt-3">{link_arrow("Explore our IPM approach", "ipm.html")}</div>
</div></section>

<section class="section dark"><div class="container split rev">
 <div class="frame reveal right"><img src="assets/img/mesh-roll.jpg" alt="Woven stainless-steel termite mesh"></div>
 <div class="reveal left"><div class="eyebrow">Physical protection</div><h2 class="h2">Stainless-steel mesh. Long-term pest prevention.</h2>
  <p class="lead mt-2">Not every pest problem needs chemicals. Our woven stainless-steel mesh is a physical barrier that stops termites and pests at the source, providing durable protection without relying solely on chemical treatment.</p>
  <div class="pills mt-3"><span class="pill">Pre-construction</span><span class="pill">Australian-sourced technology</span><span class="pill">ISO-certified scope</span><span class="pill">Reduces chemical use</span><span class="pill">Long service life</span></div>
  <div class="btn-row mt-4">{btn("Explore mesh protection", "mesh.html", "lime")}{btn("Termite services", "termites.html", "ghost")}</div></div>
</div></section>

<section class="section white"><div class="container">
 <div class="stats reveal-stagger">
  <div class="stat"><span class="ic">{I["clock"]}</span><div><b data-count="2011">0</b><span>Established</span><em>Singapore-grown since 2011</em></div></div>
  <div class="stat"><span class="ic">{I["award"]}</span><div><b>3<small>×</small></b><span>ISO certified</span><em>9001 · 14001 · 45001</em></div></div>
  <div class="stat"><span class="ic">{I["shield"]}</span><div><b data-count="0">0</b><span>Recordable injuries</span><em>FY2025, ISO 45001 aligned</em></div></div>
  <div class="stat"><span class="ic">{I["building"]}</span><div><b data-count="10" data-suffix="+">0</b><span>Landmark projects</span><em>Airports, courts, hotels, plants</em></div></div>
 </div>
</div></section>

<section class="section"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Projects</div><h2 class="h2">Trusted by Singapore's landmark facilities</h2></div><div class="hs-nav reveal"><button data-dir="prev" aria-label="Previous">{I["arrowl"]}</button><button data-dir="next" aria-label="Next">{I["arrow"]}</button></div></div></div>
 <div class="auto-slider projects" data-autoscroll><div class="track">{proj}</div></div>
 <div class="container">{link_arrow("View all projects", "projects.html")}</div></section>

<section class="section dark slant-section"><div class="slant-stage" data-slant><div class="slant-wall">{slant_cols}</div><div class="slant-veil"></div></div>
 <div class="container slant-copy"><div class="reveal left"><div class="eyebrow">Certifications &amp; compliance</div><h2 class="h2">Professional standards. Responsible practice.</h2><p class="lead mt-2">Our certifications, licences and compliance credentials are presented here for transparency. ISO 9001, 14001 and 45001 certified, bizSAFE Star and NEA-registered. Click any certificate to view it.</p><div class="btn-row mt-3">{btn("View all certifications", "certifications.html", "lime")}</div></div></div>
</section>

<section class="section"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Sustainability &amp; ESG</div><h2 class="h2">Responsible pest management for a more sustainable future</h2></div><p class="lead reveal">Our first GRI-referenced sustainability report sets a FY2025 baseline across environment, social and governance.</p></div>
 <div class="pillars reveal-stagger">
  <div class="pillar"><span class="big">E</span><h3 class="h3">Environment</h3><p>Prevention before treatment, physical protection with stainless-steel mesh, and responsible, targeted intervention. Emissions and water tracked from a FY2025 baseline.</p></div>
  <div class="pillar"><span class="big">S</span><h3 class="h3">Social</h3><p>Zero recordable injuries in FY2025. Training, PPE and toolbox meetings for every technician. Dengue talks, Bedok Market hygiene works and tchoukball sponsorship for the community.</p></div>
  <div class="pillar"><span class="big">G</span><h3 class="h3">Governance</h3><p>NEA compliance, ISO-aligned processes, zero corruption incidents and 24/7 whistleblowing access for every employee.</p></div>
 </div>
 <div class="mt-3">{link_arrow("Explore Sustainability & ESG", "sustainability.html")}</div>
</div></section>

<section class="section white"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">News &amp; community</div><h2 class="h2">What we're doing and contributing</h2></div>{link_arrow("All news & community", "news.html")}</div>
 <div class="grid grid-3 reveal-stagger">{"".join(news_card(n) for n in NEWS[:3])}</div>
</div></section>

<section class="section"><div class="container split" style="align-items:start">
 <div class="reveal left"><div class="eyebrow">FAQs</div><h2 class="h2">Frequently asked questions</h2><p class="lead mt-2">For pest-specific questions, see each service page.</p><div class="mt-3">{link_arrow("View all FAQs", "faq.html")}</div></div>
 <div class="reveal right">{faq(HOME_FAQ)}</div>
</div></section>
{cta_band("Don't Let Pests Take Over Your Space.", "Whether it's a single pest sighting or an ongoing infestation, getting the right solution early can help prevent the problem from becoming bigger. Tell us what you're experiencing and let our team recommend the appropriate next step.")}'''
    return "index.html", page("index.html", "Pest Control & Termite Protection Singapore", "Pestimesh Pte Ltd — NEA-registered pest management and termite protection specialists in Singapore since 2011. IPM, stainless-steel mesh, mosquito, rodent, bedbug and cockroach control.", body)

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
<section class="section dark"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Vision &amp; mission</div><h2 class="h2">To be the leader in the pest control industry</h2></div><p class="lead reveal">Providing the best services and quality solutions, through excellent, efficient and innovative pest control.</p></div>
 <div class="grid grid-4 reveal-stagger">
  <div class="card dark glow"><div class="num">a</div><h4>Protect</h4><p>Protecting the health and properties of customers, friends and neighbours.</p></div>
  <div class="card dark glow"><div class="num">b</div><h4>Serve</h4><p>Providing an unparalleled customer service experience.</p></div>
  <div class="card dark glow"><div class="num">c</div><h4>Respect</h4><p>Modelling courtesy and respect in every community we serve.</p></div>
  <div class="card dark glow"><div class="num">d</div><h4>Value</h4><p>Valuing our employees the same way we value our customers.</p></div>
 </div>
</div></section>
<section class="section"><div class="container">
 <div class="section-head"><div class="reveal"><div class="eyebrow">Leadership</div><h2 class="h2">People behind the protection</h2></div></div>
 <div class="grid grid-2">
  <div class="quote reveal left"><p>“We believe the future of pest management is built on smarter, more sustainable solutions. Through Integrated Pest Management, we focus on prevention, precision and responsible pest control — protecting our communities, environments and future.”</p><footer><img src="assets/img/winnie.jpg" alt="Winnie Seng"><div><b>Winnie Seng</b><span>Managing Director, Pestimesh</span></div></footer></div>
  <div class="quote reveal right"><p>“Safety is the foundation of every project we deliver. Through prevention, precision, innovation and responsible pest management, we protect our people, customers, environment and communities while upholding quality and integrity.”</p><footer><div class="ic" style="width:56px;height:56px;border-radius:50%;background:var(--teal-900);color:var(--lime);display:grid;place-items:center">{I["shield"]}</div><div><b>Vincent Tan</b><span>Project Director, Pestimesh</span></div></footer></div>
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
{cta_band("Have a Pest Problem?", "Whether you're dealing with termites, bedbugs, mosquitoes, cockroaches or other pests, our team is here to help. Contact Pestimesh today for professional pest control services.")}'''
    return "about.html", page("about.html", "About Us", "Established in 2011, Pestimesh Pte Ltd is an NEA-registered pest management and termite protection specialist in Singapore.", body)

# ---------------------------------------------------------------- SERVICES OVERVIEW

def services():
    imgs = {"ipm.html": "tp-training", "termites.html": "hero-termite", "mosquitoes.html": "tp-fogging", "bedbugs.html": "tp-misting", "cockroaches.html": "bedok-wide", "rodents.html": "tp-building", "disinfection.html": "bedok-1", "mesh.html": "mesh-roll", "termite-baiting.html": "mesh-rebar"}
    cards = "".join(card_img(h, imgs[h], n, d, "Treatment & protection" if h in ("mesh.html", "termite-baiting.html") else "Pest control") for h, n, d, _ in SERVICES)
    envs = [("Residential", "Protecting homes and families from common household pests.", "home"), ("Commercial", "Practical pest prevention and ongoing management for businesses.", "building"), ("Hotels & hospitality", "Managing pest risks around guest experience and operations.", "heart"), ("Industrial & facilities", "Structured programmes for complex operating environments.", "layers"), ("Construction", "Pre-construction soil treatment and stainless-steel mesh for developers.", "mesh"), ("Public & institutional", "Where safety, hygiene and continuity of operations matter.", "users")]
    body = page_hero("Services", "Pest control and protection, tailored to your property.", "From homes and commercial properties to construction sites and national facilities, every programme starts with an inspection and a plan built around prevention.", "fogging-wide", "Our services")
    body += f'''
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">All services</div><h2 class="h2">Pest control &amp; treatment methods</h2></div><p class="lead reveal">Prevention-led programmes, targeted treatment and physical protection, delivered by an NEA-registered, ISO-certified team.</p></div>
<div class="grid grid-3 reveal-stagger">{cards}</div></div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Environments</div><h2 class="h2">IPM across different environments</h2></div></div>
<div class="grid grid-3 reveal-stagger">{"".join(f'<div class="card dark glow"><div class="ic">{I[ic]}</div><h4>{t}</h4><p>{d}</p></div>' for t, d, ic in envs)}</div></div></section>
{cta_band("Not sure which service you need?", "Send us a photo and a short description. Our team will identify the pest and recommend the right approach.")}'''
    return "services.html", page("services.html", "Services", "Pest control, termite protection, mosquito control, disinfection and stainless-steel mesh services in Singapore.", body)

# ---------------------------------------------------------------- IPM

def ipm():
    steps = [("Inspect & Identify", "We begin by understanding the property and the pest situation. Our team assesses areas of activity, potential harbourage, entry points, conducive conditions and other factors that may contribute to pest presence. Accurate identification allows us to determine the appropriate management strategy rather than applying a one-size-fits-all solution."), ("Prevent", "Where possible, we address the conditions that allow pests to enter, survive and reproduce: potential pest entry points, food and water sources, harbourage areas, structural gaps and openings, sanitation and housekeeping factors, and environmental conditions that encourage pest activity. Prevention is the first line of defence."), ("Monitor", "Effective pest management requires more than a single treatment. Monitoring helps us understand pest activity over time and identify changes in infestation levels, movement and behaviour. Where appropriate, monitoring and detection technologies can support more precise identification of pest activity."), ("Targeted Treatment", "When intervention is required, we select the appropriate control method based on the pest, site conditions and level of activity. Depending on the situation, this may include physical control, exclusion, baiting, monitoring or targeted chemical treatment. Our objective is to apply the right solution to the right problem, at the right location."), ("Evaluate & Improve", "Pest management is an ongoing process. We review pest activity and treatment effectiveness to determine whether further action, preventive measures or adjustments are required. This continuous approach helps move pest management from reactive treatment towards long-term prevention and control.")]
    combo = [("Inspection", "Understanding where and why pest activity is occurring.", "search"), ("Sanitation & housekeeping", "Reducing food, water and harbourage opportunities.", "spray"), ("Exclusion & proofing", "Physical protection and sealing potential entry points.", "mesh"), ("Monitoring", "Tracking activity to support informed decisions.", "eye"), ("Targeted treatment", "Appropriate control measures when intervention is required.", "target"), ("Follow-up", "Reviewing results and adapting the strategy.", "refresh")]
    why = [("More prevention", "Addressing the conditions that contribute to pest activity rather than only visible pests."), ("More precision", "Inspection, monitoring and the right control methods to target the actual problem."), ("Greater safety focus", "People, property and site requirements shape the strategy."), ("Long-term protection", "Treatment combined with preventive measures reduces recurring activity."), ("Responsible management", "Physical, preventive and targeted measures rather than routine chemical intervention.")]
    body = page_hero('<a href="services.html">Services</a><span>/</span>Integrated Pest Management', "Smarter pest management starts with prevention.", "Effective pest management is not simply about treating pests when they appear. It is about understanding why pests are present, addressing the conditions that attract them, and preventing recurring activity.", "tp-training", "Integrated Pest Management")
    body += f'''
<section class="section"><div class="container split"><div class="reveal left"><div class="eyebrow">What Is Integrated Pest Management?</div><h2 class="h2">A prevention-led approach to pest management that looks beyond the immediate pest problem.</h2></div>
<div class="reveal right"><p class="lead">Instead of relying solely on routine chemical treatments, IPM considers the wider conditions that contribute to pest activity — including food sources, water, shelter, entry points, harbourage areas and property conditions.</p><p class="mt-2 muted">By addressing the underlying causes and using the most appropriate control measures, we aim to achieve effective and sustainable pest management with targeted intervention rather than unnecessary treatment.</p><p class="mt-2"><b>Protecting People. Protecting Properties. Protecting Communities.</b></p></div></div></section>
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Our IPM Approach</div><h2 class="h2">Our IPM Approach</h2></div></div>
<div class="steps reveal-stagger">{"".join(f'<div class="step"><h4>{t}</h4><p>{d}</p></div>' for t, d in steps)}</div></div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Prevention Before Treatment</div><h2 class="h2">Integrated Solutions, Not One-Size-Fits-All Treatments</h2></div><p class="lead reveal">A key principle of our IPM approach is to address the source of the problem wherever practical. Pest activity can often be influenced by the conditions around a property. By identifying and addressing these conditions, we can reduce opportunities for pests to enter, feed, harbour and reproduce. Every property is different. Our IPM approach allows the pest management strategy to be adapted according to property type and usage, pest species, level and location of activity, environmental conditions, structural vulnerabilities, operational requirements and safety considerations.</p></div>
<div class="grid grid-3 reveal-stagger">{"".join(f'<div class="card dark glow"><div class="ic">{I[ic]}</div><h4>{t}</h4><p>{d}</p></div>' for t, d, ic in combo)}</div></div></section>
<section class="section"><div class="container split"><div class="frame parallax reveal left"><img src="assets/img/mesh-rebar.jpg" alt="Stainless-steel mesh collars installed around pipe penetrations"></div>
<div class="reveal right"><div class="eyebrow">Physical Protection as Part of IPM</div><h2 class="h2">Physical Protection as Part of IPM</h2><p class="lead mt-2">Where appropriate, physical prevention can play an important role in reducing pest access. Pestimesh's woven stainless-steel mesh protection provides a long-term physical barrier that can help prevent pest entry without relying solely on chemical treatments. By focusing on exclusion and prevention, physical protection can form an important part of a broader integrated pest management strategy.</p><div class="mt-3">{link_arrow("Explore stainless-steel mesh protection", "mesh.html")}</div>
<h3 class="h3 mt-5">Precision Through Technology</h3><p class="mt-1 muted">Technology can further support a prevention-led approach by helping our team identify pest activity more accurately. For termite inspections, Pestimesh uses the Termatrac T3i, which combines radar, moisture detection and thermal sensing to help detect and track termite activity. By improving visibility of pest activity, technology can support more informed decisions and targeted intervention.</p><div class="mt-2">{link_arrow("Explore technology & innovation", "technology.html")}</div></div></div></section>
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Why IPM</div><h2 class="h2">Why Choose an IPM Approach?</h2></div></div>
<div class="grid grid-3 reveal-stagger">{"".join(f'<div class="card glow"><div class="num">0{i+1}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(why))}<div class="card lime"><div class="ic">{I["leaf"]}</div><h4>Our Approach to Responsible Pest Management</h4><p>IPM is an important part of our commitment to responsible pest management. By prioritising prevention, physical protection, monitoring and targeted intervention, we aim to manage pest risks effectively while reducing unnecessary intervention wherever practical. This approach supports our broader commitment to safety, sustainability and responsible growth.</p></div></div></div></section>
{cta_band("Start with a site assessment.", "Every IPM programme begins with an inspection. Tell us about your property and we'll recommend a practical, targeted plan.")}'''
    return "ipm.html", page("ipm.html", "Integrated Pest Management", "Pestimesh's prevention-led Integrated Pest Management approach: inspect, prevent, monitor, treat and evaluate.", body)

# ---------------------------------------------------------------- DISINFECTION

def disinfection():
    fq = [("What is professional disinfection?", "A service designed to reduce harmful microorganisms on relevant surfaces and high-contact areas."), ("Is disinfection the same as cleaning?", "No. Cleaning removes dirt and contaminants; disinfection reduces harmful microorganisms on treated surfaces."), ("How often should disinfection be carried out?", "It depends on the property, its usage and your requirements. Our team can advise based on the situation."), ("Can you disinfect offices and commercial premises?", "Yes. We provide disinfection for homes, offices, commercial premises and other facilities."), ("Do I need to prepare the area?", "Preparation varies by area and service. Our team advises on any necessary preparation beforehand."), ("How long does disinfection take?", "It depends on the size of the property and scope of service. We provide an estimate after understanding your requirements.")]
    body = page_hero('<a href="services.html">Services</a><span>/</span>Disinfection &amp; Hygiene', "Professional disinfection for cleaner, more hygienic environments.", "Cleaner environment. Professional protection. We help reduce harmful microorganisms on surfaces and high-contact areas in homes, workplaces, commercial premises and shared community spaces.", "bedok-wide", "Disinfection & Hygiene")
    body += f'''
<section class="section"><div class="container split"><div class="reveal left"><div class="eyebrow">Why Is Disinfection Important?</div><h2 class="h2">Why Is Disinfection Important?</h2><p class="lead mt-2">Surfaces and high-contact areas can be exposed to microorganisms through regular use and contact. Regular cleaning is an important part of maintaining hygiene, while professional disinfection can provide an additional level of environmental hygiene where required.</p><p class="muted mt-2">Disinfection can be particularly relevant in environments where people frequently share or interact with common spaces and surfaces. Our professional services help reduce harmful microorganisms on treated surfaces and high-contact areas, supporting a cleaner environment for occupants, customers and employees.</p><h3 class="h3 mt-4">Areas That May Require Attention</h3>
{checks(["High-contact surfaces and shared areas", "Common-use facilities and frequently used surfaces", "Areas identified during assessment", "Residential, office, commercial, F&B and public facilities"])}</div>
<div class="frame parallax reveal right"><img src="assets/img/bedok-1.jpg" alt="Pestimesh disinfection team at Bedok Market 216"><div class="badge"><b>216</b><span>Bedok Market<br>large-scale works</span></div></div></div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Why Choose Professional Disinfection?</div><h2 class="h2">Why Choose Professional Disinfection?</h2></div></div>
<div class="grid grid-4 reveal-stagger"><div class="card dark glow"><div class="ic">{I["users"]}</div><h4>Professional Service</h4><p>Our team provides professional disinfection services for residential, commercial and other facilities.</p></div><div class="card dark glow"><div class="ic">{I["target"]}</div><h4>Targeted Approach</h4><p>We focus on relevant surfaces and high-contact areas based on the requirements of the property.</p></div><div class="card dark glow"><div class="ic">{I["building"]}</div><h4>Suitable for Different Environments</h4><p>Our services can be adapted for homes, offices, commercial premises and other facilities.</p></div><div class="card dark glow"><div class="ic">{I["refresh"]}</div><h4>Supports Ongoing Hygiene</h4><p>Professional disinfection can form part of a broader approach to maintaining a cleaner and more hygienic environment.</p></div></div></div></section>
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Case study</div><h2 class="h2">Bedok Market 216</h2></div><p class="lead reveal">Our team carried out disinfection and environmental hygiene works at Bedok Market 216, helping the market reopen with a cleaner, safer environment for operators and the public. The works were covered by The Straits Times and Lianhe Zaobao and recognised by East Coast Town Council.</p></div>
{gallery([("bedok-wide","Disinfection in progress"),("bedok-2","The Pestimesh team"),("news-2","Lianhe Zaobao coverage"),("bedok-3","With community leaders"),("bedok-5","On-site briefing"),("news-1","The Straits Times coverage")], "bedok")}</div></section>
<section class="section"><div class="container split" style="align-items:start"><div class="reveal left"><div class="eyebrow">FAQs</div><h2 class="h2">Disinfection questions</h2></div><div class="reveal right">{faq(fq)}</div></div></section>
{cta_band("Cleaner environment. Professional protection.", "Tell us about your premises and we'll recommend a disinfection approach suited to your requirements.", "bedok-wide")}'''
    return "disinfection.html", page("disinfection.html", "Disinfection & Hygiene", "Professional disinfection services for homes, offices, commercial premises and public facilities in Singapore.", body)

# ---------------------------------------------------------------- MESH

def mesh():
    fq = [("What is stainless-steel mesh used for?", "It is a physical barrier that prevents pests from entering through suitable openings and vulnerable areas, especially termites in construction."), ("Does stainless-steel mesh replace pest treatment?", "Not necessarily. Mesh is primarily a prevention and exclusion measure. Where active infestation exists, other measures may also be required."), ("Is stainless-steel mesh environmentally friendly?", "Physical exclusion reduces reliance on chemical intervention, water and chemical consumption where appropriate. Benefits depend on the application and overall programme."), ("How long does mesh protection last?", "Service life depends on installation, location, environmental conditions and site factors. Stainless steel is designed for long-term durability.")]
    apps = ["Building openings", "Gaps and access points", "Ventilation-related openings", "Vulnerable structural areas", "Other locations where pest exclusion is appropriate"]
    body = page_hero('<a href="services.html">Services</a><span>/</span>Stainless-Steel Mesh Protection', "Physical protection. Long-term pest prevention.", "Not every pest problem needs to be solved with chemical treatment. Pestimesh's woven stainless-steel mesh is a physical barrier that prevents termites and pests from entering vulnerable areas of a property, at the source.", "mesh-roll", "Stainless-Steel Mesh")
    body += f'''
<section class="section"><div class="container split"><div class="reveal left"><div class="eyebrow">Prevent Entry. Protect Your Property.</div><h2 class="h2">What Is Stainless-Steel Mesh Protection?</h2><p class="lead mt-2">Stainless-steel mesh is a physical pest exclusion solution designed to block potential pest entry points. Rather than treating pests after they have entered a building, physical exclusion focuses on preventing access in the first place.</p><p class="muted mt-2">The mesh can be used to protect suitable openings and vulnerable areas where pests may otherwise gain access. This approach is particularly relevant where long-term physical protection is preferred or where exclusion forms part of an Integrated Pest Management programme.</p>
<p class="muted mt-2">Pestimesh has developed specialised expertise in physical anti-termite protection using stainless-steel termite mesh systems, with Australian-sourced mesh technology and techniques refined for Singapore's construction industry. Our ISO 9001, 14001 and 45001 certifications explicitly cover the provision of anti-termite woven stainless-steel mesh.</p></div>
<div class="grid" style="gap:14px"><div class="frame reveal right"><img src="assets/img/mesh-collar.jpg" alt="Stainless-steel mesh collar" style="aspect-ratio:16/10"></div><div class="frame reveal right"><img src="assets/img/mesh-rebar.jpg" alt="Mesh collars fitted to pipe penetrations before concrete pour" style="aspect-ratio:16/10"></div></div></div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Why Choose Physical Pest Protection?</div><h2 class="h2">Why Choose Physical Pest Protection?</h2></div></div>
<div class="grid grid-3 reveal-stagger">
<div class="card dark glow"><div class="ic">{I["shield"]}</div><h4>Prevents Pest Entry</h4><p>A properly installed physical barrier can help prevent pests from accessing protected areas through vulnerable openings.</p></div>
<div class="card dark glow"><div class="ic">{I["clock"]}</div><h4>Long-Term Protection</h4><p>Unlike treatments that address an infestation at a particular point in time, physical exclusion is designed to provide ongoing protection.</p></div>
<div class="card dark glow"><div class="ic">{I["leaf"]}</div><h4>Reduces Reliance on Chemical Treatment</h4><p>Where appropriate, physical barriers can help reduce the need to rely solely on repeated chemical intervention.</p></div>
<div class="card dark glow"><div class="ic">{I["target"]}</div><h4>Prevention-Led</h4><p>Physical exclusion addresses one of the fundamental causes of pest problems — access.</p></div>
<div class="card dark glow"><div class="ic">{I["layers"]}</div><h4>Supports Integrated Pest Management</h4><p>Mesh protection can form part of a broader IPM strategy combining inspection, prevention, monitoring and targeted treatment.</p></div>
<div class="card lime"><div class="ic">{I["award"]}</div><h4>Certified scope</h4><p>Our ISO management systems are certified for anti-termite woven stainless-steel mesh.</p></div></div>
<div class="flow mt-4"><span>Inspection</span><i></i><span>Prevention</span><i></i><span>Exclusion</span><i></i><span>Monitoring</span><i></i><span>Targeted treatment</span></div></div></section>
<section class="section white"><div class="container split rev"><div class="frame parallax reveal right"><img src="assets/img/tp-training-2.jpg" alt="Installing stainless-steel termite mesh on a construction site"></div>
<div class="reveal left"><div class="eyebrow">Applications</div><h2 class="h2">Where Can Stainless-Steel Mesh Be Used?</h2><p class="lead mt-2">The suitability of mesh protection depends on the structure and potential pest entry points identified during assessment. Potential applications may include:</p>{checks(apps)}<p class="muted">Our team can assess the property and determine whether stainless-steel mesh is suitable for the specific application.</p>
<h3 class="h3 mt-4">Is Stainless-Steel Mesh Right for Your Property?</h3><p class="muted mt-1">Every property is different. The suitability of mesh protection depends on factors such as the type of pest, potential entry points, building structure, location and accessibility, existing pest activity and long-term protection requirements. A professional site assessment can determine whether physical exclusion is appropriate.</p></div></div></section>
<section class="section"><div class="container split" style="align-items:start"><div class="reveal left"><div class="eyebrow">FAQs</div><h2 class="h2">Mesh protection questions</h2><p class="lead mt-2">A more responsible approach to pest protection, relevant to our focus on prevention, precision, safety and responsible innovation.</p></div><div class="reveal right">{faq(fq)}</div></div></section>
{cta_band("Planning a construction project?", "Talk to us early. Stainless-steel mesh is most effective when designed into the build before slabs are poured.", "tp-building")}'''
    return "mesh.html", page("mesh.html", "Stainless-Steel Mesh Protection", "Woven stainless-steel termite mesh: a physical, long-term pest barrier for construction and buildings in Singapore.", body)

# ---------------------------------------------------------------- TERMITE BAITING

def baiting():
    fq = [("Does termite baiting eliminate termites immediately?", "Baiting is a monitoring and management process rather than an immediate treatment. Colony elimination typically takes 2–12 weeks depending on colony size, with most cases around 6–8 weeks."), ("Is termite baiting suitable for every property?", "Not necessarily. A professional inspection determines the appropriate termite management approach."), ("How often are bait stations checked?", "Monitoring frequency depends on the property, system used and level of termite activity."), ("Can baiting be combined with other treatments?", "Yes. Baiting may form part of a broader programme alongside soil treatment, corrective treatment or stainless-steel mesh."), ("Do I need baiting if I don't see termites?", "Not necessarily. Termites remain concealed, which is why professional inspection helps identify potential activity and risks.")]
    steps = [("Inspection", "We first assess the property for signs of termite activity and potential areas of concern."), ("Bait Placement", "Where appropriate, bait stations or suitable baiting systems are positioned based on the property's requirements and identified termite activity."), ("Monitoring", "The baiting system is monitored to assess termite activity and determine whether further action is required."), ("Ongoing Management", "Termite baiting is an ongoing process. Monitoring and follow-up help our team assess activity and adjust the management approach where necessary.")]
    body = page_hero('<a href="services.html">Services</a><span>/</span>Termite Baiting', "Targeted termite management with ongoing monitoring.", "Detect. Monitor. Manage. Protect. Termite baiting uses termite behaviour to manage active colonies, with inspection, monitoring and follow-up forming an important part of the process.", "hero-termite", "Termite Baiting")
    body += f'''
<section class="section"><div class="container split"><div class="reveal left"><div class="eyebrow">What Is Termite Baiting?</div><h2 class="h2">What Is Termite Baiting?</h2><p class="lead mt-2">Termite baiting involves placing suitable termite bait systems in locations where termite activity can be detected. Foraging termites interact with the bait, allowing activity to be monitored and managed as part of an ongoing termite control programme.</p><p class="muted mt-2">Unlike a treatment focused only on a visible area of termite activity, baiting can be incorporated into a broader strategy aimed at managing termite activity over time.</p></div>
<div class="frame parallax reveal right"><img src="assets/img/hero-termite.jpg" alt="Subterranean termites in a tunnel"><div class="badge"><b>6–8<small> wks</small></b><span>typical colony<br>elimination</span></div></div></div></section>
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">How Termite Baiting Works</div><h2 class="h2">How Termite Baiting Works</h2></div></div>
<div class="steps reveal-stagger" style="grid-template-columns:repeat(4,1fr)">{"".join(f'<div class="step"><h4>{t}</h4><p>{d}</p></div>' for t, d in steps)}</div></div></section>
<section class="section dark"><div class="container split"><div class="reveal left"><div class="eyebrow">Why Consider Termite Baiting?</div><h2 class="h2">Why Consider Termite Baiting?</h2>{checks(["<b>Targeted Approach</b> — Baiting focuses on areas where termite activity is identified or suspected.", "<b>Monitoring-Based</b> — Regular monitoring helps track termite activity rather than relying solely on a one-time treatment.", "<b>Suitable for Ongoing Management</b> — Baiting can form part of a longer-term termite management programme.", "<b>Works Alongside Other Solutions</b> — Depending on the property and situation, baiting may be combined with other termite protection measures."])}</div>
<div class="reveal right"><h3 class="h3">Baiting as part of IPM</h3><div class="flow"><span>Inspection</span><i></i><span>Monitoring</span><i></i><span>Baiting</span><i></i><span>Physical protection</span><i></i><span>Treatment</span></div><p class="lead">The appropriate combination depends on the property, termite activity and site conditions.</p>
<h3 class="h3 mt-4">Detection &amp; technology</h3><p class="mt-1" style="color:rgba(255,255,255,.75)">Pestimesh uses the Termatrac T3i, combining radar, moisture and thermal sensing, to help decide where monitoring or treatment is appropriate.</p><div class="mt-2">{btn("Explore technology & innovation", "technology.html", "lime")}</div></div></div></section>
<section class="section"><div class="container split" style="align-items:start"><div class="reveal left"><div class="eyebrow">FAQs</div><h2 class="h2">Termite baiting questions</h2></div><div class="reveal right">{faq(fq)}</div></div></section>
{cta_band("Suspect termite activity?", "Termites stay hidden. Book an inspection with Termatrac detection and let us recommend the right programme.")}'''
    return "termite-baiting.html", page("termite-baiting.html", "Termite Baiting", "Termite baiting systems with inspection, monitoring and ongoing management in Singapore.", body)

# ---------------------------------------------------------------- PROJECTS

def projects():
    feat = "".join(card_img("#enquiry", p["img"], p["name"], p["blurb"], p["sector"]) for p in PROJECTS[:5])
    rest = "".join(card_img("#enquiry", p["img"], p["name"], p["blurb"], p["sector"], "wide") for p in PROJECTS[5:])
    wall = "".join(f'<div>{p["name"]}<small>{p["sector"]}</small></div>' for p in PROJECTS)
    body = page_hero("Projects", "Trusted by Singapore's landmark facilities.", "Our portfolio includes pest control and termite-related projects for major facilities, and pest management programmes for developers and project teams throughout the construction phase of condominium and commercial developments.", "tp-building", "Projects")
    body += f'''
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Featured projects</div><h2 class="h2">Where we've worked</h2></div><p class="lead reveal">From airports and courts to hotels, plants and community markets, each programme is built around the site's risks, operations and safety requirements.</p></div>
<div class="proj-feature reveal-stagger">{feat}</div>
<div class="grid grid-3 mt-3 reveal-stagger">{rest}</div></div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Client portfolio</div><h2 class="h2">Facilities we've protected</h2></div></div><div class="logo-wall reveal-stagger">{wall}</div></div></section>
<section class="section white"><div class="container split"><div class="frame parallax reveal left"><img src="assets/img/tp-training.jpg" alt="Construction-phase termite protection"></div>
<div class="reveal right"><div class="eyebrow">Construction partners</div><h2 class="h2">Pest management through the construction phase</h2><p class="lead mt-2">We support developers and project management teams with pest management programmes throughout the construction phase of condominium and commercial property developments: pre-construction soil treatment, stainless-steel mesh installation, mosquito control on site and hand-over protection.</p>
{checks(["Pre-construction anti-termite soil treatment with 5-year warranty", "Woven stainless-steel mesh at slab penetrations and soil-contact areas", "On-site mosquito misting, larviciding and thermal fogging", "Toolbox briefings, risk assessments and ISO 45001-aligned safe work"])}
{btn("Discuss your project", "#enquiry", "dark")}</div></div></section>
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">On site</div><h2 class="h2">Treatment in action</h2></div></div>
{gallery([("tp-fogging","Thermal fogging on site"),("tp-misting","Water-based misting"),("tp-larviciding","Larviciding treatment"),("tp-fogging-2","Fogging a basement level"),("tp-training-2","Stainless-steel mesh installation"),("fogging-wide","Site-wide mosquito control")], "site")}</div></section>
{cta_band("Planning a programme for your facility?", "Tell us about the site and its operating requirements. We'll propose a practical, targeted pest management programme.")}'''
    return "projects.html", page("projects.html", "Projects", "Pestimesh projects: Changi Airport T2, ICA, Singapore Zoo, Banyan Tree, Family Justice Courts, PUB Tuas, PSA, Indigo Hotel, Singapore Aviation Academy, Bedok Market 216.", body)

# ---------------------------------------------------------------- CERTIFICATIONS

def certifications():
    cats = list(CERTS.keys())
    all_cards = "".join(cert_card(*c).replace('<div class="cert" ', f'<div class="cert" data-cat="{k}" ', 1) for k, v in CERTS.items() for c in v)
    total = sum(len(v) for v in CERTS.values())
    filters = f'<button class="on" data-filter="all">All certificates <span>{total}</span></button>' + "".join(f'<button data-filter="{k}">{k} <span>{len(v)}</span></button>' for k, v in CERTS.items())
    safety = ["People and occupants", "Site conditions", "Appropriate treatment methods", "Product and chemical handling", "Application requirements", "Follow-up and monitoring", "Minimising disruption to operations"]
    docs = ["Service records", "Inspection findings", "Treatment details", "Monitoring information", "Recommendations", "Follow-up requirements"]
    body = page_hero("Certifications &amp; Compliance", "Professional Standards. Responsible Practice.", "At Pestimesh, professional pest management means more than effective treatment. We believe responsible pest management requires appropriate training, regulatory compliance, safe working practices and proper handling of pest management products and equipment. Our commitment is to operate professionally and responsibly while protecting people, properties and the environments in which we work.", "team-site", "Certifications & Compliance")
    body += f'''
<section class="section" id="credentials"><div class="container">
 <div class="section-head center-head"><div class="reveal"><h2 class="h2">Our Certifications &amp; Credentials</h2><p class="lead mt-2">Our certifications, licences and compliance credentials are presented here for transparency. Click any certificate to view it in full or open the original PDF.</p></div></div>
 <div class="filters center reveal">{filters}</div>
 <div class="cert-grid reveal-stagger" id="certgrid">{all_cards}</div>
 <p class="center muted small mt-4" data-count-label>Showing all {total} credentials</p>
</div></section>
<section class="section white"><div class="container">
 <div class="split"><div class="reveal left"><h2 class="h2">NEA-registered. ISO-certified. bizSAFE Star.</h2><p class="lead mt-2">Pestimesh operates with consideration for applicable Singapore regulatory and industry requirements relevant to professional pest management. Our technicians and service practices are aligned with the requirements applicable to the work being carried out.</p>
  <div class="cert-strip mt-3"><div class="cert-logo"><img src="assets/logos/nea.png" alt="National Environment Agency"><span>NEA Vector Control Operator<br><small style="font-family:var(--font-body);text-transform:none;color:var(--muted)">Reg. NEA201114018K · valid to 08.04.2028</small></span></div>
  <div class="cert-logo"><img src="assets/logos/bizsafe-star.png" alt="bizSAFE Star"><span>bizSAFE Star<br><small style="font-family:var(--font-body);text-transform:none;color:var(--muted)">WSH Council · valid to 03.07.2027</small></span></div></div></div>
  <div class="reveal right"><div class="iso-cards">
   <div class="iso-card"><span class="ring">{I["award"]}</span><b>ISO 9001<small>:2015</small></b><span class="scope">Quality Management System</span></div>
   <div class="iso-card"><span class="ring">{I["leaf"]}</span><b>ISO 14001<small>:2015</small></b><span class="scope">Environmental Management System</span></div>
   <div class="iso-card"><span class="ring">{I["shield"]}</span><b>ISO 45001<small>:2018</small></b><span class="scope">Occupational Health &amp; Safety Management System</span></div>
  </div>
  <div class="accred"><div class="plates"><img src="assets/logos/saara.png" alt="SAARA Management System Private Limited"><img src="assets/logos/uaf.png" alt="United Accreditation Foundation"><img src="assets/logos/iaf.png" alt="IAF Multilateral Recognition Arrangement"></div>
   <p class="small muted">Certified by SAARA Management System Private Limited, accredited by the United Accreditation Foundation (UAF), accreditation no. CB-MS-2809, a signatory of the IAF Multilateral Recognition Arrangement. Scope: provision of pest control services &amp; anti-termite woven stainless-steel mesh.</p></div></div></div></div></section>
<section class="section dark" id="safety"><div class="container"><div class="grid grid-3">
<div class="reveal"><div class="eyebrow">Professional Competence</div><h3 class="h3">Knowledge, experience and proper application</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Effective pest management depends on knowledge, experience and proper application. Our team works across residential, commercial and large-scale facilities and applies practical pest management methods according to the pest, property and site requirements.</p></div>
<div class="reveal"><div class="eyebrow">Safe Pest Management</div><h3 class="h3">Safety is an important part of our approach.</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Our service planning considers:</p>{checks(safety)}<p class="small" style="color:rgba(255,255,255,.6)">The appropriate safety measures depend on the service and property.</p></div>
<div class="reveal"><div class="eyebrow">Documentation &amp; Service Records</div><h3 class="h3">Professional programmes, properly documented</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Depending on the scope of the programme, this may include:</p>{checks(docs)}<p class="small" style="color:rgba(255,255,255,.6)">These records can help customers understand the pest management programme and track ongoing activity.</p></div></div>
<div class="divider" style="background:rgba(255,255,255,.12)"></div>
<div class="split"><div class="reveal left"><h3 class="h3">Responsible Product &amp; Chemical Use</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Where chemical treatment is required, responsible application is an important part of professional pest management. Our approach is to select appropriate treatment methods based on the pest, site conditions and requirements, rather than treating every situation in the same way. This supports our wider prevention-led Integrated Pest Management approach.</p></div><div class="reveal right"><h3 class="h3">Our Commitment</h3><p class="mt-2" style="color:rgba(255,255,255,.75)">Pestimesh is committed to maintaining professional standards across our services while continuing to improve our knowledge, processes and practices.</p></div></div></div></section>
{cta_band("Need documentation for your programme?", "We provide service records, inspection findings and monitoring information to support your compliance requirements.")}'''
    return "certifications.html", page("certifications.html", "Certifications & Compliance", "Pestimesh certifications: ISO 9001, ISO 14001, ISO 45001, bizSAFE Star, NEA registration, awards, memberships and letters of appreciation.", body)

# ---------------------------------------------------------------- SUSTAINABILITY

def sustainability():
    sdg = "".join(f'<img src="assets/sdg/sdg-{n}.jpg" alt="SDG {n}" title="{t}">' for n, t in [("3","Good health and well-being"),("6","Clean water and sanitation"),("8","Decent work and economic growth"),("9","Industry, innovation and infrastructure"),("11","Sustainable cities and communities"),("12","Responsible consumption and production"),("15","Life on land")])
    prio = [("Prevention", "Strengthen prevention-led pest management."), ("Physical protection", "Promote suitable exclusion and physical barrier solutions."), ("Responsible treatment", "Use appropriate and targeted intervention."), ("People & safety", "Maintain a strong focus on employee, customer and community safety."), ("Innovation", "Use technology and better methods to improve precision and effectiveness."), ("Continuous improvement", "Track progress and identify opportunities to improve environmental and social practices.")]
    body = page_hero("Sustainability &amp; ESG", "Responsible pest management for a more sustainable future.", "Responsible pest management is about more than controlling pests. It is about finding effective solutions that consider people, properties and the environment: prevention, precision and responsible intervention.", "fogging-wide", "Sustainability & ESG")
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
<h3 class="h3 mt-4">Responsible treatment</h3><p class="mt-1 muted">Rather than a fixed volume per job, we calculate chemical and water quantities from the specific site area, minimising leftover chemicals and water waste. When treatment is required, IPM combines prevention, monitoring and targeted intervention.</p><div class="mt-3">{link_arrow("Explore stainless-steel mesh", "mesh.html")}</div></div>
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
<div class="quote mt-5 reveal"><p>“At Pestimesh, we believe that sustainability and business success go hand in hand. By working responsibly today, we can help build healthier, safer and more sustainable environments for future generations.”</p><footer><img src="assets/img/winnie.jpg" alt="Winnie Seng"><div><b>Winnie Seng</b><span>Managing Director</span></div></footer></div></div></section>
{cta_band("Partner with a responsible pest management provider.", "Ask us about prevention-led programmes, physical protection and our ESG progress.")}'''
    return "sustainability.html", page("sustainability.html", "Sustainability & ESG", "Pestimesh's ESG approach: prevention-led pest management, stainless-steel mesh, safety-first culture, community initiatives and FY2025 GRI-referenced baseline.", body)

# ---------------------------------------------------------------- TECHNOLOGY

def technology():
    flow = [("Inspection", "Understand the property and pest activity.", "search"), ("Detection", "Use appropriate tools to investigate areas of concern.", "radar"), ("Assessment", "Interpret findings and identify potential sources.", "eye"), ("Targeted intervention", "Apply appropriate control measures.", "target"), ("Monitoring", "Track activity and evaluate results.", "refresh")]
    body = page_hero("Technology &amp; Innovation", "Smarter detection. Greater precision. Better pest management.", "Technology helps pest management teams see beyond what is immediately visible. We use modern tools and practical innovation to support more accurate inspection, targeted intervention and informed decisions, using the right technology where it makes pest management more precise and effective.", "hero-termite", "Technology & Innovation")
    body += f'''
<section class="section"><div class="container split"><div class="reveal left"><div class="eyebrow">Termatrac T3i</div><h2 class="h2">Advanced Termite Detection</h2><p class="lead mt-2">Termites can remain hidden within structures, making early detection challenging. Pestimesh uses the Termatrac T3i as part of termite inspection and detection. The device combines radar, moisture detection and thermal sensing to help detect and track termite activity. This can provide our technicians with additional information when assessing potential termite activity.</p>
<div class="grid grid-3 mt-3 reveal-stagger"><div class="card glow"><div class="ic">{I["radar"]}</div><h4>Radar</h4><p>Detects movement behind walls, floors and timber.</p></div><div class="card glow"><div class="ic">{I["drop"]}</div><h4>Moisture</h4><p>Subterranean termites need moisture; moisture mapping reveals where.</p></div><div class="card glow"><div class="ic">{I["thermo"]}</div><h4>Thermal</h4><p>Identifies temperature anomalies associated with nests and activity.</p></div></div></div>
<div class="frame parallax reveal right"><img src="assets/img/hero-termite.jpg" alt="Termites inside a tunnel"><div class="badge"><b>T3i</b><span>radar · moisture<br>· thermal</span></div></div></div></section>
<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Precision Pest Management</div><h2 class="h2">Technology That Supports Better Decisions</h2></div><p class="lead reveal">Effective pest management starts with understanding the problem. Technology can help our team identify activity, investigate concealed areas and gather additional information during inspection. Technology is most valuable when it improves decision-making. Our broader approach connects technology with our wider Integrated Pest Management philosophy.</p></div>
<div class="steps reveal-stagger">{"".join(f'<div class="step"><h4>{t}</h4><p>{d}</p></div>' for t, d, _ in flow)}</div></div></section>
<section class="section white"><div class="container split rev"><div class="frame reveal right"><img src="assets/img/mesh-rebar.jpg" alt="Stainless-steel mesh collars"></div>
<div class="reveal left"><div class="eyebrow">Physical Innovation</div><h2 class="h2">Technology is not limited to electronic equipment.</h2><p class="lead mt-2">Pestimesh also uses physical protection solutions such as woven stainless-steel mesh to help prevent pest entry. Physical exclusion can provide long-term protection and, where appropriate, reduce reliance on chemical intervention.</p><div class="mt-3">{link_arrow("Explore stainless-steel mesh", "mesh.html")}</div>
<h3 class="h3 mt-5">Digital &amp; AI</h3><p class="mt-1 muted">We are embracing AI and digital applications to streamline reporting and reduce repetitive administrative work, and exploring real-time monitoring, digital reporting and data-driven technologies so our people spend more time on site quality, safety and customer service.</p></div></div></section>
<section class="section"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Technology With a Purpose</div><h2 class="h2">Our approach to innovation is practical.</h2></div><p class="lead reveal">We focus on technology and methods that can help us:</p></div>
<div class="grid grid-4 reveal-stagger">{"".join(f'<div class="card glow"><div class="ic">{I["check"]}</div><h4>{t}</h4></div>' for t in ["Improve inspection", "Detect concealed activity", "Increase treatment precision", "Support monitoring", "Reduce unnecessary intervention", "Improve customer outcomes", "Strengthen preventive pest management", "Innovation that supports sustainability"])}</div>
<div class="btn-row mt-4">{btn("Explore our IPM approach", "ipm.html", "dark")}{btn("Explore Sustainability & ESG", "sustainability.html", "outline")}</div></div></section>
{cta_band("Book a Termatrac inspection.", "Find hidden termite activity before it becomes structural damage.")}'''
    return "technology.html", page("technology.html", "Technology & Innovation", "Termatrac T3i termite detection, stainless-steel mesh and digital innovation at Pestimesh.", body)

# ---------------------------------------------------------------- NEWS

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
<section class="section white"><div class="container"><div class="section-head"><div class="reveal"><div class="eyebrow">Pest management insights</div><h2 class="h2">Practical guides, coming soon</h2></div><p class="lead reveal">Prevention tips, pest identification, seasonal pest issues and property protection guidance. In the meantime, each service page has detailed prevention advice and FAQs.</p></div>
<div class="grid grid-4 reveal-stagger"><div class="card glow"><div class="ic">{I["shield"]}</div><h4>Pest prevention tips</h4><p>Simple property and hygiene measures that reduce pest risks.</p></div><div class="card glow"><div class="ic">{I["search"]}</div><h4>Pest identification</h4><p>Common signs of activity and when to call for an inspection.</p></div><div class="card glow"><div class="ic">{I["clock"]}</div><h4>Seasonal pest issues</h4><p>Pest risks that become more relevant at different times of year.</p></div><div class="card glow"><div class="ic">{I["building"]}</div><h4>Property protection</h4><p>Practical guidance for homes, businesses and facilities.</p></div></div>
<div class="btn-row mt-4"><a class="btn btn-outline" href="{LINKEDIN}" target="_blank" rel="noopener">Follow on LinkedIn {I["in"]}</a><a class="btn btn-outline" href="{INSTAGRAM}">Follow on Instagram {I["ig"]}</a></div></div></section>'''
    return "news.html", page("news.html", "News & Community", "Pestimesh company news, press coverage, community initiatives, tchoukball sponsorship and dengue awareness.", body)

# ---------------------------------------------------------------- CONTACT

def contact():
    body = page_hero("Contact Us", "Let's talk about your pest management needs.", "Whether you are dealing with an active pest problem, looking for preventive protection or planning a pest management programme for your property, our team is ready to help.", "team-bedok", "Contact Pestimesh")
    body += f'''
<section class="section"><div class="container"><div class="grid grid-3 reveal-stagger">
<a class="card glow" href="{WA}" target="_blank" rel="noopener"><div class="ic">{I["wa"]}</div><h4>WhatsApp us</h4><p>For a quick enquiry, message our team directly. Include your name, pest concern, property type and a brief description.</p></a>
<a class="card glow" href="tel:{PHONE_TEL}"><div class="ic">{I["phone"]}</div><h4>{PHONE}</h4><p>Call us now for urgent pest problems or to arrange a site assessment.</p></a>
<a class="card glow" href="mailto:{EMAIL}"><div class="ic">{I["mail"]}</div><h4>{EMAIL}</h4><p>Email us for project quotations, tenders and programme enquiries.</p></a></div></div></section>
<section class="section white" style="padding-top:0"><div class="container split"><div class="reveal left"><div class="eyebrow">Find our office</div><h2 class="h2">Pestimesh Pte Ltd</h2><p class="lead mt-2">{ADDRESS[0]}<br>{ADDRESS[1]}<br>{ADDRESS[2]}</p><p class="muted mt-2">Company registration no. 201114018K<br>NEA Vector Control Operator NEA201114018K</p><div class="btn-row mt-3"><a class="btn btn-dark" href="https://www.google.com/maps/search/?api=1&query=80+Playfair+Road+Singapore+367998" target="_blank" rel="noopener">Open in Google Maps {I["pin"]}</a></div></div>
<div class="frame reveal right" style="aspect-ratio:4/3"><iframe title="Pestimesh office map" src="https://www.google.com/maps?q=80+Playfair+Road+Singapore+367998&output=embed" style="width:100%;height:100%;border:0;min-height:360px" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>'''
    return "contact.html", page("contact.html", "Contact Us", "Contact Pestimesh Pte Ltd — 80 Playfair Road #04-05 Kapo Factory Building Singapore 367998. Call +65 8668 1988 or WhatsApp.", body)

# ---------------------------------------------------------------- FAQ

def faq_page():
    secs = f'<div class="reveal"><h3 class="h3">General</h3>{faq(HOME_FAQ)}</div>'
    for slug, d in PESTS.items():
        secs += f'<div class="reveal mt-5"><h3 class="h3">{d["short"]}</h3>{faq(d["faqs"])}<div class="mt-2">{link_arrow("See " + d["name"], slug+".html")}</div></div>'
    body = page_hero("FAQs", "Frequently asked questions.", "Practical answers about costs, treatment, preparation and prevention. Can't find what you need? Send us a message.", "tp-misting", "FAQs")
    body += f'<section class="section"><div class="container prose">{secs}</div></section>'
    return "faq.html", page("faq.html", "FAQs", "Frequently asked questions about pest control, termites, bedbugs, cockroaches, rodents and mosquitoes in Singapore.", body)


ALL = [home, about, services, ipm, disinfection, mesh, baiting, projects, certifications, sustainability, technology, news, contact, faq_page]
