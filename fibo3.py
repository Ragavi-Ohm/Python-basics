n=int(input("enter the value of n"))
a=0;b=1;sum=0;i=0
r=len(str(n))
while(sum<=(n-2)):
    sum=a+b
    if str(sum) in str(n):
        print(sum)
        
    a=b
    b=sum
    
        
