# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

strg, k = input().split()

for i in list(permutations(sorted(strg), int(k))):
    print("".join(i))



# # Enter your code here. Read input from STDIN. Print output to STDOUT


# temp, k = input().split()
# k = int(k)
 
# s = []
# for i in range(len(temp)):
#     s.append(temp[i])

# s.sort()
# result = []

# for i in list(permutations(s, k)):
#     # print(*i, sep="")
#     print(''.join(i))

# #     str = ""
# #     for j in i:
# #         str += j
# #     result.append(str)
    
    
# # for i in result:
# #     print(i)
