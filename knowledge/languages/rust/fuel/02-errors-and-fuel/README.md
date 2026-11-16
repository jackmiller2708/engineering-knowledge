# 2. Errors as values, and fuel

**Objective.** Make the machine total: whatever program you give it, `run` returns, and returns the same thing every time. You meet `Result`, `?`, error types, `Display`, checked arithmetic, and the difference between debug and release builds.

Optional, about 2 to 3 hours. Starts from exploration 1 plus `Over` and a Fibonacci program (`fib`). Same `cargo` commands in PowerShell 7 (not run there by the author). Back after a break? Read "What to take away" at the end for the recap.

## Part 1: the same source, two answers

```
cd knowledge/languages/rust/fuel/02-errors-and-fuel
cargo run -- fib
```

Observed: it prints `0 1 1 2 3 5 ...`, reaches `4660046610375530309`, then crashes:

```
thread 'main' panicked at src/main.rs:48:37:
attempt to add with overflow
```

The next Fibonacci number does not fit in an `i64`. Now build it the way you would ship it:

```
cargo run --release -- fib | head -100       # PowerShell (untested): ... | Select-Object -First 100
```

Observed: no crash. The numbers pass `7540113804746346429` and the next one is `-6246583658587674878`. The addition silently wrapped around, and the program never stops by itself. (The `head` closing the pipe makes the program complain about a broken pipe at the end. Expected.)

**What happened.** The Rust Reference says integer overflow is not unsafe, and that a program which overflows has a bug: when debug assertions are on (a non-optimized build) implementations must check and panic, and other builds "may result in panics or silently wrapped values on overflow, at the implementation's discretion", with two's complement results when they wrap (https://doc.rust-lang.org/reference/behavior-not-considered-unsafe.html, "Integer overflow"). Neither answer is undefined behavior. But `a + b` means different things depending on a build setting. The author's `--release` run shows the wrapping default; check your own profile settings if it differs. For a machine whose whole promise is "same program, same result", that is the bug. The fix is to make overflow part of the machine's meaning: an error you can name, in every build.

## Part 2: rebuild `run` so it cannot crash

Do this in `src/main.rs` in whatever order suits you. The finished version is [`../03-borrowing-the-program/src/main.rs`](../03-borrowing-the-program/src/main.rs). Try before you look.

**1. Name the ways a program can go wrong.**

```rust
#[derive(Debug, PartialEq)]
enum VmError {
    StackUnderflow { at: usize, op: Op },
    DivideByZero { at: usize },
    Overflow { at: usize },
    RanOffEnd { at: usize },
    OutOfFuel { steps: u64 },
}
```

An error is just a value, here an enum with data. Implement `std::fmt::Display` for it (the `match` writes one sentence per variant with `write!`) and then `impl std::error::Error for VmError {}`. The last line is empty because the trait's methods have defaults.

**2. Make `pop` return a `Result`.**

```rust
fn pop(&mut self, at: usize) -> Result<i64, VmError> {
    self.stack.pop().ok_or(VmError::StackUnderflow { at, op: self.program[at] })
}
```

`Option::ok_or` turns `None` into the error you give it. Callers write `let b = self.pop(at)?;`. The `?` means: if this is an `Err`, return it from the current function right now; if it is `Ok(v)`, continue with `v`. That is how errors travel up without `try`/`catch`.

**3. Use checked arithmetic.** `i64::checked_add(a, b)` returns `Some(sum)` or `None` instead of overflowing. A helper keeps `run` short:

```rust
fn arith(&mut self, at: usize, f: fn(i64, i64) -> Option<i64>) -> Result<(), VmError> {
    let b = self.pop(at)?;
    let a = self.pop(at)?;
    self.stack.push(f(a, b).ok_or(VmError::Overflow { at })?);
    Ok(())
}
// in run: Op::Add => self.arith(at, i64::checked_add)?,
```

`f` is a function pointer. `i64::checked_add` is an ordinary function, so you can pass it by name. Add `Div` yourself. Division by zero is its own error, so check `b == 0` first and then use `checked_div` (which only fails for `i64::MIN / -1`).

**4. Add fuel.** Give the struct `steps: u64`. Change `run` to `fn run(&mut self, fuel: u64) -> Result<(), VmError>`. At the top of the loop, if `self.steps == fuel` return `Err(VmError::OutOfFuel { steps: self.steps })`, and count each instruction.

**5. Replace the index panic.** `self.program.get(at)` returns an `Option<&Op>` instead of panicking when `at` is out of range. Turn `None` into `VmError::RanOffEnd { at }`, and dereference (`*`) because `Op` is `Copy`.

