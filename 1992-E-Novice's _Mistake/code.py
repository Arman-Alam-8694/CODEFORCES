def solve(n):
    result = []
    lenN=len(str(n))
    sn=str(n)
    
    for a in range(1, 10001):
        number = n * a
        temp = ""
        # b_list = []
        
        # Simulating the logic from check1
        while int(temp or "0") < number:
            for i in str(n):
                temp += i
                if int(temp) > number:
                    break
                b = number - int(temp)
                if b == 0:
                    continue
                numm = (n * a) - b
                # y = 0
                # for i in range(lenN * a - b):
                #     y = y * 10 + int(sn[i % lenN])
                app = len(str(n) * a) - b
                stringg = (str(n) * app)[:app]
                if str(numm)== stringg:
                    result.append((a, b))
                # b_list.append(b)
        
        # Now checking each (a, b) pair (combined check1 and check2 logic)
        # for b in b_list:
        #     numm = (n * a) - b
        #     # app = len(str(n) * a) - b
        #     # stringg = (str(n) * app)[:app]
            
        #     # if stringg == str(numm):
        #     #     result.append([a, b])
        #     y = 0
        #     for i in range(lenN * a - b):
        #         y = y * 10 + int(sn[i % lenN])
        #     if numm== y:
        #         result.append((a, b))
    
    print(len(result))
    for i in result:
        print(*i)

# Reading input
t = int(input())
for i in range(t):
    n = int(input())
    solve(n)

    
