from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

S = "Number & Numeration"

# ------------------------------------------------------------ integers, factors, multiples
topic("intfac", "Integers, factors & multiples", S, [
    "Integers are whole numbers and their negatives: … −3, −2, −1, 0, 1, 2, 3 …",
    "A factor divides a number exactly; a multiple is what you get when you multiply it.",
    "Prime numbers have exactly two factors: 2, 3, 5, 7, 11, 13 … (1 is NOT prime).",
    "HCF = product of the COMMON prime factors, taking the LOWEST power of each.",
    "LCM = product of ALL prime factors, taking the HIGHEST power of each.",
    "Rules of signs: (−) × (−) = (+);  (−) × (+) = (−);  a − (−b) = a + b",
])
O("Find the HCF of 24, 36 and 60.", ["12", "6", "4", "180"],
  ["24 = 2^3 × 3;  36 = 2^2 × 3^2;  60 = 2^2 × 3 × 5",
   "Common primes: 2 and 3. Take the lowest power of each: 2^2 × 3.",
   "HCF = 4 × 3 = 12"], v=math.gcd(math.gcd(24, 36), 60))
O("Find the LCM of 24, 36 and 60.", ["360", "180", "120", "720"],
  ["24 = 2^3 × 3;  36 = 2^2 × 3^2;  60 = 2^2 × 3 × 5",
   "Take the highest power of every prime: 2^3 × 3^2 × 5.",
   "LCM = 8 × 9 × 5 = 360"], v=math.lcm(24, 36, 60))
O("Evaluate −8 − (−5) + (−3).", ["−6", "−16", "0", "−10"],
  ["−8 − (−5) = −8 + 5 = −3", "−3 + (−3) = −6"], v=-8 - (-5) + (-3))
O("Which of the following is a prime number?", ["29", "27", "21", "1"],
  ["A prime has exactly two factors, 1 and itself.",
   "27 = 3 × 9, 21 = 3 × 7, and 1 has only one factor.", "29 has no factor besides 1 and 29."],
  ok=[t for t in [29, 27, 21, 1] if t > 1 and all(t % d for d in range(2, t))] == [29])
O("Three bells ring at intervals of 6, 9 and 15 minutes. If they ring together at 8:00 a.m., when will they next ring together?",
  ["9:30 a.m.", "9:00 a.m.", "8:45 a.m.", "10:00 a.m."],
  ["They ring together again after the LCM of the intervals.",
   "6 = 2 × 3;  9 = 3^2;  15 = 3 × 5 ⇒ LCM = 2 × 3^2 × 5 = 90 minutes.",
   "90 minutes after 8:00 a.m. is 9:30 a.m."], ok=math.lcm(6, 9, 15) == 90)
T("(a) Express 180 and 504 as products of their prime factors, and hence find their HCF and LCM.<br>"
  "(b) Evaluate (−12) ÷ (−4) + (−3) × 2.<br>"
  "(c) Find the smallest number which when divided by 12, 15 and 18 leaves a remainder of 5 in each case.",
  ["(a) 180 = 2^2 × 3^2 × 5;  504 = 2^3 × 3^2 × 7",
   "HCF = common primes to the lowest power = 2^2 × 3^2 = <b>36</b>",
   "LCM = all primes to the highest power = 2^3 × 3^2 × 5 × 7 = <b>2520</b>",
   "(b) (−12) ÷ (−4) = 3;  (−3) × 2 = −6;  3 + (−6) = <b>−3</b>",
   "(c) The number is LCM + 5. LCM of 12, 15 and 18 = 180.",
   "Smallest number = 180 + 5 = <b>185</b>"], marks=10,
  ok=(math.gcd(180, 504) == 36 and math.lcm(180, 504) == 2520 and math.lcm(12, 15, 18) == 180))
