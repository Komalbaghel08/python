# Move all zeros to the end of the array
def move_zeros_to_end(arr):
    # Count the number of zeros
    zero_count = arr.count(0)
    
    # Remove all zeros from the array
    arr = [x for x in arr if x != 0]
    
    # Append zeros to the end
    arr.extend([0] * zero_count)
    
    return arr

# Test the function
arr = [1, 0, 2, 0, 3, 0, 4]
print(move_zeros_to_end(arr))