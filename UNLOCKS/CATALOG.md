# Unlock Catalog (the dependency graph and time budget)

Owner: learner approves changes. This table is the single source for **prerequisites, mastery targets, class and hour estimates**. Each authored unlock file repeats `requires` and `mastery` in its header; `tools/check_course.py` fails if they differ.

- `Class`: **E** = essential (counts toward the plan), **O** = optional (extra depth; never blocks an essential unlock). An essential unlock may not require an optional one.
- `Hours`: estimate `build+study+verify+consolidate`. *Build* = writing and running code. *Study* = reading specs/docs and experiments to understand. *Verify* = tests, evaluation session, questions. *Consolidate* = notes, cleanup, revision. These are **judgment estimates, not measurements**; they are recalibrated from recorded actual hours (`LEARNER_STATE.md`).
- `Definition`: `authored` = full file `UNLOCKS/<ID>.md` exists. `planned` = title and place in the graph only; do not teach until authored and approved.
- Phase rule: an unlock may only require unlocks from the same or an earlier phase (`PX` is the stretch track, ranked last).
- Totals by phase: `python3 tools/check_course.py --budget`.

## Phase 0 — Foundation

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P0-CAR-01 | Collect an initial market snapshot from real job postings | — | L3 | E | 1+4+1+1 | planned |
| P0-GO-01 | Set up Go and ship a tested command-line tool | — | L3 | E | 3+1+1+1 | authored |
| P0-GO-02 | Go types, interfaces and errors, for a TypeScript developer | P0-GO-01 | L3 | E | 4+1+1+1 | planned |
| P0-GO-03 | Goroutines, channels and context basics | P0-GO-02 | L3 | E | 4+2+1+0 | planned |
| P0-BIT-01 | Manipulate individual bits | P0-GO-01 | L3 | E | 2+1+1+0 | authored |
| P0-BIT-02 | Build and apply bit masks | P0-BIT-01 | L3 | E | 3+1+1+0 | authored |
| P0-BIT-03 | Represent permissions as flags | P0-BIT-02 | L3 | O | 2+0+1+0 | authored |
| P0-BIT-04 | Pack structured data into bits | P0-BIT-02 | L3 | O | 3+0+1+0 | authored |
| P0-BIT-05 | Encode and decode binary formats (endianness, varints) | P0-BIT-02 | L4 | E | 4+1+1+1 | authored |
| P0-BIT-06 | Parse a framed binary protocol safely | P0-BIT-05 | L4 | E | 5+1+2+1 | authored |
| P0-BIT-07 | Package the codecs as a reusable library | P0-BIT-03, P0-BIT-04, P0-BIT-06 | L3 | O | 2+0+1+1 | authored |
| P0-DS-01 | Measure cost: benchmarks and growth rates | P0-GO-01 | L3 | E | 3+1+1+0 | planned |
| P0-DS-02 | Build a hash table from scratch | P0-DS-01, P0-BIT-02 | L4 | O | 5+1+1+0 | planned |
| P0-DS-03 | Ordered search trees and why databases use B-trees | P0-DS-01 | L3 | O | 4+2+1+0 | planned |
| P0-DS-04 | Heap and priority queue for timers | P0-DS-01 | L3 | O | 3+1+1+0 | planned |
| P0-MEM-01 | Stack, heap, pointers and escape analysis in Go | P0-GO-02 | L3 | O | 3+2+1+0 | planned |
| P0-OS-01 | Processes, files and system calls: observe with strace | P0-GO-01 | L3 | E | 2+1+1+0 | planned |
| P0-OS-02 | File durability: write, fsync and crash-safe updates | P0-OS-01 | L4 | E | 3+1+1+0 | planned |
| P0-NET-01 | Build a TCP echo server by hand | P0-GO-02 | L3 | E | 2+1+1+0 | planned |
| P0-NET-02 | Parse HTTP/1.1 requests over raw TCP | P0-NET-01, P0-BIT-06 | L3 | O | 5+1+1+0 | planned |
| P0-TYPE-01 | Model data so illegal states cannot be built | P0-GO-02 | L4 | E | 3+2+1+1 | planned |
| P0-INT-01 | Append-only record log with crash recovery | P0-BIT-06, P0-OS-02 | L4 | E | 6+1+1+1 | planned |

