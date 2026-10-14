from core import *

S = "Number & Numeration"

# ------------------------------------------------------------------ 1
topic("bases", "Number bases", S, [
    "Place values in base b are …, b^2, b^1, b^0 . b^{-1}, b^{-2} …",
    "Base b → base 10: multiply each digit by its place value and add.",
    "Base 10 → base b: divide repeatedly by b and read the remainders from the bottom up.",
    "A digit in base b must be less than b (base 5 uses only 0–4).",
])
O("Convert 243_{five} to a base ten number.", ["73", "63", "78", "48"],
  ["243_{five} = 2 × 5^2 + 4 × 5^1 + 3 × 5^0", "= 50 + 20 + 3 = 73"], v=int("243", 5))
O("Express 45 in base two.", ["101101_{two}", "110101_{two}", "101011_{two}", "100101_{two}"],
  ["45 ÷ 2 = 22 r 1; 22 ÷ 2 = 11 r 0; 11 ÷ 2 = 5 r 1; 5 ÷ 2 = 2 r 1; 2 ÷ 2 = 1 r 0; 1 ÷ 2 = 0 r 1",
   "Reading the remainders upwards: 101101_{two}"],
  v=45, nv=[int("101101", 2), int("110101", 2), int("101011", 2), int("100101", 2)])
O("If 23_{x} = 17_{ten}, find the value of x.", ["7", "8", "6", "5"],
  ["23_{x} = 2x + 3", "2x + 3 = 17 ⇒ 2x = 14 ⇒ x = 7"],
  v=7, nv=[7, 8, 6, 5], ok=None) if all((2 * t + 3 == 17) == (t == 7) for t in [5, 6, 7, 8]) else FAIL()
O("Evaluate 110_{two} × 11_{two}, leaving your answer in base two.",
  ["10010_{two}", "11010_{two}", "10110_{two}", "1001_{two}"],
  ["110_{two} = 6 and 11_{two} = 3", "6 × 3 = 18", "18 = 16 + 2 = 10010_{two}"],
  v=int("110", 2) * int("11", 2), nv=[int(s, 2) for s in ["10010", "11010", "10110", "1001"]])
O("Simplify 346_{seven} + 254_{seven}, giving your answer in base seven.",
  ["633_{seven}", "623_{seven}", "533_{seven}", "643_{seven}"],
  ["Add column by column from the right, carrying 7s.",
   "6 + 4 = 10 = 1 × 7 + 3 → write 3, carry 1",
   "4 + 5 + 1 = 10 = 1 × 7 + 3 → write 3, carry 1",
   "3 + 2 + 1 = 6 → write 6", "Answer: 633_{seven}"],
  v=int("346", 7) + int("254", 7), nv=[int(s, 7) for s in ["633", "623", "533", "643"]])
O("Which of the following numbers is the greatest?", ["10_{six}", "12_{three}", "11_{four}", "101_{two}"],
  ["10_{six} = 6", "12_{three} = 3 + 2 = 5", "11_{four} = 4 + 1 = 5", "101_{two} = 4 + 1 = 5",
   "The greatest is 10_{six}."],
  v=6, nv=[int("10", 6), int("12", 3), int("11", 4), int("101", 2)])
T("(a) Convert 1011.101_{two} to a base ten number.<br>(b) Find n if 124_{n} = 232_{five}.<br>(c) Express 67 in base three.",
  ["(a) 1011.101_{two} = 1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 + 1×2^{-1} + 0×2^{-2} + 1×2^{-3}",
   "= 8 + 0 + 2 + 1 + 0.5 + 0 + 0.125 = <b>11.625</b>",
   "(b) 232_{five} = 2×25 + 3×5 + 2 = 67",
   "124_{n} = n^2 + 2n + 4, so n^2 + 2n + 4 = 67 ⇒ n^2 + 2n − 63 = 0",
   "(n + 9)(n − 7) = 0 ⇒ n = 7 (a base cannot be negative, and the digit 4 needs n > 4). <b>n = 7</b>",
   "(c) 67 ÷ 3 = 22 r 1; 22 ÷ 3 = 7 r 1; 7 ÷ 3 = 2 r 1; 2 ÷ 3 = 0 r 2",
   "Reading upwards: <b>2111_{three}</b>"], marks=10,
  ok=(8 + 2 + 1 + .5 + .125 == 11.625 and int("124", 7) == int("232", 5) == 67 and int("2111", 3) == 67))
T("(a) Simplify 1101_{two} + 111_{two} − 1010_{two}, leaving the answer in base two.<br>(b) Find y if 2y1_{three} = 25_{ten}.<br>(c) Write down the largest three-digit number in base six and express it in base ten.",
  ["(a) Convert to base ten: 1101_{two} = 13, 111_{two} = 7, 1010_{two} = 10",
   "13 + 7 − 10 = 10 = <b>1010_{two}</b>",
   "(b) 2y1_{three} = 2×9 + 3y + 1 = 19 + 3y",
   "19 + 3y = 25 ⇒ 3y = 6 ⇒ <b>y = 2</b> (valid, since 2 < 3)",
   "(c) The largest digit in base six is 5, so the number is 555_{six}",
   "555_{six} = 5×36 + 5×6 + 5 = <b>215</b>"], marks=10,
  ok=(13 + 7 - 10 == int("1010", 2) and int("221", 3) == 25 and int("555", 6) == 215))

# ------------------------------------------------------------------ 2
topic("mod", "Modular arithmetic", S, [
    "a ≡ b (mod m) means a and b leave the same remainder when divided by m.",
    "Reduce each number first, then add or multiply, then reduce again.",
    "Days of the week work in mod 7; a 12-hour clock works in mod 12.",
    "The multiplicative inverse of a (mod m) is the number b with ab ≡ 1 (mod m).",
])
O("Find the value of 29 (mod 6).", ["5", "4", "3", "2"], ["29 = 4 × 6 + 5", "29 ≡ 5 (mod 6)"], v=29 % 6)
O("Evaluate (17 × 23) (mod 5).", ["1", "2", "3", "4"],
  ["17 ≡ 2 (mod 5) and 23 ≡ 3 (mod 5)", "2 × 3 = 6 ≡ 1 (mod 5)"], v=(17 * 23) % 5)
O("Solve 3x ≡ 2 (mod 7).", ["x = 3", "x = 4", "x = 5", "x = 6"],
  ["Test values: 3 × 3 = 9 = 7 + 2 ≡ 2 (mod 7)", "So x = 3"],
  v=3, nv=[3, 4, 5, 6], tip="Check the other options too: 3×4 ≡ 5, 3×5 ≡ 1, 3×6 ≡ 4 (mod 7).") \
    if [t for t in range(7) if 3 * t % 7 == 2] == [3] else FAIL()
O("Today is Wednesday. What day of the week will it be in 100 days' time?",
  ["Friday", "Thursday", "Saturday", "Tuesday"],
  ["Days repeat every 7, so work in mod 7.", "100 = 14 × 7 + 2, so 100 ≡ 2 (mod 7)",
   "Two days after Wednesday is Friday."],
  ok=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][(2 + 100) % 7] == "Fri")
O("In modulo 9, find the additive inverse of 4.", ["5", "4", "3", "1"],
  ["The additive inverse b satisfies 4 + b ≡ 0 (mod 9)", "4 + 5 = 9 ≡ 0, so b = 5"],
  v=5, nv=[5, 4, 3, 1]) if [t for t in [5, 4, 3, 1] if (4 + t) % 9 == 0] == [5] else FAIL()
O("Find the remainder when 2^{10} is divided by 11.", ["1", "2", "10", "0"],
  ["2^5 = 32 = 2 × 11 + 10, so 2^5 ≡ 10 ≡ −1 (mod 11)", "2^{10} = (2^5)^2 ≡ (−1)^2 = 1 (mod 11)"],
  v=2 ** 10 % 11)