extras("intfac",
  plain="Factors divide into a number; multiples come out of it. HCF is the biggest number that divides them "
        "all, and LCM is the smallest number they all divide into. Prime factors make both easy to find.",
  examples=[
    E("Find the HCF and LCM of 18 and 24 using prime factors.",
      "Step 1. Break each one down: 18 = 2 × 3 × 3 = 2 × 3^2;  24 = 2 × 2 × 2 × 3 = 2^3 × 3.",
      "Step 2. HCF — take only the primes in BOTH, at the lowest power: 2 × 3 = <b>6</b>.",
      "Step 3. LCM — take every prime at its highest power: 2^3 × 3^2 = 8 × 9 = <b>72</b>.",
      "Step 4. Check: 6 divides both; both divide 72."),
    E("A trader has 48 oranges and 60 mangoes. She wants to make identical packs with nothing left over. "
      "What is the largest number of packs, and what goes into each?",
      "Step 1. 'Largest number of equal packs with nothing left' means HCF.",
      "Step 2. 48 = 2^4 × 3;  60 = 2^2 × 3 × 5 ⇒ HCF = 2^2 × 3 = 12.",
      "Step 3. So <b>12 packs</b>, each with 48 ÷ 12 = <b>4 oranges</b> and 60 ÷ 12 = <b>5 mangoes</b>.")])
assert math.gcd(48, 60) == 12

S = "Mensuration"

# ------------------------------------------------------------ similar shapes & scale
topic("simil", "Similar shapes, congruence & scale", S, [
    "Similar shapes have the same shape but different size: equal angles, and sides in the same ratio.",
    "Congruent shapes are exactly the same shape AND size (SSS, SAS, ASA, RHS).",
    "If lengths are in the ratio k, areas are in the ratio k^2 and volumes in the ratio k^3.",
    "Map scale 1 : n means 1 cm on the map stands for n cm on the ground.",
    "On a map of scale 1 : 50 000, 1 cm represents 0.5 km, and 1 cm^2 represents 0.25 km^2.",
])
O("Two similar triangles have corresponding sides 6 cm and 9 cm. The area of the smaller is 24 cm². "
  "Find the area of the larger.", ["54 cm²", "36 cm²", "16 cm²", "81 cm²"],
  ["Ratio of sides = 6 : 9 = 2 : 3.", "Ratio of areas = 2^2 : 3^2 = 4 : 9.",
   "Area = 24 × 9/4 = 54 cm²"], v=24 * 9 / 4)
O("Two cones are similar. Their heights are 4 cm and 8 cm. The volume of the small one is 20 cm³. "
  "Find the volume of the large one.", ["160 cm³", "40 cm³", "80 cm³", "320 cm³"],
  ["Ratio of lengths = 1 : 2.", "Ratio of volumes = 1^3 : 2^3 = 1 : 8.", "Volume = 20 × 8 = 160 cm³"], v=20 * 8)
O("On a map of scale 1 : 50 000, two towns are 4 cm apart. Find the actual distance in kilometres.",
  ["2 km", "20 km", "0.2 km", "200 km"],
  ["4 cm on the map = 4 × 50 000 = 200 000 cm on the ground.",
   "200 000 cm = 2000 m = 2 km"], v=4 * 50000 / 100000)
O("Which condition does NOT prove two triangles congruent?", ["AAA", "SSS", "SAS", "RHS"],
  ["AAA only makes the triangles SIMILAR — the same shape but possibly different sizes.",
   "SSS, SAS, ASA and RHS all fix the size as well as the shape."])
O("A photograph 8 cm by 6 cm is enlarged so that the longer side becomes 20 cm. Find the new shorter side.",
  ["15 cm", "18 cm", "12 cm", "14 cm"],
  ["Scale factor = 20 ÷ 8 = 2.5", "New shorter side = 6 × 2.5 = 15 cm"], v=6 * (20 / 8))
T("(a) In triangle ABC, PQ is parallel to BC, with P on AB and Q on AC. AP = 3 cm, PB = 5 cm and PQ = 4.5 cm. "
  "Find BC.<br>(b) The areas of two similar rectangles are 50 cm² and 162 cm². If the shorter side of the "
  "smaller is 5 cm, find the shorter side of the larger.<br>"
  "(c) A map has a scale of 1 : 25 000. Find (i) the actual length, in km, of a road 12 cm long on the map; "
  "(ii) the area on the map, in cm², of a farm of 1 km².",
  ["(a) Triangles APQ and ABC are similar. AB = 3 + 5 = 8 cm.",
   f"{F('AP','AB')} = {F('PQ','BC')} ⇒ {F(3,8)} = {F('4.5','BC')} ⇒ BC = {F('4.5 × 8', 3)} = <b>12 cm</b>",
   "(b) Ratio of areas = 50 : 162 = 25 : 81, so the ratio of sides = 5 : 9.",
   f"Shorter side of the larger = 5 × {F(9,5)} = <b>9 cm</b>",
   "(c)(i) 12 cm × 25 000 = 300 000 cm = 3000 m = <b>3 km</b>",
   "(ii) 1 cm on the map = 0.25 km, so 1 cm² = 0.0625 km².",
   f"Area on the map = {F(1, '0.0625')} = <b>16 cm²</b>"], marks=12,
  ok=(close(4.5 * 8 / 3, 12) and close(5 * 9 / 5, 9) and close(12 * 25000 / 100000, 3) and close(1 / 0.0625, 16)))
