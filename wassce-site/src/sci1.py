from core import *

S = "Diversity of Matter"

# ------------------------------------------------------------------ 1
topic("measure", "Science & measurement", S, [
    "SI base units: metre (length), kilogram (mass), second (time), kelvin (temperature), ampere (current), mole (amount).",
    "Density = mass ÷ volume. Units: g/cm³ or kg/m³.  1 g/cm³ = 1000 kg/m³",
    "Volume of an irregular solid = volume of water displaced (use a eureka can or measuring cylinder).",
    "Instruments: vernier callipers (small lengths), micrometer screw gauge (wire diameter), beam balance (mass), stop-watch (time).",
    "The scientific method: observation → hypothesis → experiment → results → conclusion.",
])
O("A block of mass 240 g has a volume of 30 cm³. Calculate its density.",
  ["8.0 g/cm³", "0.125 g/cm³", "7200 g/cm³", "270 g/cm³"],
  ["Density = mass ÷ volume", "= 240 ÷ 30 = 8.0 g/cm³"], v=240 / 30, nv=[8.0, 0.125, 7200, 270])
O("Which instrument is most suitable for measuring the diameter of a thin wire?",
  ["Micrometer screw gauge", "Metre rule", "Measuring cylinder", "Beam balance"],
  ["A micrometer screw gauge reads to 0.01 mm, which a metre rule cannot do."])
O("A stone is lowered into a measuring cylinder containing 40 cm³ of water. The level rises to 65 cm³. What is the volume of the stone?",
  ["25 cm³", "105 cm³", "40 cm³", "65 cm³"],
  ["The stone displaces its own volume of water.", "Volume = 65 − 40 = 25 cm³"], v=65 - 40)
O("Which of the following is NOT an SI base unit?", ["newton", "kilogram", "second", "ampere"],
  ["The newton is a derived unit (1 N = 1 kg m s⁻²).", "The others are base units."])
O("The mass of an empty beaker is 50 g. When filled with 20 cm³ of a liquid, the total mass is 66 g. What is the density of the liquid?",
  ["0.8 g/cm³", "3.3 g/cm³", "1.25 g/cm³", "16 g/cm³"],
  ["Mass of liquid = 66 − 50 = 16 g", "Density = 16 ÷ 20 = 0.8 g/cm³"], v=(66 - 50) / 20, nv=[0.8, 3.3, 1.25, 16])
T("(a) State the scientific method in the correct order.<br>(b) A piece of metal has a mass of 89 g and a volume of 10 cm³. "
  "(i) Calculate its density in g/cm³ and in kg/m³. (ii) Suggest what the metal is likely to be.<br>"
  "(c) Describe how you would find the density of an irregular stone in the laboratory.",
  ["(a) Observation → statement of the problem → hypothesis → experiment (with a control) → collection of results → analysis → conclusion.",
   "(b)(i) Density = 89 ÷ 10 = <b>8.9 g/cm³</b> = 8.9 × 1000 = <b>8900 kg/m³</b>",
   "(ii) A density of 8.9 g/cm³ suggests <b>copper</b>.",
   "(c) Find the mass of the dry stone on a beam balance.",
   "Pour water into a measuring cylinder and record the volume V₁.",
   "Tie the stone with a thread, lower it gently into the water and record the new volume V₂.",
   "Volume of the stone = V₂ − V₁; density = mass ÷ (V₂ − V₁)."], marks=10,
  ok=(89 / 10 == 8.9 and 8.9 * 1000 == 8900))

# ------------------------------------------------------------------ 2
topic("living", "Living & non-living things", S, [
    "Characteristics of living things: Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition (MRS GREN).",
    "Non-living things may show one or two of these (a car moves, a crystal 'grows') but never all of them.",
    "Plants and animals differ in nutrition (plants make their own food), movement, growth and response.",
    "Irritability (sensitivity) is the ability to respond to a stimulus.",
])
O("Which of the following is NOT a characteristic of living things?", ["Rusting", "Excretion", "Irritability", "Reproduction"],
  ["Rusting is a chemical change in iron, not a life process."])
O("A car moves, uses fuel and gives off exhaust gases, yet it is not living. This is because a car cannot ___",
  ["reproduce and grow", "move", "use energy", "give off waste"],
  ["A living thing must show ALL the life processes; a car cannot reproduce itself or grow."])
