a = int(input("enter"))
sum = 0 
for i in range(1,11):
    c = a*i
    sum = sum+c 
    if i<10:
        print(c,end="+")
    else:
        print(c,end=" = ")    
print(sum)    