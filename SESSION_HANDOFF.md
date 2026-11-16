# Session Handoff

Owner: Claude rewrites at each session end. A hint only; `LEARNER_STATE.md` wins on conflict.

- **Written:** 2026-11-16
- **Curriculum status:** APPROVED 2026-11-16 at commit `93e5a018d75b8c67036462e1a8a146a020ef5908` (D-007).
- **Learner state:** `P0-GO-01` in progress. The learner starts at section 1 of the prepared material. No results, hours or evidence yet. Nothing completed.
- **Delivery:** self-paced (D-008). Material is in `LEARN/P0-GO-01/`. Do not run a chat quiz; help on request.

## What is ready

`LEARN/P0-GO-01/` is complete: start page, 8 sections (about 6 h), a hint ladder, answer keys, a recall card, and examples (`cnt`, `greet`, the `xd` acceptance checker, and a labelled spoiler reference solution). The learner was told to open `LEARN/P0-GO-01/01-setup.md`.

Verified in the author's Linux container (Go 1.24.7, Zsh 5.9): examples build and pass; the checker passes the reference and rejects 12 broken variants; section 7's Zsh commands were dry-run into a bundle the repository checker accepts. **Not run on Windows or PowerShell.** Nothing has been run by the learner.

## When the learner comes back

1. If they ask for help, answer from the material; do not reveal the spoiler solution unless asked after real attempts, and note it.
2. If they hand over an evidence bundle and `explanations.md`: evaluate. Re-run the manifest commands on Linux in a clean copy. If results match, record `independently-reproduced` with who and when; otherwise keep `preserved` and say what differed. Read their written explanations; ask follow-ups if needed. Record the guidance level (hints used, spoiler opened) and ask for a variation if the spoiler was opened first. Record actual hours in `LEARNER_STATE.md`.
3. Do not mark `P0-GO-01` complete without all of that. Do not award mastery for task completion alone.
4. Prepare the next unlock's material only when it is the learner's likely next choice (`P0-GO-02` is planned and needs authoring first, inside its frozen boundaries). `P0-CAR-01` is also available, planned, and also needs authoring.

## Watch

- Checkpoint 1 at 25 actual hours; the pre-Phase-3 checkpoint; risks R1 to R5 in `CURRICULUM.md`.
- Evidence time is an open risk: ask how long section 7 took.
- Review findings still open: F1 (success line on stdout in report modes), F2 (fingerprint does not cover unlock or lesson text), F5 (thin reserve), F7 (estimate pressure on `P2-CONS-01`).
- Unconfirmed choices in D-008: the labelled spoiler, the fixed `xd` layout, code under `LEARN/*/examples/`.

## Do not

- Claim the learner installed Go, ran a command or finished an exercise.
- Call any bundle `independently-reproduced` before its commands have been re-run.
- Change scope, estimates, acceptance criteria or frozen boundaries without approval.
- Schedule, prompt for or track Rust. It is a leisure track (`knowledge/languages/rust/README.md`, with the Fuel project in `fuel/`; D-010, D-011); never assign, prompt or create new Rust lessons unasked, but help fully when the learner asks.
