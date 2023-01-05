#this is a test file, it can run using pytest filename
import FEM2DPoisson
import numpy as np

# A test case for -Δu = -2x(x-1) - 2y(y-1) which has the analytical solution u = x(x-1)y(y-1)
def test_answer():
    M = 100
    h = 1/(M+1)
    b = np.zeros(M**2)
    usersFunction = lambda x,y: eval('-2*x*(x-1)-2*y*(y-1)')
    
    ycoordinate = h
    for i in range(0,M):
        xcoordinate = h
        for j in range(0,M):
            # here we multiply by a factor of h**2 because b_i = f_i*h**2
            b[j+i*M] = usersFunction(xcoordinate, ycoordinate)*(h**2)
            xcoordinate += h
        ycoordinate += h

    yNumerical = FEM2DPoisson.solutionPoisson2D(M,b)

    # we perform the reveersed operations to lines 22-28 in order to put the solution data in a matrix
    yNumericalMatrixform = np.zeros((M+2,M+2))
    for i in range(1,M+1):
        for j in range(1,M+1):
            yNumericalMatrixform[M-i+1,j] = yNumerical[(i-1)*M+j-1]


    yAnalyticalMatrixform = np.zeros((M+2,M+2))
    nodeX = h
    nodeY = h
    for i in range(1,M+1):
        nodeX = h
        for j in range(1,M+1):
            yAnalyticalMatrixform[M-i+1,j] = nodeX*(nodeX-1)*nodeY*(nodeY-1)
            nodeX += h
        nodeY += h 
    
    assert np.allclose(yNumericalMatrixform,yAnalyticalMatrixform)
    
