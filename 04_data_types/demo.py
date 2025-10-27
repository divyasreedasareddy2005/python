# data types

#numeric data types

#int
data = 10
print(data)
print(type(data))

#float
data = 10.9
print(data)
print(type(data))

#complex
data = 3 + 5j
print(data)
print(type(data))

#string
data = "python"
print(data)
print(type(data))

#boolen
data = True
print(data)
print(type(data))

#list(homogenous data)
data = [10,4,66,87]
data = [5,"divya",'true']
print(data)
print(type(data))

#tuple(heterogenious)
data = (103,"divya",'true')
data = (10,33,4,80)
print(data)
print(type(data))

#set
data = {10,30,4}
print(data)
print(type(data)) 

#dictionary
data = {"data" : "divya","id ":"149","location" : "hyd"}
print(data)
print(type(data))

#none type
x = None
print(x)
print(type(x))

#user defined datatypes
class student:
    #logics
    pass#syntax
student_john = student()
print(type(student_john))

#type conversion
a = 10#int
print(type(a))
b = 3.0#float
print(type(b))
c = a + b #dynamic
print(c)
print(type(c))

#type casting
pi = 3.14#float
print(pi)
print(type(pi))

#req round of pi and give whole num
pi_round_int = int(pi)
print(type(pi_round_int))
print(pi_round_int)

rating = "4"
print(type(rating))
print(type(pi_round_int))
print(pi_round_int)


rating = "4"
print(type(rating))
#increment rating = rating + 1 #type error : can only concatination str(not"int)to str
increment_rating = int(rating)+1
print(increment_rating)
print(type(increment_rating))

new_rating  = "four" #incompatable conversion
print(type(rating))
#increment_rating = new_rating +1 #type error : can only concatination str(not "int")to str
#increment_rating = int(new_rating)+1 #value error:invalid literal for int()wit base 10:
num = 10
print(type(num))
