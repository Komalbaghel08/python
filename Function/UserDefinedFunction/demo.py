# Write a function to take number as input and print its square value
# def square(x):
#     print("the square of",x,"is",x*x)
# square(2)
# square(12)    



# Write a function to check whether the given number is even or odd?
# def even_odd(num):
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# even_odd(22)
# even_odd(7)        
        
    
# Write a function to find factorial of given number?

# def fact(n):
#     result = 1
#     while n >= 1:
#         result = result*n
#         n = n-1
#     return result    
# i = int(input("enter any number"))
# print("the factorial of",i,"is:",fact(i))


# def factt(n):
#     Result = 1
#     for i in range(1,n+1):
#          Result *= i
#     return Result     
# i = int(input("enter any number: "))
# print("the factorial of",i,"is:",factt(i))


# def add_sub(x,y):
#     add = x+y
#     sub = x-y
#     return add,sub
# a,b = add_sub(10,20)

# print("The Addition is :",a)
# print("The Subtraction is :",b)


def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
x,y,z,p=calc(int(input("Enter first value:")),int(input("Enter second value: ")))
print("The Addition is",x)
print("The Substraction is",y)
print("The Multip is",z)
print("The Division is",p)
