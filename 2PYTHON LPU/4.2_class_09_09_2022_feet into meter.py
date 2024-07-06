# program that read a number in feet convert it into meters and didsplay the result



feet=input("Enter the value for feet ::>> ")   # taking the input from user

feet=float(feet)     #converting string into float value

meter= feet * 0.305  #converting feet into meter as (1feet = 0.305meter)


print(feet,"feet is ",meter,"meters")   # printing the result
