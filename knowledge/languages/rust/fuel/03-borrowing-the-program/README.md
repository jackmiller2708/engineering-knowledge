# 3. Borrowing the program

**Objective.** Run one program under many fuel budgets without copying it, and find out what the compiler is protecting you from. You meet references, the borrow checker, lifetimes, and `impl Display` for a type of your own.

Optional, about 1.5 to 3 hours. Starts from exploration 2 finished. Back after a break? Read "What to take away" at the end for the recap.

## The itch

```
cd knowledge/languages/rust/fuel/03-borrowing-the-program
cargo run
```

At the end of the output the countdown runs three times under different fuel. Look at the bottom of `main`:

```rust
let program = countdown();
for fuel in [10, 30, 100] {
    let mut vm = Vm::new(program.clone());   // a full copy, every time
    ...
}
```

`Vm` owns its program (`program: Vec<Op>`), so each machine needs its own copy. For 9 instructions that costs nothing. For a program with a million instructions and a thousand fuel budgets it does. The program never changes while a machine runs. Several machines could look at one copy.

## The mental model

Ownership gave every value one owner. A **reference** (`&T`) lends access without transferring ownership. The compiler enforces two rules about lending:

1. At any moment you may have **any number of shared references** (`&T`) *or* **one mutable reference** (`&mut T`), never both.
2. A reference may not outlive the thing it points to.

Rule 1 means a value that is being read through `&` cannot change underneath the reader. Rule 2 means no reference ever points at freed memory. Both are checked at compile time and cost nothing at run time. A reference is just a pointer.

A **lifetime** is the name for "how long this borrow is valid". Usually the compiler works it out and you never write one. You write one, such as `'p`, when a *type* holds a reference and the compiler needs to be told how that reference relates to the type's own lifetime. In `Vm<'p>`, `'p` reads: "this machine holds a borrow of a program, and the machine cannot outlive it."

**TypeScript connection.** In TypeScript every object variable is already a reference, and any of them may mutate the object at any time. `readonly` is erased at run time and does not stop another alias from mutating. Rust's rule 1 is the part TypeScript cannot give you: knowing that nobody else can mutate while you read.

## Do it

Make four changes. The finished version is [`../04-text-to-program/src/main.rs`](../04-text-to-program/src/main.rs).

**1.** Change the struct and its `impl`:

```rust
struct Vm<'p> {
    program: &'p [Op],
    ...
}

impl<'p> Vm<'p> {
    fn new(program: &'p [Op]) -> Vm<'p> { ... }
```

`&[Op]` is a *slice*: a pointer plus a length, a view of a run of `Op`s. Taking a slice rather than `&Vec<Op>` means any caller with an array, a `Vec`, or a part of one can use it. That is a common API choice.

**2.** In `main`, loop over `&programs` so the vector is borrowed instead of consumed, and pass `program` straight to `Vm::new`. A `&Vec<Op>` is accepted where a `&[Op]` is expected (the compiler converts it, called *deref coercion*).

**3.** In the fuel sweep, replace `program.clone()` with `&program`.

**4.** Build and run. Output is the same as before. The fix removed a copy and added no behavior. That is the Rust way: the change shows up in the types, not in the output.

## Experiments

### A. Mutate while borrowed

Add this to the end of the file and build:

```rust
fn experiment() {
    let mut program = countdown();
    let mut vm = Vm::new(&program);
    program.push(Op::Halt);
    let _ = vm.run(10);
}
```

Observed:

```
error[E0502]: cannot borrow `program` as mutable because it is also borrowed as immutable
284 |     let mut vm = Vm::new(&program);
    |                          -------- immutable borrow occurs here
285 |     program.push(Op::Halt);
    |     ^^^^^^^^^^^^^^^^^^^^^^ mutable borrow occurs here
286 |     let _ = vm.run(10);
    |             -- immutable borrow later used here
```

Read the three labelled lines as a story. `push` may reallocate the vector, which would leave the machine pointing at freed memory. The error only appears because `vm.run` is used afterwards. Delete the `vm.run` line and it compiles (with an unused-variable warning, observed). The borrow ends at its last use, not at the end of the block.

