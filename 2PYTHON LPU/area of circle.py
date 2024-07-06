def area(radius,pi=3.14):
    if radius < 0:
        return 
    else:
        ar=pi*radius*radius
        return ar
radius=float(input("enter the radius of circle ::>> "))
s = area(radius)
print(s)
