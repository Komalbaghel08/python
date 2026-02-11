# s = "python"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)    

def rev_string(s):
    rev =''
    for i in s:
        rev = str(i)+rev
    return rev
s = input("enter string :")
print("reversed string: " , rev_string(s))