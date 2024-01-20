# Enter your code here. Read input from STDIN. Print output to STDOUT

# NOTE: This code can also be done using a single for loop. #

# try here #
#    .
#    .
#    .
#    .
#    .



# -------------------------------------------- #

# shoes = int(input())
# sizes = list(map(int, input().split()))
# customers = int(input())

# availability = Counter(sizes)
# agreement = {}
# for i in range(customers):
#     size_req, price = input().split()
#     if int(size_req) in agreement:
#         agreement[int(size_req)].append(int(price))
#     else:
#         agreement[int(size_req)] = [int(price)]

# earning = 0
# for size_req, price in agreement.items():
#     i = 0
#     while availability[size_req] > 0 and i < len(price):
#         earning += price[i]
#         i += 1
#         availability[size_req] -= 1
        
# print(earning)



# -------------------------------------------- #

# x = int(input())
# sizes = input().split()
# cust = int(input())
# demand = []

# for i in range(cust):
#     d_size, price = input().split()
#     d_size = int(d_size)
#     price = int(price)    
#     demand.append((d_size, price))


# tally = dict(Counter(sizes))

# earning = 0

# for i in demand:

#     if str(i[0]) in list(tally.keys()) and tally[str(i[0])] > 0:
#         earning += i[1]
#         tally[str(i[0])] = tally[str(i[0])] - 1

# print(earning)