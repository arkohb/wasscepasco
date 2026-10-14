from core import *

S = "Cycles"

# ------------------------------------------------------------------ 11
topic("air", "Air, weather & the nitrogen cycle", S, [
    "Air by volume: nitrogen ≈ 78%, oxygen ≈ 21%, carbon dioxide ≈ 0.03%, noble gases ≈ 0.97%, plus water vapour and dust.",
    "Oxygen supports burning and respiration; carbon dioxide turns lime water milky and puts out flames.",
    "Nitrogen cycle: nitrogen fixation (lightning, <i>Rhizobium</i> in legume root nodules) → nitrification → absorption by plants → decay/ammonification → denitrification.",
    "Weather elements: temperature, rainfall, humidity, wind, sunshine, cloud cover, air pressure.",
    "Instruments: thermometer, rain gauge, hygrometer, anemometer (wind speed), wind vane (direction), barometer (pressure).",
])
O("The percentage by volume of nitrogen in the atmosphere is about ___", ["78%", "21%", "0.03%", "50%"],
  ["Nitrogen makes up roughly 78% of dry air, and oxygen about 21%."], v=78, nv=[78, 21, 0.03, 50])
O("Which organism converts atmospheric nitrogen into nitrogen compounds in the root nodules of legumes?",
  ["<i>Rhizobium</i>", "<i>Nitrobacter</i>", "<i>Escherichia coli</i>", "<i>Plasmodium</i>"],
  ["<i>Rhizobium</i> lives in the root nodules of legumes such as cowpea and groundnut and fixes nitrogen for the plant."])
O("Which instrument measures the speed of wind?", ["Anemometer", "Wind vane", "Barometer", "Hygrometer"],
  ["An anemometer measures wind speed; a wind vane shows the direction."])
O("A gas that turns lime water milky is ___", ["carbon dioxide", "oxygen", "nitrogen", "hydrogen"],
  ["Carbon dioxide reacts with lime water (calcium hydroxide) to form insoluble calcium carbonate — the milkiness."])
O("The process by which nitrates in the soil are converted back into free nitrogen gas is called ___",
  ["denitrification", "nitrification", "nitrogen fixation", "ammonification"],
  ["Denitrifying bacteria in waterlogged soils release nitrogen back to the atmosphere, reducing soil fertility."])
T("(a) Draw a simple diagram of the nitrogen cycle and describe THREE processes in it.<br>"
  "(b) Describe an experiment to show that about one-fifth of air is oxygen.<br>"
  "(c) State three ways in which farmers can increase the nitrogen content of the soil.",
  ["(a) <b>Nitrogen fixation:</b> free nitrogen is changed into nitrogen compounds by lightning, by <i>Rhizobium</i> in legume nodules and by industry.",
   "<b>Nitrification:</b> soil bacteria change ammonium compounds to nitrites and then to nitrates, which plants absorb.",
   "<b>Ammonification (decay):</b> bacteria and fungi break down dead plants, animals and excreta into ammonium compounds.",
   "<b>Denitrification:</b> denitrifying bacteria change nitrates back to free nitrogen.",
   "(b) Float a candle on water in a trough, light it and cover it with a graduated gas jar. "
   "As the candle burns, it uses up the oxygen and goes out, and the water rises into the jar.",
   "<b>Result:</b> the water rises by about one-fifth of the volume of the jar, showing that oxygen is about 20% of air. "
   "(A cleaner version uses moist iron filings left in a graduated tube for several days.)",
   "(c) Plant leguminous crops or use them in rotation; apply nitrogenous fertilisers such as ammonium sulphate or urea; "
   "apply organic manure and compost; avoid bush burning; practise green manuring."], marks=15)

# ------------------------------------------------------------------ 12
topic("hydro", "The water cycle & pollution of water", S, [
    "Water cycle: evaporation and transpiration → condensation → precipitation → run-off and infiltration.",
    "Sources of water: rain, rivers, streams, springs, wells, boreholes, lakes and the sea.",
    "Water-borne diseases: cholera, typhoid, dysentery, guinea worm, bilharzia (schistosomiasis).",
    "Domestic treatment: boiling, filtering, adding chlorine tablets or bleach, and the Sodis (solar) method.",
    "Water pollutants: sewage, refuse, industrial waste, mining mercury and mud (galamsey), farm chemicals and oil spills.",
])
O("The change of water vapour into liquid droplets in the atmosphere is called ___",
  ["condensation", "evaporation", "precipitation", "transpiration"],
  ["Rising air cools and its water vapour condenses into droplets, forming clouds."])
