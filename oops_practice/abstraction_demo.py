class Laptop:
    def procesor(self):
        print("laptop")
    def ram_rom(self):
        print("rom and ram")
        print("="*50)
class Lenova(Laptop):
    def procesor(self):
        print("lenova processor")
class Dell(Lenova):
    def ram_rom(self):
        print("ron and ram")

obj_one = Lenova()
obj_two = Dell()

#method calling
obj_one.procesor()
obj_one.ram_rom()

print("="*50)

obj_two.procesor()
obj_two.ram_rom()
