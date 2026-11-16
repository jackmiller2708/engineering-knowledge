# Section 3 of 8: Read and run a finished example

**Time:** about 30 minutes. **Goal:** you have a small, finished Go tool running on your machine, and you have tested your own picture of how it behaves.

## Why this comes first

Your real task in this unit, `xd`, reads bytes from a file or from standard input and prints them. Before you write that, you will work with a finished tool of the same shape that solves a *different* problem. Reading working code, running it, and being surprised by it is the quickest way to build an accurate picture.

## What `cnt` does

`cnt` counts **lines, words and bytes** in a file, or in whatever is sent to it on *standard input* (the stream of text a program reads when you pipe text into it or type at it).

- A *line* is counted for every newline character (`\n`).
- A *word* is a run of characters with no whitespace in it.
- A *byte* is one byte of the input. Text is stored as bytes; an English letter is one byte, but some characters take more.

## The files

Create this layout inside your `labs` module from section 2 (type it rather than pasting where you can, since typing makes you read each line). A finished copy is in `examples/cnt/`.

```
labs/
  go.mod
  cmd/cnt/main.go
  count/count.go
  count/count_test.go
```

`count/count.go`
```go
// Package count measures a stream of bytes.
package count

import (
	"bufio"
	"io"
)

// Result holds what Count measured.
type Result struct {
	Lines int
	Words int
	Bytes int
}

// isSpace reports whether b separates words. Only ASCII whitespace counts.
func isSpace(b byte) bool {
	return b == ' ' || b == '\n' || b == '\t' || b == '\r' || b == '\v' || b == '\f'
}

// Count reads r to the end and reports how many lines, words and bytes it held.
func Count(r io.Reader) (Result, error) {
	var res Result
	br := bufio.NewReader(r)
	inWord := false
	for {
		b, err := br.ReadByte()
		if err == io.EOF { // EOF = end of file: nothing left to read
			break
		}
		if err != nil {
			return res, err
		}
		res.Bytes++
		if b == '\n' {
			res.Lines++
		}
		if isSpace(b) {
			inWord = false
		} else if !inWord {
			inWord = true
			res.Words++
		}
	}
	return res, nil
}
```

`count/count_test.go`
```go
package count

import (
	"strings"
	"testing"
)

func TestCount(t *testing.T) {
	tests := []struct {
		name string
		in   string
		want Result
	}{
		{"empty", "", Result{0, 0, 0}},
		{"one word, no newline", "hello", Result{0, 1, 5}},
		{"two lines", "a b\nc\n", Result{2, 3, 6}},
		{"windows line endings", "a\r\nb\r\n", Result{2, 2, 6}},
		{"several spaces", "a   b", Result{0, 2, 5}},
		{"accented letter is one word", "caf\xc3\xa9\n", Result{1, 1, 6}},
	}
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			got, err := Count(strings.NewReader(tc.in))
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if got != tc.want {
				t.Errorf("Count(%q) = %+v, want %+v", tc.in, got, tc.want)
			}
		})
	}
}
```

`cmd/cnt/main.go`
```go
package main

import (
	"fmt"
	"os"

	"labs/count"
)

func main() {
	in := os.Stdin
	if len(os.Args) > 1 {
		f, err := os.Open(os.Args[1])
		if err != nil {
			fmt.Fprintln(os.Stderr, "cnt:", err)
			os.Exit(1)
		}
		defer f.Close()
		in = f
	}
	res, err := count.Count(in)
	if err != nil {
		fmt.Fprintln(os.Stderr, "cnt:", err)
		os.Exit(1)
	}
	fmt.Printf("%d lines, %d words, %d bytes\n", res.Lines, res.Words, res.Bytes)
}
```

## Do this

### 1. Check it builds and passes

