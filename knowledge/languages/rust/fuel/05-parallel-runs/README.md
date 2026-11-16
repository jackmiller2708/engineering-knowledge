# 5. Parallel runs

**Objective.** Run many programs at the same time and get output identical to running them one after another. Then find out what the compiler guarantees about threads, and what it does not. You meet `thread::scope`, `Send` and `Sync`, `Arc` and `Mutex`, and two classic concurrency bugs that safe Rust still allows.

Optional, about 2 to 3 hours. Back after a break? Read "What to take away" at the end for the recap. This folder is the finished project: exploration 4's assembler plus a threaded runner. Unlike the earlier explorations, the code is already written. You read it, run it, break it and measure it.

## Run it

```
cd knowledge/languages/rust/fuel/05-parallel-runs
cargo test
cargo run -- seq programs/countdown.fuel
cargo run -- par programs/countdown.fuel programs/factorial.fuel
```

`seq` runs jobs one after another, `par` runs each on its own thread, `list` prints instructions. `--fuel=N` sets the budget (default 10,000). A one-line timing summary goes to stderr, so it never mixes with the program output.

Observed: `cargo test` reports `9 passed`, `seq` and `par` print the same text.

## Mental model: what a thread changes

A thread is an independent line of execution with its own stack, sharing the process's memory. The danger is shared memory. If two threads touch the same location, at least one writes, and nothing orders them, that is a **data race**. In many languages that is a bug the language cannot rule out. Rust's promise is specific: **safe Rust cannot contain a data race** (see "Guarantees" in `../../README.md`, sources 1 and 2). It is done with types, not a runtime:

