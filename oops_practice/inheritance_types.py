#types of inheritance
#1 single inheritance
class Parent:
    def land(self):
        print("has land")
class daughter(Parent):
    def bussiness(self):
        print("has bussiness")
obj_p = Parent()
obj_p.land()
obj_d = daughter()
obj_d.land()
obj_d.bussiness()

#multi inheritance  -> parent => child=> grandparent
class grandparent:
    def agri_land(self):
        print("has agri_land")
class parent(grandparent):
    def land(self):
        print("has land")
class daughter(parent):
    def bussiness(self):
        print("has bussiness")
obj = grandparent()
obj_one = parent()
obj_child = daughter()

# method calling
obj.agri_land()
obj_one.land()
obj_one.agri_land()
obj_child.agri_land()
obj_child.bussiness()
obj_child.land()


#3 multiple inheritance => multiple parents =>single child
class grandparent:
    def agri_land(self):
        print("has agri_land")
class parent(grandparent):
    def land(self):
        print("has land")
class mother:
    def gold(self):
        print("has gold")
class daughter(parent,mother):
    def bussiness(self):
        print("has bussiness")
obj = grandparent()
obj_one = parent()
obj_two = mother()
obj_three = daughter()

# method caling
obj.agri_land()
obj_one.land()
obj_one.agri_land()
obj_two.gold()
obj_three.bussiness()
obj_three.gold()
obj_three.land()
obj_three.agri_land()

#4 hierarical inheritance =>single_parent =>multiplechild
class grandparent:
    def agri_land(self):
        print("has agri_land")
class parent(grandparent):
    def land(self):
        print("has land")
class daughter(parent):
    def bussines(self):
        print("hjas bussines")
class son(parent):
    def car(self):
        print("has car")
        
g = grandparent()
p = parent()
o_d = daughter()
o_s = son()

#calling method
o_d.agri_land()
o_d.land()
o_d.bussines()

o_s.agri_land()
o_s.land()
o_s.car()

#5 hybrid inheritance =>combination 

class A:
    def flat(self):
        print("has flat")
class B(A):
    def land(self):
        print("has land")
class C(A):
    def gold(self):
        print("has gold")
        
class D(B,C):
    def bussiness(self):
        print("has bussiness")
        
ob = A()
obb = B()
obbb = C()
obbbb = D()

#METHOD CALLING
obb.flat()
obb.land()
obbb.flat()
obbb.gold()
obbbb.flat()
obbbb.land()
obbbb.gold()
obbbb.bussiness()
obbb.land()