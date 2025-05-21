# class First:
#     pass
# print(id(First))
# obj = First
# print(id(obj))
# obj1 = First()
# print(id(obj))


# constructor-- ye aik special method h jo object bnate hi call ho jati h
class First:
    "hello"
    pass
print(dir(First ))
print(First .__doc__)


class First:
    def __init__(self):
        print("constructor called")
obj = First
obj = First()   

# self --> self aik reference variable h jo current object ka address hold krega