def solve(n,listt):
    left=None
    right=None
    for i in listt:
        if left is None and right is None :
            t_left=i-1
            t_right=i+1
            if t_left>=1:
                left=t_left
            if t_right<=n:
                right=t_right
        else:
            if i not in [left,right]:
                return "NO"
            if left==i:
                t_left=left-1
                if t_left>=1:
                    left=t_left
            elif right==i:
                t_right=right+1
                if t_right<=n:
                    right=t_right


    return "YES"


if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n=int(input())
        listt=list(map(int,input().split()))

        print(solve(n,listt))
