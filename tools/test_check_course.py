#!/usr/bin/env python3
"""Behavioural tests for check_course.py. Python 3.9+, standard library only.

Run:  python3 tools/test_check_course.py
Each test copies the repository to a temporary directory, optionally adds a valid evidence
fixture, applies ONE deliberate error, and runs the real checker as a subprocess.
Nothing in the real repository is modified.
"""
import hashlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
UID = "P0-GO-01"
ATT = "2026-12-01-1"
BUNDLE = f"EVIDENCE/{UID}/{ATT}"


def run(root, *args):
    p = subprocess.run([sys.executable, str(root / "tools" / "check_course.py"), *args],
                       capture_output=True, text=True, cwd=root)
    return p.returncode, p.stdout, p.stderr


def make_copy():
    tmp = Path(tempfile.mkdtemp(prefix="coursecheck-"))
    shutil.copytree(REPO, tmp / "r", ignore=shutil.ignore_patterns(".git", "__pycache__"))
    return tmp / "r"


def edit(root, rel, old, new):
    p = root / rel
    t = p.read_text()
    assert old in t, (rel, old)
    p.write_text(t.replace(old, new, 1))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def add_valid_fixture(root):
    """An APPROVED curriculum with one completed unlock and a valid evidence bundle."""
    _, fp, _ = run(root, "--fingerprint")
    fp = fp.strip().splitlines()[0]
    edit(root, "CURRICULUM.md", "status: PROPOSED\napproved_by: none\napproved_on: none\ncatalog_fingerprint: none",
         f"status: APPROVED\napproved_by: test learner\napproved_on: 2026-12-01\ncatalog_fingerprint: {fp}")
    b = root / BUNDLE
    (b / "artifacts" / "src").mkdir(parents=True)
    code = b"package main\nfunc main() {}\n"
    out = b"ok\n"
    (b / "artifacts" / "src" / "main.go").write_bytes(code)        # source is allowed inside a bundle
    (b / "artifacts" / "out.txt").write_bytes(out)
    (b / "evaluation.md").write_text(
        f"# Evaluation\n\n- **Result:** passed\n- **Mastery shown:** L3 (target L3)\n")
    (b / "manifest.md").write_text(f"""# Manifest

unlock: {UID}
capability: A tested hex dump command builds and passes its tests from a clean copy.
evidence_kind: preserved
implementation_attempt: 1
provenance: PRJ-LABS, directory xd/ of the learner workspace, no version control
reproduced_by: n/a

## Environment
- os: Linux 6.1
- arch: x86_64
- toolchain: go 1.22

## Setup
- none

## Artifacts
| path | sha256 | role | description |
|---|---|---|---|
| src/main.go | {sha(code)} | code | entry point |
| out.txt | {sha(out)} | output | captured test output |

## Commands
| # | command | working dir | expected | observed | exit |
|---|---|---|---|---|---|
| 1 | go test ./... | artifacts/src | all packages pass | ok | 0 |

## Limitations
- none known
""")
    edit(root, "LEARNER_STATE.md", "|---|---|---|---|---|\n",
         f"|---|---|---|---|---|\n| {UID} | 2026-12-01 | L3 | {BUNDLE} | 6 |\n")


class Base(unittest.TestCase):
    def setUp(self):
        self.root = make_copy()
        self.addCleanup(shutil.rmtree, self.root.parent, ignore_errors=True)

    def fails(self, needle, *args):
        code, out, err = run(self.root, *args)
        self.assertEqual(code, 1, f"expected exit 1\nstdout:{out}\nstderr:{err}")
        self.assertIn("ERROR:", err)
        self.assertIn(needle, err, err)
        self.assertIn("RESULT: FAIL", err)
        return out, err

    def passes(self, *args):
        code, out, err = run(self.root, *args)
        self.assertEqual(code, 0, f"expected exit 0\nstdout:{out}\nstderr:{err}")
        self.assertNotIn("ERROR:", err)
        return out


