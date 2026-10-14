from core import *
import draw

# Plain-English intros, extra worked examples and diagrams for every Maths topic.
E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

extras("bases",
  plain="A number base tells you how many digits a counting system uses. We normally count in base ten "
        "(digits 0–9). In base five you only have 0, 1, 2, 3 and 4 — so after 4 you start a new column.",
  examples=[
    E("Change 324 in base five to base ten.",
      "Step 1. Write the place values from the right: 5^0 = 1, 5^1 = 5, 5^2 = 25.",
      "Step 2. Multiply each digit by its place value: 3 × 25 = 75, 2 × 5 = 10, 4 × 1 = 4.",
      "Step 3. Add them: 75 + 10 + 4 = <b>89</b>."),
    E("Change 89 to base five.",
      "Step 1. Divide by 5 again and again, writing the remainder each time.",
      "89 ÷ 5 = 17 remainder <b>4</b>;  17 ÷ 5 = 3 remainder <b>2</b>;  3 ÷ 5 = 0 remainder <b>3</b>.",
      "Step 2. Read the remainders from the BOTTOM upwards: <b>324 in base five</b>.",
      "Step 3. Check: it takes you back to 89, which is where you started.")],
  fig=draw.flow(["89 ÷ 5 = 17 r 4", "17 ÷ 5 = 3 r 2", "3 ÷ 5 = 0 r 3", "Read up: 324"],
                note="Changing 89 to base five", label="Division method for base conversion"))
assert int("324", 5) == 89

extras("mod",
  plain="Modulo arithmetic is clock arithmetic. In mod 5 the only answers are 0, 1, 2, 3 and 4 — when you "
        "pass 4 you go back to 0, just as a clock goes back to 1 after 12.",
  examples=[
    E("Find 27 (mod 5).",
      "Step 1. Ask: how many complete 5s are in 27?  5 × 5 = 25.",
      "Step 2. What is left over? 27 − 25 = 2.",
      "So 27 ≡ <b>2</b> (mod 5)."),
    E("Today is Tuesday. What day will it be in 45 days?",
      "Step 1. Days repeat every 7, so work in mod 7.",
      "Step 2. 45 ÷ 7 = 6 remainder 3, so 45 ≡ 3 (mod 7).",
      "Step 3. Count 3 days from Tuesday: Wednesday, Thursday, <b>Friday</b>.")],
  fig=draw.cyclefig(["0", "1", "2", "3", "4"], "mod 5", label="Modulo 5 clock"))
assert 27 % 5 == 2 and 45 % 7 == 3

extras("approx",
  plain="Approximation is about giving an answer that is close enough and easy to read. Significant figures "
        "count from the first non-zero digit; decimal places count after the point.",
  examples=[
    E("Round 0.04836 to (a) 2 significant figures (b) 3 decimal places.",
      "(a) The first significant figure is 4, the second is 8. The next digit is 3, which is less than 5, so 8 stays.",
      "Answer: <b>0.048</b>",
      "(b) Three places after the point gives 0.048, and the next digit is 3, so it stays.",
      "Answer: <b>0.048</b>"),
    E("A tank holds 2.5 litres but was measured as 2.4 litres. Find the percentage error.",
      "Step 1. Error = 2.5 − 2.4 = 0.1 litres.",
      f"Step 2. Percentage error = {F('error', 'true value')} × 100 = {F('0.1', '2.5')} × 100.",
      "Step 3. = <b>4%</b>")])
assert round(0.1 / 2.5 * 100, 6) == 4

extras("indices",
  plain="An index (power) tells you how many times a number multiplies itself: 2^4 means 2 × 2 × 2 × 2. "
        "The rules simply save you from writing all those multiplications.",
  examples=[
    E("Simplify 2^5 × 2^3 ÷ 2^6.",
      "Step 1. When multiplying, ADD the powers: 2^5 × 2^3 = 2^{5+3} = 2^8.",
      "Step 2. When dividing, SUBTRACT: 2^8 ÷ 2^6 = 2^{8−6} = 2^2.",
      "Step 3. 2^2 = <b>4</b>."),
    E("Solve 3^{x+2} = 81.",
      "Step 1. Write 81 as a power of 3: 81 = 3^4.",
      "Step 2. Now both sides have base 3: 3^{x+2} = 3^4.",
      "Step 3. Equal bases ⇒ equal powers: x + 2 = 4 ⇒ <b>x = 2</b>.")])
