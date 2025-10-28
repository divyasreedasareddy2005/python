#abstraction
class Laptop:
    def processer(self):
        print("laptop processer")
    def charge (self):
        print(5000)
    def Ram_hdd(self):
        print("ram and hdd")
class Lenova(Laptop):
    def processer(self):
        print("lenova processer")
class Dell(Lenova):
    def Ram_hdd(self):
        print("dell laptop ram and hdd")
        
print("buying lenova laptop")
obj= Lenova()
obj.processer()
obj.Ram_hdd()
print("="*50)

obj = Dell()
obj.Ram_hdd()
obj.processer()
obj.charge()
print("="*50)



obj = Laptop()
obj.processer()
obj.Ram_hdd()


        