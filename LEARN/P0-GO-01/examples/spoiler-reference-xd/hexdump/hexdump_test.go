package hexdump

import (
	"bytes"
	"strings"
	"testing"
)

func dump(t *testing.T, in string) string {
	t.Helper()
	var out bytes.Buffer
	if err := Dump(&out, strings.NewReader(in)); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	return out.String()
}

func TestDump(t *testing.T) {
	// 40 bytes: two full lines and a last line of 8 bytes.
	forty := "Hello, Go!\nbytes: \x00\x01\xff\n0123456789ABCDEFGH"
	want := "00000000  48 65 6c 6c 6f 2c 20 47 6f 21 0a 62 79 74 65 73  |Hello, Go!.bytes|\n" +
		"00000010  3a 20 00 01 ff 0a 30 31 32 33 34 35 36 37 38 39  |: ....0123456789|\n" +
		"00000020  41 42 43 44 45 46 47 48                          |ABCDEFGH|\n"

	tests := []struct {
		name string
		in   string
		want string
	}{
		{"empty prints nothing", "", ""},
		{"one byte, short line", "A", "00000000  41                                               |A|\n"},
		{"exactly one full line", "ABCDEFGHIJKLMNOP", "00000000  41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50  |ABCDEFGHIJKLMNOP|\n"},
		{"40 bytes, partial last line", forty, want},
	}
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			if got := dump(t, tc.in); got != tc.want {
				t.Errorf("Dump(%q)\n got: %q\nwant: %q", tc.in, got, tc.want)
			}
		})
	}
}

func TestLineUsesDotsForUnprintableBytes(t *testing.T) {
	got := Line(0, []byte{0x1f, 0x20, 0x7e, 0x7f, 0x80})
	if !strings.HasSuffix(got, " |. ~..|\n") {
		t.Errorf("text column wrong: %q", got)
	}
}
