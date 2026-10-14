from core import *

S = "Algebraic Processes"

# ------------------------------------------------------------------ 13
topic("alg", "Expressions & linear equations", S, [
    "Clear fractions first: multiply every term by the LCM of the denominators.",
    "To change the subject, undo the operations in reverse order.",
    "Simultaneous equations: use elimination (match coefficients) or substitution.",
    "(a ± b)^2 = a^2 ± 2ab + b^2;  a^2 − b^2 = (a − b)(a + b)",
])
O("Factorise 6x^2 − 7x − 3.", ["(3x + 1)(2x − 3)", "(3x − 1)(2x + 3)", "(6x + 1)(x − 3)", "(2x + 1)(3x − 3)"],
  ["Product ac = 6 × (−3) = −18; find two numbers that multiply to −18 and add to −7: −9 and 2",
   "6x^2 − 9x + 2x − 3 = 3x(2x − 3) + 1(2x − 3) = (3x + 1)(2x − 3)"],
  v=6 * x ** 2 - 7 * x - 3, nv=["(3*x+1)*(2*x-3)", "(3*x-1)*(2*x+3)", "(6*x+1)*(x-3)", "(2*x+1)*(3*x-3)"])
O(f"Solve {F('2x − 1', 3)} − {F('x + 2', 4)} = 1.", [F(22, 5), "2", F(14, 5), "4"],
  ["Multiply every term by 12: 4(2x − 1) − 3(x + 2) = 12", "8x − 4 − 3x − 6 = 12",
   f"5x = 22 ⇒ x = {F(22,5)}"],
  v=sp.solve((2 * x - 1) / 3 - (x + 2) / 4 - 1, x)[0], nv=["22/5", "2", "14/5", "4"])
O(f"Make r the subject of the formula V = {F('πr^2h', 3)}.",
  [f"r = √({F('3V','πh')})", f"r = {F('3V','πh')}", f"r = √({F('V','3πh')})", f"r = √(3Vπh)"],
  ["Multiply both sides by 3: 3V = πr^2h", f"Divide by πh: r^2 = {F('3V','πh')}",
   f"Take the square root: r = √({F('3V','πh')})"],
  ok=(lambda V_, h_, r_: sp.simplify(sp.sqrt(3 * V_ / (sp.pi * h_)) - r_) == 0)(
      sp.pi * sp.Symbol('r', positive=True) ** 2 * sp.Symbol('h', positive=True) / 3,
      sp.Symbol('h', positive=True), sp.Symbol('r', positive=True)))
O("Solve simultaneously: 3x + 2y = 12 and x − y = −1.", ["x = 2, y = 3", "x = 3, y = 2", "x = 4, y = 0", "x = 1, y = 2"],
  ["From the second equation, x = y − 1", "3(y − 1) + 2y = 12 ⇒ 5y = 15 ⇒ y = 3", "x = 3 − 1 = 2"],
  ok=sp.solve([3 * x + 2 * y - 12, x - y + 1], [x, y]) == {x: 2, y: 3})
O("Expand (2a − 3b)^2.", ["4a^2 − 12ab + 9b^2", "4a^2 − 9b^2", "4a^2 + 12ab − 9b^2", "4a^2 − 6ab + 9b^2"],
  ["(2a)^2 − 2(2a)(3b) + (3b)^2", "= 4a^2 − 12ab + 9b^2"],
  v=(2 * a - 3 * b) ** 2, nv=["4*a**2-12*a*b+9*b**2", "4*a**2-9*b**2", "4*a**2+12*a*b-9*b**2", "4*a**2-6*a*b+9*b**2"])
O(f"If x = 2 and y = −3, evaluate {F('x^2 − y^2', 'x − y')}.", ["−1", "5", "1", "−5"],
  [f"{F('x^2 − y^2','x − y')} = {F('(x − y)(x + y)','x − y')} = x + y", "= 2 + (−3) = −1"],
  v=(4 - 9) / (2 + 3))
T(f"(a) Solve the simultaneous equations {F('x',2)} + {F('y',3)} = 4 and {F('x',4)} − {F('y',6)} = 0.<br>(b) A woman is four times as old as her son. In 20 years' time she will be twice as old as he will be. Find their present ages.",
  ["(a) Multiply the first equation by 6: 3x + 2y = 24 … (i)", "Multiply the second by 12: 3x − 2y = 0 … (ii)",
   "(i) + (ii): 6x = 24 ⇒ <b>x = 4</b>; then 2y = 3x = 12 ⇒ <b>y = 6</b>",
   "(b) Let the son be s years old; the woman is 4s.", "In 20 years: 4s + 20 = 2(s + 20)",
   "4s + 20 = 2s + 40 ⇒ 2s = 20 ⇒ s = 10", "<b>Son: 10 years; woman: 40 years</b>"], marks=10,
  ok=(sp.solve([x / 2 + y / 3 - 4, x / 4 - y / 6], [x, y]) == {x: 4, y: 6} and 40 + 20 == 2 * (10 + 20)))
T(f"(a) Make l the subject of the formula T = 2π√({F('l','g')}).<br>(b) Hence find l when T = 2, g = 9.8 and π = {F(22,7)}, correct to two decimal places.<br>(c) Factorise completely 3x^3 − 12x.",
  [f"(a) Divide by 2π: {F('T','2π')} = √({F('l','g')})", f"Square both sides: {F('T^2','4π^2')} = {F('l','g')}",
   f"<b>l = {F('gT^2','4π^2')}</b>",
   f"(b) l = {F('9.8 × 4', f'4 × ({F(22,7)})^2')} = {F('9.8', f'{F(484,49)}')} = {F('9.8 × 49', 484)} = 0.9921…",
   "<b>l ≈ 0.99</b>",
   "(c) Take out the common factor: 3x(x^2 − 4) = <b>3x(x − 2)(x + 2)</b>"], marks=10,
  ok=(round(9.8 * 4 / (4 * (22 / 7) ** 2), 2) == 0.99 and sp.factor(3 * x ** 3 - 12 * x) == 3 * x * (x - 2) * (x + 2)))

