# Section 1 of 8: Set up Go and check that it works

**Time:** about 45 minutes. **Goal:** `go version` works in your terminal, you have a folder for your own code, and you have run one Go program.

## Why this comes first

Everything in this course after today is Go. If the setup is slightly wrong, the errors later look like code problems. So we prove the tools work with the smallest possible program before writing anything real.

## A picture of what you are installing

```
   you write          the Go tool                    you get
  hello.go  ──────►   go run / go build   ──────►   a running program
  (text)              (compiler + helpers)           (machine code)
```

Go is a *compiler*: it turns your text files into a program the computer can run directly. The `go` command is the one entry point to all of it. When you type `go` in a terminal, the system looks through the folders listed in a setting called `PATH` for a program named `go`. If Go's folder is not on `PATH`, the terminal says it cannot find the command. Most setup problems are exactly this.

## Do this

### 1. Make a folder for your own code

Your code does **not** go in the course repository (it holds plans, not your work). Choose any folder you like and call it `labs`.

**Linux (Zsh), primary:**
```
mkdir -p ~/labs
cd ~/labs
```
**Windows (PowerShell 7), secondary. Not run by the author:**
```
mkdir $HOME\labs
cd $HOME\labs
```

### 2. Install Go

Follow the official instructions at **go.dev/doc/install**. They change over time, so use that page, not a copy. You need Go **1.22 or newer**; the latest stable release is fine.

What to expect, as a guide (check the page):
- **Linux:** a downloaded archive is unpacked into `/usr/local`, and `/usr/local/go/bin` is added to `PATH` (in Zsh, a line in `~/.zshrc`). Any distribution works. A package from your distribution is fine too, if its version is 1.22 or newer.
- **Windows:** the official installer adds Go to `PATH` for you.
- In both cases, **open a new terminal window afterwards.** An already-open terminal keeps the old `PATH`.

### 3. Check it

```
go version
git --version
go env GOROOT GOOS GOARCH
```
`go version` prints one line of the shape `go version go1.xx.x linux/amd64` (your numbers and system will differ). `go env GOROOT GOOS GOARCH` prints three lines: where Go is installed, your operating system, and your processor type.

If `go` is "not found" or "not recognized", go to **If something goes wrong** below.

### 4. Run your first program

Make a throwaway folder, outside `labs`, and create a file named `hello.go` with exactly this:

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello from Go")
}
```

Then run it two ways:
```
go run hello.go
go build hello.go
```
`go run` compiles and runs in one step, leaving nothing behind. `go build` leaves a program file in the folder. Look at the folder afterwards.

**Observed by the author (Linux, Go 1.24.7):** `go run hello.go` prints `Hello from Go`; after `go build hello.go` the folder contains `hello` and `hello.go`. On Windows the built file is expected to be named `hello.exe` (not run by the author).

### 5. Start your time log

Open any text file and note the time you started. For the whole unit, keep four running totals: **setup / reading / building / checking**. You will report the total in section 7, and it feeds the plan's time estimates.

## If something goes wrong

| Symptom | Likely cause | What to do |
|---|---|---|
| `command not found: go` (Zsh) or `go is not recognized` (PowerShell) | Go's folder is not on `PATH`, or the terminal was opened before installing | Open a new terminal. Check `PATH` (`echo $PATH` in Zsh, `$env:PATH` in PowerShell) for the Go `bin` folder. Re-read the install page's PATH step |
| `go version` shows a version older than 1.22 | An older Go (for example from a distribution package) comes first on `PATH` | `which -a go` (Zsh) or `where.exe go` (PowerShell) lists every `go`; remove or reorder the old one |
| Anything else | | Paste the full command and its full output in chat, and say you are in section 1 |

## Check yourself

Try these before opening `answers/01-answers.md`.

1. Why do you need a new terminal after installing Go?
2. After `go run hello.go` and `go build hello.go`, what is different about the folder, and why?
3. Which Go version do you have? Is it 1.22 or newer?

## Done when

- [ ] `go version` prints a version of 1.22 or newer.
- [ ] You ran `hello.go` with `go run` and with `go build`.
- [ ] You have a `labs` folder and a time log with section 1 filled in.

**Next:** `02-modules-packages-programs.md`. **Answers:** `answers/01-answers.md` (after you try).
