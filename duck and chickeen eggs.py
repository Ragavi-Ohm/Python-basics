n=int(input("enter the value of n"))
i=0
l=[]
l2=[]
l1=[]
l4=[]
while(i<n):
    num=input("enter the value of num")
    x=num[3:]
    t=num[:2]
    l.append(x)
    l2.append(t)
    i=i+1
for ch in l:
    y=int(ch)
    l1.append(y)
d=dict(zip(l1,l2))
for a in l1:
    for b in l1:
        r=l1.index(a)
        s=l1.index(b)
        u=sum(l1[:])-(l1[r]+l1[s])
        if(a+b==(u//2)):
            print(d[a],d[b])
            del d[b]
            del d[a]
            print(d)
            for i in d.values():
                print(i,end=' ')
            break;
       
          
           
            
            
