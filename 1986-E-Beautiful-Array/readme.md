# E. Beautiful Array

time limit per test2 seconds
memory limit per test256 megabytes

You are given an array of integers a₁,a₂,…,aₙ and an integer k. You need to make it beautiful with the least amount of operations.

Before applying operations, you can shuffle the array elements as you like. For one operation, you can do the following:
- Choose an index 1≤i≤n,
- Make aᵢ=aᵢ+k.

The array b₁,b₂,…,bₙ is beautiful if bᵢ=bₙ₋ᵢ₊₁ for all 1≤i≤n.

Find the minimum number of operations needed to make the array beautiful, or report that it is impossible.

## Input

Each test consists of several sets of input data. The first line contains a single integer t (1≤t≤10⁴) — the number of sets of input data. Then follows their description.

The first line of each set of input data contains two integers n and k (1≤n≤10⁵, 1≤k≤10⁹) — the size of the array a and the number k from the problem statement.

The second line of each set of input data contains n integers a₁,a₂,…,aₙ (1≤aᵢ≤10⁹) — the elements of the array a.

It is guaranteed that the sum of n over all sets of input data does not exceed 2⋅10⁵.

## Output

For each set of input data, output the minimum number of operations needed to make the array beautiful, or −1 if it is impossible.

## Example

### Input
```
11
1 1000000000
1
2 1
624323799 708290323
3 1
3 2 1
4 1
7 1 5 3
5 1
11 2 15 7 10
7 1
1 8 2 16 8 16 31
13 1
2 1 1 3 3 11 12 22 45 777 777 1500 74
10 2
1 2 1 2 1 2 1 2 1 2
11 2
1 2 1 2 1 2 1 2 1 2 1
13 3
2 3 9 14 17 10 22 20 18 30 1 4 28
5 1
2 3 5 3 5
```

### Output
```
0
83966524
1
4
6
1
48
-1
0
14
0
```

## Note

In the first set of input data, the array is already beautiful.

In the second set of input data, you can shuffle the array before the operations and perform the operation with index i=1 for 83966524 times.

In the third set of input data, you can shuffle the array a and make it equal to [2,3,1]. Then apply the operation with index i=3 to get the array [2,3,2], which is beautiful.

In the eighth set of input data, there is no set of operations and no way to shuffle the elements to make the array beautiful.

In the ninth set of input data, the array is already beautiful.
