m=int(input("enter m"))
n=int(input("enter n"))
count=0
i=1
j=1
l1=[]
l2=[]
while(i<=m):
    if(m%i==0):
        l1.append(i)
    i=i+1
while(j<=n):
    if(n%j==0):
        l2.append(j)
    j=j+1
print(l1)
print(l2)
for x in l1:
    if x in l2:
        count=count+1
if(x==1 and count==1):
    print("Not coprime")
else:
    print("Coprime")
    
            

            