# ------------------------------------------------------------------ 14
topic("quad", "Quadratic equations & graphs", S, [
    "Quadratic formula: x = [−b ± √(b^2 − 4ac)] / 2a",
    "Sum of roots = −b/a;  product of roots = c/a",
    "Equation with roots α, β: x^2 − (α + β)x + αβ = 0",
    "Equal roots when b^2 − 4ac = 0.",
    "On a graph, the roots are where the curve cuts the x-axis; to solve f(x) = k, draw the line y = k.",
])
O("Solve x^2 − 5x + 6 = 0.", ["x = 2 or x = 3", "x = −2 or x = −3", "x = 1 or x = 6", "x = −1 or x = 6"],
  ["(x − 2)(x − 3) = 0", "x = 2 or x = 3"], ok=sorted(sp.solve(x ** 2 - 5 * x + 6, x)) == [2, 3])
O("Find the sum and the product of the roots of 2x^2 − 7x + 3 = 0.",
  [f"sum = {F(7,2)}, product = {F(3,2)}", f"sum = −{F(7,2)}, product = {F(3,2)}", "sum = 7, product = 3", f"sum = {F(3,2)}, product = {F(7,2)}"],
  [f"Sum = −b/a = {F(7,2)}", f"Product = c/a = {F(3,2)}"],
  ok=(lambda r: sum(r) == sp.Rational(7, 2) and r[0] * r[1] == sp.Rational(3, 2))(sp.solve(2 * x ** 2 - 7 * x + 3, x)))
O("Find the quadratic equation whose roots are −2 and 5.",
  ["x^2 − 3x − 10 = 0", "x^2 + 3x − 10 = 0", "x^2 − 3x + 10 = 0", "x^2 + 7x + 10 = 0"],
  ["(x + 2)(x − 5) = 0", "x^2 − 5x + 2x − 10 = 0 ⇒ x^2 − 3x − 10 = 0"],
  v=sp.expand((x + 2) * (x - 5)), nv=["x**2-3*x-10", "x**2+3*x-10", "x**2-3*x+10", "x**2+7*x+10"])
O("Find the values of k for which x^2 + kx + 9 = 0 has equal roots.", ["k = ±6", "k = ±3", "k = 6 only", "k = ±9"],
  ["Equal roots ⇒ b^2 − 4ac = 0", "k^2 − 36 = 0 ⇒ k = ±6"], ok=sorted(sp.solve(k ** 2 - 36, k)) == [-6, 6])
O("Solve x^2 + 4x − 1 = 0.", ["x = −2 ± √5", "x = 2 ± √5", "x = −2 ± √3", "x = −4 ± √5"],
  [f"x = {F('−4 ± √(16 + 4)', 2)} = {F('−4 ± 2√5', 2)}", "= −2 ± √5"],
  ok=set(sp.solve(x ** 2 + 4 * x - 1, x)) == {-2 + sp.sqrt(5), -2 - sp.sqrt(5)})
O("Find the minimum value of y = x^2 − 6x + 10.", ["1", "3", "10", "−1"],
  ["Complete the square: y = (x − 3)^2 − 9 + 10 = (x − 3)^2 + 1",
   "(x − 3)^2 ≥ 0, so the minimum value is 1 (when x = 3)"],
  v=min(t * t - 6 * t + 10 for t in [i / 100 for i in range(0, 700)]))
_q = lambda t: 2 * t * t - t - 6
T("(a) Copy and complete the table of values for y = 2x^2 − x − 6 for −3 ≤ x ≤ 3.<br>"
  "<table class=\"mt\"><tr><th>x</th><td>−3</td><td>−2</td><td>−1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr>"
  "<tr><th>y</th><td>15</td><td></td><td>−3</td><td></td><td></td><td>0</td><td></td></tr></table>"
  "(b) Using a scale of 2 cm to 1 unit on the x-axis and 2 cm to 5 units on the y-axis, draw the graph.<br>"
  "(c) Use your graph to find (i) the roots of 2x^2 − x − 6 = 0; (ii) the minimum value of y; (iii) the roots of 2x^2 − x − 9 = 0.",
  ["(a) y(−2) = 8 + 2 − 6 = 4; y(0) = −6; y(1) = 2 − 1 − 6 = −5; y(3) = 18 − 3 − 6 = 9",
   "<table class=\"mt\"><tr><th>x</th><td>−3</td><td>−2</td><td>−1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr>"
   "<tr><th>y</th><td>15</td><td>4</td><td>−3</td><td>−6</td><td>−5</td><td>0</td><td>9</td></tr></table>",
   "(b) Plot the points and join them with a smooth curve (see the graph).",
   "(c)(i) The curve cuts the x-axis at <b>x = −1.5 and x = 2</b>",
   "(ii) The lowest point is at x = 0.25: <b>y ≈ −6.1</b> (exactly −6.125)",
   "(iii) 2x^2 − x − 9 = 0 ⇔ 2x^2 − x − 6 = 3. Draw the line y = 3; it meets the curve at <b>x ≈ −1.9 and x ≈ 2.4</b>"],
  marks=15,
  fig=plot(_q, -3, 3, -7, 15, pts=[(t, _q(t), None) for t in range(-3, 4)], lines=[(-3, 3, 3, 3)]),
  tip="Graph readings within ±0.1 of these values are usually accepted.",
  ok=([_q(t) for t in range(-3, 4)] == [15, 4, -3, -6, -5, 0, 9] and _q(-1.5) == 0 and _q(.25) == -6.125
      and all(close(float(r), e, .06) for r, e in zip(sorted(sp.solve(2 * x ** 2 - x - 9, x)), [-1.886, 2.386]))))
T("(a) The length of a rectangular garden is 5 m more than its width. Its area is 84 m². Find (i) the dimensions of the garden; (ii) its perimeter.<br>(b) Solve 3x^2 − 4x − 2 = 0, giving your answers correct to two decimal places.",
  ["(a)(i) Let the width be x m. Then x(x + 5) = 84", "x^2 + 5x − 84 = 0 ⇒ (x + 12)(x − 7) = 0",
   "x = 7 (a width cannot be negative) ⇒ <b>width 7 m, length 12 m</b>",
   "(ii) Perimeter = 2(7 + 12) = <b>38 m</b>",
   f"(b) x = {F('4 ± √(16 + 24)', 6)} = {F('4 ± √40', 6)} = {F('4 ± 6.3246', 6)}",
   "<b>x ≈ 1.72 or x ≈ −0.39</b>"], marks=10,
  ok=(sorted(sp.solve(x ** 2 + 5 * x - 84, x)) == [-12, 7] and
      [round(float(r), 2) for r in sorted(sp.solve(3 * x ** 2 - 4 * x - 2, x))] == [-0.39, 1.72]))

