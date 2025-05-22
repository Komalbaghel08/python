# def largest(a,b,c):
#   return max(a,b,c)
# print(largest(1,5,77))

# second way
def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest(66,753,333))    