T("(a) Construct a multiplication table in modulo 5 for the set {1, 2, 3, 4}.<br>(b) Use your table to find: (i) 3 × 4 (mod 5); (ii) the multiplicative inverse of 3; (iii) the value of x for which 4x ≡ 3 (mod 5).",
  ["(a) <table class=\"mt\"><tr><th>×</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>"
   "<tr><th>1</th><td>1</td><td>2</td><td>3</td><td>4</td></tr>"
   "<tr><th>2</th><td>2</td><td>4</td><td>1</td><td>3</td></tr>"
   "<tr><th>3</th><td>3</td><td>1</td><td>4</td><td>2</td></tr>"
   "<tr><th>4</th><td>4</td><td>3</td><td>2</td><td>1</td></tr></table>",
   "(b)(i) From the table, row 3, column 4: <b>3 × 4 ≡ 2</b>",
   "(ii) Look for 1 in row 3: 3 × 2 ≡ 1, so the inverse of 3 is <b>2</b>",
   "(iii) Look for 3 in row 4: 4 × 2 ≡ 3, so <b>x = 2</b>"], marks=10,
  ok=(3 * 4 % 5 == 2 and 3 * 2 % 5 == 1 and [t for t in range(1, 5) if 4 * t % 5 == 3] == [2]
      and all(i * j % 5 == [[1, 2, 3, 4], [2, 4, 1, 3], [3, 1, 4, 2], [4, 3, 2, 1]][i - 1][j - 1] for i in range(1, 5) for j in range(1, 5))))
T("(a) Kofi takes a tablet every 8 hours, starting at 6:00 a.m. on Monday. On what day and at what time does he take the 20th tablet?<br>(b) Evaluate (5 + 6) × 4 in modulo 7.<br>(c) Find all values of x, 0 ≤ x < 7, such that x^2 ≡ 2 (mod 7).",
  ["(a) Between the 1st and 20th tablets there are 19 intervals.",
   "19 × 8 = 152 hours = 6 × 24 + 8 = 6 days 8 hours",
   "Monday 6:00 a.m. + 6 days = Sunday 6:00 a.m.; + 8 hours = <b>Sunday, 2:00 p.m.</b>",
   "(b) 5 + 6 = 11 ≡ 4 (mod 7); 4 × 4 = 16 ≡ <b>2</b> (mod 7)",
   "(c) Squares mod 7: 0→0, 1→1, 2→4, 3→2, 4→2, 5→4, 6→1",
   "So <b>x = 3 or x = 4</b>"], marks=10,
  ok=(19 * 8 == 152 and (5 + 6) * 4 % 7 == 2 and [t for t in range(7) if t * t % 7 == 2] == [3, 4]))

# ------------------------------------------------------------------ 3
topic("approx", "Fractions, decimals & approximation", S, [
    "To divide by a fraction, multiply by its reciprocal.",
    "Standard form: A × 10^n with 1 ≤ A < 10.",
    "Significant figures start from the first non-zero digit; decimal places count from the point.",
    "Percentage error = (error ÷ actual value) × 100%.",
    "Recurring decimal: 0.ab ab ab… = ab/99.",
])
O(f"Evaluate 2{F(1,3)} ÷ 1{F(3,4)}.", [f"1{F(1,3)}", F(3, 4), f"4{F(1,12)}", f"1{F(1,4)}"],
  [f"2{F(1,3)} = {F(7,3)} and 1{F(3,4)} = {F(7,4)}",
   f"{F(7,3)} × {F(4,7)} = {F(4,3)} = 1{F(1,3)}"],
  v=Fr(7, 3) / Fr(7, 4), nv=[Fr(4, 3), Fr(3, 4), Fr(49, 12), Fr(5, 4)])
O("Express 0.0004072 in standard form.",
  ["4.072 × 10^{-4}", "4.072 × 10^{-3}", "4.072 × 10^{-5}", "4.072 × 10^{4}"],
  ["Move the decimal point 4 places to the right to get 4.072.", "So 0.0004072 = 4.072 × 10^{-4}"],
  v=0.0004072, nv=[4.072e-4, 4.072e-3, 4.072e-5, 4.072e4])
O("Round 0.0045678 to three significant figures.", ["0.00457", "0.005", "0.0046", "0.004568"],
  ["The first significant figure is 4; the first three are 4, 5, 6.",
   "The next digit is 7 (≥ 5), so round 6 up to 7.", "0.0045678 ≈ 0.00457"],
  v=float(f"{0.0045678:.3g}"))
O(f"Simplify {F('0.0018 × 0.24', '0.36')}.", ["0.0012", "0.012", "0.00012", "0.12"],
  ["0.0018 × 0.24 = 0.000432", "0.000432 ÷ 0.36 = 0.0012"], v=0.0018 * 0.24 / 0.36)
O("Express 0.272727… (0.27 recurring) as a fraction in its lowest terms.",
  [F(3, 11), F(27, 100), F(2, 7), F(11, 40)],
  ["Let r = 0.2727…; then 100r = 27.2727…", f"100r − r = 27 ⇒ 99r = 27 ⇒ r = {F(27,99)} = {F(3,11)}"],
  v=Fr(27, 99), nv=[Fr(3, 11), Fr(27, 100), Fr(2, 7), Fr(11, 40)])
O(f"A man spent {F(2,5)} of his money on rent and {F(1,3)} of the remainder on food. What fraction of his money is left?",
  [F(2, 5), F(4, 15), F(1, 5), F(3, 5)],
  [f"After rent: 1 − {F(2,5)} = {F(3,5)}", f"Food: {F(1,3)} × {F(3,5)} = {F(1,5)}",
   f"Left: {F(3,5)} − {F(1,5)} = {F(2,5)}"],
  v=1 - Fr(2, 5) - Fr(1, 3) * Fr(3, 5), nv=[Fr(2, 5), Fr(4, 15), Fr(1, 5), Fr(3, 5)])
T(f"(a) Without using a calculator, evaluate (3{F(1,4)} − 1{F(5,6)}) ÷ 2{F(5,6)}.<br>(b) By rounding each number to one significant figure, estimate {F('49.8 × 0.0312', '0.195')}.<br>(c) Find the exact value of the expression in (b), correct to three significant figures.",
  [f"(a) 3{F(1,4)} − 1{F(5,6)} = {F(13,4)} − {F(11,6)} = {F(39,12)} − {F(22,12)} = {F(17,12)}",
   f"{F(17,12)} ÷ {F(17,6)} = {F(17,12)} × {F(6,17)} = <b>{F(1,2)}</b>",
   f"(b) 49.8 ≈ 50, 0.0312 ≈ 0.03, 0.195 ≈ 0.2 ⇒ {F('50 × 0.03', '0.2')} = {F('1.5', '0.2')} = <b>7.5</b>",
   "(c) 49.8 × 0.0312 = 1.55376; 1.55376 ÷ 0.195 = 7.968", "≈ <b>7.97</b> (3 s.f.)"], marks=10,
  ok=((Fr(13, 4) - Fr(11, 6)) / Fr(17, 6) == Fr(1, 2) and close(49.8 * 0.0312 / 0.195, 7.968)))
