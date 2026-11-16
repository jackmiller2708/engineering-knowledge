# Answers: section 5

Open this only after you have tried all three parts.

## Part A: the expected values for your old rows

Each old row needs a `LongestLine`, worked out from the definition (bytes in the longest line, not counting the newline):

| Row | Input | Longest line |
|---|---|---|
| empty | (empty) | 0 |
| one word, no newline | `hello` | 5 |
| two lines | `a b`, newline, `c`, newline | 3 |
| windows line endings | `a`, CR LF, `b`, CR LF | 2 (the CR is still part of the line, for now) |
| several spaces | `a   b` | 5 |
| accented letter | `caf` + 2 bytes, newline | 5 |

The compile error you saw (observed): `too few values in struct literal of type Result`. Each old row built a `Result` by listing three values in order. Adding a fourth field makes every such row incomplete, and the compiler lists them for you.

## Part A: one working solution

The test table, with the new rows (the rest of the test function is unchanged):

```go
tests := []struct {
		name string
		in   string
		want Result
	}{
		{"empty", "", Result{0, 0, 0, 0}},
		{"one word, no newline", "hello", Result{0, 1, 5, 5}},
		{"two lines", "a b\nc\n", Result{2, 3, 6, 3}},
		{"windows line endings", "a\r\nb\r\n", Result{2, 2, 6, 2}},
		{"several spaces", "a   b", Result{0, 2, 5, 5}},
		{"accented letter is one word", "caf\xc3\xa9\n", Result{1, 1, 6, 5}},
		{"longest: no newline at all", "abc", Result{0, 1, 3, 3}},
		{"longest: middle line wins", "ab\ncde\nf\n", Result{3, 3, 9, 3}},
		{"longest: only newlines", "\n\n", Result{2, 0, 2, 0}},
		{"longest: carriage return counts for now", "a\r\nbcd\r\n", Result{2, 2, 8, 4}},
	}
```

`Count`, with one extra piece of state, `cur`, the length of the line being read:

```go
func Count(r io.Reader) (Result, error) {
	var res Result
	br := bufio.NewReader(r)
	inWord := false
	cur := 0 // length of the current line so far
	for {
		b, err := br.ReadByte()
		if err == io.EOF { // EOF = end of file: nothing left to read
			if cur > res.LongestLine { // a last line with no newline still counts
				res.LongestLine = cur
			}
			break
		}
		if err != nil {
			return res, err
		}
		res.Bytes++
		if b == '\n' {
			res.Lines++
			if cur > res.LongestLine {
				res.LongestLine = cur
			}
			cur = 0
		} else {
			cur++
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
```

Why the end-of-input update matters: a final line with no newline never reaches the `'\n'` branch, so without the update inside the `io.EOF` branch it is never compared with the longest so far.

## Part B: the variation

Changing the definition (a carriage return does not count) changes the code to skip it:

```go
func Count(r io.Reader) (Result, error) {
	var res Result
	br := bufio.NewReader(r)
	inWord := false
	cur := 0 // length of the current line so far
	for {
		b, err := br.ReadByte()
		if err == io.EOF { // EOF = end of file: nothing left to read
			if cur > res.LongestLine { // a last line with no newline still counts
				res.LongestLine = cur
			}
			break
		}
		if err != nil {
			return res, err
		}
		res.Bytes++
		if b == '\n' {
			res.Lines++
			if cur > res.LongestLine {
				res.LongestLine = cur
			}
			cur = 0
		} else if b != '\r' {
			cur++
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
```

**Two rows change**, not one: the dedicated row (`a`, CR LF, `bcd`, CR LF: from 4 to 3) **and** the older "windows line endings" row (from 2 to 1), because that old row also has carriage returns at the end of its longest line. The failure you get if you forget the old row (observed):
```
Count("a\r\nb\r\n") = {Lines:2 Words:2 Bytes:6 LongestLine:1}, want {Lines:2 Words:2 Bytes:6 LongestLine:2}
```
The lesson: when you change what a word in your specification means, every test that depended on the old meaning has to change. The test failure is the tool telling you which ones.

A design question this raises: the code above ignores a carriage return **anywhere** in a line, not only before a newline. Is that what you want? There is no single right answer, but it is a decision, and now it is written in a test.

## Part C: the mutation check

Removing the end-of-input update makes these rows fail (observed): `one word, no newline`, `several spaces`, and `longest: no newline at all`. They fail for the right reason (the longest line comes out as 0 instead of 5, 5 and 3). The rows that end in a newline keep passing, because the newline branch already handles them. Each row protects a specific behaviour; a test that cannot fail on a particular mistake does not protect against it.

## Check yourself

**1.** Every old row needed a fourth number, from the definition above. If you worked them out by running your code, the new field's tests are checking your code against itself.
**2.** Two rows change in Part B. Writing the list first is the habit: you predict the effect of a change before you see it.
**3.** Part C: which tests guard the last-line behaviour, and that the rest of the table does not.
