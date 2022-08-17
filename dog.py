print("enter the value of n")
print("enter the value of r")
n=eval(input())
r=eval(input())
total=0
i=0
while(i<5):
    n=n+n*r
    total=total+n
    i=i+1
print(format(total,"0.2f"))
