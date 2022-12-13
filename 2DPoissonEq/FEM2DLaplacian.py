import numpy as np
import math

M = int(input("Enter the number of partitions in each direction, M: "))
h = 1/(M+1)

#save the boundary data around the square (0,1)x(0,1) as specified below
inputtype = int(input("Enter 1 if you'd like to specify a formula for g and 0 if you'd like to enter its values manually at each point of the partition: "))

g1 = np.zeros(M+1)
g2 = np.zeros(M+1)
g3 = np.zeros(M+1)
g4 = np.zeros(M+1)

if inputtype==0:
    print("Enter the boundary data for y=0, x in [0,1): ")
    for i in range(0,M+1):
        g1[i] = float(input())
        
    print("Enter the boundary data for x=1, y in [0,1): ")
    for i in range(0,M+1):
        g2[i]=float(input())

    print("Enter the boundary data for y=1, x in (0,1] ")
    for i in range(0,M+1):
        g3[i]=float(input())

    print("Enter the boundary data for x=0, y in (0,1]: ")
    for i in range(0,M+1):
        g4[i]=float(input())
elif inputtype == 1:
    print("Enter the boundary function for y=0, x in [0,1) in terms of x: ")
    usersImput = input()
    usersFunction = lambda x: eval(usersImput)
    node = 0
    for i in range(0,M+1):
        g1[i] = usersFunction(node)
        node = node + h

    print("Enter the boundary function for x=1, y in [0,1) in terms of y: ")
    usersImput = input()
    usersFunction = lambda y: eval(usersImput)
    node = 0
    for i in range(0,M+1):
        g2[i] = usersFunction(node)
        node = node + h
    
    print("Enter the boundary function for y=1, x in (0,1] in terms of x: ")
    usersImput = input()
    usersFunction = lambda x: eval(usersImput)
    node = 0
    for i in range(0,M+1):
        g3[i] = usersFunction(node)
        node = node + h

    print("Enter the boundary function for x=0, x in (0,1] in terms of y: ")
    usersImput = input()
    usersFunction = lambda y: eval(usersImput)
    node = 0
    for i in range(0,M+1):
        g4[i] = usersFunction(node)
        node = node + h

