import numpy as np
import math
from matplotlib import pyplot as plt 

M = int(input("Enter the number of partitions, M: "))

#input the data for the f function in the problem -u'' = f
inputtype = int(input("Enter 1 if you'd like to specify a formula for f and 0 if you'd like to enter its values manually at each point of the partition: "))
f = np.zeros(M+1)
h = 1/(M+1)

if inputtype == 0:
    print("Enter the values of f at the points specified by partition h: ")
    for i in range(0,M+1):
        f[i]=float(input())
elif inputtype == 1:
    print("Enter the formula for the function f in terms of x, use math. or np. and name of the function: ")
    usersImput = input()
    usersFunction = lambda x: eval(usersImput)
    node = 0
    for i in range(0,M+1):
        f[i] = usersFunction(node)
        node = node + h
else:
    print("Input type not valid, try again!")
    # check how to break from here

# define the stifness matrix A 
A = np.zeros((M+1,M+1))
for i in range(0,M+1):
    A[i][i] = 2/h**2

for i in range(0,M):
    A[i+1][i] = -1/h**2

for i in range(1,M+1):
    A[i-1][i] = -1/h**2

# define the right hand side of the matrix equation Ax=b, which is just h^2*f
b = np.zeros(M+1)
for i in range(0,M+1):
    b[i] = f[i]

# the problem now is reduced into solving a system of the form Ax = b 
yNumerical = []
yNumerical = np.linalg.solve(A,b)

# check if the solution is correct
print(np.allclose(np.dot(A, yNumerical), b))




# plot the numerical solution
x = np.arange(0,1,h)
plt.title("Numerical Solution vs Analytical") 
plt.xlabel("x axis") 
plt.ylabel("yNumerical axis") 
plt.plot(x, yNumerical, color='r', label='Numerical')

plt.show()