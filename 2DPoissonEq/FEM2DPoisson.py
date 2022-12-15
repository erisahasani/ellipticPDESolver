import numpy as np
import matplotlib.pyplot as plt
import math

M = int(input("Enter the number of partitions in each direction, M: "))
N = (M)**2
h = 1/(M+1)

#save the data points for the right hand side of the equation, i.e the data for f
b = np.zeros(N)
inputtype = int(input("Enter 1 if you'd like to specify a formula for f and 0 if you'd like to enter its values manually at each point of the partition: "))

if inputtype==0:
    print("Enter data for f following the convention describen in the 2readme.md file: ")
    for i in range(0,M):
        # here we multiply by a factor of h**2 because b_i = f_i*h**2
        b[i] = float(input())*(h**2)
elif inputtype==1:
    print("Enter function f in terms of x and y: ")
    usersImput = input()
    usersFunction = lambda x,y: eval(usersImput)
    
    ycoordinate = h
    for i in range(0,M):
        xcoordinate = h
        for j in range(0,M):
             # here we multiply by a factor of h**2 because b_i = f_i*h**2
            b[j+i*M] = usersFunction(xcoordinate, ycoordinate)*(h**2)
            xcoordinate += h
        ycoordinate += h

# Define the matrix A based on the five point formula 
A = np.zeros((N,N))
for i in range(0,N):
    A[i][i] = 4/h
    if i+M <N:
        A[i+M][i] = -1/h
    if i-M >=0:
        A[i-M][i] = -1/h

for i in range(0,N-1):
    if (i+1)%M !=0:
        A[i+1][i] = -1/h

for i in range(1,N):
    if (i)%M !=0:
        A[i-1][i] = -1/h

# the problem now is reduced into solving a system of the form Ax = b 
yNumerical = []
yNumerical = np.linalg.solve(A,b)

# check if the solution is correct
print(np.allclose(np.dot(A, yNumerical), b))

# we perform the reveersed operations to lines 22-28 in order to put the solution data in a matrix
yNumericalMatrixform = np.zeros((M+2,M+2))
for i in range(1,M+1):
    for j in range(1,M+1):
        yNumericalMatrixform[M-i+1,j] = yNumerical[(i-1)*M+j-1]



# plot the numerical solution
x = np.linspace(0,1,M+2)
y = np.linspace(0,1,M+2)

X,Y = np.meshgrid(x,y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, yNumericalMatrixform, 100, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()