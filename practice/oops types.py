#single level inheritance -> single parent and single child
class Father:
    def house(self):
        print("has house")
        
class Daughter(Father):
    def bussines(self):
        print("has bussines")
        
daughter_obj = Daughter()
daughter_obj.house()
daughter_obj.bussines()
print("="*50)

#multi level inheritance -> grand parent ->parent->child
class Grandparent:
    def agri_land(self):
        print("ha agriculture land")
class Father(Grandparent):
    def house(self):
        print("has house")
class Daughter(Father):
    def bussinnes(self):
        print("has bussinnes")

daughter_obj = Daughter()
daughter_obj.agri_land()
daughter_obj.house()
daughter_obj.bussinnes()
print("="*50)

#multiple inheritance ->  multiple parents and single child
class Grandparent:
    def agri_land(self):
        print("has agri land")
class Father(Grandparent):
    def house(self):
        print("has house")
class Mother:
    def land(self):
        print("has land")
class Daughter(Father,Mother):
    def bussinnes(self):
        print("has bussinnes")
        
daughter_obj = Daughter()
daughter_obj.agri_land()
daughter_obj.house()
daughter_obj.land()
daughter_obj.bussinnes()
print(""*50)

#hierarical inheritance -> one parent -> multiple child

class Grandparent:
    print("="*50)
    print("hierarical inheritance")
    def agri_land(self):
        print("has agri land")
class Father(Grandparent):
    def house(self):
        print("has house")
class Mother:
    def land_gold(self):
        print("has land and gold")
class Daughter(Father,Mother):
    def bussinnes(self):
        print("has bussinnes")
class Son(Father,Mother):
    def car(self):
        print("has car")
        
daughter_obj = Daughter()
son_obj = Son()

#METHOD CALLING
daughter_obj.agri_land()
daughter_obj.house()
daughter_obj.land_gold()
daughter_obj.bussinnes()

son_obj.agri_land()
son_obj.house()
son_obj.land_gold()
son_obj.car()
print("="*50)

#hierarical inheritance
print("hierarical inheritance")
class Father:
    def house(self):
       print("has car")
class Daughter(Father):
    def bussinnes(self):
        print("has bussinnes")
class Son(Father):
    def car(self):
        print("has car")
        
daughter_obj = Daughter()
daughter_obj.house()

son_obj = Son()
son_obj.house()
print("="*50)

#hybrid inheritance
print("="*50)
print("combination or two or more types")
class Grandparent:
    def agri_land(self):
        print("has land")
class Father(Grandparent):
    def house(self):
        print("has house")
class Elderfatheradoptdaughter(Grandparent):
    def bussiness(self):
        print("has bussinnes")
class Daughter(Father,Elderfatheradoptdaughter):
    def villa(self):
        print("has villa")
        
daughter_obj = Daughter()
daughter_obj.house()
daughter_obj.bussiness()
daughter_obj.agri_land()
print("="*50)