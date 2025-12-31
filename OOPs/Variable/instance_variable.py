'''INSTANCE_VARIABLE ---> aise variable jo self pe depend hote h 
     2. aise variable jo object ke value bdlne pe apni value bdlte h 
    3.aise variable jo self ke sath likhe jate h '''
''' SELF -- self aik refrense parameter h jo current object ka address hold krta h (class ke object ka)'''  
    
class Student:
    def __init__(self,name,city):
        self.n = name    #in-side instance method(declration)
        self.c = city 
        print(self.n,self.c)  #Access inside constructor 
        
        
    def add(self,phone):
        self.p = phone   #in-side instance method(declration)
        print(self.p,self.c,self.n,self.school)  #Access inside instance method
        
obj = Student("komal","bhopal")
obj.school = 'vindhya'    #out-side instance method(declration) 

# print(obj.n,obj.p,obj.school) ---->error kyuki av phone  nhi declare hua h

obj.add(42323)  
print(obj.n,obj.p,obj.school,obj.c)        #Access out side of the class