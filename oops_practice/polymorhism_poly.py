class Animal:
    def sound(self):
        print("animals makes sounds")
class Cat(Animal):
    def sound(self):
        print("meow")
class Dog(Animal):
    def sound(self):
        print("bow")
class Cow(Animal):
    pass

obj = Animal()
obj.sound()

obj_o = Cat()
obj_o.sound()

obj_t = Dog()
obj_t.sound()

obj_th = Cow()
obj_th.sound()