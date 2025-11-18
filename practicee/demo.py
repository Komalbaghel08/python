operators = "+-*/%"

while True:
    expr = input("Enter expression: ")

    # check for double operators
    valid = True
    for i in range(len(expr) - 1):
        if expr[i] in operators and expr[i+1] in operators:
            valid = False
            break

    if not valid:
        print("Error: Two operators together are not allowed.")
        continue

    try:
        result = eval(expr)
        print("Result:", result)
    except ZeroDivisionError:  #ZeroDivisionError built in h 
        print("Error: Cannot divide by zero.")
    except:
        print("Error: Invalid expression.")
