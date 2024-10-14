def solve(s,t):
    prefix=0
    slen=len(s)
    tlen=len(t)
    for i in range(min(slen,tlen)):
        if s[i]==t[i]:
            prefix+=1
        else:
            break
    return min(slen+tlen,((slen+tlen+1)-prefix))


if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        s=input()
        t=input()
        print(solve(s,t))
