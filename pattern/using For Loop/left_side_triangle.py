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




# O/P:--
# 10
# 10 8
# 10 8 6
# 10 8 6 4
# 10 8 6 4 2
# code for above output
k=[]
for i in range(10,1,-2):
 k.append(i)
for j in k:
 print(j,end=" ")
print()







