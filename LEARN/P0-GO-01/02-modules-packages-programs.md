# Section 2 of 8: Modules, packages and programs

**Time:** about 30 minutes. **Goal:** you can say what a module, a package and a program are, and you have created your `labs` module.

## Why now

`hello.go` was one file. Real tools have many files, and Go needs a way to know which files belong together and how they refer to each other. Three ideas do all of that. After this section the folder structure of the rest of the unit will make sense instead of being a thing to copy.

## The picture

```
labs/                      ← the MODULE: the folder that holds go.mod
├── go.mod                 ← says "this module is called labs"
├── greet/                 ← a PACKAGE: one folder of .go files, a library
│   └── greet.go             (package greet)
└── cmd/
    └── hello/             ← a PACKAGE that is a PROGRAM
        └── main.go          (package main, with func main)
```

- A **module** is a folder with a `go.mod` file at its top. The file holds the module's name.
- A **package** is a folder of `.go` files that start with the same `package` line. A package's *import path* is the module name plus the folder path: the file in `labs/greet/` is imported as `"labs/greet"`.
- A package called **`main`** that contains `func main()` is a **program**: running it starts at `main`. Every other package is a **library** that programs and other packages import.
- A name that starts with a **capital letter** (`Hello`) can be used from other packages. A lowercase name (`hello`) is private to its own package.

One more fact you will see: `go mod init labs` writes `go.mod`. It contains a line `module labs` and a line `go 1.xx` showing the Go version you have installed. That second line is normal and will differ from other people's.

## Do this

### 1. Create the module and the two packages

In your `labs` folder:
```
go mod init labs
```
Then create these two files (any editor), with these folders:

`greet/greet.go`
```go
// Package greet builds greetings.
package greet

// Hello returns a greeting for name. The capital H makes it visible to other packages.
func Hello(name string) string {
	return "Hello, " + name + "!"
}
```

`cmd/hello/main.go`
```go
package main

import (
	"fmt"

	"labs/greet"
)

func main() {
	fmt.Println(greet.Hello("Go"))
}
```

Run it from the `labs` folder:
```
go run ./cmd/hello
```
`./cmd/hello` means "the package in that folder". **Observed by the author:** it prints `Hello, Go!`. A finished copy of both files is in `examples/greet/` for comparison.

### 2. Two experiments (change one thing, predict, then see)

For each one, **write down what you expect first**, then try it, then undo it.

- **Experiment A.** In `greet/greet.go`, rename `Hello` to `hello` (lowercase), and run `go run ./cmd/hello`.
- **Experiment B.** In `cmd/hello/main.go`, change the import to `"labs/grete"` (a typo), and run it again.

**Observed by the author (Go 1.24.7):** A gives `undefined: greet.Hello`; B gives a message beginning `package labs/grete is not in std`, followed by a path from the author's machine. Your wording may differ slightly with another Go version.

## Check yourself

Try these before opening `answers/02-answers.md`.

1. What decides the text you write in an `import` line, such as `"labs/greet"`?
2. Why did experiment A fail, and what does that tell you about the capital letter?
3. What makes a package a *program* rather than a library?
4. You have two folders, `labs/a/` and `labs/b/`, each with `.go` files. How many modules and how many packages is that?

## Done when

- [ ] `go run ./cmd/hello` prints `Hello, Go!`.
- [ ] You tried both experiments and undid them.
- [ ] You can explain module, package and program in your own words, without looking.

**Next:** `03-read-and-run-the-example.md`. **Answers:** `answers/02-answers.md` (after you try).
