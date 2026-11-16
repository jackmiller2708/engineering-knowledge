# Phase 5 — Intelligent execution

**Dates (proposed):** 2027-08-09 → 2027-08-22 (2 weeks). **Essential 20 h** of 20 h capacity (no reserve). Optional pool 12 h. **First phase to cut if behind schedule.** `P5-PY-01` may be done earlier in small pieces.

## Purpose
Add AI-driven steps without weakening the engine's guarantees.

## Required capabilities
Python basics for tooling; LLM API calls with schema-validated output; treating AI as an untrusted, slow, costly, nondeterministic step with timeout, retry, idempotency and a cost cap. Optional: tool calling with allow-lists (`P5-LLM-02`), human approval and audit trail (`P5-AI-02`).

## Domains
Python, LLM APIs, structured output, tool calling, validation boundaries. Retrieval (`P5-RAG`) is deliberately not in the catalog; add it only by decision if time allows.

## Dependencies
`P1-API-03` (for Python start), `P2-CONS-01`, `P3-INT-01`.

## Expected deliverables
An AI step type with schema validation, timeout, retry, idempotency, cost cap, and an audit record in the execution history.

## Exit criteria
`P5-INT-01` complete: C6 satisfied; a test shows invalid or hostile model output is rejected without breaking workflow state, and a test shows the cost cap stopping a run.

## Contribution to the objective
Shows the learner can integrate AI under engineering control, which is a current market theme. (Market claims are unverified until `P0-CAR-01` provides evidence.)
