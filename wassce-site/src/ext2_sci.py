from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

S = "Diversity of Matter"

# ------------------------------------------------------------ rocks & minerals
topic("rocks", "Rocks & mineral exploitation", S, [
    "Three rock types: igneous (cooled magma — granite, basalt), sedimentary (layers of deposits — limestone, "
    "sandstone, shale) and metamorphic (changed by heat and pressure — marble, slate, quartzite).",
    "Rocks break down by weathering — physical (heating and cooling, water), chemical (acids, oxygen) and "
    "biological (roots, lichens) — to form soil.",
    "Ghana's main minerals: gold, bauxite, manganese, diamond, limestone, salt, crude oil and natural gas.",
    "Mining may be surface (open pit, alluvial) or underground (shaft).",
    "Benefits: foreign exchange, employment, raw materials, infrastructure. Problems: land degradation, "
    "water pollution, pits left open, displacement of farmers and mining accidents.",
])
O("Granite is formed when molten magma cools and solidifies. It is therefore ___ rock.",
  ["an igneous", "a sedimentary", "a metamorphic", "an organic"],
  ["Igneous rocks form from cooled magma or lava.", "Sedimentary rocks form from deposited layers."])
O("Which rock type is formed in layers from deposited materials and may contain fossils?",
  ["Sedimentary", "Igneous", "Metamorphic", "Volcanic"],
  ["Sediments settle in layers over long periods, trapping the remains of organisms as fossils."])
O("Marble is formed from limestone by heat and pressure. Marble is therefore ___",
  ["a metamorphic rock", "an igneous rock", "a sedimentary rock", "a mineral ore"],
  ["Metamorphic rocks are existing rocks changed by heat and pressure — limestone → marble, clay → slate."])
O("Which mineral is mined at Awaso in Ghana?", ["Bauxite", "Gold", "Diamond", "Manganese"],
  ["Awaso is a bauxite mining area; Nsuta is known for manganese, Obuasi and Tarkwa for gold, "
   "and Akwatia for diamonds."])
O("Which of these is NOT a problem caused by mining?",
  ["Increase in soil fertility", "Pollution of rivers", "Destruction of farmland", "Open pits left behind"],
  ["Mining removes the topsoil and lowers fertility; it never increases it."])
T("(a) Name the three main types of rock and give one example and one use of each.<br>"
  "(b) Describe two ways in which rocks are broken down to form soil.<br>"
  "(c) State three benefits and three problems of mineral exploitation in Ghana.",
  ["(a) <b>Igneous</b> — granite; used for building stone and road chippings. "
   "<b>Sedimentary</b> — limestone; used for cement and for liming acidic soils. "
   "<b>Metamorphic</b> — marble; used for floor tiles and decoration.",
   "(b) <b>Physical weathering:</b> heating in the day and cooling at night makes rocks expand and contract "
   "until they crack and break into smaller pieces.",
   "<b>Chemical weathering:</b> rain water containing dissolved carbon dioxide forms a weak acid that "
   "dissolves minerals such as limestone. (Biological: roots and lichens widen cracks.)",
   "(c) <b>Benefits:</b> foreign exchange from exports; employment for mine workers and suppliers; "
   "raw materials for industry; roads, schools and clinics built by mining companies; royalties and taxes.",
   "<b>Problems:</b> farmland and forests destroyed; rivers polluted with silt and mercury; pits left open, "
   "causing drownings; farmers displaced; mine accidents and dust-related diseases."], marks=15)
extras("rocks",
  plain="Rocks are the solid material the earth is made of; minerals are the useful substances inside them. "
        "Igneous rocks cooled from magma, sedimentary rocks settled in layers, and metamorphic rocks were "
        "changed by heat and pressure.",
  examples=[
    E("How can you tell a sedimentary rock from an igneous one in the field?",
      "Step 1. Look for layers (strata) — sedimentary rocks are usually layered; igneous rocks are not.",
      "Step 2. Look for fossils — only sedimentary rocks contain them.",
      "Step 3. Feel the grain — many igneous rocks have interlocking crystals and feel hard and even."),
    E("Explain how a gold mining company can reduce the damage it causes.",
      "Step 1. Keep out of forest reserves and river buffers, and treat waste water before releasing it.",
      "Step 2. Store the topsoil, then replace it and replant trees after mining — land reclamation.",
      "Step 3. Fill or fence the pits, provide protective gear, and resettle or compensate affected farmers fairly.",
      fig=draw.flow(["Clear & store topsoil", "Mine the ore", "Refill the pit", "Replace soil & replant"],
                    note="Mining with land reclamation", label="Reclaiming mined land"))])

