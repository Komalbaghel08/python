class Student:
    @staticmethod
    def welcome(name):
        print('Welcome!',name)

    school = "shss"
    gread = "10th"

    def __init__(self, name):
        self.n = name
    
    def show_details(self):
        print(self.n)
        print(Student.school)
        print(Student.gread)
       
    
    @classmethod
    def update_gread(cls, update):#update veriable 
        cls.gread =  update
    
    
    @staticmethod
    def add_new(cls, cit):
        print(cls)
        print(cit)
    
    @staticmethod
    def thanks(name):
        print("thankyou",name)


Student.welcome('komal')


obj1 = Student('asshuu')
Student.add_new('BHopal','indore')
obj1.show_details()

Student.thanks("komal")