**6. Collect output instead of printing it.** Give `Vm` a field `output: Vec<i64>` and make `Print` push to it. `main` prints it afterwards. Now a run is a pure function from (program, fuel) to (output, steps, result), which also makes it testable.

**7. Add the failing programs** (`overflow`, `underflow`, `divide-by-zero`, `forever`, `wild-jump`) and make `main` print `ok after N steps` or `error: ...` for each.

When all of it compiles, `cargo run` runs every program and no program crashes. Observed:

```
== countdown ==  ok after 36 steps
== fib ==        error: arithmetic overflow at instruction 6
== underflow ==  error: stack underflow: Add at instruction 1 needs more values
== forever ==    error: out of fuel after 10000 steps
== wild-jump ==  error: no instruction at index 99
```

(The real output prints each on its own lines.)

## Experiments

### A. Ignore a `Result`

In `main`, call `vm.run(FUEL);` and drop the returned value. It still compiles. Observed:

```
warning: unused `Result` that must be used
  = note: this `Result` may be an `Err` variant, which should be handled
```

TypeScript has no equivalent: an ignored promise rejection or a swallowed return code is silent. Rust marks `Result` as `#[must_use]`. Try `let _ = vm.run(FUEL);` to say "I mean it".

### B. `unwrap` the error

Write `vm.run(FUEL).unwrap();` and run `cargo run -- underflow`. Observed:

```
called `Result::unwrap()` on an `Err` value: StackUnderflow { at: 1, op: Add }
```

You turned an error value back into a crash. Notice the message uses `{:?}` (`Debug`), not your `Display` sentence. Print the same error with `{}` and with `{:?}`. When is each useful?

### C. Same answer in every build

```
cargo run --quiet > debug.txt
cargo run --release --quiet > release.txt
```

Compare the files (`diff debug.txt release.txt`; PowerShell, untested: `Compare-Object (Get-Content debug.txt) (Get-Content release.txt)`). The author observed no difference, and also none between two debug runs. Compare that with Part 1.

### D. The case checked division catches

Add a program `push i64::MIN`, `push -1`, `div`. Observed: `Overflow { at: 2 }`. The true answer, `2^63`, does not fit. The author did not try plain `/` here. Find out what it does in debug and in release, and compare with `a + b` in Part 1.

### E. Fuel is exact

Run the countdown with fuel 10, 30 and 100. Observed: `out of fuel after 10 steps`, `out of fuel after 30 steps`, `ok after 36 steps`. Why is the count exactly 36? Count the instructions in the loop by hand: one `Push`, four full loops of seven, one shorter loop of six, one `Halt`.

### F. How fast is a step?

Timing is not part of the machine's meaning, so measure it from outside. Add this above `main`, and make `main` call it when the first argument is `speed`:

```rust
fn speed_test() {
    let mut program = countdown();
    program[0] = Op::Push(30_000_000);
    program[2] = Op::Pop; // no output, so we measure the machine
    let mut vm = Vm::new(program);
    let start = std::time::Instant::now();
    let result = vm.run(u64::MAX);
    let secs = start.elapsed().as_secs_f64();
    println!("{:?}: {} steps in {:.2} s = {:.0} million steps/s",
             result, vm.steps, secs, vm.steps as f64 / secs / 1e6);
}

// first lines of main:
if std::env::args().nth(1).as_deref() == Some("speed") {
    speed_test();
    return;
}
```

Run it with `cargo run -- speed` and `cargo run --release -- speed`. Observed on the author's Linux container: 46 to 47 million steps/s in debug and 762 to 781 million in release over several runs, about 16 times faster. Your numbers will differ; the gap is the point. Debug builds keep every check and skip optimization.

Why might this be the only place the standard library's clock appears? What would happen to your determinism guarantee if `run` read the time?

## What to take away

- Errors are ordinary values. `?` moves them up. `Result` is `#[must_use]`.
- A function that returns `Result` documents how it fails in its signature.
- `checked_*` puts overflow into the semantics instead of leaving it to the build profile.
- Determinism is a design property you add on purpose: fuel, no clock, no hidden state, output as data.

## If you want to dig further

- Make `main` return `Result<(), Box<dyn std::error::Error>>` and use `?` there. What does `Box<dyn Error>` cost, and what does it hide?
- Replace `Op::Div` by `Op::DivMod` pushing two results.
- A `run` that returns the partial output together with the error. What type is that?
- Try `i64::wrapping_add`, `saturating_add` and `overflowing_add`. Which semantics would suit a different machine?
- Read about error handling in the Rust Book: https://doc.rust-lang.org/book/ch09-00-error-handling.html (not read by the author when writing this page).

Next: [exploration 3](../03-borrowing-the-program/README.md).
