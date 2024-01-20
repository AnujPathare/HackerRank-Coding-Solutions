# Enter your code here. Read input from STDIN. Print output to STDOUT

# s = input()
# sorted_s = ''.join(sorted(s, key=lambda char: (char.isdigit(), char.isdigit() and int(char) % 2 == 0, char.swapcase())))
# print(sorted_s)

print(''.join(sorted(input(), key=lambda x: (int(x) % 2==0 if x.isdigit() else 0, x.isdigit(), x.isupper(), x))))

# string = input()

# lower = []
# upper = []
# odd_num = []
# even_num = []

# for char in string:
#     if char.islower():
#         lower.append(char)
#     elif char.isupper():
#         upper.append(char)
#     elif char.isnumeric():
#         if int(char) % 2:
#             odd_num.append(char)
#         else:
#             even_num.append(char)

# print(''.join(sorted(lower) + sorted(upper) + sorted(odd_num) + sorted(even_num)))