// SPOILER: reference solution. See hexdump/hexdump.go.
package main

import (
	"fmt"
	"os"

	"labs/hexdump"
)

func main() {
	in := os.Stdin
	if len(os.Args) > 1 {
		f, err := os.Open(os.Args[1])
		if err != nil {
			fmt.Fprintln(os.Stderr, "xd:", err)
			os.Exit(1)
		}
		defer f.Close()
		in = f
	}
	if err := hexdump.Dump(os.Stdout, in); err != nil {
		fmt.Fprintln(os.Stderr, "xd:", err)
		os.Exit(1)
	}
}
