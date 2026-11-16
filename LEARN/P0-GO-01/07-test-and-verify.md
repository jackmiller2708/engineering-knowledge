# Section 7 of 8: Test it, check it, collect the evidence

**Time:** about 45 minutes. **Goal:** `xd` is checked in three independent ways, and you have an evidence bundle that someone without your computer could re-run.

## Why this matters

"It works on my machine" is a claim, not evidence. Evidence is a record of exactly what was run, what was expected, and what happened, with enough detail for another person to repeat it. This section builds that habit on a small tool, where it is cheap. The same bundle format is used for every unlock in the course.

Three checks, each catching what the others miss:

```
 your own tests         ──► do the pieces behave as YOU specified?      (you wrote both sides)
 the acceptance checker ──► does the whole program match the SPEC?      (someone else wrote the answers)
 a clean copy           ──► does it work without your leftover files?   (nothing hidden on your machine)
```

## Part 1: write your own tests (about 15 minutes)

In `hexdump/hexdump_test.go`, using a table like the one in `cnt`. Cover:

| Case | Input | What it proves |
|---|---|---|
| Known 40 bytes | `"Hello, Go!\nbytes: \x00\x01\xff\n0123456789ABCDEFGH"` | Two full lines, then a short last line of 8 bytes |
| Empty | `""` | Prints nothing |
| Shorter than 16 | one or a few bytes | Short line, padding |
| Exactly 16 | 16 bytes | One full line, **no** extra line after it |
| 17 | 17 bytes | A second line holding one byte |

**Write each expected string by hand from the specification. Never run your program and paste its output into the test.** If you do, the test only proves that your program agrees with itself, so a bug is copied into the "expected" side and the test passes. Tip: write the expected text as several string pieces joined with `+`, one per line.

Standard input: `Dump` reads from an `io.Reader`, and `strings.NewReader` is a reader just like standard input, so the same code path is covered. The acceptance checker in Part 3 also feeds real standard input.

## Part 2: build the bundle in a clean place (about 15 minutes)

The bundle holds only the files needed to re-run the checks, in a new folder inside your clone of the course repository. Working there also **is** the clean-copy check: nothing from your working folder can leak in.

`<CLONE>` is the folder where you cloned the course repository. `<LABS>` is your own `labs` folder.

**Linux (Zsh), primary:**
```
BUNDLE=<CLONE>/EVIDENCE/P0-GO-01/$(date +%F)-1
mkdir -p $BUNDLE/artifacts/cmd
cd <LABS>
cp go.mod README.md $BUNDLE/artifacts/
cp -r hexdump $BUNDLE/artifacts/
cp -r cmd/xd $BUNDLE/artifacts/cmd/
```
**Windows (PowerShell 7), secondary. Not run by the author:**
```
$bundle = "<CLONE>\EVIDENCE\P0-GO-01\$(Get-Date -Format yyyy-MM-dd)-1"
New-Item -ItemType Directory -Force "$bundle\artifacts\cmd" | Out-Null
Set-Location <LABS>
Copy-Item go.mod, README.md "$bundle\artifacts\"
Copy-Item -Recurse hexdump "$bundle\artifacts\"
Copy-Item -Recurse cmd\xd "$bundle\artifacts\cmd\"
```
You need a short `README.md` in `<LABS>` first: what the tool is, how to build it, how to run it, and the layout it prints (a few lines). The bundle must hold your source and tests, **not** build output and not the `cnt` or `greet` folders.

Then, from inside the bundle's `artifacts` folder, run these four commands and note each one's output and **exit status** (0 means success):

| # | Command | Expected |
|---|---|---|
| 1 | `gofmt -l .` | no output |
| 2 | `go vet ./...` | no output |
| 3 | `go test ./...` | an `ok` line for `labs/hexdump`, and `[no test files]` for `labs/cmd/xd` |
| 4 | `go build ./...` | no output |

Reading the exit status: **Zsh:** run `echo $?` straight after the command. **PowerShell:** `$LASTEXITCODE` (not run by the author). `gofmt -l` prints names of files that are *not* formatted; empty output means all are.

## Part 3: the acceptance checker (about 5 minutes)

The checker runs your `xd` on seven fixtures, once as a file argument and once on standard input, compares the output to the expected text byte for byte, and checks the missing-file behaviour. It never reads your source.

