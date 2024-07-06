# palindrome

n=int(input("enter a number ::>> "))
a=n
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if a==rev:
    print(a,"is an palindrome number")
else:
    print(a,"is not a palindrome number")
