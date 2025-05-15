def sum_even():
    x = int(input("Enter the upper limit: "))
    total = 0
    for i in range(1, x + 1):
        if i % 2 == 0:
            total += i
    print("Sum of even numbers from 1 to", x, "is:", total)

sum_even()
