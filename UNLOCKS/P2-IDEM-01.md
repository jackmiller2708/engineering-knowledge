---
id: P2-IDEM-01
title: Idempotent API requests
phase: 2
requires: [P1-API-03, P1-PG-03]
mastery: L5
---

# P2-IDEM-01 — Idempotent API requests

## Objective
Make "create workflow" safe to retry: the same request sent twice has the effect of one.

## Problem
Networks time out after the server has already acted. Clients retry. Without idempotency, retries start duplicate workflows, and the SDK cannot retry safely.

## Prerequisites
`P1-API-03` (working API), `P1-PG-03` (transactions, unique constraints).

## Techniques
Client-supplied idempotency key, request fingerprint (hash of the body), storing the first response, unique constraint as the arbiter, key scope and expiry, handling an in-flight duplicate.

## What you need first
An operation is idempotent if repeating it leaves the system in the same state as doing it once. The server remembers `(scope, key)` with the request fingerprint and the response. Same key with a different body is a client error. A race between two identical requests must be settled by the database, not by application checks. There is an Internet draft for an `Idempotency-Key` header; check its current status before citing it as a standard.

## Practical challenge
Add idempotency to workflow creation: key from a header, table `idempotency_keys`, same key and body returns the original response; same key different body returns a conflict; a second request while the first is still running behaves as documented (wait or reject).

## Deliverable
Implemented feature in PRJ-ENGINE, TypeScript SDK sending keys with retries, and `project/design/idempotency.md` (rules, key lifetime, failure cases).

## Acceptance criteria
1. 50 concurrent identical requests produce exactly one workflow row and identical responses (test).
2. Same key with a different body returns the documented conflict status, creating nothing.
3. A crash between creating the workflow and storing the response (injected) cannot produce a duplicate on retry; the document explains why.
4. Expired keys are handled as documented.
5. The SDK retry test shows a timeout followed by a retry yields one workflow.

## Verification
Run tests; evaluator reviews the transaction boundary. Oral (L5): "Why not check-then-insert in code?"; "What happens if the response was stored in a separate transaction?"; "How long should keys live and what does that cost?"

## Mastery target
L5.

## Next unlocks
- P2-CONS-01 — the same idea applied to step execution and external effects.
