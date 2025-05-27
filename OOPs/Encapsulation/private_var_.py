
class  P:
    __x =10
    
    def __show(self):
        print("from P class")


class C(P):
    pass

print(dir(C))
obj = C()
obj._P__show()
