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
