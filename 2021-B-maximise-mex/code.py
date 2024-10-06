
from collections import Counter
def solve(n,x,array):
    dictt=Counter(array)
    maxx=n
    for i in range(0,n):
        if i not in dictt:
            return i
        if dictt[i]>1:
            dictt[i]-=1
            dictt[i+x]+=dictt[i]
    return n
 
t=int(input())
for i in range(t):
    n,x=map(int,input().split(" "))
    array=list(map(int,input().split(" ")))
    print(solve(n,x,array))
