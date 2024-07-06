a=int(input("enter its first length"))
b=int(input("enter its second length"))
c=int(input("enter its third length"))

# perimetere of triangel
p=(a+b+c)
print(p,"unit")

#area of triangle using heron's formula
s=(p)/2
ar=s*((s-a)*(s-b)*(s-c))**1/2
print(|ar|,"square unit")
