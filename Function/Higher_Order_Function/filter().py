# l = [1,2,3,4,5,6,7,8,9,10]
# def even_no(n):
#     if n %2 == 0:
#         return n
# x = filter(even_no,l)
# print(x)
# print(list(x))    

#greter tha 5
# l = [1,2,3,4,5,6,7,8,9,10]
# def greter5(n):
#     if n >= 5:
#         return n
# x = filter(greter5,l)
# print(list(x))  

# second method
l = [1,2,3,4,5,6,7,8,9,10]
l1 = []
for i in l:
    if i >= 5:
        l1.append(i)
print(l1)          