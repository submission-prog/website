# Service pages. Copy is taken verbatim from "Pestimesh Writeup_Services.pdf" (client, Sep 2026).
# Each page = hero + a list of blocks. Keep wording exactly as supplied; layout lives in build_service().
from common import *
import re

# Menu structure (SERVICE_GROUPS) lives in common.py so the nav, footer and overview can share it.

PAGES = {
 "mosquitoes.html": dict(
  title="Mosquitoes & Dengue Prevention", hero="tp-fogging", card="pest-mosquito",
  lead=["Mosquito activity can be more than a nuisance. Certain mosquito species can transmit diseases such as dengue, making effective mosquito management important for homes, businesses and outdoor spaces."],
  blocks=[
   ("list", "Signs of Mosquito Activity", "Common signs include:",
    ["Frequent mosquito bites", "Visible mosquito activity around the property", "Mosquito larvae or pupae in stagnant water", "Mosquito activity around shaded, damp or outdoor areas"],
    "pest-mosquito", None),
   ("cards", "Our Mosquito Control Solutions",
    ["Effective mosquito control requires a combination of adult mosquito control and targeted treatment of breeding areas.",
     "Our technicians assess the property and identify areas contributing to mosquito activity before recommending the appropriate treatment."],
    None,
    [("Water-Based Misting", ["Water-based misting applies a fine treatment to outdoor areas where adult mosquitoes are active or resting. The fine droplets help provide coverage across vegetation, sheltered areas and other potential mosquito resting sites.",
                              "This treatment is suitable for reducing adult mosquito activity around homes, gardens, commercial premises and outdoor areas."]),
     ("Larviciding Treatment", ["Larviciding targets mosquito larvae in identified breeding areas before they develop into adult mosquitoes.",
                                "Treatment can be applied to suitable water-collecting areas where removing or correcting the water source is not practical. Regular servicing may be recommended to maintain control and reduce the risk of recurring breeding."]),
     ("Thermal Fogging", ["Thermal fogging produces a fine fog designed to target adult mosquitoes in outdoor areas. It can help treat vegetation, sheltered spaces and other areas where mosquitoes may rest.",
                          "Fogging is generally used as part of a broader mosquito management programme rather than as a standalone solution."])]),
  ]),

 "cockroaches.html": dict(
  title="Cockroach Control", hero="bedok-wide", card="pest-cockroach",
  lead=["Cockroaches can contaminate food and surfaces and are particularly difficult to control because they can hide in small, inaccessible areas. Without effective treatment, infestations can spread quickly."],
  blocks=[
   ("list", "Signs of Cockroach Activity", "Common signs include:",
    ["Live or dead cockroaches", "Small dark droppings or specks", "Cockroach egg cases (oothecae)", "Unpleasant or musty odours", "Shed skins and other debris"],
    "pest-cockroach", None),
   ("cards", "Our Cockroach Control",
    ["Effective cockroach control starts with identifying areas of activity, harbourage and potential food or water sources.",
     "Our technicians assess the property and select the appropriate treatment based on the cockroach species, level of activity and site conditions."],
    "Treatment Methods",
    [("Gel Baiting", ["Gel bait is strategically placed in areas where cockroaches are active or likely to travel. Cockroaches consume the bait and can carry the active ingredient back to harbourage areas, helping to reduce activity beyond the immediately treated location.",
                      "Bait placement is targeted to minimise unnecessary application and can be particularly useful around kitchens, cabinets, equipment and other areas where cockroaches are commonly found."]),
     ("Targeted Insecticide Treatment", ["Targeted insecticide applications are used on identified areas of cockroach activity and harbourage. Treatment focuses on cracks, crevices and other suitable locations rather than unnecessary broad application.",
                                         "The treatment method is selected according to the site, cockroach activity and operational requirements."])]),
  ]),

 "bedbugs.html": dict(
  title="Bed Bug Control", hero="tp-misting", card="pest-bedbug",
  lead=["Bed bugs are persistent pests that can hide in mattresses, bed frames, furniture and other concealed areas. Pestimesh provides targeted bed bug control solutions designed to identify infestations and treat affected areas effectively."],
  blocks=[
   ("list", "Signs of Bed Bug Activity", "Common signs of bed bug activity include:",
    ["Small blood stains on bedding", "Dark spots or droppings around sleeping areas", "Shed skins or eggs", "Live bed bugs around mattresses and furniture", "Bites that may appear after sleeping"],
    "pest-bedbug", None),
   ("cards", "Our Bed Bug Control Solutions",
    ["Our technicians inspect the property to identify areas of activity and determine the appropriate treatment approach based on the severity and location of the infestation."],
    None,
    [("Targeted Insecticide Treatment", ["Targeted application of professional-grade insecticides to identified areas where bed bugs are active or likely to harbour. Treatment focuses on cracks, crevices, furniture and other concealed locations."]),
     ("Heat Treatment", ["Heat treatment uses controlled temperatures to treat affected areas and target bed bugs across different life stages. It can be considered for suitable properties and infestation conditions."])]),
  ]),

 "rodents.html": dict(
  title="Rodent Management", hero="tp-building", card="pest-rodent",
  lead=["Rats and mice can contaminate food, damage property and create hygiene concerns when they gain access to a building. Pestimesh provides targeted rodent management solutions designed to identify activity, control infestations and reduce the risk of recurring problems."],
  blocks=[
   ("list", "Signs of Rodent Activity", "Common signs of rodent activity include:",
    ["Droppings around food storage or concealed areas", "Gnaw marks on cables, packaging or other materials", "Scratching or movement sounds, particularly at night",
     "Grease marks or rub marks along walls and pathways", "Nesting materials in hidden areas", "Unusual odours associated with rodent activity"],
    "pest-rodent", None),
   ("cards", "Our Rodent Management Solutions",
    ["Our technicians inspect the property to identify signs of activity, entry points and areas where rodents may be feeding or nesting. Treatment is then tailored to the property and level of activity."],
    None,
    [("Rodent Baiting", ["Strategically placed rodent bait stations are used in suitable areas to help control active rodent populations. Bait placement is determined based on rodent activity, site conditions and safety requirements."]),
     ("Rodent Trapping", ["Trapping can be used in areas where baiting may not be suitable or where targeted removal is required. Traps are positioned at identified rodent pathways and activity points."]),
     ("Monitoring &amp; Follow-Up", ["Regular monitoring helps assess rodent activity and determine whether treatment is achieving the desired results. Bait stations and traps can be inspected and adjusted as required."])]),
  ]),

 "termites.html": dict(
  title="Termite Control", hero="hero-termite", card="pest-termite",
  lead=["Termites can remain hidden for long periods while feeding on wood and other cellulose-based materials. Without early detection and appropriate treatment, termite activity can cause significant damage to a property."],
  blocks=[
   ("list", "Signs of Termite Activity", "Common signs include:",
    ["Mud tubes on walls, foundations or other structures", "Hollow or damaged wood", "Flying termites or discarded wings", "Termite droppings (frass)", "Visible termite tunnels", "Termite nests in trees or structures"],
    "pest-termite",
    "If you notice signs of termite activity, professional inspection can help determine the extent and source of the infestation."),
   ("cards", "Our Termite Treatment Solutions",
    ["Effective termite control begins with a thorough inspection to identify termite activity, affected areas and the most suitable treatment approach."],
    None,
    [("Soil Treatment", ["Soil treatment involves applying a termite-control solution to the soil around and beneath a building to create a treated zone that helps prevent termites from gaining access to the structure.",
                         "It is commonly used during new construction, renovation, or as part of corrective termite treatment for existing properties.",
                         "This approach provides an important layer of protection by targeting termite entry points below ground."]),
     ("Woven Stainless-Steel Barrier", ["Our woven stainless-steel mesh barrier provides long-term physical protection against termite entry.",
                                        "Unlike chemical-only treatments, it provides long-term physical protection without relying solely on chemical treatments, making it an important part of an integrated termite protection strategy."]),
     ("Termite Baiting System", ["Termite baiting uses a slow-acting toxicant that termites consume and share with other colony members through trophallaxis.",
                                 "The system is designed to target the termite colony rather than only visible termites, helping address termite activity at its source. Treatment duration varies depending on factors such as colony size, termite activity and site conditions."])]),
   # Not in the write-up: kept because it was requested earlier. Remove this block if the client does not want it.
   ("types", "Types of Termites in Singapore",
    "Termites, or white ants, are small, soft-bodied insects that live in large colonies made up of a Queen, King, workers, soldiers and alates. There are over 3,000 known species. Three main types are found in Singapore.",
    [("Subterranean Termites", "<em>Coptotermes</em> species. They live underground where it is moist and damp, keeping the King and Queen's chamber at 25℃ to 35℃ so the queen can lay more eggs and grow the colony. As the colony grows, worker termites surface into buildings and homes to gather food, travelling through tunnels inside walls to trap the moisture they need to survive."),
     ("Drywood Termites", "They do not require as much moisture as subterranean termites. They live and grow their colonies inside wooden structures and are not required to move out for food, producing the moisture they need themselves. They enjoy damp wood from leaking pipes and rainfall, and once a colony matures the winged swarmers look for new places to grow."),
     ("Dampwood Termites", "The third of the three main types found in Singapore. A professional inspection identifies the species present and the extent of activity before a treatment method is recommended.")]),
  ]),

 "ipm.html": dict(
  title="Integrated Pest Management", hero="tp-training", card="tp-training",
  lead=["Smarter Pest Management Starts With Prevention"],
  blocks=[
   ("text", None,
    ["IPM is a prevention-led approach that looks beyond the immediate pest problem.",
     "Rather than relying solely on routine chemical treatments, we consider factors such as food, water, shelter, entry points, harbourage and property conditions. This allows us to address the causes of pest activity and apply targeted control where required."],
    "tp-training-2"),
   ("steps", "Our IPM Approach",
    [("Inspect &amp; Identify", "We assess the property, identify pest activity and determine the conditions contributing to the problem."),
     ("Prevent", "We address potential entry points, food and water sources, harbourage areas, structural gaps and other conducive conditions."),
     ("Monitor", "Ongoing monitoring helps us track pest activity and determine when and where intervention is needed."),
     ("Targeted Treatment", "When treatment is required, we select the appropriate method based on the pest, site conditions and level of activity. This may include exclusion, physical control, baiting or targeted chemical treatment."),
     ("Evaluate &amp; Improve", "We review results and adjust the management strategy where necessary, helping provide long-term prevention and control.")]),
   ("text", "Physical Protection",
    ["Pestimesh's woven stainless-steel mesh protection provides a durable physical barrier that helps prevent pest entry without relying solely on chemical treatments.",
     "By incorporating exclusion into an integrated pest management strategy, physical protection can help reduce pest access and recurring activity."],
    "mesh-rebar"),
  ]),

 "mesh.html": dict(
  title="Woven Stainless-Steel Termite Barrier", hero="mesh-roll", card="mesh-roll",
  lead=["Pestimesh's woven stainless-steel mesh barrier provides durable physical termite protection, making it particularly suitable for pre-construction and construction-stage termite protection."],
  blocks=[
   ("cards", None, [], None,
    [("Marine-Grade 317L Stainless Steel", ["Pestimesh's mesh is manufactured using <b>marine-grade 317L stainless steel</b>, selected for its high corrosion resistance and durability in demanding environments. This helps provide long-term physical protection against termite entry."]),
     ("Long-Term Physical Protection", ["The mesh is incorporated into key areas of a building during construction to help prevent termites from gaining access through joints, penetrations and other potential entry points.",
                                        "Unlike chemical-only treatments, the barrier provides long-term physical protection without relying solely on chemical treatments."]),
     ("Ideal for Construction Projects", ["The stainless-steel mesh can be incorporated into new developments, building construction and selected renovation projects, depending on the design and site requirements.",
                                          "By installing the barrier during construction, vulnerable entry points can be protected as part of the building's overall termite protection strategy."])]),
   ("photos", ["mesh-collar", "mesh-rebar", "tp-training-2"]),
  ]),

 "mosquito-mesh.html": dict(
  title="Mosquito Mesh Protection", hero="mesh-detail", card="mesh-window",
  lead=["Pestimesh's mosquito mesh protection provides a durable physical barrier designed to help prevent mosquitoes and other flying insects from entering indoor spaces."],
  blocks=[
   ("cards", None, [], None,
    [("Long-Term Physical Insect Protection", ["The fine woven stainless-steel mesh can be installed at windows, vents, openings and other suitable access points to help prevent mosquitoes and other flying insects from entering indoor spaces.",
                                               "The mesh provides physical protection while allowing airflow and natural ventilation, making it suitable for residential, commercial and other buildings."]),
     ("Ideal for Homes &amp; Commercial Buildings", ["The stainless-steel mosquito mesh can be used for homes, offices, commercial premises and other buildings where reducing mosquito and flying-insect entry is an important part of ongoing pest management.",
                                                    "By installing the mesh at suitable access points, vulnerable openings can be protected as part of an integrated pest management strategy."])]),
   # From the supplied stainless-steel mesh brochure (names and intro line only).
   ("imgs", "Types of stainless steel mesh",
    "Each type is designed to suit different window and door configurations while providing durability, security, and a clean, practical finish.",
    [("Casement", "mesh-casement"), ("Sliding", "mesh-sliding"), ("Fixed", "mesh-fixed"), ("Attached with grilles", "mesh-grilles")]),
  ]),

 "termite-protection.html": dict(
  title="Termite Protection", hero="tp-training-2", card="tp-training-2",
  lead=["Pestimesh provides termite protection solutions designed to help reduce the risk of termite entry and protect buildings from future termite activity.",
        "Our solutions can be tailored to the property's construction, condition and protection requirements."],
  blocks=[
   ("cards", "Our Termite Protection Solutions", [], None,
    [("Woven Stainless-Steel Termite Barrier", ["Pestimesh's woven stainless-steel mesh barrier provides a durable physical barrier designed to help prevent termite entry.",
                                                "It provides long-term physical protection without relying solely on chemical treatments, making it an important part of an integrated termite protection strategy."]),
     ("Soil Treatment", ["Soil treatment creates a treated zone around or beneath the building to help prevent termites from entering through the soil.",
                         "It can be incorporated into new construction, renovation or termite protection works, depending on site requirements."]),
     ("Termite Baiting System", ["Termite baiting can form part of an ongoing protection strategy by monitoring termite activity and targeting termite colonies when activity is detected.",
                                 "Monitoring and treatment requirements vary depending on the property, termite activity and site conditions."])]),
   ("text", "Long-Term Termite Protection",
    ["A combination of physical barriers, soil treatment, corrective measures and termite monitoring can provide a more comprehensive approach to protecting a property from termite activity."],
    "mesh-collar"),
  ]),

 "disinfection.html": dict(
  title="Disinfection & Hygiene", hero="bedok-wide", card="bedok-1",
  lead=["Professional disinfection services help reduce harmful microorganisms on surfaces and high-contact areas, supporting a cleaner and more hygienic environment.",
        "Pestimesh provides disinfection services for homes, offices, commercial premises and other facilities, with treatment areas and methods adapted to the requirements of each property."],
  blocks=[
   ("list", "Areas That May Require Attention", "Depending on the property and its usage, treatment may focus on:",
    ["High-contact surfaces", "Shared areas", "Common-use facilities", "Frequently used surfaces", "Other areas identified during assessment"],
    "bedok-1", None),
   ("cards", "Our Disinfection Services",
    ["Our technicians assess the property and identify key areas requiring treatment before recommending a suitable disinfection approach. Treatment can be tailored to the property's layout, usage and hygiene requirements."],
    None,
    [("Surface Disinfection", ["Targeted treatment of relevant surfaces to help reduce harmful microorganisms and support a cleaner, more hygienic environment. This can be applied to commonly used areas and surfaces where additional hygiene control is required."]),
     ("High-Contact Area Treatment", ["Focused disinfection of frequently touched surfaces such as door handles, switches, railings, counters and shared-contact points. These areas receive particular attention due to frequent contact by multiple people."]),
     ("Commercial &amp; Facility Disinfection", ["Disinfection solutions for offices, commercial premises, shared facilities and other high-traffic environments. Treatments can be adapted to the size and usage of the premises to support ongoing hygiene management."])]),
  ]),
 # DRAFT wording (not from the client's write-up): replace once the client supplies copy.
 "bee-treatment.html": dict(
  title="Bee Treatment", hero="pest-bee", card="pest-bee",
  lead=["Bee and hornet nests near homes, workplaces and public areas can pose a safety risk, particularly to people who are allergic to stings. Pestimesh provides bee treatment carried out by trained technicians with the appropriate protective equipment."],
  blocks=[
   ("list", "Signs of Bee Activity", "Common signs include:",
    ["Increased bee or hornet activity around a particular spot", "A visible nest or hive on trees, eaves, ceilings or wall cavities", "Bees entering and leaving through a gap or opening", "Buzzing sounds from within walls, ceilings or roof spaces"],
    "pest-bee", None),
   ("cards", "Our Bee Treatment Solutions",
    ["Our technicians assess the nest location, the species involved and the surrounding area before recommending the safest treatment approach."],
    None,
    [("Nest Assessment", ["We locate the nest, identify the species and assess access, height and risk to occupants before treatment."]),
     ("Nest Treatment &amp; Removal", ["Treatment is carried out by technicians in protective equipment, and the nest is removed where it is safe and practical to do so."]),
     ("Prevention Advice", ["We identify gaps, openings and conditions that may attract nesting and advise on sealing or managing them to reduce the risk of recurrence."])]),
  ]),

 "bird-spike.html": dict(
  title="Bird Spike", hero="pest-birdspike", card="pest-birdspike",
  lead=["Bird spikes provide a humane physical deterrent that prevents birds from landing, roosting and nesting on ledges, beams, signage and other exposed surfaces."],
  blocks=[
   ("list", "Signs of Bird Activity", "Common signs include:",
    ["Bird droppings on ledges, walkways and vehicles", "Nesting material in gutters, roof spaces or signage", "Birds roosting on beams, parapets or air-conditioning units", "Noise, feathers and debris around the property"],
    "pest-birdspike", None),
   ("cards", "Our Bird Spike Solutions",
    ["Our technicians assess the property to identify landing and roosting points before recommending where spikes should be installed."],
    None,
    [("Site Assessment", ["We identify the surfaces birds are using and the extent of activity, so spikes are placed only where they are needed."]),
     ("Spike Installation", ["Stainless-steel spikes are fixed to ledges, beams, pipes and other roosting surfaces to prevent birds from landing without harming them."]),
     ("Cleaning &amp; Maintenance", ["Affected areas can be cleaned before installation, and spikes checked and adjusted as part of ongoing pest management."])]),
  ]),
}


