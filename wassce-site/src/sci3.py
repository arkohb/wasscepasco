from core import *

S = "Energy"

# ------------------------------------------------------------------ 21
topic("energy", "Energy, its forms & transformations", S, [
    "Forms of energy: mechanical (kinetic and potential), heat, light, sound, chemical, electrical, nuclear and solar.",
    "Energy is neither created nor destroyed; it only changes from one form to another (conservation of energy).",
    "Examples: torch — chemical → electrical → light + heat;  microphone — sound → electrical;  generator — mechanical → electrical.",
    "Renewable sources: solar, wind, hydro, biomass, tidal. Non-renewable: coal, crude oil, natural gas, nuclear fuel.",
    "Nuclear energy comes from fission (splitting heavy nuclei) or fusion (joining light nuclei, as in the sun).",
])
O("The energy change that takes place in a dry cell torch is ___",
  ["chemical → electrical → light", "electrical → chemical → light",
   "light → electrical → chemical", "mechanical → electrical → light"],
  ["The cell stores chemical energy, which becomes electrical energy in the circuit and then light (and heat) in the bulb."])
O("Which of these is a renewable source of energy?", ["Wind", "Coal", "Natural gas", "Crude oil"],
  ["Wind is continuously replaced by nature; the others are fossil fuels that take millions of years to form."])
O("The energy possessed by a stone held at the top of a building is ___",
  ["potential energy", "kinetic energy", "chemical energy", "sound energy"],
  ["Energy due to position above the ground is gravitational potential energy."])
O("The energy of the sun is produced by the process of ___",
  ["nuclear fusion", "nuclear fission", "combustion", "radiation of heat from its core"],
  ["Hydrogen nuclei join to form helium, releasing enormous energy — nuclear fusion."])
O("Which statement best expresses the law of conservation of energy?",
  ["Energy can be changed from one form to another but cannot be created or destroyed.",
   "Energy is always lost as heat in every machine.",
   "The total energy of a body increases with its speed.",
   "Energy can be created in a generator."],
  ["The law states that the total energy of a closed system remains constant; machines only convert energy from one form to another."])
T("(a) State the law of conservation of energy.<br>(b) Give the energy transformation in each of the following: "
  "(i) an electric fan; (ii) a solar panel lighting a lamp; (iii) a microphone; (iv) a car battery being charged.<br>"
  "(c) State three advantages and two disadvantages of using solar energy in Ghana.",
  ["(a) Energy can neither be created nor destroyed; it can only be transformed from one form to another, and the total energy remains constant.",
   "(b)(i) electrical → mechanical (+ some heat and sound)",
   "(ii) solar (light) → electrical → light (+ heat)",
   "(iii) sound → electrical",
   "(iv) electrical → chemical",
   "(c) <b>Advantages:</b> sunshine is abundant and free all year in Ghana; it causes no pollution; it can be used in remote areas with no national grid; "
   "running costs are low and panels need little maintenance.",
   "<b>Disadvantages:</b> the initial cost of panels and batteries is high; it is not available at night and is reduced in the rainy or harmattan season, "
   "so storage batteries are needed."], marks=12)

# ------------------------------------------------------------------ 22
topic("heat", "Heat energy", S, [
    "Heat travels by conduction (solids), convection (fluids) and radiation (no medium needed).",
    "Quantity of heat: Q = mcΔθ, where c is specific heat capacity (water: 4200 J/kg K).",
    "Latent heat is absorbed during a change of state with no change in temperature.",
    "Expansion: solids < liquids < gases. Used in the bimetallic strip, thermostats and the thermometer.",
    "A vacuum flask reduces all three: vacuum (conduction and convection), silvered surfaces (radiation), stopper (evaporation).",
])
O("Heat transfer in liquids and gases takes place mainly by ___", ["convection", "conduction", "radiation", "induction"],
  ["Warmed fluid becomes less dense and rises, while cooler fluid sinks, setting up convection currents."])
O("Calculate the heat needed to raise the temperature of 2 kg of water from 25 °C to 55 °C. [c = 4200 J/kg K]",
  ["252000 J", "210000 J", "462000 J", "8400 J"],
  ["Q = mcΔθ = 2 × 4200 × (55 − 25)", "= 2 × 4200 × 30 = 252000 J"], v=2 * 4200 * 30, nv=[252000, 210000, 462000, 8400])
O("Which surface is the best absorber of radiant heat?", ["Dull black", "Shiny white", "Polished silver", "Smooth glass"],
  ["Dull black surfaces absorb (and emit) radiation best; shiny, light surfaces reflect it."])
O("The silvering of the inside walls of a vacuum flask reduces heat loss by ___",
  ["radiation", "conduction", "convection", "evaporation"],
  ["The silvered surfaces reflect radiant heat back, while the vacuum deals with conduction and convection."])