assert 2 ** 5 * 2 ** 3 / 2 ** 6 == 4 and 3 ** (2 + 2) == 81

extras("logs",
  plain="A logarithm answers the question: 'to what power must I raise this base to get that number?' "
        "So log₂ 8 = 3 because 2³ = 8. A log is just an index written the other way round.",
  examples=[
    E("Evaluate log_{5} 125.",
      "Step 1. Ask: 5 to what power gives 125?",
      "Step 2. 5 × 5 × 5 = 125, so the power is 3.",
      "log_{5} 125 = <b>3</b>"),
    E("Given log 2 = 0.3010 and log 5 = 0.6990, find log 40 without tables.",
      "Step 1. Break 40 into numbers you know: 40 = 2^3 × 5.",
      "Step 2. Use the rules: log 40 = 3 log 2 + log 5.",
      "Step 3. = 3(0.3010) + 0.6990 = 0.9030 + 0.6990 = <b>1.6020</b>")])
assert close(3 * .3010 + .6990, 1.6020)

extras("surds",
  plain="A surd is a root that cannot be worked out exactly, such as √2 or √3. We leave it as a root and "
        "tidy it up instead of using a decimal, so the answer stays exact.",
  examples=[
    E("Simplify √200.",
      "Step 1. Look for a square number that divides 200: 100 × 2 = 200.",
      "Step 2. √200 = √100 × √2.",
      "Step 3. √100 = 10, so √200 = <b>10√2</b>."),
    E(f"Rationalise {F(3, '2 − √5')}.",
      "Step 1. Multiply top and bottom by the conjugate, 2 + √5.",
      f"Step 2. Bottom: (2 − √5)(2 + √5) = 4 − 5 = −1.",
      f"Step 3. Top: 3(2 + √5) = 6 + 3√5.",
      f"Step 4. {F('6 + 3√5', '−1')} = <b>−6 − 3√5</b>")])
assert close(float(sp.sqrt(200)), 10 * float(sp.sqrt(2)))
assert sp.simplify(3 / (2 - sp.sqrt(5)) - (-6 - 3 * sp.sqrt(5))) == 0

extras("seq",
  plain="A sequence is a list of numbers that follows a rule. In an AP you ADD the same number each time; "
        "in a GP you MULTIPLY by the same number each time.",
  examples=[
    E("Find the 12th term of 7, 10, 13, 16, …",
      "Step 1. Check the type: 10 − 7 = 3 and 13 − 10 = 3, so it is an AP with d = 3, a = 7.",
      "Step 2. Use T_n = a + (n − 1)d.",
      "Step 3. T_{12} = 7 + 11 × 3 = 7 + 33 = <b>40</b>."),
    E("Find the sum of the first 5 terms of 3, 6, 12, 24, …",
      "Step 1. 6 ÷ 3 = 2 and 12 ÷ 6 = 2, so it is a GP with a = 3, r = 2.",
      f"Step 2. S_n = {F('a(r^n − 1)', 'r − 1')} = {F('3(2^5 − 1)', '2 − 1')}",
      "Step 3. = 3(32 − 1) = 3 × 31 = <b>93</b>.")])
assert 7 + 11 * 3 == 40 and sum(3 * 2 ** i for i in range(5)) == 93

extras("sets",
  plain="A set is simply a group of things. Venn diagrams let you SEE the groups: the overlap holds the "
        "members that belong to both, and everything is drawn inside the universal set.",
  examples=[
    E("In a class of 40, 22 play football, 18 play volleyball and 5 play both. How many play neither?",
      "Step 1. Fill the middle first: 5 play both.",
      "Step 2. Football only = 22 − 5 = 17.  Volleyball only = 18 − 5 = 13.",
      "Step 3. Players inside the circles = 17 + 5 + 13 = 35.",
      "Step 4. Neither = 40 − 35 = <b>5</b>.",
      fig=draw.venn2("Football", "Volleyball", 17, 5, 13, 5, label="Football and volleyball")),
    E("If n(A) = 18, n(B) = 14 and n(A ∪ B) = 25, find n(A ∩ B).",
      "Step 1. Use n(A ∪ B) = n(A) + n(B) − n(A ∩ B).",
      "Step 2. 25 = 18 + 14 − n(A ∩ B) = 32 − n(A ∩ B).",
      "Step 3. n(A ∩ B) = 32 − 25 = <b>7</b>.")])
