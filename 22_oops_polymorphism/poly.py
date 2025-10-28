# method overriding
class Animal:
    def sound(self):
        print("Animals makes a sounds")
class Dog(Animal):
    def sound(self):
        print("bow")
class Cat(Animal):
    def sound(self):
        print("meow")
class Cow(Animal):
    pass
obj = Animal()
obj.sound()

obj_one = Dog()
obj_one.sound()

obj_two = Cat()
obj_two.sound()

obj_three = Cow()
obj_three.sound()