## Phase 1 — Execution engine

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P1-PG-01 | Run PostgreSQL and query it from Go | P0-GO-02 | L3 | E | 2+1+1+0 | planned |
| P1-PG-02 | Schema and migrations for workflows | P1-PG-01, P0-TYPE-01 | L4 | E | 3+2+1+0 | planned |
| P1-PG-03 | Transactions and isolation: reproduce anomalies | P1-PG-01, P0-GO-03 | L4 | E | 4+2+1+1 | authored |
| P1-PG-04 | Indexes and query plans on a large table | P1-PG-02 | L3 | O | 4+1+1+0 | planned |
| P1-DEF-01 | Declarative workflow graph: steps, contracts, validation | P0-TYPE-01 | L5 | E | 3+2+1+1 | authored |
| P1-SM-01 | Instance and step lifecycle as a pure state machine | P0-TYPE-01, P1-DEF-01 | L5 | E | 4+2+1+1 | authored |
| P1-SM-02 | Persist state transitions atomically | P1-SM-01, P1-PG-02, P1-PG-03 | L5 | E | 3+1+1+1 | planned |
| P1-RES-01 | Persist step inputs and results; inspect a run | P1-DEF-01, P1-SM-02 | L4 | E | 3+1+1+0 | planned |
| P1-API-01 | HTTP API skeleton and resource design | P0-NET-01, P1-PG-02 | L3 | E | 3+1+1+0 | planned |
| P1-API-02 | Input validation and a consistent error model | P1-API-01 | L4 | E | 2+1+1+0 | planned |
| P1-API-03 | Create, start and inspect workflows via API | P1-API-02, P1-RES-01 | L4 | E | 3+1+1+0 | planned |
| P1-TEST-01 | Test strategy: table, property and real-database tests | P1-SM-01, P1-PG-01 | L4 | E | 3+1+1+1 | planned |
| P1-EXEC-01 | Single-process step executor with handler registry | P1-SM-02, P1-RES-01, P0-GO-03 | L4 | E | 5+1+1+1 | planned |
| P1-SDK-01 | Typed TypeScript SDK from the API contract | P1-API-03 | L3 | E | 3+1+1+0 | planned |
| P1-INT-01 | Engine v0.1 demo | P1-EXEC-01, P1-API-03, P1-TEST-01 | L4 | E | 1+0+2+1 | planned |

## Phase 2 — Reliability

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P2-DUR-01 | Append-only execution history as source of truth | P1-SM-02 | L4 | E | 3+1+1+1 | planned |
| P2-IDEM-01 | Idempotent API requests | P1-API-03, P1-PG-03, P1-SDK-01 | L5 | E | 4+2+1+1 | authored |
| P2-RET-01 | Retry policy with backoff and jitter, persisted | P1-EXEC-01 | L4 | E | 3+1+1+1 | planned |
| P2-TMO-01 | Timeouts and cancellation | P1-EXEC-01 | L4 | E | 3+2+1+0 | planned |
| P2-REC-01 | Recover unfinished workflows after restart | P2-DUR-01, P2-RET-01 | L5 | E | 4+1+2+1 | planned |
| P2-FAIL-01 | Failure-injection harness (kill mid-step, database errors) | P2-REC-01 | L4 | E | 4+0+2+1 | planned |
| P2-CONS-01 | Idempotent step effects and delivery guarantees | P2-IDEM-01, P2-REC-01 | L5 | E | 5+2+1+1 | authored |
| P2-INT-01 | Durability demo and written invariants | P2-FAIL-01, P2-CONS-01 | L5 | E | 1+1+2+1 | planned |

## Phase 3 — Distributed execution

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P3-CON-01 | Find and fix a data race; define shared-state invariants | P0-GO-03, P1-EXEC-01 | L4 | E | 3+2+1+0 | planned |
| P3-Q-01 | Claim work safely with SELECT FOR UPDATE SKIP LOCKED | P2-REC-01, P1-PG-03 | L4 | E | 3+1+1+1 | authored |
| P3-LEASE-01 | Lease-based ownership with expiry and heartbeat | P3-Q-01, P2-TMO-01 | L5 | E | 4+2+1+1 | planned |
| P3-FENCE-01 | Fencing tokens: reject commits from stale workers | P3-LEASE-01 | L5 | E | 3+1+1+1 | planned |
| P3-POOL-01 | Worker pool with bounded concurrency and graceful shutdown | P3-CON-01, P3-LEASE-01 | L4 | E | 4+1+1+1 | planned |
| P3-DIST-01 | Clocks, delays and partial failure: experiments | P3-LEASE-01 | L4 | O | 3+2+1+0 | planned |
| P3-DLV-01 | Multi-worker delivery semantics: write-up and tests | P2-CONS-01, P3-FENCE-01 | L5 | O | 2+1+1+0 | planned |
| P3-MSG-01 | Same workload on a message broker, compared with the Postgres queue | P3-Q-01 | L4 | O | 5+2+1+0 | planned |
| P3-TST-01 | Chaos tests for multiple workers | P3-POOL-01, P2-FAIL-01, P2-CONS-01 | L4 | E | 4+0+2+1 | planned |
| P3-INT-01 | Multi-worker demo with ownership guarantees | P3-TST-01, P3-FENCE-01 | L5 | E | 1+0+2+2 | planned |

