for i in range(7):
    for j in range(5):
        if (j==0 or j== 4)or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
            print("s",end="")
        else:
            print(end=" ")
    print()
            
