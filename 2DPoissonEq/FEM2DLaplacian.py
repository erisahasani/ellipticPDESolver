import numpy as np
import math
import matplotlib.pyplot as plt

M = int(input("Enter the number of partitions in each direction, M: "))
h = 1/(M+1)

#save the boundary data around the square (0,1)x(0,1) as specified below
inputtype = int(input("Enter 1 if you'd like to specify a formula for g and 0 if you'd like to enter its values manually at each point of the partition: "))

# we save the boundary data as an M by M matrix that has first and last columns and rows as the boundary data and is zero in the interior
g = np.zeros((M+2,M+2))

if inputtype==0:
    print("Enter the boundary data for y=0, x in [0,1): ")
    for i in range(0,M+2):
        g[0][i] = float(input())
        
    print("Enter the boundary data for x=1, y in [0,1): ")
    for i in range(0,M+2):
        g[i][M+1]=float(input())

    print("Enter the boundary data for y=1, x in (0,1] ")
    for i in range(0,M+2):
        g[M+1][i]=float(input())

    print("Enter the boundary data for x=0, y in (0,1]: ")
    for i in range(0,M+2):
        g[i][0]=float(input())
elif inputtype == 1:
    print("Enter the boundary function for y=0, x in [0,1) in terms of x: ")
    usersImput = input()
    usersFunction = lambda x: eval(usersImput)
    node = 0
    for i in range(0,M+2):
        g[0][i] = usersFunction(node)
        node = node + h

    print("Enter the boundary function for x=1, y in [0,1) in terms of y: ")
    usersImput = input()
    usersFunction = lambda y: eval(usersImput)
    node = 0
    for i in range(0,M+2):
        g[i][M+1] = usersFunction(node)
        node = node + h
    
    print("Enter the boundary function for y=1, x in (0,1] in terms of x: ")
    usersImput = input()
    usersFunction = lambda x: eval(usersImput)
    node = 0
    for i in range(0,M+2):
        g[M+1][i] = usersFunction(node)
        node = node + h

    print("Enter the boundary function for x=0, x in (0,1] in terms of y: ")
    usersImput = input()
    usersFunction = lambda y: eval(usersImput)
    node = 0
    for i in range(0,M+2):
        g[i][0] = usersFunction(node)
        node = node + h

    print(g)

    # Plot the boundary data for a visual representation
    x = np.linspace(0,1,M+2)
    y = np.linspace(0,1,M+2)

    X,Y = np.meshgrid(x,y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, g, 100, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()
