# Recall answers: P0-GO-01

Write yours from memory first, one week and one month after finishing. Then compare.

1. **`go.mod`** marks a module's root and holds its name and Go version. The name is the first part of every import path inside the module.
2. **Module, package, program.** A module is a folder with `go.mod`. A package is a folder of `.go` files with the same `package` name. A program is a package named `main` with `func main()`.
3. **Capital letters.** A name starting with a capital letter is visible to other packages; a lowercase name is private to its own package.
4. **`io.Reader`** is anything you can read bytes from: a file, standard input, a string reader. A function that takes one works with all of them and is easy to test.
5. **A word starts** at a non-space byte when the previous byte was a space (or there was no previous byte).
6. **`if err != nil`** handles a failure at the place it can happen. `io.EOF` is not a failure: it means the input has ended.
7. **Adding a struct field** breaks code that builds the struct by listing its values in order, and the compiler lists each place (`too few values in struct literal`). Fix them by giving the new value, derived from the specification.
8. **Expected values** are worked out by hand from the written rules, not copied from the program's output, so the test is independent of the code.
9. **`io.ReadFull`** returns `io.EOF` when it read nothing and `io.ErrUnexpectedEOF` when it read some bytes but fewer than the buffer; both are normal ends of input.
10. **The acceptance check** proves the whole program (including `main`, standard input and exit status) matches the specification. Unit tests of one function do not. Neither proves the specification itself is right, or that it works on an operating system it was not run on.

**Variation.** To count *characters* instead of bytes, `Count` can no longer treat each byte as a unit: it must decode UTF-8 (for example by reading runes with `bufio.Reader.ReadRune`), the `é` row's expected byte count stays 6 but its character count is 5, and `isSpace` could use Unicode whitespace. The structure (a loop over a reader, a result struct, a table test) is unchanged.
