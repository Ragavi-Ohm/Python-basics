#given a number n,print the frequency of a digit k if it is present in n,
#else print no if k is not present in n
print("enter the value of n")
n=int(input())
print("enter the value of k")
k=int(input())
count=0
while(n!=0):
    mod=n%10
    if(mod==k):
        count=count+1
    n=n//10
if(count==0):
    print("no")
else:
    print(count)
