# Answers: section 2

**1. What decides the text in an `import` line?**
The module name (from `go.mod`: `module labs`) plus the folder path inside the module. The package in `labs/greet/` is imported as `"labs/greet"`. The name does not come from the file's name or from the `package` line.

**2. Why did experiment A fail?**
After the rename there is no name `Hello` any more, so `greet.Hello` is *undefined* (observed, Go 1.24.7: `undefined: greet.Hello`). More generally, a name that starts with a lowercase letter is private to its package: even if `main.go` asked for `greet.hello`, other packages could not use it. The capital letter is the whole mechanism for "visible outside".

**Experiment B** (observed): Go looked for `labs/grete`, did not find it in the module, and treated it as a standard-library path: `package labs/grete is not in std`. A typo in an import is reported as a missing package.

**3. What makes a package a program?**
Its name is `main` and it has a function `func main()`. Running it starts there. Any other package name makes a library: it has no entry point of its own and exists to be imported.

**4. Two folders `labs/a/` and `labs/b/`, each with `.go` files.**
One module (the folder with `go.mod` above them) and two packages. If either folder had its own `go.mod`, it would be a separate module, which is a different and rarer arrangement.
