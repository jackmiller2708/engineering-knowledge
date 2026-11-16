# Template: learning material for one unlock (`LEARN/<ID>/`)

The complete material is written **before** the learner is asked to begin the unlock. The learner studies at their own pace; nothing in it waits on a chat reply. The unlock file (`UNLOCKS/<ID>.md`) says *what* must be achieved; this folder is *how* the learner gets there. Stay inside the unlock's frozen boundaries (`UNLOCKS/README.md`).

## Folder

```
LEARN/<ID>/
  README.md             Start here (required parts below)
  01-<name>.md ...      ordered sections, numbered without gaps
  hints/                staged hints for the main exercise, small to large
  answers/              NN-answers.md per section, plus recall answers; kept apart
  recall/               a card for spaced review (about a week and a month later)
  examples/<name>/      runnable teaching code; the only place code may live in this repository
```

## `README.md` must contain

1. **Start here**: the exact first step.
2. A table of sections with a time estimate each (estimates, not measurements; they sum to the unlock's hours in `UNLOCKS/CATALOG.md`).
3. **Get the material**: how to pull it.
4. **Completion requirements**: the list the evaluation will read.
5. **What is prepared, and what is not**: a table that separates work the author did and verified (and where: operating system, tool versions) from work the learner must do, from evidence. Never claim the learner installed, ran or finished anything. Say which platform each command was run on. State "Nothing has been run or completed by you" until it is true. No bundle is "independently reproduced" until its commands have been re-run.
6. A map of where things are.

## Each section

```
# Section N of M: <title>
**Time:** about X minutes. **Goal:** one sentence.
## Why this matters         (the problem; where it lands in PRJ-ENGINE)
## <the picture / mechanism> (concrete example, diagram or numbers first; then the real rules)
## Do this                  (numbered steps; Linux (Zsh) first, Windows (PowerShell 7) second, labelled)
## Check yourself           (questions to attempt before opening answers/)
## Done when                (checklist; required by the checker)
Next: ... Answers: answers/NN-answers.md (after you try)
```

## Rules

- **Order of the whole unit:** problem; picture; mechanism; a worked example on a *neighbouring* problem (never the unit's own challenge); the learner reconstructs or changes it; then the independent challenge, with less guidance each step; then an explanation from memory and one variation the learner has not seen. Do not name these steps to the learner.
- **Change the representation, not the vocabulary** when something is hard to picture.
- **Questions inside, answers apart.** Never put an answer in the section that asks.
- **The main challenge's solution** is never in the reading flow. Provide a hint ladder and, if useful, a clearly labelled spoiler kept apart, and have the learner record whether they opened it.
- **Verify before publishing.** Run every example and every command you can in the cloud environment, say where you ran it, and quote output only as "observed". Cross-check expected outputs with an independent method. Lesson code blocks must be identical to their example files (the checker enforces this for blocks introduced by a `path` line).
- **Expected values for the learner's tests come from the specification, not from running the learner's program.**
- **Recall and review live inside the material** and inside the unlock's existing hours. No separate workload.
- **No machine paths, no personal data.** Use placeholders such as `<CLONE>` and `<LABS>`.