O("During the melting of ice at 0 °C, the temperature does not change because the heat supplied is used to ___",
  ["break the bonds holding the particles in the solid", "raise the kinetic energy of the particles",
   "expand the ice", "make the water molecules heavier"],
  ["The energy absorbed is latent heat of fusion: it separates the particles rather than raising their temperature."])
T("(a) Define specific heat capacity.<br>(b) Calculate the heat energy given out when 500 g of water cools from 90 °C to 30 °C. [c = 4200 J/kg K]<br>"
  "(c) Explain why the handle of a cooking pot is made of wood or plastic.<br>"
  "(d) Describe an experiment to show that a dull black surface is a better absorber of heat than a shiny surface.",
  ["(a) Specific heat capacity is the quantity of heat required to raise the temperature of 1 kg of a substance by 1 K (or 1 °C).",
   "(b) m = 500 g = 0.5 kg; Δθ = 90 − 30 = 60 K",
   "Q = mcΔθ = 0.5 × 4200 × 60 = <b>126 000 J</b> (126 kJ)",
   "(c) Wood and plastic are poor conductors (insulators) of heat, so heat from the pot does not travel quickly to the hand and the cook is not burnt.",
   "(d) Take two identical metal plates, one painted dull black and the other polished. Fix a cork to the back of each with candle wax, "
   "and place both at equal distances from a heat source such as a Bunsen flame or an electric heater.",
   "<b>Result:</b> the wax on the dull black plate melts first and its cork falls sooner. "
   "<b>Conclusion:</b> a dull black surface absorbs radiant heat better than a shiny one."], marks=12,
  ok=(0.5 * 4200 * 60 == 126000))

# ------------------------------------------------------------------ 23
topic("light", "Light", S, [
    "Light travels in straight lines; this explains shadows and eclipses.",
    "Laws of reflection: angle of incidence = angle of reflection, and the incident ray, reflected ray and normal lie in the same plane.",
    "A plane mirror gives an image that is virtual, erect, laterally inverted, the same size, and as far behind the mirror as the object is in front.",
    "Refraction is the bending of light as it passes from one medium to another; it makes a stick in water look bent.",
    "Convex (converging) lens corrects long sight; concave (diverging) lens corrects short sight. White light splits into seven colours by dispersion.",
])
O("A ray of light strikes a plane mirror at an angle of incidence of 35°. What is the angle of reflection?",
  ["35°", "55°", "70°", "145°"],
  ["By the law of reflection, the angle of reflection equals the angle of incidence."], v=35)
O("The image formed in a plane mirror is ___",
  ["virtual, erect and laterally inverted", "real, inverted and magnified",
   "real, erect and the same size", "virtual, inverted and diminished"],
  ["A plane mirror image cannot be caught on a screen (virtual), is the right way up, the same size and left-right reversed."])
O("A stick placed partly in water appears bent. This is due to ___",
  ["refraction", "reflection", "diffraction", "dispersion"],
  ["Light from the submerged part changes direction as it leaves the water, so the stick appears bent at the surface."])
O("Which defect of vision is corrected with a convex lens?",
  ["Long sight (hypermetropia)", "Short sight (myopia)", "Colour blindness", "Astigmatism"],
  ["In long sight the image forms behind the retina, so a converging (convex) lens is used to bring it forward."])
O("The splitting of white light into its component colours by a prism is called ___",
  ["dispersion", "diffraction", "refraction", "reflection"],
  ["Different colours are refracted by different amounts, so they separate — dispersion."])
T("(a) State the laws of reflection of light.<br>(b) List four characteristics of the image formed by a plane mirror.<br>"
  "(c) With the aid of a diagram, explain how short sight is corrected.<br>(d) State two uses of a convex lens.",
  ["(a) 1. The angle of incidence is equal to the angle of reflection. "
   "2. The incident ray, the reflected ray and the normal at the point of incidence all lie in the same plane.",
   "(b) It is virtual; erect (upright); the same size as the object; laterally inverted; and as far behind the mirror as the object is in front.",
   "(c) In short sight the eyeball is too long or the lens too strong, so parallel rays are brought to a focus IN FRONT of the retina and distant "
   "objects look blurred. A concave (diverging) lens is placed before the eye; it spreads the rays slightly so that the eye lens then focuses "
   "them exactly on the retina. (Diagram: parallel rays → concave lens → eye lens → focus on retina.)",
   "(d) In a magnifying glass; in cameras, projectors, microscopes and telescopes; and in spectacles for long sight."], marks=12)

# ------------------------------------------------------------------ 24
topic("sound", "Sound & waves", S, [
    "Sound is produced by vibrating bodies and needs a material medium — it cannot travel through a vacuum.",
    "Speed of sound in air ≈ 330–340 m/s; it is faster in liquids and fastest in solids.",
    "v = fλ  (speed = frequency × wavelength).",
    "Echo: the reflection of sound. Distance to the reflector = (v × t) ÷ 2.",
    "Pitch depends on frequency; loudness depends on amplitude; quality (timbre) distinguishes two instruments playing the same note.",
])
O("Sound cannot travel through ___", ["a vacuum", "water", "steel", "air"],
  ["Sound needs particles to pass the vibrations along, so it cannot travel through a vacuum."])
