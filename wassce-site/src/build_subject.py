import importlib, json, re, sys
from collections import Counter

SUBJECTS = {
    "maths": {
        "mods": ["part1", "part2", "part3", "ext_maths", "ext2_maths"],
        "out": "index.html",
        "cfg": {
            "key": "wassce-core-maths-v1",
            "objSolLabel": "Working", "objSolBtn": "working",
            "thySolLabel": "Worked solution", "thySolBtn": "worked solution",
            "mockTab": "Mock Paper 1",
            "mockN": 50, "mockMins": 90, "quickN": 20, "quickMins": 30,
            "mockBlurb": "50 objective questions in 1 hour 30 minutes \u2014 the shape of WAEC Paper 1. "
                         "Questions are drawn at random from all 28 topics, and the paper is marked as soon as you submit.",
            "paperNote": "Paper 1 is 50 marks out of the 150 for the whole subject.",
            "theoryNote": "Work each question on paper first, then check the steps. In Paper 2 you must show your working to earn method marks.",
            "about": "<b>About these questions.</b> They are original practice questions written to the WAEC Core Mathematics syllabus and to the "
                     "format of Paper 1 (50 objectives, 1\u00bd h) and Paper 2 (13 theory questions, 2\u00bd h). They are <b>not</b> reproductions "
                     "of past WASSCE papers \u2014 for those, use WAEC's own e-learning portal and the past-question booklets sold by WAEC Ghana.",
        },
        "title": "WASSCE Core Maths Drill",
        "sub": "{n} original practice questions with full working \u2014 WAEC Core Mathematics syllabus. Not official past papers.",
        "acc": ("#B4295A", "#F7E4EB", "#FF7FA6", "#3A1F2A"),
    },
    "english": {
        "mods": ["eng1", "eng2", "eng3", "ext_eng", "ext2_eng"],
        "out": "english.html",
        "cfg": {
            "key": "wassce-english-v1",
            "objSolLabel": "Explanation", "objSolBtn": "explanation",
            "thySolLabel": "Model answer", "thySolBtn": "model answer",
            "mockTab": "Mock Paper 1",
            "mockN": 80, "mockMins": 60, "quickN": 20, "quickMins": 15,
            "mockBlurb": "80 objective questions in 1 hour — the shape of WAEC Paper 1 (lexis and structure). "
                         "Questions are drawn at random from every topic, and the paper is marked as soon as you submit.",
            "paperNote": "Paper 1 carries 40 of the 170 marks for English Language.",
            "theoryNote": "Write your answer out in full before you look at the model. Paper 2 rewards complete sentences in your own words.",
            "about": "<b>About these questions.</b> They are original practice questions written to the WAEC English Language syllabus and to the "
                     "format of Paper 1 (80 objectives on lexis and structure, 1 h), Paper 2 (essay, comprehension and summary, 2 h) and Paper 3 "
                     "(test of orals, 45 min). The passages were written for this app. They are <b>not</b> reproductions of past WASSCE papers — "
                     "for those, use WAEC's own e-learning portal and the past-question booklets sold by WAEC Ghana.",
        },
        "title": "WASSCE English Drill",
        "sub": "{n} original practice questions with model answers — WAEC English Language syllabus. Not official past papers.",
        "acc": ("#3A46A8", "#E7E9F8", "#93A4FF", "#242B52"),
    },
    "science": {
        "mods": ["sci1", "sci2", "sci3", "ext_sci", "ext2_sci"],
        "out": "science.html",
        "cfg": {
            "key": "wassce-science-v1",
            "objSolLabel": "Explanation", "objSolBtn": "explanation",
            "thySolLabel": "Answer guide", "thySolBtn": "answer guide",
            "mockTab": "Mock Paper 1",
            "mockN": 50, "mockMins": 60, "quickN": 20, "quickMins": 25,
            "mockBlurb": "50 objective questions in 1 hour — the shape of WAEC Paper 1. "
                         "Questions are drawn at random from all five syllabus themes, and the paper is marked as soon as you submit.",
            "paperNote": "Paper 1 carries 50 of the 190 marks for Integrated Science.",
            "theoryNote": "Answer on paper first, then compare. In Paper 2, points must be stated in full sentences, and labelled diagrams earn marks.",
            "about": "<b>About these questions.</b> They are original practice questions written to the WAEC Integrated Science syllabus and to the "
                     "format of Paper 1 (50 objectives, 1 h), Paper 2 (six essay questions, answer four, 1½ h) and Paper 3 (practical, 2 h). "
                     "They are <b>not</b> reproductions of past WASSCE papers — for those, use WAEC's own e-learning portal and the "
                     "past-question booklets sold by WAEC Ghana.",
        },
        "title": "WASSCE Science Drill",
        "sub": "{n} original practice questions with full explanations — WAEC Integrated Science syllabus. Not official past papers.",
        "acc": ("#0F7A66", "#DCF0EA", "#4FD1B0", "#0E2E27"),
    },
    "social": {
        "mods": ["sst1", "sst2", "sst3", "ext_sst", "ext2_sst"],
        "out": "social.html",
        "cfg": {
            "key": "wassce-social-v1",
            "objSolLabel": "Explanation", "objSolBtn": "explanation",
            "thySolLabel": "Answer guide", "thySolBtn": "answer guide",
            "mockTab": "Mock Paper 1",
            "mockN": 50, "mockMins": 50, "quickN": 20, "quickMins": 20,
            "mockBlurb": "50 objective questions in 50 minutes \u2014 the shape of WAEC Paper 1. "
                         "Questions are drawn at random from all three sections of the syllabus, and the paper is marked as soon as you submit.",
            "paperNote": "Paper 1 carries 50 marks; Paper 2 carries 100 (five essays at 20 marks each).",
            "theoryNote": "Plan four or five points, then write each as a paragraph: state the point, explain it, and give a Ghanaian example. That is how essay marks are earned.",
            "about": "<b>About these questions.</b> They are original practice questions written to the WASSCE Social Studies syllabus and to the "
                     "format of Paper 1 (50 objectives) and Paper 2 (three sections \u2014 The Environment; Governance, Politics and Stability; "
                     "Social and Economic Development \u2014 from which five essays are answered, at least one and at most two per section). "
                     "Confirm the exact timing on your examination timetable. They are <b>not</b> reproductions of past WASSCE papers \u2014 "
                     "for those, use WAEC's own e-learning portal and the past-question booklets sold by WAEC Ghana.",
        },
        "title": "WASSCE Social Studies Drill",
        "sub": "{n} original practice questions with answer guides \u2014 WASSCE Social Studies syllabus. Not official past papers.",
        "acc": ("#9A5B12", "#F6E9D6", "#E6A44E", "#33220E"),
    },
}

