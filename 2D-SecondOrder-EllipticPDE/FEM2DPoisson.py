import numpy as np
import math
import matplotlib.pyplot as plt
from boundaryDataAndRHS import boundary_data, vector_b

def solutionPoisson2D(partitionNumber,b):
    N = (partitionNumber)**2
    A = np.zeros((N,N))
 
    # Define the stifness matrix A
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
    
    # the problem now is reduced into solving a system of the form Ax = b 
    yNumerical = np.linalg.solve(A,b)
    # check if the solution is correct
    if not np.allclose(np.dot(A, yNumerical), b):
        print('Problem not solved')
        raise RuntimeError
    return yNumerical


if __name__ == "__main__":

    M = int(input("Enter the number of partitions in each direction, M: "))
    N = (M)**2
    h = 1/(M+1)

    
    g = boundary_data(M)
    b = vector_b(M,g)
    yNumerical = solutionPoisson2D(M,b)

    # now we save the numerical solution in the interior of matrix g, i.e writting the solution in matrix form
    for i in range(1,M+1):
        for j in range(1,M+1):
            g[M-i+1,j] = yNumerical[(i-1)*M+j-1]

    # Finally, we plot the solution
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
