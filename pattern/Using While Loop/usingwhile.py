# upper left side tringle

# n = int(input("enter any number: "))

# while n > 0:
#     print('*'*n)
#     n = n -1


# left upper and lower tringle

# n = int(input("enter any number: "))

# i = 0
# while i < n:
#     print('*'*(n-i) + ' '* i)
#     i = i + 1
# # print(i)
# i = i - 2
# while i >=0 :
#     print("*" * (n - i) + ' '*i)
#     i = i - 1

n = int(input("enter any number: "))

i = 0
while i < n:
    print(' '*(n-i) + '* '* i)
    i = i + 1
# print(i)
i = i - 2
while i >=0 :
    print(" " * (n - i) + '* '*i)
    i = i - 1