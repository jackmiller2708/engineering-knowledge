# Model answers: section 8

Compare after you have written your own. Yours may be shorter, longer or differently put. What matters is whether you can say it.

## E1 to E6

**E1. `go.mod`.** It marks the folder as a module root, declares the module's name (`labs`) and the Go version. That name is what makes `labs/hexdump` resolve to the folder `hexdump`. Without it Go treats `labs/hexdump` as a standard-library path and fails: observed, `package labs/hexdump is not in std`.

**E2. A separate package.** Logic in a library package can be imported by tests and by other programs; logic in `main` can only be exercised by running the whole program. It also keeps `main` thin: arguments, opening the file, calling, printing.

**E3. 40 bytes.** Three lines: two full lines of 16, and a last line of 8 bytes. Its offset is 32, written `00000020` (32 is `0x20`).

**E4. Padding.** The `|` and the text must start at the same column on every line, or the dump is hard to read. On a short last line the hex area has fewer bytes, so each missing column is filled with three spaces. In the code this is the 16-column loop that writes spaces when it has no byte.

**E5. Assumptions and what breaks them.** (a) *Eight hex digits for the offset* hold up to 4 GiB. Beyond that `%08x` prints a ninth digit and the columns shift; on a 32-bit system the `int` offset would overflow. (b) *The text column shows ASCII only*: a UTF-8 character such as `é` becomes two dots, so the text column is not a text view of non-English files. Also: a full line is 77 characters wide, which a very narrow terminal will wrap.

**E6. Still wrong?** Several honest answers: both the tests and the checker encode the *same specification*, so a wrong specification passes everything; no test covers a read error in the middle of a file; the tool was only run on one operating system; its behaviour on a huge file (speed, memory) was never measured; an unreadable directory given as the file argument was not tried.

## The change on paper: 8 bytes per line

**What changes in the code:** the number 16 appears in the read buffer size, in the 16-column loop, in the padding logic and anywhere you decide whether a line is full. Offset increases (by bytes actually read) stay the same.
**What changes in the tests:** every expected string, because every line breaks at a different byte; the 40-byte test becomes five lines. The acceptance fixtures also assume 16, so that checker would need a different set of fixtures (or a width option).
**What stays:** the rule for the text column, the offset format, empty-input and error behaviour, and the structure (pure line function plus a loop).
**Design so it is not repeated:** one named constant or, better, a parameter `width` passed to `Dump` and the line function, and the loop and padding written in terms of it. The `-w` flag then just sets that value, using the standard `flag` package.

## The three objections

**O1. "Your tests prove xd works."** They prove it works for the cases written, as I understood the specification. They cannot prove there is no other bug. What gives more confidence: expectations worked out by hand, an independent acceptance check, and listing what is untested.

**O2. "Why not read the whole file?"** Memory would grow with the file, which fails for very large files and cannot work for a never-ending stream such as a pipe. Reading 16 bytes at a time keeps memory constant. A fair concession: reading straight from a file 16 bytes at a time makes many small system calls, so for big inputs wrapping the reader in `bufio.NewReader` would be faster (the reference solution does not do this).

**O3. "`Dump(path string)` would be simpler."** It is simpler for the one caller that has a file, and worse for everything else: no testing with strings, no standard input, and the logic is welded to opening files. Taking an `io.Reader` and adding a thin `DumpFile(path)` on top gives both.
