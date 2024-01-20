# Enter your code here. Read input from STDIN. Print output to STDOUT

answer = set()

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))
    
answer = (b.difference(a.intersection(b))).union(a.difference(a.intersection(b)))

for elem in sorted(answer):
    print(elem)