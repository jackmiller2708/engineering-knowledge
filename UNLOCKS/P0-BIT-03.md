---
id: P0-BIT-03
title: Represent permissions as flags
phase: 0
requires: [P0-BIT-02]
mastery: L3
---

# P0-BIT-03 — Represent permissions as flags

> Optional (not part of the essential plan). Take it when ahead of schedule.

## Objective
Model a set of permissions as one integer with safe set operations.

## Problem
The platform needs compact, comparable sets (for example what a caller may do). Flags show both the power and the limits of bit sets.

## Prerequisites
`P0-BIT-02`.
Uses: bit masks from the `bits` package (P0-BIT-02).

## Techniques
Typed constants with `iota`, `Has/Grant/Revoke`, union/intersection/difference, `String()` for readable output, validation of unknown bits.

## What you need first
Each permission owns one bit. Union is OR, intersection is AND, difference is AND-NOT. A set of N flags needs N bits.

## Practical challenge
Define a `Permission` type with at least 6 flags and a `PermissionSet` type. Provide set operations, a `String()` that lists names, and parsing from a list of names. Reject sets containing bits that are not defined flags.

## Deliverable
A `perm` package with tests, and a short design note: what breaks when you need more than 64 permissions, or when flags are added later and stored data already exists.

## Acceptance criteria
1. Set-law tests: union/intersection commutative; `A &^ A` empty; `Grant` then `Revoke` restores the original.
2. Unknown bits are rejected on parse and on construction from raw integers.
3. `String()` is stable and round-trips through parsing.
4. The design note names at least two failure modes (flag limit; changing meaning of a bit in stored data) and one alternative representation.

## Verification
Tests plus oral check: "Is it safe to reorder constants?" (No: stored integers would change meaning.)

## Mastery target
L3.

## Next unlocks
- P0-BIT-07 — optional: flags become part of the reusable library.
