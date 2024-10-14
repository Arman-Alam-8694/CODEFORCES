# C. Numeric String Template

time limit per test
2 seconds
memory limit per test
256 megabytes

Kristina has an array aa, called a *template*, consisting of nn integers. She also has mm strings, each consisting only of lowercase Latin letters. The strings are numbered from 11 to mm. She wants to check which strings match the template.

A string ss is considered to match the template if all of the following conditions are simultaneously satisfied:
* The length of the string ss is equal to the number of elements in the array aa.
* The same numbers from aa correspond to the same symbols from ss. So, if ai=ajai=aj, then si=sjsi=sj for (1≤i,j≤n1≤i,j≤n).
* The same symbols from ss correspond to the same numbers from aa. So, if si=sjsi=sj, then ai=ajai=aj for (1≤i,j≤n1≤i,j≤n).

In other words, there must be a one-to-one correspondence between the characters of the string and the elements of the array.

For example, if aa = [3,5,2,1,33,5,2,1,3], then the string "abfda" matches the template, while the string "afbfa" does not, since the character "f" corresponds to both numbers 11 and 55.

**Input**

The first line of input contains a single integer tt (1≤t≤1041≤t≤104) — the number of test cases.

The following descriptions are for the test cases.

The first line of each test case contains a single integer nn (1≤n≤2⋅1051≤n≤2⋅105) — the number of elements in the array aa.

The second line of each test case contains exactly nn integers aiai (−109≤ai≤109−109≤ai≤109) — the elements of the array aa.

The third line of each test case contains a single integer mm (1≤m≤2⋅1051≤m≤2⋅105) — the number of strings to check for template matching.

Following are mm strings, each containing a non-empty string sjsj (1≤|sj|≤2⋅1051≤|sj|≤2⋅105), consisting of lowercase Latin letters.

It is guaranteed that the sum of nn across all test cases does not exceed 2⋅1052⋅105, and that the sum of the lengths of all strings does not exceed 2⋅1052⋅105.

**Output**

For each test case, output mm lines. On the ii-th line (1≤i≤m1≤i≤m) output:
* "YES", if the string with index ii matches the template;
* "NO" otherwise.

You may output the answer in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).

**Example**

**Input**
**Copy**

```
3
5
3 5 2 1 3
2
abfda
afbfa
2
1 2
3
ab
abc
aa
4
5 -3 5 -3
4
aaaa
bcbc
aba
cbcb
```

**Output**
**Copy**

```
YES
NO
YES
NO
NO
NO
YES
NO
YES
```

**Note**

The first test case is explained in the problem statement.
