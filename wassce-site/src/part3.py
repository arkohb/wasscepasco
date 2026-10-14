from core import *

S = "Trigonometry"

# ------------------------------------------------------------------ 23
topic("trig", "Trigonometric ratios & heights", S, [
    "SOH-CAH-TOA: sin = opp/hyp, cos = adj/hyp, tan = opp/adj",
    "Special angles: sin 30° = ½, cos 60° = ½, sin 60° = cos 30° = √3/2, tan 45° = 1, tan 60° = √3",
    "sin θ = cos(90° − θ) — complementary angles.",
    "The angle of elevation of A from B equals the angle of depression of B from A.",
    "Always add the observer's eye height when the question gives it.",
])
O(f"If sin θ = {F(3,5)} and θ is acute, find tan θ.", [F(3, 4), F(4, 5), F(4, 3), F(5, 3)],
  ["Opposite = 3, hypotenuse = 5, so adjacent = √(25 − 9) = 4", f"tan θ = {F(3,4)}"],
  v=Fr(3, 4), nv=[Fr(3, 4), Fr(4, 5), Fr(4, 3), Fr(5, 3)])
O("Evaluate sin 30° + cos 60°.", ["1", F(1, 2), "√3", F("√3", 2)],
  [f"sin 30° = {F(1,2)} and cos 60° = {F(1,2)}", f"{F(1,2)} + {F(1,2)} = 1"],
  v=1, nv=[1, Fr(1, 2), math.sqrt(3), math.sqrt(3) / 2])
O("From the top of a tower 30 m high, the angle of depression of a car on level ground is 30°. How far is the car from the foot of the tower?",
  ["30√3 m", "10√3 m", "15 m", "60 m"],
  [f"tan 30° = {F(30,'d')}", f"d = {F(30,'tan 30°')} = 30√3 m ≈ 51.96 m"],
  v=30 / math.tan(math.radians(30)), nv=[30 * math.sqrt(3), 10 * math.sqrt(3), 15, 60], tol=1e-9)
O("A ladder 8 m long leans against a wall making an angle of 60° with the horizontal ground. How far up the wall does it reach?",
  ["4√3 m", "4 m", "8√3 m", "6 m"],
  ["Height = 8 sin 60° = 8 × (√3/2) = 4√3 m ≈ 6.93 m"],
  v=8 * math.sin(math.radians(60)), nv=[4 * math.sqrt(3), 4, 8 * math.sqrt(3), 6], tol=1e-9)
O("If cos x = sin 40° and x is acute, find x.", ["50°", "40°", "140°", "60°"],
  ["cos x = sin(90° − x)", "90° − x = 40° ⇒ x = 50°"], v=50)
O("Solve 2 sin θ − 1 = 0 for 0° ≤ θ ≤ 180°.", ["θ = 30° or 150°", "θ = 30° only", "θ = 60° or 120°", "θ = 45° or 135°"],
  [f"sin θ = {F(1,2)}", "In the given range, θ = 30° or θ = 180° − 30° = 150°"],
  ok=[d for d in range(181) if close(2 * math.sin(math.radians(d)) - 1, 0, 1e-9)] == [30, 150])
T("A man 1.8 m tall stands 20 m away from the foot of a building on level ground. The angle of elevation of the top of the building from his eyes is 52°.<br>(a) Find the height of the building, correct to two decimal places.<br>(b) He walks 8 m towards the building. Find the new angle of elevation, correct to one decimal place.",
  ["(a) Let h be the height above eye level: tan 52° = h/20",
   "h = 20 × 1.27994 = 25.599 m", "Height of building = 25.599 + 1.8 = <b>27.40 m</b>",
   f"(b) New horizontal distance = 20 − 8 = 12 m", f"tan θ = {F('25.599', 12)} = 2.1332",
   "θ = <b>64.9°</b>"], marks=10,
  ok=(round(20 * math.tan(math.radians(52)) + 1.8, 2) == 27.40
      and round(math.degrees(math.atan(20 * math.tan(math.radians(52)) / 12)), 1) == 64.9))