T(f"(a) A student measured the length of a rod as 4.8 cm instead of 5.0 cm. Calculate the percentage error.<br>(b) Evaluate {F('(6.3 × 10^5) × (4 × 10^{-2})', '1.8 × 10^3')}, leaving your answer in standard form.<br>(c) A farmer gave {F(3,8)} of his land to his first son and {F(2,5)} of the remainder to his second son. He kept the rest, which was 15 hectares. What was the size of the whole farm?",
  [f"(a) Error = 5.0 − 4.8 = 0.2 cm; percentage error = {F('0.2', '5.0')} × 100% = <b>4%</b>",
   f"(b) Numerator: 6.3 × 4 × 10^{{5 − 2}} = 25.2 × 10^3",
   f"{F('25.2 × 10^3', '1.8 × 10^3')} = 14 = <b>1.4 × 10^1</b>",
   f"(c) Remainder after first son: 1 − {F(3,8)} = {F(5,8)}",
   f"Second son: {F(2,5)} × {F(5,8)} = {F(1,4)}",
   f"Kept: {F(5,8)} − {F(1,4)} = {F(3,8)} of the farm",
   f"{F(3,8)} × T = 15 ⇒ T = 15 × {F(8,3)} = <b>40 hectares</b>"], marks=10,
  ok=(close(0.2 / 5 * 100, 4) and close(6.3e5 * 4e-2 / 1.8e3, 14) and (1 - Fr(3, 8) - Fr(2, 5) * Fr(5, 8)) * 40 == 15))

# ------------------------------------------------------------------ 4
topic("indices", "Indices", S, [
    "a^m × a^n = a^{m+n};  a^m ÷ a^n = a^{m−n};  (a^m)^n = a^{mn}",
    "a^0 = 1;  a^{−n} = 1/a^n;  a^{m/n} = (ⁿ√a)^m",
    "For exponential equations, write both sides with the same base and equate the powers.",
    "Equations like 5^{2x} − 6(5^x) + 5 = 0 become quadratics: let y = 5^x.",
])
O("Simplify 27^{2/3} × 16^{-1/4}.", [F(9, 2), "18", "6", F(3, 2)],
  ["27^{2/3} = (∛27)^2 = 3^2 = 9", f"16^{{-1/4}} = {F(1, '16^{1/4}')} = {F(1,2)}", f"9 × {F(1,2)} = {F(9,2)}"],
  v=Fr(9, 2), nv=[Fr(9, 2), 18, 6, Fr(3, 2)]) if close(27 ** (2 / 3) * 16 ** (-1 / 4), 4.5) else FAIL()
O("Solve 2^{x + 1} = 32.", ["x = 4", "x = 5", "x = 3", "x = 6"],
  ["32 = 2^5, so 2^{x+1} = 2^5", "x + 1 = 5 ⇒ x = 4"], v=4, nv=[4, 5, 3, 6])
O(f"Simplify (a^3 b^{{-2}})^2 ÷ (a^4 b^{{-1}}).", [F("a^2", "b^3"), "a^2 b^3", F("a^{10}", "b^5"), F("a", "b^3")],
  ["(a^3 b^{-2})^2 = a^6 b^{-4}", "a^6 b^{-4} ÷ a^4 b^{-1} = a^{6−4} b^{−4−(−1)} = a^2 b^{-3}",
   f"= {F('a^2', 'b^3')}"],
  v=(a ** 3 * b ** -2) ** 2 / (a ** 4 * b ** -1), nv=["a**2/b**3", "a**2*b**3", "a**10/b**5", "a/b**3"])
O(f"Evaluate ({F(1,8)})^{{-2/3}}.", ["4", F(1, 4), "−4", "16"],
  [f"({F(1,8)})^{{-2/3}} = 8^{{2/3}}", "= (∛8)^2 = 2^2 = 4"],
  v=Fr(1, 8) ** Fr(-2, 3) if False else 4, nv=[4, Fr(1, 4), -4, 16]) if close((1 / 8) ** (-2 / 3), 4) else FAIL()
O("Solve 9^x = 27^{x − 1}.", ["x = 3", "x = −3", "x = 1", "x = 2"],
  ["9^x = 3^{2x} and 27^{x−1} = 3^{3x−3}", "2x = 3x − 3 ⇒ x = 3"],
  v=3, nv=[3, -3, 1, 2]) if [t for t in [3, -3, 1, 2] if 9 ** t == 27 ** (t - 1)] == [3] else FAIL()
O("Solve 5^{2x} − 6(5^x) + 5 = 0.", ["x = 0 or x = 1", "x = 1 or x = 5", "x = −1 or x = 0", "x = 0 only"],
  ["Let y = 5^x. Then y^2 − 6y + 5 = 0", "(y − 1)(y − 5) = 0 ⇒ y = 1 or y = 5",
   "5^x = 1 ⇒ x = 0;  5^x = 5 ⇒ x = 1"],
  ok=sorted(sp.solve(5 ** (2 * x) - 6 * 5 ** x + 5, x)) == [0, 1])
T(f"(a) Simplify {F('81^{3/4} × 32^{-2/5}', '125^{1/3}')}.<br>(b) Solve 3^{{2x + 1}} − 28(3^x) + 9 = 0.",
  ["(a) 81^{3/4} = (⁴√81)^3 = 3^3 = 27",
   f"32^{{-2/5}} = {F(1, '(⁵√32)^2')} = {F(1,4)}", "125^{1/3} = 5",
   f"{F(f'27 × {F(1,4)}', 5)} = <b>{F(27,20)}</b>",
   "(b) 3^{2x+1} = 3 × (3^x)^2. Let y = 3^x:", "3y^2 − 28y + 9 = 0 ⇒ (3y − 1)(y − 9) = 0",
   f"y = {F(1,3)} ⇒ 3^x = 3^{{-1}} ⇒ <b>x = −1</b>", "y = 9 ⇒ 3^x = 3^2 ⇒ <b>x = 2</b>"], marks=10,
  ok=(close(81 ** .75 * 32 ** -.4 / 125 ** (1 / 3), 27 / 20) and sorted(sp.solve(3 ** (2 * x + 1) - 28 * 3 ** x + 9, x)) == [-1, 2]))
T(f"(a) Solve ({F(1,16)})^x = 64^{{x − 3}}.<br>(b) Expand and simplify (x^{{1/2}} + x^{{-1/2}})^2.<br>(c) Solve the simultaneous equations 2^x × 4^y = 64 and 3^x ÷ 9^y = {F(1,3)}.",
  [f"(a) ({F(1,16)})^x = 2^{{-4x}} and 64^{{x−3}} = 2^{{6x−18}}",
   f"−4x = 6x − 18 ⇒ 10x = 18 ⇒ <b>x = {F(9,5)}</b> (= 1.8)",
   "(b) (x^{1/2})^2 + 2(x^{1/2})(x^{-1/2}) + (x^{-1/2})^2",
   f"= <b>x + 2 + {F(1,'x')}</b>",
   "(c) 2^x × 2^{2y} = 2^6 ⇒ x + 2y = 6 … (i)",
   "3^x ÷ 3^{2y} = 3^{-1} ⇒ x − 2y = −1 … (ii)",
   f"(i) + (ii): 2x = 5 ⇒ <b>x = {F(5,2)}</b>; then 2y = 6 − {F(5,2)} = {F(7,2)} ⇒ <b>y = {F(7,4)}</b>"], marks=12,
  ok=(sp.solve(-4 * x - (6 * x - 18), x) == [sp.Rational(9, 5)]
      and sp.expand((sp.sqrt(x) + 1 / sp.sqrt(x)) ** 2) == x + 2 + 1 / x
      and sp.solve([x + 2 * y - 6, x - 2 * y + 1], [x, y]) == {x: sp.Rational(5, 2), y: sp.Rational(7, 4)}))

# ------------------------------------------------------------------ 5
topic("logs", "Logarithms", S, [
    "log_a x = n means a^n = x.",
    "log(xy) = log x + log y;  log(x/y) = log x − log y;  log x^n = n log x",
    "log_a a = 1 and log_a 1 = 0.",
    "Change of base: log_a x = log x ÷ log a.",
    "Always check that solutions keep every log argument positive.",
])
O("Evaluate log_{2} 32 − log_{3} 27.", ["2", "1", "3", "8"],
  ["log_{2} 32 = 5 since 2^5 = 32", "log_{3} 27 = 3 since 3^3 = 27", "5 − 3 = 2"],
  v=round(math.log2(32) - math.log(27, 3)))
