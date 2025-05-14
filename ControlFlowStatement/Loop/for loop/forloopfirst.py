# l = [10, 20, 30, 40]

# l1 = []
# # for i in l:
# #     print(i)

# for i in l:
#     # x = i + 5
#     # l1.append(x)
#     l1.append(i + 5)

# print(l1)

# s = input("Enter string: ")# for string
# t = eval(input("Enter any tuple: "))

# for i in s:
#     print(i)

# for i in t :
#     print(i)

# d = eval(input("Enter dictionary: "))

# for k,v in d.items():
#     print(k, " = ", v)

# for k in d.keys():
#     print(k)

# for v in d.values():
#     print(v)    


n = int(input("Enter any number: "))

# for i in range(1, n + 1):
#     print(i)
# sum = 0
# for i in range(2,n + 1, 2):
#     sum = sum + i
#     if i < n :
#         print(i, end=" + ")
#     else :
#         print(i, end=" = ")    

# print(sum)


sum1 = 0
for i in range(1,n + 1, 2):
    sum1 = sum1 + i
    if i < n :
        print(i, end=" + ")
    else:
        print(i, end=" = ")    
