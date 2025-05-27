# python not supported protected variable

class P:
    _x =10
    def _show(self):
        print("from P class")
class C(P):
    pass
obj = C()
print(obj._x)   
print(obj._show())