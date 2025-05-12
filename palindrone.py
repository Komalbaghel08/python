s = 'python'
l = len(s)
s1 = ''
i = -1
while l>0:
    x=s[i]
    s1 = ''.join((s1,x))
    i = i-1
    l=l-1

    
if s==s1:
    print(f'given string{s} is palindrome')
else:    
    print("not palindrome")