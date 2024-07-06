#progrm to calculat ethe electricity bill
a=int(input("Enter your Electricity unit ::>> "))
if a>=1 and a<=100:
    print("Your electricity bill is",a*1.5)
elif a>=101 and a<=200:
    print("Your electricity bill is",a*2.5)
elif a>=201 and a<=300:
    print("Your electricity bill is",a*4)
elif a>=301 and a<=350:
    print("Your electricity bill is",a*5)
else:
    print("Your electricity bill is",a*15)
    
