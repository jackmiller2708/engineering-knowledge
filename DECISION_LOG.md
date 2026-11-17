# Decision Log

Owner: learner approves; Claude appends. **Append-only.** To reverse a decision, add a new entry that supersedes it.

Entry types: `design`, `approval`, `change`, `restart`, `governance`.

## D-001 — Initial curriculum proposal (design) — 2026-11-16 — status: PROPOSED

**Decision proposed:** Adopt the structure in `CURRICULUM.md`, `COURSE_OBJECTIVE.md`, `PHASES/`, `UNLOCKS/CATALOG.md`.

**Key choices inside the proposal:**
1. Ultimate project PRJ-ENGINE with declared-graph workflows and saved step results (no deterministic replay).
2. At-least-once delivery plus idempotent effects; no exactly-once claims.
3. PostgreSQL as the only datastore and queue.
4. Phase 0 split into a 6-week gating core and just-in-time parallel tracks.
5. Go introduced in Phase 0; Rust is an optional stretch.
6. Math taught inside unlocks, not as a separate track.
7. Career research starts in Phase 0.
8. Phase 5 (AI) shortened and first to be cut.
9. Learner progress state lives in one file; unlock status is derived from the dependency graph, not stored.

**Alternatives considered:** deterministic-replay engine (rejected: scope); Kafka-based queue (rejected: new infrastructure, not the learning goal); full linear Phase 0 (rejected: delays the project); separate math phase (rejected: theory without use).

**Approval:** pending. The learner has not yet reviewed this entry.

## D-002 — Refinement after learner decisions (design) — 2026-11-16 — status: PROPOSED (curriculum remains unapproved)

**Learner decisions received (inputs; these are decided):**
1. Planning capacity is **10 hours per week**. Weekends can hold up to 8 h/day and weekdays 2–4 h optionally; maximum availability is not a commitment. The essential plan is sized to 10 h/week.
2. Evaluate fitting the essential curriculum into about 350–370 hours, leaving room for hard challenges, revision, integration, interruptions, hardening and career preparation.
3. **Workflow execution model:** declarative graphs with persisted step results. Steps have identity, state, input/output contract and saved result. No deterministic replay in the essential project; replay becomes an optional advanced experiment.
4. Investigate three career directions in Vietnam (backend/Go/data-intensive; platform; distributed systems/reliability) from real evidence, separating observation from interpretation.
5. Learner-facing material must not repeatedly name or explain teaching techniques.
6. `KNOWLEDGE_STANDARD.md` must be supplied and reconciled; the stand-in is not authoritative.

**Claude's proposals in response (need approval as part of the curriculum):**
- Essential plan **357 h** (reserve ≈ 69 h; ≈ 43 h after protecting 26 h for Phase 6 hardening and careers). Optional pool 124 h incl. 30 h stretch. Calendar in `CURRICULUM.md`.
- 13 authored unlocks, 81 in the catalog. Added: `P1-DEF-01` (authored), `P1-RES-01`, optional `P1-PG-04`, `P3-MSG-01`, `P4-IAC-01`. Rewired: `P1-SM-01` now follows `P1-DEF-01`; `P0-BIT-05` follows `P0-BIT-02`; `P0-INT-01` follows `P0-BIT-06`; `P1-API-01` needs `P0-NET-01`; retries no longer need a heap. Reclassified as optional: `P0-BIT-03/04/07`, `P0-DS-02/03/04`, `P0-MEM-01`, `P0-NET-02`, `P3-DIST-01`, `P3-DLV-01`, `P4-LNX-01`, `P5-LLM-02`, `P5-AI-02`, `P6-SEC-01`.
- Catalog gains `Class` and `Hours` columns; checker enforces that essential unlocks never require optional ones.
- Unlock section "Minimal theory" renamed "What you need first"; level tags removed from learner-facing text. `CLAUDE.md` forbids naming teaching methods to the learner.
- `CAREER_RESEARCH.md` added with preliminary, low-confidence evidence (search summaries only).
- C6 narrowed: tool allow-lists and human approval are optional extensions.

**Supersedes (in D-001):** item 1 (workflow model now decided as above); item 4 (Phase 0 is 10 weeks and 84 essential hours, not 6 weeks); item 8 wording (Phase 5 is 2 weeks, 20 hours); all phase dates; `P0-CAR-01` scope (now builds on `CAREER_RESEARCH.md`).

