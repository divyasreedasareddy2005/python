#polymorphisam
class Dog:
    def sound(self):
        return "bow"
class Cat:
    def sound(self):
        return"meow"
class Cow:
    def sound(self):
        return "amba"
def animal_sound(self):
    print(self.sound())
    

obj_one = Dog()
obj_two = Cat()
obj_three = Cow()

#obj_one.animal_sound()
#obj_two.animal_sound()
#obj_three.animal_sound()
animal_sound(obj_one)
animal_sound(obj_two)
animal_sound(obj_three)

#method overriding

class Animal:
    def sound(self):
        print("animal makes sounds")
class Dog(Animal):
    def sound(self):
       print("dogs make bow")
class Cat(Animal):
    def sound(self):
        print("cat makes meow")
class Cow(Animal):
    pass

obj_one = Dog()
obj_one.sound()

obj_two = Cat()
obj_two.sound()

obj_three = Cow()
obj_three.sound()

#overload.
class Math:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj = Math()
    
#print(obj.add(10,20))
print(obj.add(10,30,44)) 

#handiling overloading python way
class Math:
    def add(self,a = 0,b = 0,c = 0):
        return a+b +c
      
    
obj = Math()
print(obj.add(30))
print(obj.add(10,20))
print(obj.add(10,33,55))
print(obj.add(2,4,7,8))
        