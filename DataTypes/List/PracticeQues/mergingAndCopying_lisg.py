# You're given: `a = [1, 2, 3]`, `b = [4, 5, 6]`
# - Combine both lists into a new list `c`.
# - Then make a copy of `c` and store it in `d`.
# - Change the second item of `d` to `99`.- 
# Print both `c` and `d`

a = [1,2,3]
b = [4,5,6]
c = a + b
d = c.copy()
d.insert(1,99)
print(c)
print(d)