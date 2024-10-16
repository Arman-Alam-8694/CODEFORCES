# A. Two Screens
time limit per test
2 seconds
memory limit per test
512 megabytes
There are two screens which can display sequences of uppercase Latin letters. Initially, both screens display nothing.
In one second, you can do one of the following two actions:
* choose a screen and an uppercase Latin letter, and append that letter to **the end** of the sequence displayed on that screen;
* choose a screen and copy the sequence from it to the other screen, **overwriting the sequence that was displayed on the other screen**.
You have to calculate the minimum number of seconds you have to spend so that the first screen displays the sequence ss, and the second screen displays the sequence tt.
**Input**
The first line contains one integer qq (1≤q≤5001≤q≤500) — the number of test cases.
Each test case consists of two lines. The first line contains the string ss, and the second line contains the string tt (1≤|s|,|t|≤1001≤|s|,|t|≤100). Both strings consist of uppercase Latin letters.
**Output**
For each test case, print one integer — the minimum possible number of seconds you have to spend so that the first screen displays the sequence ss, and the second screen displays the sequence tt.
**Example**
**Input**
**Copy**
3
GARAGE
GARAGEFORSALE
ABCDE
AABCD
TRAINING
DRAINING
**Output**
**Copy**
14
10
16
**Note**
In the first test case, the following sequence of actions is possible:
* spend 66 seconds to write the sequence GARAGE on the first screen;
* copy the sequence from the first screen to the second screen;
* spend 77 seconds to complete the sequence on the second screen by writing FORSALE.
In the second test case, the following sequence of actions is possible:
* spend 11 second to write the sequence A on the second screen;
* copy the sequence from the second screen to the first screen;
* spend 44 seconds to complete the sequence on the first screen by writing BCDE;
* spend 44 seconds to complete the sequence on the second screen by writing ABCD.
In the third test case, the fastest way to display the sequences is to type both of them character by character without copying, and this requires 1616 seconds.
