# Curriculum Review Report — Revision 3

Date: 2026-11-16. Everything here is **PROPOSED, not approved.** Revision 2 applied your decisions (D-002); revision 3 adds the supplied knowledge standard (D-003) and the single-repository clarification (D-004). This report is a snapshot for the approval decision, not part of ongoing course state.

## 0. What changed since revision 1

**Revision 3:** one self-contained repository, with directories carrying the standard's boundaries: `knowledge/` (concepts, created on demand), `project/` (platform plan, decisions, design documents), `career/` (research). No other repository is assumed. The platform's design documents and evidence bundles live here; the platform's source code does not. The standard (`KNOWLEDGE_STANDARD.md`) is installed unchanged and governs. The repository-identity question is closed.

- Plan sized to **10 hours/week**: essential **357 h**, optional 124 h.
- Workflow model fixed: **declarative graphs with persisted step results**; replay is an optional experiment in an isolated project area (`PRJ-REPLAY-LAB`).
- Catalog: 81 unlocks (was 76), now with essential/optional class and hour estimates; one new authored unlock (`P1-DEF-01`).
- Calendar, phase files, objective, instructions updated. Career evidence added (preliminary).

## 1. Revised time budget and phase schedule

Window 2026-11-30 → 2027-09-30: 43.6 weeks, 436 gross hours, about 426 after removing one Tet week (expected around 6 Feb 2027; verify).

| Phase | Dates | Weeks | Capacity h | Essential h | Reserve h |
|---|---|---|---|---|---|
| 0 Foundation | 2026-11-30 → 2027-02-07 | 10 | 90 | 84 | 6 |
| 1 Execution engine | 2027-02-08 → 2027-04-11 | 9 | 90 | 81 | 9 |
| 2 Reliability | 2027-04-12 → 2027-05-23 | 6 | 60 | 52 | 8 |
| 3 Distributed execution | 2027-05-24 → 2027-07-04 | 6 | 60 | 45 | 15 |
| 4 Operability | 2027-07-05 → 2027-08-08 | 5 | 50 | 45 | 5 |
| 5 Intelligent execution | 2027-08-09 → 2027-08-22 | 2 | 20 | 20 | 0 |
| 6 Completion | 2027-08-23 → 2027-09-30 | 5.6 | 56 | 30 | ~26 |
| **Total** | | **43.6** | **426** | **357** | **~69** |

Essential effort split: build 185 h, study 66 h, verify 70 h, consolidate 36 h.

**Answer to "can it fit in 350–370 hours?" Yes, at 357 h, but with a thinner margin than the target suggests.** About 26 h of the 69 h reserve is held for hardening and career preparation, leaving about **43 h (12%)** for overruns and interruptions. If actual hours exceed my estimates by more than 12% the protected hardening time is consumed; above 19% the plan fails without extra weekend hours or cuts. My estimates are judgment, not measurements, and individual unlocks are likely off by ±25%. The plan therefore re-measures after the first 25 estimated hours and at each phase end, with a pre-agreed cut order (below). Extra weekend or weekday hours are not counted; they are insurance.

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

**Cut order if behind:** all of Phase 5 (20 h) → `P6-PERF-01` (6) → `P0-INT-01` (9) → `P4-OBS-03` tracing (5) → `P4-K8S-01` (7). C1–C3 and C5 are never cut. **When ahead:** `P1-PG-04`, `P3-DIST-01`, `P3-MSG-01`, `P4-IAC-01`/`P4-LNX-01`, `P5-LLM-02`, then the rest; order is pending your career choice.

## 3. Dependency graph changes

Checked by `tools/check_course.py`: acyclic; no prerequisite from a later phase; **no essential unlock requires an optional one**; authored files match the catalog.

- New: `P1-DEF-01` (graph and contracts) → `P1-SM-01` (now needs it) → `P1-SM-02` → `P1-RES-01` (step inputs/results) → `P1-EXEC-01`, `P1-API-03`.
- `P0-BIT-05` follows `P0-BIT-02`; `P0-INT-01` follows `P0-BIT-06` and `P0-OS-02`; `P1-API-01` needs `P0-NET-01` (not the HTTP parser); `P2-RET-01` no longer needs a heap; `P3-INT-01` and `P5-AI-01` no longer need optional unlocks.
- Parallel work table: `CURRICULUM.md` ("What can run in parallel"): career research with everything; bit work with Go/types/TCP; durability basics with early Phase 1; SDK with tests; observability, container and CI work during Phases 2–3; Python during Phases 2–4.

## 4. How the project demonstrates the targeted capabilities

Ten target capabilities each map to a concrete feature, a repeatable proof, specific unlocks and a completion criterion (`project/PLAN.md` table). The project does **not** demonstrate: replicated data stores or consensus, partitions between data nodes, data-intensive scale, message brokers, public cloud, infrastructure as code. Do not claim these on a CV. The three optional unlocks above address part of the gap.

## 5. Vietnam career evidence (preliminary, low confidence) and open questions

Full detail with limits: `career/CAREER_RESEARCH.md`. Collected from web-search summaries of roughly 25–30 postings. **I could not open the posting pages** (session network blocked `itviec.com`, `topdev.vn` and similar hosts), so nothing was read in full, dates are unverified, some postings may be expired, and the sample is not random.

