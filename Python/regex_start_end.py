# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

strg = input()
k = input()

result = []

for i in range(len(strg)-len(k)+1):
    temp = strg[i:i+(len(k))]
    searcher = re.search(k, temp)
    if searcher:
        result.append((i,i+(len(k))-1))
    else:
        continue

if result == []:
    print((-1,-1))
else:
    for i in result:
        print(i)