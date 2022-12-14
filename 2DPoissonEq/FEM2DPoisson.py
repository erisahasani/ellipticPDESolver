import numpy as np

M = int(input("Enter the number of partitions in each direction, M: "))
N = (M)**2
h = 1/(M+1)

#save the data points for the right hand side of the equation, i.e the data for f
f = np.zeros(N)
inputtype = int(input("Enter 1 if you'd like to specify a formula for f and 0 if you'd like to enter its values manually at each point of the partition: "))

if inputtype==0:
    print("Enter data for f following the convention describen in the 2readme.md file: ")
    for i in range(0,M):
        f[i] = float(input())
elif inputtype==1:
    print("Enter function f in terms of x and y: ")
    usersImput = input()
    usersFunction = lambda x,y: eval(usersImput)
    xcoordinate = 0
    ycoordinate = 0
    for i in range(0,M):
        for j in range(0,M):
            f[j+i*M] = usersFunction(xcoordinate, ycoordinate)*(h**2)
            xcoordinate += h
        ycoordinate += h
