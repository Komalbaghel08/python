h = int(input('Enter hindi marks :'))
e = int(input('Enter english marks :'))
m = int(input('Enter math marks :'))
if (h >= 0 and h <= 100 and e >= 0 and e <= 100 and m >= 0 and m <= 100):
    avg = h + e + m/3
    
    if avg >= 60 :
        print(f"{avg}first division.")
    elif avg >= 45 and avg <= 59:
            print(f"{avg} second division")
    elif avg >= 35 and avg <= 44:
            print(f"{avg} third division")
    else:
        print(f"Fail!")      
else:
    print(f"you enter invalid marks")          