l = [1,4,9,16,35,43,63,25,99,12,43]
x = 43

idx = 0
for i in l:
    if(i == x):
        print("number found at idx", idx)
        break # agr chahe ki aik baar number mile aur quit kr jaye means break
    idx += 1    