# ------------------------------------------------------------------ 15
topic("ineq", "Inequalities & linear programming", S, [
    "Multiplying or dividing an inequality by a negative number reverses the sign.",
    "Quadratic inequality (x − p)(x − q) < 0 with p < q: the solution is p < x < q.",
    "Linear programming: shade the unwanted region, find the corners of the feasible region, and test the objective function at each corner.",
])
O("Solve the inequality 3 − 2x < 7.", ["x > −2", "x < −2", "x > 2", "x < 2"],
  ["−2x < 4", "Divide by −2 and reverse the sign: x > −2"],
  ok=all((3 - 2 * t < 7) == (t > -2) for t in [i / 4 for i in range(-40, 40)]))
O("Solve −1 ≤ 2x + 3 < 9.", ["−2 ≤ x < 3", "−2 < x ≤ 3", "1 ≤ x < 6", "−4 ≤ x < 6"],
  ["Subtract 3 throughout: −4 ≤ 2x < 6", "Divide by 2: −2 ≤ x < 3"],
  ok=all((-1 <= 2 * t + 3 < 9) == (-2 <= t < 3) for t in [i / 4 for i in range(-40, 40)]))
O("Find the integer values of x that satisfy −2 < x − 1 ≤ 2.", ["0, 1, 2, 3", "−1, 0, 1, 2", "−1, 0, 1, 2, 3", "0, 1, 2"],
  ["Add 1 throughout: −1 < x ≤ 3", "Integers: 0, 1, 2, 3"],
  ok=[t for t in range(-10, 10) if -2 < t - 1 <= 2] == [0, 1, 2, 3])
O("Solve x^2 − x − 6 < 0.", ["−2 < x < 3", "x < −2 or x > 3", "−3 < x < 2", "x < −3 or x > 2"],
  ["(x − 3)(x + 2) < 0", "The product is negative between the roots: −2 < x < 3"],
  ok=all((t * t - t - 6 < 0) == (-2 < t < 3) for t in [i / 4 for i in range(-40, 40)]))
O("Which of these points lies in the region defined by y ≥ 2x − 1 and x + y ≤ 4?", ["(1, 2)", "(3, 2)", "(2, 3)", "(0, −2)"],
  ["(1, 2): 2 ≥ 1 ✓ and 3 ≤ 4 ✓", "(3, 2): 2 ≥ 5 ✗", "(2, 3): 3 ≥ 3 ✓ but 5 ≤ 4 ✗", "(0, −2): −2 ≥ −1 ✗"],
  ok=[p for p in [(1, 2), (3, 2), (2, 3), (0, -2)] if p[1] >= 2 * p[0] - 1 and p[0] + p[1] <= 4] == [(1, 2)])
_lp = [(px, py, 20 * px + 35 * py) for px in range(0, 20) for py in range(0, 20) if 2 * px + 3 * py <= 30 and px >= 3 and py <= 6]
T(f"(a) Solve {F('x − 1', 3)} − {F('x + 1', 2)} ≥ −1.<br>(b) A tailor makes x shirts and y pairs of trousers. A shirt uses 2 m of cloth and a pair of trousers uses 3 m. He has 30 m of cloth. He must make at least 3 shirts and not more than 6 pairs of trousers.<br>(i) Write down the inequalities.<br>(ii) Given a profit of GH₵ 20 on a shirt and GH₵ 35 on a pair of trousers, find the number of each he should make for maximum profit, and the maximum profit.",
  ["(a) Multiply by 6: 2(x − 1) − 3(x + 1) ≥ −6", "2x − 2 − 3x − 3 ≥ −6 ⇒ −x ≥ −1 ⇒ <b>x ≤ 1</b>",
   "(b)(i) <b>2x + 3y ≤ 30,  x ≥ 3,  y ≤ 6,  y ≥ 0</b>",
   "(ii) Corners of the feasible region: (3, 0), (15, 0), (6, 6), (3, 6)",
   "P = 20x + 35y: P(3, 0) = 60;  P(15, 0) = 300;  P(6, 6) = 330;  P(3, 6) = 270",
   "Maximum: <b>6 shirts and 6 pairs of trousers, profit GH₵ 330</b>"], marks=14,
  fig=plot(None, 0, 16, 0, 11, step=2, shade=[(3, 0), (15, 0), (6, 6), (3, 6)],
           lines=[(0, 10, 15, 0), (3, 0, 3, 11), (0, 6, 16, 6)], pts=[(6, 6, "(6, 6)")]),
  ok=(max(_lp, key=lambda t: t[2]) == (6, 6, 330)
      and all(((t - 1) / 3 - (t + 1) / 2 >= -1) == (t <= 1) for t in [i / 4 for i in range(-40, 40)])))
T("(a) On the same axes, draw the lines y = x + 2 and x + y = 6 for 0 ≤ x ≤ 6.<br>(b) Shade the region satisfying y ≤ x + 2, x + y ≤ 6, x ≥ 0 and y ≥ 0.<br>(c) Find the maximum value of 3x + 2y in the region.",
  ["(a) y = x + 2 passes through (0, 2) and (4, 6); x + y = 6 passes through (0, 6) and (6, 0).",
   "(b) The region is the quadrilateral with corners (0, 0), (6, 0), (2, 4) and (0, 2).",
   "The lines meet where x + 2 = 6 − x ⇒ x = 2, y = 4",
   "(c) 3x + 2y: (0, 0) → 0;  (6, 0) → 18;  (2, 4) → 14;  (0, 2) → 4",
   "<b>Maximum = 18 at (6, 0)</b>"], marks=10,
  fig=plot(None, 0, 7, 0, 7, shade=[(0, 0), (6, 0), (2, 4), (0, 2)], lines=[(0, 2, 5, 7), (0, 6, 6, 0)],
           pts=[(2, 4, "(2, 4)")]),
  ok=max(3 * p + 2 * q for p in range(0, 7) for q in range(0, 7) if q <= p + 2 and p + q <= 6) == 18)

# ------------------------------------------------------------------ 16
topic("afunc", "Algebraic fractions & functions", S, [
    "Factorise fully before cancelling — cancel factors, never terms.",
    "An algebraic fraction is undefined when its denominator equals zero.",
    "Composite: f(g(x)) — apply g first, then f.",
    "Inverse: write y = f(x), swap x and y, then make y the subject.",
])
O(f"Simplify {F('x^2 − 9', 'x^2 + x − 6')}.", [F("x − 3", "x − 2"), F("x + 3", "x − 2"), F("x − 3", "x + 2"), F(3, 2)],
  [f"{F('(x − 3)(x + 3)', '(x + 3)(x − 2)')} = {F('x − 3','x − 2')}"],
  v=(x ** 2 - 9) / (x ** 2 + x - 6), nv=["(x-3)/(x-2)", "(x+3)/(x-2)", "(x-3)/(x+2)", "3/2"])
