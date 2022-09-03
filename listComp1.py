

x= int(input("x: "))   
y = int(input("Y: "))
z= int(input("z: "))

n= int(input('N:'))
LIST = []
for i in range(x+1): 
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k != n):
                LIST.append([i,j,k])
print(LIST)

               