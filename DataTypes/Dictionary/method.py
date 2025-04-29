# copy()-->create new object
d = {'name':'komal','age':21,'quali':'btech'}
d1 = d.copy()
print(d,d1)
print(id(d),id(d1))

# clear()-->remove all pair from dictionary
d1 = {'name':'komal','age':21,'quali':'btech'}
d1.clear()
print(d1)
print(id(d1))
# del d1   Error
# print(d1)

# pop()-->remove targeted key from dictionry
d1 = {'name':'komal','age':21,'quali':'btech'}
d1.pop('name')
print(d1)

# popitem()-->remove lat pair/item from dictionry
d1 = {'name':'komal','age':21,'quali':'btech'}
d1.popitem()
print(d1)

# get()-->get value of targeted key.
d1 = {'name':'komal','age':21,'quali':'btech'}
new = d1.get('name')
print(new)

# keys()-->collect all keys from dictionry in form of list
d1 = {'name':'komal','age':21,'quali':'btech'}
print(d1.keys())

# values()-->collect all values from dictionry in form of list
d1 = {'name':'komal','age':21,'quali':'btech'}
print(d1.values())

# items()-->collect all items(key,value) from dictionry in form of list
d1 = {'name':'komal','age':21,'quali':'btech'}
print(d1.items())

# fromkeys()--> create new  dictionry on the basis of given collection element
s = 'python'
d = dict.fromkeys(s,10) #Agr yha pe 10 ki jgh me agr kuch nhi to none value hogi
print(d)

# setdefaily()
d = {'x':10, 'y':20, 'z':30}
d.setdefault('x',50)
print(d)

# update()