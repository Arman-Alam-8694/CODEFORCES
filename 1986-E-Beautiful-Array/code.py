def solve(n,k,array):
    minn=float("inf")
    dictt={}
    array.sort()
    for i in array:
        if i%k not in dictt:
            dictt[i%k]=[]
        dictt[i%k].append(i)
    odd_count=0
    for v in dictt.values():
        if len(v)&1:
            odd_count+=1
    if odd_count>1 and n&1:
        return -1
    if odd_count and (not n&1):
        return -1
    score=0
    for arr in dictt.values():
    
        m=len(arr)
        if m&1:
            min_score=0
            for i in range(1,m,2):
                min_score+=(arr[i+1]-arr[i])//k
            postscore=min_score
            prescore=0
            
            for i in range(1,m,2):
                postscore-=(arr[i+1]-arr[i])//k
                prescore+=(arr[i]-arr[i-1])//k
              
                min_score=min(postscore+prescore,min_score)
            score+=min_score
        else:
            min_score=0
            for i in range(0,m,2):
                min_score+=(arr[i+1]-arr[i])//k
        
            score+=min_score
    return score


t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    array=list(map(int,input().split()))
    print(solve(n,k,array))
