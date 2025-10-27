
class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
        
         
    #@property->which is like getter
    @property
    def mark(self):
        return self.__marks
  
        
    #@value.setter -> which is like setter
    @marks.setter
    def marks(self,marks):
        if 0<= marks <=100:
            self.__marks = marks
        else:
            print("invalid marks , only 0-100 allowed")
        
    
s1 = Student("ravi",95)
print(s1.marks)
        
        