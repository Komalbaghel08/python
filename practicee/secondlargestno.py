numbers = [12, 45, 7, 89, 23, 56, 89, 34]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second Largest Number:", unique_numbers[-2])
else:
    print("No second largest number found")