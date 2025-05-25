n = input("enter a number: ")
# new = "".join(reversed(n))

# if n == new:
#     print(f'Given {n} is palindrome')
# else :
#     print(f'Given {n}  is not palindrome') 
    
     
    #  Second way 
if n == n[::-1] :
    print(f'Given {n} is palindrom.')
else :
    print(f'Given {n} is not palindrom.')