class Student:
    school = "shs"
    grad = "10th"
    def __init__(self,name):
        self.n = name
    def show_detail(self):
        print(self.n)
        print(Student.school)
        print(Student.grad)
        print(Student.city)
    @classmethod
    def update_grad (cls,updated) :
        cls.grad = updated
    def add_new(cls,city):
        cls.city = city
    @classmethod
    def add_new(cls,city):
        cls.city = city   
obj = Student("komal")
# obj.show_detail()  
# Student.update_grad('11th')   
obj1 = Student('singh')
# obj1.show_detail() 
Student.add_new("Bhopal")  
obj1.show_detail() 