S = "Cycles"

# ------------------------------------------------------------ farm tools & machinery
topic("farmtools", "Farm tools, machinery & safety", S, [
    "Simple tools: cutlass (clearing), hoe (weeding and ridging), mattock (digging), rake, watering can, "
    "secateurs (pruning), knapsack sprayer (chemicals), head pan.",
    "Machinery: tractor and its implements — plough (turns the soil), harrow (breaks clods), ridger (makes ridges), "
    "planter, combine harvester, maize sheller, irrigation pump.",
    "Care of tools: clean after use, sharpen cutting edges, oil metal parts, replace loose handles, store in a dry shed.",
    "Safety: wear protective clothing, boots and gloves; never spray against the wind; wash after using chemicals; "
    "keep children away from machines; service machines before the season.",
    "Advantages of machinery: speed, large areas, less drudgery. Disadvantages: high cost, fuel and spare parts, "
    "trained operators needed, and soil compaction.",
])
O("Which tool is most suitable for making ridges on a small farm?", ["Hoe", "Secateurs", "Rake", "Watering can"],
  ["The hoe is used for weeding, making mounds and ridging on small holdings.",
   "Secateurs prune, and a rake gathers trash."])
O("Which tractor implement is used to break up clods after ploughing?", ["Harrow", "Plough", "Planter", "Trailer"],
  ["The plough turns the soil over; the harrow then breaks the big clods into a fine tilth for planting."])
O("Why should a cutlass be cleaned and oiled after use?",
  ["To prevent rusting and make it last longer", "To make it heavier",
   "To change its shape", "To make it a better conductor"],
  ["Soil and sap hold moisture against the blade; cleaning and a light oiling keep oxygen and water away, "
   "so rusting is prevented."])
O("A farmer spraying a chemical should stand ___",
  ["with the wind behind him", "facing the wind",
   "under a tree in the farm", "downwind of the sprayer"],
  ["Spraying with the wind behind you carries the chemical away from your face and body."])
O("Which is a disadvantage of using heavy machinery on a farm?",
  ["It compacts the soil", "It saves time", "It covers large areas", "It reduces drudgery"],
  ["Repeated passes of heavy machines press the soil down, reducing air spaces and root growth. "
   "The other three are advantages."])
T("(a) Name four farm tools and state one use of each.<br>(b) State four ways of maintaining farm tools.<br>"
  "(c) State four safety precautions a farmer should observe when using agrochemicals.",
  ["(a) <b>Cutlass</b> — clearing bush and harvesting; <b>hoe</b> — weeding, making mounds and ridges; "
   "<b>mattock/pick-axe</b> — digging hard ground and stumping; <b>watering can</b> — watering seedlings; "
   "<b>secateurs</b> — pruning; <b>knapsack sprayer</b> — applying chemicals.",
   "(b) Clean off soil and sap after every use; sharpen cutting edges regularly; oil or grease metal parts; "
   "tighten or replace loose handles; store in a dry, locked shed off the ground.",
   "(c) Read the label and use the stated dose; wear protective clothing, boots, gloves and a nose mask; "
   "spray with the wind behind you, not against it; do not eat, drink or smoke while spraying; "
   "wash hands, body and clothes afterwards; keep chemicals and empty containers away from children, "
   "food and water sources, and observe the pre-harvest interval."], marks=12)
extras("farmtools",
  plain="Tools and machines decide how much one farmer can do in a day. Simple tools are cheap and need no "
        "fuel; machines cover large areas fast but cost a lot and need skill and servicing.",
  examples=[
    E("Put these in the right order for preparing land with a tractor: ridging, harrowing, ploughing, clearing.",
      "Step 1. <b>Clearing</b> — remove the vegetation and stumps.",
      "Step 2. <b>Ploughing</b> — turn the soil over to bury trash and loosen it.",
      "Step 3. <b>Harrowing</b> — break the clods into a fine tilth.",
      "Step 4. <b>Ridging</b> — make ridges or beds, then plant.",
      fig=draw.flow(["Clearing", "Ploughing", "Harrowing", "Ridging"],
                    note="Preparing land with a tractor", label="Land preparation order")),
    E("A farmer's knapsack sprayer leaks onto his back while spraying. What should he do?",
      "Step 1. Stop at once and move away from the spray area.",
      "Step 2. Remove the contaminated clothing and wash the skin with plenty of soap and water.",
      "Step 3. Repair or replace the faulty sprayer before using it again, and report to a clinic "
      "if he feels unwell, taking the chemical label with him.")])

