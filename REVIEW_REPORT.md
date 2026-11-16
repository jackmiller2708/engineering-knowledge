# Curriculum Review Report — Revision 4

Date: 2026-11-16. Everything here is **PROPOSED, not approved.** Revision 2 applied your decisions (D-002); revision 3 added the supplied knowledge standard (D-003) and the single-repository clarification (D-004); revision 4 is a focused correction pass (D-005) that removes contradictions without redesigning anything. This report is a snapshot for the approval decision, not part of ongoing course state.

## 0. What changed since revision 1

**Revision 4 (correction pass, D-005):**
1. Cut order no longer contains `P4-OBS-03` and `P4-K8S-01`, which `P4-OPS-01` (the C5 drill) requires. Only C6 can now be waived. A checker rule enforces this.
2. Delivery wording fixed: handlers may run more than once, at most one result is committed per step, a stale worker cannot commit, retried effects do not duplicate where the external system honors idempotency. `P2-CONS-01` now teaches step-effect idempotency as a separate problem from request idempotency (`P2-IDEM-01`).
3. After approval, planned unlocks may be authored just in time within frozen boundaries; changing a boundary still needs approval.
4. Evidence is now a bundle with an artifact manifest, expected versus observed results, exit statuses, environment, limitations, and `preserved` versus `independently-reproduced`.
5. Checker: reporting modes no longer hide errors; new structure, evidence, reference, cut-strategy and standard-pin checks; 50 behavioural tests.
6. Restart: three distinct operations and explicit record categories.
7. Prerequisite gaps found by reading each authored challenge against its prerequisites: five fixed.
8. `P0-CAR-01` narrowed to an initial snapshot and re-estimated (5 h to 7 h); evidence tiers separated.
Essential plan is now **362 h** (was 357).

**Revision 3:** one self-contained repository, with directories carrying the standard's boundaries: `knowledge/` (concepts, created on demand), `project/` (platform plan, decisions, design documents), `career/` (research). No other repository is assumed. The platform's design documents and evidence bundles live here; the platform's source code does not. The standard (`KNOWLEDGE_STANDARD.md`) is installed unchanged and governs. The repository-identity question is closed.

- Plan sized to **10 hours/week**: essential **362 h** (357 before revision 4), optional 124 h.
- Workflow model fixed: **declarative graphs with persisted step results**; replay is an optional experiment in an isolated project area (`PRJ-REPLAY-LAB`).
- Catalog: 81 unlocks (was 76), now with essential/optional class and hour estimates; one new authored unlock (`P1-DEF-01`).
- Calendar, phase files, objective, instructions updated. Career evidence added (preliminary).

## 1. Revised time budget and phase schedule

Window 2026-11-30 → 2027-09-30: 43.6 weeks, 436 gross hours, about 426 after removing one Tet week (expected around 6 Feb 2027; verify).

| Phase | Dates | Weeks | Capacity h | Essential h | Reserve h |
|---|---|---|---|---|---|
| 0 Foundation | 2026-11-30 → 2027-02-07 | 10 | 90 | 86 | 4 |
| 1 Execution engine | 2027-02-08 → 2027-04-11 | 9 | 90 | 81 | 9 |
| 2 Reliability | 2027-04-12 → 2027-05-23 | 6 | 60 | 55 | 5 |
| 3 Distributed execution | 2027-05-24 → 2027-07-04 | 6 | 60 | 45 | 15 |
| 4 Operability | 2027-07-05 → 2027-08-08 | 5 | 50 | 45 | 5 |
| 5 Intelligent execution | 2027-08-09 → 2027-08-22 | 2 | 20 | 20 | 0 |
| 6 Completion | 2027-08-23 → 2027-09-30 | 5.6 | 56 | 30 | ~26 |
| **Total** | | **43.6** | **426** | **362** | **~64** |

Essential effort split: build 187 h, study 68 h, verify 70 h, consolidate 37 h.

**Answer to "can it fit in 350–370 hours?" Yes, at 362 h, with a thin margin.** About 26 h of the 64 h reserve is held for hardening and career preparation, leaving about **38 h (10%)** for overruns and interruptions. If actual hours exceed my estimates by more than 10% the protected hardening time is consumed; above 18% the plan fails without extra weekend hours or cuts. The agreed cuts release up to 35 h for work not yet done. Evidence bundles add real work per unlock; that effort is assumed to sit inside the verify and consolidate hours, and checkpoint 1 will show whether it does. My estimates are judgment, not measurements, and individual unlocks are likely off by ±25%. The plan therefore re-measures after the first 27 estimated hours and at each phase end, with a pre-agreed cut order (below). Extra weekend or weekday hours are not counted; they are insurance.

