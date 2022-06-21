'''for i in range(1,10):
    print(i)
o/p :1,2,3,4,5,6,7,8,9
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
o/p:-
12345
1234
123
12
1

for i in range(1,6):
    for j in range(1,7-i):
        print(i,end="")
    print()
o/p
11111
2222
333
44
5
for i in range(70,65,-1):
    for j in range(65,i):
        if i%2==0:
            print(chr(j),end="")
        else:
            print(chr(j+32),end="")
    print()        
o/p:-
ABCDE
abcd
ABC
ab
A           

for i in range(70,65,-1):
    for j in range(65,i):
        k=65
        if i%2==0:
            print(chr(j),end=" ")
        else:
            print(chr(k+32),end=" ")
    print()    
o/p:-
A B C D E 
a a a a 
A B C 
a a 
A       

for i in range(1,6):
    for j in range(1,7-i):
        
        if i%2==0:
            print(j,end=" ")
        else:
            print(6-i,end=" ")
    print()    
o/p:-
5 5 5 5 5 
1 2 3 4 
3 3 3 
1 2 
1     '''

for i in range(0,6):
    a=1
    b=0
    for j in range(1,6-i):
        if j%2==0:
            print(b,end="")
            b=1
        else:
            print(a,end="")
            a=0
    print()








    



