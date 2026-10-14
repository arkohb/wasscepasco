import json

SUB = [
 ("maths", "Core Maths", "#D14A76", "bank_maths.json",
  "{n} original practice questions with full working — WAEC Core Mathematics syllabus. Not official past papers.",
  dict(objSolLabel="Working", objSolBtn="working", thySolLabel="Worked solution", thySolBtn="worked solution",
       mockTab="Mock Paper 1", mockN=50, mockMins=90, quickN=20, quickMins=30,
       mockBlurb="50 objective questions in 1 hour 30 minutes — the shape of WAEC Paper 1. "
                 "Questions are drawn at random from all 28 topics, and the paper is marked as soon as you submit.",
       paperNote="Paper 1 is 50 marks out of the 150 for the whole subject.",
       theoryNote="Work each question on paper first, then check the steps. In Paper 2 you must show your working to earn method marks.",
       about="<b>About these questions.</b> They are original practice questions written to the WAEC Core Mathematics syllabus and to the "
             "format of Paper 1 (50 objectives, 1½ h) and Paper 2 (13 theory questions, 2½ h). They are <b>not</b> reproductions of past "
             "WASSCE papers — for those, use WAEC's own e-learning portal and the past-question booklets sold by WAEC Ghana.")),
 ("english", "English", "#5A67D8", "bank_english.json",
  "{n} original practice questions with model answers — WAEC English Language syllabus. Not official past papers.",
  dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Model answer", thySolBtn="model answer",
       mockTab="Mock Paper 1", mockN=80, mockMins=60, quickN=20, quickMins=15,
       mockBlurb="80 objective questions in 1 hour — the shape of WAEC Paper 1 (lexis and structure). "
                 "Questions are drawn at random from every topic, and the paper is marked as soon as you submit.",
       paperNote="Paper 1 carries 40 of the 170 marks for English Language.",
       theoryNote="Write your answer out in full before you look at the model. Paper 2 rewards complete sentences in your own words.",
       about="<b>About these questions.</b> They are original practice questions written to the WAEC English Language syllabus and to the "
             "format of Paper 1 (80 objectives on lexis and structure, 1 h), Paper 2 (essay, comprehension and summary, 2 h) and Paper 3 "
             "(test of orals, 45 min). The passages were written for this app. They are <b>not</b> reproductions of past WASSCE papers — "
             "for those, use WAEC's own e-learning portal and the past-question booklets sold by WAEC Ghana.")),
 ("science", "Integrated Science", "#1AA189", "bank_science.json",
  "{n} original practice questions with full explanations — WAEC Integrated Science syllabus. Not official past papers.",
  dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
       mockTab="Mock Paper 1", mockN=50, mockMins=60, quickN=20, quickMins=25,
       mockBlurb="50 objective questions in 1 hour — the shape of WAEC Paper 1. "
                 "Questions are drawn at random from all five syllabus themes, and the paper is marked as soon as you submit.",
       paperNote="Paper 1 carries 50 of the 190 marks for Integrated Science.",
       theoryNote="Answer on paper first, then compare. In Paper 2, points must be stated in full sentences, and labelled diagrams earn marks.",
       about="<b>About these questions.</b> They are original practice questions written to the WAEC Integrated Science syllabus and to the "
             "format of Paper 1 (50 objectives, 1 h), Paper 2 (six essay questions, answer four, 1½ h) and Paper 3 (practical, 2 h). "
             "They are <b>not</b> reproductions of past WASSCE papers — for those, use WAEC's own e-learning portal and the past-question "
             "booklets sold by WAEC Ghana.")),
 ("social", "Social Studies", "#C08028", "bank_social.json",
  "{n} original practice questions with answer guides — WASSCE Social Studies syllabus. Not official past papers.",
  dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
       mockTab="Mock Paper 1", mockN=50, mockMins=50, quickN=20, quickMins=20,
       mockBlurb="50 objective questions in 50 minutes — the shape of WAEC Paper 1. "
                 "Questions are drawn at random from all three sections of the syllabus, and the paper is marked as soon as you submit.",
       paperNote="Paper 1 carries 50 marks; Paper 2 carries 100 (five essays at 20 marks each).",
       theoryNote="Plan four or five points, then write each as a paragraph: state the point, explain it, and give a Ghanaian example. "
                  "That is how essay marks are earned.",
       about="<b>About these questions.</b> They are original practice questions written to the WASSCE Social Studies syllabus and to the "
             "format of Paper 1 (50 objectives) and Paper 2 (three sections — The Environment; Governance, Politics and Stability; "
             "Social and Economic Development — from which five essays are answered, at least one and at most two per section). "
             "Confirm the exact timing on your examination timetable. They are <b>not</b> reproductions of past WASSCE papers — "
             "for those, use WAEC's own e-learning portal and the past-question booklets sold by WAEC Ghana.")),
]

subjects, totals = [], [0, 0]
for sid, name, dot, path, sub, cfg in SUB:
    bank = json.load(open(path))
    qs = bank["questions"]
    nobj = sum(1 for q in qs if q["type"] == "obj")
    totals[0] += nobj; totals[1] += len(qs) - nobj
    subjects.append({"id": sid, "name": name, "dot": dot, "sub": sub.format(n=len(qs)),
                     "cfg": cfg, "topics": bank["topics"], "questions": qs,
                     "syllabus": bank["syllabus"]})
    print(f"  {name:20s} {len(bank['topics']):3d} topics  {nobj:3d} obj  {len(qs)-nobj:3d} theory")

data = json.dumps({"subjects": subjects}, ensure_ascii=False)
assert "</script" not in data
html = open("hub.html").read().replace("__BANK__", data)
assert "__BANK__" not in html
open("wassce-core-four.html", "w").write(html)
print("syllabus items:", sum(len(sec["items"]) for s in subjects for sec in s["syllabus"]))
print(f"total: {sum(len(s['questions']) for s in subjects)} questions "
      f"({totals[0]} objective, {totals[1]} theory) across {sum(len(s['topics']) for s in subjects)} topics")
print(f"wrote wassce-core-four.html — {len(html)//1024} KB")
