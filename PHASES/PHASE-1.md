# Phase 1 — Execution engine

**Dates (proposed):** 2027-02-08 → 2027-04-11 (9 weeks). **Essential 81 h** of 90 h capacity. Optional pool 6 h.

## Purpose
Make workflows executable: a single-process engine over declarative workflow graphs, with PostgreSQL state and persisted step results, a typed API and SDK.

## Required capabilities
Declarative workflow graphs with step contracts; relational modeling and migrations; transactions and isolation; pure state machines; persisted step results; HTTP API design, validation and error models; test strategy including real-database tests; step execution; typed SDK.

## Domains
Go services, PostgreSQL, API design, state machines, testing, TypeScript SDK.

## Dependencies
Phase 0 gate unlocks (see `PHASE-0.md`).

## Expected deliverables
PRJ-ENGINE v0.1: define, start and inspect workflow graphs over HTTP; steps run via a handler registry; every step's state and result saved and inspectable; transactional transitions; TypeScript SDK; workflow model and invariants documents.

## Exit criteria
`P1-INT-01` complete: demo runs from a clean copy of the project (evidence bundle); invalid definitions are rejected; state machine invariants have tests; every step's input, output and state are visible through the API; SDK calls the API in a test.

## Contribution to the objective
Creates the product itself and its core model. Every later phase hardens or extends it. Strongest use of the learner's TypeScript/API-design background.
