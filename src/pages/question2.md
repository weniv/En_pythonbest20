- info
    - Lv.1
    - Regular Expression

# Cipher Text
![Colleagues who discovered seven stones](./2_1.webp)

## Problem Description
Licat obtained 7 stones on the mysterious island of Jeju. He shared the 7 stones with his colleagues and urged them to return to their respective villages to gather strength to defeat Lion.

![Colleagues who received the stones](./2_2.webp)

The colleagues with each stone headed back to their respective villages. They exchanged letters with Licat, who has returned to the cat village, using a cipher. Among various cipher texts, the final revolutionary date can be deciphered by the `month` and `day`. Please prepare for the expedition by finding out the date of the revolution in the letter according to the following rules:

- The content of the letter is given as a string.
- The date of the revolution is determined by the number which is the sum of the values after r, e, and v in the string. The digit in the tens place is considered the `month` and the digit in the ones place is considered the `day`.
- The `month` should be converted into an abbreviated form as in Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, and Sep.
- The `day` should be given in numeral form(1), not an ordinal number(1st).
- The numbers after r, e, and v are between 1 and 10. If the number is greater than 10, only the single digit right after r, e, and v is considered.


---

## Constraints

- 1 ≤ number after r, e, and v ≤ 10
- 11 ≤ sum of the numbers ≤ 99

---

## Examples

| Input                                  | Output  |
| ---------------------------------------- | ------- |
| 'a10b9r1ce33uab8wc918v2cv11v9'          | 'Jan 6' |

---

## Explanation for Examples

The extracted values from the string according to the pattern are as follows. e33 should be recognized as e3, so only 3 should be extracted.

```py
['r1', 'e3', 'v2', 'v1', 'v9']
```

When all these numbers are added together, the result is `16`, which means the digit in the tens place is the month and the digit in the ones place is the day. Then `1` is converted into `Jan`. Therefore, the date of the revolution is `Jan 6`.
