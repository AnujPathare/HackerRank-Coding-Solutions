# Enter your code here. Read input from STDIN. Print output to STDOUT

import email.utils
import re


for _ in range(int(input())):
    inp = input()
    uname, emailadd = email.utils.parseaddr(inp)
    if uname and re.match(r"^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$", emailadd):
        print(inp)