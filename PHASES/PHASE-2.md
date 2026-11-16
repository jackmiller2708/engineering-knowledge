# Phase 2 — Reliability

**Dates (proposed):** 2027-04-12 → 2027-05-23 (6 weeks). **Essential 55 h** of 60 h capacity. No optional unlocks.

## Purpose
Make workflows survive failure: restarts, retries, duplicates, timeouts.

## Required capabilities
Append-only history; idempotent requests; retry policy with backoff and jitter; timeouts and cancellation; recovery of unfinished work; failure injection; request idempotency and step-effect idempotency (two different problems); delivery guarantees G1–G4 (`project/PLAN.md`).

## Domains
Durability, transaction boundaries, consistency, failure modeling, testing under failure. Probability (retry spread) taught inside `P2-RET-01`.

## Dependencies
Phase 1 (`P1-SM-02`, `P1-RES-01`, `P1-API-03`, `P1-EXEC-01`). Recovery works from saved step results; no replay is needed.

## Expected deliverables
Durable engine: history table as source of truth; request idempotency; idempotent step effects against a fake external system; retries; recovery after `kill -9`; failure-injection harness; `project/design/invariants.md` extended.

## Exit criteria
`P2-INT-01` complete: an automated test kills the engine mid-workflow and the workflow completes from saved state; tests T4 and T5 (`project/PLAN.md`) run: after a crash between an external effect and the commit, a key-honoring external system ends with one effect and one committed result, and a key-ignoring one shows the duplicate and the documented policy; the invariants document lists each guarantee with its test. Evidence bundles record whether each test was preserved or independently reproduced.

## Contribution to the objective
Delivers completion criterion C2. This is the core of what "reliable" means in the project.
