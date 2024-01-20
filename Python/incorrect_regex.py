import re
try:
    print(bool(re.compile(input())))
except re.error:
    print('False')