O(f"Simplify {F(2,'x − 1')} − {F(1,'x + 1')}.", [F("x + 3", "x^2 − 1"), F(1, "x^2 − 1"), F("x + 1", "x^2 − 1"), F("3x + 1", "x^2 − 1")],
  [f"LCM = (x − 1)(x + 1)", f"{F('2(x + 1) − (x − 1)', '(x − 1)(x + 1)')} = {F('x + 3', 'x^2 − 1')}"],
  v=2 / (x - 1) - 1 / (x + 1), nv=["(x+3)/(x**2-1)", "1/(x**2-1)", "(x+1)/(x**2-1)", "(3*x+1)/(x**2-1)"])
O(f"For what value of x is {F('x + 2', 'x^2 − 4x + 4')} undefined?", ["2", "−2", "4", "0"],
  ["x^2 − 4x + 4 = (x − 2)^2 = 0 ⇒ x = 2"], v=sp.solve(x ** 2 - 4 * x + 4, x)[0])
O("If f(x) = 3x^2 − 2x + 1, find f(−2).", ["17", "9", "7", "−15"],
  ["f(−2) = 3(4) − 2(−2) + 1 = 12 + 4 + 1 = 17"], v=3 * 4 + 4 + 1)
O(f"If g(x) = {F('x + 3', 2)}, find g^{{-1}}(x).", ["2x − 3", "2x + 3", F("x − 3", 2), F(2, "x + 3")],
  [f"y = {F('x + 3', 2)} ⇒ swap: x = {F('y + 3', 2)}", "2x = y + 3 ⇒ y = 2x − 3"],
  v=sp.solve(sp.Eq(x, (y + 3) / 2), y)[0], nv=["2*x-3", "2*x+3", "(x-3)/2", "2/(x+3)"])
O("f(x) = 2x + 1 and g(x) = x^2. Find f(g(3)).", ["19", "49", "13", "36"],
  ["g(3) = 9", "f(9) = 2(9) + 1 = 19"], v=2 * 3 ** 2 + 1, tip="g(f(3)) = 49 is a different question — the order matters.")
T(f"(a) Simplify {F('x^2 − 5x + 6', 'x^2 − 4')} ÷ {F('x − 3', 'x^2 + 2x')}.<br>(b) Solve {F(3,'x − 1')} − {F(2,'x + 1')} = 1.",
  [f"(a) = {F('(x − 2)(x − 3)', '(x − 2)(x + 2)')} × {F('x(x + 2)', 'x − 3')}", "= <b>x</b>",
   "(b) Multiply by (x − 1)(x + 1): 3(x + 1) − 2(x − 1) = x^2 − 1",
   "x + 5 = x^2 − 1 ⇒ x^2 − x − 6 = 0 ⇒ (x − 3)(x + 2) = 0",
   "<b>x = 3 or x = −2</b> (neither makes a denominator zero)"], marks=10,
  ok=(sp.simplify((x ** 2 - 5 * x + 6) / (x ** 2 - 4) / ((x - 3) / (x ** 2 + 2 * x)) - x) == 0
      and sorted(sp.solve(3 / (x - 1) - 2 / (x + 1) - 1, x)) == [-2, 3]))
T(f"f : x → 2x − 3 and g : x → {F('x + 1','x')}, x ≠ 0.<br>(a) Find f(g(2)).<br>(b) Find f^{{-1}}(x).<br>(c) Find the value of x for which f(x) = f^{{-1}}(x).",
  [f"(a) g(2) = {F(3,2)};  f({F(3,2)}) = 3 − 3 = <b>0</b>",
   f"(b) y = 2x − 3 ⇒ swap: x = 2y − 3 ⇒ <b>f^{{-1}}(x) = {F('x + 3', 2)}</b>",
   f"(c) 2x − 3 = {F('x + 3', 2)} ⇒ 4x − 6 = x + 3 ⇒ 3x = 9 ⇒ <b>x = 3</b>"], marks=9,
  ok=(2 * Fr(3, 2) - 3 == 0 and sp.solve(2 * x - 3 - (x + 3) / 2, x) == [3]))

S = "Mensuration"
# ------------------------------------------------------------------ 17
topic("area", "Lengths, perimeters & areas", S, [
    "Arc length = (θ/360) × 2πr;  sector area = (θ/360) × πr^2",
    "Triangle: ½ab sin C, or Heron's formula √[s(s − a)(s − b)(s − c)]",
    "Trapezium = ½(a + b)h;  parallelogram = base × height",
    "Segment = sector − triangle.",
    "Perimeter of a sector = arc + 2r.",
])
PI = Fr(22, 7)
O(f"Find the area of a sector of a circle of radius 7 cm that subtends an angle of 72° at the centre. [π = {F(22,7)}]",
  ["30.8 cm²", "8.8 cm²", "61.6 cm²", "154 cm²"],
  [f"Area = {F(72,360)} × {F(22,7)} × 7^2", "= 0.2 × 154 = 30.8 cm²"], v=float(Fr(72, 360) * PI * 49))
O(f"Find the length of an arc that subtends 45° at the centre of a circle of radius 14 cm. [π = {F(22,7)}]",
  ["11 cm", "22 cm", "77 cm", "5.5 cm"],
  [f"Arc = {F(45,360)} × 2 × {F(22,7)} × 14 = {F(1,8)} × 88 = 11 cm"], v=float(Fr(45, 360) * 2 * PI * 14))
O("A trapezium has parallel sides of 8 cm and 12 cm, and a height of 5 cm. Find its area.", ["50 cm²", "100 cm²", "60 cm²", "40 cm²"],
  ["Area = ½(8 + 12) × 5 = 50 cm²"], v=.5 * 20 * 5)
O("A rectangle has a perimeter of 34 cm and a length of 12 cm. Find its area.", ["60 cm²", "204 cm²", "70 cm²", "144 cm²"],
  ["2(12 + w) = 34 ⇒ w = 5 cm", "Area = 12 × 5 = 60 cm²"], v=12 * (34 / 2 - 12))
O("Find the area of a triangle with sides 13 cm, 14 cm and 15 cm.", ["84 cm²", "42 cm²", "105 cm²", "168 cm²"],
  ["s = (13 + 14 + 15)/2 = 21", "Area = √[21 × 8 × 7 × 6] = √7056 = 84 cm²"], v=math.sqrt(21 * 8 * 7 * 6))