assert 40 - (17 + 5 + 13) == 5 and 18 + 14 - 25 == 7

extras("logic",
  plain="Logic is about deciding whether an argument really follows. Drawing a Venn diagram of the "
        "statements is the quickest way to see whether a conclusion must be true.",
  examples=[
    E("'All teachers are graduates. Kofi is a teacher.' What follows?",
      "Step 1. Draw the graduates circle, and put the teachers circle completely inside it.",
      "Step 2. Kofi is inside the teachers circle, so he must also be inside the graduates circle.",
      "Conclusion: <b>Kofi is a graduate</b>. (Note that 'All graduates are teachers' does NOT follow.)",
      fig=draw.venn2("Graduates", "Teachers", "", "Kofi", "", label="All teachers are graduates")),
    E("Write the converse and the contrapositive of 'If a triangle is equilateral, then it is isosceles.'",
      "Step 1. Name the parts: p = 'the triangle is equilateral', q = 'it is isosceles'.",
      "Step 2. Converse (q → p): If a triangle is isosceles, then it is equilateral. (This one is false.)",
      "Step 3. Contrapositive (~q → ~p): If a triangle is not isosceles, then it is not equilateral. "
      "(This is always true when the original is true.)")])

extras("fin",
  plain="Financial arithmetic is everyday money maths: sharing money, working out profit, discount, "
        "interest on savings and the extra you pay when you buy on hire purchase.",
  examples=[
    E("A trader bought a bag of rice for GH₵ 420 and sold it for GH₵ 483. Find the percentage profit.",
      "Step 1. Profit = selling price − cost price = 483 − 420 = GH₵ 63.",
      f"Step 2. Percentage profit = {F('profit', 'cost price')} × 100 = {F(63, 420)} × 100.",
      "Step 3. = <b>15%</b>  (always divide by the COST price)."),
    E("GH₵ 8,000 is saved at 9% per annum simple interest for 4 years. Find the amount.",
      f"Step 1. I = {F('PRT', 100)} = {F('8000 × 9 × 4', 100)}.",
      "Step 2. I = GH₵ 2,880.",
      "Step 3. Amount = principal + interest = 8000 + 2880 = <b>GH₵ 10,880</b>.")])
assert 63 / 420 * 100 == 15 and 8000 * 9 * 4 / 100 == 2880

extras("var",
  plain="Variation describes how one quantity changes when another changes. Direct: both grow together. "
        "Inverse: one grows while the other falls. Always find the constant k first.",
  examples=[
    E("y varies inversely as x. When x = 3, y = 8. Find y when x = 12.",
      f"Step 1. Write the relation: y = {F('k', 'x')}.",
      "Step 2. Find k: 8 = k ÷ 3, so k = 24.",
      f"Step 3. y = {F(24, 12)} = <b>2</b>.  (x became 4 times bigger, so y became 4 times smaller.)"),
    E("The cost C of hiring a bus is partly constant and partly varies with the distance d. "
      "It costs GH₵ 500 for 100 km and GH₵ 700 for 200 km. Find C when d = 350 km.",
      "Step 1. Write C = a + bd.",
      "Step 2. 500 = a + 100b … (i);  700 = a + 200b … (ii).",
      "Step 3. (ii) − (i): 200 = 100b ⇒ b = 2; then a = 500 − 200 = 300.",
      "Step 4. C = 300 + 2(350) = <b>GH₵ 1,000</b>.")])
assert 24 / 12 == 2 and 300 + 2 * 350 == 1000

extras("matrix",
  plain="A matrix is a box of numbers arranged in rows and columns. It is a neat way of handling several "
        "numbers at once — for example, solving two equations in one go.",
  examples=[
    E(f"Given A = {M([[2,3],[1,4]])}, find |A| and A^{{-1}}.",
      "Step 1. |A| = (2 × 4) − (3 × 1) = 8 − 3 = <b>5</b>.",
      "Step 2. For the inverse: swap 2 and 4, change the signs of 3 and 1.",
      f"Step 3. A^{{-1}} = {F(1,5)}{M([[4,-3],[-1,2]])}"),
    E(f"Find 3P − Q where P = {M([[1,2],[0,3]])} and Q = {M([[2,-1],[4,5]])}.",
      f"Step 1. Multiply every number in P by 3: 3P = {M([[3,6],[0,9]])}.",
      "Step 2. Subtract the matching numbers of Q.",
      f"Step 3. 3P − Q = {M([['3−2','6+1'],['0−4','9−5']])} = <b>{M([[1,7],[-4,4]])}</b>")])
