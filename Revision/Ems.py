# employee_management.py

employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")

    employee = {
        "ID": emp_id,
        "Name": name,
        "Salary": salary
    }

    employees.append(employee)
    print("✅ Employee added successfully!\n")


def view_employees():
    if not employees:
        print("No employees found.\n")
        return

    print("\nEmployee List:")
    for emp in employees:
        print(f"ID: {emp['ID']} | Name: {emp['Name']} | Salary: {emp['Salary']}")
    print()


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print("🗑 Employee deleted successfully!\n")
            return

    print("Employee not found.\n")


def menu():
    while True:
        print("------ Employee Management System ------")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


menu()


