# Enter your code here. Read input from STDIN. Print output to STDOUT

setA = set(map(int, input().split()))

flag = 0

for _ in range(int(input())):
    setB = set(map(int, input().split()))
    
    if len(setB) == len(setA):
        print(False)
    else:
        for num in setB:
            if num not in setA:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break

if flag:
    print(False)
else:
    print(True)