my__tuple =(2,"hello",(7,8,9),[12,13,14])

my__tuple[3][2] = 35
my__list = [10,20,30]
my__list.reverse()
print(my__list)

valu =my__list.copy()
print(valu)
print("hellow world")

def login(username,pasword):
    if username =="divya"and pasword == "098":
        print("login sucses")
    else: 
        print("login failure")
login("098","divya")

#employe info function
def employe_info(employe_name,employ_email,employe_location):
    print(f"hi{employe_name},your email id is {employ_email}and your work place is{employe_location}")
employe_info("divya","divya@gmail.com","hyd")

def employe_info(employe_name,employe_email,employe_location):
    print(f"hi{employe_name},your email id is {employe_email}and your work place is{employe_location}")
employe_info(employe_location = "ap",employe_name = "divya",employe_email = "divya@gmail.com")

#default values

def employe_info(employe_name,employe_email,employe_location,company_name):
    print(f"hi{employe_name},your email is {employe_email},ur working place is {employe_location}and ur working for {company_name}")
employe_info(employe_location = "hyd",employe_name = "divya",employe_email =" divya@gmail.com", company_name = "meta")

def emp_info(name,age,institute = "Edify"):
   print(institute)
emp_info("divya","20","jupiter")

#dictnory

details ={}
details["emp_name"] = "divya"
details["emp_email_id"] = "divya@gmail.com"
details["emp_location"]= "hyd"
print(details)

#global scope
ga = 30
def add(la,lb):
    print(la)
    print(lb)
    print(ga)
add(20,30)


ga = 30
def add(la,lb,ga):
    print(la)
    print(lb)
    print(ga)
    print(globals()["ga"])
add(1,2,3)



##get predifined function types

import builtins
print(dir(builtins))

#without lambda

def add(a,b):
    return a + b
print(add(3,4))

#with lambda

#lambda arguements : expression


sum = lambda a,b :a+b
print(sum(10,20))

info = lambda g, h :g*h
print(info(100,55))

##IILE

print((lambda a,b :a%b)(6,9))

print((lambda a,b :a*b)(6,9))

## with lambda

print((lambda num : num +2 ==3)(3))
print((lambda num : num *3 == 3)(9))

#without lambda

def info(num):
    if num %2 == 0:
      return True
    else:
     return False
print(info(0))
print(info(2))

def info(num):
    if num +2== 3:
      return True
    else:
     return False
print(info(3))
print(info(2))

#with lambda 
print((lambda num :"positive"if num >0 else "negative")(10))

##iile
print((lambda a,b:a+b)(5,6))

#without lambda

def is_even(num):
   if num%2==0:
      return True
   else:
      return False
print(is_even(5))

#with lambda

print((lambda num:num%2==0)(5))

      
      #

def emp_info(emp_name,emp_email,emp_loc):
   employee_details = {}
   employee_details["emp_name"] = emp_name
   employee_details["emp_email"] = emp_email
   employee_details["emp_loc"] = emp_loc

   return employee_details

print(emp_info("Divya","divya@gmail.com","mydukur"))

def emp_information(emp_name,emp_email,emp_loc):
   print(f"emp_name : {emp_name},emp_loc = {emp_loc} , emp_email : {emp_email}")

emp_information("Divya","divya@gmail.com","mydukur")

def empl_info(emp_name,emp_email,emp_location,company_name="Edify"):
   print(f"hi {emp_name},your email is {emp_email} and work location is {emp_location} and ur company name is {company_name}")
   
empl_info("divya","divya@gmail.com","mydukur")
empl_info("sai","yaminio@gmail.com","mydukur")


#without lambda
def is_even(num):
   if num%2==0:
      return True
   else:
      return False
print(is_even(5))
print(is_even(10))

#
data = (1,2,3)
def display(data):
   for num in data:
      if num % 2 == 0:
        print ("even")
      else:
         print("odd")
display(data)

print((lambda num:num%2==0)(5))

#
emp_info =((lambda emp_name,emp_email,emp_location:print(f"hi {emp_name}, ur email is {emp_email} and ur location is {emp_location}"))("divya","divya@gmail.com","hyd"))
emp_info

#regular functions

def greet (name):
   print("hello",name)
   print("welcome to python")
