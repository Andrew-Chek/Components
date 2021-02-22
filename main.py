from math import *
x = input('Enter num x: ')
x = int(x)
y = input('Enter num y: ')
y = int(y)
z = pow(cos(x), 2) + pow(sin(y), 2)
print("z is: ", z)
N = input('Enter num N: ')
N = int(N)
s = 0
for i in range(N+1):
    s = s + pow(i, 2)
print("sum of elements in square is: ", s)