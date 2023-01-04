import numpy as np
import math
import matplotlib.pyplot as plt


def solutionLaplacian2D(g,partitionNumber):
    N = (partitionNumber)**2
    A = np.zeros((N,N))
    b = np.zeros(N)

    # Define the matrix A based on the five point formula 
    for i in range(0,N):
        A[i][i] = 4
        if i+partitionNumber <N:
            A[i+partitionNumber][i] = -1
        if i- partitionNumber>=0:
            A[i-partitionNumber][i] = -1

    # lower diagonal
    for i in range(0,N-1):
        if (i+1)% partitionNumber !=0:
            A[i+1][i] = -1
    #upper diagonal
    for i in range(1,N):
        if (i)% partitionNumber !=0:
            A[i-1][i] = -1

    # since boundary conditions are added, we need to updte b
    b[0] = g[M][0] + g[M+1][1]
    b[M-1] = g[M+1][M] + g[M][M+1]
    b[N-M] = g[0][1] + g[1][0]
    b[N-1] = g[0][M] + g[1][M+1]

    # top and bottom of g
    for i in range(1,M-1):
        b[i] = g[M+1][i+1]
        b[N-M+i] = g[M+1][i+1]
        

    # left and right of g
    for i in range(2,M):
        b[N-i*M] = g[i+1][0]

    for i in range(1,M-1):
        b[N-i*M-1] = g[i+1][M+1]

    
    # the problem now is reduced into solving a system of the form Ax = b 
    yNumerical = np.linalg.solve(A,b)
    # check if the solution is correct
    if not np.allclose(np.dot(A, yNumerical), b):
        print('Problem not solved')
        raise RuntimeError
    return yNumerical


if __name__ == "__main__":

    M = int(input("Enter the number of partitions in each direction, M: "))
    h = 1/(M+1)

    #save the boundary data around the square (0,1)x(0,1) as specified below
    inputtype = int(input("Enter 1 if you'd like to specify a formula for g and 0 if you'd like to enter its values manually at each point of the partition: "))

    # we save the boundary data as an M by M matrix that has first and last columns and rows as the boundary data and is zero in the interior
    g = np.zeros((M+2,M+2))

    if inputtype==0:
        print("Enter the boundary data for y=0, x in [0,1): ")
        for i in range(0,M+2):
            g[M+1][i]=float(input())
            
            
        print("Enter the boundary data for x=1, y in [0,1): ")
        for i in range(0,M+2):
            g[i][M+1]=float(input())

        print("Enter the boundary data for y=1, x in (0,1] ")
        for i in range(0,M+2):
            g[0][i] = float(input())

        print("Enter the boundary data for x=0, y in (0,1]: ")
        for i in range(0,M+1):
            g[i][0]=float(input())
    elif inputtype == 1:
        print("Enter the boundary function for y=0, x in [0,1) in terms of x: ")
        usersImput = input()
        usersFunction = lambda x: eval(usersImput)
        node = 0
        for i in range(0,M+2):
            g[M+1][i] = usersFunction(node)
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
            g[0][i] = usersFunction(node)
            node = node + h

        print("Enter the boundary function for x=0, x in (0,1] in terms of y: ")
        usersImput = input()
        usersFunction = lambda y: eval(usersImput)
        node = 0
        for i in range(0,M+1):
            g[i][0] = usersFunction(node)
            node = node + h

        print("This is the matrix for g:")
        print(g)
        yNumerical = solutionLaplacian2D(g,M)


        # now we save the numerical solution in the interior of matrix g, i.e writting the solution in matrix form
        for i in range(1,M+1):
            for j in range(1,M+1):
                g[M-i+1,j] = yNumerical[(i-1)*M+j-1]


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
