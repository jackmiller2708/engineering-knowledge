# Final Review Package

Prepared 2026-11-16 for an independent reviewer. **This is a handoff for review, not authorization to change anything.** The curriculum is `PROPOSED`. Nothing is approved or merged. No curriculum content was changed while preparing this package, apart from the single F3 clarification in section 4.3.

## Base and candidate (provenance)

| | |
|---|---|
| **Original base: the only commit on the working branch** | `6e1b12ae18ce1af2458d2fcadaa9092472cd7903` ("Initialize engineering course control plane") |
| Review branch | `review/final-curriculum-candidate` |
| Candidate commit | the tip of `review/final-curriculum-candidate`. A commit cannot contain its own hash, so read it from `git log` on that branch or from the handoff message |
| Original working branch `ccr-b573edbb-crcfsw` | not modified; still at the base hash above |
| Everything the reviewer should diff | `git diff 6e1b12ae18ce1af2458d2fcadaa9092472cd7903..review/final-curriculum-candidate` |

Every change in this package is traceable to the base hash above: `FINAL_REVIEW_PACKAGE.patch` is the complete change set against it, excluding the two package files themselves.

**Revision note.** This package was first assembled before review finding F3 was resolved. It has been regenerated. Compared with that first version, exactly three files differ: `UNLOCKS/P2-CONS-01.md` (acceptance criterion 4 only; section 4.3), `DECISION_LOG.md` (entry D-006 appended), and `SESSION_HANDOFF.md` (two lines about the branch). The state recorded in section 1 was captured before the F3 edit and is kept unchanged as the provenance of the first capture; sections 2 to 7 describe the candidate.

## 0. Contents and how to use them

| Item | Where |
|---|---|
| This report: provenance, state, manifest, verification evidence, unvalidated areas, findings | `FINAL_REVIEW_PACKAGE.md` |
| The complete change set against the base, as one patch (tracked diff, then the four new files as full new-file diffs) | `FINAL_REVIEW_PACKAGE.patch` |

The patch is 192726 bytes and 2570 lines, so it was not split.

**Reproduce the candidate tree from the base:** check out the base hash into an empty directory, then run `git apply FINAL_REVIEW_PACKAGE.patch`. I did exactly this and compared with `diff -r`: the result is identical to the candidate working tree, excluding the two package files (section 2).

## 1. State captured before the F3 edit (first capture, preserved as provenance)

```text
$ git status --short
 M CLAUDE.md
 M COURSE_OBJECTIVE.md
 M CURRICULUM.md
 M DECISION_LOG.md
 M KNOWLEDGE_STANDARD_ADDENDUM.md
 M LEARNER_STATE.md
 M PHASES/PHASE-0.md
 M PHASES/PHASE-2.md
 M PHASES/PHASE-3.md
 M PHASES/PHASE-4.md
 M PROCEDURES.md
 M README.md
 M REVIEW_REPORT.md
 M SESSION_HANDOFF.md
 M TEMPLATES/EVALUATION.md
 M TEMPLATES/LEARNER_STATE.initial.md
 M TEMPLATES/UNLOCK.md
 M UNLOCKS/CATALOG.md
 M UNLOCKS/P0-BIT-01.md
 M UNLOCKS/P0-BIT-02.md
 M UNLOCKS/P0-BIT-03.md
 M UNLOCKS/P0-BIT-04.md
 M UNLOCKS/P0-BIT-05.md
 M UNLOCKS/P0-BIT-06.md
 M UNLOCKS/P0-BIT-07.md
 M UNLOCKS/P1-DEF-01.md
 M UNLOCKS/P1-PG-03.md
 M UNLOCKS/P1-SM-01.md
 M UNLOCKS/P2-IDEM-01.md
 M UNLOCKS/P3-Q-01.md
 M UNLOCKS/README.md
 M career/CAREER_RESEARCH.md
 M project/DECISIONS.md
 M project/PLAN.md
 M project/README.md
 M tools/check_course.py
?? TEMPLATES/MANIFEST.md
?? UNLOCKS/P2-CONS-01.md
?? career/POSTINGS.md
?? tools/test_check_course.py

$ git rev-parse HEAD
6e1b12ae18ce1af2458d2fcadaa9092472cd7903

$ git log --oneline -3
6e1b12a Initialize engineering course control plane (curriculum proposed, not approved)

$ git branch --show-current
ccr-b573edbb-crcfsw

$ git diff --stat HEAD
 CLAUDE.md                          |  12 +-
 COURSE_OBJECTIVE.md                |  23 +-
 CURRICULUM.md                      |  38 +--
 DECISION_LOG.md                    |  22 ++
 KNOWLEDGE_STANDARD_ADDENDUM.md     |   2 +
 LEARNER_STATE.md                   |   5 +-
 PHASES/PHASE-0.md                  |   4 +-
 PHASES/PHASE-2.md                  |   8 +-
 PHASES/PHASE-3.md                  |   4 +-
 PHASES/PHASE-4.md                  |   2 +-
 PROCEDURES.md                      |  85 ++++--
 README.md                          |   4 +-
 REVIEW_REPORT.md                   |  54 ++--
 SESSION_HANDOFF.md                 |  18 +-
 TEMPLATES/EVALUATION.md            |  18 +-
 TEMPLATES/LEARNER_STATE.initial.md |   5 +-
 TEMPLATES/UNLOCK.md                |   2 +
 UNLOCKS/CATALOG.md                 |  14 +-
 UNLOCKS/P0-BIT-01.md               |   1 +
 UNLOCKS/P0-BIT-02.md               |   1 +
 UNLOCKS/P0-BIT-03.md               |   1 +
 UNLOCKS/P0-BIT-04.md               |   3 +-
 UNLOCKS/P0-BIT-05.md               |   1 +
 UNLOCKS/P0-BIT-06.md               |   1 +
 UNLOCKS/P0-BIT-07.md               |   5 +-
 UNLOCKS/P1-DEF-01.md               |   1 +
 UNLOCKS/P1-PG-03.md                |   7 +-
 UNLOCKS/P1-SM-01.md                |   1 +
 UNLOCKS/P2-IDEM-01.md              |   9 +-
 UNLOCKS/P3-Q-01.md                 |   3 +-
 UNLOCKS/README.md                  |  24 +-
 career/CAREER_RESEARCH.md          | 102 ++++---
 project/DECISIONS.md               |  10 +-
 project/PLAN.md                    |  47 +++-
 project/README.md                  |  14 +-
 tools/check_course.py              | 529 ++++++++++++++++++++++++++++++++-----
 36 files changed, 828 insertions(+), 252 deletions(-)

$ git ls-files --others --exclude-standard
TEMPLATES/MANIFEST.md
UNLOCKS/P2-CONS-01.md
career/POSTINGS.md
tools/test_check_course.py

$ git diff --cached --stat   (staged changes; expect none)
(end)
```

Nothing was staged. Branch `ccr-b573edbb-crcfsw`; the base was the only commit.

Remote state captured before this publishing step:

