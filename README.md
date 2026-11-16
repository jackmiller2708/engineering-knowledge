# Engineering Course Control Plane

This repository is a single, self-contained learning workspace for a long-term engineering course. It holds the curriculum, learner state and evidence, career research, the plan for the project being built, and the instructions for Claude. Directories keep the logical boundaries (`knowledge/`, `project/`, `career/`); nothing depends on any other repository.

It does **not** hold the platform's source code. The learner's working code lives in their own workspace (see `project/README.md`).

**Status: curriculum APPROVED on 2026-11-16** (revision 4, commit `93e5a018d75b8c67036462e1a8a146a020ef5908`; see `DECISION_LOG.md` D-007). Approval authorizes the course to begin; it does not mean the designs, estimates or career conclusions are validated. Start with `SESSION_HANDOFF.md`.

## Mission

Turn a senior frontend engineer (Angular/TypeScript) into a strong backend and platform engineer by **September 2027**, at a planning pace of 10 hours per week. The learner builds one substantial project along the way: a reliable workflow execution platform. Details: `COURSE_OBJECTIVE.md`.

## How the course works

Capabilities are unlocked by doing, not by reading. Each unit (an *unlock*) is a small practical challenge that produces something reusable and is verified by evidence. See `UNLOCKS/README.md`.

## Where to start

| You are... | Read |
|---|---|
| The learner, reviewing the proposal | `REVIEW_REPORT.md`, then `CURRICULUM.md` |
| A new Claude Code session | `CLAUDE.md` (it tells you the rest) |
| Resuming after a break | `PROCEDURES.md` → "Resume" |
| Starting over | `PROCEDURES.md` → "Restart" |
| Setting up tools | `ENVIRONMENT.md` |
| The learner, exploring Rust for fun (optional, outside the course): the Fuel project | [`knowledge/languages/rust/README.md`](knowledge/languages/rust/README.md) |

## Document map (one owner per fact)

| File | Single source of truth for |
|---|---|
| `CLAUDE.md` | How Claude behaves in this repo; who may edit what |
| `COURSE_OBJECTIVE.md` | Mission, completion criteria C1–C8, fit assessment |
| `CURRICULUM.md` | Approval status, time budget, calendar, cut order, parallel tracks |
| `PHASES/PHASE-N.md` | Per-phase purpose, deliverables, exit criteria |
| `UNLOCKS/CATALOG.md` | The dependency graph: IDs, prerequisites, mastery targets, essential/optional, hour estimates |
| `career/CAREER_RESEARCH.md` | Evidence about roles and pay in Vietnam (preliminary) |
| `project/PLAN.md` | The workflow platform: scope, execution model, capability proof, milestones |
| `project/DECISIONS.md` | Platform architecture decisions |
| `project/README.md` | Project areas, workspace, evidence bundles |
| `project/design/` | Design documents the learner writes (created on first use) |
| `knowledge/` | Canonical concept documents (created on demand). Rust leisure track: `knowledge/languages/rust/README.md` |
| `UNLOCKS/<ID>.md` | Full definition of one challenge |
| `LEARN/<ID>/` | The self-paced learning material for one unlock, prepared in full before the learner begins. Start at its `README.md` |
| `LEARNER_PROFILE.md` | Stable preferences and career context |
| `LEARNER_STATE.md` | What is verified as done (never anything else) |
| `EVIDENCE/` | Records and evidence bundles backing each completion |
| `SESSION_HANDOFF.md` | Short note for the next session (never overrides state) |
| `DECISION_LOG.md` | Curriculum decisions and approvals (append-only) |
| `PROCEDURES.md` | Resume, restart, handoff, session steps |
| `ENVIRONMENT.md` | Tool requirements and setup |
| `KNOWLEDGE_STANDARD.md` | The canonical knowledge standard (learner's file, unchanged) |
| `KNOWLEDGE_STANDARD_ADDENDUM.md` | Course-specific extensions to the standard only |
| `TEMPLATES/` | Reusable document shapes |
| `ARCHIVE/` | Previous attempts, kept after a restart |
| `tools/check_course.py` | Consistency checker (optional, needs Python 3.9+). Checks structure, hashes and references; never runs evidence commands |
| `tools/test_check_course.py` | Behavioural tests for the checker (`python3 tools/test_check_course.py`) |

## Checking the repository

```
python3 tools/check_course.py            # validate graph, files, state
python3 tools/check_course.py --status   # what is done / available / blocked
python3 tools/check_course.py --mermaid  # print the dependency graph
python3 tools/check_course.py --budget   # hours by phase, essential vs optional
python3 tools/check_course.py --fingerprint  # catalog boundary fingerprint (recorded at approval)
```

Learner progress is only durable once committed. Commit `LEARNER_STATE.md`, `EVIDENCE/` and `SESSION_HANDOFF.md` at the end of each session.
