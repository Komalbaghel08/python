# pass--> skip/pass current block
n = int(input("enter a num"))
i = 1
while i<=n:
    if i==5:
        pass
    else:
        print(i)
        i = i+1