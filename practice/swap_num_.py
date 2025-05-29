s = 'python'

s = list(s)
s[0], s[-1] = s[-1], s[0] 
s = ''.join(s)
print(s)