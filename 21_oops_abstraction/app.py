#with abstractions

from abc import ABC,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def processor(self):
        pass
    @abstractmethod
    def Storage(self):
        pass
    def Screen_saver(self):
        print("screen saver")
        
#Laptop = Laptop()
#Laptop.processor()TypeError: Can't instantiate abstract class Laptop without an implementation for abstract method 'processor'

class Lenovo(Laptop):
    def processor(self):
        print("lenova processor")
    def Storage(self):
        print("lenovo storage")
obj = Lenovo()
obj.processor()
obj.Storage()