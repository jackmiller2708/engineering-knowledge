# Section 5 of 8: Change the example yourself

**Time:** about 45 minutes. **Goal:** you extend `cnt` without a solution to copy, and you keep its tests honest while you do it.

## Why this matters

Reading working code is not the same as changing it safely. Almost all real programming is changing code that already works without breaking it. This section has three parts, and each gives you less help than the one before.

## Part A (about 25 minutes, guided): add "longest line"

`cnt` should also report the **length of the longest line**, in bytes, not counting the newline. A last line that has no newline at the end still counts.

### A1. Know the answers before you write the code

| Input (as text) | Expected longest line |
|---|---|
| (empty) | 0 |
| `abc` | 3 |
| `ab`, newline, `cde`, newline, `f`, newline | 3 |
| two newlines only | 0 |
| `a`, CR LF, `bcd`, CR LF | 4 (for now, the carriage return counts as part of the line) |

### A2. Write the tests first

1. Add a field `LongestLine int` to `Result` in `count/count.go`.
2. Add the five rows above to the test table. Give them the other three numbers (lines, words, bytes) too, worked out **by hand**.
3. Run `go test ./...`.

You will not see a neat failing test. You will see **compile errors** about your old rows. Adding a field changes every place that builds a `Result` by listing its values in order. The compiler is telling you which rows to update. Update each old row with the right `LongestLine`, **worked out from the definition above, not by running your code and copying what it prints**.

### A3. Make the tests pass

`Count` needs one more piece of state: something that tracks the line it is in the middle of. Decide where it changes and where it resets. Then run the tests until they pass.

### A4. Show it

Change `main.go` to print the new number too. For the input `ab`, newline, `cde`, newline, `f`, newline, a correct program prints a line like `3 lines, 3 words, 9 bytes, longest line 3` (the wording around the numbers is yours to choose).

## Part B (about 12 minutes, described only): a decision changes the tests

Files from Windows end each line with two bytes, CR then LF. Decide that **the carriage return must not count toward the line's length**. Change the code and the tests.

Before you edit anything, write down: **which existing test rows will have to change, and why?** Then edit, and see whether your list was right.

## Part C (about 8 minutes): prove your tests can fail

A test that cannot fail proves nothing. Temporarily remove the part of your code that handles a last line with no newline. Run the tests.

- Which rows fail?
- Do they fail for the reason you expected?

Put the code back and confirm everything passes again.

## Check yourself

Try these before opening `answers/05-answers.md`.

1. Which old rows needed a new number in A2, and how did you decide each one?
2. In Part B, which rows changed? Was your list correct before you edited?
3. What did Part C show you about which tests protect which behaviour?

## Done when

- [ ] All tests pass, and the program prints the longest line.
- [ ] You worked out expected values by hand rather than copying program output.
- [ ] You ran Part C and restored the code.
- [ ] Your list for Part B was written before you edited.

**Next:** `06-build-xd.md`. **Answers:** `answers/05-answers.md` (after you try).
