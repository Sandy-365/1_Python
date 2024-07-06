x=int(input("press 1 to convert from fahrenheit to celsius" "press 2 to convert from celsius to fahrenheit.            "))
y=int(input("ask what number?           "))
if x==1:
    c=5/9*(y-32)
    print (c)
elif x==2:
    f=9/5*(y+32)
    print (f)
else :
    print("please enter either 1 or 2")
