# Answers: section 3

Your own wrong guesses are the useful part. Compare the numbers, then read why.

## The three predictions

| # | File | Result (observed by the author) |
|---|---|---|
| 1 | `notes.txt` | `3 lines, 9 words, 44 bytes` |
| 2 | `notes-crlf.txt` | `3 lines, 9 words, 47 bytes` |
| 3 | `accent.txt` | `1 lines, 3 words, 14 bytes` |

**1.** Bytes: the first line is 19 characters plus its newline (20), the second 10 plus one (11), the third 12 plus one (13): 44. The newline is a byte too; forgetting it gives 41. Words: 4 + 2 + 3 = 9.

**2.** Only the **bytes** change, by +3: each line gained one extra byte (the carriage return). The line count still counts newline characters (`\n`), so it stays 3. The words stay 9 because the carriage return is whitespace, so it separates words and never forms one.

**3.** 14 bytes, not 13. The letter `é` is stored as two bytes in UTF-8 (`c3 a9`), so the text "café au lait" plus a newline is 3 + 2 + 1 + 2 + 1 + 4 + 1 = 14. `cnt` counts *bytes*, not characters, which is exactly what the `é` row in the test table documents. Words stay 3: the two bytes of `é` are not ASCII whitespace. (This is also why `isSpace` checks ASCII whitespace only. Treating each byte as a character would misread some accented letters, because the byte `a0` is a space in Unicode.)

## Check yourself

**2. Why did nothing print until Ctrl-D (or Ctrl-Z)?**
`Count` reads until the input *ends*. A terminal keeps standard input open and waiting for more text until you signal the end: Ctrl-D on Linux, Ctrl-Z then Enter on Windows. Until then `ReadByte` waits for the next byte. A pipe or a file ends by itself when the data runs out, so those finish immediately.

**3. Why `0 lines` for text with no newline?**
`cnt` counts newline characters, not "pieces of text that look like lines". `printf 'no newline at the end' | go run ./cmd/cnt` printed `0 lines, 5 words, 21 bytes` (observed). This is the same rule the standard `wc -l` tool follows, and it is why a file without a final newline looks one line short. In section 5 you will meet the other side of this: the *last line* without a newline still has a length.
