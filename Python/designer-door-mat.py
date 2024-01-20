n, m = input().split()
n = int(n)
m = int(m)

for i in range(1, n+1):
    if i < n+1//2:
        ('.|.'*((2*i)-1)).center(m, '-')
        j = (2*i)-1
    elif i == n+1//2:
        'WELCOME'.center(m, '-')
    elif i > n+1//2:
        ('.|.'*j).center(m, '-')
        j -= 1

# n, m = input().split()
# n = int(n)
# m = int(m)
# j = 0
# for i in range(n):
#     if i < (n-1)//2:
#         print("-"*((m-3-(6*i))//2), end="")
#         print(".|."*((i*2)+1), end="")
#         print("-"*((m-3-(6*i))//2), end="")
#         print()
#     elif i == (n-1)//2:
#         print("-"*((m-7)//2) + "WELCOME" + "-"*((m-7)//2))
#     elif i > (n-1)//2:
#         print("-"*((3*j)+3), end="")        
#         print(".|."*((m-((3*j)+3)*2)//3), end="")
#         print("-"*((3*j)+3), end="")
#         print()
#         j += 1


# for i in range((n-1)//2):
#     for j in range((m-3-(6*i))//2):
#         print("-", end="")

#     for j in range((i*2)+1):
#         print(".|.", end="")

#     for j in range((m-3-(6*i))//2):
#         print("-", end="")

#     print()

# print("-"*((m-7)//2) + "WELCOME" + "-"*((m-7)//2))

# for i in range((n-1)//2):
#     for j in range((3*i)+3):
#         print("-", end="")

#     for j in range((m-((3*i)+3)*2)//3):
#         print(".|.", end="")

#     for j in range((3*i)+3):
#         print("-", end="")

#     print()