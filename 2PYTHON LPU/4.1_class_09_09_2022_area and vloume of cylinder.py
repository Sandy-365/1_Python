# program to calculate the area and volume of cylinder

rad=input("Enter the radius of cylinder ::>> ")       #taking input from user radius
height=input("Enter the height of cylinder ::>> ")    #taking input from user height
pi=3.14

rad=float(rad)         #converting string into float
height=float(height)   #converting string into float


area=rad*rad*pi       #formula for calculating area
vol=area*height       #formula for calculating volume

print("The area of cylinder is ::>>",area)      #printing the area
print("The volume of cylinder is ::>> ",vol)    #printing the volume


