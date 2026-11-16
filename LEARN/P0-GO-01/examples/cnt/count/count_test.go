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