**Note on IDs:** unlock IDs were re-wired freely because the curriculum is not yet approved. After approval the "IDs are stable" rule in `UNLOCKS/README.md` applies.

**Approval:** pending. The learner's decisions above are recorded as inputs; the learner has not approved the resulting curriculum.

## D-003 — Knowledge standard supplied and reconciled (governance) — 2026-11-16 — status: PROPOSED (learner confirmation pending)

**Input:** the learner supplied `KNOWLEDGE_STANDARD.md` and directed that it be treated as supplied (see D-002 item 6). It is installed at the repository root, byte-identical to the upload. Its own status line says "Proposed"; the learner's direction makes it canonical here.

**Reconciliation applied (proposed):**
- `KNOWLEDGE_STANDARD_ADDENDUM.md` rewritten to extensions only. Removed as duplicates of the standard: mastery table, claim labels, concept chain.
- `TEMPLATES/EXPERIMENT.md` now uses the standard's section 7 headings (Objective, Hypothesis, Setup, Procedure, Observations, Analysis, Conclusion).
- `CLAUDE.md`: adopted §8.2 (repair earliest unresolved prerequisite), §4.2 (analogy rules), §6.2 source ranking, §9.2 (corrections list dependents), §2.5 (language contrasts only when useful).
- Kept as extensions with reasons: evidence records, recorded-mastery rule, idle retrieval check, explanation pacing (internal), market-data source ranking, hour estimates.

**Unresolved (needs the learner):** standard §9.1/§10 place canonical concept documents in an *Engineering Knowledge* repository and career research in an *Engineering Career* repository. It is not stated whether this repository is either. Interim rules: no concept documents here; `CAREER_RESEARCH.md` provisional. Also: should the standard's "Proposed" status line be updated by the learner?

**Approval:** pending.

## D-004 — Single self-contained repository (governance) — 2026-11-16 — status: applied at the learner's direction; curriculum remains PROPOSED

**Learner decisions received (inputs):**
1. The course has exactly one repository, `engineering-knowledge`, created to contain and coordinate the whole learning journey. No other repository is to be assumed, created or required.
2. The standard's boundaries are to be preserved as principles (canonical ownership of concepts; separation of kinds of knowledge) using directories inside this repository.
3. Career research, the platform's project plan and milestones, curriculum and learner progress all stay here.
4. `KNOWLEDGE_STANDARD.md` governs this curriculum. Its status line and contents change only with the learner's explicit approval. The reconciliation stays subordinate to it.
5. A separate repository may be proposed only as an optional future decision, never as a current dependency.
6. The repository-identity question is closed.

**Applied:**
- Directories: `knowledge/` (canonical concept documents, created on demand), `project/` (`PLAN.md`, `DECISIONS.md`, `README.md`, later `design/`), `career/` (`CAREER_RESEARCH.md` moved here). Mapping in `KNOWLEDGE_STANDARD_ADDENDUM.md`.
- `PROJECTS.md` removed. Project areas (PRJ-LABS, PRJ-ENGINE, PRJ-REPLAY-LAB) are logical areas, not repositories. Working code lives in the learner's workspace, which is not assumed to be a Git repository and is never recorded as a path here.
- Platform scope, execution model and capability proof moved from `COURSE_OBJECTIVE.md` to `project/PLAN.md`; platform architecture decisions logged in `project/DECISIONS.md` (PD-001 records D-002 item 3).
- Evidence now uses evidence bundles (`EVIDENCE/<ID>/artifacts/`) instead of external commit references, so a fresh session can see what was proven without the workspace. Restart also archives `project/design/`.
- Unlock text, `CLAUDE.md`, `PROCEDURES.md`, `TEMPLATES/EVALUATION.md`, phase files and the checker revised to remove multi-repository assumptions.
- Kept from the original brief: the platform's source code is not built in this repository.

**Supersedes:** D-001 and D-002 references to external project repositories and `PROJECTS.md`; D-003 "Unresolved" paragraph (repository boundary) and its interim rules (no concept documents, `CAREER_RESEARCH.md` provisional).

**Not changed:** the standard (verified byte-identical to the supplied file) and its "Proposed" status line. The specific D-003 reconciliation edits still await the learner's confirmation.

## D-005 — Correction pass (design/governance) — 2026-11-16 — status: PROPOSED (curriculum remains unapproved; no architecture change)

**Input:** the learner asked for a focused correction of contradictions found in review, without redesign, without approving the curriculum, and without commits.

