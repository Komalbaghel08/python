# -------definition---------NonLocal variable == local variable ki value ko modifiy krne ke liye use krte hai
# - nonlocal variable kisi local variable ke andr hi ban skta h 

x = 10
def first():
    x= 20
    def second():
        nonlocal x
        x=30
    second()  
    print(x)  
first()        