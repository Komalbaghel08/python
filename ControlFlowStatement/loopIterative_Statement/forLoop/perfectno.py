n=int(input("Enter any no:"))
sum = 0
for i in range(1,n):
 if n%i==0:
  sum=sum+i
if n==sum:
 print(f'given number {n} is perfect number')
else:
 print(f'given number {n} is not a perfect number')