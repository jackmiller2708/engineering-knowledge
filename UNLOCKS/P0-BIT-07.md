---
id: P0-BIT-07
title: Package the codecs as a reusable library
phase: 0
requires: [P0-BIT-03, P0-BIT-04, P0-BIT-06]
mastery: L3
---

# P0-BIT-07 — Package the codecs as a reusable library

> Optional (not part of the essential plan). Take it when ahead of schedule.

## Objective
Turn the bit, permission, pack, codec and frame packages into one coherent, documented library.

## Problem
Components that only work in the folder where they were written get rewritten later. This unlock practices API design: naming, errors, documentation, versioning.

## Prerequisites
`P0-BIT-03`, `P0-BIT-04`, `P0-BIT-06`.
Uses: `bits` (P0-BIT-02), `perm` (P0-BIT-03), `pack` (P0-BIT-04), `codec` (P0-BIT-05), `frame` (P0-BIT-06).

## Techniques
Package boundaries, exported API review, Go doc comments and examples, semantic version tags, README usage.

## What you need first
Exported names are a promise to callers. Fewer, clearer exports are easier to keep. Examples in documentation can be run as tests.

## Practical challenge
Review the public API of all five packages for consistency (error style, naming, argument order). Fix inconsistencies, add examples, write a README, and record version `v0.1.0` in a changelog.

## Deliverable
The PRJ-LABS library at version `v0.1.0` (changelog entry), API review notes listing each change and why, saved as an evidence bundle.

## Acceptance criteria
1. `go test ./...` and `go vet ./...` pass from a clean copy of the bundle at `v0.1.0`.
2. Every exported identifier has a doc comment; each package has at least one runnable `Example` test.
3. Errors follow one documented convention.
4. A scratch module in a separate directory imports the library (local `replace` directive) and runs a round trip.

## Verification
Evaluator runs the commands and the scratch module from the bundle. Oral: name one API decision and its trade-off.

## Mastery target
L3.

## Next unlocks
Optional. Nothing else depends on it.
