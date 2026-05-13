# Contains Duplicate

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
# Example
arr = [1, 2, 3, 4, 2]

if contains_duplicate(arr):
    print("Duplicate element found")
else:
    print("No duplicate element")