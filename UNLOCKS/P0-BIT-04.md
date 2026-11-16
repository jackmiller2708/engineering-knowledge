---
id: P0-BIT-04
title: Pack structured data into bits
phase: 0
requires: [P0-BIT-02]
mastery: L3
---

# P0-BIT-04 — Pack structured data into bits

> Optional (not part of the essential plan). Take it when ahead of schedule.

## Objective
Pack several small fields into one 64-bit value from a declared layout.

## Problem
Compact records (headers, state words) need a defined layout and safe overflow behavior, otherwise corruption goes unnoticed.

## Prerequisites
`P0-BIT-02`.
Uses: `Extract` and `Insert` from the `bits` package (P0-BIT-02).

## Techniques
Layout tables (name, offset, width), packing/unpacking driven by the layout, overlap and overflow detection.

## What you need first
Fields must not overlap and must fit the total width. The layout is a contract: change it and old data is read wrongly.

## Practical challenge
Define a layout for a step header: kind (4 bits), state (3), attempt (6), flags (8), payload length (16). Write `Pack` and `Unpack` driven by a layout value, and a validator that rejects overlapping or oversized layouts.

## Deliverable
A `pack` package with tests and a layout validator.

## Acceptance criteria
1. Round trip for every field at minimum, maximum, and random values.
2. A value one above a field's maximum is rejected.
3. The validator rejects overlapping fields and total width above 64.
4. A second, different layout works without changing `Pack`/`Unpack` code.

## Verification
Tests; the learner explains why changing a field's width is a breaking change for stored data.

## Mastery target
L3.

## Next unlocks
- P0-BIT-07 — optional: the packing helpers join the reusable library.
