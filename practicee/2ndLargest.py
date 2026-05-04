def second_largest(nums):
    first = second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

# Example
numbers = [10, 5, 20, 8]
print("Second Largest:", second_largest(numbers))