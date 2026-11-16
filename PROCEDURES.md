# Procedures

Owner: learner approves changes. Steps are written so a new session on any machine can follow them with only this repository.

## Three different operations

People say "start over" for three different things. Keep them apart.

| Operation | What changes | What stays |
|---|---|---|
| **Resume** the current attempt | Nothing, apart from normal session records | Everything |
| **Restart learning progression** | Learner progress resets to zero as a new *learning attempt*. Old progress and evidence are archived | Curriculum, canonical project records, decisions, career and knowledge documents. The implementation workspace and its current implementation attempt are unchanged |
| **Start a new implementation attempt** | The learner begins a fresh implementation of a project area (for example a rewrite). Designs of the superseded implementation are archived | Learner progress and completed unlocks, evidence, curriculum, canonical project records. The old workspace content is untouched |

A learner may do both at once. They are separate decisions with separate records.

### Record categories (what each operation may touch)

| Category | Files | Rule |
|---|---|---|
| **Canonical**: active across all operations, never silently changed or removed | `CURRICULUM.md`, `PHASES/`, `UNLOCKS/`, `LEARN/`, `COURSE_OBJECTIVE.md`, `project/PLAN.md`, `project/DECISIONS.md`, `DECISION_LOG.md`, `career/`, `knowledge/`, `TEMPLATES/`, `KNOWLEDGE_STANDARD*.md` | Never archived by a restart. Changed only through the governance rules in `CLAUDE.md` |
| **Learning-attempt records**: belong to one learning attempt | `LEARNER_STATE.md`, `SESSION_HANDOFF.md`, `EVIDENCE/**` | Archived (moved, never deleted) on a learning restart |
| **Implementation-attempt records**: belong to one implementation attempt | `project/design/**`: drafts, per-unlock designs, session implementation notes, unfinished experimental artifacts, superseded designs | Archived on a learning restart *and* on a new implementation attempt |
| **Workspace** | The learner's working code, wherever it lives | No procedure here modifies, moves or deletes it. Procedures only record descriptions |

### Reuse after an operation

Archived material is **not active**. A design, an experiment or existing implementation code may be reused only by explicit revalidation:
1. Copy a design back from `ARCHIVE/` into `project/design/` with the first line `Status: restored draft, not validated`.
2. Complete the unlock that produces it again, with a new evidence bundle (preferably `independently-reproduced`).
3. Only then does the design count as active. Existing code in the workspace may serve as a starting point; it counts only through a new bundle.

Canonical decisions (`project/DECISIONS.md`) stay in force across restarts. A learner who now disagrees with one proposes a change; nothing is dropped by restarting.

## Resume (continue the current attempt from the latest verified state)

1. Clone or pull the repository. Do not rely on any local path.
2. `git status` and `git log -5`. Note uncommitted changes and the date of the last commit.
3. Read `LEARNER_STATE.md`. It is authoritative; `SESSION_HANDOFF.md` is only a hint. Note `learning_attempt` and `implementation_attempt`.
4. Run `python3 tools/check_course.py`. Fix or report failures before teaching.
5. Environment: for the next unlock, run each verification command in `ENVIRONMENT.md` for the tools it needs. Do not assume anything is installed.
6. Project work: read `project/PLAN.md` (current milestone) and `project/README.md` (workspace description and implementation attempts). If the next unlock needs code, ask the learner to make the workspace available. If it is unavailable, use theory and isolated experiments; evidence bundles still show what was proven earlier.
7. **Gap check (after more than 4 weeks of inactivity):** before new material, run a short retrieval check on the last 2–3 completed unlocks (ask the learner to explain and apply, no help). If they fail, record it in `SESSION_HANDOFF.md` and revisit; do not edit completed records. Re-evaluation that lowers demonstrated mastery is recorded as a new evidence bundle plus a note in `LEARNER_STATE.md`.
8. Summarize to the learner and let them choose the next unlock.

## Handoff (end of every session)