extras("simil",
  plain="Similar means same shape, different size — every length is multiplied by the same number (the scale "
        "factor). Remember: lengths × k, areas × k², volumes × k³. A map is just a very large enlargement in reverse.",
  examples=[
    E("A model of a water tank is made to a scale of 1 : 20. The model holds 2 litres. How much does the real tank hold?",
      "Step 1. Lengths are in the ratio 1 : 20.",
      "Step 2. Volumes are in the ratio 1^3 : 20^3 = 1 : 8000.",
      "Step 3. Real tank = 2 × 8000 = <b>16 000 litres</b> (16 m³)."),
    E("A tree casts a shadow 6 m long at the same time that a 1.5 m pole casts a shadow 0.9 m long. "
      "Find the height of the tree.",
      "Step 1. The sun's rays make the two triangles similar.",
      f"Step 2. {F('tree', 'its shadow')} = {F('pole', 'its shadow')} ⇒ {F('h', 6)} = {F('1.5', '0.9')}",
      "Step 3. h = 6 × 1.5 ÷ 0.9 = <b>10 m</b>.",
      fig=draw.tri(a="h = ?", c="6 m shadow", right=True, label="Tree and its shadow"))])
assert close(6 * 1.5 / 0.9, 10) and 20 ** 3 * 2 == 16000

# ------------------------------------------------------------ earth as a sphere
topic("earth", "Longitude, latitude & distances on the earth", S, [
    "Latitude lines run east–west (the equator is 0°); longitude lines (meridians) run north–south (Greenwich is 0°).",
    "Radius of the earth R ≈ 6400 km. Take π = 22/7 unless told otherwise.",
    "Along a meridian (same longitude): distance = (θ/360) × 2πR, where θ is the difference in latitude.",
    "Along a parallel of latitude: distance = (θ/360) × 2πR cos α, where α is the latitude and θ the difference in longitude.",
    "Along the equator, cos 0° = 1, so the parallel formula becomes the full circle formula.",
    "1 hour of time = 15° of longitude; places east of Greenwich are ahead in time.",
])
O("Two towns on the equator differ in longitude by 30°. Find the distance between them. [R = 6400 km, π = 22/7]",
  ["3352.4 km", "1676.2 km", "6704.8 km", "2513.0 km"],
  [f"Distance = {F(30,360)} × 2 × {F(22,7)} × 6400",
   "2 × 22/7 × 6400 = 40 228.57 km (the circumference)",
   "Distance = 40 228.57 ÷ 12 = 3352.4 km"],
  v=float(Fr(30, 360) * 2 * Fr(22, 7) * 6400), tol=1e-4)
O("Find the distance along a meridian between P(20°N, 15°E) and Q(50°N, 15°E). [R = 6400 km, π = 22/7]",
  ["3352.4 km", "2234.9 km", "5587.3 km", "1676.2 km"],
  ["Same longitude, so use the meridian formula with θ = 50 − 20 = 30°.",
   f"Distance = {F(30,360)} × 2 × {F(22,7)} × 6400 = 3352.4 km"],
  v=float(Fr(30, 360) * 2 * Fr(22, 7) * 6400), tol=1e-4)
O("Find the radius of the parallel of latitude 60°N. [R = 6400 km]", ["3200 km", "6400 km", "5542 km", "1600 km"],
  ["Radius of a parallel = R cos α = 6400 × cos 60°.", "cos 60° = 0.5, so r = 3200 km"], v=6400 * 0.5)
O("The longitude difference between two places is 45°. What is the difference in their local times?",
  ["3 hours", "45 minutes", "1 hour 30 minutes", "4 hours"],
  ["The earth turns 360° in 24 hours, so 15° takes 1 hour.", "45 ÷ 15 = 3 hours"], v=45 / 15)
O("Which of these points lies on the equator?", ["(0°, 25°W)", "(25°N, 0°)", "(25°S, 25°E)", "(90°N, 0°)"],
  ["The equator is the parallel of latitude 0°, so the LATITUDE must be 0°.",
   "In (0°, 25°W) the latitude is 0°, so it is on the equator."])
