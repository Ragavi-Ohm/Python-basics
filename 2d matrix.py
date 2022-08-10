n=int(input("enter the value of n"))
m=int(input("enter the value of m"))
a=[]
l=[]
count=0
for i in range(n):
    a.append([])
    for j in range(m):
        x=int(input("enter the value"))
        a[i].append(x)
for x in range(len(a)):
    for y in range(len(a[x])):
        if(a[x][y]==1):
            count=count+1
            l.append(count)
            
b=max(l)
