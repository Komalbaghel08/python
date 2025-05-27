class P:
    x =10
    def show(self):
        print("from P class")
class C(P):
    pass
obj = C()
print(obj.x)   
print(obj.show())