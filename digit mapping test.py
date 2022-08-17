str=input("enter the value of str")
r=len(str)
l=[]
l1=[]
i=0
for ch in str:
    l.append(ch)
from math import sqrt
a=int(sqrt(10**r-1))
t=a
while(i<t):    
    b=t-i
    x=b**2
    while(x!=0):
        mod=x%10
        l1.append(mod)
        x=x//10
        
        p=l1[::-1]
    for ch in l:
        for j in p:
            if(p.count(j)==1):
                i=i+1
    break;

            if(p.count(j)==1):
                print(ch,j)
            
                        