# ---------------------------------------------------------------- rendering

def _paras(ps, first_lead=False):
    return "".join((f'<p class="lead mt-2">{p}</p>' if first_lead and k == 0 else f'<p class="mt-2">{p}</p>') for k, p in enumerate(ps))


def _block(b, shade):
    kind = b[0]
    if kind == "list":
        _, title, intro, items, img, outro = b
        lis = "".join(f"<li>{x}</li>" for x in items)
        return (f'<section class="section {shade}"><div class="container split">'
                f'<div class="reveal left"><h2 class="h2">{title}</h2><p class="mt-2">{intro}</p><ul class="dotlist">{lis}</ul>'
                + (f'<p class="muted">{outro}</p>' if outro else "") +
                f'<div class="btn-row mt-4">{btn("Request a quote", "contact.html#enquiry", "lime")}{btn("WhatsApp us", WA, "wa", "wa")}</div></div>'
                f'<div class="frame tall reveal right"><img src="assets/img/{img}.jpg" alt="{escape(title)}"></div></div></section>')
    if kind == "cards":
        _, title, intro, label, items = b
        n = len(items)
        cols = "grid-2" if n in (2, 4) else "grid-3"
        cards = "".join(f'<div class="card"><div class="ic">{I["check"]}</div><h4>{t}</h4>{"".join(f"<p>{p}</p>" for p in ps)}</div>' for t, ps in items)
        head = ""
        if title or intro:
            h2 = f'<h2 class="h2">{title}</h2>' if title else ""
            head = (f'<div class="section-head" style="align-items:start"><div class="reveal">{h2}</div>'
                    f'<div class="reveal">{_paras(intro, True) if intro else ""}</div></div>')
        lab = f'<h3 class="h3 mb-3">{label}</h3>' if label else ""
        return f'<section class="section {shade}"><div class="container">{head}{lab}<div class="grid {cols} reveal-stagger">{cards}</div></div></section>'
    if kind == "steps":
        _, title, items = b
        steps = "".join(f'<div class="step"><h4>{t}</h4><p>{p}</p></div>' for t, p in items)
        return f'<section class="section {shade}"><div class="container"><h2 class="h2 mb-3">{title}</h2><div class="steps reveal-stagger">{steps}</div></div></section>'
    if kind == "text":
        _, title, ps, img = b
        h = f'<h2 class="h2">{title}</h2>' if title else ""
        return (f'<section class="section {shade}"><div class="container split">'
                f'<div class="reveal left">{h}{_paras(ps, first_lead=not title)}</div>'
                f'<div class="frame reveal right"><img src="assets/img/{img}.jpg" alt="{escape(title or "Pestimesh")}"></div></div></section>')
    if kind == "photos":
        _, imgs = b
        cells = "".join(f'<div class="frame"><img src="assets/img/{im}.jpg" alt="Woven stainless-steel mesh" loading="lazy"></div>' for im in imgs)
        return f'<section class="section {shade}"><div class="container"><div class="grid grid-3 reveal-stagger">{cells}</div></div></section>'
    if kind == "imgs":
        _, title, intro, items = b
        cards = "".join(f'<div class="imgcard"><img src="assets/img/{im}.jpg" alt="{nm} stainless steel mesh" loading="lazy"><div><h4>{nm}</h4></div></div>' for nm, im in items)
        return (f'<section class="section {shade}"><div class="container"><div class="section-head" style="align-items:start"><div class="reveal"><h2 class="h2">{title}</h2></div>'
                f'<p class="lead reveal">{intro}</p></div><div class="grid grid-4 reveal-stagger">{cards}</div></div></section>')
    if kind == "types":
        _, title, intro, items = b
        cards = "".join(f'<div class="card dark"><div class="ic">{I["bug"]}</div><h4>{t}</h4><p>{p}</p></div>' for t, p in items)
        return (f'<section class="section dark"><div class="container"><div class="section-head"><div class="reveal"><h2 class="h2">{title}</h2></div>'
                f'<p class="lead reveal">{intro}</p></div><div class="grid grid-3 reveal-stagger">{cards}</div></div></section>')
    raise ValueError(kind)


def build_service(file, d):
    title = escape(d["title"])
    body = page_hero(f'<a href="services.html">Services</a><span>/</span>{title}', title, d["lead"], d["hero"])
    shades = ["", "white"]
    k = 0
    for b in d["blocks"]:
        if b[0] == "types":
            body += _block(b, "dark")
        else:
            body += _block(b, shades[k % 2]); k += 1
    desc = re.sub(r"<[^>]+>", "", d["lead"][0])[:155]
    return file, page(file, d["title"], desc, body)