**Decisions and rationale**
1. **Phase 4 / C5.** Chose to keep the complete operational recovery path and remove `P4-OBS-03` and `P4-K8S-01` from the cut order. Rationale: C5 (a runbook used in a drill) needs a deployed target and cross-process visibility; a smaller path would keep C5's name and lose its meaning. Cut capacity falls from 47 h to 35 h (Phase 5, `P6-PERF-01`, `P0-INT-01`). Only C6 can be waived. C5 was rewritten to describe the drill (injected failure, detection signal, runbook-only recovery, post-recovery check, drill record). Verified by a checker rule over the cut order and the new "Completion proofs" table.
2. **Delivery guarantees.** Wording that implied exactly-once execution ("executed and committed twice", "processed exactly once") was corrected. Guarantees G1–G4 and tests T1–T6 added to `project/PLAN.md`; PD-004 added to `project/DECISIONS.md` (states PD-002 precisely). `P2-CONS-01` retitled "Idempotent step effects and delivery guarantees", widened (6 h to 9 h) and authored in full: effect identity and key, the engine/external boundary, the crash window, retries, and what is possible without external idempotency (retry with duplicate risk, or no retry with `outcome_unknown`). `P2-IDEM-01` is now explicitly about requests only. C2 and C3 rewritten; C3 no longer implies handlers run once.
3. **Just-in-time authoring.** After approval, Claude may author planned unlocks without per-unlock approval inside six frozen boundaries (identity and objective, prerequisites, class, mastery, hours, phase contribution); only the catalog's `Definition` cell changes. A boundary change needs approval and a log entry. Approving the curriculum and approving a change remain separate. A catalog fingerprint recorded at approval lets the checker detect silent boundary changes.
4. **Evidence contract.** Evidence is a bundle `EVIDENCE/<ID>/<date>-<n>/` with `evaluation.md`, `manifest.md`, `artifacts/`. The manifest records capability, artifacts with sha256, commands, expected and observed results, exit statuses, environment, setup, limitations, and `preserved` versus `independently-reproduced`. Whole-workspace copies are forbidden.
5. **Checker.** All modes now run all validation and keep failures; errors go to stderr, reports to stdout; new checks for structure, canonical locations, source code, evidence bundles, references, cut strategy, fingerprint and a pin on the standard. `tools/test_check_course.py` added (50 tests). A real gap found and fixed: malformed IDs in `Requires` were silently dropped.
6. **Restart.** Three operations (resume, restart learning progression, start a new implementation attempt) and four record categories; reuse after archiving needs explicit revalidation; the workspace is never touched.
7. **Prerequisites.** Manual review of authored challenges against prerequisites. Fixed: `P0-BIT-07` now requires `P0-BIT-04`; `P1-PG-03` requires `P0-GO-03` (goroutines); `P2-IDEM-01` requires `P1-SDK-01` (SDK sends the keys); `P3-TST-01` requires `P2-CONS-01` (effects under chaos); `P6-VER-01` requires `P2-INT-01` (Phase 2 invariants). Unlocks now declare artifacts consumed in `Uses:` lines; the checker verifies those declarations only.
8. **Career snapshot.** `P0-CAR-01` narrowed to an initial snapshot (at least 6 direct posting records per direction) and re-estimated 5 h to 7 h. Evidence tiers separated (direct record, pointer, aggregated observation, interpretation, hypothesis). 42 search-result pointers registered with URLs; none read.

**Budget effect:** essential 357 h to 362 h (+3 for `P2-CONS-01`, +2 for `P0-CAR-01`); optional pool unchanged at 124 h. Reserve about 64 h, of which about 26 h is held for Phase 6; about 38 h (10%) remains for overruns.

**Unchanged:** the objective, the September 2027 target, the 10 h/week commitment, the execution model (PD-001), the knowledge standard (hash-verified), the single repository.

**Supersedes:** the cut-order table and the 357 h figures in D-002 and revision 2 of the review report; the C2/C3 wording in `COURSE_OBJECTIVE.md` as of D-004; the restart procedure of D-004.

**Approval:** pending. Nothing here approves the curriculum.

## D-006 — F3 resolved; independent-review branch prepared (governance) — 2026-11-16 — status: PROPOSED (curriculum remains unapproved)