T("[Take R = 6400 km and π = 22/7]<br>"
  "(a) Find the distance along a parallel of latitude between A(60°N, 20°E) and B(60°N, 65°E).<br>"
  "(b) Find the distance along the meridian between B(60°N, 65°E) and C(15°N, 65°E).<br>"
  "(c) If the local time at a place on longitude 15°E is 2:00 p.m., what is the local time at 45°W?",
  ["(a) Same latitude ⇒ use distance = (θ/360) × 2πR cos α, with θ = 65 − 20 = 45° and α = 60°.",
   f"= {F(45,360)} × 2 × {F(22,7)} × 6400 × cos 60°",
   "= 0.125 × 40 228.57 × 0.5 = <b>2514.3 km</b>",
   "(b) Same longitude ⇒ meridian formula, θ = 60 − 15 = 45°.",
   f"= {F(45,360)} × 2 × {F(22,7)} × 6400 = <b>5028.6 km</b>",
   "(c) Longitude difference = 15 + 45 = 60° ⇒ time difference = 60 ÷ 15 = 4 hours.",
   "45°W is WEST of 15°E, so it is behind: 2:00 p.m. − 4 h = <b>10:00 a.m.</b>"], marks=12,
  ok=(close(float(Fr(45, 360) * 2 * Fr(22, 7) * 6400 * Fr(1, 2)), 2514.2857, 1e-3)
      and close(float(Fr(45, 360) * 2 * Fr(22, 7) * 6400), 5028.5714, 1e-3) and (15 + 45) / 15 == 4))
extras("earth",
  plain="The earth is treated as a sphere of radius about 6400 km. Going north or south you travel along a "
        "meridian (a full-size circle). Going east or west you travel along a parallel of latitude, which is "
        "a smaller circle — that is why the cos of the latitude appears in the formula.",
  examples=[
    E("Find the distance between X(30°N, 10°W) and Y(30°N, 50°E), along their parallel of latitude. "
      "[R = 6400 km, π = 22/7, cos 30° = 0.866]",
      "Step 1. Same latitude, so use distance = (θ/360) × 2πR cos α.",
      "Step 2. θ = 10 + 50 = 60° (one is west and one is east, so ADD).",
      "Step 3. = (60/360) × 40 228.57 × 0.866 = 0.1667 × 40 228.57 × 0.866.",
      "Step 4. ≈ <b>5806 km</b>."),
    E("A plane leaves Accra (0°, 0°) and flies due north to 45°N. How far does it fly? [R = 6400 km, π = 22/7]",
      "Step 1. Due north means along a meridian, so no cosine is needed.",
      "Step 2. Distance = (45/360) × 2 × (22/7) × 6400.",
      "Step 3. = 0.125 × 40 228.57 = <b>5028.6 km</b>.")])
assert close(60 / 360 * 40228.5714 * 0.866, 5806, 1)

S = "Statistics & Probability"

# ------------------------------------------------------------ cumulative frequency
_f = [3, 5, 8, 12, 7, 5]
_cf = [sum(_f[:i + 1]) for i in range(len(_f))]
topic("cumfreq", "Cumulative frequency & quartiles", S, [
    "Cumulative frequency is a running total of the frequencies.",
    "An ogive is the graph of cumulative frequency against the UPPER class boundary.",
    "Median = the value at N/2;  lower quartile Q₁ at N/4;  upper quartile Q₃ at 3N/4 — read them off the ogive.",
    "Interquartile range = Q₃ − Q₁;  semi-interquartile range = (Q₃ − Q₁)/2.",
    "By formula: value = L + [(position − cf before) ÷ f] × c, where L is the lower class boundary and c the class width.",
    "Class boundaries remove the gaps: the class 21–30 has boundaries 20.5 and 30.5.",
])
O("The frequencies of six classes are 3, 5, 8, 12, 7 and 5. What is the cumulative frequency of the fourth class?",
  ["28", "12", "16", "40"],
  ["Add the frequencies up to and including the fourth class.", "3 + 5 + 8 + 12 = 28"], v=_cf[3])
O("For 40 values, at what position is the median read on an ogive?", ["20th", "10th", "30th", "40th"],
  ["The median is at N/2.", "40 ÷ 2 = 20th value."], v=40 / 2)