O("The loss of water vapour from the leaves of plants to the atmosphere is called ___",
  ["transpiration", "respiration", "guttation", "evaporation"],
  ["Transpiration is the loss of water vapour from the aerial parts of a plant, mainly through the stomata."])
O("Which of these diseases is spread mainly through drinking contaminated water?",
  ["Cholera", "Measles", "Tuberculosis", "Tetanus"],
  ["Cholera is caused by <i>Vibrio cholerae</i> in water contaminated with faeces."])
O("The simplest and most reliable way of making water from a stream safe for drinking at home is to ___",
  ["boil it", "leave it to settle", "add sugar", "pour it through cloth"],
  ["Boiling for a few minutes kills the disease-causing organisms.",
   "Settling and filtering through cloth only remove solid particles."])
O("Mercury used in small-scale gold mining pollutes rivers and can cause ___",
  ["damage to the nervous system", "improved fish growth", "hardness of water", "an increase in dissolved oxygen"],
  ["Mercury is a cumulative poison that damages the brain, nerves and kidneys, and it builds up in fish that people eat."])
T("(a) Describe the water cycle.<br>(b) State four causes of water pollution in Ghana and one effect of each.<br>"
  "(c) Describe two methods of purifying water in the home.",
  ["(a) Heat from the sun evaporates water from seas, rivers and lakes, and plants add water vapour by transpiration. "
   "The vapour rises, cools and condenses into clouds. When the droplets become heavy enough they fall as rain (precipitation). "
   "Some of the water runs off into rivers and the sea, and some soaks into the ground to become ground water, and the cycle repeats.",
   "(b) 1. Small-scale mining (galamsey) — muddy rivers and mercury poisoning of fish and people.",
   "2. Dumping refuse and sewage into drains and rivers — cholera and typhoid outbreaks.",
   "3. Industrial waste discharged untreated — death of fish and other aquatic life.",
   "4. Farm chemicals washed into streams — fertiliser causes algal growth that removes oxygen from the water.",
   "(c) <b>Boiling:</b> heat the water until it has boiled for at least three minutes, then cool it in a clean covered container; this kills pathogens.",
   "<b>Filtering and chlorination:</b> pass the water through a clean filter or ceramic candle to remove solids, then add the recommended "
   "chlorine tablet or a measured amount of bleach and leave it for thirty minutes."], marks=15)

# ------------------------------------------------------------------ 13
topic("pests", "Pests, parasites & their life cycles", S, [
    "Complete metamorphosis (egg → larva → pupa → adult): mosquito, housefly, butterfly, beetle.",
    "Incomplete metamorphosis (egg → nymph → adult): cockroach, grasshopper, termite.",
    "<i>Anopheles</i> mosquito transmits malaria; <i>Aedes</i> transmits yellow fever and dengue; <i>Culex</i> transmits filariasis.",
    "Housefly carries cholera, typhoid and dysentery on its body and in its vomit and faeces.",
    "Control: clear stagnant water, use treated nets and insecticides, keep food covered, dispose of refuse properly, treat infected people.",
])
O("The life cycle of the mosquito is: egg → ___ → pupa → adult", ["larva", "nymph", "caterpillar", "cocoon"],
  ["A mosquito undergoes complete metamorphosis, so the stage after the egg is the larva (the 'wriggler')."])
O("Which insect undergoes incomplete metamorphosis?", ["Cockroach", "Housefly", "Butterfly", "Mosquito"],
  ["The cockroach hatches as a nymph that resembles the adult; there is no pupal stage."])
O("The mosquito that transmits the malaria parasite is ___",
  ["female <i>Anopheles</i>", "male <i>Anopheles</i>", "female <i>Aedes</i>", "male <i>Culex</i>"],
  ["Only the female takes blood meals, which is how the <i>Plasmodium</i> parasite is passed on.",
   "<i>Aedes</i> spreads yellow fever and dengue."])
