# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
n = input()
n = complex(n)

print(abs(n))
print(cmath.phase(n))