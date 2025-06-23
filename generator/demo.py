def natural(n):
    i =1
    while i<n:
        yield i
        i=i+1
x = natural(10)  
# for i in x :
#     print(i)      
print(next(x))
print('hello')
print(next(x))
print(next(x))