O("A sound wave has a frequency of 220 Hz and a wavelength of 1.5 m. Calculate its speed.",
  ["330 m/s", "146.7 m/s", "221.5 m/s", "0.0068 m/s"],
  ["v = fλ = 220 × 1.5", "= 330 m/s"], v=220 * 1.5, nv=[330, 146.7, 221.5, 0.0068])
O("A man claps his hands and hears the echo from a cliff 2 seconds later. If sound travels at 330 m/s, how far is the cliff?",
  ["330 m", "660 m", "165 m", "1320 m"],
  ["The sound travels to the cliff and back, so the total distance is 330 × 2 = 660 m",
   "Distance to the cliff = 660 ÷ 2 = 330 m"], v=330 * 2 / 2)
O("The pitch of a sound depends on its ___", ["frequency", "amplitude", "loudness", "speed"],
  ["The higher the frequency, the higher the pitch. Amplitude determines loudness."])
O("Sound travels fastest in ___", ["steel", "water", "air", "a vacuum"],
  ["Particles in a solid are closest together, so vibrations pass on most quickly."])
T("(a) State three differences between sound waves and light waves.<br>"
  "(b) A boy standing 660 m from a wall claps once and hears the echo after 4 s. Calculate the speed of sound in air.<br>"
  "(c) Explain why thunder is heard some seconds after lightning is seen.<br>(d) State two uses of echoes.",
  ["(a) 1. Sound needs a material medium; light can travel through a vacuum. "
   "2. Sound waves are longitudinal; light waves are transverse. "
   "3. Sound travels at about 330 m/s in air; light travels at 3 × 10^8 m/s. (Also: light can be polarised, sound cannot.)",
   "(b) Total distance travelled = 2 × 660 = 1320 m; time = 4 s",
   "Speed = distance ÷ time = 1320 ÷ 4 = <b>330 m/s</b>",
   "(c) Light travels about a million times faster than sound, so the flash reaches the observer almost at once while the sound takes "
   "about three seconds for every kilometre.",
   "(d) Echo-sounding to find the depth of the sea or to locate shoals of fish; ultrasound scanning in hospitals; "
   "locating cracks in metal castings; bats use echoes to find their way and their prey."], marks=12,
  ok=(2 * 660 / 4 == 330))

# ------------------------------------------------------------------ 25
topic("elec", "Electricity & magnetism", S, [
    "Ohm's law: V = IR. Resistors in series: R = R₁ + R₂. In parallel: 1/R = 1/R₁ + 1/R₂.",
    "Electrical power P = VI = I²R;  energy in kWh = power in kW × time in hours.",
    "In domestic wiring the fuse and switch go in the LIVE wire; earthing protects the user from shock.",
    "A magnet's like poles repel and unlike poles attract; repulsion is the only sure test for a magnet.",
    "A current in a coil makes an electromagnet; moving a magnet in a coil induces a current (the dynamo effect).",
])
O("A resistor of 4 Ω is connected to a 12 V battery. Calculate the current flowing.",
  ["3 A", "48 A", "0.33 A", "8 A"],
  ["V = IR ⇒ I = V ÷ R", "= 12 ÷ 4 = 3 A"], v=12 / 4)
O("Two resistors of 6 Ω and 3 Ω are connected in parallel. What is their combined resistance?",
  ["2 Ω", "9 Ω", "4.5 Ω", "18 Ω"],
  ["1/R = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2", "R = 2 Ω"], v=1 / (1 / 6 + 1 / 3))
O("An electric iron rated 2 kW is used for 3 hours. If electricity costs GH₵ 1.50 per kWh, what is the cost of the energy used?",
  ["GH₵ 9.00", "GH₵ 6.00", "GH₵ 4.50", "GH₵ 3.00"],
  ["Energy = 2 kW × 3 h = 6 kWh", "Cost = 6 × 1.50 = GH₵ 9.00"], v=2 * 3 * 1.5)
O("In domestic wiring, the fuse and the switch should be connected in the ___ wire.",
  ["live", "neutral", "earth", "neutral and earth"],
  ["Putting them in the live wire means that when the fuse blows or the switch is off, the appliance is completely cut off from the high voltage."])
O("The only sure test for a magnet is ___",
  ["repulsion of a like pole", "attraction of iron filings", "attraction of a piece of steel", "pointing north when suspended"],
  ["A magnet attracts magnetic materials, but only another magnet is REPELLED by a like pole."])