From the `labs` folder:
```
gofmt -l .
go vet ./...
go test ./...
go build ./...
```
`gofmt -l .` lists files that are not formatted the standard way (nothing printed means all fine). `go vet` looks for suspicious code (nothing printed means happy). **Observed by the author:** `go test ./...` prints `ok  labs/count` and a line saying `labs/cmd/cnt` has no test files.

### 2. Make three input files

Do this in a scratch folder, not inside `labs`. The first has three lines, each ending in a newline. The second has the **same text** but with Windows line endings (each line ends with two bytes, `\r\n`). The third contains the word "café" followed by " au lait" and a newline.

**Linux (Zsh), primary. Run by the author:**
```
printf 'the quick brown fox\njumps over\nthe lazy dog\n' > notes.txt
printf 'the quick brown fox\r\njumps over\r\nthe lazy dog\r\n' > notes-crlf.txt
printf 'caf\xc3\xa9 au lait\n' > accent.txt
```
**Windows (PowerShell 7), secondary. Not run by the author.** These write the exact bytes shown, with no extra line ending added:
```
[IO.File]::WriteAllText("notes.txt", "the quick brown fox`njumps over`nthe lazy dog`n")
[IO.File]::WriteAllText("notes-crlf.txt", "the quick brown fox`r`njumps over`r`nthe lazy dog`r`n")
[IO.File]::WriteAllText("accent.txt", "caf$([char]0xE9) au lait`n")
```
(In PowerShell, `` `n `` is a newline and `` `r `` a carriage return. Plain `Set-Content` is avoided on purpose: on Windows it adds its own line endings and would change your numbers.)

### 3. Predict first

**Before running anything below, write your guesses down.** A guess you can compare with reality teaches you more than a result you only read.

| # | Command | Your prediction (lines, words, bytes) | What actually printed | If different: why? |
|---|---|---|---|---|
| 1 | `cnt notes.txt` | | | |
| 2 | `cnt notes-crlf.txt` (which numbers change, and by how much?) | | | |
| 3 | `cnt accent.txt` (is it 13 bytes or 14, and why?) | | | |

Hint for 3 only: the letter `é` is stored as two bytes in UTF-8, written `\xc3\xa9`.

### 4. Run them

From `labs`, pass the path of each file (adjust the path to where you made them):
```
go run ./cmd/cnt notes.txt
go run ./cmd/cnt notes-crlf.txt
go run ./cmd/cnt accent.txt
```
Fill in the "what actually printed" column. For any mismatch, work out why **before** opening the answers.

### 5. Standard input, two ways

First, send text through a pipe. **Linux (Zsh):**
```
printf 'a b\nc\n' | go run ./cmd/cnt
```
**Windows (PowerShell 7), not run by the author:** `"a b`nc`n" | go run ./cmd/cnt` (PowerShell may add its own line ending to piped text, so the byte count may differ from Linux; that is a thing to explain, not a bug to fix).

Then run it with **no arguments and no pipe**, and type a couple of lines yourself. Nothing seems to happen until you tell the program the input has ended: press **Ctrl-D** on Linux, or **Ctrl-Z then Enter** on Windows (not run by the author). Predict what you will see first.

### 6. A missing file

```
go run ./cmd/cnt does-not-exist.txt
```
**Observed by the author:** a message of the shape `cnt: open does-not-exist.txt: no such file or directory`, then `exit status 1` (printed by `go run`).

## Check yourself

Try these before opening `answers/03-answers.md`.

1. For each of the three predictions that was wrong, what was your mistaken assumption?
2. When you typed text with no pipe, why did nothing print until Ctrl-D (or Ctrl-Z)?
3. `printf 'no newline at the end' | go run ./cmd/cnt` prints `0 lines`. Why, when there is clearly one line of text?

## Done when

- [ ] The tests pass on your machine.
- [ ] Your prediction table is filled in, including the "why" for every mismatch.
- [ ] You ran the standard-input forms and the missing-file case.

**Next:** `04-how-the-example-works.md`. **Answers:** `answers/03-answers.md` (after you try).
