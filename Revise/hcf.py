# Write a program to find HCF of two numbers
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a,b = b,a%b
print("HCF is: ",a)'''


# LCM of Three Numbers
def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

lcm_ab = (a * b) // hcf(a, b)
lcm_abc = (lcm_ab * c) // hcf(lcm_ab, c)

print(lcm_abc)