S = "Systems"

# ------------------------------------------------------------ teeth
topic("teeth", "Teeth & dentition", S, [
    "Types of teeth: incisors (cutting), canines (tearing), premolars and molars (chewing and grinding).",
    "An adult human has 32 teeth; the dental formula is I 2/2, C 1/1, PM 2/2, M 3/3 — for one half of each jaw.",
    "Milk (deciduous) teeth number 20 and are replaced by permanent teeth.",
    "Structure of a tooth: enamel (hard outer layer), dentine, pulp cavity (nerves and blood vessels), cement and root.",
    "Dental caries (tooth decay) is caused by bacteria acting on sugar to form acid, which dissolves the enamel.",
    "Care: brush twice daily, reduce sugary foods, rinse after meals, visit a dentist, and avoid using teeth as tools.",
])
O("Which type of tooth is best suited for tearing flesh?", ["Canine", "Incisor", "Premolar", "Molar"],
  ["Canines are long and pointed, so they grip and tear.", "Incisors are chisel-shaped for cutting."])
O("How many teeth does a normal adult human have?", ["32", "20", "28", "36"],
  ["An adult has 32 permanent teeth; a young child has 20 milk teeth."], v=32)
O("The hardest substance covering the crown of a tooth is the ___", ["enamel", "dentine", "pulp", "cement"],
  ["Enamel is the hardest substance in the body; beneath it lies dentine, and the pulp holds nerves "
   "and blood vessels."])
O("Dental caries is caused mainly by ___",
  ["acid produced by bacteria acting on sugar", "eating too much protein",
   "drinking cold water", "brushing the teeth"],
  ["Bacteria in plaque turn sugar into acid, and the acid dissolves the enamel — so sugary food and poor "
   "brushing are the real causes."])
O("Which of these would best protect a child's teeth?",
  ["Brushing twice daily and cutting down on sweets", "Chewing bottle tops",
   "Rinsing with hot water only", "Using the teeth to open tins"],
  ["Cleaning removes the plaque and less sugar means less acid; using teeth as tools cracks them."])
T("(a) Name the four types of human teeth and state the function of each.<br>"
  "(b) Draw and label a longitudinal section of a tooth (five labels).<br>"
  "(c) Explain how tooth decay happens and state four ways of preventing it.",
  ["(a) <b>Incisors</b> — chisel-shaped, for cutting and biting. <b>Canines</b> — pointed, for tearing. "
   "<b>Premolars</b> — broad with cusps, for crushing. <b>Molars</b> — largest and broadest, for grinding.",
   "(b) Labels: enamel, dentine, pulp cavity (with nerves and blood vessels), cement, root, gum, crown.",
   "(c) Food, especially sugar, sticks to the teeth and forms plaque with bacteria. The bacteria break down "
   "the sugar to acid; the acid dissolves the enamel, then the dentine, until the pulp is reached and the "
   "tooth aches.",
   "Prevention: brush at least twice a day with fluoride toothpaste; reduce sugary foods and drinks; "
   "rinse the mouth after eating; eat foods rich in calcium and vitamin D; visit the dentist regularly; "
   "do not use the teeth to crack hard objects."], marks=15)
extras("teeth",
  plain="Teeth are the body's first food processor. Each shape does a different job, and all of them depend "
        "on one thin layer — enamel — which the body cannot replace once acid has eaten through it.",
  examples=[
    E("Why do dentists say the damage is done by HOW OFTEN you eat sugar, not just how much?",
      "Step 1. Every time sugar reaches the mouth, bacteria produce acid within minutes.",
      "Step 2. Saliva needs about half an hour to wash the acid away and restore the mouth.",
      "Step 3. Sweets eaten one at a time all afternoon keep the mouth acidic for hours, "
      "while the same sweets eaten at one sitting give the saliva time to recover."),
    E("Compare the dentition of a goat with that of a dog.",
      "Step 1. A goat is a herbivore: it has broad molars for grinding grass, a horny pad instead of upper "
      "incisors, and a gap (diastema) where the tongue moves the food.",
      "Step 2. A dog is a carnivore: it has long canines for tearing and carnassial teeth for shearing meat.",
      "Step 3. The teeth match the diet — that is the point the examiner is testing.")])

