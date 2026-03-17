s = input("Enter string: ")

freq = {}

# Step 1: Count frequency
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: Find first non-repeating
index = -1
for i in range(len(s)):
    if freq[s[i]] == 1:
        index = i
        break

print("First non-repeating character index:", index)