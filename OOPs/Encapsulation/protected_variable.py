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

'''protected variable class ke bhr access nhi kr skte sirf classke andr access kr skte mtlb sirf child class me '''