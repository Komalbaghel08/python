# def count_pairs(arr, k):
#     remainder_count = [0] * k
#     count = 0

#     for num in arr:
#         remainder = num % k
#         complement = (k - remainder) % k
#         count += remainder_count[complement]
#         remainder_count[remainder] += 1

#     return count


# # Example
# arr = [2, 2, 1, 7, 5, 3]
# k = 4
# print(count_pairs(arr, k))




def first_non_repeating(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return -1

print(first_non_repeating("aabccdeff"))