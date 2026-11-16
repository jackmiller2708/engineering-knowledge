# Course Objective

Owner: learner (changes need explicit approval). Status: **APPROVED** 2026-11-16 (see `CURRICULUM.md` and D-007). Approval authorizes the course to begin; the project's designs and acceptance criteria remain hypotheses until implemented and tested.

## Mission

By **30 September 2027**, the learner can design, build, verify, deploy and operate a reliable workflow execution platform, and can explain and defend every major decision in it. The goal is hireable engineering ability for backend and platform roles in Vietnam, not a list of technologies seen. Which roles are worth targeting is an open question; evidence is in `career/CAREER_RESEARCH.md`.

## The ultimate project: PRJ-ENGINE (a workflow execution platform)

A workflow execution platform. A *workflow* is a set of steps with a defined order. The platform runs workflows, saves their progress, and finishes them correctly even when processes crash or workers disagree.

Project definition, execution model, scope, capability proof and milestones: `project/PLAN.md`. Architecture decisions: `project/DECISIONS.md`.

In one line: workflows are declarative graphs with persisted step results; delivery is at-least-once with idempotent effects; PostgreSQL is the only datastore.

## How the project maps to the three career directions being investigated

Hypotheses only; see `career/CAREER_RESEARCH.md` for evidence and its limits.

| Direction | Strongest evidence from the project | Visible gaps |
|---|---|---|
| Backend (Go, data-intensive) | Go service, PostgreSQL schema and transactions, API design, tests | No Go years on a CV; no broker, cache or scale work unless optional unlocks are taken |
| Platform / developer infrastructure | CI, containers, local Kubernetes, observability, runbooks, a typed SDK | No cloud provider, no Terraform; Kubernetes only locally |
| Distributed systems / reliability | Leases, fencing, failure injection, delivery semantics, invariants | Single database, no multi-node consensus |

## Is this the right project? (assessment)

**Fits:** it forces the targeted skills (state, transactions, concurrency, failure handling, operations), is explainable in minutes, and reuses the learner's TypeScript/API strength. The declarative-graph model keeps the core achievable by one person.

**Problems and mitigations:**

| Issue | Consequence | Mitigation |
|---|---|---|
| Phase 3 is the hardest and most uncertain | Overrun harms Phases 4–6 | Largest phase reserve; fixed chaos-test scope |
| "Distributed" means several processes on one database | Does not show partitions between data stores | Stated plainly above |
| AI is nondeterministic | Could break engine guarantees | AI is only a step; its output is validated and recorded |
| Kubernetes can swallow weeks | Phase 4 overruns | Local cluster only; depth capped |
| Scope creep toward a commercial product | Never finishes | Non-goals; changes need a logged decision |
| Estimates are judgment | Dates may be wrong | Recalibration checkpoints in `CURRICULUM.md` |

## Completion criteria

Complete when all hold, each backed by evidence in `EVIDENCE/`:

- **C1** PRJ-ENGINE runs a workflow graph end to end via API and SDK; each step's state and result can be inspected.
- **C2** (durability and effects) Tests kill a worker or the engine mid-workflow and the workflow still finishes correctly from saved state. Handlers may run more than once. For an external system that honors idempotency keys, a test that crashes the engine after the effect succeeded and before the result was committed ends with exactly one effect and exactly one committed result. For an external system that does not, the test shows the duplicate and demonstrates the documented step policy (retry with duplicate risk, or no retry with outcome recorded as unknown).
- **C3** (ownership and commits) With at least 3 worker processes, a repeatable test shows: (a) a handler may be executed more than once for a step; (b) at most one successful result is committed per step; (c) a worker whose ownership expired cannot commit, so a paused-then-resumed stale worker's commit is rejected and the stored result is unchanged; (d) external effects stay idempotent under the same chaos run. C3 does not claim that handlers run once.
- **C4** Deployed to a local Kubernetes cluster from CI-built images, with logs, metrics and a trace for one workflow run.
- **C5** A written runbook has been used in a recovery drill on the deployed platform: a failure is injected (for example kill a worker, restart the database, let a lease expire); it is detected through the logs, metrics or trace; recovery follows the runbook only; afterwards the C2 and C3 checks are re-run. The drill record states the failure, the signal that revealed it, the steps followed, the time to recover and the check results.
- **C6** An AI step runs with schema validation, timeout, retry, idempotency, cost cap and an audit record in the execution history. (Tool allow-lists and human approval are optional extensions.)
- **C7** The learner explains and defends the architecture (decision records, invariants, known limits) at the mastery level set in `UNLOCKS/CATALOG.md`.
- **C8** A career package exists: portfolio write-up, role mapping from real postings (`P0-CAR-01`), interview preparation notes.

If time runs short, follow the cut order in `CURRICULUM.md`. Only C6 can be waived; C1–C5, C7 and C8 stay reachable under every cut.

## Completion proofs (machine-checked)

Each criterion is closed by the unlock(s) below and everything they require. `Cuttable: no` means no cut in `CURRICULUM.md` may remove anything the proof needs. `tools/check_course.py` verifies this. It checks the dependency structure only; it does not run any proof.

| Criterion | Proof unlocks | Cuttable |
|---|---|---|
| C1 | P1-INT-01 | no |
| C2 | P2-INT-01 | no |
| C3 | P3-INT-01 | no |
| C4 | P4-INT-01 | no |
| C5 | P4-OPS-01 | no |
| C6 | P5-INT-01 | yes |
| C7 | P6-ARCH-01, P6-VER-01 | no |
| C8 | P6-CAR-01 | no |
