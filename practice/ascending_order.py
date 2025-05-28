l = [10, 2, 4, 6, 8, 20]

i = 0
while i < len(l) - 1:
    if l[i] > l[i + 1]:
        l[i], l[i + 1] = l[i + 1], l[i]
        i = 0  #
    else:
        i += 1

print("Ascending order:", l)
