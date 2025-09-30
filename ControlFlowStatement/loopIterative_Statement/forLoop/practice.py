# Upto n natural no
# n = int(input("enter no"))
# for i in range(1,n+1):
#     if i<n:
#         print(i,end=",")
#     else:
#         print(i)

#__________________________________OR______________________________
# n = int(input("Enter no: "))
# for i in range(1, n+1):
#     print(i)


# for upto n even natural no.
# n = int(input("enter no: "))
# for i in range(2,n+1,2):
#     print(i,end = " ")

# for upto n odd natural no.
# n = int(input("enter no: "))
# for i in range(1,n+1,2):
#     print(i,end=" ")

# WAP to check given number is prime or not.
# n = int(input("enter no: "))
# factor = 0
# if n == 0 or n == 1:
#     print(n,"is not prime num")
# elif n>1:
#     for i in range(2,n):
#         if(n % 2 == 0):
#             factor += 1
#             break
#     if factor == 0:
#         print(n,"is prime number")
#     else:
#         print(n,"is not a prime") 
        
        
## LCM :-----------        
# x = int(input("Enter any number: "))
# y = int(input("Enter any number: "))
# if x > y:
#     greater = x
# else:
#     greater = y
# while(True):
#     if((greater % x == 0) and (greater % y == 0)):
        
#         lcm = greater
#         break
#     greater += 1
# print("LCM of", x, "and", y, "is", lcm)
     
## HCF :----------
# x = int(input("Enter any number: "))
# y = int(input("Enter any number: "))
# if x<y:
#     smaller = x
# else:
#     smaller = y 
# for i in range(1,smaller+1):
#     if(x%i==0 and y%i==0):
#         hcf = i
# print("HCF of",x, "and", y ,"is", hcf )    


    
  ## Factors :--
n = int(input("enter any no.:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)                                       