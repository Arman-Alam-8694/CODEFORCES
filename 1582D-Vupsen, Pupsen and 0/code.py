
def solve(n,array):
    if not n&1:
        result=[-1]*n
        left=0
        right=n-1
        while left<right:
            result[left]=array[right]*-1
            result[right]=array[left]
            left+=1
            right-=1
    else:
        lastthree=[-1]*3
        a1=array[-3]
        a2=array[-2]
        a3=array[-1]
        if a1+a2!=0:
            lastthree[-3]=-a3
            lastthree[-2]=-a3
            lastthree[-1]=(a1+a2)
        if a2+a3!=0:
            lastthree[-3]=(a2+a3)
            lastthree[-2]=-a1
            lastthree[-1]=-a1
        if a1+a3!=0:
            lastthree[-3]=-a2
            lastthree[-2]=a1+a3
            lastthree[-1]=-a2


        if n-3==0:
            return lastthree
        else:
            result=[-1]*(n-3)
            left=0
            right=n-4
            while left<right:
                result[left]=array[right]*-1
                result[right]=array[left]
                left+=1
                right-=1
            return result+lastthre

    return result

t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split(" ")))
    print(*(solve(n,array)))
