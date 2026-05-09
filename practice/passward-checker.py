import re
import random
import string

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak 😬"
    elif score == 3 or score == 4:
        return "Medium 🙂"
    else:
        return "Strong 💪"

def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(all_chars) for _ in range(length))


if __name__ == "__main__":
    print("1. Check Password Strength")
    print("2. Generate Strong Password")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        pwd = input("Enter password: ")
        print("Password Strength:", check_strength(pwd))
    elif choice == "2":
        print("Generated Password:", generate_password())
    else:
        print("Invalid choice")