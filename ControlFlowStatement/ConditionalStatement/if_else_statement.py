# age = int(input("enter your age"))
# if age>18:
#     print("you can apply for license")
# else:
#     print("itni jaldi kya hai")

# Example:-- Checking if a year is a leap year
# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("it's leap year.")
# else:
#     print("it's not a leap year.")

     
     
# Python Program to find the area of triangle
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))  

# a = float(input("Enter first side: ")) 
# b = float(input("Enter second side: ")) 
# c = float(input("Enter third side: ")) 
# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print("Area of triangle :",area)


# Python program to swap two variables
# x = input('Enter value of x: ')
# y = input('Enter value of y: ')
# temp = x
# x = y
# y = temp
# print("the value of x after swapping is :", x)
# print("the value of y after swapping is :", y)

# without using third variable
# x = input('Enter value of x: ')
# y = input('Enter value of y: ')
# x,y = y,x
# print("the value of x after swapping is :", x)
# print("the value of y after swapping is :", y)




# By-using Addition and Subtraction.
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x+y
y = x-y
x = x-y
print('The value of x after swapping: ',x)
print('The value of y after swapping: ',y)