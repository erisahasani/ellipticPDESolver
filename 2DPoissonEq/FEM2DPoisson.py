import numpy

M = int(input("Enter the number of partitions in each direction, M: "))

#save the data points for the right hand side of the equation, i.e the data for f
f = []
print("Enter the data for the function f: ")
for i in range(0,M+1):
    f.append(float(input()))
