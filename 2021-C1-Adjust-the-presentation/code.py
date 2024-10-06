from collections import Counter
def solve(n,m,q,array1,array2):
    dictt={}
    for i in range(m):
        if array2[i] not in dictt:
            # print(array11[i])
            dictt[array2[i]]=i
    if len(set(array2))>len(set(array1)):
        return "TIDAK"
    start=-1
    for i in range(n):
        if not dictt:
            return "YA"
        if array1[i] not in dictt:
            return "TIDAK"
        if dictt[array1[i]]<start:
            return "TIDAK"
        else:
            start=dictt[array1[i]]
        
        del dictt[array1[i]]
 
    return "YA"
 
t=int(input())
for i in range(t):
    n,m,q=map(int,input().split(" "))
    array1=list(map(int,input().split(" ")))
    array2=list(map(int,input().split(" ")))
    print(solve(n,m,q,array1,array2))
