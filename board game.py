n=int(input("enter the value of n"))
b=input("enter the value of b")
print(b)
x=b[0]+b[1]+str(int(b[2])-1)
print(x)
print("1
Win in a Board Game
In a board game, a pXp board is given and the cells of the board are numbered as follows.

 

3,0

3,1

3,2

3,3

2,0

2,1

2,2

2,3

1,0

1,1

1,2

1,3

0,0

0,1

0,2

0,3

The movement of the coin in the board allowed are left, right, up and down. The coin movements are defined in the below table:

Movement

Current Position

Position after move

Left

m, n

m, n-1 if n>0

m, n otherwise

Right

m, n

m, n+1 if n<p-1

m, n otherwise

Up

m, n

m+1, n if m<p-1

m, n otherwise

Down

m, n

m-1, n if m>0

m, n otherwise

Given a size the board, p, initial cell of the coin in the board, a list of movements and a winning cell in the board, write a code to check if the coin reaches the winning cell from initial cell by these movements. If the winning position is reached then print Win and print Loss otherwise.

Input Format

Dimension of the board, p

Initial cell of the coin m,n separated by a space

Number of moves, num1

Next num1 lines contain the movements l-left, r-right, u-up and d-down

Winning cell of the coin m1, n1 separated by a space

Output Format

Print Win or Loss

Theme:

Terminal
Language

Python
Font size:

18
            new_pos=m[0]+m[1]+str(int(m[2])+1)
code:::::
     p=int(input())
m=input()
num1=int(input())
i=0
while(i<num1):
    moves=input()
    if(moves=='l'):
        if(int(m[2])>0):
            new_pos=m[0]+m[1]+str(int(m[2])-1)
        else:
            new_pos=m[:]
    elif(moves=='r'):
        if(int(m[2])<p-1):
            new_pos=m[0]+m[1]+str(int(m[2])+1)
        else:
            new_pos=m[:]
    elif(moves=='u'):
        if(int(m[0])<p-1):
            new_pos=str(int(m[0])+1)+m[1]+m[2]
        else:
            new_pos=m[:]
    elif(moves=='d'):
        if(int(m[0])>0):
            new_pos=str(int(m[0])-1)+m[1]+m[2]
        else:
            new_pos=m[:]
    m=new_pos
    new_pos=''
    i=i+1
win=input()    
if(m==win):
    print("Win")
else:
    print("Loss") 


