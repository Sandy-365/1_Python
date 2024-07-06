import math
a=int(input("enter the first side     "))
b=int(input("enter the second side      "))
c=int(input("enter the third side      "))
if a and b and c < 10:
    pt=a+b+c
    print(pt,"perimeter")
else:
    pt=a+b+c
    at=math.sqrt(pt/2*(pt/2-a)*(pt/2-b)*(pt/2-c))
    print(at,"area")

