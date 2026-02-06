l = [1,2,4,5,5,11,13,55,1,4]
result = []
for i in l:
    if i not in result:
        result.append(i)
        
print(result)