T("(a) State Ohm's law.<br>(b) Three resistors of 2 Ω, 3 Ω and 5 Ω are connected in series to a 20 V battery. Calculate "
  "(i) the total resistance; (ii) the current in the circuit; (iii) the potential difference across the 5 Ω resistor.<br>"
  "(c) State three safety precautions to observe when using electricity in the home.<br>(d) Give two differences between an electromagnet and a permanent magnet.",
  ["(a) The current flowing through a conductor is directly proportional to the potential difference across its ends, provided the temperature "
   "and other physical conditions remain constant.",
   "(b)(i) R = 2 + 3 + 5 = <b>10 Ω</b>",
   "(ii) I = V ÷ R = 20 ÷ 10 = <b>2 A</b>",
   "(iii) V = IR = 2 × 5 = <b>10 V</b>",
   "(c) Do not touch switches or appliances with wet hands; use the correct fuse rating and never replace a fuse with wire or foil; "
   "earth all metal-cased appliances; avoid overloading a socket with many appliances; repair worn or joined cables; switch off at the mains before repairs.",
   "(d) An electromagnet's magnetism can be switched on and off and its strength varied with the current, while a permanent magnet's cannot; "
   "an electromagnet is usually made of soft iron and loses its magnetism easily, whereas a permanent magnet is made of steel and keeps it."], marks=15,
  ok=(2 + 3 + 5 == 10 and 20 / 10 == 2 and 2 * 5 == 10))

# ------------------------------------------------------------------ 26
topic("electron", "Electronics & ICT", S, [
    "Conductors (copper) conduct freely; insulators (rubber, glass) do not; semiconductors (silicon, germanium) are in between.",
    "Doping adds impurities: n-type (extra electrons) and p-type (holes).",
    "A diode allows current in one direction only, so it is used to rectify a.c. to d.c.",
    "A transistor can amplify a signal or work as a switch.",
    "Computer parts: input (keyboard, mouse, scanner), processing (CPU), storage (hard disk, flash drive), output (monitor, printer).",
])
O("Which of these materials is a semiconductor?", ["Silicon", "Copper", "Rubber", "Glass"],
  ["Silicon and germanium conduct better than insulators but less well than metals, and their conductivity rises with temperature and doping."])
O("The electronic component that allows current to flow in only one direction is the ___",
  ["diode", "resistor", "capacitor", "transformer"],
  ["This property makes the diode useful for changing a.c. to d.c. — rectification."])
O("A transistor is used mainly to ___",
  ["amplify or switch signals", "store charge", "convert a.c. to d.c.", "step up voltage"],
  ["A small base current controls a much larger current, so a transistor works as an amplifier or as a fast switch."])
O("Which of these is an input device of a computer?", ["Scanner", "Printer", "Monitor", "Speaker"],
  ["A scanner puts information into the computer; the other three take information out."])
O("Adding a controlled impurity to a pure semiconductor to change its conductivity is called ___",
  ["doping", "rectifying", "amplifying", "insulating"],
  ["Doping with, for example, phosphorus gives n-type material and with boron gives p-type."])
T("(a) State two differences between conductors and insulators, giving one example of each.<br>"
  "(b) What is rectification? Name the component used for it.<br>"
  "(c) Name the four main units of a computer system and state the function of each.<br>"
  "(d) State three ways in which ICT has helped education in Ghana.",
  ["(a) Conductors have many free electrons and allow current to flow easily (copper, aluminium); insulators have almost no free electrons "
   "and do not allow current to flow (rubber, plastic, dry wood). Conductors are used for cables; insulators are used to cover them.",
   "(b) Rectification is the process of changing alternating current (a.c.) into direct current (d.c.). The component used is the <b>diode</b>.",
   "(c) <b>Input unit</b> — feeds data into the computer (keyboard, mouse). <b>Central processing unit</b> — carries out the instructions and "
   "controls the other units. <b>Storage/memory unit</b> — holds data and programs (RAM, hard disk). <b>Output unit</b> — presents the results "
   "(monitor, printer).",
   "(d) Access to learning material and past questions online; distance and online learning; faster processing of results and school records; "
   "use of projectors, videos and simulations in teaching; communication between schools, teachers and parents."], marks=12)

S = "Interactions of Matter"

# ------------------------------------------------------------------ 27
topic("eco", "Ecosystems & food chains", S, [
    "Ecosystem = the living community plus its non-living environment.",
    "Food chain: producer → primary consumer → secondary consumer → tertiary consumer, with decomposers acting at every level.",
    "Only about 10% of the energy at one trophic level passes to the next, which is why chains are short.",
    "Symbiosis (mutualism) benefits both; parasitism benefits one and harms the other; commensalism benefits one without harming the other.",
    "Terms: habitat (where an organism lives), population, community, niche, biome.",
])
O("In the food chain 'grass → grasshopper → lizard → hawk', the lizard is a ___",
  ["secondary consumer", "primary consumer", "producer", "decomposer"],
  ["Grass is the producer, the grasshopper the primary consumer and the lizard, which eats the grasshopper, the secondary consumer."])
