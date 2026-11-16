package main

import (
	"fmt"
	"strings"
	"testing"
)

// These tests check the fixtures themselves, using only arithmetic about the layout.
// They do not contain an implementation of xd.

func TestFixturesArePaired(t *testing.T) {
	ins, _ := fixtures.ReadDir("fixtures")
	n := 0
	for _, e := range ins {
		if !strings.HasSuffix(e.Name(), ".in") {
			continue
		}
		n++
		name := strings.TrimSuffix(e.Name(), ".in")
		if _, err := fixtures.ReadFile("fixtures/" + name + ".out"); err != nil {
			t.Errorf("%s has no expected output", name)
		}
	}
	if n < 7 {
		t.Errorf("expected at least 7 cases, found %d", n)
	}
}

func TestExpectedOutputsFollowTheLayout(t *testing.T) {
	ins, _ := fixtures.ReadDir("fixtures")
	for _, e := range ins {
		if !strings.HasSuffix(e.Name(), ".in") {
			continue
		}
		name := strings.TrimSuffix(e.Name(), ".in")
		in, _ := fixtures.ReadFile("fixtures/" + name + ".in")
		out, _ := fixtures.ReadFile("fixtures/" + name + ".out")

		if len(in) == 0 {
			if len(out) != 0 {
				t.Errorf("%s: empty input must give empty output", name)
			}
			continue
		}
		lines := strings.SplitAfter(string(out), "\n")
		lines = lines[:len(lines)-1] // SplitAfter leaves one empty piece after the last newline
		if want := (len(in) + 15) / 16; len(lines) != want {
			t.Errorf("%s: %d bytes need %d lines, fixture has %d", name, len(in), want, len(lines))
			continue
		}
		for i, line := range lines {
			chunk := len(in) - i*16
			if chunk > 16 {
				chunk = 16
			}
			// 8 offset digits + 2 spaces + 16 columns of 3 + " |" + text + "|" + newline
			if want := 10 + 48 + 2 + chunk + 1 + 1; len(line) != want {
				t.Errorf("%s line %d: length %d, want %d", name, i+1, len(line), want)
			}
			if !strings.HasPrefix(line, fmt.Sprintf("%08x  ", i*16)) {
				t.Errorf("%s line %d: offset column wrong: %q", name, i+1, line[:10])
			}
			if !strings.HasSuffix(line, "|\n") {
				t.Errorf("%s line %d: does not end with |\\n", name, i+1)
			}
		}
	}
}
