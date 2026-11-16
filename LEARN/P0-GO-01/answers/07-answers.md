# Answers: section 7

**1. Why not copy the expected string from your program's output?**
That makes the test circular: the program and the "expected" value agree because one came from the other. A bug in the program is copied into the expected side, and the test passes. An expectation derived by hand from the written rules is independent of your code, so a disagreement means one of them is wrong, and that is exactly what a test is for.

**2. What the acceptance checker catches that your tests may not.**
It runs the **whole program**, including `main`, with real standard input and real file arguments, and checks exit statuses and exact bytes (including line endings). Your unit tests of `Dump` do not touch `main` or the command line at all. Its expected outputs were also produced by a separate implementation, so they check your reading of the specification and not only your code.

**3. Why run from the bundle, not from `labs`?**
To catch hidden dependencies: a test that reads a file only your machine has, a missing `go.mod`, a leftover generated file, a helper you forgot to copy. If it passes in the bundle folder, the bundle is self-contained, which is what lets someone else re-run it.

**4. "All four commands exited 0, so xd is correct."**
Exit status 0 says the commands ran without reporting a failure. It does not say what they checked. `go vet` and `go build` say nothing about behaviour, and `go test` only passes what *your tests* check. The claim is missing: what was expected, what was observed, the independent acceptance run, the environment, and what is *not* verified (here, Windows). That is exactly what a manifest records.
