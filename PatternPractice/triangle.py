# triangle pattern
# r = int(input("Enter number of rows: "))
# for i in range(1,r+1):
#     print("* "*i)
    
""" 
sq. number pattern
1
1 2
1 2 3
1 2 3 4
"""

# r = int(input("Enter number of rows: "))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
'''
r = int(input("Enter number of rows: "))
for i in range(1,r+1):
    print((str(i)+" ")*i)
    
    
'''# reverse triangle pattern
*****
****
***
** 
*
'''
r = int(input("Enter number of rows: "))
for i in range(r,0,-1):
    print("* "*i)
    