greet("divya")

#normal
def add_num(*numbers):
    total=0
    for num in numbers:
      total+=num
    return total 
print(add_num(1,2,3))

##without map
def square_list(numbers):
   square_list = []
   for num in numbers:
      square_list.append(num*num)
      return square_list
print(square_list([1,2,3,4,5]))
#with map()
print(list(map(lambda num:num*num,[1,2,3,4,5])))

##
print(map(lambda num:num*num,[1,2,3,4,5]))

##without filter()
def even_list(numbers):
   even_numbers = []
   for num in numbers:
      if num % 2 == 0:
         even_numbers.append(num)
   return even_numbers

print(even_list([1,2,3,4]))

##with filters()
print(filter(lambda num :num %2==0,[1,2,3,4,5]))

print(list(filter(lambda num :num %2==0,[1,2,3])))

##print(list(filter(lambda num : num+2=0,[1,3,4])))If you want to add 2 to each number in the list, use map instead of filter (since filter expects a function returning a boolean value)

print(list(map(lambda num :num+2,[1,2,3]))) 

##print(map(lambda num:num-2,1,2,3))map(function, iterable)
#That means the second #argument must be a single iterable (like a list, tuple, or string) — not multiple numbers.


print(list(map(lambda a, b: a + b, [1, 2, 3], [4, 5, 6])))

##reduce without reduce

def even_list(numbers):
   even_numbers=[]
   for num in numbers:
      if num %2==0:
       even_numbers.append(num)
   return even_numbers
print(even_list([2,3,4,6]))


def sum_list(numbers):
    sum_numbers = []
    for num in numbers:
        sum_numbers.append(num + 2)   # store the new number in the list
    return sum_numbers                # return the result list

print(sum_list([3, 5, 6, 2]))

#with reduce()
#frome functions import reduce
#print(reduce(lambda result num:result*num,[12]))in Python, lambda parameters must be separated by a comma:

#print(reduce(lambda result , num:result*num,[1,3,7]))NameError: name 'reduce' is not defind


#studdent class

class Student :

   #class variable = class data is same for every student

    #def __init__(self,student_name,student_id)
    #self.student id =student_id
    #self.student name = student_name

   def __init__(self,student_id,student_name,student_age=none,student_email=none,student_mobile_number=none):
       
       #identity info
      self.student_id = student_id
      self.studenent_name=student_name
      self.student_age=student_age
      self.student_email=student_email
      self.student_mobile_number=student_mobile_number

      #calculate info
      self.total_sessions_attended=0
      self.attendance_credit=0
      self.performance_credit=0
      self.final_credit=0
      self.trainer_rating=0

   #however like functionalitys
   def student_basic_info(self):
      print(======="basic info"=======)
      print(f"stiudent id :{student_id}")
      print(f"student_name :{student_name}")


   # click like functionality
   def student_complete_info(self):
      print(===="complete info"======)
      print(f"student id :{student_id}")
      print(f"student name :{student_name}")
      print(f"student age :{student_age}")
      print(f"student_email :{student_email}")
      print(f"student mobile number :{student_mobile_number}")
   #calculate student attendance
   def session_credits_cal(self):
       total_sessions_attended = int(input("enter total sessions attended"))
       self.total_sesions_attended = total_sessions_attended

      if total_sessions_attended>=30:
         self.attendence_credits=+5
      elif total_sessions_attended>=20:
         self.attendance_credits=+3
      else:
         self.attendance_credits=0
         return self.attendance_credits
   #performance credits based on the score
   def performance_credits_cal(self,score):
      if score is >=90:
         self.performance_credit=+5
      elif score>=70:
         self.performance_credit=+3
      else:
         self.performance_credits=0
         return self.performance_credits
      
   #calculaye final credits based on above 
   def achivement_status(self):
      self.final_credits = self.session_credits_cal() +self.performance_credit_cal(95)

      if final_credits>=10:
         print("got gold")
      elif final_credit>=8:
         print("got silver")
      else:
         print("got bronze")
         return self.final_credits
   #trainer rating
   def trainer_rating(self):
      self.trainer_rating = int(input("enter trainer rating(1-5)"))

      if trainer_rating>=5:
         return 5000
      else:
         return 0
      

          
       
          
      