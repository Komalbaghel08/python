class Parent1:
    def car(self):
        print("Car from parent1 class")
class Parent2:
    x = 10
    def __init__(self,name):
        self.name = name
    
    def home(self):
        print("home from parent2 class")
        
class Child(Parent1,Parent2):            
       def home(self):
            print("home from child class")
            super().home()
            super().car()
    
obj = Child("python")    
print(obj.x)
print(obj.name)
obj.home()        