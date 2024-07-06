
def rm(s):
    ns=""
    for i in s:
        if i != " ":
            ns=ns+i

        else:
            continue
    print(ns)
    
s=input("enter a string ::>> ")
rm(s)

