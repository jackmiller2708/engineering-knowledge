---
id: P1-DEF-01
title: "Declarative workflow graph: steps, contracts, validation"
phase: 1
requires: [P0-TYPE-01]
mastery: L5
---

# P1-DEF-01 — Declarative workflow graph: steps, contracts, validation

## Objective
Define a workflow as data: a graph of steps, each with a stable identity and a declared input and output contract. Reject invalid definitions before anything runs.

## Problem
The engine runs, pauses, retries and resumes workflows from saved state. That only works if the workflow is something the engine can read, validate and inspect, rather than code it must re-run from the start. This is the central design decision of PRJ-ENGINE. Getting it wrong shows up in every later phase.

## Prerequisites
`P0-TYPE-01`.

## Techniques
Graph representation (steps and dependency edges), cycle detection, reachability, unique step identity, input/output contracts (declared fields and types), wiring one step's output into another's input, versioning a definition, JSON as the stored form.

## What you need first
A workflow definition has steps; each step has an ID that never changes, the name of the handler that does the work, what it needs (input contract) and what it produces (output contract). A step depends on other steps. The graph must have no cycles, or some step could never start. A saved definition is immutable once instances run against it, so changes make a new version.

## Practical challenge
Design the definition format and a validator. Include at least: unique step IDs, dependencies that point to real steps, no cycles, every input of a step traceable to the workflow input or an upstream step's declared output with a compatible type, and a version number. Write it as plain Go types plus a JSON form. Do not run anything yet. Write five valid and ten invalid definitions as test data.

## Deliverable
A `definition` package in PRJ-ENGINE with the validator, test data, and `project/design/workflow-model.md` stating the format, the rules, and what is deliberately *not* supported (loops, dynamic step creation, code-defined workflows).

## Acceptance criteria
1. Every invalid definition in the test data is rejected with an error that names the step and the rule broken.
2. A cycle of length 1, 2 and 5 is each detected.
3. A step input that references a missing or wrongly typed output is rejected.
4. Definitions round-trip through JSON without changes.
5. `project/design/workflow-model.md` lists at least three things the model cannot express and why that is acceptable for the project.

## Verification
Run the tests. Design defense: the evaluator asks "why not let users write workflows as Go functions?" and "what happens to running instances when a definition changes?". The learner answers with the consequences for retries and recovery. Then the evaluator asks for a small extension (an optional step) and the learner states which rules change.

## Mastery target
L5.

## Next unlocks
- P1-SM-01 — now the engine needs rules for how a run moves through the graph.
- P1-RES-01 — step contracts say what must be saved and shown for each step.