O("Simplify log_{10} 8 + log_{10} 5 − log_{10} 4.", ["1", "log_{10} 9", "0", "2"],
  [f"log_{{10}} ({F('8 × 5', 4)}) = log_{{10}} 10 = 1"],
  v=1, nv=[1, math.log10(9), 0, 2]) if close(math.log10(8) + math.log10(5) - math.log10(4), 1) else FAIL()
O("Solve log_{x} 81 = 4.", ["x = 3", "x = 9", "x = 4", "x = 27"],
  ["x^4 = 81 = 3^4", "x = 3"], v=3, nv=[3, 9, 4, 27]) if [t for t in [3, 9, 4, 27] if t ** 4 == 81] == [3] else FAIL()
O("Given that log_{10} 2 = 0.3010 and log_{10} 3 = 0.4771, find log_{10} 18.",
  ["1.2552", "0.7781", "1.0791", "1.5563"],
  ["18 = 2 × 3^2", "log 18 = log 2 + 2 log 3 = 0.3010 + 2(0.4771)", "= 0.3010 + 0.9542 = 1.2552"],
  v=0.3010 + 2 * 0.4771, tol=1e-6)
O("Solve log_{3}(x + 5) − log_{3}(x − 1) = 2.", [F(7, 4), F(4, 7), "2", F(7, 2)],
  [f"log_{{3}} {F('x + 5', 'x − 1')} = 2 ⇒ {F('x + 5', 'x − 1')} = 3^2 = 9",
   f"x + 5 = 9x − 9 ⇒ 8x = 14 ⇒ x = {F(7,4)}",
   f"Check: x − 1 = {F(3,4)} > 0, so the solution is valid."],
  v=sp.solve((x + 5) - 9 * (x - 1), x)[0], nv=["7/4", "4/7", "2", "7/2"])
O("Express 2 log a − ½ log b + log c as a single logarithm.",
  [f"log {F('a^2 c', '√b')}", f"log {F('2ac', '√b')}", f"log (a^2 c√b)", f"log {F('a^2', 'c√b')}"],
  ["2 log a = log a^2 and ½ log b = log √b",
   f"log a^2 − log √b + log c = log {F('a^2 × c', '√b')}"],
  ok=sp.simplify(sp.expand_log(sp.log(a ** 2 * c / sp.sqrt(b)), force=True) - (2 * sp.log(a) - sp.log(b) / 2 + sp.log(c))) == 0)
T(f"(a) Without using tables, evaluate {F('log 8 − log 2', 'log 32 − log 4')}.<br>(b) Solve log_{{10}}(x^2 + 6) − log_{{10}} x = log_{{10}} 5.<br>(c) Given log 2 = 0.3010 and log 3 = 0.4771, evaluate log 7.2 without tables.",
  [f"(a) log 8 − log 2 = log 4 = 2 log 2;  log 32 − log 4 = log 8 = 3 log 2",
   f"{F('2 log 2', '3 log 2')} = <b>{F(2,3)}</b>",
   f"(b) log {F('x^2 + 6', 'x')} = log 5 ⇒ x^2 + 6 = 5x",
   "x^2 − 5x + 6 = 0 ⇒ (x − 2)(x − 3) = 0 ⇒ <b>x = 2 or x = 3</b> (both positive, so both valid)",
   f"(c) 7.2 = {F(72,10)} = {F('2^3 × 3^2', 10)}",
   "log 7.2 = 3 log 2 + 2 log 3 − log 10 = 0.9030 + 0.9542 − 1 = <b>0.8572</b>"], marks=12,
  ok=(close((math.log10(8) - math.log10(2)) / (math.log10(32) - math.log10(4)), 2 / 3)
      and sorted(sp.solve(x ** 2 + 6 - 5 * x, x)) == [2, 3] and close(3 * .3010 + 2 * .4771 - 1, .8572)))
T("(a) Using logarithms, solve 2^x = 7, giving your answer correct to two decimal places. [log 2 = 0.3010, log 7 = 0.8451]<br>(b) Solve log_{3} x + log_{9} x = 3/2.<br>(c) Show that log_{a} b × log_{b} a = 1.",
  [f"(a) x log 2 = log 7 ⇒ x = {F('0.8451', '0.3010')} = 2.8076… ≈ <b>2.81</b>",
   f"(b) log_{{9}} x = {F('log_{3} x', 'log_{3} 9')} = ½ log_{{3}} x",
   f"log_{{3}} x + ½ log_{{3}} x = {F(3,2)} ⇒ {F(3,2)} log_{{3}} x = {F(3,2)} ⇒ log_{{3}} x = 1 ⇒ <b>x = 3</b>",
   f"(c) By change of base, log_{{a}} b = {F('log b', 'log a')} and log_{{b}} a = {F('log a', 'log b')}",
   f"Product = {F('log b', 'log a')} × {F('log a', 'log b')} = 1 ∎"], marks=10,
  ok=(round(.8451 / .3010, 2) == 2.81 and close(math.log(3, 3) + math.log(3, 9), 1.5)))

# ------------------------------------------------------------------ 6
topic("surds", "Surds", S, [
    "√(ab) = √a × √b;  simplify by pulling out square factors: √75 = √25 × √3 = 5√3.",
    "Only like surds can be added: 5√3 − 3√3 = 2√3.",
    "(√a + √b)(√a − √b) = a − b — use the conjugate to rationalise.",
    "a/√b = a√b / b.",
])
O("Simplify √75 − √27.", ["2√3", "3√2", "4√3", "8√3"],
  ["√75 = √(25 × 3) = 5√3", "√27 = √(9 × 3) = 3√3", "5√3 − 3√3 = 2√3"],
  v=sp.sqrt(75) - sp.sqrt(27), nv=["2*sqrt(3)", "3*sqrt(2)", "4*sqrt(3)", "8*sqrt(3)"])
O(f"Rationalise {F(6, '√3')}.", ["2√3", "3√2", "6√3", F("√3", 2)],
  [f"{F(6,'√3')} × {F('√3','√3')} = {F('6√3', 3)} = 2√3"],
  v=6 / sp.sqrt(3), nv=["2*sqrt(3)", "3*sqrt(2)", "6*sqrt(3)", "sqrt(3)/2"])
O("Simplify (2√3 + √2)(2√3 − √2).", ["10", "14", "12 − √6", "8"],
  ["This is (p + q)(p − q) = p^2 − q^2", "(2√3)^2 − (√2)^2 = 12 − 2 = 10"],
  v=sp.expand((2 * sp.sqrt(3) + sp.sqrt(2)) * (2 * sp.sqrt(3) - sp.sqrt(2))), nv=["10", "14", "12-sqrt(6)", "8"])
O(f"Rationalise the denominator of {F(1, '√5 − √3')}.",
  [F("√5 + √3", 2), F("√5 − √3", 2), "√5 + √3", F("√5 + √3", 8)],
  [f"Multiply by the conjugate: {F('√5 + √3', '(√5 − √3)(√5 + √3)')}", f"Denominator = 5 − 3 = 2 ⇒ {F('√5 + √3', 2)}"],
  v=1 / (sp.sqrt(5) - sp.sqrt(3)), nv=["(sqrt(5)+sqrt(3))/2", "(sqrt(5)-sqrt(3))/2", "sqrt(5)+sqrt(3)", "(sqrt(5)+sqrt(3))/8"])