```text
$ git branch --show-current
ccr-b573edbb-crcfsw

$ git rev-parse HEAD ccr-b573edbb-crcfsw
6e1b12ae18ce1af2458d2fcadaa9092472cd7903
6e1b12ae18ce1af2458d2fcadaa9092472cd7903

$ git branch -a -vv
* ccr-b573edbb-crcfsw                6e1b12a [origin/ccr-b573edbb-crcfsw] Initialize engineering course control plane (curriculum proposed, not approved)
  remotes/origin/ccr-b573edbb-crcfsw 6e1b12a Initialize engineering course control plane (curriculum proposed, not approved)

$ git remote -v
origin	https://github.com/jackmiller2708/engineering-knowledge (fetch)
origin	https://github.com/jackmiller2708/engineering-knowledge (push)

$ git ls-remote --symref origin HEAD   (default branch)
ref: refs/heads/ccr-b573edbb-crcfsw	HEAD
6e1b12ae18ce1af2458d2fcadaa9092472cd7903	HEAD

$ git ls-remote --heads origin
6e1b12ae18ce1af2458d2fcadaa9092472cd7903	refs/heads/ccr-b573edbb-crcfsw

$ git status --short | wc -l
42
```

## 2. The complete change set

- File: `FINAL_REVIEW_PACKAGE.patch`
- sha256: `134f9cb9b03c759b430f1618234cdf1f6e8466095a616e751ff863572039ed12`
- 40 file diffs: 36 modified files followed by 4 new files.
- Verified: the base plus this patch equals the candidate working tree excluding the two package files (`git apply --check` passed; `diff -r -x .git` reported no differences).

### 2.1 Manifest (Patch line = first line of that file's diff inside the patch)

| # | File | Status | Lines | Patch line |
|---|---|---|---|---|
| 1 | CLAUDE.md | M | +8 / -4 | 1 |
| 2 | COURSE_OBJECTIVE.md | M | +19 / -4 | 44 |
| 3 | CURRICULUM.md | M | +21 / -17 | 80 |
| 4 | DECISION_LOG.md | M | +40 / -0 | 185 |
| 5 | KNOWLEDGE_STANDARD_ADDENDUM.md | M | +2 / -0 | 233 |
| 6 | LEARNER_STATE.md | M | +3 / -2 | 246 |
| 7 | PHASES/PHASE-0.md | M | +2 / -2 | 269 |
| 8 | PHASES/PHASE-2.md | M | +4 / -4 | 290 |
| 9 | PHASES/PHASE-3.md | M | +2 / -2 | 322 |
| 10 | PHASES/PHASE-4.md | M | +1 / -1 | 339 |
| 11 | PROCEDURES.md | M | +69 / -16 | 352 |
| 12 | README.md | M | +3 / -1 | 467 |
| 13 | REVIEW_REPORT.md | M | +32 / -22 | 489 |
| 14 | SESSION_HANDOFF.md | M | +12 / -8 | 599 |
| 15 | TEMPLATES/EVALUATION.md | M | +10 / -8 | 642 |
| 16 | TEMPLATES/LEARNER_STATE.initial.md | M | +3 / -2 | 679 |
| 17 | TEMPLATES/UNLOCK.md | M | +2 / -0 | 702 |
| 18 | UNLOCKS/CATALOG.md | M | +7 / -7 | 715 |
| 19 | UNLOCKS/P0-BIT-01.md | M | +1 / -0 | 779 |
| 20 | UNLOCKS/P0-BIT-02.md | M | +1 / -0 | 791 |
| 21 | UNLOCKS/P0-BIT-03.md | M | +1 / -0 | 803 |
| 22 | UNLOCKS/P0-BIT-04.md | M | +2 / -1 | 815 |
| 23 | UNLOCKS/P0-BIT-05.md | M | +1 / -0 | 833 |
| 24 | UNLOCKS/P0-BIT-06.md | M | +1 / -0 | 845 |
| 25 | UNLOCKS/P0-BIT-07.md | M | +3 / -2 | 857 |
| 26 | UNLOCKS/P1-DEF-01.md | M | +1 / -0 | 880 |
| 27 | UNLOCKS/P1-PG-03.md | M | +4 / -3 | 892 |
| 28 | UNLOCKS/P1-SM-01.md | M | +1 / -0 | 924 |
| 29 | UNLOCKS/P2-IDEM-01.md | M | +5 / -4 | 936 |
| 30 | UNLOCKS/P3-Q-01.md | M | +2 / -1 | 972 |
| 31 | UNLOCKS/README.md | M | +21 / -3 | 993 |
| 32 | career/CAREER_RESEARCH.md | M | +45 / -57 | 1042 |
| 33 | project/DECISIONS.md | M | +9 / -1 | 1173 |
| 34 | project/PLAN.md | M | +41 / -6 | 1198 |
| 35 | project/README.md | M | +12 / -2 | 1272 |
| 36 | tools/check_course.py | M | +456 / -73 | 1301 |
| 37 | TEMPLATES/MANIFEST.md | A (new file) | +38 / -0 | 2002 |
| 38 | UNLOCKS/P2-CONS-01.md | A (new file) | +70 / -0 | 2046 |
| 39 | career/POSTINGS.md | A (new file) | +66 / -0 | 2122 |
| 40 | tools/test_check_course.py | A (new file) | +371 / -0 | 2194 |

### 2.2 New files (their complete contents are the last four diffs in the patch)

| File | Lines | Bytes | sha256 |
|---|---|---|---|
| TEMPLATES/MANIFEST.md | 38 | 1851 | 77d296582eb269abc84b1ea3bc1e2739786d33c97dc1127af93873cf0efec70d |
| UNLOCKS/P2-CONS-01.md | 70 | 7180 | c2fdd7d6bdc541d837d15af28c5798e44cb63f51632851733308dacf546a4336 |
| career/POSTINGS.md | 66 | 10909 | 39842b916b36440d141241091d84b774614fcba48d636a1fcf2a361c7d1efec0 |
| tools/test_check_course.py | 371 | 16034 | 26afb606debf543fb9b108bfe19c1c77fcd035247b276165b9ce10dc452f86b1 |

`KNOWLEDGE_STANDARD.md` is not in the change set: it is byte-identical to the learner's supplied file and unchanged since the base.

## 3. Verification evidence (actual commands and outputs, after the F3 edit)

All outputs below were produced in the candidate working tree on 2026-11-16 and are copied unedited, except that the long `--mermaid` listing is shortened here and given in full in Appendix A. Sections 3.1 and 3.2 were re-run after the F3 edit.

### 3.1 Checker, four modes

```text
$ python3 tools/check_course.py 
--- stdout (3 lines)

Catalog: 81 unlocks (14 authored, 67 planned)
RESULT: OK (0 warning(s)). Structure, graph, files, declared dependencies, hashes and references are consistent. Evidence commands were NOT executed.
--- stderr
--- exit code: 0

$ python3 tools/check_course.py --budget
--- stdout (15 lines)
Phase  E n  E hrs  build  study verify consol  O hrs
0       14     86     45     19     15      7     43
1       14     81     42     17     15      7      6
2        8     55     27     10     11      7      0
3        7     45     22      7      9      7     18
4        9     45     24      8     11      2     11
5        4     20     11      3      4      2     12
6        5     30     16      4      5      5      4
PX       0      0      0      0      0      0     30
Total         362    187     68     70     37    124

Essential 362 h = 36.2 weeks at 10 h/week. Optional pool 124 h (includes stretch).

Catalog: 81 unlocks (14 authored, 67 planned)
RESULT: OK (0 warning(s)). Structure, graph, files, declared dependencies, hashes and references are consistent. Evidence commands were NOT executed.
--- stderr
--- exit code: 0

$ python3 tools/check_course.py --mermaid
--- stdout (206 lines)
flowchart LR
  P0_CAR_01["P0-CAR-01"]
  P0_GO_01["P0-GO-01"]
  P0_GO_02["P0-GO-02"]
  P0_GO_03["P0-GO-03"]
  ... (206 lines total; full graph in appendix)
  P2_REC_01 --> PX_REPLAY_01
RESULT: OK (0 warning(s)). Structure, graph, files, declared dependencies, hashes and references are consistent. Evidence commands were NOT executed.
--- stderr
--- exit code: 0

$ python3 tools/check_course.py --fingerprint
--- stdout (2 lines)
d28afa7b918bda26c5780f862edbae4f812fe07d4c14af9c03910eb3143b381e
RESULT: OK (0 warning(s)). Structure, graph, files, declared dependencies, hashes and references are consistent. Evidence commands were NOT executed.
--- stderr
--- exit code: 0
```

