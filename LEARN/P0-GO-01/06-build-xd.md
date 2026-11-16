# Section 6 of 8: Build `xd`

**Time:** about 90 minutes. **Goal:** your own `xd` prints a hex dump that follows the specification below. Testing and checking come in section 7.

## Why this matters

Almost everything later in this course deals with raw bytes: bit tricks, binary formats, network protocols, a crash-safe log. A hex dump is how you look at them. You are building the tool you will keep using.

## The picture

A 22-byte file: the text `Hello, Go!`, a newline, the text `bytes: `, three odd bytes (`00 01 ff`), and a newline. Here is what `xd` must print for it:

```
00000000  48 65 6c 6c 6f 2c 20 47 6f 21 0a 62 79 74 65 73  |Hello, Go!.bytes|
00000010  3a 20 00 01 ff 0a                                |: ....|
```

```
 offset   16 columns of "hex byte + space"                 text, one character per byte
 ┌──────┐ ┌───────────────────────────────────────────────┐ ┌──────────────────┐
 00000010  3a 20 00 01 ff 0a                                |: ....|
                            └─ short last line: the unused columns are blank,
                               so the | still lines up with the full line above
```

The text column shows a byte as itself if it is a printable ASCII character, and as `.` if not. The newline (`0a`) and the three odd bytes all became dots.

## The specification (exact)

| Rule | Detail |
|---|---|
| Usage | `xd [file]`. With a file argument, read that file. With none, read standard input |
| One line per 16 bytes | The last line may have fewer than 16 |
| Offset | Position of the line's first byte, as **8 lowercase hexadecimal digits** (`00000000`, `00000010`, ...) |
| Then | **Two spaces** |
| Hex columns | **16 columns, 3 characters each**: two lowercase hex digits and a space. On a short last line, each unused column is **three spaces** |
| Then | One more space, then `\|` |
| Text | One character per input byte: the byte itself if it is `0x20` to `0x7e`, otherwise `.` . Not padded |
| Then | `\|`, then a newline (`\n`, a single character, on every platform) |
| Empty input | Prints nothing at all |
| A file that cannot be opened | A message on standard error, exit status not zero, nothing on standard output |

If you have Linux's `hexdump -C`, it is close to this, with two differences: it adds an extra gap in the middle of the hex columns and a final line with the total size. `xd` does neither.

## Where your code goes

In your `labs` module:
```
labs/
  hexdump/hexdump.go         package hexdump: the logic
  hexdump/hexdump_test.go    your tests (section 7)
  cmd/xd/main.go             package main: the command
```
Suggested name for the main function: `Dump(w io.Writer, r io.Reader) error`: read everything from `r`, write the dump to `w`. Everything else is your design.

**Sample input.** Copy the 22-byte file above from your clone of the course repository into your scratch folder.

**Linux (Zsh):**
```
cp <CLONE>/LEARN/P0-GO-01/examples/accept/fixtures/sample.in sample.bin
```
**Windows (PowerShell 7), not run by the author:**
```
Copy-Item <CLONE>\LEARN\P0-GO-01\examples\accept\fixtures\sample.in sample.bin
```
(`<CLONE>` is the folder where you cloned the course repository.)

## How to work through this

Four milestones, each with less help than the last. Do them in order.

**How to use help.** `hints/06-xd-hints.md` has four levels, from a small nudge to an outline. If you have made no progress on a milestone for about 20 minutes, take the next level. **Write down which levels you used**: it goes in your evidence, and it is useful information, not a penalty. The folder `examples/spoiler-reference-xd/` is a complete solution. Please keep it closed until you have finished or are truly stuck, and note it if you open it.

### Milestone 1 (about 20 minutes): format one full line

Write a function that takes an offset and exactly 16 bytes and returns the text of one line. **Write the test first.** For the 16 bytes `ABCDEFGHIJKLMNOP` at offset 0, the expected line is:
```
00000000  41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50  |ABCDEFGHIJKLMNOP|
```
Make it pass. Useful: `fmt.Sprintf` with the verbs `%08x` and `%02x`.

### Milestone 2 (about 20 minutes): a short line

The same function must now handle fewer than 16 bytes. **Work out the expected line for the single byte `A` yourself, from the rules**, and write the test. Only after your test passes, compare with the file `examples/accept/fixtures/one-byte.out`.

### Milestone 3 (about 25 minutes): a whole stream

Write `Dump(w io.Writer, r io.Reader) error`. Keep reading until the input ends. Each full group of 16 bytes becomes one line, the final partial group becomes one short line, and empty input produces nothing. Test it with 17 bytes read from a `strings.NewReader`: two lines, the second holding one byte. Work out the expected text by hand.

### Milestone 4 (about 25 minutes): the command

Write `cmd/xd/main.go`: file argument or standard input, an error message and non-zero exit status for a file that will not open. You have seen this shape already, in `cnt`.

Run it on your sample:
```
go run ./cmd/xd sample.bin
```
and compare by eye with the picture at the top.

## Check yourself

Try these before opening anything else; they are answered in `answers/06-answers.md` (after you try).

1. Why is formatting one line a separate function from the loop that reads?
2. What changes in the output when the input is exactly 32 bytes, and when it is 33?
3. Which part of your code makes the `|` line up on a short last line?

## Done when

- [ ] `go run ./cmd/xd sample.bin` prints what the picture shows.
- [ ] Tests for milestones 1 to 3 pass.
- [ ] You noted which hint levels you used, and whether you opened the reference solution.

**Next:** `07-test-and-verify.md`. **Hints:** `hints/06-xd-hints.md`.