O("Simplify √50 + √18 − √8.", ["6√2", "10√2", "2√15", "4√2"],
  ["√50 = 5√2, √18 = 3√2, √8 = 2√2", "5√2 + 3√2 − 2√2 = 6√2"],
  v=sp.sqrt(50) + sp.sqrt(18) - sp.sqrt(8), nv=["6*sqrt(2)", "10*sqrt(2)", "2*sqrt(15)", "4*sqrt(2)"])
O("If (√3 + 1)^2 = p + q√3, find p and q.", ["p = 4, q = 2", "p = 3, q = 1", "p = 4, q = 1", "p = 2, q = 2"],
  ["(√3 + 1)^2 = 3 + 2√3 + 1 = 4 + 2√3", "So p = 4 and q = 2"],
  ok=sp.expand((sp.sqrt(3) + 1) ** 2) == 4 + 2 * sp.sqrt(3))
T(f"(a) Simplify {F('3√2 − 2√3', '3√2 + 2√3')}, giving your answer in the form p − q√6.<br>(b) Given that x = 2 + √3, find the value of x + {F(1,'x')}.",
  [f"(a) Multiply top and bottom by (3√2 − 2√3):",
   "Numerator: (3√2 − 2√3)^2 = 18 − 12√6 + 12 = 30 − 12√6",
   "Denominator: (3√2)^2 − (2√3)^2 = 18 − 12 = 6",
   f"{F('30 − 12√6', 6)} = <b>5 − 2√6</b>",
   f"(b) {F(1,'x')} = {F(1,'2 + √3')} × {F('2 − √3','2 − √3')} = {F('2 − √3','4 − 3')} = 2 − √3",
   "x + 1/x = (2 + √3) + (2 − √3) = <b>4</b>"], marks=10,
  ok=(sp.simplify((3 * sp.sqrt(2) - 2 * sp.sqrt(3)) / (3 * sp.sqrt(2) + 2 * sp.sqrt(3)) - (5 - 2 * sp.sqrt(6))) == 0
      and sp.simplify((2 + sp.sqrt(3)) + 1 / (2 + sp.sqrt(3)) - 4) == 0))
T(f"(a) Simplify {F('√12 × √18', '√24')}.<br>(b) Evaluate (√7 + √2)^2 − (√7 − √2)^2.<br>(c) Express {F(4,'2 + √2')} in the form p + q√2.",
  [f"(a) {F('√(12 × 18)', '√24')} = √{F(216,24)} = √9 = <b>3</b>",
   "(b) (9 + 2√14) − (9 − 2√14) = <b>4√14</b>",
   f"(c) {F(4,'2 + √2')} × {F('2 − √2','2 − √2')} = {F('4(2 − √2)', '4 − 2')} = 2(2 − √2) = <b>4 − 2√2</b>"], marks=9,
  ok=(sp.simplify(sp.sqrt(12) * sp.sqrt(18) / sp.sqrt(24) - 3) == 0
      and sp.simplify((sp.sqrt(7) + sp.sqrt(2)) ** 2 - (sp.sqrt(7) - sp.sqrt(2)) ** 2 - 4 * sp.sqrt(14)) == 0
      and sp.simplify(4 / (2 + sp.sqrt(2)) - (4 - 2 * sp.sqrt(2))) == 0))

# ------------------------------------------------------------------ 7
topic("seq", "Sequences & series", S, [
    "AP: T_n = a + (n − 1)d;  S_n = n/2 [2a + (n − 1)d]",
    "GP: T_n = ar^{n−1};  S_n = a(r^n − 1)/(r − 1)",
    "Sum to infinity (|r| < 1): S_∞ = a/(1 − r)",
    "If x, y, z are consecutive AP terms, 2y = x + z; for GP, y^2 = xz.",
])
O("Find the nth term of the sequence 3, 7, 11, 15, …", ["4n − 1", "4n + 3", "3n + 1", "n + 4"],
  ["a = 3, d = 4", "T_n = 3 + (n − 1)4 = 4n − 1"],
  v=3 + (n - 1) * 4, nv=["4*n-1", "4*n+3", "3*n+1", "n+4"])
O("Find the 10th term of the arithmetic progression 5, 8, 11, …", ["32", "35", "30", "29"],
  ["a = 5, d = 3", "T_{10} = 5 + 9 × 3 = 32"], v=5 + 9 * 3)
O("Find the sum of the first 20 terms of the AP 2, 5, 8, …", ["610", "590", "620", "1220"],
  [f"S_{{20}} = {F(20,2)}[2(2) + 19(3)]", "= 10 × 61 = 610"], v=sum(2 + 3 * i for i in range(20)))
O("Find the 6th term of the geometric progression 2, 6, 18, …", ["486", "162", "1458", "243"],
  ["a = 2, r = 3", "T_6 = 2 × 3^5 = 2 × 243 = 486"], v=2 * 3 ** 5)
O("Find the sum to infinity of the GP 12, 6, 3, …", ["24", "18", "21", "36"],
  [f"a = 12, r = {F(1,2)}", f"S_∞ = {F(12, f'1 − {F(1,2)}')} = 24"], v=12 / (1 - .5))
O("The terms x − 1, 2x and 4x − 3 are consecutive terms of an AP. Find x.", ["4", "2", "3", "−4"],
  ["For an AP, 2(middle) = first + last", "2(2x) = (x − 1) + (4x − 3)", "4x = 5x − 4 ⇒ x = 4"],
  v=sp.solve(2 * (2 * x) - ((x - 1) + (4 * x - 3)), x)[0])
T("The 3rd term of an arithmetic progression is 11 and the 8th term is 31.<br>(a) Find the first term and the common difference.<br>(b) Find the sum of the first 15 terms.<br>(c) Which term of the progression is 99?",
  ["(a) a + 2d = 11 … (i);  a + 7d = 31 … (ii)",
   "(ii) − (i): 5d = 20 ⇒ <b>d = 4</b>; then a = 11 − 8 = <b>3</b>",
   f"(b) S_{{15}} = {F(15,2)}[2(3) + 14(4)] = {F(15,2)} × 62 = <b>465</b>",
   "(c) 3 + (n − 1)4 = 99 ⇒ 4(n − 1) = 96 ⇒ n − 1 = 24 ⇒ <b>25th term</b>"], marks=10,
  ok=(3 + 2 * 4 == 11 and 3 + 7 * 4 == 31 and sum(3 + 4 * i for i in range(15)) == 465 and 3 + 24 * 4 == 99))
T("The second term of a GP is 6 and the fifth term is 162.<br>(a) Find the common ratio and the first term.<br>(b) Find the sum of the first six terms.<br>(c) A worker's starting salary is GH₵ 24,000 a year and it rises by 5% each year. Find the total amount earned in the first four years.",
  [f"(a) ar = 6 and ar^4 = 162 ⇒ r^3 = {F(162,6)} = 27 ⇒ <b>r = 3</b>; a = 6 ÷ 3 = <b>2</b>",
   f"(b) S_6 = {F('2(3^6 − 1)', '3 − 1')} = 3^6 − 1 = <b>728</b>",
   "(c) The salaries form a GP with a = 24,000 and r = 1.05",
   f"S_4 = {F('24000(1.05^4 − 1)', '1.05 − 1')} = {F('24000 × 0.21550625', '0.05')}",
   "= <b>GH₵ 103,443.00</b>"], marks=12,
  ok=(2 * 3 == 6 and 2 * 3 ** 4 == 162 and sum(2 * 3 ** i for i in range(6)) == 728
      and close(sum(24000 * 1.05 ** i for i in range(4)), 103443.0, 1e-3)))

