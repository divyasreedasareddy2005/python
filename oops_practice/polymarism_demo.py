class Dog:
    def sound(self):
        return "bow"
class Cat:
    def sound(self):
        return"meow"
class Cow:
    def sound(self):
        return "amba"
    
def animal_sound(Animal):
    print(Animal.sound())
    
obj = Dog()
obj_o = Cat()
obj_t  = Cow()


animal_sound(obj)
animal_sound(obj_o)
animal_sound(obj_t)