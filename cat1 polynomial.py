n1=int(input("enter n1"))
n2=int(input("enter n2"))
l1=[1,2,4,0,3,1]
l2=[2,-3,-4]
l3=[]
if(n1>n2):
    x=n1-n2
    for i in range(0,x):
        l3.append(i*0)
    l=l3+l2
    for a in l1:
        b=l[l1.index(a)]
        print(a+b)
elif(n2>n1):
    y=n2-n1
    for j in range(0,x):
        l3.append(j*0)
    l=l3+l2
    for a in l1:
        b=l[l1.index(a)]
        print(a+b)
    
else:            
    for a in l1:
        b=l[l1.index(a)]
        print(a+b)
        
print(l1)
print(l2)
    




    
