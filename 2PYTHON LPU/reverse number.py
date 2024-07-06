r=0
rev=0
n=int(input("enter a number ::>> "))

while n>0 :
    r=n%10
    n=n//10
    rev=rev * 10 + r
    
    
