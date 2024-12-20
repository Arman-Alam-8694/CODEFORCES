# Programming Problem: Noobish_Monk's Apples

## Time Limit per Test
3 seconds

## Memory Limit per Test
256 megabytes

## Problem Statement

One of the first programming problems by K1o0n looked like this: "Noobish_Monk has n (1≤n≤100) friends. Each of them gave him a (1≤a≤10000) apples for his birthday. Delighted with such a gift, Noobish_Monk returned b (1≤b≤min(10000,a⋅n)) apples to his friends. How many apples are left with Noobish_Monk?"

K1o0n wrote a solution, but accidentally considered the value of n as a string, so the value of n⋅a−b was calculated differently. Specifically:
* When multiplying the string n by the integer a, he will get the string s=n+n+⋯+n+n (a times)
* When subtracting the integer b from the string s, the last b characters will be removed from it. If b is greater than or equal to the length of the string s, it will become empty.

Learning about this, ErnKor became interested in how many pairs (a,b) exist for a given n, satisfying the constraints of the problem, on which K1o0n's solution gives the correct answer.

"The solution gives the correct answer" means that it outputs a **non-empty** string, and this string, when converted to an integer, equals the correct answer, i.e., the value of n⋅a−b.

## Input

The first line contains a single integer t (1≤t≤100) — the number of test cases.

For each test case, a single line of input contains an integer n (1≤n≤100).

It is guaranteed that in all test cases, n is distinct.

## Output

For each test case, output the answer in the following format:

In the first line, output the integer x — the number of bad tests for the given n.

In the next x lines, output two integers ai and bi — such integers that K1o0n's solution on the test "n ai bi" gives the correct answer.

## Example

### Input
```
3
2
3
10
```

### Output
```
3
20 18 
219 216 
2218 2214 
1
165 162 
1
1262 2519 
```

## Note

In the first example, a=20, b=18 are suitable, as "22" ⋅20−18= "2222222222222222222222222222222222222222"−18=22=2⋅20−18
