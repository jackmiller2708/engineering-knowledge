# First exploration: who owns this string?

Optional. About 30 to 45 minutes. Not an unlock; nothing is recorded. Do it once, skip it, or come back later. Needs no Rust knowledge, only the tools in `README.md`.

## The problem

You write a function that uses a piece of text, then you try to use the text again afterwards. In TypeScript or Go this just works. In Rust it may not compile. Seeing why is the quickest way into how Rust handles memory.

## Set up

Work in any folder you like, outside this repository. Same commands in Zsh and PowerShell 7:

```
cargo new ownership-play
cd ownership-play
cargo run
```

Expected: `Hello, world!`. Edit `src/main.rs` for each step below, then run `cargo run`.

## Step 1: a program that does not compile

Replace `src/main.rs` with:

```rust
fn shout(text: String) {
    println!("{}!", text.to_uppercase());
}

fn main() {
    let greeting = String::from("hello");
    shout(greeting);
    println!("{}", greeting);
}
```

Run it. Before you read the error, guess which line it points at and why.

Observed (rustc 1.97.0, Linux; the exact wording changes between versions):

```
error[E0382]: borrow of moved value: `greeting`
...
7 |     shout(greeting);
  |           -------- value moved here
8 |     println!("{}", greeting);
  |                    ^^^^^^^^ value borrowed here after move
```

## The mental model

- Every value has exactly one owner: here, the variable `greeting`.
- Passing `greeting` to `shout(text: String)` **moves** the value. `shout` is now the owner. `greeting` is no longer usable.
- When an owner goes out of scope, the value is freed. Rust inserts that cleanup at compile time, so there is no garbage collector (GC) and no manual `free`.
- One owner means the compiler always knows who frees the value, so it is freed once, and never used after it is freed.

Where it differs from what you know: in TypeScript, passing an object shares a reference and both sides stay usable; the GC decides when to free it. Rust makes you say who owns it.

## Step 2: three ways to keep using the text

Try each in turn. All three compile and print `HELLO!` then `hello` (observed).

**A. Borrow it.** The function looks at the value without owning it. `&` means "borrow":

```rust
fn shout(text: &str) {
    println!("{}!", text.to_uppercase());
}

fn main() {
    let greeting = String::from("hello");
    shout(&greeting);
    println!("{}", greeting);
}
```

**B. Copy it.** `clone()` makes a second `String`. The function owns the copy. Costs an allocation:

```rust
fn shout(text: String) {
    println!("{}!", text.to_uppercase());
}

fn main() {
    let greeting = String::from("hello");
    shout(greeting.clone());
    println!("{}", greeting);
}
```

**C. Hand it back.** The function returns ownership:

```rust
fn shout(text: String) -> String {
    println!("{}!", text.to_uppercase());
    text
}

fn main() {
    let greeting = String::from("hello");
    let greeting = shout(greeting);
    println!("{}", greeting);
}
```

Which would you choose in a real API, and why? A is the usual answer when the function only reads. Notice how the function signature now tells the caller what happens to their value. That is Rust's effect on API design.

## Step 3: borrowing has rules

```rust
fn main() {
    let mut name = String::from("ada");
    let first = &name;
    name.push_str(" lovelace");
    println!("{}", first);
}
```

Observed:

```
error[E0502]: cannot borrow `name` as mutable because it is also borrowed as immutable
```

Rule: at any moment you may have many shared (`&`) borrows or one mutable (`&mut`) borrow, not both. If `push_str` could reallocate the string while `first` still pointed into it, `first` would point at freed memory. The compiler blocks that.

The same rule is why safe Rust cannot have a data race (see "Guarantees" in `README.md`). It does not stop deadlocks.

## Step 4: why did `i32` work?

```rust
fn double(n: i32) -> i32 {
    n * 2
}

fn main() {
    let n = 21;
    println!("{}", double(n));
    println!("{}", n);
}
```

Observed: prints `42` then `21`. Small fixed-size types like `i32` are `Copy`: passing them copies the bits and the original stays valid. `String` owns heap memory, so it is not `Copy`. The first error said exactly this: "which does not implement the `Copy` trait".

## Try it yourself (optional)

- Make step 1 work with a `Vec<String>` instead of a `String`. Which fix still works?
- Write `fn longest(a: &str, b: &str) -> &str` and read the error. This is where lifetimes come from. Stop there; they are a later direction in `README.md`.
- Run `rustc --explain E0382` and compare it with this page.

## Go deeper

- Official: The Rust Programming Language, "What is Ownership?": https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html
- Language-independent ideas (memory, ownership as a general idea) belong in `knowledge/<domain>/`. Ask for a concept document if you want one.

## Verification status

The author ran every program on this page on Linux with rustc and cargo 1.97.0 and observed the outputs quoted above. Not run: Windows or PowerShell. You have not run it until you do.
