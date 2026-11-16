#!/usr/bin/env python3
"""Consistency checker for the course repository. Python 3.9+, standard library only.

  check_course.py            validate catalog, unlock files, learner state
  check_course.py --status   also print completed / available / blocked
  check_course.py --mermaid  print the dependency graph as Mermaid
  check_course.py --budget   print the hour budget by phase (essential vs optional)

Exit code 1 if any error is found. Paths are relative to the repository root.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID_RE = r"P[0-6X]-[A-Z0-9]+-\d\d"
SECTIONS = ["Objective", "Problem", "Prerequisites", "Techniques", "What you need first",
            "Practical challenge", "Deliverable", "Acceptance criteria", "Verification",
            "Mastery target", "Next unlocks"]
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def rank(uid):
    p = uid.split("-")[0][1:]
    return 99 if p == "X" else int(p)


def table_rows(text, heading=None):
    """Rows (list of cells) of markdown table lines starting with '| P'. Optionally within one '## heading'."""
    if heading is not None:
        m = re.search(r"^## " + re.escape(heading) + r"\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        text = m.group(1) if m else ""
    rows = []
    for line in text.splitlines():
        if line.startswith("| P"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def parse_list(v):
    return re.findall(ID_RE, v)


def load_catalog():
    cat = {}
    text = (ROOT / "UNLOCKS" / "CATALOG.md").read_text()
    for r in table_rows(text):
        if len(r) != 7:
            err(f"CATALOG: malformed row {r}")
            continue
        uid, title, req, mastery, cls, hours, defn = r
        if not re.fullmatch(ID_RE, uid):
            err(f"CATALOG: bad id {uid}")
            continue
        if uid in cat:
            err(f"CATALOG: duplicate id {uid}")
        if not re.fullmatch(r"L[0-5]", mastery):
            err(f"CATALOG {uid}: bad mastery {mastery}")
        if cls not in ("E", "O"):
            err(f"CATALOG {uid}: class must be E or O")
        if not re.fullmatch(r"\d+\+\d+\+\d+\+\d+", hours):
            err(f"CATALOG {uid}: hours must look like 3+1+1+0")
            hours = "0+0+0+0"
        if uid.startswith("PX-") and cls != "O":
            err(f"CATALOG {uid}: stretch unlocks must be optional")
        if defn not in ("authored", "planned"):
            err(f"CATALOG {uid}: definition must be authored|planned")
        cat[uid] = {"title": title, "requires": parse_list(req), "mastery": mastery, "cls": cls,
                     "hours": [int(x) for x in hours.split("+")], "def": defn}
    return cat


def check_graph(cat):
    for uid, u in cat.items():
        for r in u["requires"]:
            if r not in cat:
                err(f"{uid}: requires unknown unlock {r}")
            elif rank(r) > rank(uid):
                err(f"{uid}: requires {r} from a later phase")
            if r == uid:
                err(f"{uid}: requires itself")
            if r in cat and u["cls"] == "E" and cat[r]["cls"] == "O":
                err(f"{uid}: essential unlock requires optional {r}")
    # cycle detection (iterative DFS colors)
    color = {}
    for start in cat:
        stack = [(start, iter(cat[start]["requires"]))]
        if color.get(start):
            continue
        color[start] = 1
        while stack:
            node, it = stack[-1]
            for nxt in it:
                if nxt not in cat:
                    continue
                if color.get(nxt) == 1:
                    err(f"cycle through {node} -> {nxt}")
                elif not color.get(nxt):
                    color[nxt] = 1
                    stack.append((nxt, iter(cat[nxt]["requires"])))
                    break
            else:
                color[node] = 2
                stack.pop()


def check_unlock_files(cat):
    files = {p.stem for p in (ROOT / "UNLOCKS").glob("P*.md")}
    for uid, u in cat.items():
        path = ROOT / "UNLOCKS" / f"{uid}.md"
        if u["def"] == "authored" and not path.exists():
            err(f"{uid}: catalog says authored but file is missing")
        if u["def"] == "planned" and path.exists():
            err(f"{uid}: file exists but catalog says planned")
    for f in files - set(cat):
        err(f"UNLOCKS/{f}.md is not in the catalog")
    for uid in sorted(files & set(cat)):
        text = (ROOT / "UNLOCKS" / f"{uid}.md").read_text()
        fm = front_matter(text)
        if fm is None:
            err(f"{uid}: missing front matter")
            continue
        if fm.get("id") != uid:
            err(f"{uid}: header id mismatch")
        if set(parse_list(fm.get("requires", ""))) != set(cat[uid]["requires"]):
            err(f"{uid}: header requires differ from catalog")
        if fm.get("mastery") != cat[uid]["mastery"]:
            err(f"{uid}: header mastery differs from catalog")
        if fm.get("phase") != uid.split("-")[0][1:]:
            err(f"{uid}: header phase does not match id")
        heads = re.findall(r"^## (.+?)\s*$", text, re.M)
        if heads[: len(SECTIONS)] != SECTIONS:
            err(f"{uid}: sections must be exactly, in order: {', '.join(SECTIONS)} (found {heads})")
        m = re.search(r"^## Next unlocks\s*$(.*)", text, re.M | re.S)
        for nxt in re.findall(ID_RE, m.group(1)) if m else []:
            if nxt not in cat:
                err(f"{uid}: next unlock {nxt} unknown")
            elif uid not in cat[nxt]["requires"]:
                err(f"{uid}: lists {nxt} as next, but {nxt} does not require it")
        if not re.search(r"^## Acceptance criteria\s*$\s*1\. ", text, re.M):
            err(f"{uid}: acceptance criteria must be a numbered list")


def load_state(cat):
    text = (ROOT / "LEARNER_STATE.md").read_text()
    done, prog = {}, []
    for r in table_rows(text, "Completed unlocks"):
        if len(r) < 4:
            err(f"STATE: malformed completed row {r}")
            continue
        uid, date, got, ev = r[:4]
        if uid not in cat:
            err(f"STATE: completed unknown unlock {uid}")
            continue
        if cat[uid]["def"] != "authored":
            err(f"STATE: {uid} completed but never authored")
        if not re.fullmatch(r"L[0-5]", got) or int(got[1]) < int(cat[uid]["mastery"][1]):
            err(f"STATE: {uid} mastery {got} below target {cat[uid]['mastery']}")
        if not list((ROOT / "EVIDENCE" / uid).glob("*.md")):
            err(f"STATE: {uid} completed but no EVIDENCE/{uid}/*.md")
        done[uid] = (date, got)
    for r in table_rows(text, "In progress"):
        if r[0] not in cat:
            err(f"STATE: in-progress unknown unlock {r[0]}")
        prog.append(r[0])
    for uid in done:
        for r in cat.get(uid, {}).get("requires", []):
            if r not in done:
                err(f"STATE: {uid} completed but prerequisite {r} is not")
    return done, prog


def curriculum_status():
    fm = front_matter((ROOT / "CURRICULUM.md").read_text()) or {}
    return fm.get("status", "UNKNOWN")


def print_status(cat, done, prog, status):
    print(f"Curriculum status: {status}")
    if status != "APPROVED":
        print("-> Not approved: no unlock may be taught. Discussion and review only.")
    avail = [u for u in cat if u not in done and all(r in done for r in cat[u]["requires"])]
    blocked = [u for u in cat if u not in done and u not in avail]
    print(f"\nCompleted ({len(done)}): {', '.join(sorted(done)) or 'none'}")
    print(f"In progress ({len(prog)}): {', '.join(prog) or 'none'}")
    note = "" if status == "APPROVED" else " (would be available once approved)"
    print(f"\nAvailable ({len(avail)}){note}:")
    for u in avail:
        tag = "" if cat[u]["def"] == "authored" else "  [planned: author before teaching]"
        print(f"  {u}  {cat[u]['title']} (target {cat[u]['mastery']}){tag}")
    print(f"\nBlocked ({len(blocked)}):")
    for u in blocked:
        missing = [r for r in cat[u]["requires"] if r not in done]
        print(f"  {u}  waiting on {', '.join(missing)}")


def print_budget(cat):
    names = ["build", "study", "verify", "consolidate"]
    print(f"{'Phase':<6}{'E n':>4}{'E hrs':>7}{'build':>7}{'study':>7}{'verify':>7}{'consol':>7}{'O n':>5}{'O hrs':>7}")
    tot_e = tot_o = 0
    sums = [0, 0, 0, 0]
    for ph in [0, 1, 2, 3, 4, 5, 6, 99]:
        es = [u for k, u in cat.items() if rank(k) == ph and u["cls"] == "E"]
        os_ = [u for k, u in cat.items() if rank(k) == ph and u["cls"] == "O"]
        parts = [sum(u["hours"][i] for u in es) for i in range(4)]
        eh, oh = sum(parts), sum(sum(u["hours"]) for u in os_)
        tot_e += eh
        tot_o += oh
        sums = [a + b for a, b in zip(sums, parts)]
        label = "PX" if ph == 99 else str(ph)
        print(f"{label:<6}{len(es):>4}{eh:>7}{parts[0]:>7}{parts[1]:>7}{parts[2]:>7}{parts[3]:>7}{len(os_):>5}{oh:>7}")
    print(f"{'Total':<6}{'':>4}{tot_e:>7}{sums[0]:>7}{sums[1]:>7}{sums[2]:>7}{sums[3]:>7}{'':>5}{tot_o:>7}")
    print(f"\nEssential {tot_e} h = {tot_e / 10:.1f} weeks at 10 h/week. Optional pool {tot_o} h (includes stretch).")
    if not 350 <= tot_e <= 370:
        print("NOTE: essential total is outside the 350-370 h planning target.")
    return tot_e


def print_mermaid(cat):
    print("flowchart LR")
    for uid, u in cat.items():
        print(f'  {uid.replace("-", "_")}["{uid}"]')
    for uid, u in cat.items():
        for r in u["requires"]:
            print(f'  {r.replace("-", "_")} --> {uid.replace("-", "_")}')


def main():
    cat = load_catalog()
    check_graph(cat)
    check_unlock_files(cat)
    done, prog = load_state(cat)
    status = curriculum_status()
    if "--mermaid" in sys.argv:
        print_mermaid(cat)
        return 0
    if "--budget" in sys.argv:
        print_budget(cat)
        return 0
    for p in ["README.md", "CLAUDE.md", "COURSE_OBJECTIVE.md", "CURRICULUM.md", "LEARNER_PROFILE.md",
              "LEARNER_STATE.md", "DECISION_LOG.md", "SESSION_HANDOFF.md", "PROCEDURES.md",
              "ENVIRONMENT.md", "KNOWLEDGE_STANDARD.md", "KNOWLEDGE_STANDARD_ADDENDUM.md", "career/CAREER_RESEARCH.md",
              "project/README.md", "project/PLAN.md", "project/DECISIONS.md", "knowledge/README.md",
              "TEMPLATES/LEARNER_STATE.initial.md"] + [f"PHASES/PHASE-{i}.md" for i in range(7)]:
        if not (ROOT / p).exists():
            err(f"missing required file {p}")
    if "--status" in sys.argv:
        print_status(cat, done, prog, status)
        print()
    authored = sum(1 for u in cat.values() if u["def"] == "authored")
    print(f"Catalog: {len(cat)} unlocks ({authored} authored, {len(cat) - authored} planned)")
    if errors:
        print(f"\n{len(errors)} ERROR(S):")
        for e in errors:
            print("  -", e)
        return 1
    print("OK: graph is acyclic, prerequisites resolve, unlock files match the catalog, state is consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
