class Student:
    #attributes
    student_name = "divya"
    student_email = "divya@gmail.com"
    
    #statement
    print(f"student name:{student_name}")
    print(f"student email :{student_email}")
    print("="*50)
    
    #function outside the class
    
def student_fun():
    #attributes
    student_name = "lucky"
    student_email = "lucky@gmail.com"
    
    #statement
    print("student name:",student_name)
    print("student_email:",student_email)
    
student_fun()#student call is must 
print("="*50)

#method type
class Student:
    #attributes
    student_name = "chinu"
    student_email="chinu@gmail.com"
    
    #method
    def info(self):
        print("student name :",{self.student_name})
        print("student email :",{self.student_email})
        print("="*50)
        print("student name:",self.student_name)
        print("student_email:",self.student_email)
        
#object
obj_one = Student()
obj_two = Student()
obj_three = Student()

#method calling is must and should
obj_one.info()
obj_two.info()
obj_three.info()

#another method type class
#class Student:
    #def info(self,student_id,student_name):
        #self.student_id = student_id
        #self.student_name = student_name
#obj_one = Student(101,"divya")
#obj_two = Student(102,"lucky")

#method calling
#obj_one.info()
#obj_two.info() this is wrong way to arrenge multiple students at a time for thart we can use constructor


#__init__constractor

class Student:
    def __init__(self,student_id,student_name):
        self.student_name = student_name
        self.student_id = student_id
    def info(self):
        print("student id :",self.student_id)
        print("student_name:",self.student_name)
obj_one = Student(101,"divya")
obj_three = Student(102,"lucky")

#method calling
obj_one.info()
obj_three.info()

#real world entity
class Student:
    #class variable is used across all class 
    
    institute_name = "edify"
    
    def __init__(self,student_name,student_email):
        if not Student.validate_email(student_email):
            raise ValueError("invalid email id")
        
        #attributes/variables
        self.student_name = student_name
        self.student_email = student_email
        
    def info(self):
    
        print("student name :",self.student_name)
        print("student email :", self.student_email)  
        print(" student institute name :",Student.institute_name)  
        
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        
    @staticmethod
    def validate_email(email):
         return "@"in email and "."in email          
        
obj_one = Student("divya","divya@gmail.com")
obj_two = Student("lucky","lucly@gmail.com")

#method calling
obj_one.info()
obj_two.info()

#change institute name 
Student.change_institute_name("digital edify")
obj_one.info()
obj_two.info()

#static method calling
print(Student.validate_email("divya@gmail.com"))
print(Student.validate_email("lucky"))


        
           