#program to check compare two given number nd disply the smallest one 
num1=float(input("Enter a number ::>> "))
num2=float(input("Enter a number ::>> "))
if num1<num2:
    print(num1)
elif num2<num1:
    print(num2)
else:
    print("both the number is equal")
