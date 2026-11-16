---
id: P0-BIT-02
title: Build and apply bit masks
phase: 0
requires: [P0-BIT-01]
mastery: L3
---

# P0-BIT-02 — Build and apply bit masks

## Objective
Extract and replace multi-bit fields inside an integer without disturbing other bits.

## Problem
Data packed into integers (flags, headers, hashes) is made of fields several bits wide. Masks are how you reach one field safely.

## Prerequisites
`P0-BIT-01`.

## Techniques
Mask construction `(1<<width)-1`, shift-then-mask extract, clear-then-or insert, overflow checking.

## What you need first
A mask has 1s where you want to keep or change bits. Extract = shift the field down, then AND with the mask. Insert = clear the field's bits, then OR in the new value shifted up.

## Practical challenge
Add `Mask(width)`, `Extract(v, lo, width)` and `Insert(v, lo, width, field)` to the `bits` package. `Insert` must reject a field value that does not fit in `width` bits.

## Deliverable
Extended `bits` package with unit tests and a Go fuzz test.

## Acceptance criteria
1. Property (fuzz or randomized test): `Extract(Insert(v, lo, w, f), lo, w) == f` for all valid inputs.
2. Property: bits outside the field are unchanged by `Insert`.
3. Width 0 and width 64 behave as documented; invalid ranges return an error, not a wrong answer.
4. `go test -fuzz` runs at least 30 seconds without failures.

## Verification
Run tests and fuzz. Ask the learner to predict the result of an insert with an oversized value, then show it is rejected.

## Mastery target
L3.

## Next unlocks
- P0-BIT-05 — fields are the base of byte-level encodings.
- P0-BIT-03 — optional: a first real use, permission flags.
- P0-BIT-04 — optional: fields assembled into a structured record.
- P0-DS-02 — hash functions rely on mixing and masking bits.
