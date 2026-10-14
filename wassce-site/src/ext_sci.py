from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

extras("measure",
  plain="Measurement is about numbers WITH units. Every answer needs the right unit — 5 alone means nothing, "
        "but 5 g/cm³ does. Density simply tells you how heavy something is for its size.",
  examples=[
    E("A piece of metal has a mass of 135 g and a volume of 50 cm³. Find its density.",
      "Step 1. Write the formula: density = mass ÷ volume.",
      "Step 2. Put in the numbers: 135 ÷ 50.",
      "Step 3. = <b>2.7 g/cm³</b> (this is the density of aluminium)."),
    E("How would you find the volume of a stone in the laboratory?",
      "Step 1. Pour water into a measuring cylinder and read the level, say 50 cm³.",
      "Step 2. Tie the stone with thread and lower it gently into the water.",
      "Step 3. Read the new level, say 68 cm³.",
      "Step 4. Volume of stone = 68 − 50 = <b>18 cm³</b> — the water it pushed out.")],
  fig=draw.flow(["Observation", "Hypothesis", "Experiment", "Conclusion"],
                note="The scientific method", label="Steps of the scientific method"))
assert 135 / 50 == 2.7

extras("living",
  plain="Living things do seven things: Move, Respire, Sense, Grow, Reproduce, Excrete and feed (Nutrition) — "
        "remember MRS GREN. A thing is only alive if it does ALL seven.",
  examples=[
    E("Is a motor car a living thing? Give reasons.",
      "Step 1. Check the list. A car moves, uses fuel (like feeding) and gives out exhaust gases (like excreting).",
      "Step 2. But it cannot grow by itself, cannot reproduce, and cannot respond to a stimulus on its own.",
      "Step 3. Because it fails some of the seven, a car is <b>not a living thing</b>."),
    E("Give two ways a maize plant differs from a goat.",
      "Step 1. Feeding: the maize makes its own food by photosynthesis; the goat eats ready-made food.",
      "Step 2. Movement: the maize is fixed in one place; the goat moves about freely.",
      "Step 3. (Also: plant cells have a cell wall and chloroplasts; the plant keeps growing at its tips all its life.)")])

extras("classify",
  plain="Classification is grouping living things by what they have in common, so that the millions of "
        "species can be studied in an orderly way. The groups go from big to small: kingdom down to species.",
  examples=[
    E("An animal has a hard outer covering, three body parts and six legs. Classify it.",
      "Step 1. A hard outer covering (exoskeleton) and jointed legs ⇒ phylum Arthropoda.",
      "Step 2. Three body parts (head, thorax, abdomen) and six legs ⇒ class <b>Insecta</b>.",
      "Step 3. An animal with two body parts and eight legs would be an arachnid, such as a spider."),
    E("Why is the name <i>Zea mays</i> written that way?",
      "Step 1. Every organism has a two-word scientific name — the binomial system.",
      "Step 2. The first word is the GENUS and starts with a capital letter: <i>Zea</i>.",
      "Step 3. The second is the SPECIES, in small letters: <i>mays</i>. Both are printed in italics "
      "or underlined when handwritten.")],
  fig=draw.flow(["Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"],
                note="From the largest group to the smallest", label="Order of classification"))

extras("cells",
  plain="All living things are made of cells — tiny building blocks. A plant cell has a stiff wall, "
        "chloroplasts for making food and a big water bag (vacuole); an animal cell has none of these three.",
  examples=[
    E("Name three structures found in a plant cell but not in an animal cell, and say what each does.",
      "Step 1. <b>Cell wall</b> — made of cellulose; gives the cell shape and support.",
      "Step 2. <b>Chloroplast</b> — contains chlorophyll and traps sunlight for photosynthesis.",
      "Step 3. <b>Large permanent vacuole</b> — stores cell sap and keeps the cell firm.",
      fig=draw.cellfig("plant", label="Plant cell")),
    E("A piece of cassava placed in strong salt solution becomes soft. Explain why.",
      "Step 1. The cell sap inside the cassava is less concentrated than the salt solution outside.",
      "Step 2. Water moves out of the cells, through the semi-permeable membrane, into the stronger solution.",
      "Step 3. This movement of water is <b>osmosis</b>; the cells lose water and the tissue becomes soft (flaccid).",
      fig=draw.cellfig("animal", label="Animal cell for comparison"))])

