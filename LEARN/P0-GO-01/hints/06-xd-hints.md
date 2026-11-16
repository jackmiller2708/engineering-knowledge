# Hints for section 6 (`xd`)

Use **one level at a time**, only after about 20 minutes without progress on a milestone. Write down the highest level you used for each milestone. It is useful information for your evidence, not a penalty.

Each level assumes you have read the one before. The reference solution (`examples/spoiler-reference-xd/`) is the step after Level 4.

## Level 1: a nudge

- Think of the output as a table. Every row comes from at most 16 bytes plus a position. Which parts of a row are the same for a full row and a short row, and which differ?
- Which `fmt` verb prints a number in hexadecimal, with a fixed width, padded on the left with zeros? Look at the `fmt` package documentation for `%x`, and for width and `0` flags.
- A byte is a number from 0 to 255. How do you decide whether it is printable?

## Level 2: structure

- Split the work in two. A **pure function** that turns an offset and a slice of at most 16 bytes into one string (the whole line, including the newline), and a **loop** that reads input and calls it. The pure function is easy to test with a table, exactly like `Count`.
- Inside the line function, build the line in the same order the specification lists it: offset, two spaces, the 16 columns, one space and `|`, the text, `|`, newline.
- For the 16 columns: loop `i` from 0 to 15. If there is a byte at `i`, write its two hex digits and a space. Otherwise write three spaces. That one loop is what makes short lines line up.
- For the text column: loop over the bytes you actually have (not 16), and write the byte or a dot.

## Level 3: the tricky parts

- **Reading.** `r.Read(buf)` is allowed to return *fewer* bytes than `len(buf)` even when more input is coming. If you call it once per line, a long file will sometimes give you short lines in the middle. The `io` package has a function that keeps reading until the buffer is full or the input ends: `io.ReadFull`.
- `io.ReadFull` returns two kinds of "the input ended" results, and **both are normal**, not failures: `io.EOF` (it read nothing) and `io.ErrUnexpectedEOF` (it read some bytes, but fewer than the buffer holds). Any other error is a real failure.
- **Offsets.** Keep a running count of how many bytes you have already written lines for. It starts at 0 and grows by the number of bytes in each line you write, not always by 16.
- **The command.** The shape is the same as `cnt`'s `main`: `os.Args`, `os.Open`, `os.Stdin`, an error to standard error, `os.Exit(1)`.

## Level 4: an outline (the loop, in words)

```
offset = 0
repeat:
    n, err = read up to 16 bytes into buf, keeping reading until full or input ends
    if n > 0:
        write the line for (offset, first n bytes of buf)
        offset = offset + n
    if err says "input ended" (either of the two normal kinds): stop, no error
    if err is anything else: stop and return it
```

For the line itself: offset formatted as eight hex digits, two spaces, then 16 columns (a byte's two hex digits and a space, or three spaces if there is no byte for that column), one more space, `|`, the text characters, `|`, newline.

## When the acceptance checker fails

The checker prints the first line that differs, with spaces and special characters visible (`want` is what is expected, `got` is what your program printed). What the message usually means:

| What you see | Likely cause |
|---|---|
| `no output at all` | Nothing is written to standard output, or the program exits before writing. Check that `main` calls your dump function and that you print to `os.Stdout` |
| `line 1 differs` and the hex looks right but the letters differ | Wrong rule for the text column: check the printable range (`0x20` to `0x7e`), and what you print for everything else |
| Hex digits are capital letters | You used `%X` rather than `%x` |
| The offset has the wrong width or case | The offset needs eight lowercase hex digits (`%08x`) |
| `got` is shorter and the last `\|` is too far left | The short last line is not padded: each missing column needs three spaces |
| `output has N lines, expected M (the first lines match)` | Too many or too few lines: look at exactly 16 bytes, at 17, and at empty input. Does the loop stop one round too early or too late? |
| `hint: your output contains a carriage return` | You wrote `\r\n`. Write `\n` only, on every platform |
| `as a file argument` passes but `on standard input` fails | Your `main` ignores standard input when there is no argument |
| `exit status 1, expected 0` | The program reports an error where it should not. Print the error it returns |
| `missing file is an error` fails | A file that cannot be opened must give a message on standard error and a non-zero exit status |

## Still stuck after Level 4

Ask in chat, with the failing message pasted. Opening `examples/spoiler-reference-xd/` is also allowed. If you do, say so in your notes, and expect the evaluation to include a variation you have not seen.
