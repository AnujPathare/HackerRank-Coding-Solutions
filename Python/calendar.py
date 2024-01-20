# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

days = list(calendar.day_name)
# print(A)

month, day, year = input().split()
month, day, year = int(month, 10), int(day, 10), int(year, 10)

print(days[calendar.weekday(year, month, day)].upper())
