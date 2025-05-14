# n = int(input("Enter no"))
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))

a, b, c, = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter third number : "))

if a > b and a > c :
    print(f'a {a} is greater than {b}, {c}')
elif b > a and b > c :
    print(f'b {b} is greater than {a}, {c}')    
elif c > a and c > b :
    print(f'c {c} is greater tha~n {a}, {b}')