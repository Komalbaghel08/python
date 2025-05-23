class student:
    def __init__(self,name,city,phone):
        self. n = name
        self .c = city 
        self .p = phone
# obj = student    
# print(obj.n,obj.c,obj.p)   ----error

# obj = student() 
# print(obj.n,obj.c,obj.p)  ---->error

obj1 = student("komal","bhopal",87695)
obj2 = student("komall","Rewa",6432345)
print(obj1.n,obj1.c,obj1.p)
print(obj2.n,obj2.c,obj2.p)