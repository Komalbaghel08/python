# Simple To-Do List App
# Good for GitHub practice 🚀

tasks = []

def show_menu():
    print("\n===== TO-DO MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            remove_index = int(input("Enter task number to remove: ")) - 1

            if 0 <= remove_index < len(tasks):
                removed = tasks.pop(remove_index)
                print(f"'{removed}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
        
        
        # passward generator
# Password Generator 🔐

import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()"

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)