If approval slips past 2026-11-30, the reserve shrinks hour for hour.

## 2. Essential vs optional

Test applied: "does a completion criterion (C1–C8) fail without it?" Full classification with per-unlock hours (`build+study+verify+consolidate`) is in `UNLOCKS/CATALOG.md`.

**Moved to optional (80 h of work that was previously essential, with effect on the objective):**

| Optional now | Hours | Effect |
|---|---|---|
| Hash table, search trees, heap (`P0-DS-02/03/04`) | 19 | Weaker interview-style data-structure depth. Retry timers use a stored next-attempt time, so no heap needed. Revisit after career evidence. |
| Memory model (`P0-MEM-01`), HTTP parser (`P0-NET-02`) | 13 | Weaker Go-internals and wire-format understanding; TCP stays. |
| Flags, packing, library packaging (`P0-BIT-03/04/07`) | 11 | Masks, varints and framed parser stay (needed for the record log). |
| Linux ops, Terraform (`P4-LNX-01`, `P4-IAC-01`) | 11 | Weaker "operate infrastructure" signal. |
| Tool calling, approval gate (`P5-LLM-02`, `P5-AI-02`) | 12 | AI step keeps validation, timeout, retry, idempotency, cost cap, audit. |
| Clock experiments, delivery write-up (`P3-DIST-01`, `P3-DLV-01`) | 10 | Fencing and chaos tests stay. |
| Security review (`P6-SEC-01`) | 4 | Threat model stays. |
| Broker comparison, query plans (`P3-MSG-01`, `P1-PG-04`), new | 14 | Closes evidence-based gaps if time allows. |
| Stretch: Rust, Angular viewer, replay | 30 | Never counted. |

**Added to essential:** `P1-DEF-01` and `P1-RES-01` (+12 h) to make the graph-with-results model explicit.

**Judgment calls you may reverse:** I kept `P0-INT-01` (record log, 9 h) and `P6-PERF-01` (load test, 6 h) essential because they give strong reliability evidence; I kept a minimal Phase 5 essential because "controlled AI integration" is in your target list. Each can be moved to optional (cut order 2, 3 and 1).

**Cut order if behind:** all of Phase 5 (20 h) → `P6-PERF-01` (6) → `P0-INT-01` (9), 35 h in total. `P4-OBS-03` and `P4-K8S-01` were removed from it because the C5 drill needs both. Only C6 can be waived. **When ahead:** `P1-PG-04`, `P3-DIST-01`, `P3-MSG-01`, `P4-IAC-01`/`P4-LNX-01`, `P5-LLM-02`, then the rest; order is pending your career choice.

## 3. Dependency graph changes

Checked by `tools/check_course.py`: acyclic; no prerequisite from a later phase; **no essential unlock requires an optional one**; authored files match the catalog.

- New: `P1-DEF-01` (graph and contracts) → `P1-SM-01` (now needs it) → `P1-SM-02` → `P1-RES-01` (step inputs/results) → `P1-EXEC-01`, `P1-API-03`.
- `P0-BIT-05` follows `P0-BIT-02`; `P0-INT-01` follows `P0-BIT-06` and `P0-OS-02`; `P1-API-01` needs `P0-NET-01` (not the HTTP parser); `P2-RET-01` no longer needs a heap; `P3-INT-01` and `P5-AI-01` no longer need optional unlocks.
- Parallel work table: `CURRICULUM.md` ("What can run in parallel"): career research with everything; bit work with Go/types/TCP; durability basics with early Phase 1; SDK with tests; observability, container and CI work during Phases 2–3; Python during Phases 2–4.

## 4. How the project demonstrates the targeted capabilities

Ten target capabilities each map to a concrete feature, a repeatable proof, specific unlocks and a completion criterion (`project/PLAN.md` table). The project does **not** demonstrate: replicated data stores or consensus, partitions between data nodes, data-intensive scale, message brokers, public cloud, infrastructure as code. Do not claim these on a CV. The three optional unlocks above address part of the gap.

## 5. Vietnam career evidence (preliminary, low confidence) and open questions

Full detail, tiers and limits: `career/CAREER_RESEARCH.md`; source records: `career/POSTINGS.md`. **No posting page has been read in full** (the session network could not reach the job sites). What exists is 42 search-result pointers (24 backend, 8 platform, 10 reliability/distributed), each with URL, title as shown, observation date 2026-11-16 and an unverified summary claim, plus salary figures from reports seen only through summaries. This is a convenience sample. It supports no counts, no market-share statement and no ranking of the directions.

