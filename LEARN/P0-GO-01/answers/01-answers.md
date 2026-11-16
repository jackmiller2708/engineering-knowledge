# Answers: section 1

**1. Why a new terminal after installing Go?**
When a terminal starts, it copies the current `PATH` setting. The installer changes the setting for programs started *afterwards*; a terminal that is already open still has its old copy, so it cannot find `go`. A new window gets the new `PATH`.

**2. What is different after `go run` and `go build`?**
`go run hello.go` compiles to a temporary place, runs the program and discards it, so the folder is unchanged. `go build hello.go` writes the finished program into the folder: `hello` on Linux, `hello.exe` on Windows (observed by the author on Linux: the folder held `hello` and `hello.go`). Use `run` while experimenting and `build` when you want the program file.

**3. Your version.**
Anything printed as `go1.22` or higher is fine. The platform part (`linux/amd64`, `windows/amd64`, ...) is your operating system and processor type. If it is older than 1.22, a different `go` is first on your `PATH`; section 1's table shows how to find it.