**Input (learner's direction):** (1) publish the current proposal for independent review on a new branch, `review/final-curriculum-candidate`, built from the working tree, with the original working branch and the default branch left unchanged and nothing merged; (2) include `FINAL_REVIEW_PACKAGE.md` and `FINAL_REVIEW_PACKAGE.patch`, keeping the original base hash in the report; (3) resolve review finding F3 first, by an acceptance-criteria clarification only, inside the proposed boundaries.

**F3, the problem.** The *no retry after an ambiguous failure* policy in `P2-CONS-01` can only work if the engine knows, after a restart, that an attempt was in flight. That needs a durable attempt-start record made before the external call. No written criterion required it, and the criterion for the policy did not name the crash points.

**F3, the change.** Only acceptance criterion 4 of `UNLOCKS/P2-CONS-01.md` was rewritten, as sub-criteria (a) to (g): attempt-start record committed and visible to a separate connection when the ledger receives the call; crash after the attempt start but before the call; crash after the call succeeded but before the commit; a timeout with no crash; the observation that those two crash points leave identical engine records; a ban on claiming the engine knows whether the effect happened when the outside system has neither idempotency nor lookup; and the contrast with the *retry* policy. The criterion also states that this unlock assumes a single engine process, because deciding that an attempt is orphaned while other workers run is the ownership problem of `P3-LEASE-01`.

**Boundaries unchanged.** Identity and title, prerequisites, class (essential), mastery (L5), hours (5+2+1+1 = 9), and phase contribution (C2). The catalog fingerprint is identical before and after (`d28afa7b…381e`). No prerequisite, hours or scope was added.

**Honest limits.** (1) `UNLOCKS/README.md` says no unlock is edited before approval; this edit was made at the learner's explicit direction, as an exception for review. (2) Criterion 4 adds crash-point cases inside experiment 4 while the estimate stays at 9 h; this may be tight, and if it proves so the right response is a proposal to change hours, which needs approval. (3) The acceptance criteria remain unexecuted.

**Provenance.** The proposal's base is the original HEAD `6e1b12ae18ce1af2458d2fcadaa9092472cd7903`. The candidate is the tip of `review/final-curriculum-candidate`. Original working branch `ccr-b573edbb-crcfsw` is not modified.

**Not changed:** every other curriculum file apart from this entry and a minimal correction to `SESSION_HANDOFF.md`.

**Approval:** pending. Nothing here approves the curriculum.

## D-007 — Curriculum approved; D-003 confirmed and reconciled with D-004; teaching workflow and checkpoints adopted (approval, governance) — 2026-11-16 — status: APPROVED

**Approval.** The learner approved the curriculum candidate and authorized the move from PROPOSED to APPROVED.

| | |
|---|---|
| Approved branch | `review/final-curriculum-candidate` |
| Approved commit | `93e5a018d75b8c67036462e1a8a146a020ef5908` |
| Base of that candidate | `6e1b12ae18ce1af2458d2fcadaa9092472cd7903` |
| Approval date | 2026-11-16 |
| Catalog fingerprint recorded | `d28afa7b918bda26c5780f862edbae4f812fe07d4c14af9c03910eb3143b381e` |

**Verified before approving.** The checked-out branch and `HEAD` were that exact commit; its parent was the named base; the working tree was clean; the remote branch pointed at the same commit. `KNOWLEDGE_STANDARD.md` had the same sha256 (`223f2e52…2f8a`) in the base commit, the candidate commit, the working tree, the learner's original upload and the addendum's pin. The checker and its tests passed on that state. Nothing was substituted.

**What approval means.** The curriculum is authorized to begin. It does not mean that its technical designs, hour estimates, acceptance criteria or career-market conclusions have been validated. They remain hypotheses until implemented, measured or read. Unexecuted criteria are not passed criteria.

**D-003 confirmed, reconciled with D-004.** The learner accepts the reconciliation of `KNOWLEDGE_STANDARD_ADDENDUM.md` with the standard recorded in D-003: the standard is canonical, the addendum holds only extensions and the directory mapping, and the standard's hash is pinned. D-004 established the single-repository approach: the one repository is `engineering-knowledge`, and the standard's logical domains (knowledge, projects, career) are directories inside it (`knowledge/`, `project/`, `career/`), not separate repositories. D-004 had already superseded the "Unresolved" paragraph of D-003 and its interim rules; this entry confirms what remained. No earlier entry is rewritten. The statuses of D-001 to D-006 that read PROPOSED are superseded by this entry for everything contained in the approved commit.

**The knowledge standard.** Unchanged, including its own header status "Proposed". Approving the curriculum does not change the status of the standard.

**Teaching workflow made operational (`CLAUDE.md` sections 1, 3, 4, 5; `TEMPLATES/LESSON.md`, `TEMPLATES/EVALUATION.md`, `TEMPLATES/LEARNER_STATE.initial.md`).** For each new concept: problem; mental picture; mechanism; worked example; reconstruction; independent application; explanation. Rules added: understanding rather than familiarity; change the representation rather than add vocabulary; theory when it becomes useful; fade guidance; return to the earliest unresolved prerequisite; keep what the learner demonstrated apart from what they were told. The terminology is not taught to the learner and no separate theory document exists.
- *Decision made while implementing:* the worked example is a solution to a **neighboring problem**, never to the unlock's own challenge. This keeps the existing rule that the challenge's solution is not handed over, while still showing a correct solution. The learner reconstructs it, then solves the real challenge independently.
- Evaluations now record the guidance level, the evidence time, and a "demonstrated versus told" table.

**Retention and transfer.** No-notes recall at session start, spaced revisits, reuse of earlier concepts, and unfamiliar variations. They sit inside each unlock's consolidate time. No hours were added and the essential budget is unchanged.

**Checkpoints (`CURRICULUM.md`, "Checkpoints"; `PHASES/PHASE-3.md`).** Checkpoint 1 after 25 **actual** study hours (this replaces the revision-4 definition of "27 estimated hours"), reviewing six named items from actual work products. An evaluation at the end of every phase that keeps completed work, demonstrated understanding, independently reproduced results, unresolved gaps and unverified assumptions apart. A critical checkpoint before Phase 3, recorded as an entry check in `PHASES/PHASE-3.md`: Phase 3 does not start on weak foundations, and slippage is handled by reserve, extra hours or a proposed cut. Records go in the Checkpoints table of `LEARNER_STATE.md`.

**Known risks carried forward (`CURRICULUM.md`, R1 to R5).** The roughly 38 h unprotected reserve; the 9 h estimate of `P2-CONS-01` (variance above 25% is reported); incomplete career research (42 search-result pointers are not 42 reviewed postings, and no specialization is forced); architecture and acceptance criteria as hypotheses; no bundle called independently reproduced before it is rerun.

**Unchanged.** The ultimate objective and September 2027 target; the 10 h/week baseline (maximum weekend time is not the commitment); the essential plan of 362 h; optional material stays optional; capability objectives; phase boundaries; acceptance criteria; the catalog fingerprint. Phase dates in `PHASES/` keep their "(proposed)" label: they remain planning estimates.

**Tooling.** `tools/test_check_course.py` hard-coded the PROPOSED header, so approval broke 23 of its 50 tests. The tests now reset each temporary copy to a known state, and four tests cover the approved state as recorded (54 tests). `tools/check_course.py` was not changed. The checker does not validate the `approved_commit`, `approved_base` or `approved_branch` fields; a test checks that they are present and well formed.

**Not done, by instruction.** No commit, push, merge, pull request, release or tag; no other repository; no source code moved into this repository; `KNOWLEDGE_STANDARD.md` untouched.

## D-008 — Self-paced delivery becomes the default; learning material added; teaching examples may be code (governance) — 2026-11-16 — status: applied at the learner's direction (curriculum approved in D-007)

**Learner's direction (inputs).** (1) Publish the current work: done as commits `d3fd988f7892458b4e02752fc41e47aca6fd22c6` (approval and governance), `3daacb15644c28f45837fbcc9b99cc3569400b55` (teaching workflow) and `8ecf14bafa81b20cc1f441542f9808f678dc9f8b` (P0-GO-01 progress records), pushed to `review/final-curriculum-candidate`. (2) Replace the conversational, question-by-question default with a self-paced course: material prepared in advance in full, presented in ordered sections, no mandatory chat answers, questions inside the material with answers kept apart, help on request, the approved teaching approach and completion requirements intact, preparation kept apart from the learner's execution, Linux with Zsh primary and Windows with PowerShell 7 secondary.

**Applied.**
- `CLAUDE.md` sections 1 to 5: the default is self-paced material in `LEARN/<ID>/`, prepared in full before the learner begins, presented progressively, with no conversational gates; the seven-step order is now the structure of the material rather than a chat routine; retention practice lives in recall blocks and cards; preparation and execution are kept apart. Teach mode may write `LEARN/<ID>/**`.
- New: `LEARN/` convention and `TEMPLATES/LEARN_UNLOCK.md`; `LEARN/P0-GO-01/` (start page, 8 sections, hint ladder, answer keys, recall card, examples).
- `tools/check_course.py`: code is allowed only under `LEARN/<ID>/examples/`; each `LEARN/<ID>/` folder is checked for shape; an unlock cannot be in progress or completed without its `LEARN/<ID>/README.md`; lesson code blocks must equal their example files. `tools/test_check_course.py`: 67 tests, including a check that the new tests fail when the rule is removed.
- `.gitattributes`: example files use LF; fixture files are never converted.
- `LEARNER_PROFILE.md`: the delivery preference, environment and experience the learner stated. `KNOWLEDGE_STANDARD_ADDENDUM.md`, `UNLOCKS/README.md`, `PROCEDURES.md`, `README.md`: updated to match.

**Choices to confirm or veto.**
1. **A labelled spoiler.** `LEARN/P0-GO-01/examples/spoiler-reference-xd/` is a complete solution to the unit's challenge. Earlier wording said the challenge is "never handed over". It is now never in the reading flow; a hint ladder comes first, the spoiler is kept apart, the learner records whether they opened it, and the evaluation asks for an unseen variation if they did. Reason: the learner asked for answer keys and a path that does not depend on chat, and the solution is also what the acceptance checker was validated against.
2. **The `xd` layout is fixed by the course.** The unlock leaves it open; the material specifies it exactly so that an independent acceptance checker (`examples/accept`) can verify any conforming implementation. This is an exercise detail inside the unlock's boundaries.
3. **Teaching examples are code in this repository.** It is the one exception to "no source code here". It is confined to `LEARN/<ID>/examples/`, is not the learner's work or PRJ-ENGINE, and is enforced by the checker.
4. **Learning material is not a concept document** (see the addendum). Language-independent concepts that deserve a canonical home still go in `knowledge/`.

**Unchanged.** `UNLOCKS/P0-GO-01.md`, the catalog and its fingerprint, estimated hours (the eight sections sum to the unlock's 6 h), the approved commit, `KNOWLEDGE_STANDARD.md`, the checkpoints, and the risks R1 to R5.

**What is verified and what is not.** Verified by the author in a Linux container (Go 1.24.7, Zsh 5.9): the examples compile and pass their tests; the acceptance checker passes the reference (15 of 15) and rejects 12 deliberately broken variants; every number and message quoted in the answer keys was observed; section 7's Zsh commands were dry-run end to end and produced a bundle the repository checker accepted. **Not run:** anything on Windows or in PowerShell; anything by the learner. No evidence exists for `P0-GO-01`, and nothing has been independently reproduced.

**Correction to an earlier statement.** At the end of the previous session I reported that the checker and all 54 tests passed. The command I used printed only the `Ran 54 tests` line, and 3 tests were in fact failing: each test copy reset the approval header but not the learner state, so the new in-progress record made them fail. This was found while preparing the publish and fixed in `8ecf14b`; the suite is now run and read in full.

**Approval:** the learner's direction above. Items 1 to 3 may be reversed by the learner.

---

## D-009 — Rust becomes a leisure track outside the core plan (governance) — 2026-11-16 — status: applied at the learner's direction

**Learner's direction.** Rust is a self-directed, curiosity-driven, parallel track. It has no mandatory hours, deadlines, order, progress reporting, credentials or mastery requirements, and no effect on core completion. No Rust course, new unlock or progress-tracking system is added.

**Applied.**
- New `knowledge/languages/rust/README.md`: the single document for the track (what it is and is not, pause and resume, how help works, precise guarantees, directions that are not a checklist, capability-based success, `PX-RUST-01` as an optional exercise).
- `LEARNER_PROFILE.md`, `ENVIRONMENT.md`, `KNOWLEDGE_STANDARD_ADDENDUM.md`, `knowledge/README.md`: wording changed from "stretch/exploratory" to the leisure track, with a pointer.
- `CURRICULUM.md`: `PX-RUST-01` removed from the "When ahead" list (it is no longer something to schedule), with a pointer to the track document.
- `CLAUDE.md` section 4 and `SESSION_HANDOFF.md`: one line each. Rust is not an unlock; do not prompt, schedule or track it; do not pre-build material.

**Unchanged.** `UNLOCKS/CATALOG.md` (including the `PX-RUST-01` row and its 5+2+1+0 hours, which are a rough size reference only), `UNLOCKS/P0-BIT-06.md`, the catalog fingerprint, core sequencing, essential unlocks, prerequisites, hours, phase boundaries, completion criteria, `KNOWLEDGE_STANDARD.md`.

**Time budget.** Rust time is outside the 10 h/week plan and the 362 h essential total. Nothing is taken from the reserve.

**Not validated.** No Rust toolchain was installed or run. The track document contains no commands that need verifying.

**Approval:** the learner's direction in this conversation.

---

## D-010 — Rust leisure track gets a runnable project; Rust source may live under `knowledge/languages/rust/` (governance) — 2026-11-16 — status: applied at the learner's direction

**Learner's direction.** The Rust track was too small to explore. The learner asked for a substantial, hands-on, optional experience: a project worth building, several self-contained explorations with runnable code and experiments, concepts introduced when the project needs them. Rust stays outside the core curriculum: no required hours, deadlines, sequence, progress reporting or mastery gates.

**Applied.**
- New project `knowledge/languages/rust/fuel/`: a deterministic stack machine ("Fuel"), five explorations (`01-the-machine` to `05-parallel-runs`), each a Cargo project with a guide. Each starts where the previous one ends. A project overview in `fuel/README.md`. No dependencies.
- **Source code rule widened, narrowly.** `CLAUDE.md` section 4 and `tools/check_course.py` now allow code under `knowledge/languages/rust/<project>/`, in addition to `LEARN/<ID>/examples/`. Anything else under `knowledge/` is still refused. The checker ignores cargo `target/` output there. `tools/test_check_course.py`: two tests added (69 in total). `.gitignore` (new) ignores `target/` and `Cargo.lock` there. `.gitattributes`: LF for Rust, `.fuel` and `Cargo.toml` files.
- `CLAUDE.md` Rust bullet reworded: never proactively assign, prompt, remind or create new Rust lessons or projects unasked; help fully when the learner asks.
- `knowledge/languages/rust/README.md`: start page now leads to `fuel/`; `first-exploration.md` stays as an optional warm-up. `README.md`, `knowledge/README.md`, `ENVIRONMENT.md`: pointers and version note.

**Unchanged.** `UNLOCKS/CATALOG.md` and its fingerprint, `PX-RUST-01`, `UNLOCKS/P0-BIT-06.md`, core sequencing, hours, phases, completion criteria, `KNOWLEDGE_STANDARD.md`. The track is not in `LEARNER_STATE.md`. Concept documents for language-independent ideas are still written only on request (`knowledge/README.md`); none were added.

**Verified and not.** The author built and ran every project on Linux with rustc and cargo 1.97.0 (4 cores), applied each experiment, and quotes only observed compiler errors and outputs. `cargo test` in `05-parallel-runs`: 9 pass. Not run: Windows or PowerShell; any other Rust version; any run by the learner. The timing figures belong to one container. The guides link Rust Book chapters that the author did not read; each says so.

**Choices to confirm or veto.** (1) Allowing Rust source under `knowledge/languages/rust/`. If vetoed, the projects move outside the repository and the guides become code blocks. (2) Edition 2021 and no external crates. (3) The choice of project.

**Approval:** the learner's direction above. Items 1 to 3 may be reversed.

---

## D-011 — Rust projects finalized: narrowed code exception, lockfile policy, toolchain record (governance) — 2026-11-16 — status: applied at the learner's direction (supersedes parts of D-010)

**Learner's direction.** Finalize the Fuel project: review everything, keep the code exception narrow and enforced, choose a lockfile policy, record the exact toolchain, separate verified Linux behavior from unverified Windows behavior, and publish to the approved branch.

**Changed from D-010.**
- **Code exception narrowed.** The checker allows only `.rs` and `Cargo.toml` files, and only one folder below `knowledge/languages/rust/` (`knowledge/languages/rust/<project>/...`). Code of other languages inside a Rust project, Rust files loose in `knowledge/languages/rust/`, and Rust files in other `knowledge/` folders are refused. `tools/test_check_course.py` gained `test_rust_exception_is_narrow` (70 tests); the test was shown to fail when the narrowing is removed. `CLAUDE.md` section 4 states the same scope.
- **`Cargo.lock` is committed**, not ignored (D-010 ignored it). Reason: these are programs, and the lockfile reproduces the build. With no dependencies it holds only the package itself. It was written by Cargo 1.97.0; older Cargo versions may not read it (untested). `target/` stays ignored.
- **Toolchain recorded.** Verified with `rustc 1.97.0 (2d8144b78 2026-07-07)` and `cargo 1.97.0 (c980f4866 2026-06-30)`, Linux x86_64, edition 2021. Recorded in `ENVIRONMENT.md` and `knowledge/languages/rust/fuel/README.md`. Windows/PowerShell 7, macOS and other Rust versions are explicitly unverified. No `rust-version` or `rust-toolchain` file was added, because no other version was tested.
- **Guide corrections found by re-running every experiment** (a script, kept out of the repository, applied each documented change to a clean copy and checked the quoted output): exploration 1 said four type errors where the compiler gives three; exploration 2's speed-test snippet omitted the lines that call it; timing numbers were refreshed. PowerShell variants are marked untested.
- **Exploration 5** gained a section separating deterministic execution (one run is a function of its inputs) from deterministic concurrent behavior (thread scheduling, which is not deterministic), and experiment H: in ten runs the job completion order varied (eight distinct orders) while stdout was identical in five further runs.
- **Navigation** from the repository `README.md` through `knowledge/README.md` and the Rust start page to `fuel/` and each exploration now uses clickable relative links.

**Unchanged.** `UNLOCKS/CATALOG.md`, its fingerprint, `PX-RUST-01`, the core curriculum, hours, `KNOWLEDGE_STANDARD.md`, `LEARNER_STATE.md`.

**Not verified.** Windows and PowerShell; any Rust version other than 1.97.0; any run by the learner. Timing figures are from one 4-core container.

**Approval:** the learner's direction above.

---

## D-012 — Learning Environment application is a separate repository (governance) — 2026-11-17 — status: applied at the learner's direction

**Source.** Owner decisions of 2026-11-17, given as task instructions. They are not part of the curriculum approved in D-007 (that approval covers commit `93e5a018d75b8c67036462e1a8a146a020ef5908`, which predates them).

**Relation to earlier decisions.** D-004 and D-007 are unchanged. D-004 (confirmed in D-007) says the course is one repository and that a separate repository is only an optional future decision. This entry makes one such decision, for one product only. It narrows D-004 item 1 ("exactly one repository") and item 5 ("never a current dependency") for the Learning Environment application. Everything else in D-004 still applies. D-004 describes working code in the learner's own workspace; that remains true for the platform and lab areas.

**Learner decisions received (inputs).**
1. This repository keeps owning concepts, curriculum, learning-platform plans and product architecture decisions.
2. The Engineering Learning Environment application is a separate implementation and delivery platform. It has its own Git repository, inside the `engineering-projects` repository of the workspace, under `projects/engineering-learning-environment`. It has no remote and is not a submodule. The workspace-level record of the placement is entry WD-005 in the workspace decision log ("Engineering Learning Environment is an independent repository under engineering-projects"). That log is outside this repository.
3. The application references this repository's content. It does not copy it.
4. The application repository is **not** a prerequisite for reading or maintaining the curriculum.

**Rust boundary (decided by the learner, 2026-11-17; D-009, D-010 and D-011 are unchanged; same as LE-004).**
1. Rust is an implementation technology used by the application. It is the application's native implementation technology (the Tauri 2 native layer).
2. Rust proficiency is not required to follow the core curriculum or to use the application.
3. The optional Rust leisure track (D-009 to D-011) remains independent of the Learning Environment. Application work does not schedule, replace or count toward it.
4. Application development creates no learner mastery requirements, unlocks, hours, deadlines or progression gates.
5. The application implementation and the learner's Rust education are separate concerns. Rust as the application's technology and Rust as an optional subject a learner may explore on their own are different things.
6. Unknown, not decided here: who writes the native layer, and how much Rust it needs.

**Applied.**
- Product plan and decisions: `project/learning-environment/` (`README.md`, `LE-PLAN.md`, `LE-DECISIONS.md`). The `LE-` file names avoid the checker's canonical names `PLAN.md` and `DECISIONS.md`.
- `project/README.md`: the sentence "nothing here depends on any other repository" is rescoped, and a short "Learning Environment" section is added.
- The Go/PostgreSQL platform (PRJ-ENGINE) is unchanged: `project/PLAN.md` and `project/DECISIONS.md` were not edited.

**Not changed.** `KNOWLEDGE_STANDARD.md` (status "Proposed", hash pinned), `KNOWLEDGE_STANDARD_ADDENDUM.md`, D-001 to D-011, the catalog and its fingerprint, `LEARNER_STATE.md`, the hour budget.

**Not verified.** Whether the application repository exists is recorded in the workspace, not here. This repository cannot check it.

**Approval:** the learner's direction above.
