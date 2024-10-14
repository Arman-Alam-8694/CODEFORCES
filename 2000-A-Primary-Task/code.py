def solve(n):
    if len(n)<3:
        return "NO"
    if not (n[0]=="1" and n[1]=="0"):
        return "NO"
    if n[2]=="0":
        return "NO"
    if len(n)>=4:
        if int(n[2:4])<2:
            return "NO"
    else:
        if n[2]=="1":
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n=int(input())

        print(solve(str(n)))
