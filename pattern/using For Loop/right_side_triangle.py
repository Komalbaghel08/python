""" 1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 """

# rows = int(input("enter a number of row : "))

# for i in range(1, rows + 1):
#     # Print spaces first
#     for space in range(rows - i):
#         print(" ", end=" ")
#     # Then print numbers
#     for num in range(1, i + 1):
#         print(num, end=" ")
#     print()

""" *
* *
* * *
* * * *
* * * * * """

# rows = int(input("enter a number of row : "))

# for i in range(1, rows + 1):
#     # Print spaces first
#     for space in range(rows - i):
#         print(" ", end=" ")
#     # Then print numbers
#     for num in range(1, i + 1):
#         print("*", end=" ")
#     print()
    
""" 1
1 2 
1 2 3
1 2 3  4
 1 2 3 4 5"""
 
rows = int(input("enter a number of row : "))

for i in range(1, rows + 1):
    # Print spaces first
    for space in range(rows - i):
        print(" ", end=" ")
    # Then print numbers
    for num in range(1, i + 1):
        print(i, end=" ")
    print()