| Direction | Observations | My interpretation (hypothesis) |
|---|---|---|
| Backend (Go, data-intensive) | Senior Go roles state years: 3+, 4+, 5+ Go or backend (Rikkeisoft, Vision, GFT, Ban Vien, Masan, Glints 6+). SQL, microservices, Docker, AWS/GCP recur. Kafka appears in 4 summaries (GFT, Grab, NexLab ×2); Redis alongside. "Distributed systems" appears in Masan, DatVietVAC, Vinrobotics. No ClickHouse posting found. | Years of Go are a barrier; entry is likely mid-to-senior backend with a strong public project. A Postgres-only course leaves a Kafka/Redis gap. |
| Platform | Kubernetes (GKE, OpenShift), GCP/Azure, Terraform, CI/CD, Linux recur (Web3 Vietnam, Trustify, Saritasa, Cyberlogitec, VPS). One summary says CKA required. Mostly DevOps titles; no confirmed "developer platform" role. | Screens on Kubernetes-in-production, cloud and Terraform; this course covers only local Kubernetes and no cloud/Terraform. |
| Distributed/reliability | SRE roles (Grab, Ninja Van, Carousell, Plus8soft, HCL, Axon) ask for Kubernetes, Go/Python, on-call. None described distributed-systems *design* work. Temporal appears in a Grab summary and a closed posting; Airflow in data-engineering roles. | Pure distributed-systems roles are rare in this sample. The project is an interview differentiator rather than a keyword match. |
| Compensation | ITviec 2025/2026 survey (summary): mid backend 30–55 M VND/month; senior band not seen. Recruiter rate card: senior DevOps 80–110 M. One employer (FPT Software) backend median total ≈ 215 M VND/year. Platform: no figure. Most postings hide salary. | Source quality differs (survey vs vendor); no direction can be ranked on pay yet. |

**Open questions the evidence raises:** Which direction hires career-changers from frontend? Do target employers screen on data-structure puzzles? How much do Kafka/Redis/Terraform/cloud matter versus the project? What do senior bands actually pay? `P0-CAR-01` is built to answer these with your own reading of postings.

## 6. Remaining decisions that need your input

| # | Decision | Needed by | Notes |
|---|---|---|---|
| 1 | **Approve (or amend) the revised curriculum**, including the 2026-11-30 start | Before any teaching | Approval is yours alone; I have not marked it |
| 2 | Confirm the reconciliation of `KNOWLEDGE_STANDARD_ADDENDUM.md` with the standard (D-003, D-004) | With approval | The standard is installed unchanged and governs; its status line and contents stay as supplied unless you approve a change. The addendum holds only extensions and the directory mapping |
| 3 | Career direction priority (backend / platform / reliability) | End of `P0-CAR-01` (about week 2); can defer | Sets the order of optional unlocks |
| 4 | Deeper career research: allow network access to the job sites so I can read postings, **or** accept that `P0-CAR-01` is your own research | Optional | Changing network settings is your decision; I have not touched them |
| 5 | Confirm my two judgment calls: keep `P0-INT-01` and a minimal Phase 5 as essential | With approval | Either can move to optional |
| 6 | Your OS and prior experience with Go, SQL, Linux, Docker | Start of `P0-GO-01` | Could shrink or grow Phase 0 estimates |

Not a decision: at the start of `P0-GO-01` you describe where your working code lives (`project/README.md`). Evidence bundles keep the course re-verifiable without it. A separate repository for code is only an optional future idea.

## Validation status

**Validated (by running the checker):** graph acyclic; prerequisites resolve and never point to later phases; essential never requires optional; 13 authored files match the catalog (headers, section order, next-unlock claims); state rules; hour totals and phase sums computed by `--budget` (357 h essential, matching the tables here). The checker caught 9 deliberately injected errors in revision 1, and the new essential-requires-optional rule was tested on a corrupted copy (it reported `P1-API-01: essential unlock requires optional P0-NET-02`).

**Not validated:** every hour estimate; acceptance criteria of the new `P1-DEF-01` (observable by design, not run); all career findings beyond what search summaries said; Tet date; tool versions; that a fresh Claude session follows `CLAUDE.md` correctly.

## Files changed in revision 2

New: `career/CAREER_RESEARCH.md` (moved from the root), `project/README.md`, `project/PLAN.md`, `project/DECISIONS.md`, `knowledge/README.md`, `UNLOCKS/P1-DEF-01.md`. Rewritten: `CURRICULUM.md`, `COURSE_OBJECTIVE.md`, `UNLOCKS/CATALOG.md`, this report. Edited: `CLAUDE.md`, `README.md`, `LEARNER_PROFILE.md`, `LEARNER_STATE.md`, `SESSION_HANDOFF.md`, `DECISION_LOG.md` (D-002 appended), `PHASES/PHASE-0…6.md`, `UNLOCKS/README.md`, 12 existing unlock files (section rename, level tags removed, wiring), `KNOWLEDGE_STANDARD.md` (added unchanged), `KNOWLEDGE_STANDARD_ADDENDUM.md` (extensions and directory mapping), `PROJECTS.md` (removed; replaced by `project/README.md`), `TEMPLATES/*`, `tools/check_course.py`. Nothing committed or pushed.