name = sys.argv[1]
spec = SUBJECTS[name]
import core
from syllabus import SYLLABUS, ordered_topic_ids
for m in spec["mods"]:
    importlib.import_module(m)
order = {tid: i for i, tid in enumerate(ordered_topic_ids(name))}
assert set(order) == {t["id"] for t in core.TOPICS}, "syllabus and topics do not match for " + name
core.TOPICS.sort(key=lambda t: order[t["id"]])

obj = [q for q in core.QS if q["type"] == "obj"]
thy = [q for q in core.QS if q["type"] == "thy"]
print(f"{name}: {len(core.TOPICS)} topics | {len(obj)} objective | {len(thy)} theory | checks {core.STATS}")
print("  answer key spread:", dict(Counter(q["ans"] for q in obj)))

# structural checks
ids = [q["id"] for q in core.QS]
assert len(ids) == len(set(ids))
for t in core.TOPICS:
    qs = [q for q in core.QS if q["topic"] == t["id"]]
    assert any(q["type"] == "obj" for q in qs), t["id"]
    assert any(q["type"] == "thy" for q in qs), t["id"]
for q in obj:
    assert len(q["opts"]) == 4 and len(set(q["opts"])) == 4, q["id"]
    assert 0 <= q["ans"] < 4
    assert q["sol"], q["id"]

def balanced(s):
    if not isinstance(s, str):
        return True
    void = {"br", "img", "line", "circle", "path", "polygon"}
    op = [x for x in re.findall(r'<(\w+)[^>]*?(?<!/)>', s) if x not in void]
    return sorted(op) == sorted(re.findall(r'</(\w+)>', s))

bad = [(q["id"], s[:60]) for q in core.QS for s in [q["q"]] + q["sol"] + (q["opts"] if q["type"] == "obj" else []) if not balanced(s)]
assert not bad, bad
print("  structure checks: passed")

cfg = dict(spec["cfg"])
bank = json.dumps({"topics": core.TOPICS, "questions": core.QS,
                   "syllabus": [{"section": sec, "items": [{"t": lab, "topic": tid} for lab, tid in items]}
                                for sec, items in SYLLABUS[name]]}, ensure_ascii=False)
assert "</script" not in bank

html = open("template.html").read()
al, asl, ad, asd = spec["acc"]
html = (html.replace("__TITLE__", spec["title"])
            .replace("__SUB__", spec["sub"].format(n=len(core.QS)))
            .replace("__MOCKTAB__", cfg["mockTab"])
            .replace("__ACC_L__", al).replace("__ACCS_L__", asl)
            .replace("__ACC_D__", ad).replace("__ACCS_D__", asd)
            .replace("__CFG__", json.dumps(cfg, ensure_ascii=False))
            .replace("__BANK__", bank))
for tok in ["__TITLE__", "__SUB__", "__CFG__", "__BANK__", "__ACC_L__", "__ACC_D__"]:
    assert tok not in html, tok
open(spec["out"], "w").write(html)
print(f"  wrote {spec['out']} ({len(html)//1024} KB)")
