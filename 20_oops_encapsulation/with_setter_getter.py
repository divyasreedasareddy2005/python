#with seter and getter

class Student:
    def __init__(self,name,marks):
        self.__name = name#private variable
        self.__marks = marks#private variable
        
    def display_info(self):
        print(f"{self.__name} has {self.__marks} marks")
    
    #setter
    def set_marks(self,marks):
        if 0 <= marks <=marks:
            self.__marks = marks
        else:
            print("invalid marks ,only 0 to 100  allowed")
            
    #getter
    def get_marks(self):
        return self.__marks
    
s1 = Student("ravi",77)
#s1.display_info()

s1.set_marks(200)
print(s1.get_marks())
        
