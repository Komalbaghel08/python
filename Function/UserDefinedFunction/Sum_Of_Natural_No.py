def naturalno_sum(n):
    sum = 0
    for i in (1,n+1):
      sum = sum+i
    return sum
x = int(input("enter a no."))
total_sum = naturalno_sum(x)
print(total_sum)