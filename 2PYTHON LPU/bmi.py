#program to clculate bmi
w=float(input("Enter your weight in pound ::>> "))
h=float(input("Enter your height in inches ::>>"))

w*=0.45359237
print(w)
h*=0.0254

bmi=w/(h*h)
print(bmi)

if bmi < 18.5:
    print("under weight")
elif bmi < 25:
    print("normal")
elif bmi <30:
    print("overweight")
else:
    print("obese")
