# Workflow Platform Plan (PRJ-ENGINE)

Owner: learner approves; Claude proposes. Status: **APPROVED** with the curriculum on 2026-11-16 (D-007). The architecture and acceptance criteria below are hypotheses until implemented and tested. This is the plan for the project the course builds. It holds plans, scope, architecture decisions and milestones, not source code. Where the code lives: `project/README.md`.

## Purpose

A workflow execution platform: it runs workflows (sets of steps with a defined order), saves their progress, and finishes them correctly even when processes crash or workers disagree. Course-level mission and completion criteria C1–C8: `COURSE_OBJECTIVE.md`.

## Execution model (decided by the learner, D-002)

Workflows are **declarative graphs with persisted step results.**

- A workflow definition is data: steps, dependencies between steps, a version.
- Every step has a stable **identity**, a **state**, a declared **input contract** and **output contract**, and a saved **result** (output, error, attempts, timestamps).
- The engine reads saved state to decide what to do next. It supports inspection, retries and recovery from saved state. It does not need deterministic replay.
- Deterministic replay is an **optional advanced experiment** (`PX-REPLAY-01`), done as an isolated project area (`PRJ-REPLAY-LAB`) on a toy workflow. It must not expand or restructure the essential project.

## Other scope decisions (proposed)

- **Delivery guarantee:** at-least-once execution with idempotent effects, stated precisely in "Delivery guarantees" below. The platform never claims exactly-once execution. PD-004 in `project/DECISIONS.md` records the decision.
- **Single datastore:** PostgreSQL only. No Kafka, Redis, etcd or custom consensus in the essential plan. An optional unlock (`P3-MSG-01`) compares a broker.

## Delivery guarantees

Terms. An **attempt** is one execution of a step's handler by a worker. A **commit** is the single database transaction that records an attempt's outcome as the step's result and moves the step's state. An **effect** is a change outside the engine database (an email sent, a payment created).

| # | Guarantee | What it means | Where it is shown |
|---|---|---|---|
| G1 | At-least-once execution | A handler may execute more than once for the same step: retries, recovery after a crash, an expired lease. The engine never promises otherwise. | `P2-CONS-01`, `P3-TST-01` |
| G2 | At most one committed result | At most one successful result is committed per step. A second commit for the same step is rejected inside the commit transaction. | `P1-SM-02`, `P3-TST-01` |
| G3 | No commit after losing ownership | A worker whose lease expired or was taken over cannot commit. The commit carries a fencing token and the transaction rejects a stale one. G3 does **not** stop that worker's handler from still running and causing effects until it notices. | `P3-FENCE-01`, `P3-TST-01` |
| G4 | Idempotent effects where the outside system allows it | Each effect has an identity: a deterministic key built from workflow instance, step and effect name, **not** the attempt number. If the outside system honors the idempotency contract, repeated attempts produce one effect. | `P2-CONS-01`, `P3-TST-01` |

**The idempotency contract** the outside system must meet: the same key returns the same outcome and never causes a second effect, and the key is remembered at least as long as the longest possible retry period. If either part fails, G4 does not hold.

**The crash window.** The engine calls the outside system, the effect succeeds, and the engine crashes before it commits the result. After restart the engine cannot know whether the effect happened. Only the outside system can answer, and only through the key: the retry sends the same key, the system returns the original outcome, and the engine commits it once.

**When the outside system has no idempotency support,** the engine cannot prevent a duplicate. The step uses one of two policies, and each costs something:
- *Retry*: may duplicate the effect.
- *No retry after an ambiguous failure*: the step ends failed with outcome `outcome_unknown` for a person to reconcile; the effect may be missing.
There is no policy that avoids both. Checking the outside system for the effect before retrying narrows the window but is not a guarantee unless that check and the effect are atomic on its side.

**Two different idempotency problems.** *Request idempotency* (`P2-IDEM-01`) stops a retried API request from creating a second workflow; the key is chosen by the client. *Effect idempotency* (`P2-CONS-01`) stops a retried step from repeating an outside effect; the key is chosen by the engine. They use different keys, different tables and different failure windows. Both are taught and both are proved.

**Not guaranteed.** Completion time; that handlers are safe to repeat on their own; that a stale worker's effects have not happened; any effect on a system outside the idempotency contract.

**How each statement is proved** (repeatable tests, run from the evidence bundle):

| Test | Shows | Closes |
|---|---|---|
| T1 Lease expires mid-step; the handler runs twice | G1: the invocation count exceeds 1 while the committed result count is exactly 1 | C3 |
| T2 Two commits race for one step | G2: one succeeds, the other is rejected | C3 |
| T3 A worker is paused past its lease, another finishes, the first resumes | G3: the stale commit is rejected and the stored result is unchanged | C3 |
| T4 Crash after the effect, before the commit, key-honoring external system | G4: exactly one effect, one committed result, handler ran at least twice | C2 |
| T5 Same crash, external system ignores keys | The duplicate is observed; the *no retry* policy avoids it and records `outcome_unknown` | C2 |
| T6 T1–T4 repeated under the multi-worker chaos run | The guarantees hold with concurrency | C3 |

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
| Idempotency, retries, timeouts, cancellation | Request idempotency keys; effect keys; persisted backoff; timeouts; cancel | 50-concurrent-duplicates test (requests); crash-window test T4 and T5 (effects); retry and timeout tests | `P2-IDEM-01`, `P2-CONS-01`, `P2-RET-01`, `P2-TMO-01` | C2 |
| Concurrent and distributed worker coordination | Safe claiming, leases, fencing tokens, bounded worker pool | Tests T1–T3 and T6: handlers may repeat, at most one result is committed per step, a stale worker's commit is rejected | `P3-Q-01`, `P3-LEASE-01`, `P3-FENCE-01`, `P3-POOL-01`, `P3-TST-01` | C3 |
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
| M2 Durable engine | 2 | `P2-INT-01` | Idempotent requests and effects, retries, history, recovery after `kill -9`, tests T4 and T5 | C2 |
| M3 Multi-worker | 3 | `P3-INT-01` | Safe claiming, leases, fencing, chaos tests T1–T3 and T6 | C3 |
| M4 Operable platform | 4 | `P4-INT-01` (drill: `P4-OPS-01`) | CI-built image, local Kubernetes deploy, logs, metrics, traces, runbook used in a recovery drill with a drill record | C4, C5 |
| M5 AI extension | 5 | `P5-INT-01` | AI step with validation, timeout, retry, idempotency, cost cap, audit | C6 |
| M6 Complete | 6 | `P6-DOC-01`, `P6-CAR-01` | Architecture records, correctness and performance reports, demo, career package | C7, C8 |

## Design documents

Documents the learner writes as unlocks complete (workflow model, invariants, idempotency rules, claiming behavior) live in `project/design/`. The directory is created when the first one is written. Concept explanations they depend on are linked, not copied (`KNOWLEDGE_STANDARD.md` §9.1).