class RealRepository(Base):
    def test_valid_repository_passes_in_every_mode(self):
        for mode in ([], ["--status"], ["--budget"], ["--mermaid"], ["--fingerprint"]):
            self.passes(*mode)

    def test_modes_print_reports_on_stdout(self):
        self.assertIn("flowchart LR", self.passes("--mermaid"))
        self.assertIn("Essential", self.passes("--budget"))
        self.assertIn("Curriculum status", self.passes("--status"))


class ReportingModesKeepFailures(Base):
    """The early-return bug: a reporting mode must not hide validation errors."""

    def test_every_mode_reports_a_graph_error(self):
        edit(self.root, "UNLOCKS/CATALOG.md", "| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01 |",
             "| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01, P3-ZZZ-01 |")
        for mode in ([], ["--status"], ["--budget"], ["--mermaid"], ["--fingerprint"]):
            with self.subTest(mode=mode):
                self.fails("P0-GO-02: requires unknown unlock P3-ZZZ-01", *mode)
        # informational output stays clean of error text
        out, _ = self.fails("unknown unlock", "--mermaid")
        self.assertNotIn("ERROR", out)

    def test_malformed_prerequisite_is_not_silently_dropped(self):
        edit(self.root, "UNLOCKS/CATALOG.md", "| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01 |",
             "| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01, P9-NOPE-01 |")
        for mode in ([], ["--budget"], ["--mermaid"]):
            with self.subTest(mode=mode):
                self.fails("malformed prerequisite 'P9-NOPE-01'", *mode)


class Structure(Base):
    def test_missing_directory(self):
        shutil.rmtree(self.root / "knowledge")
        self.fails("required directory missing: knowledge/")

    def test_missing_required_file(self):
        (self.root / "project" / "PLAN.md").unlink()
        self.fails("required file missing: project/PLAN.md")

    def test_misplaced_canonical_document(self):
        shutil.copy(self.root / "career" / "CAREER_RESEARCH.md", self.root / "CAREER_RESEARCH.md")
        self.fails("canonical location is career/CAREER_RESEARCH.md")

    def test_retired_document_name(self):
        (self.root / "PROJECTS.md").write_text("# old\n")
        self.fails("retired document name")

    def test_source_code_outside_bundles(self):
        (self.root / "project" / "main.go").write_text("package main\n")
        self.fails("source code does not belong here")

    def test_archive_without_restart_note(self):
        (self.root / "ARCHIVE" / "learning-attempt-1-2027-01-01").mkdir()
        self.fails("missing RESTART_NOTE.md")

    def test_standard_changed_without_approval(self):
        (self.root / "KNOWLEDGE_STANDARD.md").write_text((self.root / "KNOWLEDGE_STANDARD.md").read_text() + "\nedit\n")
        self.fails("differs from the pinned hash")

    def test_standard_status_line_edit_is_caught(self):
        edit(self.root, "KNOWLEDGE_STANDARD.md", "Status: Proposed", "Status: Accepted")
        self.fails("differs from the pinned hash")


class GraphAndCatalog(Base):
    def test_cycle(self):
        edit(self.root, "UNLOCKS/CATALOG.md", "| P0-GO-01 | Set up Go and ship a tested command-line tool | — |",
             "| P0-GO-01 | Set up Go and ship a tested command-line tool | P0-BIT-01 |")
        self.fails("cycle through")

    def test_essential_requires_optional(self):
        edit(self.root, "UNLOCKS/CATALOG.md", "| P1-API-01 | HTTP API skeleton and resource design | P0-NET-01, P1-PG-02 |",
             "| P1-API-01 | HTTP API skeleton and resource design | P0-NET-02, P1-PG-02 |")
        self.fails("essential unlock requires optional P0-NET-02")

    def test_bad_hours(self):
        edit(self.root, "UNLOCKS/CATALOG.md", "| 3+1+1+1 | authored |", "| 3+1+1 | authored |")
        self.fails("hours must look like")

    def test_unlock_header_drift(self):
        edit(self.root, "UNLOCKS/P0-BIT-05.md", "requires: [P0-BIT-02]", "requires: [P0-BIT-04]")
        self.fails("header requires differ from catalog")

    def test_uses_line_naming_a_non_prerequisite(self):
        edit(self.root, "UNLOCKS/P0-BIT-06.md", "Uses: the `codec` package (P0-BIT-05).",
             "Uses: the `pack` package (P0-BIT-04).")
        self.fails("not a (transitive) prerequisite")

    def test_prerequisite_text_drift(self):
        edit(self.root, "UNLOCKS/P0-BIT-07.md", "`P0-BIT-03`, `P0-BIT-04`, `P0-BIT-06`.", "`P0-BIT-03`, `P0-BIT-06`.")
        self.fails("Prerequisites text names")

    def test_unknown_unlock_mentioned(self):
        edit(self.root, "README.md", "# Engineering Course Control Plane", "# Engineering Course Control Plane\n\nSee P3-ZZZ-01.\n")
        self.fails("mentions unlock P3-ZZZ-01")


