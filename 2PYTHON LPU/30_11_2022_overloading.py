class sandeep:
    def greet(self,name=None):
        print("\nI am in sandeep class")
        if name == None:
            print("welcome")
        else:
            print("welcome "+name)
class manish(sandeep):
    def greet(self,name=None):
        print("\nI am in manish class")
        if name==None:
            print("welcome")
            super().greet()
        else:
            print("wlecome "+name)
            super().greet()
            super().greet("ramjee")
obj=manish()
obj.greet()
print(".\n.\n............first call is over.........\n\n\n")
obj.greet("ramjee")
print(".\n.\n............second call is over..........")