O("Which stage of the mosquito's life cycle is described as the 'tumbler' and does not feed?",
  ["Pupa", "Larva", "Egg", "Adult"],
  ["The comma-shaped pupa tumbles when disturbed and takes no food while it develops into an adult."])
O("The most effective long-term way of controlling mosquitoes in a community is to ___",
  ["clear all stagnant water", "spray adults every evening", "sleep with the windows open", "burn rubbish at night"],
  ["Removing breeding sites stops the cycle at the egg and larval stages; spraying only kills the adults present."])
T("(a) Draw and describe the life cycle of the housefly.<br>(b) State three ways the housefly spreads disease.<br>"
  "(c) Name two diseases transmitted by mosquitoes and state three ways of controlling mosquitoes.",
  ["(a) <b>Egg → larva (maggot) → pupa → adult.</b> The female lays batches of eggs on refuse, faeces or rotting matter. "
   "The eggs hatch in about a day into white legless maggots, which feed and moult. "
   "The maggot then moves to a drier place and forms a barrel-shaped pupa, from which the adult fly emerges after a few days. "
   "The whole cycle can be completed in one to two weeks.",
   "(b) It carries germs on its hairy legs and body from faeces and refuse to food; it vomits saliva onto food before feeding; "
   "and it passes out faeces on food. Diseases spread this way include cholera, typhoid, dysentery and diarrhoea.",
   "(c) Diseases: <b>malaria</b> (<i>Anopheles</i>) and <b>yellow fever</b> or <b>dengue</b> (<i>Aedes</i>); filariasis (<i>Culex</i>).",
   "Control: drain or fill stagnant water and clear choked gutters; sleep under insecticide-treated nets; "
   "spray or fog with insecticide; put oil on standing water to suffocate the larvae; stock ponds with larva-eating fish; "
   "screen windows and doors; treat infected people to remove the reservoir of parasites."], marks=15)

# ------------------------------------------------------------------ 14
topic("crop", "Crop production", S, [
    "Land preparation: clearing → stumping → ploughing → harrowing → ridging.",
    "Propagation: by seed (maize, rice, cowpea) or vegetatively (cassava stem cuttings, yam setts, plantain suckers, sugar cane setts).",
    "NPK: nitrogen for leaves and green growth, phosphorus for roots, potassium for fruits, flowers and disease resistance.",
    "Nitrogen deficiency shows as yellowing of older leaves (chlorosis) and stunted growth.",
    "Good practices: crop rotation, mulching, correct spacing, timely weeding, pest control and proper storage.",
])
O("Which crop is propagated by stem cuttings?", ["Cassava", "Maize", "Rice", "Cowpea"],
  ["Cassava is planted from mature stem cuttings; the others are grown from seed."])
O("A fertiliser rich in nitrogen is applied mainly to promote ___",
  ["leaf and stem growth", "root development", "fruit ripening", "flower colour"],
  ["Nitrogen is part of chlorophyll and protein, so it gives healthy green leafy growth."])
O("The practice of growing different crops on the same piece of land in a planned order from season to season is ___",
  ["crop rotation", "mixed cropping", "mono-cropping", "shifting cultivation"],
  ["Crop rotation prevents the build-up of pests and diseases and helps maintain soil fertility, especially when a legume is included."])
O("Covering the soil around crops with dry grass or leaves is called ___",
  ["mulching", "manuring", "thinning", "harrowing"],
  ["Mulching conserves soil moisture, controls weeds, moderates soil temperature and adds humus as it decays."])
O("Yellowing of the older leaves of a maize crop is most likely to indicate a deficiency of ___",
  ["nitrogen", "potassium", "calcium", "iron"],
  ["Nitrogen is mobile in the plant, so it moves to the young leaves and the older ones turn yellow first."])