assert sp.Matrix([[2, 3], [1, 4]]).det() == 5
assert 3 * sp.Matrix([[1, 2], [0, 3]]) - sp.Matrix([[2, -1], [4, 5]]) == sp.Matrix([[1, 7], [-4, 4]])

extras("alg",
  plain="Algebra uses letters to stand for numbers we do not know yet. Solving an equation means undoing "
        "what was done to the letter, doing the same thing to BOTH sides.",
  examples=[
    E("Solve 5(x − 2) = 3x + 8.",
      "Step 1. Open the bracket: 5x − 10 = 3x + 8.",
      "Step 2. Take 3x from both sides: 2x − 10 = 8.",
      "Step 3. Add 10 to both sides: 2x = 18.",
      "Step 4. Divide by 2: <b>x = 9</b>.  Check: 5(9 − 2) = 35 and 3(9) + 8 = 35 ✓"),
    E("Ama bought 3 pens and 2 books for GH₵ 34. Kofi bought 5 pens and 2 books for GH₵ 46. "
      "Find the price of a pen and of a book.",
      "Step 1. Let a pen cost p and a book cost b:  3p + 2b = 34 … (i);  5p + 2b = 46 … (ii).",
      "Step 2. The 2b is the same in both, so subtract (i) from (ii): 2p = 12 ⇒ p = 6.",
      "Step 3. Put p = 6 into (i): 18 + 2b = 34 ⇒ 2b = 16 ⇒ b = 8.",
      "<b>A pen costs GH₵ 6 and a book GH₵ 8.</b>")])
assert sp.solve(5 * (x - 2) - (3 * x + 8), x) == [9]
assert sp.solve([3 * x + 2 * y - 34, 5 * x + 2 * y - 46], [x, y]) == {x: 6, y: 8}

_p = lambda t: t * t - 2 * t - 3
extras("quad",
  plain="A quadratic has an x² in it, so it usually has TWO answers. Its graph is a smooth U-shaped curve, "
        "and the answers are where the curve crosses the x-axis.",
  examples=[
    E("Solve x^2 − 2x − 3 = 0 by factorisation.",
      "Step 1. Find two numbers that multiply to −3 and add to −2: they are −3 and +1.",
      "Step 2. x^2 − 3x + x − 3 = 0 ⇒ x(x − 3) + 1(x − 3) = 0.",
      "Step 3. (x − 3)(x + 1) = 0, so x − 3 = 0 or x + 1 = 0.",
      "Step 4. <b>x = 3 or x = −1</b> — the same two points where the curve cuts the x-axis.",
      fig=plot(_p, -3, 5, -5, 9, pts=[(3, 0, "(3, 0)"), (-1, 0, "(−1, 0)")])),
    E("Solve 2x^2 + 5x − 3 = 0 using the formula.",
      "Step 1. a = 2, b = 5, c = −3.",
      f"Step 2. x = {F('−b ± √(b^2 − 4ac)', '2a')} = {F('−5 ± √(25 + 24)', 4)}",
      "Step 3. √49 = 7, so x = (−5 + 7)/4 or (−5 − 7)/4.",
      f"Step 4. <b>x = {F(1,2)} or x = −3</b>")])
assert sorted(sp.solve(x ** 2 - 2 * x - 3, x)) == [-1, 3]
assert sorted(sp.solve(2 * x ** 2 + 5 * x - 3, x)) == [-3, sp.Rational(1, 2)]

extras("ineq",
  plain="An inequality says one side is bigger or smaller than the other, so the answer is a RANGE of "
        "values, not a single number. One rule to remember: multiplying or dividing by a negative number "
        "turns the sign round.",
  examples=[
    E("Solve 4 − 3x ≥ −5 and show the answer on a number line.",
      "Step 1. Take 4 from both sides: −3x ≥ −9.",
      "Step 2. Divide by −3 AND turn the sign round: x ≤ 3.",
      "Step 3. On the number line, shade everything up to 3, with a filled circle at 3 because 3 is included.",
      fig=draw.numline(-2, 6, seg=(None, 3, None, True), label="x is less than or equal to 3")),
    E("Find the integers that satisfy 2 < 3x − 1 ≤ 11.",
      "Step 1. Add 1 throughout: 3 < 3x ≤ 12.",
      "Step 2. Divide throughout by 3: 1 < x ≤ 4.",
      "Step 3. The integers greater than 1 and up to 4 are <b>2, 3 and 4</b>.")])
