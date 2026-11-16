// Package count measures a stream of bytes.
package count

import (
	"bufio"
	"io"
)

// Result holds what Count measured.
type Result struct {
	Lines int
	Words int
	Bytes int
}

// isSpace reports whether b separates words. Only ASCII whitespace counts.
func isSpace(b byte) bool {
	return b == ' ' || b == '\n' || b == '\t' || b == '\r' || b == '\v' || b == '\f'
}

// Count reads r to the end and reports how many lines, words and bytes it held.
func Count(r io.Reader) (Result, error) {
	var res Result
	br := bufio.NewReader(r)
	inWord := false
	for {
		b, err := br.ReadByte()
		if err == io.EOF { // EOF = end of file: nothing left to read
			break
		}
		if err != nil {
			return res, err
		}
		res.Bytes++
		if b == '\n' {
			res.Lines++
		}
		if isSpace(b) {
			inWord = false
		} else if !inWord {
			inWord = true
			res.Words++
		}
	}
	return res, nil
}
