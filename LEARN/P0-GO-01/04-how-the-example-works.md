# Section 4 of 8: Why the example is built this way

**Time:** about 30 minutes. **Goal:** you can explain the design of `cnt`, trace it by hand, and name the assumptions it makes. `xd` will use the same design.

## Why this matters

You can copy working code without understanding it, and it will work until the day it does not. The point of this section is to turn "I ran it" into "I know why it is shaped like this", because you will make the same shape decisions in `xd` without a template.

## Picture 1: one function, many sources

```
   a file you opened ──┐
   standard input ─────┼──►  io.Reader  ──►  Count(r)  ──►  Result{Lines, Words, Bytes}
   a string in a test ─┘   "something you           │
                            can read bytes from"     └─ returns an error if reading fails
```

`io.Reader` is an *interface*: a promise that a value has a `Read` method. A file, standard input, and `strings.NewReader("text")` all keep that promise, so `Count` works with all three without knowing which one it has. This is why `count_test.go` can test `Count` with plain strings and no files on disk.

Compare the alternative, `Count(path string)`. It would force every test to create a real file, and it could not read standard input at all.

## Picture 2: trace it by hand

Here is `Count` run on the four bytes of `a b` followed by a newline. `inWord` remembers whether the previous byte was part of a word.

| step | byte | what it is | space? | `inWord` before → after | Lines | Words | Bytes |
|---|---|---|---|---|---|---|---|
| start | | | | false | 0 | 0 | 0 |
| 1 | `0x61` | `a` | no | false → **true** | 0 | **1** | 1 |
| 2 | `0x20` | space | yes | true → false | 0 | 1 | 2 |
| 3 | `0x62` | `b` | no | false → **true** | 0 | **2** | 3 |
| 4 | `0x0a` | newline | yes | true → false | **1** | 2 | 4 |

Result: 1 line, 2 words, 4 bytes. The rule that counts a word is *"a non-space byte when `inWord` is false"*: a word is counted at its **first** byte, not at its end. That is why a file with no final newline still counts its last word.

**Your turn.** Trace `ab  c` (two letters, two spaces, one letter; no newline) with the same columns. What are Lines, Words and Bytes at the end? Then check by adding it as a test row, and run the test.

## How the program is organised

- **`count` is a library, `main` is a thin shell.** The package holds the logic; `main` only handles arguments, opens the file, calls `Count` and prints. Logic you can test lives where tests can reach it. Logic in `main` can only be tested by running the whole program.
- **Errors are values.** `Count` returns `(Result, error)`. Callers write `if err != nil { ... }` right after the call. There are no hidden exceptions: you can see every place a failure is handled.
- **End of file is a signal, not a failure.** `ReadByte` returns the error value `io.EOF` when the input is finished. `Count` checks for it first and stops normally.
- **Tests are a table.** Each row is a name, an input and the expected result. One loop runs them all, and `t.Run` gives each row its own name in the output. Adding a case is one new line.
- **`defer f.Close()`** arranges for the file to be closed when `main` returns. `os.Exit(1)` ends the program immediately and **does not run deferred calls**. Here that is harmless, because the operating system closes the file when the program ends, but it is worth knowing.

## What the example assumes (and where it could fail)

These are limits of this tool, not bugs to fix:
- It counts **bytes**, not characters. The `é` row in the test is there to show it.
- It treats only **ASCII whitespace** as a word separator. Other Unicode spaces are not recognised.
- It reads **one byte at a time** through a buffer. That is fine for small inputs. `xd` will read in chunks instead, and you will see why in section 6.

## Check yourself

Try these before opening `answers/04-answers.md`.

1. Why is the function `Count(r io.Reader)` and not `Count(path string)`? Give two concrete things the second form would make harder.
2. Fill in the trace for `ab  c`. How many words, and which step counts each one?
3. What does `defer f.Close()` do? In `main`, one `os.Exit(1)` happens before the `defer` line and one after. Which of them skips the `Close`, and does it matter here?
4. A teammate says: "the table test is overkill, three separate test functions would be clearer." What do you say?

## Done when

- [ ] You traced `ab  c` and confirmed it with a test row.
- [ ] You can explain, without looking, why `Count` takes an `io.Reader`.
- [ ] You can name at least two assumptions `cnt` makes.

**Next:** `05-change-the-example.md`. **Answers:** `answers/04-answers.md` (after you try).
