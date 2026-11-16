# Phase 3 — Distributed execution

**Dates (proposed):** 2027-05-24 → 2027-07-04 (6 weeks). **Essential 45 h** of 60 h capacity (largest reserve: highest-risk phase). Optional pool 18 h.

## Purpose
Run work on several worker processes with defined ownership and no double commits.

## Required capabilities
Race detection and shared-state invariants; safe job claiming; leases with heartbeats; fencing tokens; bounded worker pools and graceful shutdown; reasoning about clocks and delays; multi-worker delivery semantics; chaos testing.

## Domains
Concurrency, synchronization, queues, coordination, delivery semantics. "Distributed" here means multiple processes sharing one PostgreSQL. This is stated plainly; it does not cover replicated data stores or consensus.

## Dependencies
Phase 2 (`P2-REC-01`, `P2-FAIL-01`), plus `P0-GO-03`.

## Expected deliverables
Multi-worker engine, lease and fencing implementation, chaos test suite, delivery-semantics document.

## Exit criteria
`P3-INT-01` complete: with at least 3 workers, repeatable chaos run shows no step committed twice and stale-worker commits rejected; ownership rules documented. Optional: clock/partial-failure experiments (`P3-DIST-01`), delivery write-up (`P3-DLV-01`), broker comparison (`P3-MSG-01`).

## Contribution to the objective
Delivers C3. Main schedule risk: time box strictly. The optional unlocks are the first thing not to start if behind.