extras("matter",
  plain="Everything around you is matter. An element is made of one kind of atom; a compound is two or more "
        "elements chemically joined; a mixture is just things put together and can be separated physically.",
  examples=[
    E("An atom of an element has 19 protons and 20 neutrons. State its atomic number, mass number and "
      "electron arrangement.",
      "Step 1. Atomic number = number of protons = <b>19</b>.",
      "Step 2. Mass number = protons + neutrons = 19 + 20 = <b>39</b>.",
      "Step 3. Fill the shells 2, 8, 8, then what is left: <b>2, 8, 8, 1</b>.",
      "Step 4. One electron in the outer shell ⇒ Group I (it is potassium)."),
    E("How would you separate a mixture of sand, salt and iron filings?",
      "Step 1. Run a magnet over the mixture — the <b>iron filings</b> stick to it.",
      "Step 2. Add water and stir: the salt dissolves, the sand does not. Filter — the <b>sand</b> stays on the paper.",
      "Step 3. Evaporate the filtrate to get the <b>salt</b> back.")])
assert 19 + 20 == 39

extras("acids",
  plain="Acids taste sour (lime, vinegar) and turn blue litmus red. Bases are their opposites and feel soapy. "
        "When they meet they cancel each other out — that is neutralisation.",
  examples=[
    E("You are given three solutions, A (pH 2), B (pH 7) and C (pH 12). Describe each.",
      "Step 1. Below 7 is acidic: <b>A is an acid</b>, and pH 2 means a strong one.",
      "Step 2. Exactly 7 is <b>neutral</b> — B could be pure water.",
      "Step 3. Above 7 is basic (alkaline): <b>C is a strong base</b>, such as caustic soda solution."),
    E("A farmer's soil is too acidic. What should he add, and why?",
      "Step 1. To cancel an acid you need a base.",
      "Step 2. The cheap farm base is <b>lime</b> (calcium hydroxide or ground limestone).",
      "Step 3. It neutralises the acid, raising the pH so that crops can take up nutrients properly.")])

extras("metals",
  plain="Metals are shiny, bend without breaking and carry heat and electricity well. Their big enemy is "
        "rusting, which needs BOTH air and water — remove either one and iron will not rust.",
  examples=[
    E("Why does a bicycle chain rust quickly in the rainy season but not when it is oiled?",
      "Step 1. Rusting needs oxygen (from the air) and water together.",
      "Step 2. In the rainy season both are present, so rusting is fast.",
      "Step 3. Oil forms a layer that keeps air and water away from the metal, so rusting is prevented."),
    E("Name three ways of preventing rusting and where each is used.",
      "Step 1. <b>Painting</b> — roofing sheets, bridges, vehicle bodies.",
      "Step 2. <b>Oiling or greasing</b> — machine parts and chains.",
      "Step 3. <b>Galvanising</b> (coating with zinc) — buckets, nails and roofing sheets.")])

extras("water",
  plain="Water dissolves more substances than any other liquid. Hard water contains dissolved calcium and "
        "magnesium salts, which fight with soap and waste it.",
  examples=[
    E("How can you tell whether the water in a village is hard, and what can be done about it?",
      "Step 1. Test: shake a little soap solution with the water. If it forms scum instead of lather, it is hard.",
      "Step 2. Temporary hardness is removed by <b>boiling</b>.",
      "Step 3. Permanent hardness needs <b>washing soda</b> or an ion-exchange (water softener) unit."),
    E("Describe how water from a river is treated for town supply.",
      "Step 1. Screening removes sticks and rubbish; sedimentation lets heavy particles settle.",
      "Step 2. Alum is added so that fine particles clump together and settle (coagulation).",
      "Step 3. The water is filtered through sand and gravel, then chlorinated to kill germs before storage.",
      fig=draw.flow(["Sedimentation", "Coagulation", "Filtration", "Chlorination"],
                    note="Treating water for town supply", label="Water treatment stages"))])

