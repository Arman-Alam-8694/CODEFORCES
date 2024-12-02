def solve(n,m,n_array,m_array):
    # print(n_array)

    # array=n_array+m_array
    # array.sort(reverse=True)
    # summ=sum(array[:n])
    # minn=min(array[:n])
    # maxx=m_array[-1]
    # sett=set(array[:n])
    # if maxx in sett:
    #     return summ 
    # else:
    #     summ-=minn
    #     summ+=maxx
    # return summ
    array=n_array+m_array
    array.sort(reverse=True)
    check=m_array[-1]
    found=False
    summ=0
    for i in range(0,n-1):
        if array[i]==check:
            found=True
        summ+=array[i]
    if found:
        summ+=array[n-1]
        return summ
    else:
        return summ+check
        


t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split(" ")))
    n_array=list(map(int,input().split(" ")))
    m_array=list(map(int,input().split(" ")))
    print(solve(n,m,n_array,m_array))
