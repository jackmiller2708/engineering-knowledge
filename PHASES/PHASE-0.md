# Phase 0 — Foundation

**Dates (proposed):** 2026-11-30 → 2027-02-07 (10 weeks, one Tet week removed). **Essential 86 h** of 90 h capacity. Optional pool 43 h.

## Purpose
Give a senior frontend engineer the low-level footing (bytes, memory, files, sockets, cost of operations) and Go fluency needed to build the engine, and start career evidence-gathering.

## Required capabilities
Go toolchain and idiomatic basics; bit and binary manipulation; parsing untrusted byte streams; measuring algorithm cost; file durability; TCP basics; modeling data so illegal states cannot be built; knowing which roles the market asks for.

## Domains and where they are taught
Essential: Go (`P0-GO`), bits and binary (`P0-BIT-01/02/05/06`), cost measurement (`P0-DS-01`), OS and durability (`P0-OS`), TCP (`P0-NET-01`), types (`P0-TYPE-01`), record log (`P0-INT-01`), career (`P0-CAR-01`). Optional: hash tables, trees, heaps, memory model, HTTP parser, flags/packing/library packaging. **Math has no track:** logic, modular arithmetic and probability are taught inside the unlock that needs them.

## Dependencies
None (entry point). Gate to Phase 1: `P0-GO-02`, `P0-GO-03`, `P0-TYPE-01`, `P0-NET-01`. Other P0 unlocks are not gates and may overlap Phase 1 weekends.

## Expected deliverables
PRJ-LABS: hex dump tool, bit and codec packages, framed-record parser, crash-safe record log (`P0-INT-01`), TCP echo server; and the learner's own role map from job postings.

## Exit criteria
- All gate unlocks complete with evidence.
- `P0-INT-01` complete or explicitly deferred by a logged decision (it is cut order 3 in `CURRICULUM.md`).
- `P0-CAR-01` complete: at least 6 direct posting records per direction in `career/POSTINGS.md`, a tally with sample sizes, and interpretations kept separate from observations. A career-priority decision is recorded, or consciously deferred; the snapshot does not force it.
- A written list of foundation unlocks still open, carried as parallel work.

## Contribution to the objective
Record log and codecs prefigure the durable history; type modeling feeds the workflow graph and state machine; TCP knowledge makes the API understandable rather than magic.
