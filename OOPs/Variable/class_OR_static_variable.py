# class Student:
#     school = "vindhya"  #declaration inside class model
#     def __init__(self,name):
#         self.n = name
# obj1 = Student("komal")
# obj2 = Student("singh")   

# print(Student.school)
# # print(obj2.school)


# DECLARATION OR ACCESS KAISE KRTE H
class Sudent:
    school = "shhss"  # declaration inside class body

    def __init__(self, name):  # constructor needs a 'name' argument
        self.n = name
        Sudent.school_code = 101  # inside constructor
        print(Sudent.school)

    def addNew(self):
        Sudent.school_city = 'BHopal'  # inside instance method
        print(Sudent.school_city, Sudent.school_code)

    def Display(self):
        print(Sudent.gread)

Sudent.gread = "10th"  # outside of class

obj = Sudent("Unnamed")  # name argument required
obj.addNew()
obj.Display()

obj1 = Sudent('komal')
# obj2 = Sudent('Rahul')

print(Sudent.school)
# print(obj1.school)
# print(obj2.school)

# LOCAL VARIABLE
class Student:
    def __init__(self,name):
        grad = '10th'
        self.name = name 
        print(grad)
    def new(self):
        print(grad)
obj=Student("komal")
obj.new()
            