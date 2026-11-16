# Phase 4 — Operability

**Dates (proposed):** 2027-07-05 → 2027-08-08 (5 weeks). **Essential 45 h** of 50 h capacity. Optional pool 11 h. `P4-OBS-01/02`, `P4-DOC-01` and `P4-CI-01` may start during Phases 2–3 (weekday-sized).

## Purpose
Run the system as a service: build, ship, observe, secure, recover.

## Required capabilities
Container images; CI; structured logs, metrics, tracing; local Kubernetes deploy with probes and rollout/rollback; security baseline; recovery drills and runbooks.

## Domains
Docker, Kubernetes (capped depth), CI/CD, OpenTelemetry, security. Optional: Linux operations (`P4-LNX-01`), Terraform basics (`P4-IAC-01`).

## Dependencies
Phase 1 deliverable, Phase 3 multi-worker engine for tracing and drills.

## Expected deliverables
Container images built in CI, local cluster deployment, dashboards or queries for key signals, threat model, runbooks tested in a drill.

## Exit criteria
`P4-INT-01` complete: C4 and C5 satisfied with evidence.

## Contribution to the objective
Converts a program into a service, which is what platform roles hire for.