O("The ability of a plant shoot to grow towards light is an example of ___",
  ["sensitivity", "excretion", "nutrition", "reproduction"],
  ["Responding to a stimulus (light) is sensitivity, or irritability; this particular response is called phototropism."])
O("Which process removes metabolic waste from the body of an organism?", ["Excretion", "Egestion", "Secretion", "Digestion"],
  ["Excretion removes waste made BY the body (urea, carbon dioxide).",
   "Egestion removes undigested food, which was never part of the body's chemistry."])
O("Green plants differ from animals in that plants ___",
  ["make their own food", "respire", "grow", "respond to stimuli"],
  ["Plants are autotrophic — they make food by photosynthesis. The other three are shown by both."])
T("(a) State five characteristics of living things.<br>(b) Give two differences between plants and animals.<br>"
  "(c) Explain why a growing crystal is not considered a living thing.",
  ["(a) Movement, respiration, sensitivity (irritability), growth, reproduction, excretion and nutrition — any five.",
   "(b) 1. Plants make their own food by photosynthesis; animals feed on ready-made food.",
   "2. Most plants are fixed in one place, while animals move from place to place. (Others: plants grow throughout life at growing points; animals have a limited growth period. Plant cells have cellulose walls and chloroplasts.)",
   "(c) A crystal only enlarges by adding more of the same substance from outside. It does not feed, respire, excrete, respond or reproduce, "
   "and its 'growth' is not from within, so it shows only one apparent life process."], marks=10)

# ------------------------------------------------------------------ 3
topic("classify", "Classification of living things", S, [
    "Order of classification: Kingdom → Phylum → Class → Order → Family → Genus → Species.",
    "Five kingdoms: Monera (bacteria), Protista, Fungi, Plantae, Animalia.",
    "Vertebrates: fish, amphibians, reptiles, birds, mammals.",
    "Binomial name: genus (capital) + species (small letters), e.g. <i>Homo sapiens</i>, written in italics or underlined.",
    "Arthropods have jointed legs and an exoskeleton: insects (3 body parts, 6 legs), arachnids (2 parts, 8 legs), crustaceans, myriapods.",
])
O("The correct order of classification from the largest group to the smallest is ___",
  ["kingdom, phylum, class, order, family, genus, species",
   "kingdom, class, phylum, family, order, genus, species",
   "species, genus, family, order, class, phylum, kingdom",
   "phylum, kingdom, class, family, order, genus, species"],
  ["Kingdom is the largest group and species the smallest."])
O("An animal with three body parts and three pairs of legs belongs to the class ___",
  ["Insecta", "Arachnida", "Crustacea", "Myriapoda"],
  ["Insects have head, thorax and abdomen with six legs.", "Arachnids (spiders) have two body parts and eight legs."])
O("Which group of vertebrates has a constant body temperature and a body covered with hair?",
  ["Mammals", "Reptiles", "Amphibians", "Fish"],
  ["Mammals are warm-blooded (homoiothermic), have hair and feed their young on milk."])
O("In the name <i>Zea mays</i>, the word <i>Zea</i> refers to the ___", ["genus", "species", "family", "class"],
  ["In a binomial name the first word (with a capital letter) is the genus and the second is the species."])
O("Which kingdom contains organisms that have no true nucleus?", ["Monera", "Fungi", "Protista", "Plantae"],
  ["Monera (bacteria and blue-green algae) are prokaryotes — their genetic material is not enclosed in a nuclear membrane."])
T("(a) State two reasons why living things are classified.<br>(b) Name the five kingdoms of living things and give one example of each.<br>"
  "(c) State three differences between insects and arachnids.",
  ["(a) To make the study of the great variety of organisms easier and more orderly; to show relationships and evolutionary links between organisms; "
   "to make identification and communication among scientists easier (any two).",
   "(b) Monera — bacteria; Protista — <i>Amoeba</i>/<i>Paramecium</i>; Fungi — mushroom/mould; Plantae — maize; Animalia — goat.",
   "(c) 1. Insects have three body parts (head, thorax, abdomen); arachnids have two (cephalothorax and abdomen).",
   "2. Insects have three pairs of legs; arachnids have four pairs.",
   "3. Insects have antennae and usually wings; arachnids have neither."], marks=10)

