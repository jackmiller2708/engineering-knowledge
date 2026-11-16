---
id: P0-BIT-05
title: Encode and decode binary formats (endianness, varints)
phase: 0
requires: [P0-BIT-02]
mastery: L4
---

# P0-BIT-05 — Encode and decode binary formats

## Objective
Write bytes to and read bytes from a buffer with correct byte order and variable-length integers.

## Problem
Two programs exchanging bytes must agree on order and length. Variable-length integers save space but add parsing risk (truncation, overlong encodings).

## Prerequisites
`P0-BIT-02`.
Uses: masks and shifts from the `bits` package (P0-BIT-02).

## Techniques
Big vs little endian, unsigned varint (7 bits per byte, high bit = "more bytes follow"), zigzag mapping for signed numbers, bounds checks.

## What you need first
Endianness is the order of bytes of a multi-byte number in memory or on the wire. A varint stores 7 data bits per byte, least significant group first. Zigzag maps small negative numbers to small unsigned ones.

## Practical challenge
Implement `PutUint16/32/64` in both byte orders, `PutUvarint`/`Uvarint`, and zigzag `PutVarint`/`Varint`. Return errors for truncated or too-long input. Write your own first; only then compare with `encoding/binary`.

## Deliverable
A `codec` package with tests, fuzz test, and a one-page note on failure modes (truncation, overlong, integer overflow on decode).

## Acceptance criteria
1. Round trip for boundary values (0, 1, 127, 128, 2^32, max uint64; signed: min, max, -1).
2. Output bytes equal `encoding/binary` for all tested values.
3. Truncated input and an 11-byte continuation chain return errors, never panic.
4. Fuzz test: decode of arbitrary bytes never panics and never reads out of range.

## Verification
Tests and fuzz run; learner hand-encodes 300 as a varint on paper and checks it with the tool; explains why the decoder must bound the number of bytes.

## Mastery target
L4 (analyze failure modes).

## Next unlocks
- P0-BIT-06 — individual values are combined into framed messages on a byte stream.
