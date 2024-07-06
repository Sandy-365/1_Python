for i in range(4):
    for j in range(7):
        if(i+j==3 or i==3 or j-i==3):
            print("*",end="")
        else:
            print(end=" ")
    print()        
a=int(input("enter 0 to exit: "))
if a==0:
    exit()
