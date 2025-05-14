num1,num2,num3 = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter third number"))
if num1>num2 and num1>num3:
    print(f"{num1}greter than{num2},{num3}")
elif num2>num1 and num2>num3: 
     print(f"{num2}greter than{num1},{num3}")   
else:
    print(f"{num3} is grater then {num1}, {num2}")