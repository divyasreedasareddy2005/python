#with abstractions

from abc import ABC,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def processor(self):
        pass
    @abstractmethod
    def Storage(self):
        pass
    @abstractmethod
    def Screen_saver(self):
        print("screen saver")
        
    def charge(self):
        pass
        
#Laptop = Laptop()
#Laptop.processor()TypeError: Can't instantiate abstract class Laptop without an implementation for abstract method 'processor'

class Lenovo(Laptop):
    def processor(self):
        print("lenova processor")
    def Storage(self):
        print("lenovo storage")
        
    def Screen_saver(self):
        print("saver")
obj = Lenovo()
obj.processor()
obj.Storage()
obj.Screen_saver()