- **`Send`**: a value of this type may be moved to another thread. `Rc` (non-atomic reference counting) is not `Send`. `Arc` (atomic) is.
- **`Sync`**: a type is `Sync` if `&T` is `Send`: sharing references across threads is safe. The standard library documents these definitions at https://doc.rust-lang.org/std/marker/trait.Sync.html.
- The compiler works these out automatically for your types. A closure given to a thread must be `Send`, and anything it captures too.
- **`thread::spawn`** requires the closure to be `'static` (own all its data), because the thread might outlive the function. **`thread::scope`** guarantees every thread is joined before it returns, so scoped threads *may borrow* local data (https://doc.rust-lang.org/std/thread/fn.scope.html).

That second point is why this project can share one program between threads with no copying: exploration 3's `&[Op]` borrow, now across threads. Many shared borrows are fine, and nothing mutates the program.

## Read the code

Open `src/main.rs` and find `run_parallel`:

```rust
fn run_parallel(jobs: &[(String, Vec<Op>)], fuel: u64) -> Vec<Report> {
    thread::scope(|scope| {
        let handles: Vec<_> = jobs
            .iter()
            .map(|(name, program)| scope.spawn(move || run_job(name, program, fuel)))
            .collect();
        handles.into_iter().map(|h| h.join().unwrap()).collect()
    })
}
```

- Each thread borrows `name` and `program` from `jobs` and receives a copy of `fuel`.
- Each thread returns a `Report` that owns its data. Results cross the thread boundary by move, not by sharing.
- Results are collected by joining handles *in the order they were spawned*. That, not luck, is why output order matches `seq`.
- Nothing here is locked. Threads share only read-only data. The design avoids shared mutable state instead of guarding it.

Why does this give exactly the sequential answer? Each `run_job` is a deterministic function of its inputs (exploration 2). Threads cannot affect each other. Order is imposed when collecting. Together those make the parallel run equal to the sequential one. If any of the three were missing, it would not be.

## Two kinds of determinism

The project's rule is "same program, same fuel, same result". With threads, that sentence hides two different claims:

1. **Deterministic execution.** One run of the machine is a function of its inputs. Nothing inside `Vm::run` depends on time, memory addresses, thread identity or luck. This is a property of the machine's code, and you built it in exploration 2.
2. **Deterministic concurrent behavior.** What the threads do relative to each other: which starts first, which finishes first, how their steps interleave. The operating system's scheduler decides that. Your program does not, Rust does not, and it differs from run to run. **This project is not deterministic in that sense, and no safe-Rust feature makes it so.**

What the project does have is a deterministic **outcome** despite a nondeterministic **schedule**. It comes from three design choices, not from the language: jobs share nothing mutable, each job is a deterministic function, and results are collected in a fixed order. Take any one away and the outcome can depend on the schedule. Experiment H shows the schedule varying under an outcome that does not.

Keep the two apart when you read about "deterministic" systems. Replaying a recorded schedule, or removing scheduling decisions from the design (one thread, or independent jobs as here), are different techniques with different costs.

## Experiments

### A. Use `spawn` instead of `scope`

Replace `scope` with plain `thread::spawn`, no scope, collecting the handles directly. Observed:

```
error[E0521]: borrowed data escapes outside of function
  `jobs` is a reference that is only valid in the function body
  argument requires that `'1` must outlive `'static`
```

The compiler will not let a thread that could outlive the function hold a borrow of its argument. Fixes: `thread::scope` (what the code does), or give each thread owned data (clone the programs, or share them as `Arc<[Op]>`). Try the `Arc` version. What did it cost?

### B. Share a counter with the wrong type

Count started jobs with an `Rc<Cell<u64>>` cloned into each thread. Observed:

```
error[E0277]: `Rc<Cell<u64>>` cannot be sent between threads safely
  the trait `Send` is not implemented for `Rc<Cell<u64>>`
```

`Rc` updates its reference count without atomic operations. Two threads cloning it at once could corrupt the count. The standard library documentation says this would be undefined behavior (https://doc.rust-lang.org/std/marker/trait.Send.html). Replace it with `Arc<AtomicU64>` and `fetch_add(1, Ordering::Relaxed)`, or `Arc<Mutex<u64>>`. Then think about whether this counter belongs in a machine that promises determinism. (The total is deterministic. The order in which threads increment it is not. Nothing reads the order.)

### C. Check the determinism claim yourself

```
cargo run --quiet -- seq programs/arithmetic.fuel programs/countdown.fuel programs/factorial.fuel programs/forever.fuel programs/overflow.fuel > seq.txt 2>/dev/null
cargo run --quiet -- par programs/arithmetic.fuel programs/countdown.fuel programs/factorial.fuel programs/forever.fuel programs/overflow.fuel > par.txt 2>/dev/null
diff seq.txt par.txt
```

On PowerShell (untested), drop `2>/dev/null` and use `Compare-Object (Get-Content seq.txt) (Get-Content par.txt)`. Observed: identical, and identical across eight further `par` runs. That is evidence about this program on one machine, not a proof. What kind of change would break it? (Printing from inside `run_job`. Collecting handles in completion order. Letting jobs share a mutable counter that jobs read.)

### D. Where the compiler says nothing: a lost update

Make a scratch project outside the repository (`cargo new race-play`) and paste this into its `src/main.rs`:

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0u32));
    let handles: Vec<_> = (0..4)
        .map(|_| {
            let counter = Arc::clone(&counter);
            thread::spawn(move || {
                for _ in 0..100_000 {
                    let current = *counter.lock().unwrap(); // lock, read, unlock
                    *counter.lock().unwrap() = current + 1; // lock, write, unlock
                }
            })
        })
        .collect();
    for h in handles {
        h.join().unwrap();
    }
    println!("expected 400000, got {}", *counter.lock().unwrap());
}
```

Run it with `cargo run --release`. It compiles without a warning. Observed in three runs: `196163`, `176998`, `175449`. Every access is locked, so there is **no data race**. But the program reads, releases the lock, and writes later, so two threads can read the same value and one increment is lost. That is a **race condition**: the result depends on timing. Rust does not prevent those. Its documentation says so (https://doc.rust-lang.org/nomicon/races.html, which calls this a "general race condition").

Fix it by taking the lock once: `*counter.lock().unwrap() += 1;`. Observed: `400000`. The compiler could not tell you which version was right because only you know the invariant: the read and the write must be one step.

### E. Where the compiler says nothing: a deadlock

Replace `main` in the scratch project with two threads that take two locks in opposite order:

```rust
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

