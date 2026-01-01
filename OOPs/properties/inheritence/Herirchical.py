
class Parent:
    x = 10
    
    def __init__(self,name):
        self.name = name
    
    def home(self):
        print("home from parent class")
        
class Child1(Parent):            
    def home(self):
        print("home from child class")
        # super().home()
        # super().car()

class Child2(Parent):
    pass 

obj1 = Child1("python")  
obj2 = Child2("java")  
print(obj1.x,obj2.x)
obj1.home()
obj2.home()


# MRO (Method Resolution Order)
