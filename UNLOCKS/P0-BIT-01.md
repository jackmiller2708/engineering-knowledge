---
id: P0-BIT-01
title: Manipulate individual bits
phase: 0
requires: [P0-GO-01]
mastery: L3
---

# P0-BIT-01 — Manipulate individual bits

## Objective
Read, set, clear and toggle a single bit of an integer, and count set bits.

## Problem
Binary formats, permission flags and compact state all need single-bit control. Without it, `P0-BIT-02` masks make no sense.

## Prerequisites
`P0-GO-01`.

## Techniques
Binary and hexadecimal notation; `&`, `|`, `^`, `&^`, `<<`, `>>`; unsigned vs signed integers; `math/bits` (as a reference to check against, after writing your own).

## What you need first
A `uint64` is 64 positions, numbered 0 (least significant) to 63. `1 << n` makes a number with only bit n set. Shifts on unsigned integers fill with zeros.

## Practical challenge
In PRJ-LABS write `GetBit`, `SetBit`, `ClearBit`, `ToggleBit` and `PopCount` for `uint64`. Decide and document what happens for index ≥ 64. Then run the same ideas in TypeScript and explain the result of `1 << 31` and `1 << 32` there.

## Deliverable
A `bits` package with tests, plus a short note `EVIDENCE/P0-BIT-01/ts-bitwise.md` (written with `TEMPLATES/EXPERIMENT.md`) recording the TypeScript observations and their cause.

## Acceptance criteria
1. Table tests cover bit 0, bit 63, already-set and already-clear cases.
2. `PopCount` equals `math/bits.OnesCount64` for 10,000 random values (test).
3. Out-of-range behavior is chosen, documented, and tested.
4. The TypeScript note states observed values and the 32-bit signed conversion that explains them.

## Verification
Run tests. Ask: "Why does `1 << 63` need an unsigned type here?" and "What does `x & (x-1)` do?" (learner predicts, then verifies by experiment).

## Mastery target
L3.

## Next unlocks
- P0-BIT-02 — single bits are too small; real data uses groups of bits (fields).
