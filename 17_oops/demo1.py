
# __init__()-> constructor
class Student:
    #constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    #method
    def info(self):
        #student_email = "john@gmail.com"
        print("student name :",self.student_name)
        print("student email",self.student_email)


one_obj = Student("ravi","ravi@gmail.com")
two_obj = Student("divya","divya@gmail.com")
three_obj = Student("yamini","yamini@gmail.com")

#method calling
one_obj.info()
two_obj.info()
three_obj.info()
print("="*50)

#__init__()-> constructor
class Student:
    
    #class variable is shared across all objects
    institute_name = "edify"

    #constructor
    def __init__(self,student_name,student_email):
       if not Student.validate_email(student_email):
           raise ValueError("Invalid email address")
       #instance variables
       self.student_name = student_name 
       self.student_email = student_email  
    
    #instance method
    def info (self):
        #student_email = "divya@gmail.com"
        #accesing instance variables
        print("student name:",self.student_name)
        print("student email:",self.student_email)

        ##accessing class variables
        print("student institute:",Student.institute_name)#recommended
        #print("student institute via object:",self.institute_name)#not recommended

    #class method
    @classmethod
    def change_institute(cls,new_name):
        cls.institute_name = new_name #recommended
        #student.institute_name = new_name
        #accesing instance data inside a class method is not possible
        #print("accesing instance data :",self.student_name)

    #static method -> utility
    @staticmethod
    def validate_email(email):
        return "@" in email and "."in email
        
ravi_obj = Student("ravi","ravi@gmail.com")
divya_obj = Student("divya","divya@gmail.com")
yamini_obj = Student("yamini","yamin@gmail.com")
#method calling
ravi_obj.info()
divya_obj.info()
yamini_obj.info()

print("="*50)

#change the institute
Student.change_institute(" digital edifi")

ravi_obj.info()
divya_obj.info()
yamini_obj.info()

#calling static method
print(Student.validate_email("test@gmail.com"))
print(Student.validate_email("test"))