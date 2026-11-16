# Section 8 of 8: Explain it, vary it, defend it

**Time:** about 45 minutes. **Goal:** show, from memory, that you understand what you built, not just that it passes.

## Why this matters

Passing a checker proves the program matches a spec. It does not prove *you* can reason about it. The test of understanding is whether you can explain why it works, say where it would break, and change it when the requirements change. This section has you write that down, from memory, once.

## Part 1: explain it from memory (about 20 minutes)

**Close your code, your notes and this course.** In a new file `explanations.md`, answer each question in your own words, two to five sentences each. If you cannot answer one, **leave it blank or write "I don't know"**. A blank tells us exactly what to revisit; a guess copied from somewhere hides it.

- **E1.** What does `go.mod` do, and what would happen to `import "labs/hexdump"` without it?
- **E2.** Why does the dump logic live in its own package instead of in `main`?
- **E3.** Walk through what `Dump` does with a 40-byte input: how many lines, how many bytes in the last one, and what is its offset?
- **E4.** Why does a short last line need padding, and which part of your code does it?
- **E5.** Name two assumptions `xd` makes, and for each, an input that would break it. (Think about the offset column and the text column.)
- **E6.** All your tests and the acceptance checker pass. Name one thing that could still be wrong.

Only now may you check yourself against `answers/08-answers.md`. Put the **gaps** (what you got wrong or left blank) at the end of your file, plainly.

## Part 2: a change you have not built (about 15 minutes)

A colleague asks for **8 bytes per line** instead of 16, selectable with an option `-w 8`.

On paper, in `explanations.md` (writing code is optional):

1. List every place in **your code** that would change.
2. List every test that would change, and say why.
3. List what stays the same.
4. How would you arrange the code so the width is not repeated in many places?

This is a variation of what you built, not a copy of it. Doing it well means your design is understood, not memorised.

## Part 3: defend it (about 10 minutes)

Write a short reply (three or four sentences) to each objection:

- **O1.** "Your tests prove `xd` works."
- **O2.** "Reading 16 bytes at a time is slower than reading the whole file at once. Why not read it all?"
- **O3.** "`Dump(path string)` would be simpler than taking an `io.Reader`."

A good reply names what is true in the objection and then says what it misses.

## Part 4: set up your spaced review

`recall/recall-card.md` has ten short questions across this whole unit. Answer them **from memory about a week from now, and again about a month from now**. Put both dates in your calendar today. Each time should take about ten minutes and is part of this unit's study time, not extra. The answers are in `answers/recall-answers.md`; check them only after you have written yours.

## Finish: what to hand over

Put these in your bundle folder from section 7 (next to `manifest.md`):

1. `explanations.md`: Parts 1 to 3, including your gaps.
2. A short note at the end of `explanations.md`: your **actual hours** (setup, reading, building, checking), **which hint levels you used**, and **whether you opened the reference solution** before finishing.

Then tell me the bundle is ready (section 7, Part 5). I will evaluate it, re-run your commands on Linux, and may ask follow-up questions about your answers. What gets recorded is what you demonstrated.

## Done when

- [ ] `explanations.md` has E1 to E6, the change on paper, and the three replies, with your gaps listed.
- [ ] Your hours, hint levels and reference-solution note are written down.
- [ ] Your two recall dates are in your calendar.

**Answers:** `answers/08-answers.md` (after you write yours).