O(f"Find the perimeter of a sector of radius 10.5 cm and angle 120°. [π = {F(22,7)}]", ["43 cm", "22 cm", "32.5 cm", "64 cm"],
  [f"Arc = {F(120,360)} × 2 × {F(22,7)} × 10.5 = 22 cm", "Perimeter = 22 + 2(10.5) = 43 cm"],
  v=float(Fr(1, 3) * 2 * PI * Fr(21, 2) + 21))
T("A chord AB of a circle with centre O and radius 10 cm subtends an angle of 60° at O. [Take π = 3.142]<br>(a) Find the length of AB.<br>(b) Find the area of the minor segment.<br>(c) Find the perimeter of the minor segment.",
  ["(a) OA = OB = 10 cm and ∠AOB = 60°, so triangle AOB is equilateral ⇒ <b>AB = 10 cm</b>",
   f"(b) Sector = {F(60,360)} × 3.142 × 100 = 52.367 cm²",
   "Triangle = ½ × 10 × 10 × sin 60° = 43.301 cm²",
   "Segment = 52.367 − 43.301 = <b>9.07 cm²</b>",
   f"(c) Arc AB = {F(60,360)} × 2 × 3.142 × 10 = 10.473 cm",
   "Perimeter = 10.473 + 10 = <b>20.47 cm</b>"], marks=10,
  ok=(round(3.142 * 100 / 6 - 50 * math.sin(math.radians(60)), 2) == 9.07 and round(2 * 3.142 * 10 / 6 + 10, 2) == 20.47))
T(f"A rectangular lawn measures 20 m by 15 m. A path 2 m wide runs round the outside of the lawn.<br>(a) Find the area of the path.<br>(b) Find the cost of paving the path at GH₵ 45 per square metre.<br>(c) A circular pond of diameter 7 m is dug in the lawn. Find the area of lawn that remains. [π = {F(22,7)}]",
  ["(a) Outer rectangle = (20 + 4) × (15 + 4) = 24 × 19 = 456 m²", "Path = 456 − 300 = <b>156 m²</b>",
   "(b) Cost = 156 × 45 = <b>GH₵ 7,020</b>",
   f"(c) Pond = {F(22,7)} × 3.5^2 = 38.5 m²", "Remaining lawn = 300 − 38.5 = <b>261.5 m²</b>"], marks=10,
  ok=(24 * 19 - 300 == 156 and 156 * 45 == 7020 and float(300 - PI * Fr(7, 2) ** 2) == 261.5))

# ------------------------------------------------------------------ 18
topic("vol", "Volumes & surface areas", S, [
    "Cylinder: V = πr^2h;  curved surface area = 2πrh;  total = 2πr(r + h)",
    "Cone: V = ⅓πr^2h;  curved surface area = πrl, where l^2 = r^2 + h^2",
    "Sphere: V = 4/3 πr^3;  surface area = 4πr^2 (a hemisphere's curved surface is 2πr^2)",
    "Prism: V = cross-section area × length;  pyramid: V = ⅓ × base area × height",
    "1 m³ = 1000 litres;  1 litre = 1000 cm³",
])
O(f"Find the volume of a cylinder of radius 7 cm and height 10 cm. [π = {F(22,7)}]", ["1540 cm³", "440 cm³", "3080 cm³", "4620 cm³"],
  [f"V = {F(22,7)} × 49 × 10 = 1540 cm³"], v=float(PI * 49 * 10))
O(f"Find the volume of a cone of base radius 3 cm and height 7 cm. [π = {F(22,7)}]", ["66 cm³", "198 cm³", "22 cm³", "132 cm³"],
  [f"V = {F(1,3)} × {F(22,7)} × 9 × 7 = 66 cm³"], v=float(Fr(1, 3) * PI * 9 * 7))
O(f"Find the total surface area of a closed cylinder of radius 7 cm and height 5 cm. [π = {F(22,7)}]",
  ["528 cm²", "374 cm²", "220 cm²", "308 cm²"],
  [f"Total surface area = 2πr(r + h) = 2 × {F(22,7)} × 7 × 12 = 528 cm²"], v=float(2 * PI * 7 * 12))
O("Find the volume of a sphere of radius 3 cm, in terms of π.", ["36π cm³", "12π cm³", "108π cm³", "27π cm³"],
  [f"V = {F(4,3)}π(3)^3 = {F(4,3)} × 27π = 36π cm³"],
  v=sp.Rational(4, 3) * sp.pi * 27, nv=["36*pi", "12*pi", "108*pi", "27*pi"])
O("A cube has a total surface area of 150 cm². Find its volume.", ["125 cm³", "25 cm³", "216 cm³", "150 cm³"],
  ["6s^2 = 150 ⇒ s^2 = 25 ⇒ s = 5 cm", "V = 5^3 = 125 cm³"], v=(150 / 6) ** 1.5)
O("Find the curved surface area of a cone with base radius 6 cm and slant height 10 cm, in terms of π.",
  ["60π cm²", "96π cm²", "36π cm²", "120π cm²"],
  ["Curved surface area = πrl = π × 6 × 10 = 60π cm²"], v=60 * sp.pi, nv=["60*pi", "96*pi", "36*pi", "120*pi"],
  tip="96π is the TOTAL surface area (it adds the base, 36π). Read the question carefully.")
T("A solid is made of a cone of height 8 cm standing on a cylinder of height 10 cm. Both have a radius of 6 cm. [π = 3.142]<br>(a) Find the slant height of the cone.<br>(b) Find the total surface area of the solid.<br>(c) Find the volume of the solid.",
  ["(a) l = √(6^2 + 8^2) = √100 = <b>10 cm</b>",
   "(b) Surface = cone curved + cylinder curved + base = π(6)(10) + 2π(6)(10) + π(6)^2",
   "= 60π + 120π + 36π = 216π = 216 × 3.142 = <b>678.67 cm²</b>",
   f"(c) V = {F(1,3)}π(36)(8) + π(36)(10) = 96π + 360π = 456π",
   "= 456 × 3.142 = <b>1432.75 cm³</b>"], marks=12,
  ok=(math.hypot(6, 8) == 10 and round(216 * 3.142, 2) == 678.67 and round(456 * 3.142, 2) == 1432.75))