assert [t for t in range(-5, 9) if 2 < 3 * t - 1 <= 11] == [2, 3, 4]

extras("afunc",
  plain="A function is a machine: you put a number in, and it gives one number out. f(3) simply means "
        "'put 3 into the machine'. The inverse machine undoes what the first one did.",
  examples=[
    E("If f(x) = 4x − 5, find (a) f(3) (b) f^{-1}(x) (c) f^{-1}(7).",
      "(a) Put 3 in place of x: f(3) = 4(3) − 5 = <b>7</b>.",
      "(b) Write y = 4x − 5, swap the letters: x = 4y − 5.",
      f"Make y the subject: 4y = x + 5 ⇒ f^{{-1}}(x) = {F('x + 5', 4)}.",
      f"(c) f^{{-1}}(7) = {F('7 + 5', 4)} = <b>3</b> — it takes us back to where we started in (a)."),
    E(f"Simplify {F(1, 'x − 2')} + {F(3, 'x + 1')}.",
      "Step 1. The common denominator is (x − 2)(x + 1).",
      f"Step 2. {F('1(x + 1) + 3(x − 2)', '(x − 2)(x + 1)')}",
      f"Step 3. Top: x + 1 + 3x − 6 = 4x − 5.",
      f"Answer: <b>{F('4x − 5', '(x − 2)(x + 1)')}</b>")])
assert sp.simplify(1 / (x - 2) + 3 / (x + 1) - (4 * x - 5) / ((x - 2) * (x + 1))) == 0

extras("area",
  plain="Perimeter is the distance round the edge; area is the space inside. For a sector (a slice of a "
        "circle), first find what fraction of the whole circle you have, then take that fraction of the circle.",
  examples=[
    E(f"Find the area and the perimeter of a sector of radius 7 cm with angle 90°. [π = {F(22,7)}]",
      f"Step 1. The fraction of the circle is {F(90,360)} = {F(1,4)}.",
      f"Step 2. Area = {F(1,4)} × {F(22,7)} × 7 × 7 = {F(1,4)} × 154 = <b>38.5 cm²</b>.",
      f"Step 3. Arc = {F(1,4)} × 2 × {F(22,7)} × 7 = {F(1,4)} × 44 = 11 cm.",
      "Step 4. Perimeter = arc + the two radii = 11 + 7 + 7 = <b>25 cm</b>.",
      fig=draw.sectorfig(90, "7 cm", label="Quarter circle of radius 7 cm")),
    E("A room is 6 m by 4.5 m. Find the cost of tiling it at GH₵ 85 per square metre.",
      "Step 1. Area = length × breadth = 6 × 4.5 = 27 m².",
      "Step 2. Cost = 27 × 85.",
      "Step 3. = <b>GH₵ 2,295</b>.")])
assert float(Fr(1, 4) * Fr(22, 7) * 49) == 38.5 and 27 * 85 == 2295

extras("vol",
  plain="Volume is the space inside a solid — how much it can hold. Surface area is the skin: how much "
        "material would be needed to cover it.",
  examples=[
    E(f"A cylindrical tank has radius 7 cm and height 20 cm. Find its volume. [π = {F(22,7)}]",
      "Step 1. Volume of a cylinder = πr²h.",
      f"Step 2. = {F(22,7)} × 7 × 7 × 20.",
      f"Step 3. {F(22,7)} × 49 = 154, and 154 × 20 = <b>3,080 cm³</b>.",
      fig=draw.solidfig("cylinder", ("7 cm", "20 cm"), label="Cylinder, radius 7 cm, height 20 cm")),
    E("A cone has base radius 6 cm and height 8 cm. Find its slant height and curved surface area, in terms of π.",
      "Step 1. The radius, height and slant height form a right-angled triangle.",
      "Step 2. l = √(6² + 8²) = √100 = <b>10 cm</b>.",
      "Step 3. Curved surface area = πrl = π × 6 × 10 = <b>60π cm²</b>.",
      fig=draw.solidfig("cone", ("6 cm", "8 cm", "l = 10"), label="Cone, radius 6 cm, height 8 cm"))])
