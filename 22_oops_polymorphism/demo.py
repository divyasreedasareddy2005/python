class Dog:
    def sound(self):
        return "wooof"
class Cat:
    def sound(self):
        return"meow"
class Cow:
    def sound(self):
        return "amba"
def Animals_sounds(animals):
    print(animals.sound())
obj_one = Dog()
obj_two = Cat()
obj_three = Cow()

#method caling
Animals_sounds(obj_one)
Animals_sounds(obj_two)
Animals_sounds(obj_three) 
