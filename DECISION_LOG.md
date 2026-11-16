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
