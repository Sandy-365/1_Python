l1=list(input("enter any list items:::>>>"))
print('''
''')
print("the lenght of your list is :::>>>",len(l1) , " ' <<<::: to find the lenghth of list we use len() '")
print('''
''')
print("Here is your list:::>>>",l1 , " ' <<<::: to print your list u can simpliy use print(list name)'")
print('''
''')
a=input("enter your favroute number:::>>>")
print('''
''')
print("Let's check wheather your favroute number is there or not:::>>>",a in l1)
print('''
''')
l2=list(input("enter your second list:::>>>"))
print('''
''')
print("let's Concatenate your both lists:::>>>",l1 + l2)
print('''
''')
print("let's replicate your first and second list 2 times",l1*2,";;;",l2*2)
print('''
''')
#l1[0]=a
#print("let's remove first number and add your favroute number in your first list:::>>>",l1)
#print('''
#''')
print("here is the combination which can be made using list one and list two ")
for i in l1:
    for j in l2:
        print([i,j])
print("total no of combination is:::>>>",len(l1)*len(l2))
print('''
''')
l1.append(a)
print("let's add your favroute number in list one using append method",l1)
print('''
''')
l2 += a
print("let's add your favroute number in list two using += method",l2)



    






