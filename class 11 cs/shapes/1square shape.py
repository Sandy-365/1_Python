for i in range(6):
    for j in range(11):
        if(i==0 or i==5 or j==0 or j==10):
            print("*",end="")
        else:
            print(end=" ")
    print()        
a=int(input("enter 0 to exit: "))
if a==0:
    exit()