O("Which group of organisms is responsible for returning nutrients from dead bodies to the soil?",
  ["Decomposers", "Producers", "Herbivores", "Carnivores"],
  ["Bacteria and fungi break down dead matter, releasing mineral salts that plants can use again."])
O("The relationship between <i>Rhizobium</i> bacteria and a cowpea plant is an example of ___",
  ["mutualism", "parasitism", "commensalism", "predation"],
  ["The bacteria get food and shelter while the plant gets fixed nitrogen — both benefit."])
O("Approximately what percentage of the energy at one trophic level is passed on to the next?",
  ["10%", "50%", "90%", "100%"],
  ["Most energy is lost as heat, in respiration and in undigested material, so only about a tenth is passed on."],
  v=10, nv=[10, 50, 90, 100])
O("The place where an organism lives is called its ___", ["habitat", "niche", "population", "community"],
  ["A habitat is the physical place; the niche is the role the organism plays there."])
T("(a) Define the terms: (i) ecosystem; (ii) food web; (iii) trophic level.<br>"
  "(b) Construct a food chain of four organisms found on a Ghanaian farm and name the trophic level of each.<br>"
  "(c) Explain why food chains rarely have more than five links.<br>(d) State two effects of removing all the carnivores from an ecosystem.",
  ["(a)(i) An <b>ecosystem</b> is a community of living organisms interacting with one another and with the non-living parts of their environment.",
   "(ii) A <b>food web</b> is a network of interconnected food chains in a community.",
   "(iii) A <b>trophic level</b> is a feeding level in a food chain.",
   "(b) maize (producer) → grasshopper (primary consumer/herbivore) → toad (secondary consumer) → snake (tertiary consumer). "
   "Decomposers act on all of them.",
   "(c) Because only about 10% of the energy at each level is passed on; after four or five links there is too little energy left to support "
   "another population.",
   "(d) The population of herbivores would increase sharply at first; the vegetation would then be overgrazed and destroyed, "
   "after which the herbivores themselves would starve and disease would spread — the ecosystem loses its balance."], marks=15)

# ------------------------------------------------------------------ 28
topic("force", "Force, motion & pressure", S, [
    "Newton's first law: a body stays at rest or in uniform motion unless a force acts on it (inertia).",
    "F = ma;  weight W = mg (g ≈ 10 m/s²). Mass is in kilograms; weight is a force in newtons.",
    "a = (v − u)/t;  v = u + at;  s = ut + ½at².",
    "Pressure P = F/A (pascals). In a liquid, P = ρgh — it depends on depth and density, not on the shape of the vessel.",
    "Atmospheric pressure is measured with a barometer; it decreases with height.",
])
O("A body of mass 5 kg is acted on by a force of 20 N. Calculate its acceleration.",
  ["4 m/s²", "100 m/s²", "0.25 m/s²", "25 m/s²"],
  ["F = ma ⇒ a = F ÷ m", "= 20 ÷ 5 = 4 m/s²"], v=20 / 5)
O("A car moving at 5 m/s accelerates uniformly to 20 m/s in 3 s. Calculate its acceleration.",
  ["5 m/s²", "6.7 m/s²", "15 m/s²", "45 m/s²"],
  ["a = (v − u) ÷ t = (20 − 5) ÷ 3", "= 15 ÷ 3 = 5 m/s²"], v=(20 - 5) / 3)
O("A force of 200 N acts on an area of 0.5 m². Calculate the pressure exerted.",
  ["400 Pa", "100 Pa", "40 Pa", "0.0025 Pa"],
  ["P = F ÷ A = 200 ÷ 0.5", "= 400 Pa"], v=200 / 0.5)
O("Calculate the pressure at a point 2 m below the surface of water. [density = 1000 kg/m³, g = 10 m/s²]",
  ["20000 Pa", "2000 Pa", "5000 Pa", "500 Pa"],
  ["P = ρgh = 1000 × 10 × 2", "= 20000 Pa (20 kPa)"], v=1000 * 10 * 2)
O("The weight of a body of mass 8 kg on the earth's surface is ___ [g = 10 m/s²]", ["80 N", "8 N", "0.8 N", "800 N"],
  ["W = mg = 8 × 10 = 80 N"], v=8 * 10)