# ------------------------------------------------------------------ 4
topic("cells", "Cells & their structures", S, [
    "The cell is the basic unit of life. Cell → tissue → organ → system → organism.",
    "Plant cells have a cellulose cell wall, chloroplasts and a large permanent vacuole; animal cells do not.",
    "Nucleus controls the cell; mitochondria release energy; ribosomes make protein; the cell membrane controls what enters and leaves.",
    "Osmosis is the movement of water from a dilute to a concentrated solution through a semi-permeable membrane.",
    "Diffusion is the movement of particles from a region of higher to lower concentration.",
])
O("Which structure is found in a plant cell but NOT in an animal cell?", ["Cell wall", "Cell membrane", "Nucleus", "Mitochondrion"],
  ["The cellulose cell wall is found only in plant cells."])
O("The part of the cell that controls the entry and exit of substances is the ___",
  ["cell membrane", "cell wall", "nucleus", "vacuole"],
  ["The cell membrane is selectively (semi-) permeable."])
O("Energy is released in the cell mainly in the ___", ["mitochondria", "ribosomes", "nucleus", "vacuole"],
  ["Mitochondria are the sites of aerobic respiration, so they are called the powerhouse of the cell."])
O("A fresh piece of yam placed in concentrated salt solution becomes soft and loses weight. This is because water moves out of the cells by ___",
  ["osmosis", "diffusion of salt", "active transport", "transpiration"],
  ["Water passes from the dilute cell sap to the more concentrated salt solution through the semi-permeable membrane — osmosis."])
O("The correct order of organisation in a living organism is ___",
  ["cell → tissue → organ → system", "tissue → cell → organ → system",
   "organ → tissue → cell → system", "cell → organ → tissue → system"],
  ["Cells of the same kind form tissues, tissues form organs, and organs working together form a system."])
T("(a) Draw and label a plant cell (six labels).<br>(b) State three differences between a plant cell and an animal cell.<br>"
  "(c) Describe an experiment to demonstrate osmosis using a fresh potato or yam tuber.",
  ["(a) Labels: cell wall, cell membrane, cytoplasm, nucleus, chloroplast, vacuole (also: cell sap, mitochondrion).",
   "(b) 1. A plant cell has a cellulose cell wall; an animal cell has only a cell membrane.",
   "2. A plant cell has chloroplasts; an animal cell has none.",
   "3. A plant cell has one large permanent vacuole; an animal cell has small temporary vacuoles or none.",
   "(c) Cut two equal cups out of a peeled potato/yam tuber. Half-fill one with concentrated sugar or salt solution (A) and leave the other empty (B, the control).",
   "Stand both in a dish of water so that the water is below the rim, and leave for about an hour.",
   "<b>Result:</b> the level of solution in A rises, while B stays as it was.",
   "<b>Conclusion:</b> water moved from the dish (dilute) through the living tuber tissue into the concentrated solution — osmosis."], marks=12)

# ------------------------------------------------------------------ 5
topic("matter", "Matter, elements, compounds & mixtures", S, [
    "Matter is anything that has mass and occupies space; it exists as solid, liquid or gas.",
    "An atom has protons (+) and neutrons in the nucleus, with electrons (−) in shells: 2, 8, 8…",
    "Atomic number = number of protons; mass number = protons + neutrons.",
    "A compound's parts are chemically combined in fixed proportions; a mixture's are not, and can be separated physically.",
    "Separation: filtration (insoluble solid), evaporation/crystallisation (dissolved solid), distillation (solvent), chromatography (dyes), magnet (iron).",
])
O("An atom has an atomic number of 11 and a mass number of 23. How many neutrons does it have?",
  ["12", "11", "23", "34"],
  ["Neutrons = mass number − atomic number", "= 23 − 11 = 12"], v=23 - 11)
O("Which of the following is a compound?", ["Water", "Air", "Brass", "Soil"],
  ["Water is made of hydrogen and oxygen chemically combined in a fixed ratio.",
   "Air, brass and soil are mixtures."])