extras("soil",
  plain="Soil is the thin top layer that plants grow in: broken rock, humus, water, air and living things. "
        "Loam is the farmer's favourite because it holds enough water but still drains.",
  examples=[
    E("A farmer's land is sandy and crops dry up quickly. Suggest what he can do.",
      "Step 1. Sandy soil has big particles, so water drains away fast and nutrients are washed out.",
      "Step 2. Add organic manure or compost — humus holds water and nutrients.",
      "Step 3. Mulch the surface with dry grass to cut down evaporation, and plant cover crops "
      "to protect the soil."),
    E("Why does farming on a steep slope need special care?",
      "Step 1. Rain water runs fast down a slope and carries the topsoil away — erosion.",
      "Step 2. Plough along the contour (across the slope), not up and down.",
      "Step 3. Make terraces or strips, and plant grass barriers to slow the water.")])

extras("organic",
  plain="Organic compounds are built around carbon. Crude oil is a mixture of them; heating it separates the "
        "parts by their different boiling points, which is why one well gives petrol, kerosene and diesel.",
  examples=[
    E("Why does petrol come out near the top of the fractionating column and bitumen at the bottom?",
      "Step 1. The crude oil is heated and the vapours rise up the column, which is hottest at the bottom.",
      "Step 2. Fractions with LOW boiling points rise high before they cool and condense — petrol and petroleum gas.",
      "Step 3. Fractions with HIGH boiling points condense early, near the bottom — lubricating oil and bitumen."),
    E("How do you show that ethene is unsaturated?",
      "Step 1. Unsaturated means it has a double bond.",
      "Step 2. Add a few drops of bromine water and shake.",
      "Step 3. The red-brown colour disappears (it is decolourised) — ethene is <b>unsaturated</b>. "
      "Ethane, which is saturated, leaves the colour unchanged.")],
  fig=draw.flow(["Petroleum gas", "Petrol", "Kerosene", "Diesel", "Bitumen"],
                note="Fractions from the top of the column to the bottom", label="Fractions of crude oil"))

extras("air",
  plain="Air is a mixture, not a compound: mostly nitrogen, about a fifth oxygen, and a little carbon dioxide "
        "and noble gases. Nitrogen keeps cycling between the air, the soil and living things.",
  examples=[
    E("Describe the composition of air and how you would show that oxygen is about one-fifth of it.",
      "Step 1. Nitrogen ≈ 78%, oxygen ≈ 21%, noble gases ≈ 0.97%, carbon dioxide ≈ 0.03%.",
      "Step 2. Float a candle on water, light it and cover it with a gas jar.",
      "Step 3. The candle burns until the oxygen is used up, and water rises to take its place.",
      "Step 4. The water rises about one-fifth of the way up the jar — so oxygen is about 20% of air.",
      fig=draw.piefig([("Nitrogen", 78), ("Oxygen", 21), ("Others", 1)], label="Composition of air")),
    E("How does nitrogen from the air get into a maize plant?",
      "Step 1. Plants cannot use nitrogen gas directly.",
      "Step 2. Lightning and nitrogen-fixing bacteria (such as <i>Rhizobium</i> in legume nodules) change it "
      "into compounds — nitrogen fixation.",
      "Step 3. Soil bacteria change these into nitrates (nitrification), and the roots absorb the nitrates.",
      fig=draw.cyclefig(["Nitrogen in air", "Fixation", "Nitrates in soil", "Taken by plants", "Decay"],
                        "Nitrogen cycle", label="The nitrogen cycle"))])

extras("hydro",
  plain="The water cycle is nature recycling its water: the sun lifts it as vapour, clouds form, rain falls, "
        "and it runs back to the sea. No new water is ever made.",
  examples=[
    E("Explain why it rains more near the coast and the forest than in the far north.",
      "Step 1. Evaporation is greatest over the sea and where there is thick vegetation (transpiration).",
      "Step 2. Moist air rising over these areas cools and condenses into clouds.",
      "Step 3. More moisture in the air means more rain; drier inland air gives less.",
      fig=draw.cyclefig(["Evaporation", "Condensation", "Precipitation", "Run-off"],
                        "Water cycle", label="The water cycle")),
    E("Water from a stream looks clear. Why is it still unsafe to drink?",
      "Step 1. Clearness only means there are few solid particles.",
      "Step 2. Germs such as <i>Vibrio cholerae</i> and typhoid bacteria are far too small to see.",
      "Step 3. Boil the water for a few minutes, or filter and add the recommended chlorine tablets, before drinking.")])

