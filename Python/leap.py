year = int(input())

leap = False

for i in range(2000, 100001, 400):
    if year == i:
        leap = True

print(leap)