### B. Return a machine built from a local

```rust
fn make_vm() -> Vm {
    let program = countdown();
    Vm::new(&program)
}
```

Observed: `error[E0106]: missing lifetime specifier` with the help "this function's return type contains a borrowed value, but there is no value for it to be borrowed from". The compiler's suggestion is `-> Vm<'static>`. Accept it and build again:

```
error[E0515]: cannot return value referencing local variable `program`
    returns a value referencing data owned by the current function
```

`program` is dropped when the function ends, so the machine would point at nothing. This is the classic dangling pointer, turned into a compile error. What would fix it? (Return the program too. Take the program as an argument. Or make the machine own it again.) Which is best, and when would you give up the borrow and use `Vec<Op>` instead?

### C. Leave out the lifetime

Change the field to `program: &[Op],` without `'p`. Observed:

```
error[E0106]: missing lifetime specifier
 69 |     program: &[Op],
    |              ^ expected named lifetime parameter
help: consider using the `'p` lifetime
```

There is no function here to infer anything from, so Rust asks you to say it.

### D. When the compiler can and cannot work it out

```rust
fn first_print(program: &[Op]) -> Option<&Op> {
    program.iter().find(|op| **op == Op::Print)
}

fn longer(a: &[Op], b: &[Op]) -> &[Op] {
    if a.len() >= b.len() { a } else { b }
}
```

Observed: `first_print` compiles. `longer` fails: "the signature does not say whether it is borrowed from `a` or `b`". With one input reference the result obviously borrows from it. With two, you must say, and the suggestion is `fn longer<'a>(a: &'a [Op], b: &'a [Op]) -> &'a [Op]`. Apply it and it builds. What does `'a` promise a caller about the result?

### E. Many readers at once

```rust
fn two_vms() {
    let program = countdown();
    let mut a = Vm::new(&program);
    let mut b = Vm::new(&program);
    let _ = a.run(10);
    let _ = b.run(100);
    println!("{} {}", a.steps, b.steps);
}
```

This compiles (the author built it and, calling it from `main`, observed `10 36`). Two machines read one program. That is rule 1: many shared borrows are fine. Why is `a.run(10)` allowed to take `&mut self` while the program is shared? What exactly is mutable, and what is not?

### F. Teach an instruction to print itself

The finished version has `impl fmt::Display for Op` and a `list` mode:

```
cargo run -- list countdown
```

Write the `Display` impl yourself, one `write!` per variant (`push 5`, `add`, `jz 8`). Observed output:

```
== countdown ==
  0  push 5
  1  dup
  2  print
  ...
  8  halt
```

You implemented a *trait*: a named set of behavior that a type can promise. `Display` is what `{}` calls. The same mechanism lets `{:?}` use `Debug` (which `derive` wrote for you) and gives you `to_string()` for free. Exploration 4 reads this text format back.

## What to take away

- Passing `&x` instead of cloning is about *who may change what while someone reads*, not only speed.
- A lifetime annotation does not change how long anything lives. It documents a relationship so the compiler can check it.
- Most borrow errors have the same shape: a borrow is still needed later, and something conflicts with it in between.
- API choice: accept `&[Op]` (borrowed, flexible), or `Vec<Op>` (owned, simple), or `Rc<[Op]>`/`Arc<[Op]>` (shared ownership). Each trades flexibility, copying and complexity differently.

## If you want to dig further

- Make `Vm` generic over any `P: AsRef<[Op]>`. Then it works with `Vec<Op>`, `&[Op]`, `Box<[Op]>`, and more. What does the compiler generate?
- Hold the program in an `Rc<Vec<Op>>` and count references with `Rc::strong_count`. When does that beat borrowing?
- Try to store a `Vm` inside a struct together with the program it borrows. The compiler will object. Why is a self-referencing struct hard?
- Read about references and borrowing in the Rust Book: https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html and lifetimes in https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html (the author did not read these pages when writing this guide).

Next: [exploration 4](../04-text-to-program/README.md).
