#oops basic

data = 10
print(type(data))

#class
class employee:
    pass
#object
emp_obj = employee()
print(type(emp_obj))

#student ->real world entity
class Student:
    #attribute/variables
    student_name = "ravi"
    student_email = "ravi@gmail.com"

    #statements
    print(f"student name :{student_name}")
    print("student email :",student_email)
    print("="*50)

#function(out side the class)
def student_fun():
    #variable
    student_name = "john"
    student_email = "john@gmail.com"
    
    #statements
    print("student name :",student_name)
    print("student email :", student_email)

student_fun()# function call is must
print("="*50)

#student real world entity
class student:
    #attributes /variables
    student_name = "divya"
    student_email ="divya@gmail.com"

    #method
    def info(self):
        #student_email = "john@gmail.com"
        print("student name :",self.student_name)
        print("student email:" ,self.student_email)

    
student_one_obj = student()#object creation
student_two_obj =student ()
student_three_obj = student()
#method call is required
student_one_obj.info()
student_two_obj.info()
student_three_obj.info()
print("="*50)

