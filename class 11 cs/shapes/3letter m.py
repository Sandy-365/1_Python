for i in range(5):
    for j in range(5):
        if(j==0 or j==4 or (i-j==0 and i<3) or (i+j==4 and i<3)):
            print("*",end="")
        else:
            print(end=" ")
    print()        
a=int(input("enter 0 to exit: "))
if a==0:
    exit()
