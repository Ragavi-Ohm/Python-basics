n=int(input("enter the value of n"))
a=[]
s=0
for j in range(0,n):
    a.append([])
    for i in range(0,n):
        x=int(input("enter the value of x"))
        a[i].append(x)
print(a)
for c in range(len(a)):
    for d in range(len(a[c])):
        if(c==d):
            s=s+a[c]
            for m in range(0,n-1):
                
            
              