O("For a distribution of 40 values, at what position is the lower quartile Q₁?", ["10th", "20th", "30th", "4th"],
  ["Q₁ is at N/4.", "40 ÷ 4 = 10th value."], v=40 / 4)
O("If Q₁ = 23 and Q₃ = 43, find the semi-interquartile range.", ["10", "20", "33", "66"],
  ["Interquartile range = Q₃ − Q₁ = 43 − 23 = 20.", "Semi-interquartile range = 20 ÷ 2 = 10"], v=(43 - 23) / 2)
O("On an ogive, cumulative frequency is plotted against ___",
  ["the upper class boundary", "the class midpoint", "the lower class boundary", "the frequency"],
  ["Every value in the class is less than or equal to the upper boundary, so the running total belongs there."])
T("The table shows the marks of 40 candidates.<br>"
  "<table class=\"mt\"><tr><th>Marks</th><td>1–10</td><td>11–20</td><td>21–30</td><td>31–40</td><td>41–50</td><td>51–60</td></tr>"
  "<tr><th>Frequency</th><td>3</td><td>5</td><td>8</td><td>12</td><td>7</td><td>5</td></tr></table>"
  "(a) Prepare a cumulative frequency table.<br>(b) Draw the ogive.<br>"
  "(c) Use it to estimate the median, Q₁, Q₃ and the semi-interquartile range.<br>"
  "(d) If the pass mark is 35, estimate how many candidates passed.",
  ["(a) Upper boundaries 10.5, 20.5, 30.5, 40.5, 50.5, 60.5 with cumulative frequencies "
   "<b>3, 8, 16, 28, 35, 40</b>.",
   "(b) Plot cumulative frequency against the upper class boundary and join with a smooth curve.",
   "(c) <b>Median</b> at N/2 = 20th value: it lies in 31–40.",
   f"Median = 30.5 + ({F('20 − 16', 12)}) × 10 = 30.5 + 3.33 = <b>33.8</b>",
   f"<b>Q₁</b> at 10th value, in 21–30: 20.5 + ({F('10 − 8', 8)}) × 10 = 20.5 + 2.5 = <b>23.0</b>",
   f"<b>Q₃</b> at 30th value, in 41–50: 40.5 + ({F('30 − 28', 7)}) × 10 = 40.5 + 2.86 = <b>43.4</b>",
   "Semi-interquartile range = (43.4 − 23.0) ÷ 2 = <b>10.2</b>",
   "(d) Read the cumulative frequency at 35: about 20.5, so about 40 − 20.5 = <b>20 candidates</b> passed."],
  marks=15,
  fig=draw.barfig([("10.5", 3), ("20.5", 8), ("30.5", 16), ("40.5", 28), ("50.5", 35), ("60.5", 40)],
                  label="Cumulative frequency at each upper class boundary", ylab="cum. freq."),
  tip="Always use CLASS BOUNDARIES (20.5, 30.5 …), not the class limits, when you plot or use the formula.",
  ok=(_cf == [3, 8, 16, 28, 35, 40] and close(30.5 + 4 / 12 * 10, 33.833, 1e-2)
      and close(20.5 + 2 / 8 * 10, 23.0) and close(40.5 + 2 / 7 * 10, 43.357, 1e-2)))
extras("cumfreq",
  plain="A cumulative frequency table answers 'how many scored LESS THAN this?' Its graph, the ogive, lets "
        "you read off the middle value (median) and the quartiles that split the data into four equal parts.",
  examples=[
    E("From an ogive of 60 values, the 15th value is 28 and the 45th value is 52. Find the interquartile range.",
      "Step 1. Q₁ is at N/4 = 60 ÷ 4 = the 15th value ⇒ Q₁ = 28.",
      "Step 2. Q₃ is at 3N/4 = 45th value ⇒ Q₃ = 52.",
      "Step 3. Interquartile range = 52 − 28 = <b>24</b>; the semi-interquartile range is 12."),
    E("In a class of 50, the ogive shows 32 students scored less than 40 marks. "
      "How many scored 40 or more, and what percentage is that?",
      "Step 1. Read the cumulative frequency at 40: 32 students.",
      "Step 2. Scored 40 or more = 50 − 32 = <b>18 students</b>.",
      f"Step 3. Percentage = {F(18,50)} × 100 = <b>36%</b>.")])
assert 50 - 32 == 18 and 18 / 50 * 100 == 36