extras("pests",
  plain="A pest damages crops or property; a parasite lives on or inside another organism and harms it. "
        "Knowing the life cycle shows you where to break it — usually at the egg or larva stage.",
  examples=[
    E("Explain how clearing stagnant water reduces malaria in a town.",
      "Step 1. The mosquito lays its eggs on still water; the larva and pupa also live there.",
      "Step 2. No still water means no breeding place, so the cycle is broken early.",
      "Step 3. Fewer adult mosquitoes emerge, so fewer bites and less malaria.",
      fig=draw.cyclefig(["Egg", "Larva", "Pupa", "Adult"], "Mosquito", label="Life cycle of the mosquito")),
    E("State two ways the housefly spreads disease and two ways to control it.",
      "Step 1. It carries germs on its hairy legs from faeces and refuse to food.",
      "Step 2. It vomits and passes faeces on food while feeding.",
      "Step 3. Control: cover food and dispose of refuse properly (no breeding place); "
      "use screens, traps or approved insecticide.")])

extras("crop",
  plain="Crop production is growing plants for food and money. The main ideas: prepare the land well, plant "
        "at the right spacing and time, feed the soil, and control weeds and pests early.",
  examples=[
    E("A farmer's maize leaves are turning yellow from the bottom of the plant upwards. What is wrong?",
      "Step 1. Yellowing of the OLDER leaves first points to nitrogen deficiency.",
      "Step 2. Nitrogen moves inside the plant to the young leaves, leaving the old ones pale.",
      "Step 3. Apply a nitrogen fertiliser such as sulphate of ammonia or urea, or well-rotted manure."),
    E("Why does a farmer rotate maize, cowpea and cassava instead of planting maize every year?",
      "Step 1. Different crops take different nutrients and feed at different soil depths.",
      "Step 2. The cowpea is a legume — its root nodules add nitrogen to the soil.",
      "Step 3. Rotation also breaks the life cycles of pests and diseases that attack one crop, "
      "and helps control weeds.")])

extras("animal",
  plain="Animal production is keeping livestock for meat, eggs, milk and money. Good housing, a balanced "
        "ration, clean water and vaccination are what keep animals productive.",
  examples=[
    E("A poultry farmer's layers are producing eggs with thin shells. What is the likely cause and the remedy?",
      "Step 1. Egg shell is made mainly of calcium carbonate.",
      "Step 2. Thin shells suggest too little calcium in the feed.",
      "Step 3. Add a calcium source — oyster shell, limestone powder or a layers' mash — to the ration."),
    E("State four ways of preventing disease outbreaks on a poultry farm.",
      "Step 1. Follow the vaccination programme (for example against Newcastle disease).",
      "Step 2. Keep the house clean and dry, and disinfect equipment.",
      "Step 3. Use a foot bath and limit visitors; isolate sick birds at once.",
      "Step 4. Avoid overcrowding and give clean water and a balanced ration.")])

extras("nutrition",
  plain="Food gives energy, materials for growth and protection from disease. Digestion breaks big food "
        "molecules into small ones that can pass into the blood.",
  examples=[
    E("How do you test a food sample for starch and for protein?",
      "Step 1. <b>Starch:</b> add two drops of iodine solution — a blue-black colour shows starch.",
      "Step 2. <b>Protein:</b> add sodium hydroxide, then a few drops of copper(II) sulphate (the Biuret test) "
      "— a purple colour shows protein.",
      "Step 3. Always compare with a control, such as plain water."),
    E("A child eats mainly kenkey and gari and develops a swollen body and pale hair. Explain.",
      "Step 1. These foods are almost all carbohydrate — plenty of energy, very little protein.",
      "Step 2. Without protein the body cannot make new tissue or plasma proteins, so fluid collects in the tissues.",
      "Step 3. The condition is <b>kwashiorkor</b>. Add beans, fish, eggs, groundnut or milk to the diet.",
      fig=draw.flow(["Mouth", "Oesophagus", "Stomach", "Small intestine", "Large intestine"],
                    note="Path of food through the gut", label="The digestive path"))])