T("(a) Outline the steps in preparing land for planting maize.<br>(b) State three advantages of crop rotation.<br>"
  "(c) Name three methods of vegetative propagation and give one crop for each.<br>"
  "(d) State three ways of storing farm produce to prevent losses.",
  ["(a) Clearing the vegetation → removing stumps and burning off or packing the trash → ploughing to loosen the soil → "
   "harrowing to break the clods → ridging or making mounds/beds → marking out and planting at the correct spacing.",
   "(b) It maintains soil fertility (especially with a legume in the rotation); it breaks the life cycles of pests and diseases; "
   "it controls weeds; it makes use of nutrients at different soil depths; and it spreads the farmer's risk and income.",
   "(c) Stem cuttings — cassava or sugar cane; suckers — plantain or banana or pineapple; "
   "setts (tubers) — yam; slips or vines — sweet potato; budding or grafting — citrus and mango.",
   "(d) Dry the produce properly before storage; store in clean, dry, well-ventilated barns, cribs or silos; "
   "treat against weevils with the recommended chemicals or with hermetic (airtight) bags; "
   "protect against rodents with rat guards; process into a form that keeps longer (gari, flour)."], marks=15)

# ------------------------------------------------------------------ 15
topic("animal", "Animal production", S, [
    "Farm animals: cattle, sheep, goats, pigs, poultry, rabbits, grasscutters and fish.",
    "Poultry systems: extensive (free range), semi-intensive and intensive (deep litter, battery cage).",
    "Chick → grower → layer/broiler. A balanced ration contains carbohydrate, protein, fat, minerals, vitamins and water.",
    "Ruminants (cattle, sheep, goats) have a four-chambered stomach: rumen, reticulum, omasum, abomasum.",
    "Common diseases: Newcastle disease and fowl pox in poultry; anthrax and rinderpest in cattle. Prevent by vaccination and good sanitation.",
])
O("Which of these animals is a ruminant?", ["Goat", "Pig", "Fowl", "Rabbit"],
  ["Goats, like cattle and sheep, chew the cud and have a four-chambered stomach."])
O("The rearing of poultry in cages where birds cannot move about freely is known as the ___ system.",
  ["battery cage", "free range", "semi-intensive", "extensive"],
  ["In the battery cage system birds are kept in cages, which makes egg collection easy and feeding efficient."])
O("A viral disease of poultry that spreads rapidly and is controlled mainly by vaccination is ___",
  ["Newcastle disease", "coccidiosis", "anthrax", "foot and mouth disease"],
  ["Newcastle disease is viral and very contagious; coccidiosis is caused by a protozoan, and anthrax and foot-and-mouth affect livestock."])
O("Which nutrient must be increased in the ration of a laying bird to give strong egg shells?",
  ["Calcium", "Carbohydrate", "Fat", "Vitamin C"],
  ["Egg shell is largely calcium carbonate, so layers need extra calcium — often from oyster shell or limestone."])
O("The main product obtained from a broiler is ___", ["meat", "eggs", "wool", "milk"],
  ["Broilers are raised for meat; layers are kept for eggs."])
T("(a) State three differences between the deep litter and the battery cage systems of poultry keeping.<br>"
  "(b) State four ways of preventing disease on a poultry farm.<br>"
  "(c) Name the four chambers of a ruminant's stomach and state the function of the first.<br>"
  "(d) Give three reasons why fish farming should be encouraged in Ghana.",
  ["(a) 1. In deep litter the birds move freely on litter; in the battery system they are confined in cages.",
   "2. Eggs are collected from nest boxes in deep litter, but roll out onto a tray in the battery system, so fewer are dirty or broken.",
   "3. Deep litter allows exercise and normal behaviour but risks disease spreading through the flock; the battery system gives better "
   "control of feeding and disease but has a higher set-up cost.",
   "(b) Vaccinate according to the programme; keep the house and equipment clean and disinfected; provide a foot bath and restrict visitors; "
   "isolate and treat sick birds; avoid overcrowding; supply clean water and a balanced ration; dispose of dead birds properly.",
   "(c) <b>Rumen, reticulum, omasum, abomasum.</b> In the rumen, micro-organisms break down cellulose in the food by fermentation, "
   "and the partly digested food is later returned to the mouth to be chewed again as cud.",
   "(d) It supplies cheap animal protein; it creates employment and income; it reduces pressure on wild fish stocks; "
   "it makes use of land and water that may be unsuitable for crops; and it can earn foreign exchange."], marks=15)

S = "Systems"