fn main() {
    let a = Arc::new(Mutex::new(0));
    let b = Arc::new(Mutex::new(0));

    let (a1, b1) = (Arc::clone(&a), Arc::clone(&b));
    let t1 = thread::spawn(move || {
        let _first = a1.lock().unwrap();
        thread::sleep(Duration::from_millis(100));
        let _second = b1.lock().unwrap(); // waits for t2 to release b
    });

    let (a2, b2) = (Arc::clone(&a), Arc::clone(&b));
    let t2 = thread::spawn(move || {
        let _first = b2.lock().unwrap();
        thread::sleep(Duration::from_millis(100));
        let _second = a2.lock().unwrap(); // waits for t1 to release a
    });

    t1.join().unwrap();
    t2.join().unwrap();
    println!("never printed");
}
```

It compiles. Run it in a terminal where you can press Ctrl-C. Observed: it hangs. The author ran the built binary under `timeout 3` (Linux) and it ended with exit status 124. Each thread holds one lock and waits for the other forever.

Rust does not prevent deadlocks. The Reference lists them as behavior "not considered unsafe" (https://doc.rust-lang.org/reference/behavior-not-considered-unsafe.html), and the Rust Book says `Mutex<T>` "comes with the risk of creating deadlocks" (https://doc.rust-lang.org/book/ch16-03-shared-state.html). Fix it by always taking locks in the same order. Why does that work? Could the compiler ever check it for you?

### F. Measure

```
cargo run --release --quiet -- seq --fuel=1000000000 programs/heavy.fuel programs/heavy.fuel programs/heavy.fuel programs/heavy.fuel > /dev/null
cargo run --release --quiet -- par --fuel=1000000000 programs/heavy.fuel programs/heavy.fuel programs/heavy.fuel programs/heavy.fuel > /dev/null
```

(`> $null` on PowerShell, untested.) The timing line appears on stderr. Observed on the author's 4-core Linux container, release build, each job 100 million steps (several runs):

| | 4 jobs |
|---|---|
| `seq` | 550 to 588 ms |
| `par` | 137 to 165 ms |

About four times faster, which fits four independent jobs on four cores. In a debug build the author saw 2.05 s for one job alone and 2.32 s for four in parallel: about the same wall time for four times the work. Your numbers depend on your cores. Try fewer jobs than cores, then more. What happens at 8 jobs on 4 cores?

### G. Fuel across threads

```
cargo run -- par programs/forever.fuel programs/forever.fuel
```

Observed: both report `out of fuel after 10000 steps`. A runaway program is stopped by a rule inside the machine, not by an external watchdog or timeout, so the stopping point is the same on every run. Compare that with killing a thread after a number of seconds.

### H. Watch the schedule vary while the output does not

In `run_job`, add one line just before `Report { ... }`:

```rust
eprintln!("finished {name}");
```

Make four copies of `programs/heavy.fuel` named `heavy-a.fuel` to `heavy-d.fuel` and run, several times:

```
cargo run --release --quiet -- par --fuel=1000000000 programs/heavy-a.fuel programs/heavy-b.fuel programs/heavy-c.fuel programs/heavy-d.fuel
```

Observed in ten runs on the author's 4-core container, the order the jobs finished (stderr): `dcab`, `adbc`, `dbac`, `bdac`, `dacb`, `dbac`, `acbd`, `adbc`, `bcad`, `abcd`. Eight different orders in ten runs. The stdout of five further runs hashed identically. The schedule changed every time and the outcome did not. That is the difference described above, on screen.

Now think about what would make stdout vary: printing inside `run_job` instead of after `join`; collecting in completion order instead of spawn order; a shared counter that jobs read. Try the first one.

## What to take away

- Rust's type system prevents **data races** in safe code. It does not prevent **race conditions** or **deadlocks**. Both of those are logic errors that need design: fewer shared things, one lock per invariant, a fixed lock order.
- `Send` and `Sync` are how the compiler knows which types may cross threads. Compiler errors about `Rc` or non-`'static` borrows are those rules at work.
- The best concurrency design here was almost no concurrency: pure deterministic jobs, read-only shared data, results collected in order.
- Deterministic execution (one run is a function of its inputs) is not deterministic scheduling (the order threads run in). You get a deterministic outcome by design, not from Rust.
- `unsafe` code can break these guarantees. This project contains none.

## If you want to dig further

- Use a channel (`std::sync::mpsc`) instead of `join`. Results arrive in completion order. What do you have to add to restore deterministic output?
- Limit the number of running threads to the number of cores with a work queue.
- Add a shared, read-only cache of assembled programs behind `Arc`. Then try a `RwLock`.
- Check with `fn assert_send<T: Send>() {}` and a call like `assert_send::<Report>();`. Which of your types are `Send`, and which are not? Why?
- Async is a different tool, for waiting on many things at once. This workload is computing, not waiting, so there is no reason to use it here.
- Read the concurrency chapters of the Rust Book: https://doc.rust-lang.org/book/ch16-00-concurrency.html (the author read only the shared-state page when writing this).

That is the end of the project. There is no next exploration unless you make one.
