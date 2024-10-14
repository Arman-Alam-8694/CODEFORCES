# A. Primary Task

time limit per test
1 second
memory limit per test
256 megabytes

Dmitry wrote down tt integers on the board, and that is good. He is sure that he lost an *important* integer nn among them, and that is bad.

The integer nn had the form 10^x10^x (x≥2x≥2), where the symbol '^^' denotes exponentiation.. Something went wrong, and Dmitry missed the symbol '^^' when writing the *important* integer. For example, instead of the integer 105105, he would have written 105105, and instead of 10191019, he would have written 10191019.

Dmitry wants to understand which of the integers on the board could have been the *important* integer and which could not.

**Input**

The first line of the input contains one integer tt (1≤t≤1041≤t≤104) — the number of integers on the board.

The next tt lines each contain an integer aa (1≤a≤100001≤a≤10000) — the next integer from the board.

**Output**

For each integer on the board, output "YES" if it could have been the *important* integer and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

**Example**

**Input**
**Copy**

```
7
100
1010
101
105
2033
1019
1002
```

**Output**
**Copy**

```
NO
YES
NO
YES
NO
YES
NO
```
