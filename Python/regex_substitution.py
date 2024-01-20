# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    inp = input()
    inp = re.sub(r"(?<=\s)&&(?=\s)", 'and', inp)
    inp = re.sub(r"(?<=\s)\|\|(?=\s)", 'or', inp)
    print(inp)
    
# The above code runs for the test case

# # 1
# # c $&1|| || && && &|&&| & | | &&c


# The below code fails
# import re

# for _ in range(int(input())):
#     inp = input()
#     new = re.sub(r" && ", ' and ', inp)
#     new = re.sub(r" \|\| ", ' or ', new)
#     print(new)