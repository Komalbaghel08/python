def sum_odd():
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    print("Sum of odd numbers from 1 to", n, "is:", total)

sum_odd()