O("Which method would you use to obtain pure water from sea water?",
  ["Distillation", "Filtration", "Evaporation to dryness", "Decantation"],
  ["Distillation vaporises the water and condenses it, leaving the dissolved salts behind.",
   "Evaporation to dryness would give the salt, not the water."])
O("The electron configuration of an element with atomic number 12 is ___", ["2, 8, 2", "2, 8, 8", "8, 2, 2", "2, 2, 8"],
  ["Fill the shells in order: 2, then 8, leaving 2 — so 2, 8, 2.",
   "Two electrons in the outermost shell means it is in Group II (magnesium)."])
O("A mixture of iron filings and sulphur can best be separated by ___",
  ["using a magnet", "filtering", "distilling", "heating strongly"],
  ["Iron is magnetic and sulphur is not, so a magnet separates them.",
   "Heating would make them react chemically to form iron(II) sulphide."])
T("(a) Give three differences between a compound and a mixture.<br>"
  "(b) An atom of an element X has 17 protons and 18 neutrons. State (i) its atomic number; (ii) its mass number; (iii) its electron configuration; (iv) the group to which it belongs.<br>"
  "(c) Describe how you would obtain pure salt from a mixture of salt and sand.",
  ["(a) 1. The parts of a compound are chemically combined; those of a mixture are only physically mixed.",
   "2. A compound has a fixed composition by mass; a mixture can be in any proportion.",
   "3. A compound's properties differ from those of its elements, and it can only be separated chemically; a mixture keeps the properties of its parts and separates physically.",
   "(b)(i) <b>17</b> &nbsp;(ii) 17 + 18 = <b>35</b> &nbsp;(iii) <b>2, 8, 7</b> &nbsp;(iv) seven outer electrons ⇒ <b>Group VII</b> (it is chlorine).",
   "(c) Add water to the mixture and stir — the salt dissolves and the sand does not.",
   "Filter: the sand remains on the filter paper as residue and the salt solution passes through as filtrate.",
   "Evaporate the filtrate to the point of crystallisation and allow it to cool, or evaporate to dryness, to obtain the salt."], marks=12,
  ok=(17 + 18 == 35))

# ------------------------------------------------------------------ 6
topic("acids", "Acids, bases & salts", S, [
    "Acids turn blue litmus red, have pH below 7 and react with metals to give hydrogen.",
    "Bases (alkalis when soluble) turn red litmus blue and have pH above 7.",
    "Acid + base → salt + water (neutralisation);  acid + carbonate → salt + water + carbon dioxide.",
    "pH 7 is neutral (pure water). The lower the pH, the stronger the acid.",
    "Everyday acids: citric (citrus), acetic (vinegar), lactic (sour milk), tannic (tea). Bases: wood ash, lime, caustic soda, antacids.",
])
O("A solution turns blue litmus paper red. The solution is most likely to have a pH of ___", ["3", "7", "9", "12"],
  ["Turning blue litmus red shows an acid, so the pH must be below 7."])
O("Which gas is produced when dilute hydrochloric acid reacts with zinc?",
  ["Hydrogen", "Oxygen", "Carbon dioxide", "Nitrogen"],
  ["Acid + metal → salt + hydrogen.", "The gas burns with a 'pop' sound when tested with a lighted splint."])
O("The reaction between an acid and a base to form salt and water only is called ___",
  ["neutralisation", "hydrolysis", "oxidation", "displacement"],
  ["It is neutralisation: H⁺ from the acid joins OH⁻ from the base to form water."])
O("Which of these would best relieve indigestion caused by excess acid in the stomach?",
  ["Magnesium hydroxide", "Lemon juice", "Vinegar", "Common salt"],
  ["Magnesium hydroxide is a base, so it neutralises the excess hydrochloric acid.",
   "Lemon juice and vinegar are themselves acids."])
O("When dilute acid is added to a carbonate, the gas given off turns lime water milky. The gas is ___",
  ["carbon dioxide", "hydrogen", "oxygen", "ammonia"],
  ["Acid + carbonate → salt + water + carbon dioxide, and CO₂ turns lime water milky."])