extras("respcirc",
  plain="Respiration is releasing energy from food inside every cell — it is not the same as breathing. "
        "The blood is the delivery system: it carries oxygen and food in, and waste out.",
  examples=[
    E("Why do you breathe faster and deeper when running?",
      "Step 1. Running muscles need much more energy, so they respire faster.",
      "Step 2. Faster respiration needs more oxygen and produces more carbon dioxide.",
      "Step 3. Breathing rate and depth increase to supply the oxygen and remove the carbon dioxide quickly."),
    E("Trace a drop of blood from the right side of the heart until it returns there.",
      "Step 1. Right atrium → right ventricle → pulmonary artery → lungs (it picks up oxygen here).",
      "Step 2. Lungs → pulmonary vein → left atrium → left ventricle.",
      "Step 3. Left ventricle → aorta → body organs → vena cava → back to the right atrium.",
      fig=draw.flow(["Right heart", "Lungs", "Left heart", "Body", "Back to heart"],
                    note="Double circulation", label="Path of blood"))])

extras("excskel",
  plain="Excretion removes the poisonous waste your body itself makes (urea, carbon dioxide). The skeleton "
        "supports and protects, and the nervous system carries messages.",
  examples=[
    E("Distinguish between excretion and egestion, with an example of each.",
      "Step 1. <b>Excretion</b> removes waste made BY the body's own chemistry — urea in urine, "
      "carbon dioxide from the lungs.",
      "Step 2. <b>Egestion</b> removes undigested food, which never became part of the body's chemistry — faeces.",
      "Step 3. So the kidney excretes; the anus egests."),
    E("Why do you pull your hand away from a hot coal before you feel the pain?",
      "Step 1. Heat receptors in the skin send an impulse along a sensory neurone to the spinal cord.",
      "Step 2. A relay neurone passes it straight to a motor neurone, which makes the arm muscle contract.",
      "Step 3. This short path is a <b>reflex arc</b>; the message reaches the brain afterwards, "
      "which is why the pain comes later.",
      fig=draw.flow(["Receptor in skin", "Sensory neurone", "Spinal cord", "Motor neurone", "Muscle"],
                    note="The reflex arc", label="Reflex arc"))])

extras("repro",
  plain="Reproduction makes new individuals. In flowering plants, pollination moves pollen to the stigma and "
        "fertilisation joins the gametes; the ovule then becomes the seed and the ovary becomes the fruit.",
  examples=[
    E("A flower is small, green, has no scent and hangs outside the leaves with feathery stigmas. "
      "How is it pollinated, and why?",
      "Step 1. Insects are attracted by colour, scent and nectar — this flower has none.",
      "Step 2. The exposed anthers and feathery stigmas are made for catching moving air.",
      "Step 3. It is <b>wind-pollinated</b>, like maize and grasses."),
    E("What happens after pollen lands on the stigma?",
      "Step 1. The pollen grain germinates and grows a pollen tube down the style.",
      "Step 2. The male gamete travels down the tube and fuses with the egg cell — fertilisation.",
      "Step 3. The ovule becomes the <b>seed</b>, the ovary becomes the <b>fruit</b>, and the petals wither.")])

extras("photo",
  plain="Photosynthesis is how green plants make their own food using sunlight. It is the start of nearly "
        "every food chain and the source of the oxygen we breathe.",
  examples=[
    E("Describe how you would show that chlorophyll is necessary for photosynthesis.",
      "Step 1. Use a plant with variegated (green and white) leaves, and destarch it in the dark for 48 hours.",
      "Step 2. Leave it in sunlight for some hours, then take a leaf and draw the pattern of green and white parts.",
      "Step 3. Boil in water, then in alcohol to remove the chlorophyll, wash, and add iodine.",
      "Step 4. <b>Only the parts that were green turn blue-black</b> — so chlorophyll is necessary."),
    E("Why is a seed able to germinate in the dark but not able to keep growing there?",
      "Step 1. Germination uses the food stored in the seed, so light is not needed at first.",
      "Step 2. Once the store is used up, the seedling must make its own food.",
      "Step 3. Without light there is no photosynthesis, so the seedling turns pale and dies.")])

