
Digit Mapping for Characters
Given a string S with distinct letter find a mapping for each letter in it such that the number formed by replacing the letter with the numbers is a largest possible perfect square with different digits.

A number is said to be perfect square if the number is square of an integer. For example, if the word given is ‘care’ then the following map shall be done for the characters:

c – 9

a – 8

r – 0

e – 1

The number 9801 is a perfect square since 992 is 9801.

Input Format

First line contains the string for which numbers are to be assigned for characters

Output Format

Print character of the string and the number mapped for it separated by a space

Theme:

Terminal
Language

C++
Font size:

18
Status















str=input("enter the value of str")
r=len(str)
l=[]
l1=[]
i=0
for ch in str:
    l.append(ch)
from math import sqrt
a=int(sqrt(10**r-1))
t=a
while(i<t):    
    b=t-i
    x=b**2
    while(x!=0):
        mod=x%10
        l1.append(mod)
        x=x//10
        
        p=l1[::-1]
    for ch in l:
        for j in p:
            if(p.count(j)!=1):
                i=i+1
    break;

            else:
                print(ch,j)
            
            
        #i=i+1
#print(p)        
        #for ch in l:
         #   for j in p:
               
        #break;
                    
       # i=i+1    
                
      
                
        