class CurriculumAndCuts(Base):
    def test_cut_order_that_contradicts_c5(self):
        edit(self.root, "CURRICULUM.md", "cut_order: P5-PY-01,P5-LLM-01,P5-AI-01,P5-INT-01 | P6-PERF-01 | P0-INT-01",
             "cut_order: P5-PY-01,P5-LLM-01,P5-AI-01,P5-INT-01 | P4-OBS-03 | P4-K8S-01")
        code, _, err = run(self.root)
        self.assertEqual(code, 1)
        self.assertIn("strands P4-OPS-01", err)
        self.assertIn("protected criterion C5", err)

    def test_cut_that_strands_an_essential_unlock(self):
        edit(self.root, "CURRICULUM.md", "| P6-PERF-01 | P0-INT-01", "| P1-SDK-01 | P0-INT-01")
        code, _, err = run(self.root)
        self.assertEqual(code, 1)
        self.assertIn("strands P2-IDEM-01", err)

    def test_budget_prose_drift(self):
        edit(self.root, "CURRICULUM.md", "**Essential plan: 362 hours.**", "**Essential plan: 357 hours.**")
        self.fails("states essential plan 357")

    def test_budget_table_drift(self):
        edit(self.root, "CURRICULUM.md", "| 2 Reliability | 8 | 55 |", "| 2 Reliability | 8 | 52 |")
        self.fails("hours table, phase 2")

    def test_missing_completion_proof_row(self):
        edit(self.root, "COURSE_OBJECTIVE.md", "| C8 | P6-CAR-01 | no |\n", "")
        self.fails("no completion-proof row for C8")

    def test_progress_recorded_while_proposed(self):
        text = (self.root / "LEARNER_STATE.md").read_text()
        i = text.index("## In progress")
        j = text.index("|---|---|---|", i)
        k = text.index("\n", j)
        (self.root / "LEARNER_STATE.md").write_text(text[:k + 1] + "| P0-GO-01 | 2026-12-01 | trying |\n" + text[k + 1:])
        self.fails("records progress but CURRICULUM.md is not APPROVED")

    def test_approved_without_fingerprint(self):
        edit(self.root, "CURRICULUM.md", "status: PROPOSED\napproved_by: none", "status: APPROVED\napproved_by: x")
        self.fails("no catalog_fingerprint recorded")

    def test_boundary_change_after_approval(self):
        add_valid_fixture(self.root)
        self.passes()
        edit(self.root, "UNLOCKS/CATALOG.md", "| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01 | L3 | E | 4+1+1+1 |",
             "| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01 | L3 | E | 4+1+1+2 |")
        edit(self.root, "CURRICULUM.md", "**Essential plan: 362 hours.**", "**Essential plan: 363 hours.**")
        code, _, err = run(self.root)
        self.assertEqual(code, 1)
        self.assertIn("catalog boundaries", err)

    def test_authoring_a_planned_unlock_does_not_trip_the_fingerprint(self):
        add_valid_fixture(self.root)
        # Only the Definition cell may change after approval; fingerprint excludes it.
        edit(self.root, "UNLOCKS/CATALOG.md", "| 1+4+1+1 | planned |", "| 1+4+1+1 | authored |")
        code, _, err = run(self.root)
        self.assertNotIn("catalog boundaries", err)  # fails only because the file does not exist
        self.assertIn("catalog says authored but file is missing", err)


