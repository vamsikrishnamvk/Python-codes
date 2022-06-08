
x = int(input())
y = int(input())
z = int(input())
n = int(input())

a=list()    
for i in range(x+1):
    for j in range(y+1):  
        for k in range(z+1):
            if(x+y+z)!=n:
                a.append([i,j,k])
print(a)