class A:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
obj = A (10,20)
print(obj.a)
print(obj.b)

#private

class A :
    def __init__(self,a,b):
        self.__a = a 
        self.b__ = b
        
obj = A (12,44)
#print(obj.a)
#print(obj.b)

print(obj._A__a)
print("="*50)

#protected
class A:
    def __init__(self,a,b):
        
      self._a = a
      self._b = b 
class B(A):
    def show(self):
        obj=A(20,30) 
        print(obj._a)
obj = B(333,44)
obj.show()
print(obj._a)


##no seter getter
class A:
    def __init__(self,name,marks):
         self.name = name 
         self.marks = marks
obj = A("divya",93)
print(obj.name)
print(obj.marks)

obj.marks = 22
print(obj.marks)

#with getter and setter

class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def display_info(self):
        print(f" hello {self.__name} has {self.__marks} marks")
    #setter
    def set_marks(self,marks):
        if marks>=0 and marks<=100: #or if 0<= marks<=100:
            self.__marks = marks
        else:
            print ("invalid marks")
    #getter
    def get_marks(self):
        return self.__marks
obj = Student("divya",44)
obj.display_info()
obj.set_marks(987)
obj.display_info()
print(obj.get_marks())

#propertys
class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
        
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,marks):
        if 0<= marks <=100:
            self.__marks = marks
        else:
            print("invalid marks")
            
obj = Student("divya",99)
print(obj.marks)

obj.marks = 444
print(obj.marks)


    
            
