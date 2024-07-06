# armstrong

n=int(input("enter a number ::>> "))
a=n
ar=0

while n>0:
    r=n%10
    n=n//10

    ar+=(r**3)

if ar==a:
    print(a,"is armstrong number")
else:
    print(a,"is not a armstrong number")