T(f"An open rectangular tank measures 2 m by 1.5 m by 1.2 m.<br>(a) Find its capacity in litres.<br>(b) The full tank is emptied into cylindrical drums of radius 0.35 m and height 0.9 m. How many drums can be filled completely, and how many litres are left over? [π = {F(22,7)}]<br>(c) Find the area of metal sheet used to make the tank.",
  ["(a) V = 2 × 1.5 × 1.2 = 3.6 m³ = <b>3600 litres</b>",
   f"(b) Drum = {F(22,7)} × 0.35^2 × 0.9 = 0.3465 m³ = 346.5 litres",
   f"{F(3600,'346.5')} = 10.39… ⇒ <b>10 full drums</b>",
   "Left over = 3600 − 10 × 346.5 = <b>135 litres</b>",
   "(c) Base = 2 × 1.5 = 3 m²; sides = 2(2 × 1.2) + 2(1.5 × 1.2) = 4.8 + 3.6 = 8.4 m²",
   "Total (open top) = <b>11.4 m²</b>"], marks=12,
  ok=(close(2 * 1.5 * 1.2, 3.6) and float(PI * Fr(35, 100) ** 2 * Fr(9, 10)) == 0.3465
      and int(3.6 / 0.3465) == 10 and close(3600 - 3465, 135) and close(3 + 8.4, 11.4)))

S = "Plane Geometry"
# ------------------------------------------------------------------ 19
topic("geo", "Angles, triangles & polygons", S, [
    "Sum of interior angles of an n-sided polygon = (n − 2) × 180°",
    "Exterior angles of any polygon add up to 360°; for a regular polygon, each = 360°/n",
    "Alternate angles are equal; corresponding angles are equal; co-interior angles add up to 180°",
    "Similar triangles: the ratio of areas = (ratio of sides)^2",
    "Pythagoras: c^2 = a^2 + b^2 (right-angled triangles only)",
])
O("Find the size of each interior angle of a regular hexagon.", ["120°", "108°", "135°", "60°"],
  ["Sum = (6 − 2) × 180° = 720°", "Each = 720° ÷ 6 = 120°"], v=(6 - 2) * 180 / 6)
O("Find the sum of the interior angles of a nonagon (9 sides).", ["1260°", "1440°", "1080°", "1620°"],
  ["(9 − 2) × 180° = 1260°"], v=7 * 180)
O("Each exterior angle of a regular polygon is 24°. How many sides does it have?", ["15", "12", "18", "24"],
  ["n = 360° ÷ 24° = 15"], v=360 / 24)
O("The angles of triangle PQR are P = 2x°, Q = (3x + 10)° and R = (x + 20)°. Find x.", ["25", "30", "20", "35"],
  ["2x + 3x + 10 + x + 20 = 180", "6x + 30 = 180 ⇒ x = 25"], v=sp.solve(6 * x + 30 - 180, x)[0])
O("A transversal cuts two parallel lines. A pair of alternate angles are (3y − 15)° and (2y + 20)°. Find y.", ["35", "5", "39", "25"],
  ["Alternate angles are equal: 3y − 15 = 2y + 20", "y = 35"], v=sp.solve(3 * y - 15 - (2 * y + 20), y)[0])
O("The vertical angle of an isosceles triangle is 40°. Find each base angle.", ["70°", "40°", "140°", "50°"],
  ["Base angles are equal: 2b + 40 = 180", "b = 70°"], v=(180 - 40) / 2)
T("(a) The interior angles of a pentagon are x°, 2x°, (x + 30)°, 110° and 130°. Find x and the size of the largest angle.<br>(b) Each interior angle of a regular polygon is four times its exterior angle. Find the number of sides.<br>(c) A 13 m ladder leans against a vertical wall with its foot 5 m from the wall. How high up the wall does it reach?",
  ["(a) Sum of the angles of a pentagon = 540°", "x + 2x + x + 30 + 110 + 130 = 540 ⇒ 4x = 270 ⇒ <b>x = 67.5</b>",
   "The angles are 67.5°, 135°, 97.5°, 110° and 130° ⇒ the largest is <b>135°</b>",
   "(b) Interior + exterior = 180° ⇒ 4e + e = 180 ⇒ e = 36°", "n = 360 ÷ 36 = <b>10 sides</b> (a decagon)",
   "(c) h = √(13^2 − 5^2) = √144 = <b>12 m</b>"], marks=10,
  ok=(4 * 67.5 + 270 == 540 and max(67.5, 135, 97.5, 110, 130) == 135 and 360 / 36 == 10 and math.sqrt(169 - 25) == 12))
T("In triangle ABC, D is on AB and E is on AC such that DE ∥ BC. AD = 4 cm, DB = 6 cm and DE = 5 cm.<br>(a) Find BC.<br>(b) If AE = 3 cm, find EC.<br>(c) Find the ratio of the area of triangle ADE to the area of triangle ABC.",
  [f"(a) Triangles ADE and ABC are similar (DE ∥ BC). AB = 10 cm", f"{F('AD','AB')} = {F('DE','BC')} ⇒ {F(4,10)} = {F(5,'BC')} ⇒ <b>BC = 12.5 cm</b>",
   f"(b) {F('AD','DB')} = {F('AE','EC')} ⇒ {F(4,6)} = {F(3,'EC')} ⇒ <b>EC = 4.5 cm</b>",
   f"(c) Area ratio = ({F(4,10)})^2 = <b>4 : 25</b>"], marks=9,
  ok=(Fr(4, 10) == Fr(5, 1) / Fr(25, 2) and Fr(4, 6) == Fr(3, 1) / Fr(9, 2) and Fr(4, 10) ** 2 == Fr(4, 25)))

# ------------------------------------------------------------------ 20
topic("circle", "Circle theorems", S, [
    "The angle at the centre is twice the angle at the circumference standing on the same arc.",
    "Angles in the same segment are equal; the angle in a semicircle is 90°.",
    "Opposite angles of a cyclic quadrilateral add up to 180°.",
    "A tangent is perpendicular to the radius at the point of contact; tangents from an external point are equal.",
    "Alternate segment theorem: the angle between a tangent and a chord equals the angle in the alternate segment.",
    "Intersecting chords: AX × XB = CX × XD",
])
O("An arc subtends an angle of 130° at the centre of a circle. What angle does it subtend at a point on the remaining part of the circumference?",
  ["65°", "130°", "50°", "260°"], ["The angle at the circumference is half the angle at the centre: 130° ÷ 2 = 65°"], v=130 / 2)
O("One angle of a cyclic quadrilateral is 72°. Find the angle opposite to it.", ["108°", "72°", "18°", "288°"],
  ["Opposite angles add up to 180°: 180° − 72° = 108°"], v=180 - 72)
