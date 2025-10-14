#operators

#arthamatica operators
num1 =2
num2 =4
print(f"sum of {num1} and {num2} is {num1+num2}")
print(f"difference of {num1} and {num2} is {num1-num2}")
print(f"product of {num1} and {num2} is{num1*num2}")
print(f"module of  {num1} and {num2} is {num1%num2}")
print(f"division of {num1} and {num2} is{num1/num2}")

print(num1//num2)# flore division it remove the values after . and give the single value from the answer of division
print(num1**num2) #2^4 #explanation:num1 ** num2 means 24(2 power 4)=16

# 2 compoud assignment operators
num = 10
num = num+5 #without compound assignment operators
print(num)

num =10
num +=4
print(num)#with compound assignment operators
num*=5
print(num)

count = 1
#increment count
count+=4
print(count)

bill = 30
bill+=8#incriment the bill
print(bill)

salary = 60000
salary -=5000
print(salary)

# 3 comparision operators

a =30
b=60
c =4
d =5

print(a==b)# this are the comparision arguments
print(c>b)
print(d<a)
print(c>a)
print(b!=d)
print(c!=d)

# 4 logical operators
a =10
b =5
c=3
d =2
# and table
#truth Table for AND:

#A		 B       A AND B
#true	True	True
#True	False	False
#False	True	False
#False	False	False

data_and= a>b and c<d# t and f => f
print(data_and)

data_and = a>b and c>d # t and t ->t
print(data_and)

# 0r table
#truth Table for OR:
#A	    B	    A OR B
#True	True	True
#True	False	True
#False	True	True
#False	False	False

data_or = a> b or c<d #t or f=>t
print(data_or)


#Truth Table for NOT:

# a 	NOT A
#True	False
#False	True

is_logged_in = "true" 
print(not is_logged_in)
#explanation: Since is_logged_in is False, not is_logged_in becomes True, so the message is printed.

## membership operators
# sting is a sw=equence of data type

data = "python is language"
is_z_present = "z"in data
print(is_z_present)
is_p_present = "p" in data
print(is_p_present)

is_python_present = "python" in data
print(is_python_present)

# employees

id = 122
emp_ids = [134,555,890,122]
is_id_present = id in emp_ids
print(is_id_present)
is_id_not_present = id not in emp_ids
print(is_id_not_present)


##identity operators

num1=10
num2 =10
print(num1==num2)## comparision of values 
print(num is num2)# comparision for memory

a =[20,55]
b=[44,0]

print(a == b)## comparision of values 
print(a is b)##comparision for memory


##bitwise operators

num1 =3
num2 =7
print(num1&num2)
print(num1|num2)

#Operator	Meaning	       Example	       Result
#& 	         AND             3&5   	            1
#`	          `              OR	               3 | 5
#^	         XOR	       3 ^ 5   	             6     
#~	         NOT	        ~3	                 -4
#<<	       Left Shift	   3 << 2	             12
#>>	       Right Shift	    8 >> 2	             2   