**Linux (Zsh):**
```
XD="$(mktemp -d)/xd"
(cd $BUNDLE/artifacts && go build -o "$XD" ./cmd/xd)
(cd <CLONE>/LEARN/P0-GO-01/examples/accept && go run . -xd "$XD")
```
**Windows (PowerShell 7), not run by the author:**
```
$xd = Join-Path $env:TEMP "xd.exe"
Push-Location "$bundle\artifacts"; go build -o $xd .\cmd\xd; Pop-Location
Push-Location <CLONE>\LEARN\P0-GO-01\examples\accept; go run . -xd $xd; Pop-Location
```
A correct `xd` ends with `15 of 15 checks passed`. A failure prints the first line that differs, with spaces and special characters made visible. `hints/06-xd-hints.md` has a table that turns each message into the likely cause.

## Part 4: write the manifest (about 10 minutes)

Copy `TEMPLATES/MANIFEST.md` to `manifest.md` in the bundle folder (next to `artifacts/`) and fill it in. For this unlock:

| Field | What to write |
|---|---|
| `unlock` | `P0-GO-01` |
| `capability` | One sentence, for example: "A hex-dump command, `xd`, that follows the written layout, with its own tests, passes vet, test and build from a clean copy and passes the acceptance checker." |
| `evidence_kind` | `preserved`. It means you captured this from your own run. It becomes `independently-reproduced` only if someone else re-runs it from the bundle |
| `implementation_attempt` | `1` |
| `provenance` | Where the work came from, **without machine paths**, for example: "PRJ-LABS, folder `labs` on the learner's Linux machine; no version control." |
| `reproduced_by` | `n/a` |
| Environment | `- os:` your system, `- arch:` your processor, `- toolchain:` the line from `go version`, and the Zsh or PowerShell version if you like |
| Setup | "Go 1.22 or newer installed. The acceptance checker from the course repository at `LEARN/P0-GO-01/examples/accept`. No other dependencies." |
| Artifacts | One row per file in `artifacts/`: path relative to `artifacts/`, its SHA-256, a role (`code`, `test`, `doc`, `config`), a short description |
| Commands | The four commands above plus the acceptance run, each with: working directory, what you expected, what you observed, exit status |
| Limitations | Be specific, for example "run on Linux only; not tried on Windows". "None known" is rarely true |

Getting a SHA-256 (the manifest needs it in **lowercase**):

**Zsh:** `sha256sum <file>` (the long hex string is the first column).
**PowerShell 7, not run by the author:** `(Get-FileHash -Algorithm SHA256 <file>).Hash.ToLower()`

Also copy `TEMPLATES/EVALUATION.md` into the bundle folder as `evaluation.md`, and set two lines so the repository checker accepts it for now: `**Result:** not yet` and `**Mastery shown:** L0`. The evaluator replaces them. Put your `explanations.md` from section 8 in the bundle folder too.

## Part 5: check the bundle's shape, then hand it over

In your clone of the course repository:

**Linux (Zsh):** `python3 tools/check_course.py`
**Windows (PowerShell 7), not run by the author:** `py -3 tools\check_course.py` (or `python`)

It should end with `RESULT: OK`. It checks that the files exist, that every artifact is listed, and that the hashes match. **It does not run your commands**, so `OK` does not mean your tool works; Parts 1 to 3 do that.

To hand it over, commit the bundle folder on a branch of your own and push it, then tell me the branch name. Or paste the contents into chat. I will read it and re-run your commands on Linux. If the results match, the bundle is recorded as independently reproduced; otherwise it stays `preserved`, and I will tell you what differed.

## Check yourself

Try these before opening `answers/07-answers.md`.

1. Why must the expected string in your test not be copied from your own program's output?
2. What can the acceptance checker catch that your own tests might not?
3. Why run the commands from the bundle folder rather than from `labs`?
4. A teammate says: "all four commands exited 0, so xd is correct." What is missing from that claim?

## Done when

- [ ] Your tests cover the five cases and pass.
- [ ] The four commands succeed from the bundle's `artifacts` folder.
- [ ] The acceptance checker prints `15 of 15 checks passed`.
- [ ] `manifest.md` is filled in, hashes included, and `python3 tools/check_course.py` ends in `RESULT: OK`.

**Next:** `08-explain-and-defend.md`. **Answers:** `answers/07-answers.md` (after you try).
