#binary prob---pat4
n=int(input("enter the nos"))
i=0
l=[]
l1=[]

l2=[]
while(i<n):
    num=input("enter the num")
    l1.append(int(num))
    l.append(int(num,2))
    i=i+1
print(l1)
print(l)
d=dict(zip(l,l1))
def bsort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
print(bsort(l))
for w in bsort(l):
    l2.append(d[w])
print(l2)    
                