## Phase 4 — Operability

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P4-LNX-01 | Linux operations: signals, limits, service management | P0-OS-01 | L3 | O | 3+1+1+0 | planned |
| P4-DOC-01 | Containerize the engine (multi-stage, non-root) | P0-OS-01, P1-INT-01 | L3 | E | 3+1+1+0 | planned |
| P4-CI-01 | CI pipeline: test, race detector, lint, image build | P1-TEST-01, P4-DOC-01 | L3 | E | 2+1+1+0 | planned |
| P4-OBS-01 | Structured logs and correlation IDs | P1-API-02 | L3 | E | 2+1+1+0 | planned |
| P4-OBS-02 | Metrics with OpenTelemetry | P4-OBS-01 | L3 | E | 2+1+1+0 | planned |
| P4-OBS-03 | Distributed tracing from API to worker | P4-OBS-02, P3-POOL-01 | L4 | E | 3+1+1+0 | planned |
| P4-K8S-01 | Local Kubernetes deploy: probes, config, rollout, rollback | P4-DOC-01 | L3 | E | 4+2+1+0 | planned |
| P4-IAC-01 | Terraform basics: describe and create infrastructure as code | P4-DOC-01 | L3 | O | 3+2+1+0 | planned |
| P4-SEC-01 | Security baseline and threat model | P1-API-03 | L4 | E | 3+1+1+0 | planned |
| P4-OPS-01 | Recovery drills and runbooks | P4-K8S-01, P4-OBS-03, P3-INT-01 | L4 | E | 3+0+2+1 | planned |
| P4-INT-01 | Deployed, observable platform | P4-OPS-01, P4-CI-01, P4-SEC-01 | L4 | E | 2+0+2+1 | planned |

## Phase 5 — Intelligent execution

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P5-PY-01 | Python project, typing and HTTP client | P1-API-03 | L3 | E | 2+1+1+0 | planned |
| P5-LLM-01 | Call an LLM API with schema-validated output | P5-PY-01 | L3 | E | 3+1+1+0 | planned |
| P5-LLM-02 | Tool calling with allow-list and argument validation | P5-LLM-01 | L4 | O | 4+1+1+0 | planned |
| P5-AI-01 | AI as an untrusted step: timeout, retry, idempotency, cost cap | P5-LLM-01, P2-CONS-01 | L5 | E | 4+1+1+1 | planned |
| P5-AI-02 | Human approval gate and audit trail | P5-AI-01, P2-DUR-01 | L4 | O | 4+1+1+0 | planned |
| P5-INT-01 | AI-assisted workflow extension demo | P5-AI-01, P3-INT-01 | L4 | E | 2+0+1+1 | planned |

## Phase 6 — Completion

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| P6-ARCH-01 | Architecture review and decision records | P4-INT-01 | L5 | E | 3+1+1+1 | planned |
| P6-VER-01 | Correctness report: invariants and evidence | P3-INT-01, P2-INT-01 | L5 | E | 2+1+1+1 | planned |
| P6-PERF-01 | Load test and bottleneck analysis | P4-INT-01 | L4 | E | 4+1+1+0 | planned |
| P6-SEC-01 | Security review | P4-SEC-01, P4-INT-01 | L4 | O | 3+0+1+0 | planned |
| P6-DOC-01 | Documentation and live demo | P6-ARCH-01 | L3 | E | 3+0+1+1 | planned |
| P6-CAR-01 | Portfolio, CV and interview preparation | P6-DOC-01, P0-CAR-01 | L4 | E | 4+1+1+2 | planned |

## Stretch track (optional; never counts toward the plan)

| ID | Title | Requires | Mastery | Class | Hours | Definition |
|---|---|---|---|---|---|---|
| PX-RUST-01 | Re-implement the frame codec in Rust and compare | P0-BIT-06 | L3 | O | 5+2+1+0 | planned |
| PX-UI-01 | Angular execution-history viewer | P1-API-03 | L3 | O | 7+1+1+1 | planned |
| PX-REPLAY-01 | Advanced experiment: deterministic replay on a toy workflow, in an isolated project area | P2-REC-01 | L4 | O | 8+2+1+1 | planned |
