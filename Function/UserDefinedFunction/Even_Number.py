 # even number code 
def even(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
x = int(input("enter a no."))
even(x)
