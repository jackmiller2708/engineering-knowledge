// Command accept checks an xd executable against the P0-GO-01 fixtures.
//
// It runs your xd on every fixture twice (file argument, then standard input), compares
// the output byte for byte with the expected output, and checks that a missing file is
// reported as an error. It does not look at your source code.
//
//	Linux (Zsh):             go run . -xd /path/to/xd
//	Windows (PowerShell 7):  go run . -xd C:\path\to\xd.exe
package main

import (
	"bytes"
	"context"
	"embed"
	"errors"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strings"
	"time"
)

//go:embed fixtures/*.in fixtures/*.out
var fixtures embed.FS

const limit = 10 * time.Second

// run starts xd with args and the given standard input, and returns what it printed.
func run(xd string, stdin []byte, args ...string) (stdout []byte, exitCode int, err error) {
	ctx, cancel := context.WithTimeout(context.Background(), limit)
	defer cancel()
	cmd := exec.CommandContext(ctx, xd, args...)
	cmd.Stdin = bytes.NewReader(stdin)
	var out bytes.Buffer
	cmd.Stdout = &out
	cmd.Stderr = nil
	err = cmd.Run()
	if ctx.Err() == context.DeadlineExceeded {
		return out.Bytes(), -1, fmt.Errorf("did not finish within %s (is it waiting for input?)", limit)
	}
	var ee *exec.ExitError
	if errors.As(err, &ee) {
		return out.Bytes(), ee.ExitCode(), nil
	}
	return out.Bytes(), 0, err
}

// describe says where got first differs from want, with whitespace made visible.
func describe(want, got []byte) string {
	if len(got) == 0 {
		return "no output at all"
	}
	wl := strings.SplitAfter(string(want), "\n")
	gl := strings.SplitAfter(string(got), "\n")
	for i := 0; i < len(wl) && i < len(gl); i++ {
		if wl[i] != gl[i] {
			msg := fmt.Sprintf("line %d differs\n        want %q\n         got %q", i+1, wl[i], gl[i])
			if strings.Contains(gl[i], "\r") {
				msg += "\n        hint: your output contains a carriage return; write \\n only"
			}
			return msg
		}
	}
	return fmt.Sprintf("output has %d lines, expected %d (the first lines match)", len(gl)-1, len(wl)-1)
}

func main() {
	xdFlag := flag.String("xd", "", "path to the xd executable you built")
	flag.Parse()
	if *xdFlag == "" {
		fmt.Fprintln(os.Stderr, "usage: accept -xd <path to your xd executable>")
		os.Exit(2)
	}
	xd, err := filepath.Abs(*xdFlag)
	if err != nil {
		fmt.Fprintln(os.Stderr, "accept:", err)
		os.Exit(2)
	}
	if _, err := os.Stat(xd); err != nil {
		fmt.Fprintln(os.Stderr, "accept: cannot find the executable:", err)
		os.Exit(2)
	}

	dir, err := os.MkdirTemp("", "accept-")
	if err != nil {
		fmt.Fprintln(os.Stderr, "accept:", err)
		os.Exit(2)
	}
	defer os.RemoveAll(dir)

	entries, _ := fixtures.ReadDir("fixtures")
	var names []string
	for _, e := range entries {
		if strings.HasSuffix(e.Name(), ".in") {
			names = append(names, strings.TrimSuffix(e.Name(), ".in"))
		}
	}
	sort.Strings(names)

	total, passed := 0, 0
	report := func(ok bool, label, detail string) {
		total++
		if ok {
			passed++
			fmt.Printf("PASS  %s\n", label)
			return
		}
		fmt.Printf("FAIL  %s\n        %s\n", label, detail)
	}

	for _, n := range names {
		in, _ := fixtures.ReadFile("fixtures/" + n + ".in")
		want, _ := fixtures.ReadFile("fixtures/" + n + ".out")
		path := filepath.Join(dir, n+".in")
		if err := os.WriteFile(path, in, 0o644); err != nil {
			fmt.Fprintln(os.Stderr, "accept:", err)
			os.Exit(2)
		}

		got, code, err := run(xd, nil, path) // file argument; standard input is empty
		label := fmt.Sprintf("%-10s as a file argument", n)
		switch {
		case err != nil:
			report(false, label, err.Error())
		case code != 0:
			report(false, label, fmt.Sprintf("exit status %d, expected 0", code))
		case !bytes.Equal(got, want):
			report(false, label, describe(want, got))
		default:
			report(true, label, "")
		}

		got, code, err = run(xd, in) // no arguments; the bytes arrive on standard input
		label = fmt.Sprintf("%-10s on standard input", n)
		switch {
		case err != nil:
			report(false, label, err.Error())
		case code != 0:
			report(false, label, fmt.Sprintf("exit status %d, expected 0", code))
		case !bytes.Equal(got, want):
			report(false, label, describe(want, got))
		default:
			report(true, label, "")
		}
	}

	got, code, err := run(xd, nil, filepath.Join(dir, "no-such-file"))
	label := "missing file is an error"
	switch {
	case err != nil:
		report(false, label, err.Error())
	case code == 0:
		report(false, label, "exit status 0; a file that does not exist should give a non-zero exit status")
	case len(got) != 0:
		report(false, label, "printed output on standard output for a file that does not exist")
	default:
		report(true, label, "")
	}

	fmt.Printf("\n%d of %d checks passed\n", passed, total)
	if passed != total {
		os.Exit(1)
	}
}
