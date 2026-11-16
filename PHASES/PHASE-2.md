# Phase 2 — Reliability

**Dates (proposed):** 2027-04-12 → 2027-05-23 (6 weeks). **Essential 52 h** of 60 h capacity. No optional unlocks.

## Purpose
Make workflows survive failure: restarts, retries, duplicates, timeouts.

## Required capabilities
Append-only history; idempotent requests; retry policy with backoff and jitter; timeouts and cancellation; recovery of unfinished work; failure injection; delivery semantics (at-least-once plus idempotent effects).

## Domains
Durability, transaction boundaries, consistency, failure modeling, testing under failure. Probability (retry spread) taught inside `P2-RET-01`.

## Dependencies
Phase 1 (`P1-SM-02`, `P1-RES-01`, `P1-API-03`, `P1-EXEC-01`). Recovery works from saved step results; no replay is needed.

## Expected deliverables
Durable engine: history table as source of truth; idempotency; retries; recovery after `kill -9`; failure-injection harness; `docs/invariants.md` extended.

## Exit criteria
`P2-INT-01` complete: automated test kills the engine mid-workflow and the workflow completes; duplicate-effect scenarios are tested; invariants document lists each guarantee with its test.

## Contribution to the objective
Delivers completion criterion C2. This is the core of what "reliable" means in the project.
