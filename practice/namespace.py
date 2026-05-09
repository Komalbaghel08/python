# Namespace == name+objectvalue
# type--- 1:local  2:global  3:builtin
#  .py ka entry point __main__ (underscrore underscrore main underscrore underscrore) hota h. 


import builtins
x = 10
y=20
z=30
def first():
    x = 1
    y=2
    z=3
    print(locals())
first()
print(globals())   
print(dir(builtins))