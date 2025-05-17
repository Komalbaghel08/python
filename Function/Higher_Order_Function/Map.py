# Sntax
# map(fun_name,collection) ----->collection--> list,tuple,string
# l = [1,2,3,4,5]
# def add5(n):
#     return n+5
# x = map(add5,l)
# print(x)
# print(tuple(x))


# -->Que2
l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]
def add5(n,m):
    return n+m
x = map(add5,l1,l2)
print(x)
print(tuple(x))

