h = int(input("Enter the number of partitions in each direction, h: "))
#save the boundary data around the square (0,1)x(0,1) as specified below
g1 = []
g2 = [] 
g3 = [] 
g4 = []

print("Enter the boundary data for y=0, x in [0,1): ")
for i in range(0,h):
    g1.append(float(input()))
    
print("Enter the boundary data for x=1, y in [0,1): ")
for i in range(0,h):
    g2.append(float(input()))

print("Enter the boundary data for y=1, x in (0,1] ")
for i in range(0,h):
    g3.append(float(input()))

print("Enter the boundary data for x=0, y in (0,1]: ")
for i in range(0,h):
    g4.append(float(input()))
