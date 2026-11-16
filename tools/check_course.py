#!/usr/bin/env python3
"""Consistency checker for the course repository. Python 3.9+, standard library only.

  check_course.py                validate everything
  check_course.py --status       also print completed / available / blocked
  check_course.py --budget       also print the hour budget by phase
  check_course.py --mermaid      print the dependency graph as Mermaid
  check_course.py --fingerprint  print the catalog fingerprint (recorded at approval)

Every mode runs ALL validation. Reports go to stdout. Errors and warnings go to stderr,
prefixed "ERROR:" / "WARNING:". Exit code 1 if any error was found, otherwise 0.

What this checks: structure, graph, files, declared dependencies, hashes, field presence,
internal references, the shape of each LEARN/<ID>/ learning-material folder, and that lesson code
blocks match their example files. What it does NOT do: it never runs an evidence bundle's commands, so a
passing check does not show that any artifact reproduces. Paths are relative to the repo root.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID_RE = r"P[0-6X]-[A-Z0-9]+-\d\d"
SECTIONS = ["Objective", "Problem", "Prerequisites", "Techniques", "What you need first",
            "Practical challenge", "Deliverable", "Acceptance criteria", "Verification",
            "Mastery target", "Next unlocks"]
REQUIRED_DIRS = ["PHASES", "UNLOCKS", "TEMPLATES", "EVIDENCE", "ARCHIVE", "tools",
                 "knowledge", "project", "career"]
REQUIRED_FILES = [
    "README.md", "CLAUDE.md", "COURSE_OBJECTIVE.md", "CURRICULUM.md", "LEARNER_PROFILE.md",
    "LEARNER_STATE.md", "DECISION_LOG.md", "SESSION_HANDOFF.md", "PROCEDURES.md",
    "ENVIRONMENT.md", "KNOWLEDGE_STANDARD.md", "KNOWLEDGE_STANDARD_ADDENDUM.md",
    "UNLOCKS/README.md", "UNLOCKS/CATALOG.md",
    "TEMPLATES/LEARNER_STATE.initial.md", "TEMPLATES/UNLOCK.md", "TEMPLATES/EVALUATION.md",
    "TEMPLATES/MANIFEST.md", "TEMPLATES/EXPERIMENT.md", "TEMPLATES/LEARN_UNLOCK.md", "LEARN/README.md",
    "career/CAREER_RESEARCH.md", "career/POSTINGS.md",
    "project/README.md", "project/PLAN.md", "project/DECISIONS.md", "knowledge/README.md",
] + [f"PHASES/PHASE-{i}.md" for i in range(7)]
# Document names that have exactly one canonical location (anywhere else is an error,
# except inside ARCHIVE/ and EVIDENCE/ which hold copies by design).
CANONICAL = {
    "CAREER_RESEARCH.md": "career/CAREER_RESEARCH.md", "POSTINGS.md": "career/POSTINGS.md",
    "PLAN.md": "project/PLAN.md", "DECISIONS.md": "project/DECISIONS.md",
    "CURRICULUM.md": "CURRICULUM.md", "COURSE_OBJECTIVE.md": "COURSE_OBJECTIVE.md",
    "LEARNER_STATE.md": "LEARNER_STATE.md", "DECISION_LOG.md": "DECISION_LOG.md",
    "SESSION_HANDOFF.md": "SESSION_HANDOFF.md", "KNOWLEDGE_STANDARD.md": "KNOWLEDGE_STANDARD.md",
    "KNOWLEDGE_STANDARD_ADDENDUM.md": "KNOWLEDGE_STANDARD_ADDENDUM.md",
}
RETIRED_NAMES = {"PROJECTS.md"}
CODE_EXT = {".go", ".rs", ".ts", ".tsx", ".js", ".jsx", ".java", ".c", ".cpp", ".sql", ".py"}
CODE_FILES = {"go.mod", "go.sum", "package.json", "Cargo.toml", "pom.xml"}
EXAMPLE_CODE_OK = re.compile(r"^LEARN/[^/]+/examples/")  # teaching examples are the one place code may live
FORBIDDEN_IN_BUNDLE = {"node_modules", ".git", "vendor", "target", "__pycache__", ".venv"}
MISSING_OK_PREFIXES = ("project/design/", "EVIDENCE/", "ARCHIVE/", "knowledge/")
TOP_DIRS = ("PHASES", "UNLOCKS", "TEMPLATES", "EVIDENCE", "ARCHIVE", "tools", "knowledge",
            "project", "career")
HISTORY_DOCS = {"DECISION_LOG.md", "KNOWLEDGE_STANDARD.md"}  # append-only / supplied: skip ref checks
MAX_FILE_KB, MAX_BUNDLE_KB = 512, 5120

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def rank(uid):
    p = uid.split("-")[0][1:]
    return 99 if p == "X" else int(p)


def sha256_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def table_rows(text, heading=None, prefix="| P"):
    if heading is not None:
        m = re.search(r"^## " + re.escape(heading) + r"\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        text = m.group(1) if m else ""
    rows = []
    for line in text.splitlines():
        if line.startswith(prefix):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def section(text, name):
    m = re.search(r"^## " + re.escape(name) + r"\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def md_table(sec):
    """Data rows of the first markdown table in a section (header and separator removed)."""
    rows = []
    for line in (sec or "").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


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


def parse_ids(v):
    return re.findall(ID_RE, v)


# ---------------------------------------------------------------- structure

def check_structure():
    for d in REQUIRED_DIRS:
        if not (ROOT / d).is_dir():
            err(f"required directory missing: {d}/")
    for f in REQUIRED_FILES:
        if not (ROOT / f).is_file():
            err(f"required file missing: {f}")
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        in_held = rel.startswith(("ARCHIVE/", "EVIDENCE/"))
        if p.name in RETIRED_NAMES and not in_held:
            err(f"{rel}: retired document name (its content moved; see DECISION_LOG D-004)")
        if p.name in CANONICAL and not in_held and rel != CANONICAL[p.name]:
            err(f"{rel}: canonical location is {CANONICAL[p.name]}")
        is_code = p.suffix in CODE_EXT or p.name in CODE_FILES
        if is_code and not in_held and not (rel.startswith("tools/") and p.suffix == ".py") \
                and not EXAMPLE_CODE_OK.match(rel):
            err(f"{rel}: source code does not belong here (plans, design and evidence only; "
                "teaching examples go under LEARN/<ID>/examples/)")
        if rel.startswith("EVIDENCE/") and p.name not in (".gitkeep",):
            parts = p.relative_to(ROOT / "EVIDENCE").parts
            if len(parts) < 3 and p.name != "README.md":
                err(f"{rel}: evidence files must live in EVIDENCE/<ID>/<date>-<n>/")
    for d in (ROOT / "ARCHIVE").glob("*") if (ROOT / "ARCHIVE").is_dir() else []:
        if d.is_dir() and not (d / "RESTART_NOTE.md").is_file():
            err(f"ARCHIVE/{d.name}: missing RESTART_NOTE.md (reason, date, what moved, what stayed)")


# ---------------------------------------------------------------- catalog and graph

def load_catalog():
    cat = {}
    text = read("UNLOCKS/CATALOG.md")
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
        for tok in [x.strip() for x in req.split(",")]:
            if tok not in ("", "—", "-") and not re.fullmatch(ID_RE, tok):
                err(f"CATALOG {uid}: malformed prerequisite '{tok}' in Requires")
        if cls not in ("E", "O"):
            err(f"CATALOG {uid}: class must be E or O")
        if not re.fullmatch(r"\d+\+\d+\+\d+\+\d+", hours):
            err(f"CATALOG {uid}: hours must look like 3+1+1+0")
            hours = "0+0+0+0"
        if uid.startswith("PX-") and cls != "O":
            err(f"CATALOG {uid}: stretch unlocks must be optional")
        if defn not in ("authored", "planned"):
            err(f"CATALOG {uid}: definition must be authored|planned")
        cat[uid] = {"title": title, "requires": parse_ids(req), "mastery": mastery, "cls": cls,
                    "hours": [int(x) for x in hours.split("+")], "def": defn}
    if not cat:
        err("CATALOG: no unlocks found")
    return cat


def closure(cat, ids):
    seen, stack = set(), list(ids)
    while stack:
        n = stack.pop()
        for r in cat.get(n, {}).get("requires", []):
            if r not in seen:
                seen.add(r)
                stack.append(r)
    return seen


def check_graph(cat):
    for uid, u in cat.items():
        for r in u["requires"]:
            if r not in cat:
                err(f"{uid}: requires unknown unlock {r}")
                continue
            if rank(r) > rank(uid):
                err(f"{uid}: requires {r} from a later phase")
            if r == uid:
                err(f"{uid}: requires itself")
            if u["cls"] == "E" and cat[r]["cls"] == "O":
                err(f"{uid}: essential unlock requires optional {r}")
    color = {}
    for start in cat:
        if color.get(start):
            continue
        color[start] = 1
        stack = [(start, iter(cat[start]["requires"]))]
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


def fingerprint(cat):
    lines = []
    for uid in sorted(cat):
        u = cat[uid]
        lines.append("|".join([uid, u["title"], ",".join(sorted(u["requires"])), u["mastery"],
                               u["cls"], "+".join(map(str, u["hours"]))]))
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


# ---------------------------------------------------------------- unlock files

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
        text = read(f"UNLOCKS/{uid}.md")
        fm = front_matter(text)
        if fm is None:
            err(f"{uid}: missing front matter")
            continue
        if fm.get("id") != uid:
            err(f"{uid}: header id mismatch")
        if set(parse_ids(fm.get("requires", ""))) != set(cat[uid]["requires"]):
            err(f"{uid}: header requires differ from catalog")
        if fm.get("mastery") != cat[uid]["mastery"]:
            err(f"{uid}: header mastery differs from catalog")
        if fm.get("phase") != uid.split("-")[0][1:]:
            err(f"{uid}: header phase does not match id")
        heads = re.findall(r"^## (.+?)\s*$", text, re.M)
        if heads[: len(SECTIONS)] != SECTIONS:
            err(f"{uid}: sections must be exactly, in order: {', '.join(SECTIONS)} (found {heads})")
        nxt_sec = section(text, "Next unlocks") or ""
        for nxt in parse_ids(nxt_sec):
            if nxt not in cat:
                err(f"{uid}: next unlock {nxt} unknown")
            elif uid not in cat[nxt]["requires"]:
                err(f"{uid}: lists {nxt} as next, but {nxt} does not require it")
        if not re.search(r"^## Acceptance criteria\s*$\s*1\. ", text, re.M):
            err(f"{uid}: acceptance criteria must be a numbered list")
        # prerequisites: text must match header; declared consumption must be reachable
        pre = section(text, "Prerequisites") or ""
        plain, used = [], []
        for line in pre.splitlines():
            (used if line.strip().startswith("Uses:") else plain).append(line)
        if set(parse_ids("\n".join(plain))) != set(cat[uid]["requires"]):
            err(f"{uid}: Prerequisites text names {sorted(set(parse_ids(chr(10).join(plain))))} "
                f"but catalog requires {sorted(cat[uid]['requires'])}")
        reach = closure(cat, [uid])
        for c in parse_ids("\n".join(used)):
            if c not in reach:
                err(f"{uid}: 'Uses:' declares an artifact from {c}, which is not a (transitive) prerequisite")


# ---------------------------------------------------------------- learner state and evidence

def load_state(cat):
    text = read("LEARNER_STATE.md")
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
        ev = ev.strip("`")
        d = ROOT / ev
        if not re.fullmatch(rf"EVIDENCE/{re.escape(uid)}/\d{{4}}-\d{{2}}-\d{{2}}-\d+", ev) or not d.is_dir():
            err(f"STATE: {uid} evidence must be an existing EVIDENCE/{uid}/<date>-<n> directory (got '{ev}')")
        else:
            m = re.search(r"\*\*Result:\*\*\s*(\S+(?: \S+)?)", read(f"{ev}/evaluation.md"))
            if not m or not m.group(1).startswith("passed"):
                err(f"STATE: {uid} evidence {ev} does not record Result: passed")
            m2 = re.search(r"\*\*Mastery shown:\*\*\s*(L[0-5])", read(f"{ev}/evaluation.md"))
            if m2 and m2.group(1) != got:
                err(f"STATE: {uid} mastery {got} differs from evaluation ({m2.group(1)})")
        done[uid] = (date, got, ev)
    for r in table_rows(text, "In progress"):
        if r[0] not in cat:
            err(f"STATE: in-progress unknown unlock {r[0]}")
        prog.append(r[0])
    for uid in done:
        for r in cat.get(uid, {}).get("requires", []):
            if r not in done:
                err(f"STATE: {uid} completed but prerequisite {r} is not")
    return done, prog


def check_evidence(cat):
    base = ROOT / "EVIDENCE"
    if not base.is_dir():
        return
    for ud in sorted(p for p in base.iterdir() if p.is_dir()):
        if ud.name not in cat:
            err(f"EVIDENCE/{ud.name}: not an unlock in the catalog")
            continue
        for ad in sorted(ud.iterdir()):
            rel = ad.relative_to(ROOT).as_posix()
            if not ad.is_dir() or not re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d+", ad.name):
                err(f"{rel}: expected an attempt directory named <YYYY-MM-DD>-<n>")
                continue
            check_bundle(ud.name, ad, rel)


def check_bundle(uid, ad, rel):
    ev = read(f"{rel}/evaluation.md")
    if not ev:
        err(f"{rel}: missing evaluation.md")
    else:
        if not re.search(r"\*\*Result:\*\*\s*(passed|not yet)\b", ev):
            err(f"{rel}/evaluation.md: needs '**Result:** passed' or 'not yet'")
        if not re.search(r"\*\*Mastery shown:\*\*\s*L[0-5]", ev):
            err(f"{rel}/evaluation.md: needs '**Mastery shown:** L0-L5'")
    mt = read(f"{rel}/manifest.md")
    if not mt:
        err(f"{rel}: missing manifest.md")
        return
    head = mt.split("\n## ", 1)[0]
    keys = dict(re.findall(r"^([a-z_]+):\s*(.+)$", head, re.M))
    for k in ["unlock", "capability", "evidence_kind", "implementation_attempt", "provenance", "reproduced_by"]:
        if not keys.get(k) or keys[k].startswith("<"):
            err(f"{rel}/manifest.md: field '{k}' missing or still a placeholder")
    if keys.get("unlock") and keys["unlock"] != uid:
        err(f"{rel}/manifest.md: unlock '{keys['unlock']}' does not match directory {uid}")
    kind = keys.get("evidence_kind", "")
    if kind not in ("preserved", "independently-reproduced"):
        err(f"{rel}/manifest.md: evidence_kind must be 'preserved' or 'independently-reproduced'")
    if kind == "independently-reproduced" and keys.get("reproduced_by", "n/a").strip().lower() == "n/a":
        err(f"{rel}/manifest.md: independently-reproduced needs 'reproduced_by' (who, when)")
    if re.search(r"(^|[\s`(])(/home/|/Users/|[A-Za-z]:\\)", mt):
        err(f"{rel}/manifest.md: contains a machine-specific absolute path")
    env = section(mt, "Environment") or ""
    for need in ("os", "toolchain"):
        if not re.search(rf"^- {need}:\s*\S", env, re.M):
            err(f"{rel}/manifest.md: Environment needs a '- {need}: ...' line")
    for name in ("Setup", "Limitations"):
        s = section(mt, name)
        if s is None or not re.search(r"\S", s):
            err(f"{rel}/manifest.md: section '{name}' missing or empty")
    # artifacts
    rows = md_table(section(mt, "Artifacts"))
    art = ad / "artifacts"
    listed = set()
    if not rows:
        err(f"{rel}/manifest.md: Artifacts table has no rows")
    for r in rows:
        if len(r) < 3:
            err(f"{rel}/manifest.md: malformed artifact row {r}")
            continue
        path, digest, role = r[0].strip("`"), r[1], r[2]
        listed.add(path)
        if role not in ("code", "test", "data", "output", "script", "doc", "config"):
            err(f"{rel}/manifest.md: artifact '{path}' has unknown role '{role}'")
        f = art / path
        if not f.is_file():
            err(f"{rel}: manifest lists artifacts/{path} but it does not exist")
        elif sha256_file(f) != digest:
            err(f"{rel}: artifacts/{path} does not match its manifest sha256")
    total = 0
    if art.is_dir():
        for f in sorted(p for p in art.rglob("*") if p.is_file()):
            r_ = f.relative_to(art).as_posix()
            total += f.stat().st_size
            if r_ not in listed:
                err(f"{rel}: artifacts/{r_} is not listed in the manifest")
            if FORBIDDEN_IN_BUNDLE & set(f.relative_to(art).parts):
                err(f"{rel}: artifacts/{r_} is inside a directory that must not be copied")
            if f.stat().st_size > MAX_FILE_KB * 1024:
                warn(f"{rel}: artifacts/{r_} is over {MAX_FILE_KB} KB; keep only what verification needs")
        if total > MAX_BUNDLE_KB * 1024:
            warn(f"{rel}: bundle is over {MAX_BUNDLE_KB} KB; avoid copying whole workspaces")
    elif rows:
        err(f"{rel}: artifacts/ directory missing")
    # commands
    crows = md_table(section(mt, "Commands"))
    if not crows:
        err(f"{rel}/manifest.md: Commands table has no rows")
    for r in crows:
        if len(r) < 6 or any(not c for c in r[:6]):
            err(f"{rel}/manifest.md: command row needs #, command, working dir, expected, observed, exit: {r}")
        elif not re.fullmatch(r"-?\d+", r[5]):
            err(f"{rel}/manifest.md: exit status must be an integer (got '{r[5]}')")


# ---------------------------------------------------------------- curriculum, budget, cuts

def budget_numbers(cat):
    out = {}
    for ph in [0, 1, 2, 3, 4, 5, 6, 99]:
        es = [u for k, u in cat.items() if rank(k) == ph and u["cls"] == "E"]
        os_ = [u for k, u in cat.items() if rank(k) == ph and u["cls"] == "O"]
        parts = [sum(u["hours"][i] for u in es) for i in range(4)]
        out[ph] = (len(es), sum(parts), parts, sum(sum(u["hours"]) for u in os_))
    return out


def check_curriculum(cat):
    text = read("CURRICULUM.md")
    fm = front_matter(text) or {}
    status = fm.get("status", "UNKNOWN")
    if status not in ("PROPOSED", "APPROVED"):
        err(f"CURRICULUM.md: status must be PROPOSED or APPROVED (got {status})")
    fp = fingerprint(cat)
    rec = fm.get("catalog_fingerprint", "")
    if status == "APPROVED":
        if not re.fullmatch(r"[0-9a-f]{64}", rec):
            err("CURRICULUM.md: APPROVED but no catalog_fingerprint recorded (run --fingerprint at approval)")
        elif rec != fp:
            err("CURRICULUM.md: catalog boundaries (title, prerequisites, mastery, class, hours) changed since "
                "approval. Present the change, get approval, log it, then update catalog_fingerprint")
        if fm.get("approved_by", "none") == "none":
            err("CURRICULUM.md: APPROVED but approved_by is 'none'")
    elif rec not in ("none", "") and rec != fp:
        warn("CURRICULUM.md: catalog_fingerprint is set but does not match the catalog (status is PROPOSED)")
    # budget numbers stated in prose must match the catalog
    b = budget_numbers(cat)
    tot_e = sum(v[1] for v in b.values())
    m = re.search(r"\*\*Essential plan: (\d+) hours", text)
    if not m:
        err("CURRICULUM.md: must state '**Essential plan: N hours**'")
    elif int(m.group(1)) != tot_e:
        err(f"CURRICULUM.md states essential plan {m.group(1)} h; catalog totals {tot_e} h")
    seen = set()
    for line in text.splitlines():
        r = re.match(r"^\| (\d) [^|]*\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", line)
        if r:
            ph = int(r.group(1))
            seen.add(ph)
            want = (b[ph][0], b[ph][1], *b[ph][2], b[ph][3])
            got = tuple(int(x) for x in r.groups()[1:])
            if got != want:
                err(f"CURRICULUM.md hours table, phase {ph}: states {got}, catalog gives {want}")
    for ph in range(7):
        if ph not in seen:
            err(f"CURRICULUM.md hours table: no row for phase {ph}")
    if not 350 <= tot_e <= 370:
        warn(f"essential total {tot_e} h is outside the 350-370 h planning target")
    # cut strategy vs completion criteria
    cut_groups = [[x.strip() for x in g.split(",") if x.strip()] for g in fm.get("cut_order", "").split("|")]
    cut = set()
    for g in cut_groups:
        for x in g:
            if x not in cat:
                err(f"CURRICULUM.md cut_order: unknown unlock {x}")
            elif cat[x]["cls"] != "E":
                err(f"CURRICULUM.md cut_order: {x} is not essential")
            cut.add(x)
    for uid, u in cat.items():
        if u["cls"] == "E" and uid not in cut:
            for r in u["requires"]:
                if r in cut:
                    err(f"cut strategy strands {uid}: it requires {r}, which the cut order removes")
    proofs = {}
    for r in table_rows(read("COURSE_OBJECTIVE.md"), "Completion proofs (machine-checked)", prefix="| C"):
        if not re.fullmatch(r"C\d", r[0]):
            continue  # header row
        if len(r) != 3:
            err(f"COURSE_OBJECTIVE.md: malformed completion-proof row {r}")
            continue
        crit, ids, cuttable = r
        proofs[crit] = (parse_ids(ids), cuttable)
        for i in parse_ids(ids):
            if i not in cat:
                err(f"COURSE_OBJECTIVE.md: {crit} proof unlock {i} unknown")
            elif cat[i]["cls"] != "E":
                err(f"COURSE_OBJECTIVE.md: {crit} proof unlock {i} is not essential")
        if cuttable not in ("yes", "no"):
            err(f"COURSE_OBJECTIVE.md: {crit} 'cuttable' must be yes or no")
    for c in [f"C{i}" for i in range(1, 9)]:
        if c not in proofs:
            err(f"COURSE_OBJECTIVE.md: no completion-proof row for {c}")
    for crit, (ids, cuttable) in proofs.items():
        if cuttable == "no":
            need = set(ids) | closure(cat, ids)
            hit = need & cut
            if hit:
                err(f"cut strategy makes protected criterion {crit} unreachable: needs {sorted(hit)}")
    return status


# ---------------------------------------------------------------- learning material

CODE_BLOCK = re.compile(r"\n`([\w./-]+)`\n```go\n(.*?)\n```", re.S)


def check_learn(cat, done, prog):
    base = ROOT / "LEARN"
    if not base.is_dir():
        return
    dirs = sorted(p for p in base.iterdir() if p.is_dir())
    for d in dirs:
        rel = f"LEARN/{d.name}"
        if d.name not in cat:
            err(f"{rel}: not an unlock in the catalog")
            continue
        if cat[d.name]["def"] != "authored":
            err(f"{rel}: learning material exists but the unlock is not authored")
        readme = d / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        if not text:
            err(f"{rel}: missing README.md (the start page)")
        else:
            for need in ("Start here", "What is prepared, and what is not", "Completion requirements"):
                if need not in text:
                    err(f"{rel}/README.md: missing the part '{need}'")
        sections = sorted(p for p in d.glob("*.md") if re.match(r"\d\d-.+\.md$", p.name))
        if not sections:
            err(f"{rel}: no numbered section files (01-....md)")
        nums = [int(p.name[:2]) for p in sections]
        if nums and nums != list(range(1, len(nums) + 1)):
            err(f"{rel}: section numbers must run 01, 02, ... without gaps (found {nums})")
        for s in sections:
            if s.name not in text:
                err(f"{rel}/README.md: does not list section {s.name}")
            st = s.read_text(encoding="utf-8")
            if "## Done when" not in st:
                err(f"{rel}/{s.name}: missing '## Done when'")
        ans = d / "answers"
        if ans.is_dir():
            for a in ans.glob("[0-9][0-9]-answers.md"):
                if not any(s.name.startswith(a.name[:2] + "-") for s in sections):
                    err(f"{rel}/answers/{a.name}: no section {a.name[:2]} for these answers")
        # lesson code blocks must equal the example file they show
        exdir = d / "examples"
        for s in sections:
            st = s.read_text(encoding="utf-8")
            for m in CODE_BLOCK.finditer(st):
                path, code = m.group(1), m.group(2)
                homes = [e for e in exdir.glob("*") if (e / path).is_file()] if exdir.is_dir() else []
                if len(homes) == 1:
                    want = (homes[0] / path).read_text(encoding="utf-8").rstrip("\n")
                    if want != code:
                        err(f"{rel}/{s.name}: code block for `{path}` differs from examples/{homes[0].name}/{path}")
    for uid in sorted(set(done) | set(prog)):
        if not (base / uid / "README.md").is_file():
            err(f"{uid} is in progress or completed but LEARN/{uid}/README.md does not exist "
                "(its learning material must be prepared before the learner begins)")


# ---------------------------------------------------------------- references, pins

def check_refs(cat):
    skip = {"CHANGELOG.md"}
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if ".git" in p.parts or p.name in HISTORY_DOCS or rel.startswith(("ARCHIVE/", "EVIDENCE/")) or p.name in skip:
            continue
        text = p.read_text(encoding="utf-8")
        for tok in set(re.findall(r"`([A-Za-z0-9_./-]+)`", text)):
            is_path = tok.endswith((".md", ".py")) or (("/" in tok) and tok.split("/")[0] in TOP_DIRS)
            if not is_path or tok.startswith("http") or tok.endswith("/"):
                continue
            if tok.startswith(MISSING_OK_PREFIXES) or tok in ("check_course.py", "manifest.md", "evaluation.md", "RESTART_NOTE.md", "explanations.md") or re.search(r"-N\.", tok):
                continue
            if not ((ROOT / tok).exists() or (p.parent / tok).exists()):
                err(f"{rel}: reference `{tok}` does not exist")
        for tgt in set(re.findall(r"\]\(([^)#\s]+)\)", text)):
            if tgt.startswith(("http", "mailto:")):
                continue
            if not (p.parent / tgt).exists():
                err(f"{rel}: link ({tgt}) does not exist")
        for uid in set(re.findall(ID_RE, text)):
            if uid not in cat:
                err(f"{rel}: mentions unlock {uid}, which is not in the catalog")


def check_standard_pin():
    add = read("KNOWLEDGE_STANDARD_ADDENDUM.md")
    m = re.search(r"Pinned sha256:\s*`([0-9a-f]{64})`", add)
    std = ROOT / "KNOWLEDGE_STANDARD.md"
    if not m:
        err("KNOWLEDGE_STANDARD_ADDENDUM.md: missing 'Pinned sha256: `<hash>`' for the standard")
    elif std.is_file() and sha256_file(std) != m.group(1):
        err("KNOWLEDGE_STANDARD.md differs from the pinned hash. It changes only with the learner's "
            "explicit approval; if approved, update the pin and log it")


# ---------------------------------------------------------------- reports

def print_status(cat, done, prog, status):
    print(f"Curriculum status: {status}")
    if status != "APPROVED":
        print("-> Not approved: no unlock may be taught. Discussion and review only.")
    avail = [u for u in cat if u not in done and all(r in done for r in cat[u]["requires"])]
    blocked = [u for u in cat if u not in done and u not in avail]
    print("\nCompleted (%d):" % len(done))
    for u, (_, got, ev) in sorted(done.items()):
        kind = re.search(r"^evidence_kind:\s*(\S+)", read(f"{ev}/manifest.md"), re.M)
        print(f"  {u}  {got}  evidence: {kind.group(1) if kind else 'unknown'}")
    if not done:
        print("  none")
    print(f"In progress ({len(prog)}): {', '.join(prog) or 'none'}")
    note = "" if status == "APPROVED" else " (would be available once approved)"
    print(f"\nAvailable ({len(avail)}){note}:")
    for u in avail:
        tag = "" if cat[u]["def"] == "authored" else "  [planned: author before teaching]"
        print(f"  {u}  {cat[u]['title']} (target {cat[u]['mastery']}, {cat[u]['cls']}){tag}")
    print(f"\nBlocked ({len(blocked)}):")
    for u in blocked:
        missing = [r for r in cat[u]["requires"] if r not in done]
        print(f"  {u}  waiting on {', '.join(missing)}")


def print_budget(cat):
    b = budget_numbers(cat)
    print(f"{'Phase':<6}{'E n':>4}{'E hrs':>7}{'build':>7}{'study':>7}{'verify':>7}{'consol':>7}{'O hrs':>7}")
    tot = [0, 0, 0, 0]
    te = to = 0
    for ph, (n, eh, parts, oh) in b.items():
        tot = [a + c for a, c in zip(tot, parts)]
        te += eh
        to += oh
        print(f"{'PX' if ph == 99 else ph:<6}{n:>4}{eh:>7}{parts[0]:>7}{parts[1]:>7}{parts[2]:>7}{parts[3]:>7}{oh:>7}")
    print(f"{'Total':<6}{'':>4}{te:>7}{tot[0]:>7}{tot[1]:>7}{tot[2]:>7}{tot[3]:>7}{to:>7}")
    print(f"\nEssential {te} h = {te / 10:.1f} weeks at 10 h/week. Optional pool {to} h (includes stretch).")


def print_mermaid(cat):
    print("flowchart LR")
    for uid in cat:
        print(f'  {uid.replace("-", "_")}["{uid}"]')
    for uid, u in cat.items():
        for r in u["requires"]:
            print(f'  {r.replace("-", "_")} --> {uid.replace("-", "_")}')


# ---------------------------------------------------------------- main

def main(argv):
    cat = load_catalog()
    check_structure()
    check_graph(cat)
    check_unlock_files(cat)
    done, prog = load_state(cat)
    check_evidence(cat)
    status = check_curriculum(cat)
    if (done or prog) and status != "APPROVED":
        err("LEARNER_STATE.md records progress but CURRICULUM.md is not APPROVED")
    check_learn(cat, done, prog)
    check_refs(cat)
    check_standard_pin()

    if "--fingerprint" in argv:
        print(fingerprint(cat))
    if "--mermaid" in argv:
        print_mermaid(cat)
    if "--budget" in argv:
        print_budget(cat)
    if "--status" in argv:
        print_status(cat, done, prog, status)
    informational = any(a in argv for a in ("--fingerprint", "--mermaid", "--budget", "--status"))
    if not informational or "--status" in argv or "--budget" in argv:
        authored = sum(1 for u in cat.values() if u["def"] == "authored")
        print(f"\nCatalog: {len(cat)} unlocks ({authored} authored, {len(cat) - authored} planned)")

    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if errors:
        print(f"RESULT: FAIL ({len(errors)} error(s), {len(warnings)} warning(s))", file=sys.stderr)
        return 1
    print(f"RESULT: OK ({len(warnings)} warning(s)). Structure, graph, files, declared dependencies, hashes "
          "and references are consistent. Evidence commands were NOT executed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
