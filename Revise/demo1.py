# s = "python"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)    

'''using function'''
# def rev_string(s):
#     rev =''
#     for i in s:
#         rev = str(i)+rev
#     return rev
# s = input("enter string :")
# print("reversed string: " , rev_string(s))


'''palindrome'''
def is_palindrome(s):
    rev = ""
    s = str(s)
    for i in s:
        rev = i+rev
    if s == rev:
        return "palindrome"
    else:
        return "not palindrome"
s = input("enter string :")
print(is_palindrome(s))