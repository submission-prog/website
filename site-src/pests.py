# Pest service pages. Copy is taken verbatim from "Pestimesh Sitemap.pdf".
from common import *

PESTS = {
 "bedbugs": dict(
  name="Bedbugs Control", short="Bedbugs", singular="Bedbug", hero="tp-misting", concern="Bedbug",
  tagline="Targeted bedbug treatment designed to address active infestations and help prevent recurrence.",
  what=["Bedbugs are small, flat, reddish-brown insects that feed on the blood of humans and other warm-blooded animals. Adult bedbugs are about the size of an apple seed and are excellent at hiding in cracks, crevices, mattresses, bed frames and furniture.",
        "Bedbugs are mainly active at night, which makes them difficult to spot. They can also spread from one location to another by hiding in luggage, clothing, bedding, furniture and other personal belongings.",
        "Despite their name, bedbugs are not limited to beds. An infestation can develop in bedrooms, sofas, carpets, wardrobes and other areas where people rest or spend time."],
  why=["A bedbug infestation can be stressful and difficult to eliminate without the right treatment. Their bites can cause itchy, irritated skin, while the presence of bedbugs can interfere with sleep and cause significant discomfort.",
       "Bedbugs are also difficult to control because they hide in small, hard-to-reach areas and can survive for extended periods without feeding. Eggs and young bedbugs can be easily missed during a basic cleaning or inspection, allowing the infestation to continue.",
       "The sooner a bedbug infestation is identified and treated, the easier it can be to prevent it from spreading further."],
  business=["Bedbugs can have a serious impact on businesses, particularly hotels, hostels, serviced apartments and other commercial properties. Infestations can lead to customer complaints, negative reviews, reputational damage and lost revenue.",
            "Bedbugs can also disrupt operations when affected rooms or areas need to be closed for treatment. Fast, professional pest control can help minimise disruption and prevent the infestation from spreading."],
  signs_intro="Bedbugs can be difficult to see, especially during the early stages of an infestation. Look out for these common warning signs:",
  signs=[("Small bites","Red, itchy marks that may appear in clusters or lines, particularly after sleeping."),("Blood spots","Small reddish or rusty marks on sheets, pillowcases or mattresses."),("Dark spots","Tiny dark stains caused by bedbug droppings may appear around mattress seams and hiding places."),("Shed skins","Bedbugs shed their skins as they grow, which may be found around infested areas."),("Eggs and eggshells","Tiny, pale eggs may be found in mattress seams, furniture joints and cracks."),("Live bedbugs","Adult bedbugs may be visible around mattresses, bed frames and other hiding spots."),("Unusual odour","Larger infestations can sometimes produce a distinctive musty or sweet smell.")],
  signs_outro="If you notice several of these signs, it is best to arrange a professional inspection rather than waiting for the infestation to become more severe.",
  hide=["Bedbugs are experts at hiding. During the day, they often stay in dark, protected areas close to where people sleep or rest.",
        "Common hiding places include mattress seams, bed frames, headboards, furniture joints, cracks and crevices, sofas, curtains and behind loose wallpaper. They may also hide in luggage, clothing and other belongings, allowing them to spread between rooms or properties.",
        "A professional inspection can help identify both visible signs and potential hiding areas that may otherwise be overlooked."],
  treatment_title="Bedbug Treatment",
  treatment=["Bed Bugs, or <em>Cimex lectularius</em>, are one of the world's most common pests and also pose a nuisance to people in Singapore and across the globe.",
             "Effective bedbug control requires more than simply treating the mattress or washing the bedding. Because bedbugs can hide in many different locations and at different stages of their life cycle, treatment needs to be thorough and carefully planned.",
             "Our bedbug treatment process typically begins with a professional inspection to identify signs of activity, infestation areas and potential hiding places. We then recommend an appropriate treatment approach based on the severity and location of the infestation.",
             "Treatment may involve targeted applications to affected areas, along with preparation and follow-up recommendations. In some cases, more than one treatment may be required to achieve effective control.",
             "Our technicians will explain the treatment process and any preparation steps you need to take before treatment begins."],
  methods=[],
  pro_title="Why Choose Professional Bedbug Control?",
  pro_intro=["Bedbugs can be persistent, and DIY treatments may not reach all the areas where they are hiding. Treating only the places where bedbugs have been spotted can leave eggs, nymphs or hidden adults behind.",
             "Professional pest control technicians have the experience and equipment to inspect an infestation systematically and develop a treatment plan suited to the property.",
             "<b>Our goal is not simply to treat the bedbugs you can see, but to identify the source of the infestation and address the areas where they may be hiding.</b>"],
  pro=[],
  prevent_title="How to Prevent Bedbugs",
  prevent_intro=["While bedbugs can affect even clean and well-maintained properties, a few precautions can reduce the risk of bringing them into your home or business.",
                 "When travelling, inspect hotel beds and furniture before unpacking, keep luggage away from beds where possible, and wash or heat-dry clothing after returning home. Avoid bringing second-hand mattresses or upholstered furniture into your property without carefully inspecting them first.",
                 "If you suspect you have brought bedbugs home, acting quickly can help prevent them from spreading to other rooms."],
  prevent=[], prevent_outro="",
  faqs=[("How do I know if I have bedbugs?","You may have bedbugs if you notice itchy bites in clusters, small blood stains on bedding, shed skin, a musty odor, or living bugs hiding near your sleeping area."),
        ("Can bedbugs live in my mattress?","Yes, bedbugs can live inside a mattress, hiding in seams, folds and even deeper internal layers."),
        ("How do bedbugs spread?","Bedbugs primarily spread by hitchhiking on clothing, luggage, furniture or other personal items, moving from place to place faster than they can on their own. They can also move within walls, through floor and ceiling openings."),
        ("Can bedbugs be seen with the naked eye?","Adult bedbugs are visible to the naked eye, but nymphs and eggs are much harder to see due to their small size and translucence. Spotting bedbugs can also be challenging due to their nocturnal nature and expert hiding abilities."),
        ("How long does bedbug treatment take?","The duration of bedbug treatment depends on factors such as the severity of the infestation, size of the affected area and treatment method.<br><br>Heat treatment is generally the fastest option and typically takes around four to eight hours, depending on the size of the space. Once treatment is completed and the technician confirms it is safe to re-enter, the space can generally be used immediately. A follow-up inspection is recommended two to three weeks later to check for any remaining activity.<br><br>Chemical treatment generally requires multiple visits, as a single treatment may not reliably eliminate bedbug eggs. During the initial visit, the technician will inspect the premises and apply treatment to affected and harbourage areas. A follow-up visit is typically scheduled two to three weeks later to assess the results and carry out further treatment if required. Additional visits may be necessary for severe infestations or where treatment preparation was insufficient.<br><br>The actual treatment duration and number of visits will vary depending on the individual infestation."),
        ("Will one treatment get rid of bedbugs?","One treatment can eliminate bedbugs only if it is a professionally executed whole-room heat treatment that reaches at least (49–55°C) in every hiding spot; chemical treatments almost never succeed in a single visit."),
        ("Do bedbugs only live in dirty homes?","No, bedbugs are not attracted to dirt or clutter; they are instead attracted to warmth, blood and carbon dioxide. However, clutter and trash offers more hiding spots for them to remain undetected in."),
        ("Can bedbugs come back after treatment?","Yes, bedbugs can return after treatment if eggs or hidden bedbugs remain, or if they are reintroduced from another location. Following the recommended preparation and treatment steps, along with any necessary follow-up treatments, can help prevent reinfestation. If bedbugs reappear, contact a professional pest control team for a follow-up inspection."),
        ("What should I do before bedbug treatment?","Follow the preparation instructions provided by your pest control technician. This may include removing clutter, washing and drying bedding and clothing, and making affected areas accessible for inspection and treatment. Avoid moving items from an infested area to other rooms, as this can spread the bedbugs."),
        ("How can I prevent bedbugs from spreading?","Avoid moving bedding, clothing, furniture or other belongings from an infested area to other parts of the property. Wash and heat-dry clothing and bedding where possible, inspect luggage and second-hand furniture carefully, and arrange professional treatment as soon as you suspect an infestation.")],
  resources="Learn more about bedbugs, their habits and effective ways to prevent and control bedbug activity around your home or business.",
 ),
 "cockroaches": dict(
  name="Cockroaches Control", short="Cockroaches", singular="Cockroach", hero="bedok-wide", concern="Cockroach",
  tagline="Effective cockroach treatment for homes and businesses, with solutions tailored to the level and location of infestation.",
  what=["Cockroaches are resilient insects that can adapt to a wide range of environments. They are commonly found in warm, damp areas with access to food and water, making kitchens, drains, storerooms and other areas of a property attractive to them.",
        "Cockroaches are mainly active at night and can hide in small cracks and crevices, making an infestation difficult to detect in its early stages."],
  why=["Cockroaches can contaminate food, surfaces and other areas of a property as they move between dirty and clean environments. They can carry bacteria and other microorganisms on their bodies and may contribute to poor hygiene conditions.",
       "Cockroach droppings, shed skins and other debris can also trigger allergic reactions and worsen asthma symptoms in sensitive individuals.",
       "Because cockroaches reproduce quickly and are good at hiding, a small infestation can develop into a larger problem if left untreated. Early professional control can help prevent the infestation from spreading."],
  business=["Cockroaches can be particularly damaging to businesses where hygiene and cleanliness are essential, including restaurants, hotels, food establishments and commercial kitchens.",
            "A cockroach infestation can result in customer complaints, food contamination, operational disruption and reputational damage. Businesses may also face additional costs associated with cleaning, treatment and temporarily closing affected areas.",
            "Professional cockroach control helps businesses maintain hygienic premises and minimise the risk of recurring infestations."],
  signs_intro="Identifying cockroach activity early can help prevent an infestation from becoming more severe. Common signs include:",
  signs=[("Live or dead cockroaches","around your property"),("Cockroach droppings","which may appear as small dark spots or specks"),("Egg cases (oothecae)","in hidden areas"),("Unpleasant or musty odour","particularly with larger infestations"),("Shed skins","or other cockroach debris"),("Gnaw or feeding damage","to food packaging and other materials")],
  signs_outro="If you notice these signs, professional inspection and treatment can help identify the extent of the infestation.",
  hide=["Cockroaches prefer warm, dark and humid areas close to food and water sources. Common hiding places include kitchens, cabinets, sinks, drains, rubbish areas, appliances, storerooms and cracks or gaps around walls and floors.",
        "They can also hide behind refrigerators, ovens and other appliances where warmth and moisture are present."],
  treatment_title="Cockroaches Treatment",
  treatment=["Effective cockroach treatment involves identifying where cockroaches are hiding, feeding and breeding. Our treatment focuses on targeted areas of activity and potential harbourage points to reduce the infestation at its source.",
             "Depending on the property and level of infestation, treatment may include targeted insecticide applications, gel baiting and other appropriate control methods. Follow-up treatments may be recommended for more established infestations."],
  methods=[],
  pro_title="Why Choose Professional Cockroach Control?",
  pro_intro=["Cockroaches are highly adaptable and can hide in areas that are difficult to access. DIY sprays may kill visible cockroaches but often do not reach hidden harbourage areas or address the wider infestation.","Professional cockroach control offers:"],
  pro=["<b>Thorough inspection</b> – Identify areas of activity and potential hiding spots.","<b>Targeted treatment</b> – Apply appropriate control methods to affected areas.","<b>Professional expertise</b> – Assess the property and recommend a suitable treatment plan.","<b>Reduced recurrence</b> – Identify conditions that may contribute to recurring cockroach activity."],
  prevent_title="How to Prevent Cockroaches?",
  prevent_intro=["Keeping your property clean and reducing access to food, water and hiding places can help prevent cockroach infestations.","Simple prevention measures include:"],
  prevent=["Store food in sealed containers","Clean food spills and crumbs promptly","Empty rubbish regularly","Keep kitchens and food preparation areas clean","Fix leaking taps and pipes","Keep drains clean and covered where appropriate","Seal cracks, gaps and potential entry points","Reduce clutter and unnecessary storage","Avoid leaving pet food exposed overnight"],
  prevent_outro="Regular inspections and professional pest control can provide additional protection for properties with recurring cockroach activity.",
  faqs=[("Can Cockroaches Come Back After Treatment?","Yes. Cockroaches can return if they are reintroduced or if food, water and suitable hiding areas remain available. Following treatment recommendations and maintaining good sanitation can help reduce the risk of recurring infestations."),
        ("How Quickly Do Cockroaches Multiply?","Cockroaches can reproduce rapidly under favourable conditions. Warmth, moisture and access to food can allow populations to grow quickly, making early treatment important."),
        ("Can Cockroaches Live Without Food?","Cockroaches can survive for extended periods without food, although they still require water. Removing access to food and moisture can therefore help reduce conditions that support an infestation."),
        ("Is One Cockroach a Sign of an Infestation?","Not necessarily, but seeing a cockroach can indicate that others may be hiding nearby. If cockroaches are regularly seen, particularly during the day, a professional inspection is recommended.")],
  resources="Learn more about cockroaches, their habits and effective ways to identify, prevent and control infestations around your home or business.",
 ),
 "termites": dict(
  name="Termites Protection", short="Termites", singular="Termite", hero="hero-termite", concern="Termite",
  tagline="Termite protection solutions, including chemical treatment and physical barrier solutions where appropriate.",
  what=["Termites or also known as white ants are small, soft bodied insects that live in large colonies. The colonies are made up of a Queen, King, workers, soldiers and alates. Termites feed on cellulose like wood and plant materials. Termites thrive in countries with warm and humid tropical climates.",
        "Appearance wise, Termites are pale, white or light brown. They may appear like ants, but they have straight antennae and thick waists. There are over 3000 known species of termites. There are 3 main types in Singapore; Subterranean Termites (<em>Coptotermes</em> species), Drywood Termites and Dampwood Termites."],
  why=["Termites are a major problem as they silently eat and destroy wood, paper and any other materials containing cellulose. This can cause Structural Damage to homes and buildings.",
       "Termites live and feed inside walls, floors and underground. This means an infestation can grow for a long time before it is noticeable.",
       "Termites can be dangerous as there are safety risks. Termites can weaken floors, ceiling beams and roof structures. This can cause collapsing. Termites can damage building materials and, in some cases, contribute to damage around electrical components and wiring. Termites also pose health threats as they leave behind their dust, frass. As the frass builds it can bother individuals with allergies and asthma."],
  business=["Many Businesses in Singapore are affected by termites as many business and commercial properties rely on heavily wooden interiors, paper products and structural integrity. Hotels, Restaurants and Cafes, are affected as these businesses rely on wooden furniture, expensive wooden flooring and decorative wood panels.",
            "Retail shops and corporate offices with wooden floors or walls and large archives of paper files are vulnerable. Logistics Warehouses and storage facilities that store wood pallets, cardboard and paper goods are feeding grounds for Termites."],
  signs_intro="Early Stages of Termite infestation can be difficult to spot but there are a few signs to look out for:",
  signs=[("Mud Tubes","Subterranean termites build their shelter tubes out of mud, dirt and debris to travel to and from their food source and nest. These tubes are pencil sized tunnels and can be found on exterior and interior walls."),("Wooden Tunnels","These tunnels can be difficult to spot from outside but can be spotted within broken wood and timbre. This sign confirms that the termite infestation has occurred."),("Flying Termites and Discarded Wings","One of the first signs of infestation are when fly termites or alates discard their wings. These termites shed their wings after finding their mate."),("Hollow wood sounds","Usually infested areas that have been eaten will sound hollow if knocked on."),("Termite droppings (Frass)","Frass are tiny pallets that are mostly found at entry points of tunnels. These droppings will accumulate over time near the infested wood. The texture is rougher and harder compared to other frass from other pests."),("Termite tree nests","There are cases where termites nest in hollow centers of tree roots or trunks.")],
  signs_outro="If you notice several of these signs, it is best to arrange a professional inspection rather than waiting for the infestation to become more severe.",
  hide=["<b>Subterranean Termites</b><br>Subterranean termites live underground where it is moist and damp. These termites require moisture to live therefore they create their colony underground. The Termites ensure that their King and Queen's chamber is moist and is of suitable temperature of 25℃ to 35℃ to allow the queen to lay more eggs to grow the colony.",
        "As the colony grows the worker termites expand their underground colony and set many other nesting sites and expand to gather more food. This is when the termites start surfacing above to buildings and homes to gather food. These termites do not forge in open and other travel through tunnels inside the walls to trap moisture for their survival.",
        "<b>Drywood Termites</b><br>Drywood termites do not require as much moisture as the subterranean termites. These pests live and grow their colonies inside wooden structures and are not required to move out for food. As they live in wood that provides them with shelter and source of food. Unlike subterranean termites, drywood termites are capable of producing the amount of moisture they require. These termites enjoy damp wood from leaking pipes and rainfall.",
        "High levels of humidity and moisture can grow drywood termite colonies quickly. Once the termites colony matures, the winged swarmer termites will begin to look for new places to grow their colonies."],
  treatment_title="Our Termite Treatment Solutions",
  treatment=["Termites, also known as “white ants,” thrive in Singapore's tropical climate and can cause extensive property damage. The two main types found in Singapore are subterranean termites and drywood termites.",
             "Effective termite control begins with a thorough inspection to identify the termite species and extent of infestation. Based on the findings, we recommend the most suitable treatment to eliminate termite activity and help prevent recurrence."],
  methods=[("Soil Treatment","Primarily used during the pre-construction phase, soil treatment creates an anti-termite barrier beneath the building. Termiticides are applied before concrete slabs are laid to help prevent subterranean termite damage. A 5-year warranty is provided upon completion of treatment."),
           ("Corrective Treatment","Corrective treatment involves drilling or coring at intervals around the property and injecting termite-control solution into each hole before sealing it with concrete and waterproofing cement. This creates a chemical barrier designed to protect the property, with a 5-year warranty provided."),
           ("Woven Stainless Steel Barrier","An environmentally friendly termite barrier made from high-quality materials and installed using carefully researched techniques. It provides long-term physical protection against termite entry without relying solely on chemical treatments."),
           ("Termatrac T3i","The Termatrac T3i is an advanced termite detection system that combines radar, moisture and thermal sensing technologies to detect and track termite activity. This allows technicians to identify termite presence more accurately, particularly as subterranean termites require moisture to survive."),
           ("Termite Baiting System","Termite baiting uses a food source containing a slow-acting toxicant. Foraging termites consume the bait and share it with other colony members, including the queen and king, through trophallaxis. Colony elimination typically takes 2–12 weeks, depending on the size of the colony, with most cases taking around 6–8 weeks.")],
  pro_title="Why Choose Professional Termite Control?",
  pro_intro=["Termites can remain hidden for long periods, causing damage before an infestation becomes obvious. DIY treatments may only address visible termites without reaching the colony or identifying the source of the infestation.",
             "Professional termite control begins with a thorough inspection to identify the termite species, activity and affected areas. Depending on the property and infestation, treatment may involve soil treatment, termite baiting or targeted wood treatment. Different methods have different applications, so choosing the right approach is important for effective control.",
             "Professional termite control can help to:"],
  pro=["Identify the source of termite activity and potential entry points","Target the colony, rather than only treating visible termites","Protect your property from further termite damage","Provide ongoing monitoring to detect recurring activity early","Recommend the right treatment based on your property and type of termite"],
  pro_outro="Termite control is often a long-term process rather than a one-time treatment. Regular inspections, monitoring and preventive measures can help maintain protection and reduce the risk of recurring infestations.",
  prevent_title="How to Prevent Termites?",
  prevent_intro=["Termites have a chance of returning and recurring after a period of time due to weather or home conditions. Here are tips on how to prevent termites infestation."],
  prevent=["Keep home dry and moisture free especially areas with wood and furniture.","Discard all damaged and infested wood, branches, logs and timber.","Avoid placing wood near termites' homes and tunnels.","Fix any holes, gaps and cracks to prevent termites from entering","Limit the use of wood flooring, planks and furniture."],
  prevent_outro="",
  faqs=[("How Do I Know If I Have a Termite Infestation?","Common signs include mud tubes, discarded wings, hollow-sounding or damaged wood, and small piles of termite droppings (frass). Because termites often remain hidden, professional inspection can help detect activity before significant damage occurs."),
        ("Can Termites Cause Serious Property Damage?","Yes. Termites feed on cellulose found in wood and other materials, and infestations can cause significant structural and property damage if left untreated. Early detection and professional treatment can help limit further damage."),
        ("Can I Get Rid of Termites Myself?","DIY products may only address visible termite activity without reaching the colony. Professional termite control involves identifying the source of the infestation and selecting an appropriate treatment method based on the property and type of termite."),
        ("How Long Does Termite Treatment Take?","The treatment duration depends on factors such as the type of termite, extent of the infestation, property size and treatment method. Some termite control programmes also require follow-up inspections or monitoring to ensure continued control."),
        ("Can Termites Return After Treatment?","Yes. New termite activity can occur if termites enter the property from surrounding areas or if conditions remain favourable for infestation. Regular inspections and preventive measures can help detect and address new activity early.")],
  resources="Learn more about termites, the signs of infestation and effective ways to protect your home or business from termite damage.",
 ),
 "rodents": dict(
  name="Rodents Management", short="Rodents", singular="Rodent", hero="tp-building", concern="Rodent",
  tagline="Rodent management solutions focused on controlling activity and identifying potential entry and harbourage points.",
  what=["Rodents are mammals characterised by their continuously growing front teeth. Common pest rodents include rats and mice, which are highly adaptable and can live in a wide range of environments.",
        "They are attracted to properties where they can find food, water and shelter, and can enter buildings through surprisingly small gaps and openings."],
  why=["Rodents can pose significant hygiene and property concerns. They may contaminate food and surfaces through their droppings, urine and contact with contaminated areas.",
       "Rodents can also gnaw on electrical wiring, wood, insulation, packaging and other materials. If left uncontrolled, an infestation can grow quickly and spread to different areas of a property.",
       "Early detection and professional rodent control can help minimise health risks, property damage and the likelihood of a larger infestation."],
  business=["Rodent infestations can be particularly disruptive for businesses, especially restaurants, food establishments, warehouses, hotels and commercial facilities.",
            "Rats and mice can contaminate food, damage stock and packaging, and gnaw on electrical cables and building materials. Their presence can also result in customer complaints, operational disruption and reputational damage.",
            "Professional rodent control helps businesses protect their premises, products and reputation while reducing the risk of recurring rodent activity."],
  signs_intro="Rodents are often active at night and may remain hidden, but they can leave several signs of their presence:",
  signs=[("Rodent droppings","around food storage, cabinets and hidden areas"),("Gnaw marks","on wires, wood, packaging and other materials"),("Scratching or scurrying sounds","particularly at night"),("Grease or rub marks","along walls and frequently used paths"),("Nesting materials","such as shredded paper, fabric or other soft materials"),("Unusual odours","around hidden or enclosed areas"),("Damaged food packaging","or missing food")],
  signs_outro="If you notice these signs, professional inspection can help identify the source and extent of the infestation",
  hide=["Rodents prefer dark, sheltered areas close to food and water. Common hiding places include storerooms, cabinets, ceilings, wall cavities, roof spaces, warehouses, drains and areas behind appliances.",
        "They may also hide around clutter, rubbish areas and other places that provide shelter and easy access to food."],
  treatment_title="Rodent Treatment",
  treatment=["Effective rodent control starts with identifying signs of activity, potential entry points and areas where rodents are feeding or nesting.",
             "Our treatment may include targeted rodent control measures, monitoring and recommendations to address potential entry points and attractants. The appropriate approach depends on the type and severity of the infestation and the property's environment."],
  methods=[],
  pro_title="Why Choose Professional Rodent Control?",
  pro_intro=["Rodents can be difficult to control because they are cautious, adaptable and capable of hiding in inaccessible areas. DIY traps or products may provide temporary control without addressing the source of the infestation or potential entry points.","Professional rodent control offers:"],
  pro=["<b>Thorough inspection</b> – Identify signs of activity, nesting areas and entry points.","<b>Targeted control</b> – Use appropriate methods based on the property and infestation.","<b>Professional expertise</b> – Assess the source and extent of rodent activity.","<b>Ongoing monitoring</b> – Help detect continued or recurring activity.","<b>Prevention advice</b> – Identify conditions that may attract or allow rodents into the property."],
  prevent_title="How to Prevent Rodents ?",
  prevent_intro=["Reducing access to food, water and shelter can help make your property less attractive to rodents.","Simple prevention measures include:"],
  prevent=["Store food and rubbish in secure, sealed containers","Clean up food spills and crumbs promptly","Keep rubbish areas clean","Remove unnecessary clutter and potential nesting materials","Seal cracks, gaps and openings around the property","Keep doors and windows properly closed or screened","Maintain drains and surrounding areas","Avoid leaving pet food exposed for extended periods"],
  prevent_outro="Regular inspections and professional rodent control can help identify and address potential problems before they become more serious.",
  faqs=[("How Do I Know If I Have Rats or Mice?","Droppings, gnaw marks, scratching sounds, nesting materials and damaged food packaging are common signs of rodent activity. A professional inspection can help identify the type of rodent and locate areas of activity."),
        ("Can Rodents Cause Property Damage?","Yes. Rodents have strong teeth and may gnaw on electrical wiring, wood, insulation, packaging and other materials. This can result in property damage and, in some situations, create electrical and fire hazards."),
        ("Can Rats and Mice Enter Through Small Gaps?","Yes. Rodents can squeeze through relatively small openings, making gaps around doors, pipes, drains, walls and other structural areas potential entry points."),
        ("Can Rodents Come Back After Treatment?","Yes. Rodents can return if access points remain open or if food, water and shelter continue to be available. Sealing potential entry points and maintaining good sanitation can help reduce the risk of recurring activity."),
        ("How Long Does Rodent Treatment Take?","Treatment duration depends on the type and severity of the infestation, the size of the property and the level of rodent activity. Follow-up visits or monitoring may be required for established infestations.")],
  resources="Learn more about rodents, the signs they leave behind and effective ways to prevent and control rodent activity around your property.",
 ),
 "mosquitoes": dict(
  name="Mosquitoes & Dengue Prevention", short="Mosquitoes", singular="Mosquito", hero="tp-fogging", concern="Mosquito",
  tagline="Targeted mosquito-control solutions designed to address both adult mosquitoes and potential breeding sources.",
  what=["Mosquitoes are small flying insects known for their blood-feeding habits and role as vectors of disease. Mosquitoes feed primarily on plant nectar while female mosquitoes require blood to produce eggs. They are commonly found in areas with standing water, where they lay their eggs and breed. Some mosquito species can also transmit diseases through their bites."],
  why=["Mosquitoes are more than just a nuisance. Their bites can cause itching and skin irritation, while certain mosquito species can transmit diseases.",
       "Mosquitoes are known vectors of diseases such as malaria, dengue, Zika and yellow fever. Depending on the disease, infected mosquito bites can lead to symptoms such as high fever, headache, allergic reactions and joint and muscle pain. Mosquitoes can also pose a risk to pets and wildlife.",
       "Beyond health concerns, mosquito breeding can also affect the hygiene and appearance of water features. Mosquito larvae and pupae can develop in stagnant water, potentially reducing its aesthetic and sanitary quality.",
       "Early mosquito control can help reduce breeding, minimise health risks and maintain a cleaner, more comfortable environment."],
  business=["Mosquito problems can make outdoor spaces less enjoyable or even unusable for customers. Restaurants, resorts, hotels and event venues may lose customers if their premises become known for mosquito activity, resulting in reduced revenue and reputational damage.",
            "Mosquito-borne illnesses can also affect employees, potentially leading to absenteeism, reduced productivity and increased healthcare costs for businesses.",
            "Professional mosquito control helps businesses maintain a more comfortable environment for customers and employees while reducing mosquito activity around the premises."],
  signs_intro="Identifying mosquito activity early can help prevent the problem from getting worse. Common signs of mosquito activity and breeding include:",
  signs=[("Visible mosquitoes","around your home or property"),("Frequent mosquito bites","especially when spending time outdoors"),("High-pitched buzzing noise","around your ears, particularly at night"),("Standing or stagnant water","in drains, plant pots, contains, gutters or other areas where mosquitoes can breed."),("Mosquito larvae or pupae","in stagnant water.")],
  signs_outro="If you notice these signs, early professional treatment can help reduce mosquito activity and prevent further breeding.",
  hide=["Mosquitoes prefer cool, shaded and sheltered areas, especially during the day. They can be found around dense vegetation, bushes, drains, gutters, under outdoor furniture and other damp areas. Mosquitoes also breed in stagnant or standing water, including plant pots, containers, or poorly drained areas."],
  treatment_title="Our Mosquito Treatment Solutions",
  treatment=["Mosquitoes thrive in Singapore's warm and humid climate and can become a nuisance around homes and commercial properties. Effective mosquito control requires both adult mosquito control and targeted treatment of breeding areas.",
             "Our technicians will assess the property and recommend the most suitable treatment based on mosquito activity and potential breeding sites."],
  methods=[("Water-Based Misting","A fine mist treatment designed to eliminate airborne mosquitoes and reach hard-to-access areas such as cracks and crevices. Its small particle size provides thorough coverage with a low-toxicity formulation."),
           ("Larviciding Treatment","Targets mosquito larvae in identified breeding areas and water-collecting receptacles where physical correction is not possible. Regular servicing is recommended to maintain effective control and reduce the risk of reinfestation."),
           ("Thermal Fogging","Targets existing adult mosquitoes and leaves a residual treatment on surrounding vegetation to provide additional protection and strengthen mosquito control.")],
  pro_title="Why Choose Professional Mosquito Control?",
  pro_intro=["Singapore's warm and humid climate provides favourable conditions for mosquitoes to breed and thrive. While DIY methods may help reduce mosquitoes temporarily, they often do not address hidden breeding sites or provide complete coverage.","Professional mosquito control offers:"],
  pro=["<b>More thorough coverage</b> – Identify and target potential breeding and resting areas around your property.","<b>Longer-lasting results</b> – Address the source of mosquito activity rather than only the mosquitoes you can see.","<b>Professional expertise</b> – Trained technicians can assess your property and recommend the appropriate treatment.","<b>Reduced risk of recurring activity</b> – Regular treatment and monitoring can help keep mosquito populations under control."],
  prevent_title="How to Prevent Mosquitoes?",
  prevent_intro=["The most effective way to reduce mosquito activity is to eliminate potential breeding sites around your property. Regularly inspect your surroundings and remove any stagnant water where mosquitoes can lay eggs.","Simple prevention measures include:"],
  prevent=["Emptying water from plant pots, containers and other items","Keeping drains and gutters clear","Covering water storage containers properly","Maintaining good drainage around the property","Keeping outdoor areas clean and free of clutter","Checking for stagnant water after rainfall","Arranging regular professional mosquito control for properties with persistent activity"],
  prevent_outro="Taking these steps regularly can help reduce mosquito breeding and keep your home or business more comfortable.",
  faqs=[("Is DIY Treatment Enough to Remove Mosquitoes?","DIY mosquito control methods may reduce mosquito activity temporarily, but they may not address hidden breeding sites or the source of the infestation. Professional treatment can help identify breeding areas and provide more thorough control."),
        ("How Quickly Can Mosquitoes Multiply?","Mosquitoes can reproduce quickly when suitable breeding conditions are available. Even small amounts of stagnant water can provide a place for mosquitoes to lay eggs, which is why removing standing water is an important part of mosquito prevention."),
        ("Can Mosquitoes Breed in My Home?","Yes. Mosquitoes can breed around homes wherever stagnant water collects. Common areas include plant pots, drains, containers, gutters and other places where water can accumulate."),
        ("Does Rain Increase Mosquito Activity?","Rain can create new breeding sites by leaving stagnant water in containers, drains, gutters and other areas around your property. Regularly checking for and removing standing water after rainfall can help reduce mosquito breeding."),
        ("How Often Should Mosquito Control Be Done?","The appropriate treatment frequency depends on factors such as the property, level of mosquito activity and surrounding environment. Properties with persistent mosquito problems may benefit from regular inspections and scheduled treatments."),
        ("Are Mosquitoes Active During the Day?","Mosquito activity varies between species. Some mosquitoes are more active during the day, while others are more active around dawn, dusk or at night. Mosquitoes may rest in cool, shaded areas when they are not actively feeding."),
        ("How Can I Find Mosquito Breeding Sites?","Check your property regularly for stagnant water in plant pots, containers, drains, gutters, buckets and other areas that can collect water. A professional inspection can also help identify less obvious breeding areas."),
        ("Can Mosquitoes Be Completely Eliminated?","Completely eliminating mosquitoes from an outdoor environment can be difficult because mosquitoes can enter from surrounding areas. However, professional treatment combined with proper prevention can significantly reduce mosquito activity and breeding around your property."),
        ("Are Mosquitoes a Problem for Businesses?","Yes. Mosquitoes can affect customer comfort and employee wellbeing, particularly in restaurants, hotels, resorts, event venues and properties with outdoor areas. Effective mosquito control can help reduce complaints and maintain a more comfortable environment."),
        ("What Should I Do Before Mosquito Treatment?","Keep treatment areas accessible and follow any preparation instructions provided by your pest control technician. Remove or empty containers holding stagnant water where possible, and inform the technician about areas where you have noticed high mosquito activity."),
        ("How Long Does Mosquito Treatment Take?","Treatment time depends on the size and layout of the property, the level of mosquito activity and the areas requiring treatment. Your pest control technician can provide a more accurate estimate after assessing the property."),
        ("Can Mosquitoes Come Back After Treatment?","Yes. Mosquitoes can return if new breeding sites develop or mosquitoes enter from surrounding areas. Removing stagnant water and following recommended treatment schedules can help maintain long-term mosquito control.")],
  resources="Explore our mosquito control guides for practical information on identifying mosquito activity, preventing breeding and keeping your home or business protected.",
 ),
}


