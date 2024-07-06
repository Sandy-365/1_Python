"""
        *
       * *
      * * *
     * * * *
    * * * * *
    
        """
n=int(input("enter the number of lines ::>> "))

for i in range(1,n):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
