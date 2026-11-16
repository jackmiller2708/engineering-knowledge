# Platform Decision Log

Owner: learner approves; Claude proposes. Append-only. Architecture decisions for PRJ-ENGINE only (`KNOWLEDGE_STANDARD.md` §10.1 rule 5). Curriculum governance decisions are in `DECISION_LOG.md`.

## PD-001 — Workflow execution model: declarative graphs with persisted step results

- **Status:** Decided by the learner (2026-11-16, recorded in D-002). Part of a curriculum that is not yet approved.
- **Decision:** A workflow is data: steps, dependencies, a version. Each step has a stable identity, a state, a declared input contract and output contract, and a saved result. The engine decides what to do next from saved state. Inspection, retries and recovery work from that state.
- **Consequences:** The engine needs a validator for definitions (`P1-DEF-01`), a pure lifecycle machine (`P1-SM-01`), and persisted step results (`P1-RES-01`). Workflows cannot express loops or dynamic step creation; code-defined workflows are out of scope.
- **Alternative considered:** workflows as code, recovered by deterministic replay. Not in the essential project: it needs strict determinism rules and is a project in itself. Kept as optional `PX-REPLAY-01`, isolated.
- **Evidence still needed:** whether graph-with-results is expressive enough for the AI step (Phase 5) is an assumption until `P5-INT-01`.

## PD-002 — Delivery guarantee: at-least-once with idempotent effects

- **Status:** Proposed.
- **Decision:** A step may run more than once; effects must be safe to repeat. No exactly-once claim.
- **Consequences:** Idempotency keys (`P2-IDEM-01`), retry policy (`P2-RET-01`), documented delivery semantics (`P2-CONS-01`).

## PD-003 — Single datastore: PostgreSQL

- **Status:** Proposed.
- **Decision:** State, history and work claiming use PostgreSQL only. No broker, cache or consensus system in the essential plan.
- **Consequences:** Claiming relies on row locks (`P3-Q-01`). "Distributed" means several processes sharing one database; this limit is stated in `PLAN.md`. Optional `P3-MSG-01` compares a broker.