What the summaries claimed, labelled as pointer claims: backend listings often state Go or backend years of 2–6; Kafka appears in four, Redis in two; Kubernetes appears in every platform/SRE summary read; Terraform in one; a CKA requirement in one; no summary described distributed-systems design work. Interpretations (I1–I5) and hypotheses (H1–H3) are listed separately in the research file. The salary sources differ in quality (survey versus vendor estimate) and cannot rank the directions.

`P0-CAR-01` is now a defensible initial snapshot, 7 h: at least 6 posting pages read in full per direction (18 in total), recorded with exact wording, tallied with sample sizes, with interpretations kept apart. It supplies evidence for a later priority decision and does not force one.

## 6. Remaining decisions that need your input

| # | Decision | Needed by | Notes |
|---|---|---|---|
| 1 | **Approve (or amend) the revised curriculum**, including the 2026-11-30 start and the revision-4 choices: complete Phase 4 recovery path kept (cut order shrinks to 35 h), just-in-time authoring rule, 362 h essential, three-operation restart | Before any teaching | Approval is yours alone; I have not marked it. Approval also fixes the catalog fingerprint |
| 2 | Confirm the reconciliation of `KNOWLEDGE_STANDARD_ADDENDUM.md` with the standard (D-003, D-004) | With approval | The standard is installed unchanged and governs; its status line and contents stay as supplied unless you approve a change. The addendum holds only extensions and the directory mapping |
| 3 | Career direction priority (backend / platform / reliability) | End of `P0-CAR-01` (about week 2); can defer | Sets the order of optional unlocks |
| 4 | Deeper career research: allow network access to the job sites so I can read postings, **or** accept that `P0-CAR-01` is your own research | Optional | Changing network settings is your decision; I have not touched them |
| 5 | Confirm my two judgment calls: keep `P0-INT-01` and a minimal Phase 5 as essential | With approval | Either can move to optional |
| 6 | Your OS and prior experience with Go, SQL, Linux, Docker | Start of `P0-GO-01` | Could shrink or grow Phase 0 estimates |

Not a decision: at the start of `P0-GO-01` you describe where your working code lives (`project/README.md`). Evidence bundles keep the course re-verifiable without it. A separate repository for code is only an optional future idea.

## Validation status

**Validated, by running the checker and its tests:**
- Valid repository: exit 0 in every mode. Deliberately broken temporary copies: exit 1 in every mode for every case tried.
- The old committed checker returned exit 0 under `--budget` and `--mermaid` on a repository with a bad prerequisite (reproduced on a copy of the committed tree); the new checker reports it in all modes.
- 50 behavioural tests (`python3 tools/test_check_course.py`), all passing. They cover: reporting modes keeping failures; missing directory and file; misplaced and retired documents; source code outside evidence bundles; archive without a restart note; edits to the standard and its status line; cycle, malformed and unknown prerequisites, essential-requires-optional, bad hours, header drift, `Uses:` drift, prerequisite-text drift; a cut order that contradicts C5, a cut that strands an unlock, budget prose and table drift, missing completion proofs, progress under an unapproved curriculum, approval without a fingerprint, a boundary change after approval, authoring a planned unlock; 19 evidence-bundle cases (one valid, 18 broken); broken references.
- One real checker gap was found by these tests and fixed: a malformed ID in `Requires` was silently dropped.

**Not validated:** the checker never runs a bundle's commands, so it does not show that any artifact reproduces; semantic dependencies are only checked where an unlock declares them in a `Uses:` line (a missing declaration is not detectable, so I also read each authored challenge by hand); every hour estimate; the acceptance criteria of `P1-DEF-01` and `P2-CONS-01` (observable by design, not run); career findings beyond search summaries; Tet date; tool versions; that a fresh Claude session follows `CLAUDE.md` correctly.

## Files changed in revisions 2 to 4

New: `career/CAREER_RESEARCH.md` (moved from the root), `project/README.md`, `project/PLAN.md`, `project/DECISIONS.md`, `knowledge/README.md`, `UNLOCKS/P1-DEF-01.md`. Rewritten: `CURRICULUM.md`, `COURSE_OBJECTIVE.md`, `UNLOCKS/CATALOG.md`, this report. Edited: `CLAUDE.md`, `README.md`, `LEARNER_PROFILE.md`, `LEARNER_STATE.md`, `SESSION_HANDOFF.md`, `DECISION_LOG.md` (D-002 appended), `PHASES/PHASE-0…6.md`, `UNLOCKS/README.md`, 12 existing unlock files (section rename, level tags removed, wiring), `KNOWLEDGE_STANDARD.md` (added unchanged), `KNOWLEDGE_STANDARD_ADDENDUM.md` (extensions and directory mapping), the old projects file (removed; replaced by `project/README.md`), `TEMPLATES/*`, `tools/check_course.py`. Nothing committed or pushed.
