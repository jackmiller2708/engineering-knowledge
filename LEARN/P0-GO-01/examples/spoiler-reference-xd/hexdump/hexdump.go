// SPOILER: a reference solution for P0-GO-01 section 6. Open it only after you have
// written your own xd, or after the hint ladder has not been enough.

// Package hexdump writes a classic hex dump of a stream of bytes.
package hexdump

import (
	"fmt"
	"io"
	"strings"
)

const width = 16 // bytes per line

// Dump reads r to the end and writes one line per 16 bytes to w.
func Dump(w io.Writer, r io.Reader) error {
	buf := make([]byte, width)
	offset := 0
	for {
		// ReadFull fills buf unless the input ends first. It returns io.EOF only when
		// it read nothing, and io.ErrUnexpectedEOF when it read a partial line.
		n, err := io.ReadFull(r, buf)
		if n > 0 {
			if _, werr := io.WriteString(w, Line(offset, buf[:n])); werr != nil {
				return werr
			}
			offset += n
		}
		if err == io.EOF || err == io.ErrUnexpectedEOF {
			return nil
		}
		if err != nil {
			return err
		}
	}
}

// Line formats up to 16 bytes that start at offset, including the final newline.
func Line(offset int, b []byte) string {
	var sb strings.Builder
	fmt.Fprintf(&sb, "%08x  ", offset)
	for i := 0; i < width; i++ {
		if i < len(b) {
			fmt.Fprintf(&sb, "%02x ", b[i])
		} else {
			sb.WriteString("   ") // keep the text column aligned on a short last line
		}
	}
	sb.WriteString(" |")
	for _, c := range b {
		if c >= 0x20 && c <= 0x7e {
			sb.WriteByte(c)
		} else {
			sb.WriteByte('.')
		}
	}
	sb.WriteString("|\n")
	return sb.String()
}
