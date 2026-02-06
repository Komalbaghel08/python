# marks = {
#     "A": 78,
#     "B": 92,
#     "C": 85
# }

# max_val = 0 
# topper = ""
# for key in marks:
#     if marks[key] > max_val:
#         max_val = marks[key]
#         topper = key
# print(topper, max_val)



# username = "admin"
# password = "1234"

# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid credentials")



data = [10, 20, 30]

try:
    print(data[5])
except IndexError:
    print("Index out of range")