Observation: in `--mermaid` mode the success line `RESULT: OK` is printed on stdout after the diagram, so piping that mode into a diagram renderer includes a non-diagram line (finding F1).

### 3.2 The 50 checker tests (`python3 tools/test_check_course.py -v`; tests exit code: 0)

```text
test_approved_without_fingerprint (__main__.CurriculumAndCuts.test_approved_without_fingerprint) ... ok
test_authoring_a_planned_unlock_does_not_trip_the_fingerprint (__main__.CurriculumAndCuts.test_authoring_a_planned_unlock_does_not_trip_the_fingerprint) ... ok
test_boundary_change_after_approval (__main__.CurriculumAndCuts.test_boundary_change_after_approval) ... ok
test_budget_prose_drift (__main__.CurriculumAndCuts.test_budget_prose_drift) ... ok
test_budget_table_drift (__main__.CurriculumAndCuts.test_budget_table_drift) ... ok
test_cut_order_that_contradicts_c5 (__main__.CurriculumAndCuts.test_cut_order_that_contradicts_c5) ... ok
test_cut_that_strands_an_essential_unlock (__main__.CurriculumAndCuts.test_cut_that_strands_an_essential_unlock) ... ok
test_missing_completion_proof_row (__main__.CurriculumAndCuts.test_missing_completion_proof_row) ... ok
test_progress_recorded_while_proposed (__main__.CurriculumAndCuts.test_progress_recorded_while_proposed) ... ok
test_artifact_hash_mismatch (__main__.Evidence.test_artifact_hash_mismatch) ... ok
test_copied_dependency_directory (__main__.Evidence.test_copied_dependency_directory) ... ok
test_evaluation_not_passed (__main__.Evidence.test_evaluation_not_passed) ... ok
test_evaluation_without_result (__main__.Evidence.test_evaluation_without_result) ... ok
test_evidence_for_unknown_unlock (__main__.Evidence.test_evidence_for_unknown_unlock) ... ok
test_independent_claim_without_reproducer (__main__.Evidence.test_independent_claim_without_reproducer) ... ok
test_listed_artifact_missing (__main__.Evidence.test_listed_artifact_missing) ... ok
test_machine_path (__main__.Evidence.test_machine_path) ... ok
test_missing_manifest (__main__.Evidence.test_missing_manifest) ... ok
test_missing_manifest_field (__main__.Evidence.test_missing_manifest_field) ... ok
test_missing_toolchain (__main__.Evidence.test_missing_toolchain) ... ok
test_non_integer_exit_status (__main__.Evidence.test_non_integer_exit_status) ... ok
test_placeholder_field (__main__.Evidence.test_placeholder_field) ... ok
test_state_mastery_differs_from_evaluation (__main__.Evidence.test_state_mastery_differs_from_evaluation) ... ok
test_state_points_to_missing_bundle (__main__.Evidence.test_state_points_to_missing_bundle) ... ok
test_stray_file_outside_attempt_directory (__main__.Evidence.test_stray_file_outside_attempt_directory) ... ok
test_unknown_evidence_kind (__main__.Evidence.test_unknown_evidence_kind) ... ok
test_unlisted_artifact (__main__.Evidence.test_unlisted_artifact) ... ok
test_valid_fixture_passes_and_status_shows_evidence_kind (__main__.Evidence.test_valid_fixture_passes_and_status_shows_evidence_kind) ... ok
test_bad_hours (__main__.GraphAndCatalog.test_bad_hours) ... ok
test_cycle (__main__.GraphAndCatalog.test_cycle) ... ok
test_essential_requires_optional (__main__.GraphAndCatalog.test_essential_requires_optional) ... ok
test_prerequisite_text_drift (__main__.GraphAndCatalog.test_prerequisite_text_drift) ... ok
test_unknown_unlock_mentioned (__main__.GraphAndCatalog.test_unknown_unlock_mentioned) ... ok
test_unlock_header_drift (__main__.GraphAndCatalog.test_unlock_header_drift) ... ok
test_uses_line_naming_a_non_prerequisite (__main__.GraphAndCatalog.test_uses_line_naming_a_non_prerequisite) ... ok
test_modes_print_reports_on_stdout (__main__.RealRepository.test_modes_print_reports_on_stdout) ... ok
test_valid_repository_passes_in_every_mode (__main__.RealRepository.test_valid_repository_passes_in_every_mode) ... ok
test_broken_link (__main__.References.test_broken_link) ... ok
test_broken_path_reference (__main__.References.test_broken_path_reference) ... ok
test_future_design_documents_are_allowed (__main__.References.test_future_design_documents_are_allowed) ... ok
test_every_mode_reports_a_graph_error (__main__.ReportingModesKeepFailures.test_every_mode_reports_a_graph_error) ... ok
test_malformed_prerequisite_is_not_silently_dropped (__main__.ReportingModesKeepFailures.test_malformed_prerequisite_is_not_silently_dropped) ... ok
test_archive_without_restart_note (__main__.Structure.test_archive_without_restart_note) ... ok
test_misplaced_canonical_document (__main__.Structure.test_misplaced_canonical_document) ... ok
test_missing_directory (__main__.Structure.test_missing_directory) ... ok
test_missing_required_file (__main__.Structure.test_missing_required_file) ... ok
test_retired_document_name (__main__.Structure.test_retired_document_name) ... ok
test_source_code_outside_bundles (__main__.Structure.test_source_code_outside_bundles) ... ok
test_standard_changed_without_approval (__main__.Structure.test_standard_changed_without_approval) ... ok
test_standard_status_line_edit_is_caught (__main__.Structure.test_standard_status_line_edit_is_caught) ... ok

----------------------------------------------------------------------
Ran 50 tests in 3.399s

OK
```

### 3.3 Catalog fingerprint

Algorithm, from `tools/check_course.py`:

```text
$ grep -n "def fingerprint" -A8 tools/check_course.py
241:def fingerprint(cat):
242-    lines = []
243-    for uid in sorted(cat):
244-        u = cat[uid]
245-        lines.append("|".join([uid, u["title"], ",".join(sorted(u["requires"])), u["mastery"],
246-                               u["cls"], "+".join(map(str, u["hours"]))]))
247-    return hashlib.sha256("\n".join(lines).encode()).hexdigest()
248-
249-

$ grep -n "catalog_fingerprint\|catalog boundaries" tools/check_course.py
456:    rec = fm.get("catalog_fingerprint", "")
459:            err("CURRICULUM.md: APPROVED but no catalog_fingerprint recorded (run --fingerprint at approval)")
461:            err("CURRICULUM.md: catalog boundaries (title, prerequisites, mastery, class, hours) changed since "
462:                "approval. Present the change, get approval, log it, then update catalog_fingerprint")
466:        warn("CURRICULUM.md: catalog_fingerprint is set but does not match the catalog (status is PROPOSED)")
```

In words. Rows are taken from the catalog table, sorted by unlock ID. Each row contributes one line: ID, title, prerequisites (sorted, comma-joined), mastery target, class (E or O), hours as build+study+verify+consolidate, joined with `|`. The lines are joined with newlines and hashed with SHA-256.