# ------------------------------------------------------------ hormones
topic("hormone", "Hormones & the endocrine system", S, [
    "Hormones are chemical messengers made by endocrine (ductless) glands and carried in the blood.",
    "Pituitary — the 'master gland': growth hormone and hormones that control other glands.",
    "Thyroid — thyroxine, controls the rate of metabolism; it needs iodine, and a shortage causes goitre.",
    "Pancreas — insulin lowers blood sugar; too little insulin leads to diabetes mellitus.",
    "Adrenal glands — adrenaline, the 'fight or flight' hormone: faster heartbeat and breathing.",
    "Testes — testosterone; ovaries — oestrogen and progesterone: these control the changes of puberty.",
    "Nervous messages are fast and short-lived; hormonal messages are slower but last longer.",
])
O("Hormones are transported round the body in the ___", ["blood", "nerves", "lymph vessels only", "air passages"],
  ["Endocrine glands have no ducts; they release their hormones straight into the bloodstream."])
O("Which gland produces insulin?", ["Pancreas", "Thyroid", "Pituitary", "Adrenal"],
  ["The islets of Langerhans in the pancreas produce insulin, which lowers blood sugar."])
O("A shortage of iodine in the diet leads to ___", ["goitre", "rickets", "scurvy", "anaemia"],
  ["Iodine is needed to make thyroxine; without it the thyroid swells, which is goitre.",
   "Iodised salt prevents it."])
O("Which hormone prepares the body for 'fight or flight'?", ["Adrenaline", "Insulin", "Thyroxine", "Oestrogen"],
  ["Adrenaline from the adrenal glands raises the heartbeat, breathing rate and blood sugar in an emergency."])
O("Which statement about nervous and hormonal control is correct?",
  ["Nervous messages are faster but shorter-lasting than hormonal ones",
   "Hormonal messages travel along nerves", "Nervous control is slower than hormonal control",
   "Hormones act only on the gland that made them"],
  ["Impulses travel in a fraction of a second and their effect ends quickly; hormones travel in the blood "
   "and their effects last much longer."])
T("(a) What are hormones?<br>(b) Name four endocrine glands, the hormone each produces and its effect.<br>"
  "(c) State two differences between nervous and hormonal coordination.<br>"
  "(d) Explain what happens in the body of a person whose pancreas produces too little insulin.",
  ["(a) Hormones are chemical substances produced in small quantities by endocrine (ductless) glands and "
   "carried by the blood to target organs, where they control or regulate activities.",
   "(b) <b>Pituitary</b> — growth hormone — controls growth and other glands. "
   "<b>Thyroid</b> — thyroxine — controls the rate of metabolism. "
   "<b>Pancreas</b> — insulin — lowers blood sugar. "
   "<b>Adrenal</b> — adrenaline — prepares the body for emergency. "
   "(Also testes — testosterone; ovaries — oestrogen.)",
   "(c) Nervous messages are electrical impulses along nerves, very fast, with short-lived effects on "
   "particular muscles or glands; hormonal messages are chemicals in the blood, slower to act, "
   "and their effects are widespread and longer lasting.",
   "(d) Blood sugar is not taken into the cells properly, so it rises. The person passes much urine, feels "
   "thirsty and tired, loses weight, and wounds heal slowly — the condition is diabetes mellitus. "
   "It is managed with diet, exercise and, where prescribed, insulin."], marks=15)
extras("hormone",
  plain="Hormones are the body's slow messengers. The nervous system sends a quick telegram; the hormone "
        "system posts a letter that keeps working for hours or years — such as the hormones of puberty.",
  examples=[
    E("A student is suddenly frightened by a snake. Describe what adrenaline does.",
      "Step 1. The adrenal glands release adrenaline into the blood.",
      "Step 2. The heart beats faster and breathing deepens, so more oxygen and glucose reach the muscles.",
      "Step 3. Stored glycogen is changed to glucose for energy, the pupils widen and blood is directed "
      "to the muscles — the body is ready to run or to fight."),
    E("Why is iodised salt sold in Ghana?",
      "Step 1. Soils in some areas contain little iodine, so local foods supply little.",
      "Step 2. Without iodine the thyroid cannot make thyroxine and swells, causing goitre; "
      "in children it also slows growth and mental development.",
      "Step 3. Adding iodine to common salt reaches everybody cheaply, so the deficiency is prevented.")])

