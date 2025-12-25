# n = int(input("Enter number: "))
# count = 0

# for i in str(n):
#     count += 1

# print("Total digits =", count)

# Display numbers except prime numbers
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num)
                break