T("(a) Without using tables or a calculator, evaluate sin 60° cos 30° − cos 60° sin 30°.<br>"
  "(b) Given that tan x = −5/12 and 90° < x < 180°, find sin x − cos x.<br>"
  "(c) Copy and complete the table for y = 2 sin x, then state the maximum value of y.<br>"
  "<table class=\"mt\"><tr><th>x</th><td>0°</td><td>30°</td><td>60°</td><td>90°</td><td>120°</td><td>150°</td><td>180°</td></tr>"
  "<tr><th>y</th><td>0</td><td></td><td>1.73</td><td></td><td></td><td>1</td><td></td></tr></table>",
  [f"(a) = ({F('√3',2)})({F('√3',2)}) − ({F(1,2)})({F(1,2)}) = {F(3,4)} − {F(1,4)} = <b>{F(1,2)}</b>",
   "(b) In the second quadrant sine is positive and cosine is negative.",
   f"With opposite 5 and adjacent 12, the hypotenuse is 13 ⇒ sin x = {F(5,13)}, cos x = −{F(12,13)}",
   f"sin x − cos x = {F(5,13)} + {F(12,13)} = <b>{F(17,13)}</b> (≈ 1.31)",
   "(c) 2 sin 30° = 1;  2 sin 90° = 2;  2 sin 120° = 1.73;  2 sin 180° = 0",
   "<table class=\"mt\"><tr><th>x</th><td>0°</td><td>30°</td><td>60°</td><td>90°</td><td>120°</td><td>150°</td><td>180°</td></tr>"
   "<tr><th>y</th><td>0</td><td>1</td><td>1.73</td><td>2</td><td>1.73</td><td>1</td><td>0</td></tr></table>",
   "Maximum value of y = <b>2</b> (at x = 90°)"], marks=12,
  ok=(close(math.sin(math.radians(60)) * math.cos(math.radians(30)) - math.cos(math.radians(60)) * math.sin(math.radians(30)), .5)
      and close(Fr(5, 13) + Fr(12, 13), Fr(17, 13))
      and [round(2 * math.sin(math.radians(d)), 2) for d in (0, 30, 60, 90, 120, 150, 180)] == [0, 1, 1.73, 2, 1.73, 1, 0]))

# ------------------------------------------------------------------ 24
topic("bear", "Bearings, sine & cosine rules", S, [
    "Bearings are measured clockwise from north and always written with three figures (e.g. 075°).",
    "Back bearing = bearing ± 180°.",
    "Sine rule: a/sin A = b/sin B = c/sin C",
    "Cosine rule: a^2 = b^2 + c^2 − 2bc cos A",
    "Area of a triangle = ½ab sin C",
])
O("The bearing of A from B is 065°. What is the bearing of B from A?", ["245°", "115°", "295°", "025°"],
  ["Back bearing = 065° + 180° = 245°"], v=65 + 180)
O("A ship sails 8 km due north, then 6 km due east. How far is it from its starting point?", ["10 km", "14 km", "2 km", "√28 km"],
  ["The path forms a right angle.", "d = √(8^2 + 6^2) = √100 = 10 km"], v=10, nv=[10, 14, 2, math.sqrt(28)])
O("Express the bearing S 40° W as a three-figure bearing.", ["220°", "140°", "040°", "320°"],
  ["Start from north and turn clockwise: south is 180°, then 40° further towards west gives 220°."], v=180 + 40)
O("In triangle ABC, a = 10 cm, ∠A = 30° and ∠B = 45°. Find b.", ["10√2 cm", "5√2 cm", "20 cm", "10√3 cm"],
  [f"{F('a','sin A')} = {F('b','sin B')} ⇒ b = {F('10 sin 45°','sin 30°')}",
   f"= {F('10 × 0.7071','0.5')} = 10√2 ≈ 14.14 cm"],
  v=10 * math.sin(math.radians(45)) / math.sin(math.radians(30)),
  nv=[10 * math.sqrt(2), 5 * math.sqrt(2), 20, 10 * math.sqrt(3)], tol=1e-9)
O("In triangle ABC, b = 5 cm, c = 7 cm and ∠A = 60°. Find a.", ["√39 cm", "√74 cm", "√109 cm", "39 cm"],
  ["a^2 = 25 + 49 − 2(5)(7)cos 60°", "= 74 − 70(0.5) = 39 ⇒ a = √39 ≈ 6.24 cm"],
  v=math.sqrt(39), nv=[math.sqrt(39), math.sqrt(74), math.sqrt(109), 39], tol=1e-9)
