#common person class of abstract

from contracts import personal

class Abstractperson(Personal):
    def __init__ (self,id = None,name = None,age = None,email = None,mobile_num = None):
        
        #emcapsulation
        self.__id = id
        self.__name = name
        self.__age = age 
        self.__email = email
        self.__mobile_num = mobile_num
        
    #using property in pythonic way for getter and setters
    
    @property
    
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
        
    @property
    def age(self,value):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age = value
        
    @property
    def email(self,value):
        return self.__email
    @email.setter
    def email(self,value):
        self.__email = value
        
    @property
    def mobile_num(self,value):
        return self.__mobile_num
    @mobile_num.setter
    def mobile_num(self,value):
        return self.__mobile_num=value
    
    #implementation
    def set_personal_details(self,id,name,age,email,mobile_num):
        #set set person details
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.mobile_num = mobile_num
        
#implementaion of peronal ->ocerride(polymorphism)
def personal_complete_info(self):
   #display perason details
   print("======complete info ========")
   print(f"id: {self.id}")
   print(f"name:{self.name}")
   print(f"age : {self.age}")
   print(f"email:{self.email}")
   print(f"mobile_num:{self.mobile_num}")   
   
   