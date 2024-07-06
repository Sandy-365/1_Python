
for i in range(20):
    for j in range(25):
        if((j==0 and i>5 and i<13) or (j==1 and i>8 and i<14) or
           (j==2 and i>9 and i<15) or (j==3 and i>10 and i<16) or
           (j==4 and i>10 and i<17)or (j==5 and i>9) or
           (i==19 and j>5 and j<8) or (i==19 and j>5 and j<7) or
           (j==6 and i>8 and i<18) or (j==7 and i>7 and i<17) or
           (j==8 and i>6 and i<17) or
           (j==9 and i>5 and i<17) or
           (j==10 and i>5 and i<17) or
           (j==11 and i>5 and i<18) or
           (j==12 and i>5 and i<24) or
           (i==19 and j>12 and j<15) or
           (i==20 and j>12 and j<14) or
           (j==13 and i>0 and i<16) or
           (j==14 and i<15) or
           (j==15 and i<14) or
           (j==16 and i<13) or
           (j==17 and i<12) or
           (j==18 and i<4) or (j==19 and i<4) or (j==20 and i<2) or (j==21 and i<2) or (j==22 and i<2) or (j==23 and i<2 and i>0) or (i==3 and j>19 and j<23) or (j==24 and i<3 and i>1) or (i==7 and j>16 and j<24) or (j==23 and i>7 and i<9)or (i==9 and j>16 and j<21) or (j==21 and i>8 and i<11)) :
            print("*",end="")
        else:
            print(end=" ")
    print()        



















































a=int(input("press enter to exit: "))
if a==0:
    exit()