def paras(ps): return "".join(f"<p>{p}</p>" for p in ps)


def sign_grid(signs):
    return '<div class="sign-grid">' + "".join(f'<div class="sign"><i>{I["alert"]}</i><div><b>{b}</b><span>{t}</span></div></div>' for b, t in signs) + '</div>'


def build_pest(slug, d):
    file = f"{slug}.html"
    s = d["short"]; sg = d["singular"]
    methods = f'<div class="grid grid-3 reveal-stagger mt-4">' + "".join(f'<div class="card glow"><div class="ic">{I["check"]}</div><h4>{m}</h4><p>{t}</p></div>' for m, t in d["methods"]) + '</div>' if d["methods"] else ""
    pro_list = checks(d["pro"]) if d["pro"] else ""
    pro_outro = f'<p class="muted">{d["pro_outro"]}</p>' if d.get("pro_outro") else ""
    prevent_list = checks(d["prevent"]) if d["prevent"] else ""
    body = page_hero(f'<a href="services.html">Services</a><span>/</span>{d["name"]}', d["name"], d["tagline"], d["hero"], "Pest control")
    body += f'''
<div class="subnav"><div class="container"><ul><li><a href="#what">What are {s}?</a></li><li><a href="#signs">Signs</a></li><li><a href="#treatment">Treatment</a></li><li><a href="#prevent">Prevention</a></li><li><a href="#faq">FAQs</a></li><li><a href="#enquiry">Get a quote</a></li></ul></div></div>
<section class="section"><div class="container two-col">
 <div class="prose">
  <div id="what" class="reveal"><div class="eyebrow">Know your pest</div><h2 class="h2">What Are {s}?</h2><div class="mt-2">{paras(d["what"])}</div></div>
  <div class="reveal"><h3 class="h3">Why Are {s} a Problem?</h3>{paras(d["why"])}</div>
  <div class="reveal"><h3 class="h3">{sg} Damage to Businesses</h3>{paras(d["business"])}</div>
  <div id="signs" class="reveal"><h3 class="h3">Signs of {'a ' if sg != 'Cockroach' and sg != 'Mosquito' else ''}{sg if sg not in ('Cockroach','Mosquito') else s} Infestation{'?' if sg in ('Cockroach','Mosquito') else ''}</h3><p>{d["signs_intro"]}</p>{sign_grid(d["signs"])}<p>{d["signs_outro"]}</p></div>
  <div class="reveal"><h3 class="h3">Where Do {s} Hide?</h3>{paras(d["hide"])}</div>
 </div>
 <aside class="infobox reveal right">
  <span class="badge-lime">Quick facts</span><h4 class="mt-2">{d["name"]}</h4>
  <div class="row"><b>Approach</b><span>Inspect → Identify → Targeted treatment → Follow-up</span></div>
  <div class="row"><b>Suitable for</b><span>Residential, commercial, F&amp;B, hospitality, construction and facilities</span></div>
  <div class="row"><b>Framework</b><span>Integrated Pest Management (IPM), prevention-led</span></div>
  <div class="row"><b>Compliance</b><span>NEA-registered · ISO 9001 · ISO 14001 · ISO 45001 · bizSAFE Star</span></div>
  {btn("Request a quote", "#enquiry", "lime")}{btn("WhatsApp us", WA, "wa", "wa")}
 </aside>
</div></section>
<section class="section dark" id="treatment"><div class="container">
 <div class="section-head" style="align-items:start"><div class="reveal"><div class="eyebrow">Our treatment</div><h2 class="h2">{d["treatment_title"]}</h2></div><div class="reveal">{"".join(f'<p class="lead">{p}</p>' for p in d["treatment"])}</div></div>
 {methods}
 <div class="split mt-5"><div class="reveal left"><h3 class="h3">{d["pro_title"]}</h3><div class="mt-2 light">{paras(d["pro_intro"])}</div>{pro_list}{pro_outro}</div>
 <div class="frame parallax reveal right"><img src="assets/img/{d["hero"]}.jpg" alt="{d["name"]} by Pestimesh"><div class="badge"><b>2011</b><span>Protecting Singapore<br>properties since</span></div></div></div>
</div></section>
<section class="section" id="prevent"><div class="container split">
 <div class="frame reveal left"><img src="assets/img/tp-training-2.jpg" alt="Pestimesh technician on site"></div>
 <div class="reveal right"><div class="eyebrow">Prevention</div><h2 class="h2">{d["prevent_title"]}</h2><div class="mt-2 muted">{paras(d["prevent_intro"])}</div>{prevent_list}{f'<p class="muted">{d["prevent_outro"]}</p>' if d["prevent_outro"] else ''}</div>
</div></section>
<section class="section white" id="faq"><div class="container"><div class="section-head"><div><div class="eyebrow">FAQs</div><h2 class="h2">{s} FAQs</h2></div><p class="lead">Still unsure? Send us a photo and a short description and our team will advise on the next step.</p></div>{faq(d["faqs"])}
<div class="mt-4"><div class="eyebrow">{s} Blogs &amp; Resources</div><p class="muted">{d["resources"]}</p><p class="small muted">To be updated in the future.</p></div></div></section>
{cta_band("Don't Let Pests Take Over Your Space.", "Whether it's a single pest sighting or an ongoing infestation, getting the right solution early can help prevent the problem from becoming bigger. Tell us what you're experiencing and let our team recommend the appropriate next step.")}'''
    return file, page(file, d["name"], d["tagline"], body)