O("Find the area of a triangle with sides 6 cm and 8 cm and an included angle of 150°.", ["12 cm²", "24 cm²", "20.78 cm²", "48 cm²"],
  ["Area = ½ab sin C = ½ × 6 × 8 × sin 150°", "sin 150° = 0.5 ⇒ Area = 24 × 0.5 = 12 cm²"],
  v=.5 * 6 * 8 * math.sin(math.radians(150)), tol=1e-6)
T("A boat leaves port P and sails 12 km on a bearing of 060° to Q. It then sails 9 km on a bearing of 150° to R.<br>(a) Show that ∠PQR = 90°.<br>(b) Find the distance PR.<br>(c) Find the bearing of R from P, correct to the nearest degree.",
  ["(a) The bearing of P from Q is 060° + 180° = 240°. The bearing of R from Q is 150°.",
   "∠PQR = 240° − 150° = <b>90°</b>",
   "(b) By Pythagoras, PR = √(12^2 + 9^2) = √225 = <b>15 km</b>",
   f"(c) In right-angled triangle PQR, tan ∠QPR = {F(9,12)} = 0.75 ⇒ ∠QPR = 36.87°",
   "Bearing of R from P = 060° + 36.87° ≈ <b>097°</b>"], marks=12,
  ok=(math.hypot(12, 9) == 15 and round(60 + math.degrees(math.atan(9 / 12))) == 97))
T("Town Y is 50 km from town X on a bearing of 040°. Town Z is 70 km from X on a bearing of 110°.<br>(a) Find ∠YXZ.<br>(b) Find the distance YZ, correct to two decimal places.<br>(c) Find the area of triangle XYZ, correct to one decimal place.",
  ["(a) ∠YXZ = 110° − 040° = <b>70°</b>",
   "(b) By the cosine rule: YZ^2 = 50^2 + 70^2 − 2(50)(70)cos 70°",
   "= 2500 + 4900 − 7000(0.34202) = 7400 − 2394.14 = 5005.86",
   "YZ = <b>70.75 km</b>",
   "(c) Area = ½(50)(70) sin 70° = 1750 × 0.93969 = <b>1644.5 km²</b>"], marks=12,
  ok=(round(math.sqrt(2500 + 4900 - 7000 * math.cos(math.radians(70))), 2) == 70.75
      and round(1750 * math.sin(math.radians(70)), 1) == 1644.5))

S = "Introductory Calculus"
# ------------------------------------------------------------------ 25
topic("calc", "Differentiation & integration", S, [
    "If y = ax^n, then dy/dx = anx^{n−1}; the derivative of a constant is 0.",
    "The gradient of a curve at a point is the value of dy/dx there.",
    "Turning points: solve dy/dx = 0. If d²y/dx² > 0 it is a minimum; if < 0 it is a maximum.",
    "∫ax^n dx = ax^{n+1}/(n + 1) + c (n ≠ −1); remember + c for indefinite integrals.",
    "Area under a curve between x = a and x = b is the definite integral.",
])
O("Differentiate 3x^4 − 2x^2 + 5 with respect to x.", ["12x^3 − 4x", "12x^3 − 4x + 5", "12x^3 − 2x", "3x^3 − 4x"],
  ["d/dx(3x^4) = 12x^3;  d/dx(−2x^2) = −4x;  d/dx(5) = 0"],
  v=sp.diff(3 * x ** 4 - 2 * x ** 2 + 5, x), nv=["12*x**3-4*x", "12*x**3-4*x+5", "12*x**3-2*x", "3*x**3-4*x"])
O("Find the gradient of the curve y = x^2 − 4x + 1 at the point where x = 3.", ["2", "−2", "6", "−1"],
  [f"{F('dy','dx')} = 2x − 4", "At x = 3: 2(3) − 4 = 2"], v=float(sp.diff(x ** 2 - 4 * x + 1, x).subs(x, 3)))
