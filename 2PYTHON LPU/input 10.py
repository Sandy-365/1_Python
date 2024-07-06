l=[]
for i in range(1,11):
    a=input("enter the element : ")
    l.append(a)
print(sorted(l[::2],reverse=True))
print(sorted(l[1::2],reverse=True))
