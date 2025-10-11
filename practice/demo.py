def math_ops():
    a = 20
    b = 10
    print(a+b)
    print(a-b)
    print(a*b)
math_ops()

def math_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
math_ops(17,2)
# positional arguements
def login(user_name,password):
    if user_name=="ravi"and password=="098" :
        print("login success")

    else:
        print("login failed")
login("098","ravi")


def login(user_name,password):
    if user_name=="ravi"and password=="098" :
        print("login success")

    else:
        print("login failed")
login("ravi","098")


def employe_info(employe_name,employe_email,employe_location):
    print(f"hi{employe_name}your email is {employe_email}and your location is {employe_location}")
employe_info("divya","divya@gmail.com","hyd")

def employe_info(employe_name,employe_email,employe_location):
    print(f"hi{employe_name}your email is {employe_email}and your location is {employe_location}")
employe_info("hyd","divya@gmail.com","divya")



def employe_info(employe_name,employe_email,employe_location):
    print(f"hi{employe_name}your email is {employe_email}and your location is {employe_location}")
employe_info("hyd","divya@gmail.com","divya")

    #default values

def employe_info(employe_name,employe_email,employe_location,company_name):
    print(f"hi{employe_name}your email is {employe_email}and your location is {employe_location} working fo {company_name}")
employe_info(employe_location = "hyd",employe_name = "divya",employe_email ="divya@gmail.com",company_name ="meta")

#arbitary positional arguements(*args)
def add_all(*numbers):
    total = 0
    for num in numbers:
        total = total+num
    print(f"the total sum is {total}")
add_all(10)

#arbitary keywords arguments (**kwargs)

def profile (**info):
    print(info)
profile(name = "divya")