# 4. From text to program

**Objective.** Write an assembler: read a text file like `countdown.fuel` and produce the `Vec<Op>` the machine runs. Along the way you meet `String` versus `&str`, iterators, `collect` into a `Result`, `HashMap`, modules, `Box<dyn Error>`, and `cargo test`.

Optional, about 2 to 3 hours. Starts from exploration 3 finished. Back after a break? Read "What to take away" at the end for the recap.

## The format

```
# Prints 5 4 3 2 1.
push 5
loop:                # a label names the next instruction
  dup
  print
  push 1
  sub
  dup
  jz done            # jump operands are labels or plain numbers
  jmp loop
done:
  halt
```

One instruction per line. `#` starts a comment. `name:` on its own line is a label. Blank lines are ignored. Jump operands may be a label or a number, so the `list` output from exploration 3 can be read back.

## Set up

```
cd knowledge/languages/rust/fuel/04-text-to-program
cargo run
```

Create `programs/countdown.fuel` with the text above. You can copy the other example programs from `../05-parallel-runs/programs/` (Zsh: `cp ../05-parallel-runs/programs/*.fuel programs/`; PowerShell, untested: `Copy-Item ..\05-parallel-runs\programs\*.fuel programs\`). They are the same programs exploration 1 and 2 wrote as Rust.

Create `src/asm.rs` and add `mod asm;` near the top of `src/main.rs`. In `asm.rs`, start with `use crate::Op;`. A child module can see the private items of the file that declares it, so `Op` needs no `pub`.

## Mental model: owned text and borrowed text

`String` owns its characters on the heap and frees them when dropped. `&str` is a borrowed view: a pointer and a length into text someone else owns. String literals are `&str` too.

`source.lines()` gives you an iterator of `&str`. Each one is a slice *of `source`*. No text is copied. `line.split('#')`, `trim()`, `split_whitespace()` and `strip_suffix(':')` also return slices of the same bytes. Rust tracks that those slices cannot outlive `source`. Exploration 3's rule applies, now to text.

**TypeScript connection.** A JavaScript substring behaves as a fresh value and the garbage collector keeps the original alive as long as needed. Rust gives you the same zero-copy sharing without a collector, but you pay with lifetimes. The price shows up in experiment C.

## The shape of the assembler

Two passes. Pass 1 finds labels, because a `jmp` can refer to a label defined *later*. Pass 2 turns each line into an `Op`.

**Errors first.** Each error knows its line number and owns its text:

```rust
#[derive(Debug, PartialEq)]
pub enum AsmErrorKind {
    UnknownInstruction(String),
    MissingOperand,
    UnexpectedOperand(String),
    BadNumber(String),
    UnknownLabel(String),
    DuplicateLabel(String),
}

/// An error plus the (1-based) line it happened on.
/// It owns its text (`String`), so it can outlive the source it came from.
#[derive(Debug, PartialEq)]
pub struct AsmError {
    pub line: usize,
    pub kind: AsmErrorKind,
}
```

`AsmError` has `line` and `kind`. Implement `Display` (for example `line 3: unknown instruction foo`) and `std::error::Error` for it, as you did for `VmError`. The kinds hold `String`, not `&str`. That is a design decision: an owning error can be returned, stored and printed after the source text is gone. A borrowing one could not. Experiment C shows why that matters.

**Pass 1 and the glue:**

```rust
pub fn assemble(source: &str) -> Result<Vec<Op>, AsmError> {
    // Pass 1: find labels and collect instruction lines.
    // Both borrow from `source`; nothing is copied.
    let mut labels: HashMap<&str, usize> = HashMap::new();
    let mut lines: Vec<(usize, &str)> = Vec::new();
    for (i, raw) in source.lines().enumerate() {
        let line_no = i + 1;
        let text = raw.split('#').next().unwrap_or("").trim();
        if text.is_empty() {
            continue;
        }
        if let Some(name) = text.strip_suffix(':') {
            let name = name.trim();
            if labels.insert(name, lines.len()).is_some() {
                let kind = AsmErrorKind::DuplicateLabel(name.to_string());
                return Err(AsmError { line: line_no, kind });
            }
        } else {
            lines.push((line_no, text));
        }
    }

    // Pass 2: turn each line into an instruction.
    lines
        .into_iter()
        .map(|(line, text)| parse_line(text, &labels).map_err(|kind| AsmError { line, kind }))
        .collect() // Vec<Result<Op, _>> becomes Result<Vec<Op>, _>: the first error wins
}
```

Read it slowly. Things to notice:

- `labels` maps `&str` to an index. Its keys are slices of `source`.
- `lines.len()` at the moment a label is seen is the index of the next instruction. Labels are not instructions and take no slot.
- `HashMap::insert` returns the old value if there was one, so `.is_some()` detects a duplicate in one call.
- `.map(...).collect()` turns an iterator of `Result<Op, AsmError>` into one `Result<Vec<Op>, AsmError>`. If any item is an error, collection stops at the first one and returns it. The type you ask for decides this: `collect` can build many kinds of containers.
- `map_err` turns the `AsmErrorKind` `parse_line` returns into an `AsmError` with the line attached.

**Pass 2, one line:**

```rust
fn parse_line(text: &str, labels: &HashMap<&str, usize>) -> Result<Op, AsmErrorKind> {
    use AsmErrorKind::*;

    let mut parts = text.split_whitespace();
    let mnemonic = parts.next().unwrap_or("");
    let operand = parts.next();
    if let Some(extra) = parts.next() {
        return Err(UnexpectedOperand(extra.to_string()));
    }

    let plain = |op: Op| match operand {
        None => Ok(op),
        Some(x) => Err(UnexpectedOperand(x.to_string())),
    };
    let target = || -> Result<usize, AsmErrorKind> {
        let x = operand.ok_or(MissingOperand)?;
        match x.parse::<usize>() {
            Ok(n) => Ok(n),
            Err(_) => labels.get(x).copied().ok_or_else(|| UnknownLabel(x.to_string())),
        }
    };

    match mnemonic {
        "push" => {
            let x = operand.ok_or(MissingOperand)?;
            Ok(Op::Push(x.parse().map_err(|_| BadNumber(x.to_string()))?))
        }
        "jmp" => Ok(Op::Jmp(target()?)),
        "jz" => Ok(Op::Jz(target()?)),
        "add" => plain(Op::Add),
        "sub" => plain(Op::Sub),
        "mul" => plain(Op::Mul),
        "div" => plain(Op::Div),
        "dup" => plain(Op::Dup),
        "swap" => plain(Op::Swap),
        "over" => plain(Op::Over),
        "pop" => plain(Op::Pop),
        "print" => plain(Op::Print),
        "halt" => plain(Op::Halt),
        other => Err(UnknownInstruction(other.to_string())),
    }
}
```

Try writing `parse_line` yourself before you read it. The two closures, `plain` and `target`, capture `operand` and `labels` from the surrounding function. A closure is an anonymous function that can use the variables around it.

## Wire it into `main`

Replace the Rust functions `countdown()`, `arithmetic()` and the rest with files. The new `main` loads each path from the command line:

```rust
fn run_file(path: &str, list_only: bool) -> Result<(), Box<dyn std::error::Error>> {
    let source = std::fs::read_to_string(path)?;
    let program = asm::assemble(&source)?;
    ...
}
```

One function, two different error types: `std::io::Error` from reading the file and `AsmError` from assembling. The `?` converts both into `Box<dyn Error>`, because both implement `Error`. That is why you wrote `impl std::error::Error for AsmError {}`. Run:

```
cargo run -- programs/countdown.fuel programs/factorial.fuel
cargo run -- list programs/countdown.fuel
```

The finished `main.rs`, `asm.rs` and example programs are in [`../05-parallel-runs/`](../05-parallel-runs/README.md). That folder also adds threads, which is exploration 5.

## Tests

`cargo test` runs functions marked `#[test]`. The finished `asm.rs` has four, inside `#[cfg(test)] mod tests` at the bottom, and `main.rs` has five for the machine. Write your own before you read them. Which behaviors would you check first? The finished set covers: labels become indexes, numbers work as targets, each error kind carries its line number, and listing then reassembling gives the same program.

Observed with the finished crate: `cargo test` reports `9 passed`.

## Experiments

### A. Make the errors say something

Write small broken programs and run them. Observed:

```
push 1               ->  error: line 2: unknown instruction `frobnicate`
frobnicate

push 1               ->  error: line 3: `two` is not a number
(blank line)
push two

jmp nowhere          ->  error: line 1: unknown label `nowhere`

add 1                ->  error: line 1: unexpected operand `1`

push                 ->  error: line 1: missing operand
```

Is the message enough to find the mistake in a 500-line program? What would you add (the line's text, a column)?

### B. Which error comes first?

Write a file with an unknown instruction on line 2 and a repeated label on line 6. Observed: `line 6: label `x` is defined twice`. Why does the later line win? (Look at which pass reports which error.) Is that what you want, and how would you change it?

### C. Return labels from a function that owns the file

```rust
pub fn labels_of_file(path: &str) -> HashMap<&str, usize> {
    let source = std::fs::read_to_string(path).unwrap();
    let mut labels = HashMap::new();
    for (i, line) in source.lines().enumerate() {
        if let Some(name) = line.trim().strip_suffix(':') {
            labels.insert(name, i);
        }
    }
    labels
}
```

Observed:

```
error[E0515]: cannot return value referencing local variable `source`
    returns a value referencing data owned by the current function
```

The keys are slices of `source`, and `source` is freed when the function returns. Fix it by making the keys owned (`String`), and note what that costs. This is the same pattern as exploration 3, now with text. It is also why `AsmErrorKind` holds `String`.

### D. Break the assembler and watch the tests

In `assemble`, change `strip_suffix(':')` to `strip_suffix(';')`. Observed with the finished crate: `3 failed; 6 passed`. The failures are the label, error-line and round-trip tests. If you added the experiment E test, it fails too. A failing test points at the broken behavior from several sides. Put it back.

### E. Test every example program

Add to the `tests` module in `asm.rs`:

```rust
#[test]
fn every_example_program_round_trips() {
    for entry in std::fs::read_dir("programs").unwrap() {
        let path = entry.unwrap().path();
        let source = std::fs::read_to_string(&path).unwrap();
        let program = assemble(&source).unwrap();
        let listing: Vec<String> = program.iter().map(|op| op.to_string()).collect();
        assert_eq!(assemble(&listing.join("\n")).unwrap(), program, "{}", path.display());
    }
}
```

Observed: it passes with the example programs. `cargo test` runs from the package folder, so `programs` resolves. Add a program with an unusual layout (comments after labels, extra blank lines) and see whether it still round-trips.

### F. A different design

Pass 2 could look up labels itself instead of `parse_line` receiving the map. Or labels could resolve to `Op` placeholders and be patched afterwards. Sketch both. Which one makes the error for an unknown label simplest to produce?

## What to take away

- `&str` slices are views. The compiler makes you prove they do not outlive their owner.
- Iterator chains are lazy. `collect` is where work happens, and its target type decides what you get, including `Result<Vec<_>, _>`.
- Own the data in errors, borrow the data in short-lived working structures.
- `?` converts error types, which is why the `Error` trait is worth implementing.
- Tests check behavior in your own dialect of the problem. The round-trip test (parse the output of print) is a cheap way to find disagreement between two halves of a system.

## If you want to dig further

- Support `push 0x1f` and negative numbers in different bases. Where does `str::parse` stop helping?
- Add a `.data` section or a `call`/`ret` pair, and extend the error enum.
- Report *all* errors in a file instead of the first. What type does `assemble` return now?
- Replace `Box<dyn Error>` in `run_file` with an enum of your own. When is each better?
- Read about strings in the Rust Book: https://doc.rust-lang.org/book/ch08-02-strings.html (the author did not read this page when writing this guide).

Next: [exploration 5](../05-parallel-runs/README.md).
