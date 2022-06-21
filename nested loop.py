for i in range(1,6):
    for j in range(0,5):
        if i==2 or j==2 or( i==1 and j==1 or(j==3)) or (j==5 and i==4 or i==5)
              print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