- **Included:** ID, title, prerequisites, mastery, class, hours (each of the four parts). The set of rows is included implicitly, so adding or removing an unlock changes the hash.
- **Excluded:** the Definition cell (planned or authored); the order in which prerequisites are written; everything outside the catalog table.
- **Not covered:** unlock-file text (including its Objective section and acceptance criteria), phase files, and the completion-proof table. Of the six frozen boundaries in `UNLOCKS/README.md`, five are enforced by the fingerprint (identity, prerequisites, class, mastery, hours, with the title standing in for the objective). The sixth, phase contribution, and the full Objective text are protected by the governance rule only, not by the tool (finding F2). The F3 edit lives in this unprotected area, which is why section 3.8 verifies it separately.

Demonstration against the real catalog (each case applied to a fresh temporary copy, run before the F3 edit; the catalog is unchanged since):

```text
baseline fingerprint: d28afa7b918bda26 ...

ok  Definition cell planned->authored (P0-GO-02)          fingerprint SAME      (expected SAME)
ok  Definition cell authored->planned (P2-CONS-01)        fingerprint SAME      (expected SAME)
ok  order of prerequisites swapped (P0-BIT-07)            fingerprint SAME      (expected SAME)
ok  unlock FILE body text edited (P1-DEF-01 objective)    fingerprint SAME      (expected SAME (limitation))
ok  phase file edited (PHASES/PHASE-3.md)                 fingerprint SAME      (expected SAME (limitation))
ok  frozen: TITLE changed                                 fingerprint DIFFERENT (expected DIFFERENT)
ok  frozen: PREREQUISITE added                            fingerprint DIFFERENT (expected DIFFERENT)
ok  frozen: MASTERY target changed                        fingerprint DIFFERENT (expected DIFFERENT)
ok  frozen: CLASS changed E->O                            fingerprint DIFFERENT (expected DIFFERENT)
ok  frozen: HOURS changed 4+1+1+1 -> 4+1+1+2              fingerprint DIFFERENT (expected DIFFERENT)
ok  frozen: HOURS moved between parts 4+1+1+1 -> 3+2+1+1  fingerprint DIFFERENT (expected DIFFERENT)
ok  identity: new unlock row added                        fingerprint DIFFERENT (expected DIFFERENT)
ok  identity: unlock row removed (P0-DS-04)               fingerprint DIFFERENT (expected DIFFERENT)
```

End-to-end flow with approval, just-in-time authoring, and a frozen-boundary change (temporary copy, run before the F3 edit):

```text
1. curriculum approved with the recorded fingerprint (no unlock authored yet)
   exit=0  no errors
2. just-in-time authoring AFTER approval: new unlock file + Definition planned->authored only
   exit=0  no errors
3. same unlock, then hours raised 7 -> 8 (a frozen boundary) without an approved update
   exit=1  ERROR: CURRICULUM.md: catalog boundaries (title, prerequisites, mastery, class, hours) changed since approval. Present the change, get approval, log i
```

Step 3 also changed the prose total in `CURRICULUM.md` so that only the fingerprint rule was left to fire.

### 3.4 Reachability of C1–C8 under the cut strategy

Computed before the F3 edit from the real cut_order line and the real "Completion proofs" table by the checker's own functions. Neither input has changed since:

```text
cut_order (from CURRICULUM.md front matter):
  1. P5-PY-01, P5-LLM-01, P5-AI-01, P5-INT-01  (20 h)
  2. P6-PERF-01  (6 h)
  3. P0-INT-01  (9 h)
  total cut capacity: 35 h

crit proof unlock(s)       cuttable closure size closure ∩ cut closure all essential result
C1   P1-INT-01             no       18           -             True                  REACHABLE
C2   P2-INT-01             no       24           -             True                  REACHABLE
C3   P3-INT-01             no       31           -             True                  REACHABLE
C4   P4-INT-01             no       43           -             True                  REACHABLE
C5   P4-OPS-01             no       40           -             True                  REACHABLE
C6   P5-INT-01             yes      35           ['P5-AI-01', 'P5-INT-01', 'P5-LLM-01', 'P5-PY-01']True                  REACHABLE if Phase 5 is kept; WAIVED by design if cut #1 is taken
C7   P6-ARCH-01, P6-VER-01 no       46           -             True                  REACHABLE
C8   P6-CAR-01             no       47           -             True                  REACHABLE

essential unlocks outside the cut set that require a cut unlock: none

What C6's closure needs (it is the only cuttable criterion):
  P5 unlocks in closure: ['P5-AI-01', 'P5-INT-01', 'P5-LLM-01', 'P5-PY-01']

What each protected criterion needs that is in Phase 4 (the old contradiction):
  C4: P4-K8S-01 in closure=True, P4-OBS-03 in closure=True, either in cut set=False
  C5: P4-K8S-01 in closure=True, P4-OBS-03 in closure=True, either in cut set=False
```

Reading: C1–C5, C7, C8 do not depend on anything the cut order removes, and every unlock in their closures is essential. C6 depends on Phase 5, which is cut step 1, so C6 is reachable only if Phase 5 is kept and is waived by design if it is cut. The Phase 4 items that used to be in the cut order are in the closures of C4 and C5 and are not in the cut set.

### 3.5 Dependency chains and artifact consumption for six unlocks

Run before the F3 edit; prerequisites and Uses lines of these unlocks are unchanged since:

```text
=== P0-BIT-07  Package the codecs as a reusable library  [O, L3, 4 h, authored]
  direct requires : P0-BIT-03, P0-BIT-04, P0-BIT-06
  transitive closure (7): P0-BIT-01, P0-BIT-02, P0-BIT-03, P0-BIT-04, P0-BIT-05, P0-BIT-06, P0-GO-01
  Prerequisites text IDs : ['P0-BIT-03', 'P0-BIT-04', 'P0-BIT-06'] == requires: True
   Uses: `bits` (P0-BIT-02), `perm` (P0-BIT-03), `pack` (P0-BIT-04), `codec` (P0-BIT-05), `frame` (P0-BIT-06).
      P0-BIT-02: in closure   (Build and apply bit masks)
      P0-BIT-03: in closure   (Represent permissions as flags)
      P0-BIT-04: in closure   (Pack structured data into bits)
      P0-BIT-05: in closure   (Encode and decode binary formats (endianness, varints))
      P0-BIT-06: in closure   (Parse a framed binary protocol safely)

=== P1-PG-03  Transactions and isolation: reproduce anomalies  [E, L4, 8 h, authored]
  direct requires : P1-PG-01, P0-GO-03
  transitive closure (4): P0-GO-01, P0-GO-02, P0-GO-03, P1-PG-01
  Prerequisites text IDs : ['P0-GO-03', 'P1-PG-01'] == requires: True
   Uses: PostgreSQL and Go database access (P1-PG-01); goroutines (P0-GO-03).
      P1-PG-01: in closure   (Run PostgreSQL and query it from Go)
      P0-GO-03: in closure   (Goroutines, channels and context basics)

=== P2-IDEM-01  Idempotent API requests  [E, L5, 8 h, authored]
  direct requires : P1-API-03, P1-PG-03, P1-SDK-01
  transitive closure (16): P0-GO-01, P0-GO-02, P0-GO-03, P0-NET-01, P0-TYPE-01, P1-API-01, P1-API-02, P1-API-03, P1-DEF-01, P1-PG-01, P1-PG-02, P1-PG-03, P1-RES-01, P1-SDK-01, P1-SM-01, P1-SM-02
  Prerequisites text IDs : ['P1-API-03', 'P1-PG-03', 'P1-SDK-01'] == requires: True
   Uses: the workflow-creation API (P1-API-03); unique constraints and transactions (P1-PG-03); the TypeScript SDK (P1-SDK-01).
      P1-API-03: in closure   (Create, start and inspect workflows via API)
      P1-PG-03: in closure   (Transactions and isolation: reproduce anomalies)
      P1-SDK-01: in closure   (Typed TypeScript SDK from the API contract)

=== P2-CONS-01  Idempotent step effects and delivery guarantees  [E, L5, 9 h, authored]
  direct requires : P2-IDEM-01, P2-REC-01
  transitive closure (21): P0-GO-01, P0-GO-02, P0-GO-03, P0-NET-01, P0-TYPE-01, P1-API-01, P1-API-02, P1-API-03, P1-DEF-01, P1-EXEC-01, P1-PG-01, P1-PG-02, P1-PG-03, P1-RES-01, P1-SDK-01, P1-SM-01, P1-SM-02, P2-DUR-01, P2-IDEM-01, P2-REC-01, P2-RET-01
  Prerequisites text IDs : ['P2-IDEM-01', 'P2-REC-01'] == requires: True
   Uses: recovery and persisted attempts (P2-REC-01); the idea of a stored key with a stored outcome (P2-IDEM-01).
      P2-REC-01: in closure   (Recover unfinished workflows after restart)
      P2-IDEM-01: in closure   (Idempotent API requests)

=== P3-TST-01  Chaos tests for multiple workers  [E, L4, 7 h, planned]
  direct requires : P3-POOL-01, P2-FAIL-01, P2-CONS-01
  transitive closure (28): P0-GO-01, P0-GO-02, P0-GO-03, P0-NET-01, P0-TYPE-01, P1-API-01, P1-API-02, P1-API-03, P1-DEF-01, P1-EXEC-01, P1-PG-01, P1-PG-02, P1-PG-03, P1-RES-01, P1-SDK-01, P1-SM-01, P1-SM-02, P2-CONS-01, P2-DUR-01, P2-FAIL-01, P2-IDEM-01, P2-REC-01, P2-RET-01, P2-TMO-01, P3-CON-01, P3-LEASE-01, P3-POOL-01, P3-Q-01
  (planned: no unlock file, so no 'Uses:' declarations exist and artifact consumption cannot be checked by the tool)

=== P6-VER-01  Correctness report: invariants and evidence  [E, L5, 5 h, planned]
  direct requires : P3-INT-01, P2-INT-01
  transitive closure (32): P0-GO-01, P0-GO-02, P0-GO-03, P0-NET-01, P0-TYPE-01, P1-API-01, P1-API-02, P1-API-03, P1-DEF-01, P1-EXEC-01, P1-PG-01, P1-PG-02, P1-PG-03, P1-RES-01, P1-SDK-01, P1-SM-01, P1-SM-02, P2-CONS-01, P2-DUR-01, P2-FAIL-01, P2-IDEM-01, P2-INT-01, P2-REC-01, P2-RET-01, P2-TMO-01, P3-CON-01, P3-FENCE-01, P3-INT-01, P3-LEASE-01, P3-POOL-01, P3-Q-01, P3-TST-01
  (planned: no unlock file, so no 'Uses:' declarations exist and artifact consumption cannot be checked by the tool)
```

Limits of this evidence: the tool verifies only what an unlock declares in its Uses line, and only for authored unlocks. P3-TST-01 and P6-VER-01 are planned, so no declaration exists. I read the four authored challenges by hand against their prerequisites and found no undeclared consumption. For the two planned unlocks the dependency reasoning comes from their catalog titles and the phase files only.

### 3.6 The defect in the committed checker (reproduced)

```text
Setup: git archive of HEAD (the committed checker) with one deliberately unknown prerequisite added to one catalog row.
COMMITTED checker, mode 'default': exit=1  0 error line(s) on stderr
     lines mentioning the unknown prerequisite in combined output: 1
COMMITTED checker, mode '--budget': exit=0  0 error line(s) on stderr
     lines mentioning the unknown prerequisite in combined output: 0
COMMITTED checker, mode '--mermaid': exit=0  0 error line(s) on stderr
     lines mentioning the unknown prerequisite in combined output: 0
COMMITTED checker, mode '--status': exit=1  0 error line(s) on stderr
     lines mentioning the unknown prerequisite in combined output: 1
```

The committed checker printed errors to stdout; the point is the exit code and whether the error appears. Under --budget and --mermaid it exited 0 and showed nothing. The candidate checker reports it in every mode (section 3.2, class ReportingModesKeepFailures).

### 3.7 Read-only scan for stale text (nothing was edited; re-run after the F3 edit)

