import re

for i in range(int(input())):
    x = re.fullmatch("^[+-]?[0-9]*[.][0-9]+", input())
    print(bool(x))