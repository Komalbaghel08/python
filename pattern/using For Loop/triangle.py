# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
 print("* "*i)
m=n-1
for i in range(m,0,-1):
 print("* "*i)
 
 # *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *
n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
 print(" "*(n-i),"*"*i)
for i in range(n,0,-1):
 print(" "*(n-i),"*"*i)
 
 