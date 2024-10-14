def solve(n):
    if 102<=n<=109 or 1010<=n<=1099:
        return "YES"
    else:
        return "NO"
        
        
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n=int(input())

        print(solve(n))
