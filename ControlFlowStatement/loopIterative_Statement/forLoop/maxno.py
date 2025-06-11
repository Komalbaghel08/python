l = [2,4,9,3,5]
max = l[0]
for i in range(len(l)-1):
 if l[i]>l[i+1]:
  max = l[i]
  l[i],l[i+1]=l[i+1],l[i]
else:
 max=l[i+1]
print(max)