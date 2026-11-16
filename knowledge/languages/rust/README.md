# Rust (leisure track)

Owner: learner. This is the starting page for Rust. It is not an unlock, a phase or a course.

## Start here

1. **Install** (once; skip if `cargo --version` already prints a version). Follow the official instructions: https://doc.rust-lang.org/book/ch01-01-installation.html. The page says you also need a linker, usually from a C compiler. Nothing else is needed. Verified toolchain and platform: `rustc`/`cargo` 1.97.0 on Linux. Windows/PowerShell 7 and other versions: not verified. Details: [`ENVIRONMENT.md`](../../../ENVIRONMENT.md) and [`fuel/README.md`](fuel/README.md).
2. **Begin** with the project in [`fuel/`](fuel/README.md): a deterministic stack machine you run, break and extend over several afternoons, in five explorations. Each exploration is a runnable Cargo project plus a guide, and each starts where the previous one ends, so any of them is a fine starting point. If you want something much smaller first, [`first-exploration.md`](first-exploration.md) is a 30 to 45 minute warm-up on ownership.
3. **Run experiments** by `cd`-ing into an exploration folder and running `cargo run`; edit `src/main.rs` and run again. For your own scratch ideas, use a folder outside this repository (`cargo new <name>`).
4. **Understand a concept more deeply:** the official Rust Book is the reference (https://doc.rust-lang.org/book/). For ideas that are not specific to Rust, ask for a concept document in `knowledge/<domain>/`.
5. **Get help:** ask in a session, for example "explain borrowing with a small example". Claude helps fully when you ask and never brings Rust up on its own.

## What this is

A self-directed, curiosity-driven track that runs beside the course. The learner opens it when they feel like it.

- No hours, deadlines, order, progress reports, credentials or mastery targets.
- It does not appear in `LEARNER_STATE.md`, and nothing here counts toward any phase, checkpoint or budget.
- Core completion never depends on it. It never delays or replaces a core unlock.
- Claude does not schedule it, prompt for it or ask how it is going. Claude helps when the learner asks.

## Pause and resume

Stopping costs nothing and leaves no backlog. There is nothing to catch up on. To resume, the learner says what they are curious about now. Claude starts from there, not from "where we left off".

## How help works

- Start with a small program the learner runs, such as one of the `fuel/` projects. Explain only what that program needs.
- Language-independent concepts (memory, ownership as a general idea, concurrency, error handling, API design) have one canonical home in `knowledge/<domain>/`, written only when asked (`knowledge/README.md`). Rust help links there and explains only how Rust realizes the concept.
- Compare with TypeScript or Go only when the comparison teaches something. Do not translate Go exercises line by line.
- Be exact about guarantees (next section). Check any further claim against the official Rust documentation and say when it is unverified.
- Rust source lives only in the projects under this folder (`CLAUDE.md` section 4, D-010). Scratch experiments belong outside the repository.

## Guarantees, stated precisely

Status: **fact**, checked against the sources below on 2026-11-16. The docs track the current stable release; the Rust version was not recorded.

- **Data races.** Safe Rust guarantees the absence of data races: two or more threads concurrently accessing a memory location, at least one writing, at least one unsynchronized. A data race is undefined behavior (UB) and cannot be performed in safe Rust. Ownership does most of the work (a mutable reference cannot be aliased); `Send` and `Sync` cover interior mutability. [1] [2]
- **General race conditions are not prevented.** A data race is one kind of race. Rust does not prevent general race conditions (a result that depends on thread timing). The Nomicon calls this impossible when you do not control the scheduler. [1]
- **Deadlocks and logic errors are not prevented.** The Nomicon says it is "safe" for a program to deadlock or do something nonsensical with incorrect synchronization. The Reference lists deadlocks and logic errors as behavior not considered unsafe. The Book says `Mutex<T>` carries the risk of deadlocks. A race condition on its own cannot violate memory safety. Combined with other `unsafe` code, it can. [1] [3] [5]
- **Leaks are allowed.** Preventing memory leaks is not a Rust guarantee, so leaks are memory safe. `Rc<T>` reference cycles can leak. `mem::forget` is safe because Rust's guarantees do not include running destructors. [4] [5] [6]
- **`unsafe` does not suspend the rules.** Code in `unsafe` blocks and functions must still never cause UB. `unsafe` means the programmer, not the compiler, must ensure that. Unsafe code is sound if no safe client can trigger UB through it, and unsound if one can. [2]
- **Not claimed here.** Which operations need `unsafe`, and what each one requires, are not covered. Read the Reference and the Rustonomicon before writing `unsafe`; the Reference says its UB list is not exhaustive. [2]

Sources (official; the cited passages were read on 2026-11-16, not whole pages):

1. The Rustonomicon, "Data Races and Race Conditions" (page title "Races"): https://doc.rust-lang.org/nomicon/races.html
2. The Rust Reference, "Behavior considered undefined": https://doc.rust-lang.org/reference/behavior-considered-undefined.html
3. The Rust Programming Language, "Shared-State Concurrency": https://doc.rust-lang.org/book/ch16-03-shared-state.html
4. Standard library, `std::mem::forget` (section Safety): https://doc.rust-lang.org/std/mem/fn.forget.html
5. The Rust Reference, "Behavior not considered unsafe": https://doc.rust-lang.org/reference/behavior-not-considered-unsafe.html
6. The Rust Programming Language, "Reference Cycles Can Leak Memory": https://doc.rust-lang.org/book/ch15-06-reference-cycles.html

## Directions (not a checklist)

Take any, in any order, or none. Nothing is "next".

- A small program and Cargo (`first-exploration.md`, `fuel/01-the-machine/`).
- Ownership, seen through `String` (`first-exploration.md`).
- Moves, borrowing, shared and mutable references (`fuel/03-borrowing-the-program/`).
- Lifetimes, once an example needs them (`fuel/03-borrowing-the-program/`).
- Enums, pattern matching, structs, traits, generics, error handling (`fuel/01-the-machine/`, `fuel/02-errors-and-fuel/`, `fuel/04-text-to-program/`).
- Concurrency and systems programming, after the foundations (`fuel/05-parallel-runs/`).
- Async, only if a concrete problem calls for it. Nothing in `fuel/` needs it.
- Generics and traits beyond `Display`, closures, modules, `unsafe`: not covered yet. Ask, or extend the project.

## What success looks like

Capabilities, not completion. The learner can read and write ordinary Rust, explain ownership, use the type system and error handling, and see how Rust's design shapes an API. The learner decides when that is enough.

## Optional integration exercise

`PX-RUST-01` (re-implement the frame codec and compare) is an optional exercise for later, once the learner has finished `P0-BIT-06` and has some Rust. It is not a starting point and not the whole of Rust learning. Its catalog entry is unchanged. Its hours in `UNLOCKS/CATALOG.md` are a rough size reference, not time set aside for Rust.
