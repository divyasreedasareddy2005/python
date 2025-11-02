class math:
    def add(self,a,b):
       return a+b 
    def add(self,a,b,c):
        print(a+b+c)
        
obj = math()
obj.add(10,20,3)

class mathh:
    def add(self,a = 0,b=0,c=0):
        return a+b+c
    
obj_o = mathh()
print(obj_o.add(10))
print(obj_o.add(10,2))
print(obj_o.add(2,3,4))
print(obj_o.add(1,2,3,4))
    