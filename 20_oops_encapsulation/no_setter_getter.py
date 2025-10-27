#with encapsulation and with setter - getter
class Student:
    def __init__(self,name,marks):
        self.name = name#private variable
        self.marks = marks#private variable
        
s1 = Student("ravi",77)
print(s1.name)
print(s1.marks)

s1.marks = -10
print(s1.marks)

s1.marks = 100
print(s1.marks)



