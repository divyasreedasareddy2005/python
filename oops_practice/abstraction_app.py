from abc import ABC ,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def processor(self):
        pass
    @abstractmethod
    def storage(self):
        pass
    @abstractmethod
    def sales(self):
        print("sales")

class Victus(Laptop):
    def processor(self):
        print("victus sales")
    def storage(self):
        print("victus storage")
        
    def sales(self):
        print("sales")
        

obj_one = Victus()

#method caling
obj_one.processor()
obj_one.storage()   
obj_one.sales()     