# ------------------------------------------------------------------ 8
topic("sets", "Sets", S, [
    "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)",
    "Three sets: n(A∪B∪C) = ΣnA − Σn(pairs) + n(A∩B∩C)",
    "A set with n elements has 2^n subsets.",
    "A′ (complement) contains the elements of U that are not in A.",
    "In Venn diagram problems, fill in the centre (all three) first and work outwards.",
])
O("If n(A) = 15, n(B) = 12 and n(A ∩ B) = 5, find n(A ∪ B).", ["22", "27", "17", "32"],
  ["n(A ∪ B) = 15 + 12 − 5 = 22"], v=15 + 12 - 5)
O("In a class of 40 students, 25 study French, 20 study Twi and 8 study neither. How many study both?",
  ["13", "5", "12", "8"],
  ["Students studying at least one = 40 − 8 = 32", "32 = 25 + 20 − x ⇒ x = 13"], v=25 + 20 - (40 - 8))
O("How many subsets does the set {a, b, c, d} have?", ["16", "8", "15", "4"],
  ["Number of subsets = 2^n = 2^4 = 16"], v=2 ** 4)
O("If U = {1, 2, 3, …, 10} and P = {prime numbers in U}, find P′.",
  ["{1, 4, 6, 8, 9, 10}", "{2, 3, 5, 7}", "{4, 6, 8, 9, 10}", "{1, 4, 6, 8, 10}"],
  ["P = {2, 3, 5, 7}", "P′ = the elements of U not in P = {1, 4, 6, 8, 9, 10}", "Remember that 1 is not a prime number."],
  ok=sorted(set(range(1, 11)) - {2, 3, 5, 7}) == [1, 4, 6, 8, 9, 10])
O("If A = {x : 2 < x ≤ 7, x is an integer}, find n(A).", ["5", "6", "4", "7"],
  ["A = {3, 4, 5, 6, 7}", "n(A) = 5"], v=len([t for t in range(-10, 20) if 2 < t <= 7]))
T("In a survey of 100 students, 45 like Mathematics (M), 40 like English (E) and 38 like Science (S). 15 like M and E, 12 like E and S, 14 like M and S, and 5 like all three subjects.<br>(a) Draw a Venn diagram to show this information.<br>(b) How many students like none of the subjects?<br>(c) How many like Mathematics only?<br>(d) How many like exactly two subjects?",
  ["(a) Centre (all three) = 5. M∩E only = 15 − 5 = 10; E∩S only = 12 − 5 = 7; M∩S only = 14 − 5 = 9.",
   "M only = 45 − 10 − 9 − 5 = 21; E only = 40 − 10 − 7 − 5 = 18; S only = 38 − 7 − 9 − 5 = 17.",
   "(b) Total in the circles = 21 + 18 + 17 + 10 + 7 + 9 + 5 = 87 ⇒ none = 100 − 87 = <b>13</b>",
   "(c) Mathematics only = <b>21</b>",
   "(d) Exactly two = 10 + 7 + 9 = <b>26</b>"], marks=12,
  ok=(21 + 18 + 17 + 10 + 7 + 9 + 5 == 45 + 40 + 38 - 15 - 12 - 14 + 5 == 87 and 45 - 10 - 9 - 5 == 21))
T("U = {x : 1 ≤ x ≤ 15, x is an integer}, A = {multiples of 3} and B = {factors of 12}.<br>(a) List the elements of A and B.<br>(b) Find A ∩ B and A ∪ B.<br>(c) Find (A ∪ B)′ and n(A ∪ B)′.",
  ["(a) A = {3, 6, 9, 12, 15};  B = {1, 2, 3, 4, 6, 12}",
   "(b) A ∩ B = <b>{3, 6, 12}</b>;  A ∪ B = <b>{1, 2, 3, 4, 6, 9, 12, 15}</b>",
   "(c) (A ∪ B)′ = <b>{5, 7, 8, 10, 11, 13, 14}</b>, so n(A ∪ B)′ = <b>7</b>"], marks=9,
  ok=(lambda A, B: sorted(A & B) == [3, 6, 12] and sorted(A | B) == [1, 2, 3, 4, 6, 9, 12, 15]
      and sorted(set(range(1, 16)) - (A | B)) == [5, 7, 8, 10, 11, 13, 14])(
      {t for t in range(1, 16) if t % 3 == 0}, {t for t in range(1, 16) if 12 % t == 0}))

# ------------------------------------------------------------------ 9
topic("logic", "Logical reasoning", S, [
    "Negation of 'All X are Y' is 'Some X are not Y'.",
    "p → q is false only when p is true and q is false.",
    "Converse: q → p.  Inverse: ~p → ~q.  Contrapositive: ~q → ~p (equivalent to p → q).",
    "Use Venn diagrams to test whether a conclusion must follow.",
])
O("What is the contrapositive of the statement 'If it rains, the ground is wet'?",
  ["If the ground is not wet, then it did not rain.", "If the ground is wet, then it rained.",
   "If it does not rain, the ground is not wet.", "It rains and the ground is not wet."],
  ["For p → q, the contrapositive is ~q → ~p.", "p: it rains; q: the ground is wet.",
   "~q → ~p: If the ground is not wet, then it did not rain."])
O("What is the negation of the statement 'All the students passed'?",
  ["Some students did not pass.", "No student passed.", "All the students failed.", "Some students passed."],
  ["The negation of 'All X are Y' is 'At least one X is not Y'.", "So: Some students did not pass."])
O("p: 'Kofi is tall' and q: 'Kofi is strong'. What does p ∧ ~q mean?",
  ["Kofi is tall but not strong.", "Kofi is tall or not strong.", "Kofi is not tall but strong.", "If Kofi is tall, he is not strong."],
  ["∧ means 'and'; ~q means 'Kofi is not strong'.", "p ∧ ~q: Kofi is tall and (but) not strong."])
O("If p is true and q is false, which of the following statements is true?", ["p ∨ q", "p ∧ q", "p → q", "~p"],
  ["p ∨ q: T or F = T ✓", "p ∧ q: T and F = F", "p → q: T → F = F", "~p = F"],
  ok=((True or False) and not (True and False) and not ((not True) or False) and not (not True)))
O("Premises: 'All farmers are hardworking' and 'Ama is a farmer'. Which conclusion is valid?",
  ["Ama is hardworking.", "All hardworking people are farmers.", "Ama is not hardworking.", "Some farmers are not hardworking."],
  ["The set of farmers lies inside the set of hardworking people.", "Ama is in the farmers set, so she must be in the hardworking set."])
T("(a) Copy and complete the truth table for p → q and ~q → ~p, and state what you notice.<br>(b) p: 'x is an even number'; q: 'x² is an even number'. Write down in words (i) p → q; (ii) its converse; (iii) its inverse.",
  ["(a) <table class=\"mt\"><tr><th>p</th><th>q</th><th>p → q</th><th>~q</th><th>~p</th><th>~q → ~p</th></tr>"
   "<tr><td>T</td><td>T</td><td>T</td><td>F</td><td>F</td><td>T</td></tr>"
   "<tr><td>T</td><td>F</td><td>F</td><td>T</td><td>F</td><td>F</td></tr>"
   "<tr><td>F</td><td>T</td><td>T</td><td>F</td><td>T</td><td>T</td></tr>"
   "<tr><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td><td>T</td></tr></table>",
   "The last column matches the p → q column, so <b>p → q ≡ ~q → ~p</b> (a statement and its contrapositive are equivalent).",
   "(b)(i) If x is an even number, then x² is an even number.",
   "(ii) Converse (q → p): If x² is an even number, then x is an even number.",
   "(iii) Inverse (~p → ~q): If x is not an even number, then x² is not an even number."], marks=10,
  ok=all(((not p) or q) == ((not (not q)) or (not p)) for p in (True, False) for q in (True, False)))
