class A:
    def __init__(self,a,b):
        self.a = a 
        self.__b = b 
obj = A(9,8)
print(obj.a)
#print(obj.b)

# to access the private variable use below process

class B :
    def __init__(self,a,b):
        self.a = a 
        self.__b = b 
obj = B(10,3)
print(obj.a)
print(obj._B__b)
#print(obj._myclass_variable)