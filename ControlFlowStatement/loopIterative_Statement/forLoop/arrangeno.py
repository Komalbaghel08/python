# WAP to arrenge all even and odd no at a place.
l = [2,1,3,8,4,8,5] # [2,8,4,8,1,3,5]
l1=[]
for i in l:
 if i %2==0:
  l1.append(i)
for i in l:
 if i%2 !=0:
  l1.append(i)
print(l1)


# WAP to arrenge all zeroes at the end.
l = [2,0,3,0,1,0,5] # [2,3,1,5,0,0,0]
l1=[]
for i in l:
 if i !=0:
  l1.append(i)
n = len(l)-len(l1)
for i in range(n):
 l1.append(0)
print(l1)