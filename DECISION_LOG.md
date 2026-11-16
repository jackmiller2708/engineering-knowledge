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
