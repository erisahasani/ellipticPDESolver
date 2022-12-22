import FEM1D
import numpy as np
import math
from matplotlib import pyplot as plt 
from numpy import linalg

# A test case for the problem -u"-2u'-4u = -4x**2
def test_answer():
    M=1000
    h=1/(M+1)
    B= -2
    C= -4

    b = np.zeros(M)
    usersFunction = lambda x: eval('-4*x**2')
    node = 0
    for i in range(0,M):
        b[i] = usersFunction(node)*h
        node = node + h
    
    yNumerical = np.zeros(M+2) 
    yNumerical[1:M+1]= FEM1D.solution1D(b,M,B,C)
    yAnalytical = np.zeros(M+2)

    analyticalSol = lambda x: eval('x**2-x')
    node =0
    for i in range(0,M+2):
        yAnalytical[i] = analyticalSol(node)
        node = node+h
    
    yNumerical=np.zeros((M+2))
    yNumerical[1:M+1] =  FEM1D.solution1D(b,M,B,C)
    

    # plot the numerical solution
    x = np.linspace(0,1,M+2)
    plt.title("Numerical Solution vs Analytical") 
    plt.xlabel("x axis") 
    plt.ylabel("yNumerical axis") 
    plt.plot(x, yNumerical, color='r', label='Numerical')

    print('error', linalg.norm(yNumerical-yAnalytical))
    # plot analytical solution to test for the case u''+2u'+4u= 4x*2
    plt.plot(x, yAnalytical, color='g', label='Analytical')

    plt.show()


    assert np.allclose(yNumerical,yAnalytical,atol=1e-03)