# Answers: section 6

**1. Why is formatting one line separate from the loop that reads?**
The formatting is a pure function of an offset and a few bytes, so it can be tested with a table and no input at all. The loop has its own tricky part, which is partial reads and the end of input. Keeping them apart means a mistake in one cannot hide behind the other, each can change on its own (a different layout never touches the reader), and you can test the loop with a `strings.NewReader` without caring how a line looks.

**2. Exactly 32 bytes, and 33.**
At 32 bytes there are exactly two full lines and **no third line**: the third read finds nothing, which is a normal end, so it prints nothing. At 33 bytes the third read returns one byte and prints a short line with one byte, padded. This is the classic place for an off-by-one: exactly 16 or 32 bytes must not produce an extra empty line.

**3. What makes the `|` line up on a short last line?**
The loop over all 16 columns that writes three spaces for each column that has no byte. It runs 16 times whatever the number of bytes, and the text column then starts at the same position on every line.
