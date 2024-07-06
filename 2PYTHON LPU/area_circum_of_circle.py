def ar(r):
    p=3.14
    if r<0:
        return
    else:
        return p*r*r, 2*p*r
n=eval(input("enter the radius of circle ::>> "))
r1,r2=ar(n)
print("area of circle is",r1)
print("circumference of circle is",r2)
