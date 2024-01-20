import math

a = float(2)
b = float(1)
c = float(5)
d = float(6)

x = complex(a,b)
y = complex(c,d)
# print(f'{x:.2f}')
# print(x.real)
# x.real = 0.00 + x.real
# print(x.real)
mul = x/y
# if mul.imag <0:
#     print('neg')
# else:
#     print('pos')
print(x.mod())
print('%.2f%.2fi' % (mul.real, mul.imag))
# print(addition.real, addition.imag)
# print('%.2f+%.2fi' % (x.real, x.imag))
# class Complex(object):
#     xreal = None
#     ximg = None
#     yreal = None
#     yimg = None
#     count = 0
#     x = None
#     y = None

#     def __init__(self, real, imaginary):
#         if Complex.count == 0:
#             Complex.xreal = float(real)
#             Complex.ximg = float(imaginary)
#             Complex.count += 1
#         elif Complex.count == 1:
#             Complex.yreal = float(real)
#             Complex.yimg = float(imaginary)
#             Complex.x = complex(Complex.xreal, Complex.ximg)
#             Complex.y = complex(Complex.yreal, Complex.yimg)

#     def __add__(self, no):
#         print(Complex.x + Complex.y)

#     def __sub__(self, no):
#         print('sub')
        
#     def __mul__(self, no):
#         print('mul')
        
#     def __truediv__(self, no):
#         print('truediv')
        
#     def mod(self):
#         print('mod')
        
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')