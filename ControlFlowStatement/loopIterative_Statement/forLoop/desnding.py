l = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(l)
for i in range(n-1):
 for j in range(n-i-1):
  if l[j] < l[j+1]:
   l[j], l[j+1] = l[j+1], l[j]
print(l)