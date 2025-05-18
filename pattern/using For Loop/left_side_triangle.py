# row = int (input("enter a number of row : "))
# for i in range(0,row+1):
#     print('*' *i)
    

"""1
22
333
4444
55555"""

# row = int (input("enter a number of row : "))
# for i in range(1, row+1):
#     print(str(i) * i)


""" 1
12
123
1234
12345 """

row = int (input("enter a number of row : "))
for i in range(1, row+1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