T("(a) State the difference between mass and weight.<br>"
  "(b) A vehicle of mass 1200 kg starts from rest and reaches a speed of 24 m/s in 8 s. Calculate (i) its acceleration; (ii) the force applied.<br>"
  "(c) Explain why the walls of a dam are made thicker at the bottom than at the top.<br>"
  "(d) A rectangular block of weight 60 N rests on a surface with its base measuring 0.2 m by 0.3 m. Calculate the pressure on the surface.",
  ["(a) Mass is the quantity of matter in a body; it is measured in kilograms with a beam balance and is the same everywhere. "
   "Weight is the force with which gravity pulls the body; it is measured in newtons with a spring balance and varies from place to place.",
   "(b)(i) a = (24 − 0) ÷ 8 = <b>3 m/s²</b>",
   "(ii) F = ma = 1200 × 3 = <b>3600 N</b>",
   "(c) Pressure in a liquid increases with depth (P = ρgh), so the water pushes hardest at the bottom; the thicker wall there "
   "withstands the greater pressure.",
   "(d) Area = 0.2 × 0.3 = 0.06 m²",
   "P = F ÷ A = 60 ÷ 0.06 = <b>1000 Pa</b>"], marks=15,
  ok=(24 / 8 == 3 and 1200 * 3 == 3600 and close(60 / (0.2 * 0.3), 1000)))

# ------------------------------------------------------------------ 29
topic("machines", "Work, power & simple machines", S, [
    "Work = force × distance moved in the direction of the force (joules). Power = work ÷ time (watts).",
    "Mechanical advantage MA = load ÷ effort.  Velocity ratio VR = distance moved by effort ÷ distance moved by load.",
    "Efficiency = (MA ÷ VR) × 100% = (work output ÷ work input) × 100%. It is always less than 100% because of friction and the weight of moving parts.",
    "Levers: first class (see-saw, scissors), second class (wheelbarrow, bottle opener), third class (tongs, fishing rod, human forearm).",
    "For an inclined plane, VR = length ÷ height; for a pulley system, VR = number of rope sections supporting the load.",
])
O("A man pushes a load with a force of 50 N through a distance of 4 m. Calculate the work done.",
  ["200 J", "12.5 J", "54 J", "0.08 J"],
  ["Work = force × distance = 50 × 4", "= 200 J"], v=50 * 4)
O("A machine does 600 J of work in 30 s. Calculate its power.", ["20 W", "18000 W", "0.05 W", "630 W"],
  ["Power = work ÷ time = 600 ÷ 30", "= 20 W"], v=600 / 30)
O("A pulley system is used to raise a load of 200 N with an effort of 50 N. Calculate the mechanical advantage.",
  ["4", "0.25", "250", "150"],
  ["MA = load ÷ effort = 200 ÷ 50 = 4"], v=200 / 50)
O("A machine with a velocity ratio of 5 has a mechanical advantage of 4. Calculate its efficiency.",
  ["80%", "125%", "20%", "90%"],
  ["Efficiency = (MA ÷ VR) × 100% = (4 ÷ 5) × 100%", "= 80%"], v=4 / 5 * 100)
O("A wheelbarrow is an example of a ___ class lever.", ["second", "first", "third", "fourth"],
  ["In a wheelbarrow the load is between the fulcrum (the wheel) and the effort (the hands) — a second-class lever."])
T("(a) Define mechanical advantage, velocity ratio and efficiency.<br>"
  "(b) An effort of 150 N is used to raise a load of 450 N using a pulley system in which the effort moves 6 m while the load rises 1.5 m. "
  "Calculate (i) MA; (ii) VR; (iii) efficiency.<br>"
  "(c) Give two reasons why the efficiency of a machine is always less than 100%.<br>"
  "(d) Name the class of lever in each case: scissors, tongs, bottle opener.",
  ["(a) <b>MA</b> = load ÷ effort. <b>VR</b> = distance moved by effort ÷ distance moved by load. "
   "<b>Efficiency</b> = (work output ÷ work input) × 100%, or (MA ÷ VR) × 100%.",
   "(b)(i) MA = 450 ÷ 150 = <b>3</b>",
   "(ii) VR = 6 ÷ 1.5 = <b>4</b>",
   "(iii) Efficiency = (3 ÷ 4) × 100 = <b>75%</b>",
   "(c) Some of the work input is used to overcome friction between the moving parts, and some is used to lift the moving parts of the "
   "machine itself (ropes, pulley blocks). Both appear mainly as heat, so the useful work output is always less than the work input.",
   "(d) Scissors — <b>first class</b>; tongs — <b>third class</b>; bottle opener — <b>second class</b>."], marks=15,
  ok=(450 / 150 == 3 and 6 / 1.5 == 4 and 3 / 4 * 100 == 75))

# ------------------------------------------------------------------ 30
topic("health", "Diseases, immunisation & first aid", S, [
    "Pathogens: bacteria (cholera, tuberculosis), viruses (measles, HIV, COVID-19), protozoa (malaria), fungi (ringworm), worms (bilharzia).",
    "Transmission: air (droplets), water and food, vectors (mosquito, housefly), contact, and body fluids.",
    "Immunisation gives the body antibodies or makes it produce them; EPI vaccines include BCG, OPV, DPT, measles and yellow fever.",
    "First aid for a burn: cool with clean running water for at least ten minutes; never apply oil or toothpaste.",
    "Drug abuse: taking a drug without prescription or in the wrong amount; it damages the liver, brain and lungs and can cause addiction.",
])
O("Malaria is caused by a ___", ["protozoan", "bacterium", "virus", "fungus"],
  ["The parasite is <i>Plasmodium</i>, a protozoan, carried by the female <i>Anopheles</i> mosquito."])