O("AB is a diameter of a circle and C is a point on the circle. If ∠CAB = 35°, find ∠ABC.", ["55°", "35°", "45°", "145°"],
  ["∠ACB = 90° (angle in a semicircle)", "∠ABC = 180° − 90° − 35° = 55°"], v=180 - 90 - 35)
O("PT is a tangent from P to a circle with centre O, touching it at T. If OP = 13 cm and the radius is 5 cm, find PT.",
  ["12 cm", "8 cm", "18 cm", "√194 cm"],
  ["OT ⊥ PT (radius ⊥ tangent)", "PT = √(13^2 − 5^2) = √144 = 12 cm"],
  v=12, nv=[12, 8, 18, math.sqrt(194)]) if math.sqrt(169 - 25) == 12 else FAIL()
O("The tangent to a circle at A makes an angle of 58° with the chord AB. Find the angle ACB, where C is a point on the circle in the alternate segment.",
  ["58°", "32°", "116°", "122°"], ["By the alternate segment theorem, ∠ACB = 58°"])
O("Chords AB and CD of a circle intersect at X inside the circle. AX = 4 cm, XB = 6 cm and CX = 3 cm. Find XD.", ["8 cm", "4.5 cm", "2 cm", "7 cm"],
  ["AX × XB = CX × XD", "4 × 6 = 3 × XD ⇒ XD = 8 cm"], v=4 * 6 / 3)
T("ABCD is a cyclic quadrilateral with ∠BAD = 3x° and ∠BCD = (2x + 30)°.<br>(a) Find x.<br>(b) What does your answer tell you about BD?<br>(c) If ∠ABD = 35°, find ∠ACD and ∠ADB.",
  ["(a) Opposite angles are supplementary: 3x + 2x + 30 = 180 ⇒ 5x = 150 ⇒ <b>x = 30</b>",
   "(b) ∠BAD = 90°, so BD subtends a right angle at A ⇒ <b>BD is a diameter</b>",
   "(c) ∠ACD and ∠ABD stand on the same arc AD ⇒ <b>∠ACD = 35°</b>",
   "In triangle ABD: ∠ADB = 180° − 90° − 35° = <b>55°</b>"], marks=10,
  ok=(sp.solve(5 * x + 30 - 180, x) == [30] and 180 - 90 - 35 == 55))
T("TA and TB are tangents from T to a circle with centre O, touching it at A and B. ∠ATB = 50°. C is a point on the major arc AB.<br>(a) Find ∠AOB.<br>(b) Find ∠ACB.<br>(c) Find ∠TAB.<br>(d) If OA = 6 cm, find TA correct to two decimal places.",
  ["(a) ∠OAT = ∠OBT = 90° (radius ⊥ tangent). In quadrilateral OATB: ∠AOB = 360 − 90 − 90 − 50 = <b>130°</b>",
   "(b) ∠ACB = ½ ∠AOB = <b>65°</b>",
   "(c) TA = TB, so triangle TAB is isosceles: ∠TAB = (180 − 50) ÷ 2 = <b>65°</b>",
   "(d) OT bisects ∠ATB, so ∠ATO = 25°. In right-angled triangle OAT: tan 25° = OA/TA",
   f"TA = {F(6,'tan 25°')} = {F(6,'0.4663')} = <b>12.87 cm</b>"], marks=12,
  tip="Part (c) also follows from the alternate segment theorem: ∠TAB = ∠ACB = 65°.",
  ok=(360 - 90 - 90 - 50 == 130 and round(6 / math.tan(math.radians(25)), 2) == 12.87))

# ------------------------------------------------------------------ 21
topic("loci", "Constructions & loci", S, [
    "Points equidistant from two points lie on the perpendicular bisector of the line joining them.",
    "Points equidistant from two intersecting lines lie on the bisectors of the angles between them.",
    "Points at a fixed distance from a point form a circle; points at a fixed distance from a line form a pair of parallel lines.",
    "With a ruler and compasses, construct 60° (equilateral arc), then bisect to get 30° and 15°; 90° bisects to 45°. Combine these: 75° = 60° + 15°, 105° = 90° + 15°.",
])
O("What is the locus of points equidistant from two fixed points A and B?",
  ["The perpendicular bisector of AB", "A circle with diameter AB", "A line parallel to AB", "The line AB"],
  ["Every point on the perpendicular bisector of AB is the same distance from A and from B."])
O("What is the locus of a point P that moves so that it is always 3 cm from a fixed point O?",
  ["A circle with centre O and radius 3 cm", "A straight line 3 cm from O", "A circle with diameter 3 cm", "Two parallel lines 3 cm apart"],
  ["All points a fixed distance from O form a circle with centre O and that radius."])
O("What is the locus of points equidistant from two intersecting straight lines?",
  ["The bisectors of the angles between the lines", "A circle through the point of intersection", "A line parallel to both lines", "The perpendicular bisector of one line"],
  ["Points on an angle bisector are the same distance from both arms of the angle."])
O("Which of these angles CANNOT be constructed using only a ruler and a pair of compasses by the usual methods?", ["50°", "75°", "105°", "22.5°"],
  ["75° = 60° + 15°; 105° = 90° + 15°; 22.5° = ½ of 45°", "50° cannot be built from 60° and 90° by bisecting and adding."])
O("In constructing an angle of 60° with a ruler and compasses, which figure is effectively being drawn?",
  ["An equilateral triangle", "A right-angled triangle", "A square", "A regular hexagon's diagonal"],
  ["Arcs of equal radius from each end produce three equal sides, so every angle is 60°."])
T("(a) Using a ruler and a pair of compasses only, construct triangle PQR with PQ = 7 cm, ∠PQR = 60° and QR = 5 cm. Measure PR.<br>(b) Construct the locus of points equidistant from P and Q, and the locus of points equidistant from Q and R. Label their intersection O and measure OP.",
  ["(a) Draw PQ = 7 cm. At Q, construct 60°: with centre Q draw an arc cutting QP, and with the same radius, centre at that point, cut the arc again. Join Q through this point.",
   "Mark R on this arm with QR = 5 cm, and join PR.",
   f"Check by the cosine rule: PR^2 = 49 + 25 − 2(7)(5)cos 60° = 39 ⇒ <b>PR ≈ 6.2 cm</b>",
   "(b) Construct the perpendicular bisectors of PQ and QR; they meet at O (the circumcentre).",
   f"OP = circumradius = {F('PR', '2 sin Q')} = {F('6.245', '1.732')} ⇒ <b>OP ≈ 3.6 cm</b>",
   "O is equidistant from P, Q and R, so a circle with centre O through P also passes through Q and R."], marks=12,
  tip="Always leave your construction arcs visible — examiners award marks for them.",
  ok=(close(math.sqrt(49 + 25 - 35), 6.245, 1e-3) and round(math.sqrt(39) / (2 * math.sin(math.radians(60))), 1) == 3.6))
