# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input())
headers = input().split()

data = namedtuple('data', " ".join(headers))

sum = 0
for i in range(n):
    inp = input().split()
    temp = data(*inp)
    sum += int(temp.MARKS)

print(sum/n)