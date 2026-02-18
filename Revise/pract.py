# Reverse a Number
# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n  //= 10
# print("Reversed number: ", rev)

# # Check Prime
# n = int(input("Enter a number: "))
# flag = True
# if n <= 1:
#     flag = False
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             flag = False
#             break
# if flag:
#     print("prime")
# else:
#     print("not prime")


# Armstrong Number
# n = int(input("Enter a number: "))
# temp = n 
# power = len(str(n))
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total = total+digit**power
#     temp //= 10
# if total == n:
#     print("Armstrong number")
# else:   
#     print("Not an Armstrong number")
    
    
# Palindrome Number
# num = int(input("Enter number: "))
# original = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# if original == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

'''second method'''
# def is_palindrome(s):
#     rev = " "
#     for i in s:
#         rev = i + rev
#     if rev == s:
#         return "palindrome"
#     else:
#         return "not palindrome"
# s = input("Enter a string: ")
# print(is_palindrome(s))



# Factorial
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial: ", fact)