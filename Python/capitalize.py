s = input()

result = ""
for i in range(len(s)):
    if i == 0:
        result += s[i].capitalize()
    elif s[i-1] == " ":
        result += s[i].capitalize()
    else:
        result += s[i]

print(result)


# cap = []
# new_lst = s.split()
# for word in new_lst:
#     cap.append(word.capitalize())

# result = ""
# for word in cap:
#     result += word + " "

# print(result.rstrip())

# result = ""
# temp = 1
# space = 0

# for i in s:

#     if space == 0:
#         if temp == 1:
#             result += i.upper()      
#     elif space == 1:
#         result += i.upper()
#         temp = 1
#         space = 0
    
#     if temp == 0:
#         result += i

#     if i == " ":
#         space = 1

#     temp = 0
# print(result)    