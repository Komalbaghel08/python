t = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0
# while i < len(t):
#     if (t[i] == x):
#         print("FOUND AT IDX", i)
# else:
#         print("finding..")
# i += 1

    
    # using break
x = 36
i = 0
while i < len(t):
    if (t[i] == x):
        print("FOUND AT IDX", i)
        break
    else:
        print("finding..")
    i += 1
print("end of loop")    