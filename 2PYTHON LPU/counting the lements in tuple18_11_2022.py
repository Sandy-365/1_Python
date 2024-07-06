print("way 1")
d=tuple(map(int,input("data ::>> ").split(",")))
print("tuple ::>>",d)
e=int(input("element ::>> "))
l=len(d)
s=0
for i in range(l):
    if d[i]==e:
        s+=1
if s==0:
    print("enter valid element")
else:
    print("existed",s,"times")

print("\n")
print("way 2")
d=tuple(map(int,input("data ::>> ").split(",")))
print("tuple ::>>",d)
e=int(input("element ::>> "))
f=d.count(e)
if f==0:
    print("enter valid element")
else:
    print("existed",s,"times")
