#  append --> add single element in last position
l = [2,4,5,'python','java']
l.append('HTML')
print(l)

# extend --> add multiple element in last position
l = [2,4,5,'python','java']
# l.extend(22,22) isme error aayega wo v dekhna h 
l.extend("html" "css")

# OR
# aisa v kr skte h 
t = (10,20,30)
l.extend(t)
print(l)

# insert --> add single elememt in targeted position
l = [2,4,5,6,7,10]
l.insert(0,'python')
l.insert(1,['python','java','php'])
print(l)

# pop()  --> remove last element from list (kv v beech ke element ko target krke nhi htayege jb khi jada jrurt h to kr skte )
l = [2,4,5,6,7,10]
print(l.pop())
# print(l.pop(2)) -->(aisa bht kam krege remove se krte h ye )
print(l)

# remove()--> remove targeted element from list
l = [2,4,5,6,7,10]
print(l.pop(4))
print(l)

# copy()--> creat new object with same element
l = [2,4,5,6,'python','php']
l1 = l.copy()
print(id(l),id(l1))

# clear() --> remove all the element from list
l = [2,4,5,6,'python','php']
print (l.clear())
print(l)
print(id(l))
# del l
# print(l) error

# reverse() --> reverse all element from list 
l = [2,4,5,6,7,10]
print(l.reverse())
print(l)

# sort() --> arrange assending order
# l = [2,4,5,6,7,10,'python']   error 
# print(l.sort())
l = ['python','java','php']
print(l.sort())
print(l)

# index()--> finding element position
l = [2,4,5,6,7,10]
print(l.index(2))

# count()-->calculate frequency  or  of occurence of any element --(aur agr aisa number de jo nhi h usme 0 aayega)
l = [2,4,5,6,7,10]
print(l.count(2))

