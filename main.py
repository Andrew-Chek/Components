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
if N > 0:
    for i in range(N+1):
        s = s + pow(i, 2)
    print("sum of elements in square is: ", s)
else:
    print("Error: number N can't be negative")

a = [-17, -1, 12, 4, 3, -12, 10, 6]
print(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
print("max of array is: ", max(a))
product = 1
for i in range(len(a)):
    product = product * a[i]
print(product)
ending = " "
for i in range(len(a)):
    if a[i] > 0:
        print(a[i], end=ending)
