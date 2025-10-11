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
emp_info("divya","age","jupiter")

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
#name conflict
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