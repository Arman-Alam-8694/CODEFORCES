# A. Array and Peaks

### Problem:
A sequence of `n` integers is called a permutation if it contains all integers from `1` to `n` exactly once.

Given two integers `n` and `k`, construct a permutation `a` of numbers from `1` to `n` which has exactly `k` peaks. An index `i` of an array `a` of size `n` is said to be a peak if `1 < i < n` and `a[i] > a[i-1]` and `a[i] > a[i+1]`. If such a permutation is not possible, then print `-1`.

### Input:
- The first line contains an integer `t` (1 ≤ t ≤ 100) — the number of test cases.
- Then `t` lines follow, each containing two space-separated integers `n` (1 ≤ n ≤ 100) and `k` (0 ≤ k ≤ n) — the length of an array and the required number of peaks.

### Output:
Output `t` lines. For each test case, if there is no permutation with the given length and number of peaks, then print `-1`. Otherwise, print a line containing `n` space-separated integers which forms a permutation of numbers from `1` to `n` and contains exactly `k` peaks.