T("Consider the statements:<br>1. All good students attend classes.<br>2. Some people who attend classes are prefects.<br>3. Esi does not attend classes.<br>Using a Venn diagram, decide whether each conclusion is valid: (i) Esi is not a good student. (ii) Some prefects are good students. (iii) Esi is not a prefect.",
  ["Draw U; inside it, a circle C (attend classes); put G (good students) entirely inside C; draw P (prefects) overlapping C.",
   "Esi lies outside C.",
   "(i) G is inside C and Esi is outside C, so Esi cannot be in G. <b>Valid.</b>",
   "(ii) P overlaps C, but it need not overlap G. <b>Not valid</b> (it may be true, but it does not have to be).",
   "(iii) Part of P may lie outside C, so Esi could still be a prefect. <b>Not valid.</b>"], marks=9)

# ------------------------------------------------------------------ 10
topic("fin", "Ratio, percentages & financial arithmetic", S, [
    "Simple interest I = PRT/100;  amount A = P + I",
    "Compound interest A = P(1 + r/100)^n;  depreciation A = P(1 − r/100)^n",
    "Profit % = (profit ÷ cost price) × 100%",
    "Hire purchase price = deposit + total of the instalments",
    "To share in the ratio a : b : c, the parts are a/(a+b+c), b/(a+b+c), c/(a+b+c) of the whole.",
])
O("GH₵ 360 is shared in the ratio 2 : 3 : 4. What is the largest share?", ["GH₵ 160", "GH₵ 120", "GH₵ 80", "GH₵ 180"],
  ["Total parts = 2 + 3 + 4 = 9", f"Largest share = {F(4,9)} × 360 = GH₵ 160"], v=360 * 4 / 9)
O("A shirt marked GH₵ 250 is sold at a 12% discount. What is the selling price?", ["GH₵ 220", "GH₵ 238", "GH₵ 212", "GH₵ 280"],
  ["Discount = 12% of 250 = GH₵ 30", "Selling price = 250 − 30 = GH₵ 220"], v=250 * .88)
O("Find the simple interest on GH₵ 5,000 at 8% per annum for 3 years.", ["GH₵ 1,200", "GH₵ 1,500", "GH₵ 400", "GH₵ 6,200"],
  [f"I = {F('PRT', 100)} = {F('5000 × 8 × 3', 100)} = GH₵ 1,200"], v=5000 * 8 * 3 / 100)
O("GH₵ 2,000 is invested at 10% per annum compound interest. Find the amount after 2 years.",
  ["GH₵ 2,420", "GH₵ 2,400", "GH₵ 2,200", "GH₵ 2,440"],
  ["A = 2000(1.1)^2 = 2000 × 1.21 = GH₵ 2,420"], v=2000 * 1.1 ** 2)
O("A trader bought an item for GH₵ 80 and sold it for GH₵ 100. Find the percentage profit.", ["25%", "20%", "80%", "125%"],
  ["Profit = GH₵ 20", f"Profit % = {F(20,80)} × 100% = 25%"], tip="Percentage profit is always on the cost price, not the selling price.",
  v=20 / 80 * 100)
O("A car valued at GH₵ 120,000 depreciates by 15% each year. Find its value after 2 years.",
  ["GH₵ 86,700", "GH₵ 84,000", "GH₵ 102,000", "GH₵ 88,200"],
  ["Value = 120,000 × (0.85)^2", "= 120,000 × 0.7225 = GH₵ 86,700"], v=120000 * .85 ** 2)
O("5 men can do a piece of work in 12 days. How long will 4 men take, working at the same rate?",
  ["15 days", "9.6 days", "10 days", "16 days"],
  ["Total work = 5 × 12 = 60 man-days", "4 men: 60 ÷ 4 = 15 days"], v=5 * 12 / 4)
T("(a) The exchange rates are $1 = GH₵ 15.50 and £1 = GH₵ 19.80. Convert £250 to dollars, correct to the nearest cent.<br>(b) A salesman earns a basic salary of GH₵ 1,800 a month plus a 4% commission on all sales above GH₵ 20,000. In one month his sales were GH₵ 65,000. Find his total earnings.<br>(c) In a certain country, the first GH₵ 500 of monthly income is tax-free, the next GH₵ 1,000 is taxed at 10% and the rest at 17.5%. Find the tax on the salesman's earnings in (b).",
  ["(a) £250 = 250 × 19.80 = GH₵ 4,950", f"GH₵ 4,950 = {F(4950, '15.50')} = <b>$319.35</b>",
   "(b) Sales above GH₵ 20,000 = 65,000 − 20,000 = GH₵ 45,000",
   "Commission = 4% × 45,000 = GH₵ 1,800", "Total = 1,800 + 1,800 = <b>GH₵ 3,600</b>",
   "(c) First GH₵ 500: GH₵ 0", "Next GH₵ 1,000: 10% = GH₵ 100",
   "Rest: 3,600 − 1,500 = 2,100 at 17.5% = GH₵ 367.50", "Total tax = <b>GH₵ 467.50</b>"], marks=12,
  tip="The tax bands here are made up for practice. They are not Ghana's actual GRA rates.",
  ok=(round(250 * 19.8 / 15.5, 2) == 319.35 and 1800 + .04 * 45000 == 3600 and close(100 + .175 * 2100, 467.5)))
T("(a) A television costs GH₵ 4,800 cash. On hire purchase, a buyer pays a deposit of 25% of the cash price and 12 monthly instalments of GH₵ 350. Find (i) the hire purchase price; (ii) the extra amount paid as a percentage of the cash price.<br>(b) GH₵ 15,000 is invested at 12% per annum compound interest. Find the interest after 3 years.<br>(c) If x : y = 3 : 5 and y : z = 4 : 7, find x : y : z.",
  ["(a)(i) Deposit = 25% × 4,800 = GH₵ 1,200; instalments = 12 × 350 = GH₵ 4,200",
   "HP price = 1,200 + 4,200 = <b>GH₵ 5,400</b>",
   f"(ii) Extra = GH₵ 600; {F(600,4800)} × 100% = <b>12.5%</b>",
   "(b) A = 15,000 × 1.12^3 = 15,000 × 1.404928 = GH₵ 21,073.92",
   "Interest = 21,073.92 − 15,000 = <b>GH₵ 6,073.92</b>",
   "(c) Make y the same in both ratios: x : y = 12 : 20 and y : z = 20 : 35",
   "x : y : z = <b>12 : 20 : 35</b>"], marks=12,
  ok=(1200 + 12 * 350 == 5400 and close(600 / 4800 * 100, 12.5) and round(15000 * 1.12 ** 3 - 15000, 2) == 6073.92
      and Fr(12, 20) == Fr(3, 5) and Fr(20, 35) == Fr(4, 7)))

# ------------------------------------------------------------------ 11
topic("var", "Variation", S, [
    "Direct: y ∝ x ⇒ y = kx.   Inverse: y ∝ 1/x ⇒ y = k/x.",
    "Joint: y ∝ xz ⇒ y = kxz.   Partial: y = a + bx (two constants — you need two pairs of values).",
    "Always find k first, then write the full equation.",
])
O("y varies directly as x. If y = 12 when x = 4, find y when x = 7.", ["21", "28", "16", "3"],
  ["y = kx ⇒ 12 = 4k ⇒ k = 3", "y = 3 × 7 = 21"], v=12 / 4 * 7)
O("y varies inversely as the square of x. If y = 8 when x = 2, find y when x = 4.", ["2", "4", "16", "1"],
  [f"y = {F('k','x^2')} ⇒ 8 = {F('k',4)} ⇒ k = 32", f"y = {F(32,16)} = 2"], v=32 / 16)
O("P varies jointly as Q and R. P = 24 when Q = 2 and R = 3. Find P when Q = 5 and R = 4.", ["80", "60", "40", "96"],
  ["P = kQR ⇒ 24 = 6k ⇒ k = 4", "P = 4 × 5 × 4 = 80"], v=4 * 5 * 4)
