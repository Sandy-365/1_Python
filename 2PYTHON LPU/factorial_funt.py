def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
m=int(input("enter a number to in its factorial ::>> "))
print("factorial of",m,"is",fact(m))
