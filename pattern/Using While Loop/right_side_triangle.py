# i = 1
# row = int(input('enter row : '))
# while i <= row:
#     b = 1
#     while b <= row-i:
#         print(" ",end="")
#         b = b+1
#     j = 1
#     while j<=i:
#         print("*", end = "")
#         j = j+1 
#     print()
#     i = i+1       


"""1
   22
  333
 4444
55555"""

# i = 1
# row = int(input('enter row : '))
# while i <= row:
#     b = 1
#     while b <= row-i:
#         print(" ",end="")
#         b = b+1
#     j = 1
#     while j<=i:
#         print(i, end = "")
#         j = j+1 
#     print()
#     i = i+1 
    
    
""" 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5"""
       
i = 1
row = int(input('enter row : '))
while i <= row:
    b = 1
    while b <= row-i:
        print(" ",end="")
        b = b+1
    j = 1
    while j<=i:
        print(j, end = "")
        j = j+1 
    print()
    i = i+1 
    