# ------------------------------------------------------------ food preservation
topic("preserve", "Food preservation & processing", S, [
    "Food spoils because of micro-organisms (bacteria, moulds), enzymes in the food, insects, rodents and moisture.",
    "Preservation works by removing water, excluding air, lowering temperature, or adding substances that "
    "micro-organisms cannot live in.",
    "Methods: sun drying, smoking, salting, sugaring, canning and bottling, refrigeration and freezing, "
    "pasteurisation, frying in oil, and chemical preservatives.",
    "Local examples: smoked fish, dried pepper and okra, gari from cassava, salted fish (koobi), shea butter.",
    "Good storage: dry the produce well, store in clean airtight containers or silos, raise sacks off the floor, "
    "and protect against rodents and weevils.",
])
O("The main reason for drying fish in the sun is to ___",
  ["remove water that micro-organisms need", "add salt to the fish",
   "make the fish heavier", "increase its protein content"],
  ["Bacteria and moulds need moisture; removing the water stops them from growing."])
O("Which method of preservation works by killing micro-organisms with heat and then sealing out air?",
  ["Canning", "Salting", "Freezing", "Smoking"],
  ["In canning the food is heated to destroy micro-organisms and sealed in an airtight tin."])
O("Refrigeration preserves food because low temperature ___",
  ["slows the growth of micro-organisms", "kills all micro-organisms",
   "removes all the water", "adds preservatives to the food"],
  ["Cold slows down the organisms and the enzymes; it does not kill them, which is why thawed food spoils quickly."])
O("Gari is made from ___", ["cassava", "maize", "millet", "yam"],
  ["Cassava is grated, pressed to remove the liquid, fermented and roasted to give gari, which keeps for months."])
O("Which of these would best protect stored maize from weevils?",
  ["Drying well and storing in airtight bags", "Storing while still moist",
   "Keeping the sacks directly on a damp floor", "Leaving the store open at night"],
  ["Weevils and moulds need moisture and air; dry grain in hermetic (airtight) bags denies them both."])
T("(a) State four causes of food spoilage.<br>(b) Describe four methods of food preservation, giving a local "
  "example of each.<br>(c) State three advantages of food preservation to a farming community.",
  ["(a) Micro-organisms (bacteria, moulds, yeasts); enzymes within the food itself; insects, rodents and birds; "
   "moisture and warmth; rough handling that bruises the produce.",
   "(b) <b>Sun drying</b> — pepper, okra and maize are spread in the sun to remove moisture. "
   "<b>Smoking</b> — fish is smoked over a fire; the heat dries it and the smoke contains preserving chemicals. "
   "<b>Salting</b> — koobi and other fish are packed in salt, which draws out water. "
   "<b>Refrigeration/freezing</b> — meat and fish are kept cold so that organisms cannot multiply. "
   "(Also canning, frying, and processing cassava into gari.)",
   "(c) Food is available in the lean season, so prices and hunger are reduced; farmers avoid selling "
   "everything cheaply at harvest and can wait for better prices; post-harvest losses are cut; "
   "processed products such as gari and shea butter add value and create jobs."], marks=15)
extras("preserve",
  plain="Food goes bad because tiny organisms feed on it. Every preservation method simply takes away "
        "something they need — water, air, warmth — or adds something they cannot survive, like salt.",
  examples=[
    E("Why does smoked fish keep longer than fresh fish?",
      "Step 1. The heat of the fire dries the fish, removing the water micro-organisms need.",
      "Step 2. The heat also kills many of the organisms already on it.",
      "Step 3. Chemicals in the smoke itself slow the growth of bacteria and moulds, and the dry surface "
      "keeps new ones out."),
    E("A farmer harvests 20 bags of maize and loses 5 bags to weevils. Work out his loss and suggest two remedies.",
      f"Step 1. Loss = {F(5,20)} × 100 = <b>25%</b> of the harvest.",
      "Step 2. Remedy 1: dry the grain to the right moisture level before storing.",
      "Step 3. Remedy 2: store in airtight (hermetic) bags or a treated silo, raised off the floor, "
      "and keep the store clean and rodent-proof.")])