# ------------------------------------------------------------------ 16
topic("nutrition", "Food, nutrition & digestion", S, [
    "Food classes: carbohydrates, proteins, fats and oils, vitamins, mineral salts, water and roughage.",
    "Tests: starch + iodine → blue-black;  reducing sugar + Benedict's, heated → brick red;  protein + Biuret → purple;  fat → translucent spot on paper.",
    "Enzymes: amylase (starch → maltose), pepsin (protein → peptides), lipase (fats → fatty acids + glycerol).",
    "Bile from the liver emulsifies fats; it is not an enzyme.",
    "Deficiency diseases: kwashiorkor and marasmus (protein/energy), rickets (vitamin D), scurvy (vitamin C), anaemia (iron), goitre (iodine), night blindness (vitamin A).",
])
O("A food substance turns blue-black when iodine solution is added. The food contains ___",
  ["starch", "protein", "fat", "reducing sugar"],
  ["Iodine gives a blue-black colour with starch."])
O("The enzyme in saliva that acts on starch is ___", ["amylase (ptyalin)", "pepsin", "lipase", "trypsin"],
  ["Salivary amylase breaks starch down into maltose."])
O("Kwashiorkor in children is caused mainly by a shortage of ___", ["protein", "carbohydrate", "vitamin C", "iron"],
  ["Kwashiorkor results from too little protein in a diet that may still have enough energy; it shows as swelling (oedema) and a thin, pale skin."])
O("Bile helps in the digestion of fats by ___",
  ["emulsifying them", "changing them to glucose", "acting as an enzyme on them", "absorbing them into the blood"],
  ["Bile breaks large fat droplets into tiny ones, giving lipase a much larger surface area to work on. Bile contains no enzyme."])
O("Most of the absorption of digested food takes place in the ___",
  ["ileum", "stomach", "colon", "oesophagus"],
  ["The ileum is long and folded, with villi that give a very large surface area and a rich blood supply."])
T("(a) Name the seven classes of food and give one source and one function of each of any four.<br>"
  "(b) Describe the test for (i) starch; (ii) protein.<br>"
  "(c) Explain why a person on a diet of only cassava and plantain may develop kwashiorkor.<br>"
  "(d) State the function of roughage in the diet.",
  ["(a) Carbohydrates (rice, yam — supply energy); proteins (fish, beans — growth and repair); fats and oils (palm oil, groundnut — energy and warmth); "
   "vitamins (fruits and vegetables — protect against disease); mineral salts (milk, leafy vegetables — bones, teeth, blood); "
   "water (drinks, foods — transport and temperature control); roughage (unrefined cereals, vegetables).",
   "(b)(i) <b>Starch:</b> put a little of the food in a test tube, add two drops of iodine solution; a blue-black colour shows starch is present.",
   "(ii) <b>Protein:</b> to the food solution add sodium hydroxide solution, then a few drops of copper(II) sulphate solution (the Biuret test); "
   "a purple or violet colour shows protein.",
   "(c) Cassava and plantain are almost entirely carbohydrate. Such a diet supplies energy but very little protein, "
   "so the body lacks the amino acids needed for growth, repair and the making of plasma proteins, and the child develops kwashiorkor.",
   "(d) Roughage (dietary fibre) adds bulk to the food, holds water and stimulates the muscles of the gut so that waste moves along easily, "
   "preventing constipation."], marks=15)

# ------------------------------------------------------------------ 17
topic("respcirc", "Respiration & circulation", S, [
    "Aerobic respiration: glucose + oxygen → carbon dioxide + water + energy (about 2900 kJ per mole of glucose).",
    "Anaerobic respiration in muscle gives lactic acid; in yeast it gives ethanol and carbon dioxide.",
    "Breathing in: ribs move up and out, diaphragm flattens, chest volume increases, pressure falls, air rushes in.",
    "Blood: red cells (haemoglobin carries oxygen), white cells (defence), platelets (clotting), plasma (transport).",
    "Heart: right side handles deoxygenated blood, left side oxygenated. Arteries carry blood away from the heart; veins have valves.",
])
O("The equation 'glucose + oxygen → carbon dioxide + water + energy' represents ___",
  ["aerobic respiration", "anaerobic respiration", "photosynthesis", "transpiration"],
  ["Respiration using oxygen is aerobic respiration.",
   "Photosynthesis is the reverse: carbon dioxide + water → glucose + oxygen."])
