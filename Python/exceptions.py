# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ValueError as valErr:
        print('Error Code:', valErr)
    except ZeroDivisionError as zeroDiv:
        print('Error Code:', zeroDiv)