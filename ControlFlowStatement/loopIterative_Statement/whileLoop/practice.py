# Printing numbers from 1 to 5 by using while loop
# x = 1
# while x<=5:
#     print(x)
#     x+=1


# Printing even numbers from 10 to 20 by using while loop.
# x = 10
# while(x>=10) and (x<=20):
#     print(x)
#     x+=2
# print("End")    


#  print sum of given natural number
# x=int(input("Enter any no : "))
# sum = 0 
# i = 1
# while i<=x:
#     sum = sum+i
#     if i<x:
#         print(i,end='+')
#     else:
#         print(i,end='=')
#     i=i+1
# print(sum)      


# print n even numbers
# x= int(input("Enter how many even number you want :"))
# n = 1
# while n<=x:
#     print(2*n)
#     n = n+1
    
    
# Print sum of given even numbers    
# x= int(input("Enter how many even number you want :"))
# n = 1 
# sum = 0
# while n<=x:
#     sum = sum+2*n
#     if n<x:
#         print(2*n,end="+")
#     else:
#         print(2*n,end="=")
#     n = n+1
# print(sum) 



# Print  n odd numbers    
# x= int(input("Enter how many even number you want :"))
# n = 1 
# while n<=x:
#     if n<x:
#         print((2*n-1),end=",")
#     else:
#         print((2*n-1),end="")
#     n = n+1
  
  
# Print sum of n odd numbers    
x= int(input("Enter how many even number you want :"))
n = 1 
sum = 0
while n<=x:
    sum = sum+(2*n-1)
    if n<x:
        print((2*n-1),end="+")
    else:
        print((2*n-1),end="=")
    n = n+1
print(sum)                