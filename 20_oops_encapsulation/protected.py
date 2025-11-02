class A :
    def __init__(self,a,b):
        self._a = a #proteacted
        self._b = b #protected
        
obj =  A(12,22)
#print(obj.a)#not accessible
#print(obj.b)# not accessible

class A:
    def __init__(sel,a,b):
        self._a = a 
        self._b = b 
class B(A):
    def show(self):
        print("super")
obj = B(22,33)
#obj.show()

class A:
    def __init__(self,a,b):
        self._a = a 
        self._b = b 
class B(A):
    def showA(self):
        a = A(20,30)
        print(a._a)
obj = B(22,33)
obj.showA()
