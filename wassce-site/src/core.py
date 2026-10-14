"""Question-bank helpers with built-in answer checking.

Every objective question is written with the CORRECT option first.
If `v` (the independently computed answer) is given, the checker confirms
that exactly one option equals it and that it is option 0. Options are then
shuffled deterministically so the key is spread across A-D.
"""
import re, zlib, random, math
from fractions import Fraction as Fr
import sympy as sp

x, y, a, b, n, k, c = sp.symbols('x y a b n k c')

TOPICS, QS = [], []
STATS = {"auto": 0, "ok": 0, "manual": 0}
_cur = None
_counter = {}


def topic(tid, name, section, notes):
    global _cur
    _cur = tid
    TOPICS.append({"id": tid, "name": name, "section": section, "notes": [fmt(s) for s in notes]})


# ---------- display helpers ----------
def F(p, q):
    return f'<span class="fr"><span>{p}</span><span>{q}</span></span>'


def R(s):
    return f'√<span class="ov">{s}</span>'


def M(rows):
    body = "".join("<span class=\"mr\">" + "".join(f"<span>{c}</span>" for c in r) + "</span>" for r in rows)
    return f'<span class="mx">{body}</span>'


def V(*vals):
    return M([[v] for v in vals])


def fmt(s):
    if not isinstance(s, str):
        return s
    s = re.sub(r'\^\{([^}]*)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'\^(−?[0-9A-Za-z]+)', r'<sup>\1</sup>', s)
    s = re.sub(r'_\{([^}]*)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'(?<=[\s(=,\[{>])-(?=[\d(√])', '−', s)
    return s


# ---------- checking ----------
def _num(o):
    t = re.sub(r'<[^>]+>', '', o)
    assert not re.search(r'[√π^]', t) and not re.search(r'\d\s*/\s*\d', t), f"option needs nv: {o}"
    t = t.replace('−', '-').replace(',', '')
    m = re.search(r'-?\d+(\.\d+)?', t)
    assert m, f"no number in option {o}"
    return float(m.group(0))


def _eq(p, v, tol):
    if isinstance(v, str):
        return p == v
    if isinstance(v, sp.MatrixBase):
        return sp.Matrix(p) == v
    if isinstance(v, tuple):
        return len(p) == len(v) and all(_eq(pi, vi, tol) for pi, vi in zip(p, v))
    if isinstance(p, str):
        p = sp.sympify(p)
    try:
        pv, vv = float(p), float(v)
        return abs(pv - vv) <= tol * max(1, abs(vv))
    except TypeError:
        return sp.simplify(sp.sympify(p) - sp.sympify(v)) == 0


def O(q, opts, sol, v=None, nv=None, ok=None, tol=1e-9, tip=None, fig=None):
    assert len(opts) == 4, q
    assert len(set(opts)) == 4, f"duplicate options: {q}"
    if v is not None:
        vals = nv if nv is not None else [_num(o) for o in opts]
        hits = [i for i, p in enumerate(vals) if _eq(p, v, tol)]
        assert hits == [0], f"CHECK FAILED ({hits}) in: {q}\n v={v} vals={vals}"
        STATS["auto"] += 1
    elif ok is not None:
        assert ok is True, f"CHECK FAILED (ok) in: {q}"
        STATS["ok"] += 1
    else:
        STATS["manual"] += 1
    order = list(range(4))
    random.Random(zlib.crc32(q.encode())).shuffle(order)
    _add({"type": "obj", "q": fmt(q), "opts": [fmt(opts[i]) for i in order], "ans": order.index(0),
          "sol": [fmt(s) for s in sol], "tip": fmt(tip), "fig": fig})


def T(q, sol, marks=None, tip=None, fig=None, ok=None):
    if ok is not None:
        assert ok is True, f"THEORY CHECK FAILED in: {q}"
        STATS["ok"] += 1
    _add({"type": "thy", "q": fmt(q), "sol": [fmt(s) for s in sol], "marks": marks, "tip": fmt(tip), "fig": fig})


def _add(d):
    _counter[_cur] = _counter.get(_cur, 0) + 1
    d["id"] = f"{_cur}-{_counter[_cur]}"
    d["topic"] = _cur
    QS.append(d)


def close(a_, b_, t=1e-6):
    return abs(a_ - b_) < t


# ---------- simple SVG graph ----------
def plot(fn, x0, x1, y0, y1, step=1, pts=None, lines=(), shade=None, w=320, h=260, label="y"):
    pad = 26
    sx = lambda X: pad + (X - x0) / (x1 - x0) * (w - 2 * pad)
    sy = lambda Y: h - pad - (Y - y0) / (y1 - y0) * (h - 2 * pad)
    g = []
    for X in range(math.ceil(x0), math.floor(x1) + 1, step):
        g.append(f'<line x1="{sx(X):.1f}" y1="{sy(y0):.1f}" x2="{sx(X):.1f}" y2="{sy(y1):.1f}" class="gg"/>')
        if X != 0:
            g.append(f'<text x="{sx(X):.1f}" y="{sy(0)+13 if y0 < 0 < y1 else h-pad+13:.1f}" class="gt" text-anchor="middle">{str(X).replace("-", "−")}</text>')
    ystep = max(1, round((y1 - y0) / 10))
    for Y in range(math.ceil(y0), math.floor(y1) + 1, ystep):
        g.append(f'<line x1="{sx(x0):.1f}" y1="{sy(Y):.1f}" x2="{sx(x1):.1f}" y2="{sy(Y):.1f}" class="gg"/>')
        if Y != 0:
            g.append(f'<text x="{sx(0)-5 if x0 < 0 < x1 else pad-5:.1f}" y="{sy(Y)+3.5:.1f}" class="gt" text-anchor="end">{str(Y).replace("-", "−")}</text>')
    if y0 < 0 < y1:
        g.append(f'<line x1="{sx(x0)}" y1="{sy(0)}" x2="{sx(x1)}" y2="{sy(0)}" class="ga"/>')
    if x0 <= 0 <= x1:
        g.append(f'<line x1="{sx(0)}" y1="{sy(y0)}" x2="{sx(0)}" y2="{sy(y1)}" class="ga"/>')
    if shade:
        g.append('<polygon points="' + " ".join(f"{sx(p):.1f},{sy(q):.1f}" for p, q in shade) + '" class="gs"/>')
    for (p0, q0, p1, q1) in lines:
        g.append(f'<line x1="{sx(p0):.1f}" y1="{sy(q0):.1f}" x2="{sx(p1):.1f}" y2="{sy(q1):.1f}" class="gl"/>')
    if fn:
        N = 120
        path = []
        for i in range(N + 1):
            X = x0 + (x1 - x0) * i / N
            Y = fn(X)
            if y0 - 1 <= Y <= y1 + 1:
                path.append(f"{'M' if not path else 'L'}{sx(X):.1f},{sy(max(min(Y, y1), y0)):.1f}")
        g.append(f'<path d="{" ".join(path)}" class="gc"/>')
    for (p, q, t) in (pts or []):
        g.append(f'<circle cx="{sx(p):.1f}" cy="{sy(q):.1f}" r="3.5" class="gp"/>')
        if t:
            g.append(f'<text x="{sx(p)+6:.1f}" y="{sy(q)-6:.1f}" class="gt gpt">{t}</text>')
    return f'<svg viewBox="0 0 {w} {h}" class="graph" role="img" aria-label="Graph">{"".join(g)}</svg>'


def FAIL():
    raise AssertionError("pre-check failed")


def use(tid):
    """Continue adding questions to an existing topic."""
    global _cur
    assert any(t["id"] == tid for t in TOPICS), tid
    _cur = tid


def extras(tid, plain=None, examples=None, fig=None):
    """Attach a plain-English intro, worked examples and/or a diagram to a topic.

    examples: list of dicts {"q": question, "steps": [step, ...], "fig": svg or None}
    """
    for t in TOPICS:
        if t["id"] == tid:
            if plain:
                t["plain"] = fmt(plain)
            if examples:
                t["examples"] = [{"q": fmt(e["q"]),
                                  "steps": [fmt(s) for s in e["steps"]],
                                  "fig": e.get("fig")} for e in examples]
            if fig:
                t["fig"] = fig
            return t
    raise AssertionError("no such topic: " + tid)
