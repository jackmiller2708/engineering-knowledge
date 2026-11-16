# Workflow Platform Plan (PRJ-ENGINE)

Owner: learner approves; Claude proposes. Status: **PROPOSED** (part of the unapproved curriculum). This is the plan for the project the course builds. It holds plans, scope, architecture decisions and milestones, not source code. Where the code lives: `project/README.md`.

## Purpose

A workflow execution platform: it runs workflows (sets of steps with a defined order), saves their progress, and finishes them correctly even when processes crash or workers disagree. Course-level mission and completion criteria C1–C8: `COURSE_OBJECTIVE.md`.

## Execution model (decided by the learner, D-002)

Workflows are **declarative graphs with persisted step results.**

- A workflow definition is data: steps, dependencies between steps, a version.
- Every step has a stable **identity**, a **state**, a declared **input contract** and **output contract**, and a saved **result** (output, error, attempts, timestamps).
- The engine reads saved state to decide what to do next. It supports inspection, retries and recovery from saved state. It does not need deterministic replay.
- Deterministic replay is an **optional advanced experiment** (`PX-REPLAY-01`), done as an isolated project area (`PRJ-REPLAY-LAB`) on a toy workflow. It must not expand or restructure the essential project.

## Other scope decisions (proposed)

- **Delivery guarantee:** at-least-once execution plus idempotent effects. No exactly-once claims.
- **Single datastore:** PostgreSQL only. No Kafka, Redis, etcd or custom consensus in the essential plan. An optional unlock (`P3-MSG-01`) compares a broker.

## Explicit non-goals

Multi-tenant SaaS features, billing, a visual workflow designer, autoscaling, multi-region operation, SDKs beyond TypeScript, loops or dynamic step creation in workflows, performance parity with commercial products. An Angular inspection UI is an optional stretch.

## How the project demonstrates each target capability

Each row says what exists, how it is proved, and where it is learned. If the proof does not exist, the capability is not claimed.

| Target capability | What the project contains | Proof (repeatable) | Unlocks | Criterion |
|---|---|---|---|---|
| Typed public API and SDK | Versioned HTTP API, validation, one error model, TypeScript SDK | Contract tests; SDK test that retries a timed-out request | `P1-API-01/02/03`, `P1-SDK-01`, `P2-IDEM-01` | C1 |
| Workflow definitions and state machines | Declarative graph with step contracts; pure lifecycle machines for instance and step | Exhaustive transition test; invariants document with a test per invariant | `P1-DEF-01`, `P1-SM-01` | C1 |
| Durable execution and persistent state | All state, step results and history in PostgreSQL | Restart test: state intact | `P1-SM-02`, `P1-RES-01`, `P2-DUR-01` | C2 |
| Transaction boundaries and consistency | Atomic transitions; documented boundaries; anomaly experiments | Tests that fail without the fix | `P1-PG-03`, `P1-SM-02` | C2, C7 |
| Idempotency, retries, timeouts, cancellation | Idempotency keys; persisted backoff; timeouts; cancel | 50-concurrent-duplicates test; retry and timeout tests | `P2-IDEM-01`, `P2-RET-01`, `P2-TMO-01` | C2 |
| Concurrent and distributed worker coordination | Safe claiming, leases, fencing tokens, bounded worker pool | Multi-worker chaos test: no step committed twice; stale worker rejected | `P3-Q-01`, `P3-LEASE-01`, `P3-FENCE-01`, `P3-POOL-01`, `P3-TST-01` | C3 |
| Recovery after process failures | Resume unfinished work on restart | `kill -9` mid-workflow test; failure-injection harness | `P2-REC-01`, `P2-FAIL-01` | C2 |
| Execution history, observability, tracing | Append-only history; structured logs; metrics; one trace per run | A traced run inspected end to end | `P2-DUR-01`, `P4-OBS-01/02/03` | C4 |
| Deployment, monitoring, operational recovery | Container image, CI, local Kubernetes, runbooks, recovery drill | Drill record; deploy from CI-built image | `P4-DOC-01`, `P4-CI-01`, `P4-K8S-01`, `P4-OPS-01` | C4, C5 |
| Controlled AI integration | AI step with validation, timeout, retry, idempotency, cost cap, audit | Hostile-output test; budget exhaustion test | `P5-LLM-01`, `P5-AI-01`, `P5-INT-01` | C6 |

## What the project does not demonstrate

Replicated data stores or consensus; real network partitions between data nodes; data-intensive scale (volume, streaming, analytics); message brokers; public-cloud services; infrastructure as code. Optional unlocks (`P1-PG-04`, `P3-MSG-01`, `P4-IAC-01`) address part of this. Do not claim it otherwise in a CV.


## Milestones

One milestone per phase, each closed by an integration unlock. Exit criteria and details: `PHASES/PHASE-N.md`. Dates: `CURRICULUM.md`.

| Milestone | Phase | Closed by | What exists | Criterion |
|---|---|---|---|---|
| M0 Foundations | 0 | `P0-INT-01` (and the gate unlocks) | Hex dump tool, bit and codec packages, framed parser, crash-safe record log, TCP echo server | — |
| M1 Engine v0.1 | 1 | `P1-INT-01` | Graph definitions, state machine, persisted step results, API, TypeScript SDK | C1 |
| M2 Durable engine | 2 | `P2-INT-01` | Idempotent requests, retries, history, recovery after `kill -9` | C2 |
| M3 Multi-worker | 3 | `P3-INT-01` | Safe claiming, leases, fencing, chaos tests | C3 |
| M4 Operable platform | 4 | `P4-INT-01` | CI-built image, local Kubernetes deploy, logs, metrics, traces, runbook drill | C4, C5 |
| M5 AI extension | 5 | `P5-INT-01` | AI step with validation, timeout, retry, idempotency, cost cap, audit | C6 |
| M6 Complete | 6 | `P6-DOC-01`, `P6-CAR-01` | Architecture records, correctness and performance reports, demo, career package | C7, C8 |

## Design documents

Documents the learner writes as unlocks complete (workflow model, invariants, idempotency rules, claiming behavior) live in `project/design/`. The directory is created when the first one is written. Concept explanations they depend on are linked, not copied (`KNOWLEDGE_STANDARD.md` §9.1).
