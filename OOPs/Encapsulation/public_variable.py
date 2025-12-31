class P:
    x =10
    def show(self):
        print("from P class")
class C(P):
    pass
obj = C()
print(obj.x)   
print(obj.show())

'''aisa variable ya method jisko unke  child class me v acce4s kr paye aur bhr v class ke access kr paye '''