O("Evaluate ∫(6x^2 + 2x) dx.", ["2x^3 + x^2 + c", "12x + 2 + c", "2x^3 + 2x^2 + c", "6x^3 + x^2 + c"],
  [f"∫6x^2 dx = {F('6x^3', 3)} = 2x^3;  ∫2x dx = x^2", "Answer: 2x^3 + x^2 + c"],
  v=sp.integrate(6 * x ** 2 + 2 * x, x), nv=["2*x**3+x**2", "12*x+2", "2*x**3+2*x**2", "6*x**3+x**2"])
O("Evaluate the definite integral of (3x^2 − 1) from x = 0 to x = 2.", ["6", "10", "8", "4"],
  ["∫(3x^2 − 1)dx = x^3 − x", "[x^3 − x] from 0 to 2 = (8 − 2) − 0 = 6"], v=float(sp.integrate(3 * x ** 2 - 1, (x, 0, 2))))
O("Find the coordinates of the turning point of y = x^2 − 6x + 5.", ["(3, −4)", "(−3, 32)", "(3, 4)", "(6, 5)"],
  [f"{F('dy','dx')} = 2x − 6 = 0 ⇒ x = 3", "y = 9 − 18 + 5 = −4 ⇒ (3, −4)"],
  ok=(sp.solve(sp.diff(x ** 2 - 6 * x + 5, x), x) == [3] and (9 - 18 + 5) == -4))
O("The distance s metres moved by a body in t seconds is s = t^3 − 3t^2 + 4. Find its velocity when t = 2 s.",
  ["0 m/s", "4 m/s", "6 m/s", "−2 m/s"],
  [f"v = {F('ds','dt')} = 3t^2 − 6t", "At t = 2: 12 − 12 = 0 m/s"],
  v=float(sp.diff(x ** 3 - 3 * x ** 2 + 4, x).subs(x, 2)), nv=[0, 4, 6, -2])
T("A curve is given by y = x^3 − 3x^2 − 9x + 5.<br>(a) Find dy/dx.<br>(b) Find the coordinates of the turning points.<br>(c) Determine the nature of each turning point.",
  ["(a) <b>dy/dx = 3x^2 − 6x − 9</b>",
   "(b) 3x^2 − 6x − 9 = 0 ⇒ 3(x^2 − 2x − 3) = 0 ⇒ (x − 3)(x + 1) = 0 ⇒ x = 3 or x = −1",
   "y(3) = 27 − 27 − 27 + 5 = −22;  y(−1) = −1 − 3 + 9 + 5 = 10",
   "Turning points: <b>(3, −22) and (−1, 10)</b>",
   "(c) d²y/dx² = 6x − 6.  At x = 3: 12 > 0 ⇒ <b>minimum</b>.  At x = −1: −12 < 0 ⇒ <b>maximum</b>"], marks=12,
  ok=(sorted(sp.solve(sp.diff(x ** 3 - 3 * x ** 2 - 9 * x + 5, x), x)) == [-1, 3]
      and [(x ** 3 - 3 * x ** 2 - 9 * x + 5).subs(x, t) for t in (3, -1)] == [-22, 10]))
T("(a) Find the equation of the tangent to the curve y = 2x^2 − 3x + 1 at the point where x = 2.<br>(b) Find the area bounded by the curve y = 4 − x^2 and the x-axis.",
  ["(a) When x = 2: y = 8 − 6 + 1 = 3, so the point is (2, 3)",
   "dy/dx = 4x − 3 ⇒ gradient at x = 2 is 5",
   "y − 3 = 5(x − 2) ⇒ <b>y = 5x − 7</b>",
   "(b) The curve cuts the x-axis where 4 − x^2 = 0 ⇒ x = −2 and x = 2",
   f"Area = ∫(4 − x^2)dx from −2 to 2 = [4x − {F('x^3',3)}]",
   f"= (8 − {F(8,3)}) − (−8 + {F(8,3)}) = 16 − {F(16,3)} = <b>{F(32,3)}</b> square units (≈ 10.67)"], marks=10,
  ok=(sp.integrate(4 - x ** 2, (x, -2, 2)) == sp.Rational(32, 3)
      and sp.diff(2 * x ** 2 - 3 * x + 1, x).subs(x, 2) == 5))

