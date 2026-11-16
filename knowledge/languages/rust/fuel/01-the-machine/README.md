# 1. The machine

**Objective.** Run a tiny stack machine, then change it and watch what the compiler does. You meet enums with data, exhaustive `match`, structs, `Vec`, `&mut self`, `Copy`, and what a panic looks like.

Optional, about 1 to 2 hours. Start at `../README.md` if you have not seen the project.

## Run it

```
cd knowledge/languages/rust/fuel/01-the-machine
cargo run
cargo run -- countdown
```

You should see `42`, then `5 4 3 2 1`, then `-7` and `1`. Naming a program after `--` runs just that one. The same `cargo` commands work in PowerShell 7 (not run there by the author).

Come back after a break? Run it again, then read "What to take away" below for the recap.

## The code in five minutes

Open `src/main.rs`.

**A stack machine** keeps a stack of numbers. `push 6` puts 6 on it. `add` pops two numbers and pushes their sum. `print` pops one and prints it. `jz 8` pops a number and, if it was zero, continues at instruction 8 instead of the next one. `(2 + 4) * 7` is `push 2, push 4, add, push 7, mul, print`. The `pc` (program counter) field is the index of the next instruction.

**`enum Op`** is the instruction set. Some variants carry data: `Push(i64)`, `Jmp(usize)`. An `Op` value is exactly one variant at a time, plus its data. Its size is the largest variant plus a tag: 16 bytes here (observed with `std::mem::size_of::<Op>()`).

**`match op { ... }`** in `run` handles each variant. The compiler checks that every variant has an arm. That is the first thing to test.

**`impl Vm`** puts methods on the struct. `&mut self` means "this method may change the machine, and nobody else may look at it while it does". `fn pop(&mut self) -> i64` calls `self.stack.pop()`, which returns an `Option<i64>` (`Some(n)` or `None`), and `.unwrap()` turns `None` into a crash. Keep that in mind.

**TypeScript connection.** `Op` is a discriminated union (`{ kind: "push", n: number } | { kind: "add" } | ...`) with the tag handled for you. The difference that matters: in TypeScript you opt in to exhaustiveness checking (a `never` check in the `default` branch). In Rust a non-exhaustive `match` does not compile.

## Experiments

Change one thing at a time. Undo each edit before the next, or restore the folder (see `../README.md`).

### A. Watch it run

In `main`, change `.run(false)` to `.run(true)` and run `cargo run -- countdown`. Observed (the stack shown is the one *before* the instruction runs):

```
  pc=0  Push(5)    stack=[]
  pc=1  Dup        stack=[5]
  pc=2  Print      stack=[5, 5]
5
  pc=3  Push(1)    stack=[5]
```

Follow one loop around by hand. Where does `Jz(8)` decide, and what is on the stack when it does?

### B. Delete an arm

Delete the `Op::Pop => { ... }` arm in `run`. Observed:

```
error[E0004]: non-exhaustive patterns: `Op::Pop` not covered
...
help: ensure that all possible cases are being handled by adding a match arm with a wildcard pattern or an explicit pattern as shown
```

This is the point of the enum. Add an instruction later and the compiler lists every `match` that now needs updating. Notice the tempting fix, a wildcard arm `_ => {}`. Try it, then think about what you lost. (You would stop getting this error for new variants.)

### C. Add an instruction

Add `Over`: copy the second item to the top, so `[a b]` becomes `[a b a]`. First add only the variant `Over,` to the enum. Observed:

```
error[E0004]: non-exhaustive patterns: `Op::Over` not covered
```

Now write the arm. Then write a Fibonacci program that prints 0 1 1 2 3 5 and so on, using `Over`, `Swap` and `Add` in a loop. Add it to the `programs` list in `main` and run it by name.

Expect it to end in a crash. Read the message. Exploration 2 is about why, and about making the machine stop crashing.

The version with `Over` and a Fibonacci program is the starting point of exploration 2 (`../02-errors-and-fuel/`). Compare yours with it.

### D. Remove `Copy`

`#[derive(Debug, Clone, Copy, PartialEq)]` asks the compiler to write some trait implementations for `Op`. Remove `Copy` and build. Observed:

```
error[E0507]: cannot move out of index of `Vec<Op>`
  --> src/main.rs:37:22
   |
37 |             let op = self.program[self.pc];
   |                      ^^^^^^^^^^^^^^^^^^^^^ move occurs because value has type `Op`, which does not implement the `Copy` trait
help: consider borrowing here
help: consider cloning the value if the performance cost is acceptable
```

What is going on: `let op = self.program[i]` would *move* the value out of the vector, leaving a hole in the middle of it. A `Vec` cannot have holes, so Rust refuses. Three honest fixes, all in the compiler's help text:

- `Copy`: the value is small plain data, so copying the 16 bytes is as cheap as passing a reference. This is what the file does.
- Borrow with `&self.program[self.pc]`. Then `match` works on a reference, and the arms get references to the data inside.
- `.clone()` explicitly.

Try the borrow version. Observed: three `E0308 mismatched types` errors (the `Push`, `Jmp` and `Jz` arms), because those arms now bind references (`&i64`, `&usize`) instead of values. How would you fix each? (Dereference with `*`, or match on `*op`.) Why can `i64` and `usize` be `Copy` while `String` and `Vec` cannot? (Hint: who frees the memory?)

### E. Break the machine on purpose

Add these to the `programs` list and run each by name:

```rust
("underflow", vec![Op::Add, Op::Halt]),
("wild-jump", vec![Op::Jmp(99)]),
```

Observed (the line numbers differ in your edit):

```
thread 'main' panicked at src/main.rs:31:26:
called `Option::unwrap()` on a `None` value
```

```
thread 'main' panicked at src/main.rs:37:34:
index out of bounds: the len is 1 but the index is 99
```

Two different crashes, one cause: the machine trusts its program. A panic is not undefined behavior. Rust stops the thread in a controlled way and reports where. But a machine that crashes on bad input is not much of a machine.

## What to take away

- An enum value is one variant plus its data, and `match` must handle every variant.
- Adding a variant turns "find every place that needs updating" into a compiler error list.
- `unwrap` is a promise to the compiler that `None` cannot happen. Break it and you get a panic.
- Whether a value can be duplicated freely (`Copy`) or must be moved is a property of the type. It becomes important from exploration 3 on.

## If you want to dig further

- Add `Neg`, `Jnz` (jump if not zero), or `Rot` (rotate three items). Which of them make the countdown shorter?
- Write a program that computes the greatest common divisor of two numbers.
- Make `Push` take an `i32` instead. What breaks, and how far from the change?
- Why is `Jmp(usize)` a `usize` and not an `i64`? What does indexing a `Vec` require?
- Read about `#[derive]` in the Rust Book: https://doc.rust-lang.org/book/appendix-03-derivable-traits.html (not read by the author when writing this page).

Next: [exploration 2](../02-errors-and-fuel/README.md).
