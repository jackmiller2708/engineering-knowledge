# Procedures

Owner: learner approves changes. Steps are written so a new session on any machine can follow them with only this repository.

## Resume (continue from the latest verified state)

1. Clone or pull the repository. Do not rely on any local path.
2. `git status` and `git log -5`. Note uncommitted changes and the date of the last commit.
3. Read `LEARNER_STATE.md`. It is authoritative. `SESSION_HANDOFF.md` is only a hint.
4. Run `python3 tools/check_course.py`. Fix or report failures before teaching.
5. Environment: for the next unlock, run each verification command in `ENVIRONMENT.md` for the tools it needs. Do not assume anything is installed.
6. Project work: read `project/PLAN.md` (current milestone) and `project/README.md` (workspace description). If the next unlock needs code, ask the learner to make their workspace available. If it is unavailable, use theory and isolated experiments; evidence bundles in `EVIDENCE/` still show what was proven earlier.
7. **Gap check (after more than 4 weeks of inactivity):** before new material, run a short retrieval check on the last 2–3 completed unlocks (ask the learner to explain and apply, no help). If they fail, record it in `SESSION_HANDOFF.md` and revisit; do not edit completed records. Re-evaluation that lowers demonstrated mastery is recorded as a new evidence entry plus a note in `LEARNER_STATE.md`.
8. Summarize to the learner and let them choose the next unlock.

## Handoff (end of every session)

1. If anything was evaluated, update `LEARNER_STATE.md` and `EVIDENCE/` first.
2. Rewrite `SESSION_HANDOFF.md` using its structure (short; facts only).
3. Run `python3 tools/check_course.py`.
4. Tell the learner which files changed and that they must commit them. Do not commit unless asked.

## Restart (reset progression to the beginning)

Restart resets *learner progress only*. It must never delete curriculum, decisions, templates or history.

1. Confirm with the learner in plain words: "This archives your progress and evidence and resets state to zero." Wait for a yes.
2. Choose an attempt number N (first restart = `2`; the original run is attempt 1).
3. Create `ARCHIVE/attempt-<N-1>-<YYYY-MM-DD>/`.
4. `git mv` into it: every file in `EVIDENCE/` except `.gitkeep`, and everything in `project/design/` (it is the learner's work product), plus copies of `LEARNER_STATE.md` and `SESSION_HANDOFF.md`.
5. Replace `LEARNER_STATE.md` with a copy of `TEMPLATES/LEARNER_STATE.initial.md`; set `attempt: N` and today's date.
6. Rewrite `SESSION_HANDOFF.md` as a fresh start.
7. Append a `DECISION_LOG.md` entry (type `restart`) with the reason.
8. Run the checker. Tell the learner to commit.
9. Do not alter `CURRICULUM.md`, `PHASES/`, `UNLOCKS/`, `project/PLAN.md`, `project/DECISIONS.md`, `career/`, `knowledge/`. The learner's workspace is untouched; suggest a new directory name per attempt and record it in `project/README.md` only if the learner asks.

Partial restart (redo one phase) is a curriculum-governance decision: propose it, get approval, log it. Never silently remove completed entries.

## Recording evidence

`EVIDENCE/<UNLOCK-ID>/<YYYY-MM-DD>-<attempt>.md` from `TEMPLATES/EVALUATION.md`. Must reference an evidence bundle (see `project/README.md`): the commands to re-run, the files needed to run them, and a summary of observed output. Failed evaluations are recorded too.

## Curriculum change

See `CLAUDE.md` section 6. Every change gets a `DECISION_LOG.md` entry with id `D-NNN`.