S = "Statistics & Probability"
# ------------------------------------------------------------------ 26
topic("stat", "Statistics", S, [
    "Mean = Σfx / Σf;  for grouped data use the class midpoints.",
    "Median = the middle value when the data is arranged in order (average the two middle values if n is even).",
    "Mode = the most frequent value; modal class = the class with the highest frequency.",
    "Standard deviation = √(Σf(x − x̄)² / Σf) = √(Σfx²/Σf − x̄²)",
    "Pie chart angle = (frequency ÷ total) × 360°",
])
O("Find the mean of 4, 7, 9, 10 and 15.", ["9", "10", "8", "45"],
  [f"Mean = {F('4 + 7 + 9 + 10 + 15', 5)} = {F(45,5)} = 9"], v=45 / 5)
O("Find the median of 12, 5, 8, 20, 15, 9.", ["10.5", "11.5", "10", "12"],
  ["Arrange in order: 5, 8, 9, 12, 15, 20", f"Median = {F('9 + 12', 2)} = 10.5"], v=(9 + 12) / 2)
O("The scores 1, 2, 3, 4, 5 have frequencies 3, 7, 5, 7, 2 respectively. What is the mode?",
  ["2 and 4", "4", "3", "7"], ["The highest frequency is 7, and it occurs for both 2 and 4.",
                               "The distribution is bimodal: the modes are 2 and 4."])
O("In a pie chart, 45 out of 120 students chose Science. Find the angle of that sector.", ["135°", "90°", "45°", "120°"],
  [f"Angle = {F(45,120)} × 360° = 135°"], v=45 / 120 * 360)
O("Find the standard deviation of 2, 4, 6, 8, 10, correct to two decimal places.", ["2.83", "8.00", "3.16", "2.00"],
  ["Mean = 6", f"Σ(x − x̄)^2 = 16 + 4 + 0 + 4 + 16 = 40", f"Variance = {F(40,5)} = 8 ⇒ SD = √8 = 2.83"],
  v=math.sqrt(8), tol=1e-3)
O("The mean of x, x + 2, x + 4 and x + 6 is 10. Find x.", ["7", "8", "6", "10"],
  ["Sum = 4x + 12 = 4 × 10 = 40", "4x = 28 ⇒ x = 7"], v=sp.solve(4 * x + 12 - 40, x)[0])
O("The mean of five numbers is 12. When one number is removed, the mean of the rest is 10. Find the number removed.",
  ["20", "2", "14", "22"], ["Total of the five = 60", "Total of the remaining four = 40", "Removed = 60 − 40 = 20"],
  v=5 * 12 - 4 * 10)
_f = [3, 5, 8, 12, 7, 5]
_mid = [5.5, 15.5, 25.5, 35.5, 45.5, 55.5]
T("The table shows the marks of 40 students in a test.<br>"
  "<table class=\"mt\"><tr><th>Marks</th><td>1–10</td><td>11–20</td><td>21–30</td><td>31–40</td><td>41–50</td><td>51–60</td></tr>"
  "<tr><th>Frequency</th><td>3</td><td>5</td><td>8</td><td>12</td><td>7</td><td>5</td></tr></table>"
  "(a) Calculate the mean mark.<br>(b) State the modal class.<br>(c) Calculate the median mark.<br>(d) What is the probability that a student chosen at random scored more than 40 marks?",
  ["(a) Midpoints: 5.5, 15.5, 25.5, 35.5, 45.5, 55.5",
   "Σfx = 16.5 + 77.5 + 204 + 426 + 318.5 + 277.5 = 1320",
   f"Mean = {F(1320,40)} = <b>33 marks</b>",
   "(b) The highest frequency is 12 ⇒ modal class is <b>31–40</b>",
   "(c) Cumulative frequencies: 3, 8, 16, 28, 35, 40. The 20th value lies in the class 31–40.",
   f"Median = 30.5 + ({F('20 − 16', 12)}) × 10 = 30.5 + 3.33 = <b>33.83 marks</b>",
   f"(d) Students scoring above 40 = 7 + 5 = 12 ⇒ P = {F(12,40)} = <b>{F(3,10)}</b> (0.3)"], marks=12,
  ok=(sum(_f) == 40 and close(sum(f * m for f, m in zip(_f, _mid)), 1320) and close(30.5 + 4 / 12 * 10, 33.833333, 1e-4)))
