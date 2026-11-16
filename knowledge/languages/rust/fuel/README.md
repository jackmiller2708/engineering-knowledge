# Fuel: a deterministic stack machine

An optional project for exploring Rust. Several afternoons of programming, at your pace, in any order, or never. Nothing here is recorded or expected.

## What you build

A small virtual machine: a stack, a list of instructions, a loop that runs them. You give it a program as text, it runs it and prints what the program printed.

```
push 5
loop:
  dup
  print
  push 1
  sub
  dup
  jz done
  jmp loop
done:
  halt
```

Its rule is the interesting part: **the same program, the same fuel, always the same result.** A program that loops forever stops with an error after exactly the steps you allowed. A program that overflows, underflows or divides by zero returns an error. It never crashes the machine and never gives a different answer on another run or build.

That rule is a reason to meet most of Rust: enums and exhaustive `match`, `Result`, ownership and borrowing, traits, iterators, tests, and threads. Each arrives when the machine needs it. It is also the kind of thing a workflow engine needs from its step runner, but nothing here depends on that.

## The explorations

Each folder is a complete Cargo project plus a `README.md` guide (the table links to each). Each project starts where the previous exploration ends, so you can start at any of them. A guide takes roughly 1 to 3 hours if you experiment properly. Those figures are the author's guess, not a target.

| Folder | You work on | Rust you meet |
|---|---|---|
| [`01-the-machine/`](01-the-machine/README.md) | Instructions as an enum; the run loop | `enum`, `match` exhaustiveness, `struct`/`impl`, `Vec`, `&mut self`, `Copy`, panics |
| [`02-errors-and-fuel/`](02-errors-and-fuel/README.md) | Making the machine total and deterministic | `Result`, `?`, error types, `Display`, checked arithmetic, build profiles |
| [`03-borrowing-the-program/`](03-borrowing-the-program/README.md) | Running one program many times without copying | `&`, lifetimes (`'p`), the borrow checker, `impl Display` |
| [`04-text-to-program/`](04-text-to-program/README.md) | An assembler from text, with labels and tests | `&str` vs `String`, iterators, `collect` into `Result`, `HashMap`, modules, `cargo test` |
| [`05-parallel-runs/`](05-parallel-runs/README.md) | Many programs at once, same output every time | threads, `thread::scope`, `Send`/`Sync`, `Arc`/`Mutex`, deadlocks |

Suggested order is the table order. Skipping is fine. Exploration 5 is the one most worth jumping to if concurrency is what you are curious about.

## How to use a folder

1. Open its `README.md`. It has an objective, a short mental model, and a sequence of experiments.
2. In a terminal, `cd` into the folder and run `cargo run`. The `cargo` commands are the same in Zsh and PowerShell 7; see "what was actually verified" below.
3. Edit `src/main.rs`, run again, and read what the compiler says. Reading compiler errors is part of the exercise. The guides quote what the author observed, so you can compare.
4. When you want to see one possible answer, the next folder holds the finished version of the previous exploration.

Nothing breaks permanently. Once these files are committed, `git restore knowledge/languages/rust/fuel/<folder>` puts a folder back as it was. If you want to keep your own version, copy the folder somewhere outside the repository first, and experiment freely.

## Tools, and what was actually verified

You need Rust with `cargo`; install steps are in [the Rust start page](../README.md). The projects have no dependencies, so nothing is downloaded after Rust itself.

| | |
|---|---|
| Verified toolchain | `rustc 1.97.0 (2d8144b78 2026-07-07)`, `cargo 1.97.0 (c980f4866 2026-06-30)` |
| Verified platform | Linux x86_64, Zsh 5.9, a 4-core container |
| Verified how | every project built (no warnings) and run, every experiment applied and its quoted output observed, `cargo test` in exploration 5 (9 tests), and a clean clone built with `--locked` |
| Edition | 2021 |
| **Not verified** | Windows and PowerShell 7 (the `cargo` commands are the same, but nobody has run them there; PowerShell variants in the guides are marked untested), macOS, any other Rust version |

Compiler messages differ between Rust versions. If yours differ in wording from the quoted ones, that is expected. If an experiment does not do what the guide says, that is worth a closer look.

**`Cargo.lock` is committed** in each project. These are programs, not libraries, so the lockfile is how a build is reproduced. With no dependencies it contains only the project itself, and it was written by Cargo 1.97.0, so an older Cargo may not read it (not tested). Build with `cargo build --locked` if you want Cargo to refuse to change it. The day you add a dependency, commit the new `Cargo.lock` with it. `target/` is never committed.

## Pause and resume

Nothing here keeps score, so there is nothing to catch up on. Your edits stay in the folder you changed. After a break, open that exploration's guide, read "What to take away" for the recap, run `cargo run`, and carry on or skip ahead. Each exploration starts from a working project, so you never need an earlier one finished.

## When you want the concept, not the Rust

The guides explain how Rust realizes an idea, not the idea itself. For the language-independent version (ownership and aliasing in general, determinism, integer overflow, concurrency hazards), ask for a concept document. It would live in `knowledge/<domain>/`, and the Rust page would link to it. None exist yet.

## Where you could take it next

Not a list of tasks. Ideas that fall out of the project when you feel like it:

- A `Step` iterator: one call per instruction, so you can single-step and inspect.
- A tracing hook as a generic parameter, then as `dyn Trait`. Measure the difference with the speed test from exploration 2.
- `call` and `ret` with a second stack; recursion; a stack-depth limit as a second kind of budget.
- A memory region and `load`/`store`, with bounds errors as values.
- Property tests: random programs must never panic the machine. Whatever happens, `run` returns.
- A compact binary encoding of programs, and a decoder that treats its input as untrusted.
- Compare the same machine written in TypeScript or Go, but only if the comparison interests you.
- Async: only if you find a problem here that needs it. This project does not.
