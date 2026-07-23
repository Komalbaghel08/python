def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


arr = list(map(int, input().split()))
print(find_largest(arr))