O("Which of these diseases is caused by a virus?", ["Measles", "Cholera", "Tuberculosis", "Ringworm"],
  ["Measles is viral; cholera and tuberculosis are bacterial and ringworm is fungal."])
O("The BCG vaccine given to a newborn baby protects against ___",
  ["tuberculosis", "measles", "polio", "tetanus"],
  ["BCG (Bacille Calmette–Guérin) protects against tuberculosis."])
O("The best immediate first aid for a minor burn is to ___",
  ["cool it with clean running water", "apply engine oil", "rub it with toothpaste", "cover it with ash"],
  ["Cooling with clean water for about ten minutes reduces the damage and the pain.",
   "Oil, toothpaste and ash trap heat and introduce infection."])
O("Which of the following is a social effect of drug abuse?",
  ["Increase in crime and broken homes", "Damage to the liver", "Loss of appetite", "Shortness of breath"],
  ["Liver damage, loss of appetite and breathlessness are effects on the body; crime and family breakdown are social effects."])
T("(a) Name two diseases spread by each of the following: (i) air; (ii) water; (iii) vectors.<br>"
  "(b) Explain how immunisation protects a child against disease.<br>"
  "(c) Describe the first aid you would give to someone who has fainted.<br>"
  "(d) State four effects of drug abuse on a student.",
  ["(a)(i) Air/droplets: tuberculosis, measles, influenza, COVID-19, meningitis.",
   "(ii) Water: cholera, typhoid, dysentery, guinea worm, bilharzia.",
   "(iii) Vectors: malaria and yellow fever (mosquito), sleeping sickness (tsetse fly), cholera and typhoid carried by houseflies.",
   "(b) A vaccine contains a weakened, killed or partial form of the pathogen (or its antigen). It causes the body's white blood cells to "
   "produce antibodies and memory cells without the child becoming ill, so if the real pathogen enters later, antibodies are produced "
   "quickly and in large amounts and the disease is prevented.",
   "(c) Lay the person flat on the back in a cool, airy place and loosen tight clothing at the neck and waist. "
   "Raise the legs slightly above the level of the head to help blood reach the brain. Keep onlookers away so that air can circulate, "
   "and do not give anything by mouth while the person is unconscious. Turn the head to one side, and when the person recovers, "
   "give sips of water and seek medical help if recovery is slow.",
   "(d) Poor concentration and falling grades; absenteeism and dropping out; damage to health (liver, lungs, brain) and addiction; "
   "involvement in crime and violence; loss of friends and family support; mental illness."], marks=15)

# ------------------------------------------------------------------ 31
topic("genes", "Variation, inheritance & biotechnology", S, [
    "Variation may be continuous (height, weight) or discontinuous (blood group, sex, tongue rolling).",
    "Genes are carried on chromosomes; humans have 23 pairs, of which one pair determines sex (XX female, XY male).",
    "A dominant allele shows in the offspring even when only one copy is present; a recessive one shows only in the homozygous state.",
    "Monohybrid cross of two heterozygotes (Tt × Tt) gives a 3 : 1 ratio.",
    "Biotechnology uses living things in industry: brewing, baking, yoghurt, antibiotics, biogas and genetic engineering.",
])
O("Which of these is an example of discontinuous variation?", ["Blood group", "Height", "Weight", "Skin colour"],
  ["Blood group falls into distinct classes (A, B, AB, O) with nothing in between; height and weight vary continuously."])
O("A human body cell contains ___ pairs of chromosomes.", ["23", "46", "22", "12"],
  ["A human body cell has 46 chromosomes, that is 23 pairs; a gamete has 23 single chromosomes."],
  v=23, nv=[23, 46, 22, 12])
O("The sex of a child is determined by the ___",
  ["sperm from the father", "egg from the mother", "size of the placenta", "diet of the mother"],
  ["The mother's egg always carries X. The sperm may carry X (girl) or Y (boy), so the father's sperm decides the sex."])
O("When two heterozygous tall plants (Tt) are crossed, what is the expected ratio of tall to short offspring?",
  ["3 : 1", "1 : 1", "1 : 3", "2 : 1"],
  ["The cross gives TT, Tt, Tt and tt — three tall to one short."])
O("Which of these processes uses micro-organisms to make a food product?",
  ["Production of yoghurt", "Filtration of water", "Distillation of crude oil", "Galvanising of iron"],
  ["Lactic acid bacteria ferment milk sugar to make yoghurt — an everyday use of biotechnology."])