extras("energy",
  plain="Energy is the ability to do work. It is never created or destroyed — it only changes form, for "
        "example chemical energy in a battery becoming light in a bulb.",
  examples=[
    E("State the energy changes when a boy uses a torch, and when a hydro dam lights a town.",
      "Step 1. Torch: chemical (cell) → electrical → light + heat.",
      "Step 2. Dam: potential energy of stored water → kinetic energy of falling water → "
      "mechanical energy of the turbine → electrical energy → light and heat in homes.",
      "Step 3. Some energy is always lost as heat — that is why no machine is 100% efficient."),
    E("Give two advantages and two disadvantages of solar energy for a village in the north.",
      "Advantages: sunshine is free and abundant there; it causes no pollution and needs no fuel deliveries.",
      "Disadvantages: the panels and batteries cost a lot at first; there is no sun at night and less "
      "during the harmattan, so storage is needed.")])

extras("heat",
  plain="Heat moves in three ways: conduction through solids, convection in liquids and gases, and radiation "
        "which needs no material at all — that is how the sun's heat reaches us.",
  examples=[
    E("Calculate the heat needed to raise the temperature of 3 kg of water by 20 °C. [c = 4200 J/kg K]",
      "Step 1. Formula: Q = mcΔθ.",
      "Step 2. Q = 3 × 4200 × 20.",
      "Step 3. = <b>252 000 J</b> (252 kJ)."),
    E("Explain why a cooking pot is metal but its handle is wooden.",
      "Step 1. Metals are good conductors, so heat passes quickly into the food.",
      "Step 2. Wood is a poor conductor (an insulator).",
      "Step 3. The handle therefore stays cool enough to hold, and the cook is not burnt.")])
assert 3 * 4200 * 20 == 252000

extras("light",
  plain="Light travels in straight lines. When it hits a mirror it bounces back at the same angle "
        "(reflection); when it passes into water or glass it bends (refraction).",
  examples=[
    E("A ray hits a plane mirror at 30° to the mirror surface. Find the angle of reflection.",
      "Step 1. Angles are always measured from the NORMAL, not from the mirror.",
      "Step 2. Angle of incidence = 90 − 30 = 60°.",
      "Step 3. Angle of reflection = angle of incidence = <b>60°</b>.",
      fig=draw.raysfig("reflect", label="Reflection at a plane mirror")),
    E("Why does a coin at the bottom of a bucket of water look nearer the surface than it really is?",
      "Step 1. Light from the coin passes from water into air.",
      "Step 2. At the surface it bends away from the normal — refraction.",
      "Step 3. Your eye traces the bent rays back in straight lines, so the coin appears raised.",
      fig=draw.raysfig("refract", label="Refraction at a water surface"))])

extras("sound",
  plain="Sound is made by something vibrating, and it needs a material to travel through — there is no sound "
        "in a vacuum. It travels much more slowly than light.",
  examples=[
    E("A girl shouts towards a cliff and hears the echo 3 seconds later. If sound travels at 340 m/s, "
      "how far is the cliff?",
      "Step 1. The sound goes to the cliff AND comes back, so it covers twice the distance.",
      "Step 2. Total distance = 340 × 3 = 1020 m.",
      "Step 3. Distance to the cliff = 1020 ÷ 2 = <b>510 m</b>."),
    E("Why do you see lightning before you hear thunder?",
      "Step 1. Both happen at the same moment.",
      "Step 2. Light travels at about 300 000 000 m/s; sound travels at about 340 m/s.",
      "Step 3. Light reaches you almost at once, while the sound takes about 3 seconds for every kilometre.")])
assert 340 * 3 / 2 == 510