1. If anything was evaluated, update `LEARNER_STATE.md` and `EVIDENCE/` first.
2. Rewrite `SESSION_HANDOFF.md` using its structure (short; facts only).
3. Run `python3 tools/check_course.py`.
4. Tell the learner which files changed and that they must commit them. Do not commit unless asked.

## Restart learning progression

Resets learner progress only. It must never delete curriculum, canonical project records, decisions, evidence or the workspace.

1. Confirm in plain words: "This archives your progress, evidence and attempt-specific designs, and resets progress to zero. Your curriculum, project plan, decisions and workspace stay as they are." Wait for a yes. Ask whether the implementation continues unchanged (the default) or a new implementation attempt starts too.
2. Let K be the current `learning_attempt` (the first restart archives attempt 1).
3. Create `ARCHIVE/learning-attempt-<K>-<YYYY-MM-DD>/`.
4. `git mv` into it: every attempt directory in `EVIDENCE/` (not `.gitkeep`) and everything in `project/design/`, plus copies of `LEARNER_STATE.md` and `SESSION_HANDOFF.md`.
5. Write `RESTART_NOTE.md` in the archive directory: reason, date, what moved, what stayed active, and "workspace untouched".
6. Replace `LEARNER_STATE.md` with a copy of `TEMPLATES/LEARNER_STATE.initial.md`; set `learning_attempt` to K+1 and `implementation_attempt` to its current value; set today's date.
7. Rewrite `SESSION_HANDOFF.md` as a fresh start.
8. Append a `DECISION_LOG.md` entry (type `restart`) with the reason.
9. Run the checker. Tell the learner to commit.

Partial restart (redo one phase) is a curriculum-governance decision: propose it, get approval, log it. Never silently remove completed entries.

## Start a new implementation attempt

For when the learner begins a fresh implementation of a project area while learning progress continues.

1. Confirm: "This starts implementation attempt M. Your progress stays. Designs of attempt M-1 are archived. Milestones are re-demonstrated against the new implementation." Wait for a yes.
2. In `project/README.md`, mark the current row of the "Implementation attempts" table superseded (with the date) and add a new row: attempt number, a description of the new workspace area (no machine paths), start date.
3. Create `ARCHIVE/implementation-attempt-<M-1>-<YYYY-MM-DD>/`. `git mv` everything in `project/design/` into it. Write `RESTART_NOTE.md`.
4. In `LEARNER_STATE.md` set `implementation_attempt` to M. Completed unlocks stay completed, because they record capability. List every integration or milestone unlock (`P*-INT-01`) and every unlock whose deliverable lived in the superseded implementation under "Open gaps and re-checks", to be re-demonstrated. New evidence manifests record `implementation_attempt: M`.
5. Do not touch the old workspace content. Do not change `project/PLAN.md` or `project/DECISIONS.md`; new design decisions for the new implementation go in as new `PD-` entries.
6. Append a `DECISION_LOG.md` entry. Run the checker. Tell the learner to commit.

## Recording evidence

Every completed unlock needs an evidence bundle at `EVIDENCE/<UNLOCK-ID>/<YYYY-MM-DD>-<n>/`:

```
evaluation.md    decision, criteria, questions  (TEMPLATES/EVALUATION.md)
manifest.md      what was evaluated and how to reproduce it  (TEMPLATES/MANIFEST.md)
artifacts/       only the files the listed commands need
```

The manifest states the capability, each artifact with its sha256, the commands with expected results, observed results and exit statuses, the environment and toolchain versions, setup and dependencies, limitations, and the evidence kind:
- `preserved`: captured from the learner's run; nobody else re-ran it.
- `independently-reproduced`: an evaluator re-ran the commands from this bundle in a clean environment and the results matched; who and when are recorded.

Do not copy a whole workspace. Keep only what the verification needs and point to the workspace through `provenance`. A failed evaluation also gets a bundle that records the failing commands and observed results. `tools/check_course.py` checks that the structure, fields and hashes are present and consistent; it never runs the commands.

## Curriculum change

See `CLAUDE.md` section 6. Every change gets a `DECISION_LOG.md` entry with id `D-NNN`.
