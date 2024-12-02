def solve(n,k):
    cuts=0
    total=2**n
    while total!=k:
        cuts+=1
        total//=2
        if k>total:
            k-=total
    return cuts
    
  

t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split(" ")))
    print(solve(n,k))
