n=int(input("enter the value of n"))
a=0;b=1;sum=0;i=0
r=len(str(n))
l1=[0,1]
l=[]
l3=[]
while(i<(n-2)):
    sum=a+b
    l.append(sum)
    a=b
    b=sum
    i=i+1
l2=l1+l
t=n
for j in range(1,r+1):
    while(r%j==0):
        while(n!=0):
            mod=n%(10^j)
            l3.append(mod)
            n=n//(10^j)
        n=t    
        j=j+1        
for item in l2:
    for ch in l3:
        if(item==ch):
            print(ch)
            break;
            
    
    
        

