#ek list hai jisme tumhe:
#1. sab number ka even nikalna hai using filter
#2. phir even number ka square kerna hai using map
#3. phir jo even number the uska sum / total kera hai using reduce

from functools import reduce

def even_num(n):
    return n % 2 == 0

def square_num(n):
    return n * n

def total_num(x, y):
    return x + y

number = [1,2,3,4,5,6,7,8,9]

even = list(filter(even_num, number))
print(even)

square = list(map(square_num, even))
print(square)

total = reduce(total_num, square)
print(total)