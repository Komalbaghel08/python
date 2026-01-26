n = int(input("Enter number: "))

count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

# Optimized version
n = int(input("Enter number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
    
    