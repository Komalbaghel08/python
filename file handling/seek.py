# cursor movement - seek()
f =open('n1.py')
print(f.tell())

# data = f.read(10)
# print(data)
# print(f.tell())
# data = f.read(10)
# print(data)

# f.close()
# f =open('n1.py','rb')
# print(f.tell())

data = f.read(5)
print(data)
f.seek(5,1)
print(f.tell())
data = f.read(10)
print(data)

f.close()