class Evidence(Base):
    def setUp(self):
        super().setUp()
        add_valid_fixture(self.root)

    def test_valid_fixture_passes_and_status_shows_evidence_kind(self):
        self.passes()
        self.assertIn("evidence: preserved", self.passes("--status"))

    def test_missing_manifest(self):
        (self.root / BUNDLE / "manifest.md").unlink()
        self.fails("missing manifest.md")

    def test_missing_manifest_field(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "capability: A tested hex dump command builds and passes its tests from a clean copy.\n", "")
        self.fails("field 'capability' missing")

    def test_placeholder_field(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "provenance: PRJ-LABS, directory xd/ of the learner workspace, no version control", "provenance: <where>")
        self.fails("field 'provenance' missing or still a placeholder")

    def test_artifact_hash_mismatch(self):
        (self.root / BUNDLE / "artifacts" / "out.txt").write_bytes(b"changed\n")
        self.fails("does not match its manifest sha256")

    def test_unlisted_artifact(self):
        (self.root / BUNDLE / "artifacts" / "extra.txt").write_text("x")
        self.fails("is not listed in the manifest")

    def test_listed_artifact_missing(self):
        (self.root / BUNDLE / "artifacts" / "out.txt").unlink()
        self.fails("it does not exist")

    def test_copied_dependency_directory(self):
        d = self.root / BUNDLE / "artifacts" / "node_modules"
        d.mkdir()
        (d / "x.txt").write_text("x")
        self.fails("must not be copied")

    def test_non_integer_exit_status(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "| ok | 0 |", "| ok | zero |")
        self.fails("exit status must be an integer")

    def test_independent_claim_without_reproducer(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "evidence_kind: preserved", "evidence_kind: independently-reproduced")
        self.fails("independently-reproduced needs 'reproduced_by'")

    def test_unknown_evidence_kind(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "evidence_kind: preserved", "evidence_kind: trust-me")
        self.fails("evidence_kind must be")

    def test_missing_toolchain(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "- toolchain: go 1.22\n", "")
        self.fails("Environment needs a '- toolchain")

    def test_machine_path(self):
        edit(self.root, f"{BUNDLE}/manifest.md", "directory xd/ of the learner workspace", "/home/someone/work/xd")
        self.fails("machine-specific absolute path")

    def test_evaluation_without_result(self):
        edit(self.root, f"{BUNDLE}/evaluation.md", "- **Result:** passed\n", "")
        self.fails("needs '**Result:**")

    def test_state_points_to_missing_bundle(self):
        edit(self.root, "LEARNER_STATE.md", BUNDLE, f"EVIDENCE/{UID}/2026-12-02-1")
        self.fails("evidence must be an existing")

    def test_state_mastery_differs_from_evaluation(self):
        edit(self.root, f"{BUNDLE}/evaluation.md", "L3 (target L3)", "L4 (target L3)")
        self.fails("differs from evaluation")

    def test_evaluation_not_passed(self):
        edit(self.root, f"{BUNDLE}/evaluation.md", "passed", "not yet")
        self.fails("does not record Result: passed")

    def test_stray_file_outside_attempt_directory(self):
        (self.root / "EVIDENCE" / UID / "notes.md").write_text("x")
        self.fails("expected an attempt directory")

    def test_evidence_for_unknown_unlock(self):
        (self.root / "EVIDENCE" / "P9-NOPE-01").mkdir()
        self.fails("not an unlock in the catalog")


class References(Base):
    def test_broken_path_reference(self):
        edit(self.root, "README.md", "# Engineering Course Control Plane", "# Engineering Course Control Plane\n\nSee `project/PLANX.md`.\n")
        self.fails("reference `project/PLANX.md` does not exist")

    def test_broken_link(self):
        edit(self.root, "README.md", "# Engineering Course Control Plane", "# Engineering Course Control Plane\n\n[x](nofile.md)\n")
        self.fails("link (nofile.md) does not exist")

    def test_future_design_documents_are_allowed(self):
        edit(self.root, "README.md", "# Engineering Course Control Plane", "# Engineering Course Control Plane\n\nSee `project/design/later.md`.\n")
        self.passes()


if __name__ == "__main__":
    unittest.main(verbosity=2)
