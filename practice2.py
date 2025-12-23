# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)

# factorial
# n = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= n:
#     fact = fact * i
#     i += 1

# print("Factorial =", fact)


#  ------Write a program to print your names ten times.
# n = "komal"
# i = 1
# while i<=10:
#     print(n)
#     i+=1
    
    
    
# Example 7: Write a program to find how many vowels and consonants are present
# in strings    
# s = input("Enter string:")
# v = 0
# c = 0
# i = 0
# while i<len(s):
#     if s[i] in "aeiouAEIOU":
#         v += 1
#     elif s[i] != ' ':
#         c   += 1
#     i += 1
    
# print("vowel :",v)  
# print("consonent :",c)        
    
    
    
#  Write a program to add 5 in each elements in given tuple.
# (10,20,30,40,50)
# t = (10, 20, 30, 40, 50)

# new_t = ()

# for x in t:
#     new_t = new_t + (x + 5,)

# print(new_t)
    
    

#: Write a program to create a list from given string
s = "python"

l = []

for ch in s:
    l.append(ch)

print(l)
 