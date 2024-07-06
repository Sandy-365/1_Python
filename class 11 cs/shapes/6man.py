for i in range(20):
    for j in range(15):
        if((i==0 and j>3 and j<10))or((j==3 or j==10) and (i<4)) or (i==3)or(i-j==3 and i<8) or(i+j==17 and i<8) or (i+j==13 and i>7) or (j-i==1 and i>7) or (i==13)or (i==8 and j>5 and j<10) or ((j==14 or j==0) and i>2 and i<9) or (i==1 and j>4 and j<6) or (i==1 and j>7 and j<9)or (i==2 and j>5 and j<8)or  ((j==4 or j==10) and i>12) or (i==19 and j>4 and j<7) or (i==19 and j>10 and j<13):
            print("#",end="")
        else:
            print(end=" ")
    print()
a=int(input("enter 0 to exit: "))
if a==0:
    exit()
