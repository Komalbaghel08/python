#start with this list: `letters = ['a', 'b', 'c', 'd', 'e', 'f']`
# - Slice and print the first three elements.
# -Slice and print the last two elements.
# - Replace the middle two (`'c'` and `'d'`) with `['x', 'y']`.
# - Show the modified list.

letters = ['a','b','c','d','e','f']
print(letters[0:3:1])
print(letters[4:6:1])
letters[2:3] = ['x','y']
print(letters)