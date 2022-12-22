import numpy as np
import math
from matplotlib import pyplot as plt 

def solution1D(b, partitionNumber,const1,const2):
    h = 1/(partitionNumber+1)
    # define the stifness matrix A 
    A = np.zeros((partitionNumber,partitionNumber))
    for i in range(0,partitionNumber):
        if i==0:
            A[i][i] = 2/h - const1/2 + (const2*h)/3
        elif i==partitionNumber-1:
            A[i][i] = 2/h + const1/2 +(const2*h)/3
        else:
            A[i][i] = 2/h + (2*h*const2)/3

    # top diagonal
    A[0][1] = -1/h + const1/2 - (const2*h)/6
    for i in range(2,partitionNumber):  
        A[i-1][i] = -1/h + const1/2 + (const2*h)/6

    # bottom diagonal
    for i in range(0,partitionNumber-1):
        A[i+1][i] = -1/h - const1/2 + (const2*h)/6

    print(A)
    # the problem now is reduced into solving a system of the form Ax = b 
    yNumerical = np.linalg.solve(A,b)
    # check if the solution is correct
    if not np.allclose(np.dot(A, yNumerical), b):
        print('Problem not solved')
        raise RuntimeError

    return yNumerical

if __name__ == "__main__":
    print("Enter the values of the constants B and C for the equation u''+Bu'+Cu = f(x), in that order: ")
    B = float(input())
    C = float(input())

    M = int(input("Enter the number of partitions, M: "))

    #input the data for the f function in the problem -u''+bu'+cu = f
    inputtype = int(input("Enter 1 if you'd like to specify a formula for f and 0 if you'd like to enter its values manually at each point of the partition: "))
    b = np.zeros(M)
    h = 1/(M+1)

    if inputtype == 0:
        print("Enter the values of f at the points specified by partition h: ")
        for i in range(0,M):
            b[i]=float(input())
    elif inputtype == 1:
        print("Enter the formula for the function f in terms of x, use math. or np. and name of the function: ")
        usersImput = input()
        usersFunction = lambda x: eval(usersImput)
        node = 0
        for i in range(0,M):
            b[i] = usersFunction(node)*h
            node = node + h
    else:
        print("Input type not valid, try again!")
        # check how to break from here

    yNumerical=np.zeros((M+2))
    yNumerical[1:M+1] =  solution1D(b,M,B,C)
    print(yNumerical)

    # plot the numerical solution
    x = np.linspace(0,1,M+2)
    plt.title("Numerical Solution vs Analytical") 
    plt.xlabel("x axis") 
    plt.ylabel("yNumerical axis") 
    plt.plot(x, yNumerical, color='r', label='Numerical')

    # xAnalytical = np.linspace(0,1,100)
    # yAnalytical = xAnalytical **2-xAnalytical 
    
    # # plot analytical solution to test for the case -u''+2u'+4u= 4x*2
    # plt.plot(xAnalytical, yAnalytical, color='g', label='Analytical')

    plt.show()


    plt.show()