for i in range(5):
    for j in range(11):
        if(j==0 or j==4 or (i-j==0 and i<3) or (i+j==4 and i<3)) or((i==0 or i==4 or i==2) and (j>5 and j<11))or ((j==6 and i<3) or (j==10 and i>2)) :
            print("#",end="")
        else:
            print(end=" ")
    print()
a=int(input("enter 0 to exit: "))
if a==0:
    exit()
    
