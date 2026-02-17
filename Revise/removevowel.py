# Write a program to remove all vowels from a string

s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.lower() not in "aeiou":
        result += ch
print("String after removing vowels: ", result)