class A:
    def __init__(self,a,b):
        self.a = a #public
        self.__b = b #private
obj =A(33,66) 
print(obj.a)#accessable
print(obj.b)#un accessable
#print(obj._A__a)

class B:
    def __init__(self,a,b):
        self.__a = a #private
        self.__b = b#private
        
obj = B(100,600)
print(obj._B__a)#accessing via mangling
#OBJ._MYCLASS__PRIVATEVARIABLE