assert float(Fr(22, 7) * 49 * 20) == 3080 and math.hypot(6, 8) == 10

extras("geo",
  plain="Plane geometry is about shapes drawn flat on paper: their angles and their sides. Most questions "
        "come back to two facts — angles in a triangle add up to 180°, and angles on a straight line add up to 180°.",
  examples=[
    E("A ladder leans against a wall. Its foot is 9 m from the wall and it reaches 12 m up the wall. "
      "How long is the ladder?",
      "Step 1. The wall, the ground and the ladder form a right-angled triangle.",
      "Step 2. Pythagoras: ladder² = 9² + 12² = 81 + 144 = 225.",
      "Step 3. Ladder = √225 = <b>15 m</b>.",
      fig=draw.tri(a="12 m", c="9 m", b="15 m", right=True, label="Right-angled triangle 9, 12, 15")),
    E("Find the number of sides of a regular polygon whose interior angle is 156°.",
      "Step 1. Interior + exterior = 180°, so the exterior angle = 180 − 156 = 24°.",
      "Step 2. All the exterior angles add up to 360°.",
      "Step 3. Number of sides = 360 ÷ 24 = <b>15</b>.")])
assert math.hypot(9, 12) == 15 and 360 / 24 == 15

extras("circle",
  plain="Circle theorems are a small set of facts about angles inside a circle. The one examiners use most: "
        "the angle at the centre is twice the angle at the circumference standing on the same arc.",
  examples=[
    E("O is the centre of a circle. Angle AOB = 130°. Find angle ACB, where C is on the major arc.",
      "Step 1. AOB is at the centre; ACB is at the circumference, on the same arc AB.",
      "Step 2. Angle at the centre = 2 × angle at the circumference.",
      "Step 3. 130 = 2 × ACB ⇒ ACB = <b>65°</b>.",
      fig=draw.circlefig("centre", ["130°", "65°"], label="Angle at centre is twice angle at circumference")),
    E("In a cyclic quadrilateral ABCD, angle A = 72°. Find angle C.",
      "Step 1. A and C are opposite angles of a cyclic quadrilateral.",
      "Step 2. Opposite angles add up to 180°.",
      "Step 3. Angle C = 180 − 72 = <b>108°</b>.",
      fig=draw.circlefig("cyclic", ["72°", "108°"], label="Opposite angles of a cyclic quadrilateral"))])

extras("loci",
  plain="A locus is the path traced by a point that obeys a rule — for example, 'always 3 m from this post'. "
        "In construction questions, show all your arcs: the examiner gives marks for them.",
  examples=[
    E("Construct an angle of 30° at a point A on a line.",
      "Step 1. With centre A and any radius, draw an arc cutting the line at P.",
      "Step 2. With the SAME radius and centre P, cut the arc at Q. Join AQ — angle QAP is 60°.",
      "Step 3. Bisect angle QAP: draw arcs of equal radius from P and from Q so that they cross at R.",
      "Step 4. Join AR. Angle RAP = <b>30°</b>."),
    E("A goat is tied to a post with a 4 m rope in an open field. Describe and find the area it can graze.",
      "Step 1. The furthest points form a circle of radius 4 m about the post — that is the locus.",
      f"Step 2. Area = πr² = {F(22,7)} × 4 × 4.",
      "Step 3. = <b>50.29 m²</b> (2 d.p.)")])
assert round(float(Fr(22, 7) * 16), 2) == 50.29

extras("coord",
  plain="Coordinate geometry puts shapes on a grid so that you can work with numbers instead of drawings. "
        "Gradient means steepness: how far up divided by how far across.",
  examples=[
    E("Find the gradient of the line through A(1, 2) and B(5, 10), and its equation.",
      f"Step 1. Gradient m = {F('y_2 − y_1', 'x_2 − x_1')} = {F('10 − 2', '5 − 1')} = {F(8,4)} = 2.",
      "Step 2. Use y − y₁ = m(x − x₁) with A(1, 2): y − 2 = 2(x − 1).",
      "Step 3. y − 2 = 2x − 2 ⇒ <b>y = 2x</b>.",
      fig=plot(lambda t: 2 * t, 0, 6, 0, 12, pts=[(1, 2, "A"), (5, 10, "B")], label="Line through A and B")),
    E("Find the distance between P(−2, 3) and Q(4, 11).",
      "Step 1. Difference in x = 4 − (−2) = 6.  Difference in y = 11 − 3 = 8.",
      "Step 2. Distance = √(6² + 8²) = √(36 + 64).",
      "Step 3. = √100 = <b>10 units</b>.")])
