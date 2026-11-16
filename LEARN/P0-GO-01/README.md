# P0-GO-01: Set up Go and ship a tested command-line tool

**Start here.** About 6 hours in 8 sections. By the end you will have a working Go setup and a hex-dump tool, `xd`, that you wrote, tested and can explain.

## Your first step

Open `01-setup.md` and do it. You need nothing else yet.

## Sections

| # | File | You will | Time (estimate) |
|---|---|---|---|
| 1 | `01-setup.md` | Install Go, check it, run a first program | 45 min |
| 2 | `02-modules-packages-programs.md` | Understand modules, packages and programs, and create your `labs` module | 30 min |
| 3 | `03-read-and-run-the-example.md` | Run a small finished tool (`cnt`) and predict what it prints | 30 min |
| 4 | `04-how-the-example-works.md` | See why it is built the way it is | 30 min |
| 5 | `05-change-the-example.md` | Change `cnt` yourself | 45 min |
| 6 | `06-build-xd.md` | Build `xd`, in four milestones | 90 min |
| 7 | `07-test-and-verify.md` | Test it, check it, collect evidence | 45 min |
| 8 | `08-explain-and-defend.md` | Explain it from memory and answer objections | 45 min |

Times are estimates, not measurements. Keep a simple log of your actual time (setup, reading, building, checking) from section 1: you will need the total.

## Get the material

Your own code lives in your own folder. These files live in a clone of the course repository.

**Linux (Zsh) and Windows (PowerShell 7), same commands:**
```
git clone <your repository URL>          # first time only
cd <the cloned folder>
git fetch origin
git switch review/final-curriculum-candidate
git pull
```
`review/final-curriculum-candidate` is the branch this material is on at the time of writing. If you were told to use another branch, use that one. Run `git pull` again whenever you want newer material.

## How to study

- Go in order. Each section says what it is for and when you are done.
- Try every "Check yourself" question before opening `answers/`. Wrong answers are useful: note them, then read the explanation.
- Stuck on `xd`? Use `hints/06-xd-hints.md` one level at a time. Please do not open `examples/spoiler-reference-xd/` until you have finished or are truly stuck.
- Ask for help in chat any time. Nothing here depends on you answering me.

## Completion requirements

You are done when you have all of these. The evaluation then reads them; it may ask follow-up questions, but it does not block your access to anything.

1. `xd` works: `go build`, `go vet` and `go test` pass from a clean copy, and the acceptance checker prints `15 of 15 checks passed`.
2. Your own tests cover: a known 40-byte input compared with an expected string you wrote by hand, empty input, input shorter than 16 bytes, a final partial line, and standard input.
3. An evidence bundle, built as described in section 7.
4. `explanations.md`: your written answers from section 8, written from memory.
5. Your actual hours, and which hints you used (and whether you opened the reference solution).

## What is prepared, and what is not

| Item | Status |
|---|---|
| All 8 sections, hints, answer keys, recall card | Written and complete |
| `examples/cnt` and `examples/greet` | Compile, vet and pass their tests in the author's Linux container (Go 1.24.7). Not run on Windows |
| `examples/accept` (acceptance checker) | Passes against the author's reference solution (15 of 15). Rejected all 12 deliberately broken variants. Not run on Windows |
| Shell commands for Zsh | Run by the author in Zsh 5.9 |
| Shell commands for PowerShell 7 | **Not run by the author** (no PowerShell available). Treat them as untested; tell me if one fails |
| Your setup, your code, your results | **Nothing yet.** Nothing has been run or completed by you |
| Evidence | **None preserved. Nothing independently reproduced** |

## Where things are

```
LEARN/P0-GO-01/
  README.md               this page
  01-… to 08-….md         the sections
  hints/06-xd-hints.md    staged hints for xd
  answers/                answer keys (open after attempting)
  recall/recall-card.md   spaced review, after a week and after a month
  examples/
    cnt/                  the finished example from sections 3 to 5
    greet/                the tiny demo from section 2
    accept/               checks your xd (section 7)
    spoiler-reference-xd/ a complete solution; open last
```
