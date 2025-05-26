class GrandParent:
    def car(self):
        print("Car from Gparent class")
class Parent(GrandParent):
    x = 10
    def __init__(self,name):
        self.name = name
    
    def home(self):
        print("home from parent class")
        
class Child(Parent):            
       def home(self):
            print("home from child class")
            super().home()
            super().car()
    
obj = Child("python")    
print(obj.x)
print(obj.name)
obj.home()        