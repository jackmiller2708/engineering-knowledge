# Learning Environment Decision Log

Owner: learner approves; Claude proposes. Append-only. Product and architecture decisions for the Engineering Learning Environment only. Curriculum and repository-wide decisions: [`DECISION_LOG.md`](../../DECISION_LOG.md). Platform decisions for the Go/PostgreSQL project: [`../DECISIONS.md`](../DECISIONS.md) (PD-nnn, unchanged). The workspace decision log, outside this repository, records placement as WD-005.

Source for all entries: owner decisions, 2026-11-17.

## LE-001 — Technical direction

- **Status:** Decided by the learner.
- **Decision:**
  - Angular + TypeScript frontend.
  - Tauri 2 desktop runtime with a Rust native layer.
  - Pure TypeScript simulation and domain logic. It does not depend on Angular, Tauri, or the host OS.
  - Local-first persistence.
  - Modular monolith.
  - pnpm.
  - Vitest, subject to compatibility with current Angular tooling.
  - Linux is the initial development target.
- **Why:** Simulation and learning logic must stay testable and portable. The host provides only controlled native capabilities.
- **Consequence:** Something must enforce the boundary between domain and host code. How is open (see [LE-PLAN.md](LE-PLAN.md)).
- **Not included:** No universal simulation framework. No microservices.

## LE-002 — Separate application repository

- **Status:** Decided by the learner.
- **Decision:** The application is an independent Git repository, nested inside the `engineering-projects` repository of the workspace at `projects/engineering-learning-environment`. It has no remote and is not a submodule.
- **Ownership:**

  | Owner | Owns |
  |---|---|
  | This repository | Concepts, curriculum, plans, product architecture |
  | Application repository | Code, tests, implementation docs |

- **Relation to D-004:** D-004 stays as written. `DECISION_LOG.md` D-012 records how this narrows D-004 for this product.
- **Consequence:** The application references this content. It does not copy it. It is not needed to read or maintain the curriculum.
- **See also:** workspace decision WD-005, "Engineering Learning Environment is an independent repository under engineering-projects" (workspace decision log, outside this repository).

## LE-003 — First milestone

- **Status:** Decided by the learner.
- **Decision:** M1 is a minimal desktop application that can create a workspace, persist it, close, and reopen it successfully.
- **Consequence:** No learning content is built before this works.

## LE-004 — Rust boundary

- **Status:** Decided by the learner (2026-11-17). Recorded in `DECISION_LOG.md` D-012.
- **Decision:**
  1. Rust is an implementation technology used by the application: its native implementation technology (the Tauri 2 native layer).
  2. Rust proficiency is not required to follow the core curriculum or to use the application.
  3. The optional Rust leisure track (`DECISION_LOG.md` D-009 to D-011) remains independent of the Learning Environment. Application work does not schedule, replace or count toward it.
  4. Application development creates no learner mastery requirements, unlocks, hours, deadlines or progression gates.
  5. The application implementation and the learner's Rust education are separate concerns. Rust as the application's technology and Rust as an optional subject a learner may explore on their own are different things.
- **Why:** D-009 to D-011 describe a leisure track with no obligations. The application makes Rust a product dependency. Without this entry the two could be read as conflicting. They govern different things (Interpretation).
- **Unknown:** Who writes the native layer, and how much Rust it needs. Not decided here.
- **Not changed:** D-009, D-010, D-011.
