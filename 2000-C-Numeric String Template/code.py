def solve(n,listt,m,stringg):
    lengthh=len(stringg)
    dictt={}
    dicttt={}
    if n!=lengthh:
        return "NO"
    for i in range(n):
        if  stringg[i] not in dictt:
            dictt[stringg[i]]=listt[i]
        else:
            if listt[i]!=dictt[stringg[i]]:
                return "NO"
        if listt[i] not in dicttt:
            dicttt[listt[i]]=stringg[i]
        else:
            if stringg[i]!=dicttt[listt[i]]:
                return "NO"

    return "YES"


if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n=int(input())
        listt=list(map(int,input().split()))
        m=int(input())
        for _ in range(m):
            stringg=input()
            print(solve(n,listt,m,stringg))