O("During strenuous exercise, the substance that accumulates in muscles and causes cramp is ___",
  ["lactic acid", "ethanol", "glucose", "urea"],
  ["When oxygen is insufficient, glucose is broken down anaerobically to lactic acid."])
O("Which component of blood is mainly responsible for transporting oxygen?",
  ["Red blood cells", "White blood cells", "Platelets", "Plasma"],
  ["Haemoglobin in the red cells combines with oxygen to form oxyhaemoglobin."])
O("During inhalation, the diaphragm ___", ["flattens and moves down", "relaxes and domes up", "remains still", "moves sideways"],
  ["The diaphragm muscle contracts and flattens, which increases the volume of the chest cavity and lowers the pressure inside it."])
O("Blood is carried from the heart to the lungs by the ___",
  ["pulmonary artery", "pulmonary vein", "aorta", "vena cava"],
  ["The pulmonary artery carries deoxygenated blood from the right ventricle to the lungs — the only artery that carries deoxygenated blood."])
T("(a) State three differences between aerobic and anaerobic respiration.<br>"
  "(b) Describe what happens to the ribs, diaphragm and chest volume during inhalation and exhalation.<br>"
  "(c) Name the four chambers of the human heart and trace the path of blood from the body back to the body.<br>"
  "(d) State two differences between arteries and veins.",
  ["(a) 1. Aerobic respiration uses oxygen; anaerobic does not. 2. Aerobic gives carbon dioxide and water; anaerobic gives lactic acid "
   "(in animals) or ethanol and carbon dioxide (in yeast). 3. Aerobic releases much more energy per molecule of glucose.",
   "(b) <b>Inhalation:</b> the intercostal muscles contract, the ribs move upwards and outwards, the diaphragm contracts and flattens, "
   "the chest volume increases, the pressure inside falls below atmospheric, and air rushes into the lungs.",
   "<b>Exhalation:</b> the muscles relax, the ribs move down and in, the diaphragm domes upwards, the volume decreases, the pressure rises, "
   "and air is forced out.",
   "(c) <b>Right atrium, right ventricle, left atrium, left ventricle.</b>",
   "Body → vena cava → right atrium → right ventricle → pulmonary artery → lungs (oxygenated) → pulmonary vein → left atrium → "
   "left ventricle → aorta → body.",
   "(d) Arteries carry blood away from the heart, usually oxygenated, at high pressure and have thick muscular walls with no valves; "
   "veins carry blood towards the heart, usually deoxygenated, at low pressure, with thinner walls and valves to prevent backflow."], marks=15)

# ------------------------------------------------------------------ 18
topic("excskel", "Excretion, skeleton & the nervous system", S, [
    "Excretory organs: kidneys (urea, water, salts), lungs (carbon dioxide, water vapour), skin (sweat), liver (bile pigments).",
    "The nephron is the functional unit of the kidney: ultrafiltration in the glomerulus, then selective reabsorption.",
    "Skeleton functions: support, protection, movement, blood-cell formation and mineral storage.",
    "Joints: hinge (elbow, knee), ball-and-socket (hip, shoulder), pivot (neck), gliding, immovable (skull).",
    "Nervous system: brain and spinal cord (central) plus nerves. A reflex arc is receptor → sensory neurone → relay → motor neurone → effector.",
])
O("Which organ excretes urea from the human body?", ["Kidney", "Liver", "Lung", "Pancreas"],
  ["The liver makes urea from excess amino acids, but the kidney excretes it in urine."])
O("The functional unit of the kidney is the ___", ["nephron", "neurone", "nephridium", "alveolus"],
  ["Each kidney contains about a million nephrons, where filtration and reabsorption take place."])
O("The type of joint found at the elbow is a ___ joint.", ["hinge", "ball-and-socket", "pivot", "gliding"],
  ["A hinge joint allows movement in one plane only, like a door."])
O("The part of the brain that controls balance and coordination of movement is the ___",
  ["cerebellum", "cerebrum", "medulla oblongata", "hypothalamus"],
  ["The cerebellum coordinates muscular activity and balance; the cerebrum handles thought and voluntary action."])
