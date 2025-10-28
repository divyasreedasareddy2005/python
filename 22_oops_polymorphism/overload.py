#traditional overloading

class Mathops:
    def add (self,a,b):
        return a+b
    def add (self,a,b,c):
        print( a+b+c)
    
    
obj = Mathops()
#print(obj.add(10,20))TypeError: Mathops.add() missing 1 required positional argument: 'c'
obj.add(10,20,30)

class Maths:
    def add(self,a=0,b=0,c=0):
        return a+b+c
obj= Maths()
print(obj.add(10))#10+0+0
print(obj.add(10,20))#10+20+0
print(obj.add(144,5,3))#144+5+3
print(obj.add(10,3,2,4))#typeerror: Maths.add() takes from 1 to 4 positional arguments but 5 were given
