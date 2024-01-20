# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

A = map(int, input().split())
B = map(int, input().split())

print(*list(product(A, B)))


# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# cart_prod = []

# for i in range(len(A)):
#     for j in range(len(B)):
#         temp = (A[i], B[j])
#         cart_prod.append(temp)

# for i in range(len(cart_prod)):
#     print(cart_prod[i], end=' ')