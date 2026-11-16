---
id: P0-BIT-06
title: Parse a framed binary protocol safely
phase: 0
requires: [P0-BIT-05]
mastery: L4
---

# P0-BIT-06 — Parse a framed binary protocol safely

## Objective
Read frames from a byte stream that may arrive in arbitrary pieces and may be damaged.

## Problem
Network connections and files deliver bytes, not messages. A parser that trusts input lengths can crash or exhaust memory. The same parser design later reads the record log and HTTP.

## Prerequisites
`P0-BIT-05`.

## Techniques
Frame layout (magic, version, type, length, payload, checksum), streaming reads with `io.Reader`, maximum frame size, CRC-32 checksums (`hash/crc32`), error types for each failure.

## What you need first
A frame has a header with the payload length. The reader must wait for all bytes, reject lengths above a limit *before* allocating, and verify the checksum. A CRC detects accidental corruption; it does not stop deliberate tampering.

## Practical challenge
Define a frame format, write an encoder and a streaming decoder. Test the decoder when the input is delivered one byte at a time, when a frame is truncated, when the checksum is wrong, when the length is huge, and when the version is unknown.

## Deliverable
A `frame` package with spec document (`project/design/frame-format.md`), tests, and fuzz test.

## Acceptance criteria
1. Frames round-trip regardless of how the stream is chunked (test with 1-byte and random chunk sizes).
2. Each malformed case returns a distinct, typed error.
3. A header declaring a 4 GB payload is rejected without allocating it (test or memory check).
4. Fuzz test runs 60 seconds with no panic.
5. Written spec lets another person implement a compatible decoder.

## Verification
Run tests and fuzz. Evaluator feeds a corrupted file produced by the learner's own encoder with one flipped bit and checks the error. Oral: "What does the CRC not protect against?"

## Mastery target
L4.

## Next unlocks
- P0-INT-01 — the frame format is what the crash-safe record log writes and reads back.
- P0-BIT-07 — optional: consolidate into a reusable library.
- P0-NET-02 — the same stream-parsing discipline applies to HTTP text parsing.
- PX-RUST-01 — optional: compare the same codec in Rust.