O("Withdrawing your hand quickly from a hot object is an example of ___",
  ["a reflex action", "a voluntary action", "a conditioned response", "tropism"],
  ["It is automatic, rapid and does not involve the will — a simple reflex action."])
T("(a) Name four excretory organs in the human body and the substance each removes.<br>"
  "(b) State four functions of the skeleton.<br>(c) Describe a reflex arc, using the withdrawal of the hand from a hot object as an example.<br>"
  "(d) State two ways of keeping the kidneys healthy.",
  ["(a) Kidneys — urea, excess water and mineral salts; lungs — carbon dioxide and water vapour; "
   "skin — sweat (water, salts and a little urea); liver — bile pigments from broken-down red cells.",
   "(b) Support for the body; protection of delicate organs (skull–brain, ribs–heart and lungs); "
   "movement, by giving muscles a place of attachment and acting as levers; production of blood cells in the red bone marrow; "
   "storage of calcium and phosphorus; and giving the body its shape.",
   "(c) The heat stimulates receptors in the skin. A sensory neurone carries the impulse to the spinal cord, where a relay neurone passes it "
   "to a motor neurone. The motor neurone carries the impulse to the muscle of the arm (the effector), which contracts and pulls the hand away. "
   "The brain is informed afterwards, which is why you feel the pain after moving.",
   "(d) Drink plenty of clean water each day; avoid the abuse of drugs and painkillers; treat infections promptly; "
   "reduce excessive salt; go for regular medical check-ups."], marks=15)

# ------------------------------------------------------------------ 19
topic("repro", "Reproduction in humans & plants", S, [
    "A flower: sepals, petals, stamens (anther + filament, male) and carpel/pistil (stigma, style, ovary, female).",
    "Pollination is the transfer of pollen from anther to stigma; fertilisation is the fusion of male and female gametes.",
    "Wind-pollinated flowers are small, dull and scentless with feathery stigmas; insect-pollinated flowers are large, coloured, scented and have nectar.",
    "After fertilisation: ovule → seed, ovary → fruit.",
    "In humans, fertilisation occurs in the fallopian tube (oviduct); the embryo develops in the uterus, and the placenta exchanges food, oxygen and waste.",
])
O("The male reproductive part of a flower is the ___", ["stamen", "carpel", "sepal", "receptacle"],
  ["The stamen consists of the anther, which produces pollen grains, and the filament that holds it up."])
O("In flowering plants, fertilisation results in the ovule developing into a ___", ["seed", "fruit", "flower", "stem"],
  ["The ovule becomes the seed and the ovary becomes the fruit."])
O("Which features show that a flower is wind-pollinated?",
  ["Small dull petals and feathery stigma", "Large coloured petals and nectar",
   "Sticky pollen and strong scent", "Brightly coloured sepals and nectar guides"],
  ["Wind-pollinated flowers do not need to attract insects; they produce large amounts of light pollen and have exposed, feathery stigmas."])
O("In humans, fertilisation normally takes place in the ___", ["fallopian tube", "uterus", "ovary", "vagina"],
  ["The sperm meets the egg in the fallopian tube (oviduct); the fertilised egg then moves to the uterus to implant."])
O("The structure through which the developing foetus obtains food and oxygen from the mother is the ___",
  ["placenta", "amnion", "umbilical vein only", "uterus wall"],
  ["The placenta allows exchange of nutrients, oxygen and waste between the mother's blood and the foetal blood, which do not mix."])
