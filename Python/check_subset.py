# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    A_length = int(input())
    setA = set(map(int, input().split()))
    
    B_length = int(input())
    setB = set(map(int, input().split()))
    
    print(setA.issubset(setB))
    
    # flag = 0
    # for num in setA:
    #     if num not in setB:
    #         flag = 1
    
    # if flag:
    #     print(False)
    # else:
    #     print(True)