T("(a) State three properties each of acids and of bases.<br>(b) Write a word equation for the reaction between "
  "hydrochloric acid and sodium hydroxide.<br>(c) Describe how you would use litmus paper to show that wood ash solution is basic.<br>"
  "(d) State two uses of neutralisation in everyday life.",
  ["(a) <b>Acids:</b> turn blue litmus red; taste sour; have pH below 7; react with metals to give hydrogen; react with carbonates to give CO₂.",
   "<b>Bases:</b> turn red litmus blue; feel soapy or slippery; have pH above 7; neutralise acids to give salt and water.",
   "(b) hydrochloric acid + sodium hydroxide → sodium chloride + water",
   "(c) Dissolve a little wood ash in water and filter. Dip a piece of red litmus paper into the filtrate. "
   "The red litmus turns blue, showing that the solution is basic (alkaline).",
   "(d) 1. Treating soil that is too acidic by adding lime. 2. Taking antacids for indigestion. "
   "(Others: toothpaste neutralising mouth acids; treating wasp or ant stings; treating acidic factory waste before discharge.)"], marks=12)

# ------------------------------------------------------------------ 7
topic("metals", "Metals, non-metals & rusting", S, [
    "Metals are shiny, malleable, ductile and good conductors; non-metals are usually dull, brittle and poor conductors (graphite is the exception).",
    "Rusting of iron needs BOTH oxygen and water; salt speeds it up.",
    "Rust is hydrated iron(III) oxide.",
    "Rusting is prevented by painting, oiling/greasing, galvanising (zinc coating), electroplating, and alloying to make stainless steel.",
    "Alloys: brass = copper + zinc;  bronze = copper + tin;  steel = iron + carbon.",
])
O("Rusting of iron takes place only in the presence of ___",
  ["oxygen and water", "oxygen and carbon dioxide", "water and nitrogen", "oxygen only"],
  ["Iron in dry air does not rust, and iron in boiled water under oil does not rust.",
   "Both oxygen and water must be present."])
O("Which of these is a non-metal that conducts electricity?", ["Graphite", "Sulphur", "Phosphorus", "Iodine"],
  ["Graphite, a form of carbon, has free electrons between its layers, so it conducts."])
O("Coating iron with zinc to prevent rusting is called ___", ["galvanising", "electroplating", "annealing", "smelting"],
  ["Zinc is more reactive than iron, so it corrodes first and protects the iron — galvanising."])
O("Brass is an alloy of ___", ["copper and zinc", "copper and tin", "iron and carbon", "lead and tin"],
  ["Brass = copper + zinc.", "Copper + tin gives bronze; iron + carbon gives steel."])
O("Which property of metals allows them to be drawn into wires?", ["Ductility", "Malleability", "Conductivity", "Sonority"],
  ["Ductility is the ability to be drawn into wires.",
   "Malleability is the ability to be hammered into sheets."])
T("(a) State four physical properties of metals.<br>(b) Describe an experiment to show that both air and water are needed for rusting.<br>"
  "(c) State three methods of preventing rusting and give one place where each is used.",
  ["(a) Shiny (lustrous) when polished; malleable; ductile; good conductors of heat and electricity; sonorous; usually have high melting points and high density.",
   "(b) Set up three test tubes, each with a clean iron nail.",
   "Tube A: nail in water and air (open tube). Tube B: nail in boiled water covered with a layer of oil (water, no air). "
   "Tube C: nail in dry air over anhydrous calcium chloride, sealed (air, no water).",
   "Leave for a few days. <b>Result:</b> only the nail in tube A rusts.",
   "<b>Conclusion:</b> rusting needs both air (oxygen) and water.",
   "(c) Painting — bridges, roofing sheets and vehicle bodies; oiling or greasing — machine parts and bicycle chains; "
   "galvanising — roofing sheets, buckets and nails; electroplating with chromium — taps and car fittings; using stainless steel — cutlery."], marks=12)

# ------------------------------------------------------------------ 8
topic("water", "Water & solutions", S, [
    "Water is a universal solvent; pure water boils at 100 °C and freezes at 0 °C at sea level.",
    "Hard water contains dissolved calcium and magnesium salts, wastes soap and forms scum.",
    "Temporary hardness (hydrogen carbonates) is removed by boiling; permanent hardness (sulphates) needs washing soda or an ion-exchange resin.",
    "A solution = solute + solvent. Saturated solution: no more solute will dissolve at that temperature.",
    "Water treatment: sedimentation → coagulation (alum) → filtration → chlorination.",
])
O("Hard water is water that ___",
  ["does not lather easily with soap", "contains no dissolved substances",
   "boils above 100 °C", "is unfit for drinking"],
  ["Calcium and magnesium salts react with soap to form scum, so hard water wastes soap.",
   "Hard water is not necessarily unsafe to drink."])
