# SET METHOD()

# add()
s = {10,20,30,10,40,"python","java","php"}
s.add('html')
print(s)

# update()
s1 = {10,20,30,10,40,"python","java","php"}
s1.update('html','da')
s1.update([10,20])
# ERROR--->s1.update(10,20)
print(s1)

# pop()
s2 = {10,20,30,10,40,"python","java","php"}
s2.pop()
print(s2)

# remove()
s3 = {10,20,30,10,40,"python","java","php"}
s3.remove("java")
# jo element nhi rhta wo dalege to error dega usi ko overcpme krne ke liye discard aaya 
# ERROR --> s3.remove(2)
print(s3)

# discard()
s4 = {10,20,30,10,40,"python","java","php"}
s4.discard(2)
print(s4)

# copy()
s5 = {10,20,30,10,40,"python","java","php"} 
s6 = s5.copy()
print(s5)
print(id(s5),id(s6))

# clear()
s2 = {10,20,30,10,40,"python","java","php"}
s2.clear()
print(s2)

# FOR MATHEMATICAL OPERATION
