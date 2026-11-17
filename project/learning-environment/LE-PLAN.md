# Learning Environment Plan

Owner: learner approves; Claude proposes. Status: **proposal**. Source: owner decisions of 2026-11-17 (`DECISION_LOG.md` D-012) and the project brief. Code lives in the application repository; see [README.md](README.md).

## Approved technical direction

| Area | Choice |
|---|---|
| Frontend | Angular + TypeScript |
| Desktop runtime | Tauri 2 |
| Native layer | Rust, for controlled native capabilities only (see LE-004) |
| Simulation and domain logic | Pure TypeScript. It must not depend on Angular, Tauri, or the host OS |
| Persistence | Local-first |
| Structure | Modular monolith |
| Package manager | pnpm |
| Test runner | Vitest, if compatible with current Angular tooling (see Open items) |
| First target | Linux |

## Non-goals

- A universal simulation framework. Build only what the current learning world needs.
- Microservices.
- Application scaffolding before M1 starts.
- Rust, Angular or Tauri learning requirements for the learner (LE-004).

## Milestones

Only M1 is approved. Nothing after it is committed.

| ID | Milestone | Status |
|---|---|---|
| M0 | Repositories and decisions established | Done (documentation and repository setup, no application code) |
| M1 | A minimal desktop application that can create a workspace, persist it, close, and reopen it successfully | Approved, not started |
| Later | Computer Foundations vertical slice: manual binary numbers up to a binary adder built from logic gates | Direction only (Hypothesis) |

M1 acceptance (approved wording): create a workspace, persist it, close the application, reopen it, and find the workspace intact.

## Open items

| Item | Label | Detail |
|---|---|---|
| Tauri system libraries on Linux | Observation (2026-11-17) | `pkg-config` found none of `webkit2gtk-4.1`, `libsoup-3.0`, `javascriptcoregtk-4.1`, `gtk+-3.0`, `librsvg-2.0`, `openssl`. `cargo tauri` was not installed. A desktop build is blocked until they are installed |
| Installed versions | Observation (2026-11-17) | node 24.15.0, pnpm 12.6.0, Angular CLI 22.1.7, rustc 1.100.0 |
| Vitest with the Angular version in use | Unknown | Not checked. Verify against current docs at scaffold time |
| Workspace file format and location | Unknown | Not decided. Decide in M1 |
| Where the domain core lives (own package, or a folder with a boundary rule) | Unknown | Not decided. Decide in M1 |
| Who writes the native layer, and how much Rust it needs | Unknown | Not decided (D-012, Rust boundary item 6) |

## Boundaries

- Concepts and curriculum are referenced from this repository. Do not copy them into the application.
- Product architecture decisions are logged in [LE-DECISIONS.md](LE-DECISIONS.md).
