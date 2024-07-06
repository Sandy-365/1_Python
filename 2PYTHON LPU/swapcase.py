s=input("string ::>> ")
m=[]
for i in s:
    n=ord(i)
    m.append(n)
min1=min(m)  
max1=max(m)

print("character with min value ::>> ",chr(min1))
print("charachret with max value ::>> ",chr(max1))
