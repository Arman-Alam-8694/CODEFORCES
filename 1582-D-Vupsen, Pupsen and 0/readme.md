D. Vupsen, Pupsen and 0
time limit per test1 second
memory limit per test256 megabytes
Vupsen and Pupsen were gifted an integer array. Since Vupsen doesn't like the number 0
, he threw away all numbers equal to 0
 from the array. As a result, he got an array a
 of length n
.

Pupsen, on the contrary, likes the number 0
 and he got upset when he saw the array without zeroes. To cheer Pupsen up, Vupsen decided to come up with another array b
 of length n
 such that ∑ni=1ai⋅bi=0
. Since Vupsen doesn't like number 0
, the array b
 must not contain numbers equal to 0
. Also, the numbers in that array must not be huge, so the sum of their absolute values cannot exceed 109
. Please help Vupsen to find any such array b
!

Input
The first line contains a single integer t
 (1≤t≤100
) — the number of test cases. The next 2⋅t
 lines contain the description of test cases. The description of each test case consists of two lines.

The first line of each test case contains a single integer n
 (2≤n≤105
) — the length of the array.

The second line contains n
 integers a1,a2,…,an
 (−104≤ai≤104
, ai≠0
) — the elements of the array a
.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case print n
 integers b1,b2,…,bn
 — elements of the array b
 (|b1|+|b2|+…+|bn|≤109
, bi≠0
, ∑ni=1ai⋅bi=0
).

It can be shown that the answer always exists.
