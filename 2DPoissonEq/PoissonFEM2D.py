import numpy
# Here we solve the problem -Δu = f in a box (0,1)x(0,1) with u=0 on the boundary
# For a better understanding, read also the file 1readme.md in the same folder

h = int(input("Enter the number of partitions in each direction, h: "))

#save the data points for the right hand side of the equation, i.e the data for f
f = []
print("Enter the data for the function f: ")
for i in range(0,h):
    f.append(float(input()))
