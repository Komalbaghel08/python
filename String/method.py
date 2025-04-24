# upeer case to lower case convert krta h
s="this is python class"
print(s.lower())

# lower case ko upper case me convert krta h
s="this is python class"
print (s.upper())

# swap krta lower case ko upper case me nd vice versa
s="this is python class"
print (s.swapcase())
 
#  capitalize  kar deta h 1st letter ko
s="this is python class"
print (s.title())
 
#  center 
s="this is python class"
print (s.center(100))

# index no. batata h
s="this is python class"
# print(s.index("is"))
# print(s.index("z"))
print(s.index("is",5))

s="this is python class"
print(s.find("is"))
# return -1 if element is noy found
print(s.find("z"))

# count
s="this is python class"
print(s.count("is"))
# return -1 if element is not found
print(s.count("z"))

# join
s1="python"
s2="java"
s3="php"
# print(' ' .join(s1, s2, s3))
print(' ' .join([s1,s2,s3]))
# random koi sa print hoga phle fr koi sa aise
print( type(' ' .join({s1,s2,s3})))

# split Syntax = String.split('seprator',Hoe many time split)
s="this is python class"
print(s.split('i'))
# jitne baar split krna h 1  ki jgh wo digit likh dege
print(s.split('i',1))
# Aur agr aisa kuch de diye jo h hi mhi string me to puri strin de dega 
print(s.split('k'))