T("(a) State two differences between continuous and discontinuous variation, with one example of each.<br>"
  "(b) Using a genetic diagram, show the cross between a homozygous tall pea plant (TT) and a homozygous short one (tt), and state the "
  "appearance of the F1 generation.<br>(c) If the F1 plants are crossed among themselves, what ratio would you expect in the F2?<br>"
  "(d) State three uses of biotechnology.",
  ["(a) Continuous variation shows a complete range of values between two extremes and is usually controlled by many genes and affected by "
   "the environment (height, weight). Discontinuous variation falls into clear-cut groups with no intermediates and is controlled by one or "
   "a few genes (blood group, sex, ability to roll the tongue).",
   "(b) Parents: TT × tt. Gametes: all T from one parent, all t from the other.",
   "F1: all <b>Tt</b> — every plant is <b>tall</b>, because T (tall) is dominant over t (short).",
   "(c) Tt × Tt gives TT, Tt, Tt, tt ⇒ <b>3 tall : 1 short</b>.",
   "(d) Brewing and baking with yeast; making yoghurt and cheese; producing antibiotics such as penicillin from fungi; "
   "producing biogas from waste; making insulin and vaccines by genetic engineering; producing improved, disease-resistant crop varieties."], marks=15)

# ------------------------------------------------------------------ 32
topic("env", "Environment, pollution & climate change", S, [
    "Pollution types: air (smoke, exhaust fumes), water (sewage, mining waste), land (refuse, plastics), noise.",
    "Greenhouse gases (carbon dioxide, methane) trap heat and cause global warming; CFCs damage the ozone layer.",
    "Effects of deforestation: erosion, loss of soil fertility, drought, loss of wildlife, increased carbon dioxide.",
    "The three Rs: reduce, reuse, recycle. Waste may be separated, composted, incinerated or land-filled.",
    "Conservation: afforestation, forest reserves, laws against galamsey and bad fishing methods, environmental education.",
])
O("Which gas contributes most to global warming?", ["Carbon dioxide", "Nitrogen", "Oxygen", "Helium"],
  ["Carbon dioxide from burning fossil fuels and forests is the main greenhouse gas by quantity."])
O("The gases that destroy the ozone layer are ___",
  ["chlorofluorocarbons", "oxides of iron", "noble gases", "hydrocarbons"],
  ["CFCs, once used in refrigerators and aerosol sprays, break down ozone in the stratosphere."])
O("Which of these is a consequence of deforestation?", ["Increased soil erosion", "Increased rainfall", "Cooler temperatures", "Richer topsoil"],
  ["Without tree cover and roots, rain washes the topsoil away, and the loss of trees also reduces rainfall and raises temperatures."])
O("The best way to deal with plastic and metal waste in a community is to ___",
  ["separate and recycle it", "burn it in the open", "bury it in a river bed", "dump it in the gutter"],
  ["Recycling saves raw materials and energy.",
   "Open burning of plastic releases toxic fumes, and dumping blocks drains and causes floods."])
O("Which human activity is most responsible for the pollution of rivers in south-western Ghana?",
  ["Small-scale mining", "Fishing with nets", "Cattle rearing", "Planting of cocoa"],
  ["Galamsey operations wash mud and mercury into the rivers, making the water unusable."])
T("(a) Name four types of pollution and give one source and one effect of each.<br>"
  "(b) Explain the greenhouse effect and state two of its consequences.<br>"
  "(c) State four ways of managing solid waste in a community.<br>"
  "(d) Suggest three ways students can help protect the environment.",
  ["(a) <b>Air</b> — vehicle exhaust and factory smoke; causes respiratory disease and acid rain. "
   "<b>Water</b> — sewage and mining waste; causes cholera and kills aquatic life. "
   "<b>Land</b> — refuse and plastics; breeds pests and makes land unusable. "
   "<b>Noise</b> — loudspeakers, generators and heavy traffic; causes deafness, stress and loss of concentration.",
   "(b) Short-wave radiation from the sun passes through the atmosphere and warms the earth. The earth re-radiates the heat as long-wave "
   "radiation, which greenhouse gases such as carbon dioxide and methane absorb and send back, so the atmosphere warms up. "
   "Consequences: rising global temperatures; melting of ice and rising sea levels that flood coastal towns; "
   "unpredictable rainfall, drought and failed harvests.",
   "(c) Separate waste at source into organic and inorganic; compost the organic part for manure; recycle plastics, metals, glass and paper; "
   "use properly engineered sanitary landfills; incinerate hazardous medical waste; educate the public and enforce sanitation by-laws.",
   "(d) Join or form a school environmental club and plant trees; keep the school and community clean and stop dumping in gutters; "
   "reduce, reuse and recycle materials such as sachets and bottles; switch off lights and fans when not needed; "
   "teach others in the community about the dangers of bush burning and galamsey."], marks=15)
