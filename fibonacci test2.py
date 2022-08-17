n=int(input("enter the value of n"))
a=0;b=1;sum=0;i=0
r=len(str(n))
l1=[0]
l=[]
l3=[]
while(i<=(n-2)):
    sum=a+b
    l.append(sum)
    a=b
    b=sum
    i=i+1
l2=l1+l
for j in l2:
    if str(j) in str(n):
        print(j)
    
