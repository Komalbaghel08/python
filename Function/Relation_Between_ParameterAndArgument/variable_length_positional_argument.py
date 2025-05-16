# def fibo(* args):
#     print(args)
#     print(type(n))
    
# fibo(2,4,6,8,10)    

# single * agruments ya aingle(*) args ky hote h interview me pucha jata h

def fibo(* args):
    sum = 0
    for i in args:
        sum = sum+i
        return sum
x = fibo(2,4,5,3,2)
print (x)  


# agr runtym pe tuple leke dikhao
def fibo(* args):
    sum = 0
    for i in args:
        for j in i:
            sum = sum+i
    return sum        
p = (2,4,6,8,10) 
x = fibo(p)
print(x)
            