n = int(input())
nums = list(map(int, input().split()))
print(all([num>0 for num in nums]) and any([str(num) == str(num)[::-1] for num in nums]))