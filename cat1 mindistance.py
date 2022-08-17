n=int(input("enter n"))
i=0
l=[]
l1=[]
l2=[]
from math import sqrt
while(i<n):
    x=int(input("enter x"))
    y=int(input("enter y"))
    l.append((x,y))
    i=i+1
print(l)    
for i in l:
    for j in l[l.index(i)+1:]:
        d=sqrt((i[0]-j[0])**2+(i[1]-j[1])**2)
        l1.append((i,j))
        l2.append(d)
print(l1)
print(l2)
d=dict(zip(l2,l1))
s=min(l2)
print(d[s])
    


            
    
