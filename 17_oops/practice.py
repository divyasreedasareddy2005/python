#oops basic
data = 10
print(type(data))

class employe:
    pass
emp_obj = employe()
#print(type(emp_obj)) <class '__main__.employe'>

# real world entity
class Student:
    student_id = 101
    student_name = "divya"
    
    #statement
    print("student id :",student_id)
    print("student name:",student_name)
    print("="*50)

#function (out side the class)
def student_fun():
    student_id = 102
    student_name = "yamin"
    #statement
    print("student id :",student_id)
    print("student name :",student_name)
#function call is must and should
student_fun()
print("="*50)

#real world entity 2
class employe:
    #variables/attributes
    employe_id = 103
    employe_name = "sai"
    #method
    def info(self):
        print("employe id :",self.employe_id)
        print("employe name :", self.employe_name)
        
#object cal 
one_object = employe()
two_object = employe()
three_object = employe()

#method cal
one_object.info()
two_object.info()
three_object.info()
print("="*50)

#__init__ constructor
class School:
    #variable
    principal_name = "sree lakshmi"
    
    #constructor
    def __init__(self,class_name,class_teacher):
        if not School.validate_class_teacher(class_teacher):
            raise ValueError("invalid class teacher")
        
        #variables/attributes
        self. class_name = class_name
        self.class_teacher= class_teacher
        
        #instance method
    def info(self):
        print("class name :",self.class_name) 
        print("class teacher :",self.class_teacher)
        print("principal name:",School.principal_name)
            
    #class method
            
    @classmethod
    def change_principal_name (cls,new_name):
        cls.principal_name = new_name
        
    #static method
    @staticmethod
    def validate_class_teacher(class_teacher):
        return "dasareddy"in class_teacher
    
divya_obj = School("class 9th","lakshmi kumari dasareddy")
yamini_obj = School("class 9th","lakshmi kumari dasareddy")
sai_obj = School("class 9th","lakshmi kumari dasareddy")

#method call
divya_obj.info()
yamini_obj.info()
sai_obj.info()
print("="*50)

#change principal name 
School.change_principal_name("sharada")
divya_obj.info()
yamini_obj.info()
sai_obj.info()

#calling static method
print(School.validate_class_teacher("lakshmi kumari dasareddy"))
print(School.validate_class_teacher("kumari"))      
    