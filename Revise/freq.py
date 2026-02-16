s = input()

freq = {}

i = 0
while i < len(s):
    ch = s[i]
    num = int(s[i+1])
    
    if ch in freq:
        freq[ch] += num
    else:
        freq[ch] = num
    
    i += 2

result = ""
for ch in sorted(freq):
    result += ch + str(freq[ch])

print(result)