assert math.hypot(6, 8) == 10

extras("trig",
  plain="Trigonometry connects the angles of a right-angled triangle with the lengths of its sides. "
        "Remember SOH-CAH-TOA: Sin = Opposite/Hypotenuse, Cos = Adjacent/Hypotenuse, Tan = Opposite/Adjacent.",
  examples=[
    E("A tree casts a shadow 15 m long. The angle of elevation of the top of the tree from the end of the "
      "shadow is 40°. Find the height of the tree.",
      "Step 1. Draw it: the height is OPPOSITE the angle, the shadow is ADJACENT — so use tan.",
      f"Step 2. tan 40° = {F('height', 15)} ⇒ height = 15 × tan 40°.",
      "Step 3. tan 40° = 0.8391, so height = 15 × 0.8391 = <b>12.59 m</b> (2 d.p.).",
      fig=draw.tri(a="height", c="15 m (shadow)", A="40°", right=True, label="Angle of elevation 40 degrees")),
    E(f"If cos θ = {F(8,17)} and θ is acute, find sin θ and tan θ.",
      "Step 1. cos = adjacent ÷ hypotenuse, so adjacent = 8 and hypotenuse = 17.",
      "Step 2. Opposite = √(17² − 8²) = √(289 − 64) = √225 = 15.",
      f"Step 3. sin θ = {F(15,17)} and tan θ = {F(15,8)}.")])
assert round(15 * math.tan(math.radians(40)), 2) == 12.59 and math.isqrt(289 - 64) == 15

extras("bear",
  plain="A bearing tells direction. You always start facing North and turn clockwise, and you always write "
        "three figures — 060°, not 60°.",
  examples=[
    E("A town Q is 8 km from P on a bearing of 060°. R is 6 km from Q on a bearing of 150°. "
      "Find |PR| and the bearing of R from P.",
      "Step 1. The back bearing of P from Q is 060 + 180 = 240°, and the bearing of R is 150°, "
      "so angle PQR = 240 − 150 = 90°.",
      "Step 2. Pythagoras: PR = √(8² + 6²) = √100 = <b>10 km</b>.",
      "Step 3. tan(angle QPR) = 6 ÷ 8 = 0.75 ⇒ angle QPR = 36.87°.",
      "Step 4. Bearing of R from P = 060 + 36.87 ≈ <b>097°</b>.",
      fig=draw.compass([(60, "Q", 0.9), (150, "R", 0.75)], label="Bearings 060 and 150")),
    E("The bearing of X from Y is 205°. Find the bearing of Y from X.",
      "Step 1. Back bearing = bearing ± 180°.",
      "Step 2. 205 is more than 180, so subtract: 205 − 180 = 25.",
      "Step 3. Write it in three figures: <b>025°</b>.")])
assert round(60 + math.degrees(math.atan(6 / 8))) == 97

_c = lambda t: t * t - 4 * t + 5
extras("calc",
  plain="Calculus measures change. Differentiation gives the gradient — how steep a curve is at a point. "
        "Integration is the opposite: it adds up, and gives the area under a curve.",
  examples=[
    E("Find the gradient of y = x² − 4x + 5 at the point where x = 3, and the equation of the tangent there.",
      "Step 1. Differentiate term by term: dy/dx = 2x − 4.",
      "Step 2. At x = 3: gradient = 2(3) − 4 = <b>2</b>.",
      "Step 3. y at x = 3 is 9 − 12 + 5 = 2, so the point is (3, 2).",
      "Step 4. Tangent: y − 2 = 2(x − 3) ⇒ <b>y = 2x − 4</b>.",
      fig=plot(_c, 0, 5, 0, 7, pts=[(3, 2, "(3, 2)")], lines=[(1, -2, 5, 6)], label="Curve and its tangent at x = 3")),
    E("Evaluate ∫(4x^3 − 6x) dx from x = 1 to x = 2.",
      "Step 1. Integrate: add one to each power and divide by the new power ⇒ x^4 − 3x^2.",
      "Step 2. Put in the top value: 2^4 − 3(2²) = 16 − 12 = 4.",
      "Step 3. Put in the bottom value: 1 − 3 = −2.",
      "Step 4. Subtract: 4 − (−2) = <b>6</b>.")])
