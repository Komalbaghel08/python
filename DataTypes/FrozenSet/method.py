# 1. union()
s = [1,2,4,5,6,5]
s1 = [5,6,7,5,4]
fs1 =  frozenset(s)
fs2 =  frozenset(s1)
print(fs1.union(fs2))

# 2. intersection()
s = [1,2,4,5,6,5]
s1 = [5,6,7,5,4]
fs1 =  frozenset(s)
fs2 =  frozenset(s1)
print(fs1.intersection(fs2))

# 3. difference()
s = [1,2,4,5,6,5]
s1 = [5,6,7,5,4]
fs1 =  frozenset(s)
fs2 =  frozenset(s1)
print(fs1.difference(fs2))

# 4. symmetric difference()
# 5. superset()
# 6. dissjoint()
# 7. subset()