O("Temporary hardness of water can be removed by ___",
  ["boiling", "adding common salt", "filtering", "adding more soap"],
  ["Boiling decomposes calcium hydrogen carbonate, depositing it as an insoluble carbonate."])
O("In water treatment, alum is added mainly to ___",
  ["make suspended particles settle", "kill germs", "remove hardness", "add minerals"],
  ["Alum is a coagulant: it makes fine suspended particles clump together and settle.",
   "Germs are killed by chlorination."])
O("A solution in which no more solute can dissolve at a given temperature is said to be ___",
  ["saturated", "dilute", "concentrated", "unsaturated"],
  ["That is the definition of a saturated solution."])
O("Which of the following is NOT a use of water in the body?", ["Supplying energy", "Transporting nutrients", "Regulating body temperature", "Removing waste in urine"],
  ["Water supplies no energy — it contains no calories.", "The other three are genuine roles of water in the body."])
T("(a) State three differences between hard and soft water.<br>(b) Explain how temporary hardness of water is caused and how it can be removed.<br>"
  "(c) Outline the stages in treating water for town supply.<br>(d) State two advantages and two disadvantages of hard water.",
  ["(a) 1. Hard water does not lather easily with soap; soft water lathers readily.",
   "2. Hard water forms scum with soap; soft water does not.",
   "3. Hard water contains dissolved calcium/magnesium salts; soft water contains little or none.",
   "(b) Rain water containing dissolved carbon dioxide passes through limestone, forming soluble calcium hydrogen carbonate. "
   "Boiling breaks it down into insoluble calcium carbonate (the 'fur' in kettles), carbon dioxide and water, so the hardness is removed.",
   "(c) Screening → sedimentation → coagulation with alum → filtration through sand and gravel → chlorination → storage and distribution.",
   "(d) <b>Advantages:</b> supplies calcium for bones and teeth; better taste; useful in brewing and tanning.",
   "<b>Disadvantages:</b> wastes soap; furs kettles, boilers and pipes, which wastes fuel and may cause them to burst."], marks=15)

# ------------------------------------------------------------------ 9
topic("soil", "Soil, rocks & conservation", S, [
    "Soil is formed by the weathering of rocks (physical, chemical and biological) plus the decay of organic matter.",
    "Soil components: mineral particles, water, air, organic matter (humus) and living organisms.",
    "Loam is the best agricultural soil: it holds water well and drains well, and is rich in humus.",
    "Sandy soil drains fast and is poor in nutrients; clay holds too much water and is badly aerated.",
    "Erosion is controlled by contour ploughing, terracing, cover cropping, mulching, strip cropping, afforestation and avoiding bush burning.",
])
O("Which soil type has the largest particles and drains most quickly?", ["Sandy soil", "Clay soil", "Loamy soil", "Silt"],
  ["Sand particles are the largest, so the spaces between them are big and water passes through quickly."])
O("The organic matter formed from decayed plant and animal remains in soil is called ___",
  ["humus", "loam", "leachate", "compost activator"],
  ["Humus improves soil structure, water retention and nutrient supply."])
O("Which of the following is NOT a method of controlling soil erosion?", ["Bush burning", "Contour ploughing", "Mulching", "Afforestation"],
  ["Bush burning destroys the vegetation cover and the humus, so it INCREASES erosion."])
O("The removal of soluble mineral salts from the topsoil by water moving downwards is called ___",
  ["leaching", "erosion", "weathering", "capillarity"],
  ["Leaching washes nutrients down beyond the reach of roots; erosion carries soil away from the surface."])
O("A farmer whose soil is too acidic should add ___", ["lime", "sulphur", "ammonium sulphate", "common salt"],
  ["Lime (calcium hydroxide/carbonate) is basic and neutralises soil acidity.",
   "Ammonium sulphate would make the soil more acidic."])