assert sp.integrate(4 * x ** 3 - 6 * x, (x, 1, 2)) == 6

extras("stat",
  plain="Statistics is about making sense of a set of figures: the mean is the average, the median is the "
        "middle one, and the mode is the most common. A chart shows the picture at a glance.",
  examples=[
    E("The marks of 5 students are 12, 15, 15, 18 and 20. Find the mean, median and mode.",
      "Step 1. Mean = (12 + 15 + 15 + 18 + 20) ÷ 5 = 80 ÷ 5 = <b>16</b>.",
      "Step 2. Arrange in order — they already are. The middle (3rd) value is <b>15</b>, the median.",
      "Step 3. 15 appears twice, more than any other, so the mode is <b>15</b>.",
      fig=draw.barfig([("12", 1), ("15", 2), ("18", 1), ("20", 1)], label="Frequency of each mark", ylab="frequency")),
    E("In a class of 60, 25 chose Science, 20 Arts and 15 Business. Find the pie chart angles.",
      f"Step 1. Angle = {F('frequency', 'total')} × 360°.",
      f"Step 2. Science = {F(25,60)} × 360 = <b>150°</b>;  Arts = {F(20,60)} × 360 = <b>120°</b>.",
      f"Step 3. Business = {F(15,60)} × 360 = <b>90°</b>.  Check: 150 + 120 + 90 = 360 ✓",
      fig=draw.piefig([("Science", 25), ("Arts", 20), ("Business", 15)], label="Pie chart of subject choices"))])
assert 80 / 5 == 16 and 25 / 60 * 360 == 150

extras("prob",
  plain="Probability measures how likely something is, on a scale from 0 (impossible) to 1 (certain). "
        "It is simply: the number of ways you can win, divided by the total number of ways.",
  examples=[
    E("A bag has 3 red, 5 green and 2 yellow balls. One ball is picked. Find P(green) and P(not green).",
      "Step 1. Total = 3 + 5 + 2 = 10 balls.",
      f"Step 2. P(green) = {F(5,10)} = <b>{F(1,2)}</b>.",
      f"Step 3. P(not green) = 1 − {F(1,2)} = <b>{F(1,2)}</b>."),
    E("Two balls are picked from the bag above, one after the other, WITHOUT replacement. Find P(both red).",
      f"Step 1. First ball red: {F(3,10)}.",
      f"Step 2. Now only 2 red balls are left out of 9: {F(2,9)}.",
      f"Step 3. Multiply along the branch: {F(3,10)} × {F(2,9)} = {F(6,90)} = <b>{F(1,15)}</b>.",
      fig=draw.tree("First pick (10 balls)", ["Red 3/10", "Green 5/10", "Yellow 2/10"],
                    sub=["then 2/9 red", "", ""], label="Probability tree for the first pick"))])
assert Fr(3, 10) * Fr(2, 9) == Fr(1, 15)

extras("vec",
  plain="A vector has both size and direction — like saying '5 km north' instead of just '5 km'. "
        "You add vectors by adding the top numbers and the bottom numbers separately.",
  examples=[
    E(f"Given a = {V(4,-3)} and b = {V(-1,5)}, find a + 2b and |a|.",
      f"Step 1. 2b = {V(-2,10)}.",
      f"Step 2. a + 2b = {V('4 − 2','−3 + 10')} = <b>{V(2,7)}</b>.",
      "Step 3. |a| = √(4² + (−3)²) = √(16 + 9) = √25 = <b>5</b>."),
    E("The point P(3, −2) is reflected in the y-axis, then translated by (1, 4). Find the final position.",
      "Step 1. Reflection in the y-axis changes the sign of x: (3, −2) → (−3, −2).",
      "Step 2. Translation adds the vector: (−3 + 1, −2 + 4).",
      "Step 3. Final position: <b>(−2, 2)</b>.",
      fig=plot(None, -5, 5, -4, 4, pts=[(3, -2, "P"), (-3, -2, "P′"), (-2, 2, "P″")],
               label="Reflection then translation"))])
assert math.hypot(4, 3) == 5