_x, _fr = [0, 1, 2, 3, 4, 5], [4, 6, 10, 8, 5, 2]
T("The table shows the number of children in 35 families.<br>"
  "<table class=\"mt\"><tr><th>Children</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>"
  "<tr><th>Families</th><td>4</td><td>6</td><td>10</td><td>8</td><td>5</td><td>2</td></tr></table>"
  "(a) Find the mean number of children, correct to two decimal places.<br>(b) Find the median and the mode.<br>(c) Find the standard deviation, correct to two decimal places.<br>(d) Find the angle that would represent families with 2 children on a pie chart.",
  ["(a) Σfx = 0 + 6 + 20 + 24 + 20 + 10 = 80",
   f"Mean = {F(80,35)} = <b>2.29 children</b>",
   "(b) The 18th value: cumulative frequencies are 4, 10, 20, … so the median is <b>2</b>. The highest frequency (10) also gives mode = <b>2</b>",
   "(c) Σfx² = 0 + 6 + 40 + 72 + 80 + 50 = 248",
   f"Variance = {F(248,35)} − (2.2857)^2 = 7.0857 − 5.2245 = 1.8612",
   "SD = √1.8612 = <b>1.36</b>",
   f"(d) Angle = {F(10,35)} × 360° = <b>102.86°</b>"], marks=12,
  ok=(sum(_fr) == 35 and sum(f * v for f, v in zip(_fr, _x)) == 80
      and sum(f * v * v for f, v in zip(_fr, _x)) == 248
      and round(math.sqrt(248 / 35 - (80 / 35) ** 2), 2) == 1.36 and round(10 / 35 * 360, 2) == 102.86))

# ------------------------------------------------------------------ 27
topic("prob", "Probability", S, [
    "P(event) = favourable outcomes ÷ total outcomes;  0 ≤ P ≤ 1",
    "P(not A) = 1 − P(A)",
    "Independent events: P(A and B) = P(A) × P(B)",
    "Mutually exclusive events: P(A or B) = P(A) + P(B)",
    "Without replacement, the second denominator drops by 1.",
])
O("A fair die is thrown once. Find the probability of obtaining a number greater than 4.", [F(1, 3), F(1, 2), F(1, 6), F(2, 3)],
  ["Favourable outcomes: 5 and 6", f"P = {F(2,6)} = {F(1,3)}"], v=Fr(1, 3), nv=[Fr(1, 3), Fr(1, 2), Fr(1, 6), Fr(2, 3)])
O("A bag contains 5 red, 3 blue and 2 green balls. One ball is picked at random. Find the probability that it is not red.",
  [F(1, 2), F(1, 5), F(3, 10), F(2, 5)],
  [f"P(red) = {F(5,10)} = {F(1,2)}", f"P(not red) = 1 − {F(1,2)} = {F(1,2)}"],
  v=Fr(1, 2), nv=[Fr(1, 2), Fr(1, 5), Fr(3, 10), Fr(2, 5)])
O("Two fair coins are tossed together. Find the probability of getting at least one head.", [F(3, 4), F(1, 2), F(1, 4), F(2, 3)],
  ["Sample space: HH, HT, TH, TT", f"At least one head: 3 outcomes ⇒ P = {F(3,4)}"],
  v=Fr(3, 4), nv=[Fr(3, 4), Fr(1, 2), Fr(1, 4), Fr(2, 3)])
O("Two fair dice are thrown together. Find the probability that the sum of the scores is 7.", [F(1, 6), F(1, 12), F(7, 36), F(5, 36)],
  ["Favourable: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) — 6 outcomes out of 36",
   f"P = {F(6,36)} = {F(1,6)}"],
  v=Fr(len([1 for i in range(1, 7) for j in range(1, 7) if i + j == 7]), 36), nv=[Fr(1, 6), Fr(1, 12), Fr(7, 36), Fr(5, 36)])