O("T varies directly as the square root of L. If L is increased by 21%, find the percentage increase in T.",
  ["10%", "21%", "11%", "4.4%"],
  ["T = k√L. New L = 1.21L", "New T = k√(1.21L) = 1.1 × k√L", "So T increases by 10%"],
  v=(math.sqrt(1.21) - 1) * 100, tol=1e-6)
O("Which of these relationships shows that y varies inversely as x?", ["xy = k", "y = kx", "y = x + k", "y = kx^2"],
  [f"Inverse variation: y = {F('k','x')}, which rearranges to xy = k (a constant)."])
T("y is partly constant and partly varies as x. When x = 2, y = 11, and when x = 4, y = 19.<br>(a) Find the relationship between x and y.<br>(b) Find y when x = 6.<br>(c) Find x when y = 43.",
  ["(a) y = a + bx", "11 = a + 2b … (i);  19 = a + 4b … (ii)", "(ii) − (i): 8 = 2b ⇒ b = 4; a = 11 − 8 = 3",
   "<b>y = 3 + 4x</b>", "(b) y = 3 + 24 = <b>27</b>", "(c) 43 = 3 + 4x ⇒ 4x = 40 ⇒ <b>x = 10</b>"], marks=10,
  ok=(3 + 4 * 2 == 11 and 3 + 4 * 4 == 19 and 3 + 4 * 6 == 27 and 3 + 4 * 10 == 43))
T("F varies directly as m and inversely as the square of d. F = 12 when m = 3 and d = 2.<br>(a) Find the formula connecting F, m and d.<br>(b) Find F when m = 5 and d = 4.<br>(c) Find d when F = 4 and m = 9.",
  [f"(a) F = {F('km','d^2')} ⇒ 12 = {F('3k',4)} ⇒ k = 16 ⇒ <b>F = {F('16m','d^2')}</b>",
   f"(b) F = {F('16 × 5', 16)} = <b>5</b>",
   f"(c) 4 = {F('16 × 9','d^2')} ⇒ d^2 = {F(144,4)} = 36 ⇒ <b>d = 6</b>"], marks=9,
  ok=(16 * 3 / 4 == 12 and 16 * 5 / 16 == 5 and 16 * 9 / 36 == 4))

# ------------------------------------------------------------------ 12
topic("matrix", "Matrices & determinants", S, [
    "For A = [a b; c d], the determinant |A| = ad − bc.",
    "A^{-1} = (1/|A|)[d −b; −c a]; A has no inverse when |A| = 0 (a singular matrix).",
    "Multiply row × column: (AB)_{ij} = row i of A · column j of B.",
    "To solve ax + by = p, cx + dy = q, write X = A^{-1}B.",
])
O(f"Evaluate the determinant of {M([[3,2],[5,4]])}.", ["2", "22", "−2", "7"],
  ["|A| = (3)(4) − (2)(5) = 12 − 10 = 2"], v=sp.Matrix([[3, 2], [5, 4]]).det())
O(f"If A = {M([[1,2],[3,4]])} and B = {M([[2,0],[1,3]])}, find AB.",
  [M([[4, 6], [10, 12]]), M([[2, 0], [3, 12]]), M([[2, 4], [10, 14]]), M([[3, 2], [4, 7]])],
  ["Row 1: (1×2 + 2×1, 1×0 + 2×3) = (4, 6)", "Row 2: (3×2 + 4×1, 3×0 + 4×3) = (10, 12)"],
  v=sp.Matrix([[1, 2], [3, 4]]) * sp.Matrix([[2, 0], [1, 3]]),
  nv=[[[4, 6], [10, 12]], [[2, 0], [3, 12]], [[2, 4], [10, 14]], [[3, 2], [4, 7]]])
O(f"Find the value of x for which {M([['x',3],[2,4]])} is a singular matrix.", [F(3, 2), F(2, 3), "6", f"−{F(3,2)}"],
  [f"Singular ⇒ determinant = 0", f"4x − 6 = 0 ⇒ x = {F(3,2)}"],
  v=sp.solve(4 * x - 6, x)[0], nv=["3/2", "2/3", "6", "-3/2"])
O(f"Find the inverse of {M([[2,1],[5,3]])}.",
  [M([[3, -1], [-5, 2]]), M([[3, 1], [5, 2]]), M([[-3, 1], [5, -2]]), M([[2, -5], [-1, 3]])],
  ["|A| = 6 − 5 = 1", "Swap a and d, change the signs of b and c, then divide by |A| = 1."],
  v=sp.Matrix([[2, 1], [5, 3]]).inv(),
  nv=[[[3, -1], [-5, 2]], [[3, 1], [5, 2]], [[-3, 1], [5, -2]], [[2, -5], [-1, 3]]])
O(f"If A = {M([[3,1],[0,2]])} and B = {M([[1,4],[2,-1]])}, find 2A − B.",
  [M([[5, -2], [-2, 5]]), M([[5, 2], [-2, 3]]), M([[2, -3], [-2, 3]]), M([[7, 6], [2, 3]])],
  [f"2A = {M([[6,2],[0,4]])}", f"2A − B = {M([['6−1','2−4'],['0−2','4+1']])} = {M([[5,-2],[-2,5]])}"],
  v=2 * sp.Matrix([[3, 1], [0, 2]]) - sp.Matrix([[1, 4], [2, -1]]),
  nv=[[[5, -2], [-2, 5]], [[5, 2], [-2, 3]], [[2, -3], [-2, 3]], [[7, 6], [2, 3]]])
T("Use the matrix method to solve the simultaneous equations<br>2x + 3y = 13<br>x − y = −1",
  [f"Write {M([[2,3],[1,-1]])}{V('x','y')} = {V(13,-1)}",
   "|A| = (2)(−1) − (3)(1) = −5",
   f"A^{{-1}} = {F(1,-5)}{M([[-1,-3],[-1,2]])}",
   f"{V('x','y')} = {F(1,-5)}{M([[-1,-3],[-1,2]])}{V(13,-1)} = {F(1,-5)}{V('−13 + 3','−13 − 2')} = {F(1,-5)}{V(-10,-15)}",
   "<b>x = 2, y = 3</b>", "Check: 2(2) + 3(3) = 13 ✓ and 2 − 3 = −1 ✓"], marks=10,
  ok=(sp.Matrix([[2, 3], [1, -1]]).inv() * sp.Matrix([13, -1]) == sp.Matrix([2, 3])))
T(f"P = {M([[2,-1],[3,4]])} and Q = {M([[1,2],[0,-3]])}.<br>(a) Find PQ.<br>(b) Show that |PQ| = |P| × |Q|.<br>(c) Solve P{V('x','y')} = {V(1,18)}.",
  [f"(a) PQ = {M([['2 + 0','4 + 3'],['3 + 0','6 − 12']])} = <b>{M([[2,7],[3,-6]])}</b>",
   "(b) |PQ| = (2)(−6) − (7)(3) = −12 − 21 = −33",
   "|P| = 8 + 3 = 11;  |Q| = −3 − 0 = −3;  11 × (−3) = −33 ✓",
   "(c) 2x − y = 1 and 3x + 4y = 18", "From the first equation, y = 2x − 1 ⇒ 3x + 8x − 4 = 18 ⇒ 11x = 22",
   "<b>x = 2, y = 3</b>"], marks=10,
  ok=(lambda P, Q: P * Q == sp.Matrix([[2, 7], [3, -6]]) and (P * Q).det() == P.det() * Q.det() == -33
      and P.inv() * sp.Matrix([1, 18]) == sp.Matrix([2, 3]))(sp.Matrix([[2, -1], [3, 4]]), sp.Matrix([[1, 2], [0, -3]])))
