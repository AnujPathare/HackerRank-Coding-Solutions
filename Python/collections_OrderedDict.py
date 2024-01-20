# s = input().split()
# print(type(s[-1:][0]))
# print(" ".join(s[:-1]))
# print(len(" ".join(s[:-1])))
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

tally = OrderedDict()
for i in range(int(input())):
    item_name = input().split()
    
    if " ".join(item_name[:-1]) in tally:
        tally[" ".join(item_name[:-1])] += int(item_name[-1:][0])
    else:
        tally[" ".join(item_name[:-1])] = int(item_name[-1:][0])

for key, value in tally.items():
    print(key, value)