# Recall card: P0-GO-01

**Do this about a week after you finish the unit, and again about a month after.** Put both dates in your calendar. It takes about ten minutes each time and is part of the unit's study time, not extra.

**Rules:** no notes, no code, no course. Write each answer in a sentence or two, in your own words. Leave a blank if you do not know; a blank is the most useful answer, because it shows what to revisit. Then compare with `../answers/recall-answers.md`. If you got something wrong, go back to the section named in brackets and redo its experiment before you move on.

1. What does `go.mod` contain, and what does it decide? [section 2]
2. What is the difference between a module, a package and a program? [section 2]
3. Why do some names start with a capital letter? [section 2]
4. What is an `io.Reader`, and why does `Count` take one instead of a file path? [section 4]
5. How does `Count` decide that a new word has started? [section 4]
6. What does the pattern `if err != nil` express, and why is `io.EOF` treated differently from other errors? [section 4]
7. Why can adding a field to a struct make existing tests stop compiling, and what should the new value in each old row come from? [section 5]
8. How should the expected value in a test be obtained, and why? [sections 5 and 7]
9. What can `io.ReadFull` return when the input ends, and which of those are normal? [section 6]
10. Name two things the acceptance check proves that unit tests of one function do not, and one thing neither proves. [section 7]

**Variation (one you have not built):** `cnt` should now count *characters* instead of bytes. What has to change in `Count`, and what stays the same?

After each recall, write the date and your score (how many you answered without hesitation) at the bottom of your own notes. If a question you knew last time was blank this time, that is the interesting result.