extras("elec",
  plain="Current is the flow of charge round a circuit; voltage is the push that drives it; resistance slows "
        "it down. Ohm's law ties the three together: V = IR.",
  examples=[
    E("A lamp of resistance 20 Ω is connected to a 12 V battery. Find the current and the power.",
      "Step 1. V = IR, so I = V ÷ R = 12 ÷ 20 = <b>0.6 A</b>.",
      "Step 2. Power P = VI = 12 × 0.6.",
      "Step 3. = <b>7.2 W</b>.",
      fig=draw.circuitfig(label="Simple series circuit")),
    E("A household uses a 1.5 kW heater for 4 hours a day for 30 days. Find the cost at GH₵ 1.20 per kWh.",
      "Step 1. Energy per day = 1.5 kW × 4 h = 6 kWh.",
      "Step 2. In 30 days: 6 × 30 = 180 kWh.",
      "Step 3. Cost = 180 × 1.20 = <b>GH₵ 216</b>.")])
assert 12 / 20 == 0.6 and 1.5 * 4 * 30 * 1.2 == 216

extras("electron",
  plain="Electronics uses materials that are between conductors and insulators — semiconductors. A diode lets "
        "current pass one way only; a transistor works as a switch or an amplifier.",
  examples=[
    E("Why is a diode used in a phone charger?",
      "Step 1. The mains supplies alternating current (a.c.), which keeps changing direction.",
      "Step 2. A phone battery can only be charged by direct current (d.c.).",
      "Step 3. The diode allows current in one direction only, so it changes a.c. to d.c. — rectification."),
    E("Name the four units of a computer and give one example of each.",
      "Step 1. <b>Input</b> — keyboard, mouse, scanner.",
      "Step 2. <b>Processing</b> — the CPU, which carries out the instructions.",
      "Step 3. <b>Storage</b> — hard disk, flash drive.",
      "Step 4. <b>Output</b> — monitor, printer, speaker.")])

extras("eco",
  plain="An ecosystem is living things plus their surroundings, working together. Energy enters as sunlight, "
        "passes along a food chain, and most of it is lost as heat at every step.",
  examples=[
    E("Construct a food chain from a Ghanaian farm and name each feeding level.",
      "Step 1. Start with a green plant, the producer: maize.",
      "Step 2. maize → grasshopper (primary consumer) → toad (secondary consumer) → snake (tertiary consumer).",
      "Step 3. Decomposers — bacteria and fungi — break down all of them and return nutrients to the soil.",
      fig=draw.pyramidfig(["Snake", "Toad", "Grasshopper", "Maize"], label="Pyramid of feeding levels")),
    E("Why are there always fewer snakes than grasshoppers?",
      "Step 1. Only about 10% of the energy at one level passes to the next.",
      "Step 2. The rest is lost as heat, in respiration and in undigested material.",
      "Step 3. So each level supports a smaller population than the one below it.")])

extras("force",
  plain="A force is a push or a pull. It can start, stop or change motion. Pressure is force spread over an "
        "area — a sharp knife cuts because the same force acts on a very small area.",
  examples=[
    E("A truck of mass 2000 kg accelerates from rest to 15 m/s in 10 s. Find the acceleration and the force.",
      "Step 1. a = (v − u) ÷ t = (15 − 0) ÷ 10 = <b>1.5 m/s²</b>.",
      "Step 2. F = ma = 2000 × 1.5.",
      "Step 3. = <b>3000 N</b>."),
    E("Why do tractors have wide tyres while a nail has a sharp point?",
      "Step 1. Pressure = force ÷ area.",
      "Step 2. Wide tyres spread the tractor's weight over a LARGE area, so the pressure is small "
      "and it does not sink into soft soil.",
      "Step 3. A nail's point puts the force on a VERY small area, so the pressure is huge and it goes into the wood.")])
assert (15 - 0) / 10 == 1.5 and 2000 * 1.5 == 3000

