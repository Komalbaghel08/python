l = [10, 2, 4, 6, 8, 20]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] < l[j]: 
            l[i], l[j] = l[j], l[i]

print("Descending order:", l)
