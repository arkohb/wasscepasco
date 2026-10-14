import importlib, json, sys, re
import core
from syllabus import SYLLABUS, ordered_topic_ids
name, mods = sys.argv[1], sys.argv[2].split(",")
for m in mods:
    importlib.import_module(m)
missing = [t["id"] for t in core.TOPICS if not t.get("plain")]
assert not missing, "topics with no plain-words intro: " + ", ".join(missing)
for t in core.TOPICS:
    for e in t.get("examples", []):
        assert e["q"] and e["steps"], t["id"]
obj = [q for q in core.QS if q["type"] == "obj"]
# structural checks
ids = [q["id"] for q in core.QS]
assert len(ids) == len(set(ids))
for q in obj:
    assert len(q["opts"]) == 4 and len(set(q["opts"])) == 4, q["id"]
    assert 0 <= q["ans"] < 4 and q["sol"], q["id"]
for t in core.TOPICS:
    qs = [q for q in core.QS if q["topic"] == t["id"]]
    assert any(x["type"] == "obj" for x in qs) and any(x["type"] == "thy" for x in qs), t["id"]
# every syllabus item must point at a real topic, and every topic must appear in the syllabus
ids = {t["id"] for t in core.TOPICS}
syl_ids = set(ordered_topic_ids(name))
unknown = [tid for _, items in SYLLABUS[name] for _, tid in items if tid not in ids]
orphan = sorted(ids - syl_ids)
assert not unknown, "syllabus points at missing topics: " + ", ".join(unknown)
assert not orphan, "topics missing from the syllabus map: " + ", ".join(orphan)

# order the topics the way the syllabus runs
order = {tid: i for i, tid in enumerate(ordered_topic_ids(name))}
core.TOPICS.sort(key=lambda t: order[t["id"]])

json.dump({"topics": core.TOPICS, "questions": core.QS,
           "syllabus": [{"section": sec, "items": [{"t": lab, "topic": tid} for lab, tid in items]}
                        for sec, items in SYLLABUS[name]]},
          open(f"bank_{name}.json", "w"), ensure_ascii=False)
ex = sum(len(t.get("examples", [])) for t in core.TOPICS)
figs = sum(1 for t in core.TOPICS if t.get("fig")) + sum(1 for t in core.TOPICS for e in t.get("examples", []) if e.get("fig"))
print(f"{name}: {len(core.TOPICS)} topics, {len(obj)} obj, {len(core.QS)-len(obj)} theory, "
      f"{ex} worked examples, {figs} diagrams, "
      f"{sum(len(i) for _, i in SYLLABUS[name])} syllabus items, checks {core.STATS}")
