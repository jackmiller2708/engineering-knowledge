# Answers: section 4

## Trace of `ab  c` (two letters, two spaces, one letter, no newline)

| step | byte | space? | `inWord` before → after | Lines | Words | Bytes |
|---|---|---|---|---|---|---|
| 1 | `a` | no | false → true | 0 | 1 | 1 |
| 2 | `b` | no | true → true (already in a word) | 0 | 1 | 2 |
| 3 | space | yes | true → false | 0 | 1 | 3 |
| 4 | space | yes | false → false | 0 | 1 | 4 |
| 5 | `c` | no | false → true | 0 | 2 | 5 |

Result: 0 lines, 2 words, 5 bytes (observed by running it). A word is counted when it **starts**: steps 1 and 5. Step 2 is inside a word that was already counted. Step 4 shows that several spaces in a row do not create extra words.

## Check yourself

**1. `Count(r io.Reader)` rather than `Count(path string)`.**
With a path, (a) every test would need a real file created and cleaned up on disk; (b) it could not read standard input at all; (c) it could not be tested with a plain string, and you could not simulate a failing read. With a reader, the same function serves files, standard input and in-memory strings.

**3. `defer f.Close()` and the two `os.Exit(1)` calls.**
`defer` schedules `f.Close()` to run when the function returns. The **first** `os.Exit(1)` is before the `defer` line: the file failed to open, so there is nothing to close. The **second**, after a read error, is after it and **skips the deferred call**, because `os.Exit` ends the program immediately. It does not matter here, because the operating system closes the file when the program ends. In a long-running program it could leak a file.

**4. Table test versus three separate functions.**
A fair answer has both sides. The table makes a new case one line, runs every case through the same checks, and names each failing row. Separate functions are clearer when each case needs a different setup or a different kind of check. Here every case has the same shape (input, expected result), so the table fits.
