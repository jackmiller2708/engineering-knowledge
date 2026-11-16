# Project Area

Owner: learner approves changes. This directory is the course's *Engineering Projects* boundary (`KNOWLEDGE_STANDARD_ADDENDUM.md`). It holds project plans, architecture decisions and design documents. It does **not** hold the platform's source code, and nothing here depends on any other repository.

| File | Contents |
|---|---|
| `PLAN.md` | The workflow platform: scope, execution model, capability proof, milestones |
| `DECISIONS.md` | Architecture decision log for the platform |
| `design/` | Design documents the learner writes as unlocks complete (created on first use) |

## Project areas

Logical projects used by the unlocks. A project area is a named piece of work; it is not a repository.

| ID | Purpose | Produced by | Notes |
|---|---|---|---|
| PRJ-LABS | Foundations: hex dump tool, bit and codec packages, record log, TCP experiments | `P0-*` unlocks | Standalone. Parts may be reused in PRJ-ENGINE |
| PRJ-ENGINE | The workflow platform | `P1-` to `P6-` unlocks | See `PLAN.md` |
| PRJ-REPLAY-LAB | Optional: deterministic replay on a toy workflow (`PX-REPLAY-01`) | optional | Isolated. Must not change PRJ-ENGINE's schema, API or completion criteria. Not in the essential plan |

## Workspace (where working code lives)

The learner keeps working code in a workspace of their choosing. It is not assumed to be a Git repository and its location is never written in this repository (no machine paths). The learner describes it at the start of the first unlock that needs code (`P0-GO-01`). If the work later benefits from version control or sharing in a separate repository, that is an optional future decision, never a dependency.

## Implementation attempts

The learner's workspace can hold more than one attempt at implementing a project area. This table records the attempts; it never records machine paths. How a new attempt starts: `PROCEDURES.md`.

| Attempt | Project area | Description of the workspace area | Started | Status |
|---|---|---|---|---|
| 1 | PRJ-LABS, PRJ-ENGINE | to be described by the learner at the start of `P0-GO-01` | not started | planned |

## Keeping the course portable without the workspace

A fresh session with only this repository must be able to say exactly what was proven. Each completed unlock therefore has an **evidence bundle** at `EVIDENCE/<ID>/<YYYY-MM-DD>-<n>/` with `evaluation.md`, `manifest.md` and `artifacts/`. Structure, required fields and the two evidence kinds (`preserved`, `independently-reproduced`) are in `PROCEDURES.md` ("Recording evidence") and `TEMPLATES/MANIFEST.md`.

A bundle holds only the files needed to reproduce one verification, plus `provenance` pointing to the workspace. It never holds a whole workspace, dependency folders or build output. Design documents are stored here directly in `project/design/`.

If the work outgrows bundles, propose where the code should live. Do not assume an answer.

## If the workspace is unavailable

Continue with theory and isolated experiments. Do not mark an unlock complete without a bundle whose manifest lets the acceptance criteria be re-checked.
