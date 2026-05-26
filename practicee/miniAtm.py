balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print("Amount Deposited Successfully")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You for Using ATM")
        break

    else:
        print("Invalid Choice! Please try again.")