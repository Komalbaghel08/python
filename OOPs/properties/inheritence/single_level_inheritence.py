# class Parent:
#     x = 10
#     def __init__(self,name):
#         self.name = name
    
#     def home(self):
#         print("home from parent class")
        
# class Child(Parent):            
#         pass
    
# obj = Child("python")    
# print(obj.x)
# print(obj.name)
# obj.home()



# method overriding
class Parent:
    x = 10
    def __init__(self,name):
        self.name = name
    
    def home(self):
        print("home from parent class")
        
        
        # Method overriding ho rhi yha 
        # python supported method overriding
class Child(Parent):            
        def home(self):
            print("home from child class")
            super().home()  # parent class ko v call kr skte h super() ka use kr ke
obj = Child("python")    
print(obj.x)
print(obj.name)
obj.home()