O("If P(A) = 0.4 and P(B) = 0.5 and A and B are independent, find P(A and B).", ["0.2", "0.9", "0.1", "0.45"],
  ["P(A ∩ B) = 0.4 × 0.5 = 0.2"], v=0.4 * 0.5)
O("A bag has 4 red and 6 white balls. Two balls are drawn at random without replacement. Find the probability that both are red.",
  [F(2, 15), F(4, 25), F(2, 5), F(1, 5)],
  [f"P(first red) = {F(4,10)};  P(second red) = {F(3,9)}", f"P(both) = {F(4,10)} × {F(3,9)} = {F(12,90)} = {F(2,15)}"],
  v=Fr(4, 10) * Fr(3, 9), nv=[Fr(2, 15), Fr(4, 25), Fr(2, 5), Fr(1, 5)])
T("A box contains 5 red, 4 blue and 3 white balls. Two balls are drawn one after the other without replacement.<br>(a) Find the probability that both are blue.<br>(b) Find the probability that both are of the same colour.<br>(c) Find the probability that at least one is white.",
  [f"(a) P = {F(4,12)} × {F(3,11)} = {F(12,132)} = <b>{F(1,11)}</b>",
   f"(b) P(both red) = {F(5,12)} × {F(4,11)} = {F(20,132)}; P(both blue) = {F(12,132)}; P(both white) = {F(3,12)} × {F(2,11)} = {F(6,132)}",
   f"Total = {F('20 + 12 + 6', 132)} = {F(38,132)} = <b>{F(19,66)}</b>",
   f"(c) P(no white) = {F(9,12)} × {F(8,11)} = {F(72,132)}",
   f"P(at least one white) = 1 − {F(72,132)} = {F(60,132)} = <b>{F(5,11)}</b>"], marks=12,
  ok=(Fr(4, 12) * Fr(3, 11) == Fr(1, 11)
      and Fr(5 * 4 + 4 * 3 + 3 * 2, 12 * 11) == Fr(19, 66) and 1 - Fr(9, 12) * Fr(8, 11) == Fr(5, 11)))
T(f"The probability that Kwame passes an examination is {F(2,3)} and the probability that Esi passes it is {F(3,5)}. The two events are independent.<br>(a) Find the probability that both pass.<br>(b) Find the probability that exactly one of them passes.<br>(c) Find the probability that at least one passes.<br>(d) Two fair dice are thrown. Find the probability that the product of the scores is even.",
  [f"(a) P = {F(2,3)} × {F(3,5)} = {F(6,15)} = <b>{F(2,5)}</b>",
   f"(b) Kwame only: {F(2,3)} × {F(2,5)} = {F(4,15)};  Esi only: {F(1,3)} × {F(3,5)} = {F(3,15)}",
   f"Total = {F(7,15)} ⇒ <b>{F(7,15)}</b>",
   f"(c) P(neither) = {F(1,3)} × {F(2,5)} = {F(2,15)} ⇒ P(at least one) = 1 − {F(2,15)} = <b>{F(13,15)}</b>",
   f"(d) The product is odd only when both scores are odd: {F(3,6)} × {F(3,6)} = {F(1,4)}",
   f"P(even product) = 1 − {F(1,4)} = <b>{F(3,4)}</b>"], marks=12,
  ok=(Fr(2, 3) * Fr(3, 5) == Fr(2, 5) and Fr(2, 3) * Fr(2, 5) + Fr(1, 3) * Fr(3, 5) == Fr(7, 15)
      and 1 - Fr(1, 3) * Fr(2, 5) == Fr(13, 15)
      and Fr(len([1 for i in range(1, 7) for j in range(1, 7) if i * j % 2 == 0]), 36) == Fr(3, 4)))

