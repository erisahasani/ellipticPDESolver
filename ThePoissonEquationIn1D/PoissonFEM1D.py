import numpy as np
import math

h = int(input("Enter the number of partitions, h: "))

#input the data for the f function in the problem -u'' = f
inputtype = int(input("Enter 1 if you'd like to specify a formula for f and 0 if you'd like to enter its values manually at each point of the partition: "))
f = np.zeros(h+1)

if inputtype == 0:
    print("Enter the values of f at the points specified by partition h: ")
    for i in range(0,h+1):
        f[i]=float(input())
elif inputtype == 1:
    print("Enter the formula for the function f in terms of x: ")
    usersImput = input()
    usersFunction = lambda x: eval(usersImput)
    node = 0
    for i in range(0,h+1):
        f[i] = usersFunction(node)
        node = node + 1/h
else:
    print("Input type not valid, try again!")

print(f)
# define the stifness matrix A 
A = np.zeros((h+1,h+1))
for i in range(0,h+1):
    A[i][i] = 2

for i in range(0,h):
    A[i+1][i] = -1

for i in range(1,h+1):
    A[i-1][i] = -1

# define the right hand side of the matrix equation Ax=b, which is just h^2*f
b = np.zeros(h+1)
for i in range(0,h+1):
    b[i] = f[i]*(h**2) 