```text
(DECISION_LOG.md, KNOWLEDGE_STANDARD.md and the package itself excluded)
--- pattern: \b357\b
./REVIEW_REPORT.md:16:Essential plan is now **362 h** (was 357).
./REVIEW_REPORT.md:20:- Plan sized to **10 hours/week**: essential **362 h** (357 before revision 4), optional 124 h.
./CURRICULUM.md:63:The earlier proposal totalled about 440 hours by a rough count. I did not compress estimates to fit. I (1) estimated each unlock in four parts, (2) separated essential from optional by asking "does a completion 
--- pattern: never cut|C1.C3 and C5
--- pattern: fresh clone|separate repositor|external repo|PROJECTS\.md
./REVIEW_REPORT.md:101:Not a decision: at the start of `P0-GO-01` you describe where your working code lives (`project/README.md`). Evidence bundles keep the course re-verifiable without it. A separate repository for code is only 
./CLAUDE.md:94:`KNOWLEDGE_STANDARD.md` (repo root) is canonical and overrides this repository's wording on any conflict. Never edit it from here. Never change its contents or its status line without the learner's explicit approval
./KNOWLEDGE_STANDARD_ADDENDUM.md:40:The standard describes a larger ecosystem with separate repositories. This course is one self-contained repository (learner's decision, D-004). Its principles are preserved by directories, not b
./project/README.md:23:The learner keeps working code in a workspace of their choosing. It is not assumed to be a Git repository and its location is never written in this repository (no machine paths). The learner describes it at 
--- pattern: Revision (2|3)\b
./REVIEW_REPORT.md:3:Date: 2026-11-16. Everything here is **PROPOSED, not approved.** Revision 2 applied your decisions (D-002); revision 3 added the supplied knowledge standard (D-003) and the single-repository clarification (D-0
./REVIEW_REPORT.md:18:**Revision 3:** one self-contained repository, with directories carrying the standard's boundaries: `knowledge/` (concepts, created on demand), `project/` (platform plan, decisions, design documents), `career
./COURSE_OBJECTIVE.md:3:Owner: learner (changes need explicit approval). Status: **PROPOSED** (see `CURRICULUM.md`). Revision 2 (D-002).
--- pattern: P4-OBS-03.*cut|cut.*P4-K8S-01
./CURRICULUM.md:97:**Why `P4-OBS-03` and `P4-K8S-01` are not in the cut order.** An earlier version listed both. That contradicted C5: `P4-OPS-01` (recovery drill and runbook) requires both, and `P4-INT-01` requires `P4-OPS-01`. T
./PHASES/PHASE-4.md:21:`P4-INT-01` complete: C4 and C5 satisfied with evidence. C5 means a drill, not only a document: on the deployed platform a failure is injected (for example kill a worker, restart the database, let a lease ex
```

Every hit is an intentional historical or explanatory mention, except one stale label: `COURSE_OBJECTIVE.md` still says "Revision 2 (D-002)" (finding F4).

### 3.8 The F3 edit stayed inside the frozen boundaries

```text
Fingerprint before the F3 edit (captured earlier in this session): d28afa7b918bda26c5780f862edbae4f812fe07d4c14af9c03910eb3143b381e
Fingerprint now:                                                  d28afa7b918bda26c5780f862edbae4f812fe07d4c14af9c03910eb3143b381e

Catalog row and header of P2-CONS-01 (frozen boundaries):
| P2-CONS-01 | Idempotent step effects and delivery guarantees | P2-IDEM-01, P2-REC-01 | L5 | E | 5+2+1+1 | authored |
---
id: P2-CONS-01
title: Idempotent step effects and delivery guarantees
phase: 2
requires: [P2-IDEM-01, P2-REC-01]
mastery: L5
---


== files that differ between the first-package tree and the candidate:
Files DECISION_LOG.md differs
Files SESSION_HANDOFF.md differs
Files UNLOCKS/P2-CONS-01.md differs

== P2-CONS-01: changed line range (diff hunk header) vs acceptance-criteria section range
49c49,56
acceptance criteria section: lines 45 to 59
```

## 4. P2-CONS-01: the crash-after-external-success window

### 4.1 The window

1. A worker starts an attempt of a step. The engine commits an attempt-start record, then the handler calls the outside system with the effect key built from workflow instance, step and effect name.
2. The outside system performs the effect. It now exists outside the engine database.
3. The engine crashes before it commits the step result to its own database.
4. After restart the engine's records say the step is unfinished. It has no record that the effect happened.

Two different histories leave the engine in the same state: the crash came before step 2 (no effect) or after it (an effect exists). The engine cannot tell them apart. Only the outside system knows, and it can say so only through the key. That is why the key comes from the step and not the attempt: a retry must present the same identity.

Outcomes:
- Outside system honors keys: the retry sends the same key, gets the original outcome, no second effect; the engine commits once.
- Outside system ignores keys: the retry repeats the effect (duplicate).
- Outside system honors keys but forgot this one (retention shorter than the retry period): duplicate.
- Policy "no retry after an ambiguous failure": no second call; the step ends failed as outcome_unknown. If the effect did happen, the engine reports it as unknown; if the crash came before the call, an effect that was never attempted is also reported as unknown. No policy avoids both duplicates and loss.

### 4.2 What the exercise expects the learner to demonstrate (after F3)

From `UNLOCKS/P2-CONS-01.md`. The learner builds a fake outside "ledger" that records effects, can honor or ignore keys, and can fail before the effect, after it but before replying, or after replying.

| Experiment | Setup | Expected observation | Acceptance criterion |
|---|---|---|---|
| 1 Identity | Derive key from instance, step, effect name | Same key on every attempt of one step; different keys for different steps | 1 |
| 2 Crash window | Honoring ledger; crash after the ledger recorded the effect, before the commit; restart | Handler ran at least twice; ledger holds exactly 1 effect; exactly 1 successful result committed | 2 |
| 3 Same crash, ledger ignores keys | As 2 with a key-ignoring ledger | Ledger holds 2 effects; the design document records this as the expected result | 3 |
| 4 Policy "no retry after an ambiguous failure", ledger ignores keys | Test (a): when the ledger receives the call, a separate DB connection already sees the committed attempt-start record. Crash points: (b) after attempt start, before the call; (c) after the call succeeded, before the commit; (d) timeout after the effect, no crash | In (b), (c), (d): step failed as outcome_unknown, shown through the API with the attempt history; no second call; never committed as succeeded. (b): ledger holds 0 effects. (c) and (d): ledger holds exactly the 1 original effect. (b) and (c) leave identical engine records. Policy "retry": (b) gives 1 effect, (c) gives 2 | 4 (a to g) |
| 5 Key retention | Honoring ledger that forgets keys before the retry period ends | A duplicate; the design document states the retention rule that was broken | 5 |

The design document must also say that, with an outside system offering neither idempotency nor a lookup, the engine cannot determine whether the effect happened, and that outcome_unknown means exactly that. Acceptance 6: no exactly-once claim; a stale or crashed worker's handler may still run. The oral check asks why the engine cannot tell whether the effect happened, why the key comes from the step, what to tell users of an API without idempotency, and how this key differs from the request key in P2-IDEM-01.

Not demonstrated by this unlock: real external systems, real network failure (the ledger simulates it), several workers (so "orphaned attempt" means "after restart of the single engine process"; deciding it while other workers run is the ownership problem of P3-LEASE-01), and the stale-worker rule (G3 is enforced later; chaos tests with several workers are in P3-TST-01).

The acceptance criteria exactly as now written:

```text
$ sed -n "/^## Acceptance criteria/,/^## Verification/p" UNLOCKS/P2-CONS-01.md
## Acceptance criteria
1. The effect key is deterministic and unchanged across attempts of the same step, and differs between steps (test).
2. Experiment 2: the handler runs at least twice, the ledger holds exactly one effect, and exactly one successful result is committed.
3. Experiment 3: the ledger holds two effects, and the design document records this as the expected result for an outside system that ignores keys.
4. Experiment 4, policy *no retry after an ambiguous failure*, against a ledger that ignores keys. An attempt is *ambiguous* when the engine cannot tell whether the call took effect: an attempt that started and has no recorded outcome after a restart, or a call that ended without a reply (timeout, lost connection). This unlock assumes one engine process, so after a restart every started attempt without an outcome counts as ambiguous; deciding that while other workers are running is the ownership problem of `P3-LEASE-01`. The tests show all of the following:
   a. **Durable attempt start.** The engine commits an attempt-start record to its database before it makes the external call. At the moment the ledger receives a call, a separate database connection already sees that committed record (test).
   b. **Crash after the attempt start, before the call.** Inject a crash there. After restart the step is failed with reason `outcome_unknown`, the ledger holds no effect, and no call is made.
   c. **Crash after the call succeeded, before the result is committed.** Inject a crash there. After restart the step is failed with reason `outcome_unknown`, the ledger holds exactly the one original effect, and no second call is made.
   d. **No crash, no reply.** A call that times out after the ledger recorded the effect ends the same way as (c).
   e. **Same restart state.** After restart, (b) and (c) leave identical engine records: an attempt that started and has no outcome. The design document says so.
   f. **No false claim.** In (b) to (d) the step is never committed as succeeded. The API, the history and the design document describe the outcome only as `outcome_unknown` together with the attempt history, and none of them says the effect happened or did not happen. The design document states that, with an outside system that offers neither idempotency nor a way to look the effect up, the engine cannot determine whether the effect happened, and that this policy accepts reporting an effect that was never attempted (b) as unknown.
   g. **Contrast with *retry*.** With policy *retry* and the same ledger, (b) ends with exactly one effect and (c) ends with two, the duplicate of experiment 3.
5. Experiment 5 reproduces a duplicate and the design document states the required retention rule.
6. The design document makes no claim of exactly-once execution, and says plainly that a stale or crashed worker's handler may still run.

## Verification
```

### 4.3 Finding F3: resolved

**The finding.** The "no retry after an ambiguous failure" policy needs the engine to know, after a crash, that an attempt was in flight when it died. That requires recording "attempt started" durably before the external call. No written criterion required it, and the criterion for the policy named no crash points.

**The change (one criterion; nothing else in the unlock was edited).** Acceptance criterion 4 was rewritten as sub-criteria (a) to (g):
- (a) the attempt-start record is committed before the call, and a separate database connection sees it at the moment the ledger receives the call;
- (b) crash after the attempt start, before the call: step failed as outcome_unknown, no effect, no call;
- (c) crash after the call succeeded, before the commit: step failed as outcome_unknown, exactly the one original effect, no second call;
- (d) a timeout after the effect with no crash ends like (c);
- (e) (b) and (c) leave identical engine records, and the design document says so;
- (f) the step is never committed as succeeded, the API, history and document describe the outcome only as outcome_unknown, and none claims the effect did or did not happen; the document states that with neither idempotency nor a lookup the engine cannot determine whether the effect happened;
- (g) contrast with policy retry: (b) gives one effect, (c) gives two.
It also states the single-engine-process assumption.

**Why this fits the boundaries.** Identity and title, prerequisites, class (essential), mastery (L5), hours (5+2+1+1) and phase contribution (C2) are unchanged. No prerequisite, hours or scope was added. The catalog fingerprint is identical before and after, and only the acceptance-criteria lines of the file changed (section 3.8). Because the edit is outside what the fingerprint covers (finding F2), that was checked by comparing files rather than by the tool.

**What this does not do.** It does not make the criteria executed or validated (section 5). It does not add a prerequisite: the persisted-attempt behavior still arrives through P2-REC-01, which is planned. The attempt-start requirement now sits in this unlock's own criteria, so it no longer depends on P2-REC-01 being written a particular way.

## 5. Unvalidated areas (not run, not verified)

| Area | Status |
|---|---|
| P1-DEF-01 acceptance criteria | Written and designed to be observable. Never executed: no workflow definition format, validator or test data exists. No learner has attempted it. |
| P2-CONS-01 acceptance criteria | Written, never executed, including the F3 additions. No ledger, effect support or tests exist. |
| Reproducibility of evidence bundles | Not shown. The checker validates structure, field presence, paths and sha256 only, and says so in its own output ("Evidence commands were NOT executed"). The only bundle that has ever existed is a synthetic fixture inside the tests, with a stub source file and a command (go test) that was never run. This machine has Go 1.24.7, psql, node and docker, so a real run would be possible; none was done. No bundle has been independently reproduced. |
| Time to create and verify evidence | Not measured. No unlock has been completed, so no hours were recorded. The assumption that bundle assembly fits inside the verify and consolidate hours (70 h verify and 37 h consolidate across the essential plan) is unchecked until the first recalibration checkpoint. |
| Whether 9 h still covers P2-CONS-01 after F3 | Unknown. Criterion 4 now implies several crash-point cases inside experiment 4. Hours were deliberately not changed. |
| All hour estimates | Judgment, unmeasured. |
| Career evidence | 42 search-result pointers, none read. No direct posting record exists. |
| Tool versions and install steps in `ENVIRONMENT.md` | Not validated on a learner machine. |
| Tet date; weekly capacity assumptions | Not verified. |
| Whether a fresh Claude session follows `CLAUDE.md` correctly | Never tested. |
| Semantic dependencies of planned unlocks | Checked only through catalog titles and phase text; planned unlocks have no Uses declarations. |

## 6. Findings for the reviewer

Severity is my judgment. Only F3 was changed.

| # | Finding | Severity | Status |
|---|---|---|---|
| F1 | --mermaid and --fingerprint print the success line on stdout, so the output is not a pure diagram. The tests extract the first line for the fingerprint. | Low (tooling) | Open. Move the success line to stderr, or print it only when no report mode is used. |
| F2 | The fingerprint does not cover phase contribution or the text of an unlock file. Those boundaries are enforced by rule only. | Low to medium | Open. Accept as governance-only, or extend the fingerprint. |
| F3 | The "no retry after an ambiguous failure" policy depended on recording the attempt start before the external call; no written criterion required it. | Medium (design) | **Resolved** by the rewrite of acceptance criterion 4 (section 4.3). |
| F4 | `COURSE_OBJECTIVE.md` still says "Revision 2 (D-002)". | Cosmetic | Open. |
| F5 | Margin is thin: about 38 h (10%) of reserve after protecting Phase 6, and 5 h in Phase 2. | Planning risk | Open; the learner's call. |
| F6 | Work existed only in the working tree. | Process | **Resolved** by publishing the candidate to the review branch. |
| F7 | After F3, criterion 4 implies more test cases than experiment 4's original description, while the estimate stays at 9 h. | Planning risk | Open. If it proves too tight the response is a proposal to change hours, which needs approval. |

## 7. Approval readiness

No technical defect I found would prevent the learner from approving the curriculum. Two decisions remain the learner's: approval itself (which also records the catalog fingerprint in the header of `CURRICULUM.md`) and confirmation of the knowledge-standard addendum reconciliation recorded in `DECISION_LOG.md` (D-003). The earlier pre-approval concern, F3, is resolved; the open findings (F1, F2, F4, F5, F7) can be accepted or handled later.

## Appendix A. Full --mermaid output

```text
flowchart LR
  P0_CAR_01["P0-CAR-01"]
  P0_GO_01["P0-GO-01"]
  P0_GO_02["P0-GO-02"]
  P0_GO_03["P0-GO-03"]
  P0_BIT_01["P0-BIT-01"]
  P0_BIT_02["P0-BIT-02"]
  P0_BIT_03["P0-BIT-03"]
  P0_BIT_04["P0-BIT-04"]
  P0_BIT_05["P0-BIT-05"]
  P0_BIT_06["P0-BIT-06"]
  P0_BIT_07["P0-BIT-07"]
  P0_DS_01["P0-DS-01"]
  P0_DS_02["P0-DS-02"]
  P0_DS_03["P0-DS-03"]
  P0_DS_04["P0-DS-04"]
  P0_MEM_01["P0-MEM-01"]
  P0_OS_01["P0-OS-01"]
  P0_OS_02["P0-OS-02"]
  P0_NET_01["P0-NET-01"]
  P0_NET_02["P0-NET-02"]
  P0_TYPE_01["P0-TYPE-01"]
  P0_INT_01["P0-INT-01"]
  P1_PG_01["P1-PG-01"]
  P1_PG_02["P1-PG-02"]
  P1_PG_03["P1-PG-03"]
  P1_PG_04["P1-PG-04"]
  P1_DEF_01["P1-DEF-01"]
  P1_SM_01["P1-SM-01"]
  P1_SM_02["P1-SM-02"]
  P1_RES_01["P1-RES-01"]
  P1_API_01["P1-API-01"]
  P1_API_02["P1-API-02"]
  P1_API_03["P1-API-03"]
  P1_TEST_01["P1-TEST-01"]
  P1_EXEC_01["P1-EXEC-01"]
  P1_SDK_01["P1-SDK-01"]
  P1_INT_01["P1-INT-01"]
  P2_DUR_01["P2-DUR-01"]
  P2_IDEM_01["P2-IDEM-01"]
  P2_RET_01["P2-RET-01"]
  P2_TMO_01["P2-TMO-01"]
  P2_REC_01["P2-REC-01"]
  P2_FAIL_01["P2-FAIL-01"]
  P2_CONS_01["P2-CONS-01"]
  P2_INT_01["P2-INT-01"]
  P3_CON_01["P3-CON-01"]
  P3_Q_01["P3-Q-01"]
  P3_LEASE_01["P3-LEASE-01"]
  P3_FENCE_01["P3-FENCE-01"]
  P3_POOL_01["P3-POOL-01"]
  P3_DIST_01["P3-DIST-01"]
  P3_DLV_01["P3-DLV-01"]
  P3_MSG_01["P3-MSG-01"]
  P3_TST_01["P3-TST-01"]
  P3_INT_01["P3-INT-01"]
  P4_LNX_01["P4-LNX-01"]
  P4_DOC_01["P4-DOC-01"]
  P4_CI_01["P4-CI-01"]
  P4_OBS_01["P4-OBS-01"]
  P4_OBS_02["P4-OBS-02"]
  P4_OBS_03["P4-OBS-03"]
  P4_K8S_01["P4-K8S-01"]
  P4_IAC_01["P4-IAC-01"]
  P4_SEC_01["P4-SEC-01"]
  P4_OPS_01["P4-OPS-01"]
  P4_INT_01["P4-INT-01"]
  P5_PY_01["P5-PY-01"]
  P5_LLM_01["P5-LLM-01"]
  P5_LLM_02["P5-LLM-02"]
  P5_AI_01["P5-AI-01"]
  P5_AI_02["P5-AI-02"]
  P5_INT_01["P5-INT-01"]
  P6_ARCH_01["P6-ARCH-01"]
  P6_VER_01["P6-VER-01"]
  P6_PERF_01["P6-PERF-01"]
  P6_SEC_01["P6-SEC-01"]
  P6_DOC_01["P6-DOC-01"]
  P6_CAR_01["P6-CAR-01"]
  PX_RUST_01["PX-RUST-01"]
  PX_UI_01["PX-UI-01"]
  PX_REPLAY_01["PX-REPLAY-01"]
  P0_GO_01 --> P0_GO_02
  P0_GO_02 --> P0_GO_03
  P0_GO_01 --> P0_BIT_01
  P0_BIT_01 --> P0_BIT_02
  P0_BIT_02 --> P0_BIT_03
  P0_BIT_02 --> P0_BIT_04
  P0_BIT_02 --> P0_BIT_05
  P0_BIT_05 --> P0_BIT_06
  P0_BIT_03 --> P0_BIT_07
  P0_BIT_04 --> P0_BIT_07
  P0_BIT_06 --> P0_BIT_07
  P0_GO_01 --> P0_DS_01
  P0_DS_01 --> P0_DS_02
  P0_BIT_02 --> P0_DS_02
  P0_DS_01 --> P0_DS_03
  P0_DS_01 --> P0_DS_04
  P0_GO_02 --> P0_MEM_01
  P0_GO_01 --> P0_OS_01
  P0_OS_01 --> P0_OS_02
  P0_GO_02 --> P0_NET_01
  P0_NET_01 --> P0_NET_02
  P0_BIT_06 --> P0_NET_02
  P0_GO_02 --> P0_TYPE_01
  P0_BIT_06 --> P0_INT_01
  P0_OS_02 --> P0_INT_01
  P0_GO_02 --> P1_PG_01
  P1_PG_01 --> P1_PG_02
  P0_TYPE_01 --> P1_PG_02
  P1_PG_01 --> P1_PG_03
  P0_GO_03 --> P1_PG_03
  P1_PG_02 --> P1_PG_04
  P0_TYPE_01 --> P1_DEF_01
  P0_TYPE_01 --> P1_SM_01
  P1_DEF_01 --> P1_SM_01
  P1_SM_01 --> P1_SM_02
  P1_PG_02 --> P1_SM_02
  P1_PG_03 --> P1_SM_02
  P1_DEF_01 --> P1_RES_01
  P1_SM_02 --> P1_RES_01
  P0_NET_01 --> P1_API_01
  P1_PG_02 --> P1_API_01
  P1_API_01 --> P1_API_02
  P1_API_02 --> P1_API_03
  P1_RES_01 --> P1_API_03
  P1_SM_01 --> P1_TEST_01
  P1_PG_01 --> P1_TEST_01
  P1_SM_02 --> P1_EXEC_01
  P1_RES_01 --> P1_EXEC_01
  P0_GO_03 --> P1_EXEC_01
  P1_API_03 --> P1_SDK_01
  P1_EXEC_01 --> P1_INT_01
  P1_API_03 --> P1_INT_01
  P1_TEST_01 --> P1_INT_01
  P1_SM_02 --> P2_DUR_01
  P1_API_03 --> P2_IDEM_01
  P1_PG_03 --> P2_IDEM_01
  P1_SDK_01 --> P2_IDEM_01
  P1_EXEC_01 --> P2_RET_01
  P1_EXEC_01 --> P2_TMO_01
  P2_DUR_01 --> P2_REC_01
  P2_RET_01 --> P2_REC_01
  P2_REC_01 --> P2_FAIL_01
  P2_IDEM_01 --> P2_CONS_01
  P2_REC_01 --> P2_CONS_01
  P2_FAIL_01 --> P2_INT_01
  P2_CONS_01 --> P2_INT_01
  P0_GO_03 --> P3_CON_01
  P1_EXEC_01 --> P3_CON_01
  P2_REC_01 --> P3_Q_01
  P1_PG_03 --> P3_Q_01
  P3_Q_01 --> P3_LEASE_01
  P2_TMO_01 --> P3_LEASE_01
  P3_LEASE_01 --> P3_FENCE_01
  P3_CON_01 --> P3_POOL_01
  P3_LEASE_01 --> P3_POOL_01
  P3_LEASE_01 --> P3_DIST_01
  P2_CONS_01 --> P3_DLV_01
  P3_FENCE_01 --> P3_DLV_01
  P3_Q_01 --> P3_MSG_01
  P3_POOL_01 --> P3_TST_01
  P2_FAIL_01 --> P3_TST_01
  P2_CONS_01 --> P3_TST_01
  P3_TST_01 --> P3_INT_01
  P3_FENCE_01 --> P3_INT_01
  P0_OS_01 --> P4_LNX_01
  P0_OS_01 --> P4_DOC_01
  P1_INT_01 --> P4_DOC_01
  P1_TEST_01 --> P4_CI_01
  P4_DOC_01 --> P4_CI_01
  P1_API_02 --> P4_OBS_01
  P4_OBS_01 --> P4_OBS_02
  P4_OBS_02 --> P4_OBS_03
  P3_POOL_01 --> P4_OBS_03
  P4_DOC_01 --> P4_K8S_01
  P4_DOC_01 --> P4_IAC_01
  P1_API_03 --> P4_SEC_01
  P4_K8S_01 --> P4_OPS_01
  P4_OBS_03 --> P4_OPS_01
  P3_INT_01 --> P4_OPS_01
  P4_OPS_01 --> P4_INT_01
  P4_CI_01 --> P4_INT_01
  P4_SEC_01 --> P4_INT_01
  P1_API_03 --> P5_PY_01
  P5_PY_01 --> P5_LLM_01
  P5_LLM_01 --> P5_LLM_02
  P5_LLM_01 --> P5_AI_01
  P2_CONS_01 --> P5_AI_01
  P5_AI_01 --> P5_AI_02
  P2_DUR_01 --> P5_AI_02
  P5_AI_01 --> P5_INT_01
  P3_INT_01 --> P5_INT_01
  P4_INT_01 --> P6_ARCH_01
  P3_INT_01 --> P6_VER_01
  P2_INT_01 --> P6_VER_01
  P4_INT_01 --> P6_PERF_01
  P4_SEC_01 --> P6_SEC_01
  P4_INT_01 --> P6_SEC_01
  P6_ARCH_01 --> P6_DOC_01
  P6_DOC_01 --> P6_CAR_01
  P0_CAR_01 --> P6_CAR_01
  P0_BIT_06 --> PX_RUST_01
  P1_API_03 --> PX_UI_01
  P2_REC_01 --> PX_REPLAY_01
RESULT: OK (0 warning(s)). Structure, graph, files, declared dependencies, hashes and references are consistent. Evidence commands were NOT executed.
```