T(f"A goat is tied by a 5 m rope to a post at one corner of a rectangular field measuring 12 m by 8 m.<br>(a) Describe the locus of the furthest points the goat can reach.<br>(b) Find the area of the field the goat can graze. [π = {F(22,7)}]<br>(c) Find the area of the field it cannot reach.",
  ["(a) An arc of a circle with centre at the post and radius 5 m — a quarter circle, because the corner angle is 90°.",
   f"(b) Area = {F(1,4)} × {F(22,7)} × 5^2 = {F(550,28)} = <b>19.64 m²</b>",
   "(c) Field = 12 × 8 = 96 m²; unreachable = 96 − 19.64 = <b>76.36 m²</b>"], marks=8,
  ok=(round(float(Fr(1, 4) * PI * 25), 2) == 19.64 and round(96 - float(Fr(1, 4) * PI * 25), 2) == 76.36))

S = "Coordinate Geometry"
# ------------------------------------------------------------------ 22
topic("coord", "Straight lines", S, [
    "Gradient m = (y_2 − y_1)/(x_2 − x_1);  distance = √[(x_2 − x_1)^2 + (y_2 − y_1)^2]",
    "Midpoint = ((x_1 + x_2)/2, (y_1 + y_2)/2)",
    "Line: y − y_1 = m(x − x_1), or y = mx + c",
    "Parallel lines: m_1 = m_2.  Perpendicular lines: m_1 × m_2 = −1",
])
O("Find the gradient of the line joining (2, −3) and (6, 5).", ["2", F(1, 2), "−2", "4"],
  [f"m = {F('5 − (−3)', '6 − 2')} = {F(8,4)} = 2"], v=Fr(8, 4), nv=[2, Fr(1, 2), -2, 4])
O("Find the distance between the points (−1, 2) and (5, 10).", ["10 units", "14 units", "8 units", "√28 units"],
  ["d = √(6^2 + 8^2) = √100 = 10"], v=math.hypot(6, 8), nv=[10, 14, 8, math.sqrt(28)])
O("Find the midpoint of the line joining (4, −2) and (−6, 8).", ["(−1, 3)", "(1, 3)", "(−1, 5)", "(−5, 5)"],
  [f"({F('4 + (−6)',2)}, {F('−2 + 8',2)}) = (−1, 3)"], ok=((4 - 6) / 2, (-2 + 8) / 2) == (-1, 3))
O("Find the equation of the line with gradient 3 passing through (1, 4).", ["y = 3x + 1", "y = 3x + 4", "y = 3x − 1", "y = x + 3"],
  ["y − 4 = 3(x − 1)", "y = 3x + 1"], v=3 * (x - 1) + 4, nv=["3*x+1", "3*x+4", "3*x-1", "x+3"])
O("The lines 2y = 3x + 5 and ky + 2x = 7 are perpendicular. Find k.", ["3", "−3", F(4, 3), f"−{F(4,3)}"],
  [f"The gradients are {F(3,2)} and −{F(2,'k')}", f"{F(3,2)} × (−{F(2,'k')}) = −1 ⇒ {F(3,'k')} = 1 ⇒ k = 3"],
  v=sp.solve(sp.Rational(3, 2) * (-2 / k) + 1, k)[0], nv=["3", "-3", "4/3", "-4/3"])
O("Find the x-intercept of the line 3x − 4y = 12.", ["4", "−3", "3", "12"],
  ["At the x-axis, y = 0: 3x = 12 ⇒ x = 4"], v=12 / 3)
T("The points A(−2, 1), B(4, 5) and C(6, 2) are the vertices of a triangle.<br>(a) Find the gradient of AB.<br>(b) Find the equation of the line through C parallel to AB.<br>(c) Show that triangle ABC is right-angled, and state where the right angle is.<br>(d) Find the area of the triangle.",
  [f"(a) m_{{AB}} = {F('5 − 1','4 − (−2)')} = <b>{F(2,3)}</b>",
   f"(b) y − 2 = {F(2,3)}(x − 6) ⇒ 3y − 6 = 2x − 12 ⇒ <b>2x − 3y − 6 = 0</b>",
   f"(c) m_{{BC}} = {F('2 − 5','6 − 4')} = −{F(3,2)}; m_{{AB}} × m_{{BC}} = {F(2,3)} × (−{F(3,2)}) = −1",
   "So AB ⊥ BC ⇒ <b>right angle at B</b>. (Check: AB^2 + BC^2 = 52 + 13 = 65 = AC^2.)",
   f"(d) Area = ½ × AB × BC = ½ × √52 × √13 = ½ × √676 = <b>13 square units</b>"], marks=12,
  ok=(Fr(4, 6) * Fr(-3, 2) == -1 and 52 + 13 == 8 ** 2 + 1 ** 2 and 2 * 6 - 3 * 2 - 6 == 0 and close(.5 * math.sqrt(52) * math.sqrt(13), 13)))
T("P(1, 3) and Q(5, −1) are two points.<br>(a) Find the equation of the perpendicular bisector of PQ.<br>(b) Find where it crosses the y-axis.<br>(c) Show that R(7, 5) lies on this line, and verify that RP = RQ.",
  [f"(a) Midpoint = (3, 1); m_{{PQ}} = {F('−1 − 3','5 − 1')} = −1 ⇒ the perpendicular gradient is 1",
   "y − 1 = 1(x − 3) ⇒ <b>y = x − 2</b>", "(b) At x = 0, y = −2 ⇒ <b>(0, −2)</b>",
   "(c) 7 − 2 = 5 ✓ so R lies on the line.",
   "RP = √[(7 − 1)^2 + (5 − 3)^2] = √40;  RQ = √[(7 − 5)^2 + (5 + 1)^2] = √40 ⇒ <b>RP = RQ</b> ✓"], marks=10,
  ok=(7 - 2 == 5 and (7 - 1) ** 2 + (5 - 3) ** 2 == (7 - 5) ** 2 + (5 + 1) ** 2 == 40))
