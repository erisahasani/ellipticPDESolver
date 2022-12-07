import numpy
# Here we solve the problem -Δu = 0 in a box (0,1)x(0,1) and specified boundary conditions 

h = int(input("Enter the number of partitions in each direction, h: "))
f1 = []
f2 = [] 
f3 = [] 
f4 = []

# first save the boundary data around the square formed by (0,1)x(0,1)
print("Enter the boundary data for y=0, x in [0,1): ")
for i in range(0,h):
    f1.append(float(input()))
    
print("Enter the boundary data for x=1, y in [0,1): ")
for i in range(0,h):
    f2.append(float(input()))

print("Enter the boundary data for y=1, x in (0,1] ")
for i in range(0,h):
    f3.append(float(input()))

print("Enter the boundary data for x=0, y in (0,1]: ")
for i in range(0,h):
    f3.append(float(input()))
