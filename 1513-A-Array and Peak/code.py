
def solve(n,k):

    if (n-k)<k+1:
        print("-1")
        return 
    lp=(n+1)-k
   
    end=1
    while lp<=n:
        print(end,end=" ")
        print(lp,end=" ")
        lp+=1
        end+=1
    for i in range(n-k,end-1,-1):
        print(i,end=" ")
    print()
        



t=int(input())
for i in range(t):
    n,k=map(int,input().split(" "))
    solve(n,k)
