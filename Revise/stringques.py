# Reverse String 
s = input("Enter a string: ")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev+s[i]
print("Reversed string: ", rev)


# ------------------------------
def is_palindrome(s):
    rev = " "
    for i in s:
        rev = i + rev
    if rev == s:
        return "palindrome"
    else:
        return "not palindrome"
    
    
# Count Vowels
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in 'aeiouAEIOU':
        count += 1
print("Number of vowels in the string: ", count)


# Remove Spaces
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch != " ":
        result += ch
print("String after removing spaces: ", result)


# Count Digits
n = int(input())
count = 0

while n > 0:
    n = n // 10
    count += 1

print(count)