T("(a) Draw and label the parts of a typical flower (six labels).<br>(b) State four differences between wind-pollinated and insect-pollinated flowers.<br>"
  "(c) Describe what happens from pollination to seed formation in a flowering plant.<br>"
  "(d) State three functions of the placenta.",
  ["(a) Labels: sepal, petal, anther, filament, stigma, style, ovary, ovule, receptacle (any six).",
   "(b) 1. Wind: small, dull petals or none; Insect: large, brightly coloured petals. 2. Wind: no scent or nectar; Insect: scented, with nectar. "
   "3. Wind: pollen light, smooth and in large amounts; Insect: pollen sticky or spiky and in smaller amounts. "
   "4. Wind: anthers and feathery stigmas hang outside the flower; Insect: anthers and sticky stigmas are inside.",
   "(c) A pollen grain lands on the stigma and germinates, growing a pollen tube down the style to the ovary. "
   "The male gamete passes down the tube and fuses with the egg cell in the ovule — fertilisation. "
   "The fertilised ovule develops into a seed, containing an embryo and stored food, while the ovary wall develops into the fruit. "
   "The petals, stamens and style usually wither and fall off.",
   "(d) It allows food and oxygen to pass from the mother's blood to the foetus; it allows carbon dioxide and urea to pass from the foetus "
   "to the mother; it acts as a barrier against some harmful substances and germs; and it produces hormones that maintain the pregnancy."], marks=15)

# ------------------------------------------------------------------ 20
topic("photo", "Photosynthesis & plant growth", S, [
    "Photosynthesis: carbon dioxide + water --(light, chlorophyll)--> glucose + oxygen.",
    "It needs light, chlorophyll, carbon dioxide and water; the products are glucose (stored as starch) and oxygen.",
    "Destarch a plant by keeping it in the dark for 24–48 hours before a starch test.",
    "Starch test on a leaf: boil in water → boil in alcohol to remove chlorophyll → wash → add iodine.",
    "Germination needs water, oxygen and a suitable temperature; light is not needed for germination.",
    "Transpiration is measured with a potometer; it is faster in hot, dry, windy conditions.",
])
O("The raw materials for photosynthesis are ___",
  ["carbon dioxide and water", "oxygen and water", "glucose and oxygen", "carbon dioxide and glucose"],
  ["Light energy trapped by chlorophyll combines carbon dioxide and water to make glucose and oxygen."])
O("Why is a plant kept in the dark for 48 hours before an experiment on photosynthesis?",
  ["To remove the starch already in the leaves", "To kill the leaf cells",
   "To increase the chlorophyll", "To open the stomata"],
  ["Destarching makes sure that any starch found afterwards was made during the experiment."])
O("A leaf is boiled in alcohol during the starch test in order to ___",
  ["remove the chlorophyll", "kill bacteria", "soften the leaf", "add iodine to the leaf"],
  ["The green colour would hide the blue-black result, so the chlorophyll is dissolved out in hot alcohol (heated in a water bath, as alcohol is flammable)."])
O("Which condition is NOT necessary for the germination of a maize grain?",
  ["Light", "Water", "Oxygen", "A suitable temperature"],
  ["Seeds germinate underground in the dark; light is needed only after the seedling appears above the ground."])
O("Transpiration is fastest on a day that is ___",
  ["hot, dry and windy", "cool, humid and still", "cold and rainy", "warm and humid"],
  ["Heat and wind increase evaporation from the leaf surfaces, and dry air keeps the diffusion gradient steep."])
T("(a) Write the word equation for photosynthesis and state its importance to living things.<br>"
  "(b) Describe an experiment to show that light is necessary for photosynthesis.<br>"
  "(c) State three conditions necessary for the germination of seeds and describe how you would show that one of them is needed.",
  ["(a) carbon dioxide + water --(sunlight, chlorophyll)--> glucose + oxygen",
   "Importance: it is the source of all food in nature; it releases the oxygen used in respiration; it removes carbon dioxide from the air; "
   "and it stores energy in a form that other organisms can use.",
   "(b) Destarch a potted plant by keeping it in the dark for 48 hours. Cover part of one leaf on both sides with black paper (the covered part "
   "is the control) and put the plant in sunlight for several hours.",
   "Remove the leaf, boil it in water to kill it, boil it in alcohol in a water bath to remove the chlorophyll, wash it in warm water and add iodine.",
   "<b>Result:</b> the exposed part turns blue-black; the covered part stays brown. <b>Conclusion:</b> light is necessary for photosynthesis.",
   "(c) Water, oxygen (air) and a suitable temperature.",
   "To show that water is needed: put equal numbers of similar seeds in two containers on cotton wool. Keep one moist and the other dry, "
   "leaving both in the same warm place with air. Only the seeds in the moist container germinate, showing that water is needed."], marks=15)