assert 5 / 20 * 100 == 25

S = "Interactions of Matter"

# ------------------------------------------------------------ magnetism
topic("magnet", "Magnetism", S, [
    "Magnetic materials: iron, steel, cobalt, nickel. Non-magnetic: wood, plastic, copper, aluminium, glass.",
    "Like poles repel; unlike poles attract. REPULSION is the only sure test for a magnet.",
    "A freely suspended magnet comes to rest pointing north–south — the basis of the compass.",
    "Magnets can be made by stroking with another magnet, by induction, or electrically with a d.c. current in a coil.",
    "A magnet loses its magnetism when heated strongly, hammered, dropped repeatedly or stored carelessly.",
    "Keep bar magnets in pairs with unlike poles together and keepers across the ends.",
    "An electromagnet is a soft-iron core inside a coil; its magnetism can be switched on and off.",
])
O("Which material is attracted by a magnet?", ["Steel", "Copper", "Aluminium", "Plastic"],
  ["Iron, steel, cobalt and nickel are magnetic materials; copper and aluminium are not."])
O("The only sure test for a magnet is ___",
  ["repulsion", "attraction of iron filings", "attraction of a nail", "pointing north when hung"],
  ["A magnet attracts any magnetic material, but only another magnet is REPELLED by a like pole."])
O("A soft-iron core is used in an electromagnet because it ___",
  ["is easily magnetised and demagnetised", "keeps its magnetism for ever",
   "does not conduct electricity", "is cheaper than every other metal"],
  ["Soft iron gains strong magnetism when the current flows and loses it at once when the current stops, "
   "which is what a switchable magnet needs. Steel is used for permanent magnets."])
O("Which of these would make a magnet lose its magnetism?",
  ["Heating it strongly", "Keeping it with a keeper", "Storing it in pairs", "Keeping it away from heat"],
  ["Strong heating, hammering and repeated dropping disturb the arrangement inside the magnet and weaken it."])
O("A magnet is cut into two equal halves. Each piece will ___",
  ["have both a north and a south pole", "have only a north pole",
   "have only a south pole", "lose its magnetism completely"],
  ["However small the piece, it is still a magnet with two poles — you cannot get a single pole by cutting."])
T("(a) State three properties of magnets.<br>(b) Describe how you would make a steel bar into a magnet by "
  "the stroking method.<br>(c) State two differences between an electromagnet and a permanent magnet, and "
  "give two uses of an electromagnet.",
  ["(a) Like poles repel and unlike poles attract; a freely suspended magnet points north–south; "
   "the magnetic force is strongest at the poles; a magnet attracts magnetic materials and can induce "
   "magnetism in them.",
   "(b) Place the steel bar on the bench. Stroke it from one end to the other with ONE pole of a bar magnet, "
   "always in the same direction, lifting the magnet high at the end of each stroke. Repeat about thirty times. "
   "The end where the stroking finishes becomes a pole opposite to the stroking pole. Test it with another magnet.",
   "(c) <b>Differences:</b> an electromagnet works only while current flows and its strength can be varied, "
   "while a permanent magnet keeps its magnetism all the time; an electromagnet uses a soft-iron core, "
   "a permanent magnet is made of steel.",
   "<b>Uses of an electromagnet:</b> lifting scrap iron in a crane; electric bells; relays and circuit breakers; "
   "loudspeakers, electric motors and generators."], marks=12)
extras("magnet",
  plain="A magnet pulls on iron and steel and always has two poles. The one test you can trust is repulsion — "
        "a magnet attracts plenty of things, but only another magnet pushes back.",
  examples=[
    E("You are given two identical steel bars; one is a magnet. How do you tell which?",
      "Step 1. Bring one end of bar A near the MIDDLE of bar B.",
      "Step 2. If there is attraction, A could still be either — a magnet attracts unmagnetised steel too.",
      "Step 3. The sure test: bring the ends together both ways round. If you ever feel a push (repulsion), "
      "<b>both are magnets</b>. If one end always attracts and never repels anywhere, that one is the plain steel."),
    E("How would you increase the strength of an electromagnet?",
      "Step 1. Increase the current flowing through the coil.",
      "Step 2. Increase the number of turns of wire on the coil.",
      "Step 3. Use a soft-iron core rather than an air core, and bring the poles closer to the load.")])
