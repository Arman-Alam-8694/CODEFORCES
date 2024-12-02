# C. Firewood

## Time Limit
* 2 seconds

## Memory Limit
* 512 megabytes

## Problem Description
Monocarp has a log weighing 2n grams and needs to burn k grams today. In one minute, he can split any log into two equal halves. The goal is to obtain logs totaling exactly k grams through splitting.

## Constraints
* Each log split creates two equal-weight logs
* Cannot split 1-gram logs
* Must achieve exactly k grams total from some combination of logs
* Remaining logs must total 2n-k grams

## Input
* First line: integer t (1≤t≤104) - test cases
* Each test case: two integers n and k (1≤n≤60; 1≤k≤2n-1)

## Output
For each test case: minimum minutes needed for splitting logs

## Example

### Input
```
4
2 2
2 1
10 3
50 36679020707840
```

### Output
```
1
2
10
16
```

## Note
First case: One cut creates two 2-gram logs.

Second case: Two cuts needed:
1. Cut 4-gram log into two 2-gram logs
2. Cut one 2-gram log into two 1-gram logs
Result: One 2-gram log and two 1-gram logs.