S = "Vectors & Transformation"
# ------------------------------------------------------------------ 28
topic("vec", "Vectors & transformations", S, [
    "Add or subtract vectors component by component;  |(x, y)| = √(x² + y²)",
    "AB = OB − OA (position vectors).",
    "Reflection: in the x-axis (x, y) → (x, −y); in the y-axis (x, y) → (−x, y); in y = x, (x, y) → (y, x).",
    "Rotation about the origin: 90° anticlockwise (x, y) → (−y, x); 180° (x, y) → (−x, −y).",
    "Translation by (a, b): (x, y) → (x + a, y + b).  Enlargement, scale factor k, centre origin: (x, y) → (kx, ky); areas scale by k².",
])
O(f"If a = {V(3,-2)} and b = {V(-1,4)}, find 2a + b.", [V(5, 0), V(5, 8), V(4, 2), V(2, 2)],
  [f"2a = {V(6,-4)}", f"2a + b = {V('6 − 1','−4 + 4')} = {V(5,0)}"],
  v=sp.Matrix([5, 0]), nv=[[[5], [0]], [[5], [8]], [[4], [2]], [[2], [2]]])
O(f"Find the magnitude of the vector {V(5,-12)}.", ["13", "17", "7", "√17"],
  ["|v| = √(5^2 + (−12)^2) = √169 = 13"], v=math.hypot(5, 12), nv=[13, 17, 7, math.sqrt(17)])
O("Find the image of the point (3, −5) after a reflection in the x-axis.", ["(3, 5)", "(−3, −5)", "(−3, 5)", "(−5, 3)"],
  ["Reflection in the x-axis: (x, y) → (x, −y)", "(3, −5) → (3, 5)"])
O("Find the image of (2, 3) after a rotation of 90° anticlockwise about the origin.", ["(−3, 2)", "(3, −2)", "(−2, −3)", "(3, 2)"],
  ["90° anticlockwise: (x, y) → (−y, x)", "(2, 3) → (−3, 2)"])
O(f"The translation vector {V(4,-1)} maps P(−2, 5) onto P′. Find P′.", ["(2, 4)", "(2, 6)", "(−6, 6)", "(6, 4)"],
  ["Add the components: (−2 + 4, 5 − 1)", "P′ = (2, 4)"])
O("Find the image of (−1, 2) under an enlargement with scale factor 3 and centre the origin.", ["(−3, 6)", "(3, 6)", "(−3, −6)", "(2, 5)"],
  ["Multiply both coordinates by 3: (−1 × 3, 2 × 3) = (−3, 6)"])
T(f"O is the origin, OA = {V(2,3)} and OB = {V(6,-1)}.<br>(a) Find AB.<br>(b) Find |AB|, correct to two decimal places.<br>(c) M is the midpoint of AB. Find OM.<br>(d) Find OC, where OC = 2OA − ½OB.",
  [f"(a) AB = OB − OA = {V('6 − 2','−1 − 3')} = <b>{V(4,-4)}</b>",
   "(b) |AB| = √(4^2 + (−4)^2) = √32 = 4√2 = <b>5.66</b>",
   f"(c) OM = OA + ½AB = {V(2,3)} + {V(2,-2)} = <b>{V(4,1)}</b>",
   f"(d) 2OA = {V(4,6)};  ½OB = {V(3,'−0.5')}", f"OC = {V('4 − 3','6 + 0.5')} = <b>{V(1,'6.5')}</b>"], marks=10,
  ok=(round(math.hypot(4, 4), 2) == 5.66 and (2 + 2, 3 - 2) == (4, 1) and (4 - 3, 6 + 0.5) == (1, 6.5)))
T("Triangle PQR has vertices P(1, 1), Q(4, 1) and R(1, 3).<br>(a) Find the images of the vertices after a reflection in the line y = x.<br>(b) Find the images after a rotation of 180° about the origin.<br>(c) Find the images after an enlargement with scale factor −2, centre the origin, and state the ratio of the area of the image to the area of triangle PQR.",
  ["(a) Reflection in y = x swaps the coordinates: <b>P′(1, 1), Q′(1, 4), R′(3, 1)</b>",
   "(b) 180° about O: (x, y) → (−x, −y) ⇒ <b>P″(−1, −1), Q″(−4, −1), R″(−1, −3)</b>",
   "(c) Multiply by −2: <b>(−2, −2), (−8, −2), (−2, −6)</b>",
   "Area of PQR = ½ × 3 × 2 = 3 square units; areas scale by k² = (−2)² = 4",
   "Image area = 12 square units ⇒ ratio <b>4 : 1</b>"], marks=12,
  ok=(abs(-2) ** 2 == 4 and .5 * 3 * 2 == 3))
