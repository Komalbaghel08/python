# WAP to find sum of first n numbers (n = natural number)
n = int(input("Enter number : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum = ",sum)    