extras("machines",
  plain="A machine makes work easier — it lets a small effort move a big load. It never gives you more energy "
        "than you put in, which is why efficiency is always below 100%.",
  examples=[
    E("A man uses an effort of 250 N to lift a load of 1000 N with a pulley system. The effort moves 8 m "
      "while the load rises 1.6 m. Find the MA, the VR and the efficiency.",
      "Step 1. MA = load ÷ effort = 1000 ÷ 250 = <b>4</b>.",
      "Step 2. VR = effort distance ÷ load distance = 8 ÷ 1.6 = <b>5</b>.",
      "Step 3. Efficiency = (MA ÷ VR) × 100 = (4 ÷ 5) × 100 = <b>80%</b>.",
      "Step 4. The missing 20% is used against friction and in lifting the moving parts."),
    E("Why is a wheelbarrow easier to use than carrying the load on your head?",
      "Step 1. The wheelbarrow is a second-class lever: the load sits between the wheel (fulcrum) and your hands.",
      "Step 2. The effort arm is longer than the load arm, so a small effort balances a big load.",
      "Step 3. The wheel also reduces friction, so the load moves easily.",
      fig=draw.leverfig(2, label="Wheelbarrow: a second-class lever"))])
assert 1000 / 250 == 4 and 8 / 1.6 == 5

extras("health",
  plain="Diseases are caused by germs (bacteria, viruses, protozoa, fungi and worms) and spread by air, "
        "water, food, insects or contact. Most can be prevented by sanitation, vaccination and simple care.",
  examples=[
    E("A whole family has diarrhoea and vomiting after a funeral. Explain what may have happened and what to do.",
      "Step 1. Sudden diarrhoea and vomiting in several people points to food or water contaminated with germs "
      "such as cholera or typhoid bacteria.",
      "Step 2. Give oral rehydration salts (ORS) at once to replace the lost water and salts, and go to a clinic.",
      "Step 3. Prevent it: boil or treat drinking water, wash hands with soap, cover food and dispose of waste properly."),
    E("Explain how a vaccine protects a child.",
      "Step 1. The vaccine contains a weakened or killed germ, or part of it, so the child does not fall ill.",
      "Step 2. The body's white blood cells make antibodies against it, and keep memory cells.",
      "Step 3. If the real germ enters later, antibodies are made quickly and in large numbers, "
      "so the disease is prevented.")])

extras("genes",
  plain="Children resemble their parents because characteristics are passed on in genes, carried on "
        "chromosomes. A dominant gene shows even when only one copy is present.",
  examples=[
    E("A tall pea plant (TT) is crossed with a short one (tt). Show the F1 and the F2 generations.",
      "Step 1. Parents TT × tt. Gametes: all T from one, all t from the other.",
      "Step 2. F1: every plant is Tt — all <b>tall</b>, because T is dominant over t.",
      "Step 3. F1 × F1 (Tt × Tt) gives TT, Tt, Tt, tt.",
      "Step 4. F2 ratio = <b>3 tall : 1 short</b>."),
    E("Why is the father, not the mother, said to determine the sex of a baby?",
      "Step 1. The mother's egg always carries an X chromosome.",
      "Step 2. The father's sperm may carry X or Y.",
      "Step 3. X + X gives a girl; X + Y gives a boy — so it depends on which sperm fertilises the egg.")])

extras("env",
  plain="The environment is everything around us. Human activity — mining, farming, burning and dumping — "
        "can damage it faster than nature repairs it, and we all pay the cost in health and money.",
  examples=[
    E("Explain how galamsey affects a farming community downstream.",
      "Step 1. Pits and heaps destroy farmland, and the topsoil is lost.",
      "Step 2. Silt and mercury enter the river, so the water is unsafe for drinking, cooking and irrigation, "
      "and fish die or become poisonous.",
      "Step 3. Treating the water costs more, health suffers, and farmers who sold their land are left "
      "with neither land nor income."),
    E("Suggest four practical things a school can do to protect the environment.",
      "Step 1. Plant and care for trees on the compound.",
      "Step 2. Separate waste and sell or recycle plastics, bottles and paper.",
      "Step 3. Stop burning refuse in the open; compost the organic part for the school garden.",
      "Step 4. Teach the community through clubs, drama and durbars, and keep gutters clear.")])
