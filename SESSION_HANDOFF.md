# Session Handoff

Owner: Claude rewrites at each session end. A hint only; `LEARNER_STATE.md` wins on conflict.

- **Written:** 2026-11-16
- **Curriculum status:** APPROVED 2026-11-16 at commit `93e5a018d75b8c67036462e1a8a146a020ef5908` (D-007).
- **Learner state:** `P0-GO-01` in progress (started 2026-11-16, Part 1 delivered). Nothing completed. No actual hours recorded yet.
- **Repository:** the approval record, teaching-workflow changes and this session's records (17 files) are uncommitted on `review/final-curriculum-candidate`. Check `git status`. The approved commit is the candidate; the approval record will be a later commit.

## What happened

The candidate was verified against the named commit, base and the supplied knowledge standard, then approved. D-003 confirmed, reconciled with D-004. The teaching workflow, retention practice and checkpoints (25 actual hours, every phase end, before Phase 3) were written into `CLAUDE.md`, the templates and `CURRICULUM.md`. The risks are listed in `CURRICULUM.md` ("Known risks carried forward").

## Where `P0-GO-01` stands

The learner reported their environment (recorded in `ENVIRONMENT.md` and `project/README.md`): Linux at home (Zsh, primary) and Windows at work (PowerShell 7); no Go experience; SQL knowledge about six years old (plan a refresher inside the study time of `P1-PG-01`, not as extra hours); Docker beginner. They want the workflow portable across both.

Part 1 given: install Go and check it; create a module `labs`; run and test a small tool `cnt` (counts lines, words, bytes) that solves a *different* problem from `xd`; three predictions to make before running (3-line file, same file with Windows line endings, a file with an accented letter); one question about why the counting logic lives in its own package. The `cnt` code was run in a Linux container with Go 1.24.7: vet, build and tests pass. It has **not** been run on Windows.

Held back on purpose: the answers to the three predictions (3 lines, 9 words, 44 bytes; with CRLF 47 bytes, same lines and words; accent file 14 bytes because the accented letter is 2 bytes).

## Next step

1. Read the learner's results, predictions and reasoning. Fix any wrong mental model with a different representation, not more vocabulary.
2. Part 2: the learner changes `cnt` themselves (add the length of the longest line, test first), without copying.
3. Part 3: the learner writes `xd` independently; hints small to large. Part 4: evidence bundle and the explanation questions.
4. Ask for actual hours (build, study, verify, consolidate).
5. Pending question to the learner: record the experience levels in `LEARNER_PROFILE.md` (needs approval and a decision-log entry).

## Watch

- Record actual hours for every unlock. Run Checkpoint 1 when cumulative actual hours reach 25.
- Report any unlock whose actual hours exceed the estimate by more than 25%, especially `P2-CONS-01`.
- Phase 3 does not start until the pre-Phase-3 checkpoint is recorded as passed.
- Open review findings: F1 (success line on stdout in report modes), F2 (fingerprint does not cover unlock text), F4 (stale "Revision 2" label before this change; now replaced), F5 (thin reserve), F7 (estimate pressure on `P2-CONS-01`).

## Do not

- Mark an unlock complete without an evidence bundle and the learner's own reconstruction, independent application and explanation.
- Call any bundle `independently-reproduced` before its commands have been rerun.
- Treat the career pointers as reviewed postings, or push a specialization decision.
- Change scope, estimates, acceptance criteria or frozen boundaries without approval.