T("(a) Name the three main types of soil and state one characteristic of each.<br>(b) Explain why loamy soil is the best for crop growth.<br>"
  "(c) Describe an experiment to compare the rate of drainage of sandy soil and clay soil.<br>(d) State four ways of maintaining soil fertility.",
  ["(a) Sandy — large particles, drains quickly, poor in nutrients. Clay — very fine particles, holds water, poorly aerated and sticky when wet. "
   "Loamy — a mixture of sand, silt and clay with humus.",
   "(b) It holds enough water for plants but allows excess to drain away; it is well aerated; and it is rich in humus and plant nutrients.",
   "(c) Set up two filter funnels with cotton wool at the neck, one holding dry sandy soil and the other an equal mass of dry clay soil. "
   "Stand each over a measuring cylinder. Pour equal volumes of water (say 100 cm³) into each at the same time and record the volume collected after five minutes.",
   "<b>Result:</b> much more water drains through the sandy soil. <b>Conclusion:</b> sandy soil drains faster than clay soil.",
   "(d) Applying organic manure or compost; crop rotation; planting leguminous cover crops; applying fertilisers correctly; mulching; "
   "avoiding bush burning; fallowing (any four)."], marks=15)

# ------------------------------------------------------------------ 10
topic("organic", "Organic compounds & petrochemicals", S, [
    "Organic compounds contain carbon; hydrocarbons contain carbon and hydrogen only.",
    "Alkanes (C_nH_{2n+2}): methane, ethane, propane, butane — saturated, single bonds.",
    "Alkenes (C_nH_{2n}) have a double bond and are unsaturated; they decolourise bromine water.",
    "Crude oil is separated by fractional distillation: petroleum gas, petrol, kerosene, diesel, lubricating oil, bitumen (top to bottom).",
    "Plastics are polymers made from small molecules (monomers); most are non-biodegradable.",
])
O("The general formula of alkanes is ___", ["C_{n}H_{2n+2}", "C_{n}H_{2n}", "C_{n}H_{2n−2}", "C_{n}H_{n}"],
  ["Alkanes are saturated hydrocarbons with the formula CnH2n+2 — for example methane, CH₄ (n = 1)."])
O("Which of these is an unsaturated hydrocarbon?", ["Ethene", "Ethane", "Methane", "Propane"],
  ["Ethene (C₂H₄) contains a carbon-to-carbon double bond, so it is unsaturated."])
O("Crude oil is separated into its various fractions by ___",
  ["fractional distillation", "filtration", "crystallisation", "chromatography"],
  ["The fractions have different boiling points, so they condense at different heights in the fractionating column."])
O("Which fraction of crude oil is used as fuel for aircraft and for lamps?",
  ["Kerosene", "Bitumen", "Petrol", "Lubricating oil"],
  ["Kerosene is used for jet engines and for lanterns and stoves."])
O("A major environmental problem caused by plastics is that they ___",
  ["are non-biodegradable", "dissolve in water", "rust quickly", "evaporate easily"],
  ["Most plastics are not broken down by micro-organisms, so they block drains and litter the land for many years."])
T("(a) What are hydrocarbons? Give two examples.<br>(b) State two differences between alkanes and alkenes.<br>"
  "(c) Name four fractions obtained from crude oil and state one use of each.<br>(d) Suggest three ways of reducing plastic pollution in your community.",
  ["(a) Hydrocarbons are organic compounds made up of carbon and hydrogen only. Examples: methane (CH₄), ethane (C₂H₆), ethene (C₂H₄).",
   "(b) 1. Alkanes have only single bonds (saturated); alkenes have at least one double bond (unsaturated).",
   "2. Alkanes do not decolourise bromine water; alkenes do. (Also: general formulae CnH2n+2 and CnH2n.)",
   "(c) Petroleum gas — cooking (LPG); petrol — fuel for cars; kerosene — lamps, stoves and jet fuel; diesel — trucks and generators; "
   "lubricating oil — oiling machines; bitumen — surfacing roads (any four).",
   "(d) Reduce, reuse and recycle plastic containers; use cloth or paper bags instead of polythene; "
   "separate waste at home and support collection points that buy sachets and bottles; enforce laws against dumping in drains and gutters."], marks=15)
