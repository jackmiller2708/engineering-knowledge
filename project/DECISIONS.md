# Platform Decision Log

Owner: learner approves; Claude proposes. Append-only. Architecture decisions for PRJ-ENGINE only (`KNOWLEDGE_STANDARD.md` §10.1 rule 5). Curriculum governance decisions are in `DECISION_LOG.md`.

## PD-001 — Workflow execution model: declarative graphs with persisted step results

- **Status:** Decided by the learner (2026-11-16, recorded in D-002). Part of a curriculum that is not yet approved.
- **Decision:** A workflow is data: steps, dependencies, a version. Each step has a stable identity, a state, a declared input contract and output contract, and a saved result. The engine decides what to do next from saved state. Inspection, retries and recovery work from that state.
- **Consequences:** The engine needs a validator for definitions (`P1-DEF-01`), a pure lifecycle machine (`P1-SM-01`), and persisted step results (`P1-RES-01`). Workflows cannot express loops or dynamic step creation; code-defined workflows are out of scope.
- **Alternative considered:** workflows as code, recovered by deterministic replay. Not in the essential project: it needs strict determinism rules and is a project in itself. Kept as optional `PX-REPLAY-01`, isolated.
- **Evidence still needed:** whether graph-with-results is expressive enough for the AI step (Phase 5) is an assumption until `P5-INT-01`.

## PD-002 — Delivery guarantee: at-least-once with idempotent effects

- **Status:** Proposed. Wording superseded by PD-004 (the decision stands; PD-004 states it precisely).
- **Decision:** A step may run more than once; effects must be safe to repeat. No exactly-once claim.
- **Consequences:** Idempotency keys (`P2-IDEM-01`), retry policy (`P2-RET-01`), documented delivery semantics (`P2-CONS-01`).

## PD-003 — Single datastore: PostgreSQL

- **Status:** Proposed.
- **Decision:** State, history and work claiming use PostgreSQL only. No broker, cache or consensus system in the essential plan.
- **Consequences:** Claiming relies on row locks (`P3-Q-01`). "Distributed" means several processes sharing one database; this limit is stated in `PLAN.md`. Optional `P3-MSG-01` compares a broker.

## PD-004 — Delivery guarantees G1–G4 (states PD-002 precisely)

- **Status:** Proposed (part of the unapproved curriculum). Added 2026-11-16 by the correction pass (D-005).
- **Decision:** The platform guarantees: G1 a handler may execute more than once; G2 at most one successful result is committed per step; G3 a worker that lost ownership cannot commit; G4 a retried external effect does not duplicate where the external system honors the idempotency contract. It does not guarantee exactly-once execution, and it cannot prevent duplicates against a system without idempotency support. Full wording, the crash window and the two policies for such systems: `project/PLAN.md`, "Delivery guarantees".
- **Why:** An earlier wording ("no step is executed and committed twice") read as exactly-once execution, which contradicts at-least-once. The commit and the execution are different events with different guarantees.
- **Consequences:** Request idempotency (`P2-IDEM-01`) and effect idempotency (`P2-CONS-01`) are separate unlocks with separate keys. Chaos tests (`P3-TST-01`) check commits and effects, not only commits. Completion criteria C2 and C3 were rewritten to match.
- **Evidence still needed:** whether the idempotency contract is realistic for the external systems the learner cares about is an assumption; the fake external system in `P2-CONS-01` only models it.
