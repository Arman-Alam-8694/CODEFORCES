def solve(n,array):
    array.sort()
    while len(array)!=1:
        average=(array[0]+array[1])//2
        array.pop(0)
        array.pop(0)
        array.append(average)
        array.sort()
    return array[0]
    
 
 
t=int(input())
for i in range(t):
    n=int(input())
    array=list(map(int,input().split(" ")))
    print(solve(n,array))
