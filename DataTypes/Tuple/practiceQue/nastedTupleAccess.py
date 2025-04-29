#Access the number 6 from this tuple: (1, (2, 3, (4, 5, 6))). 
t = (1, (2, 3, (4, 5, 6)))
t1 = t[1][2][2]
print(t1)