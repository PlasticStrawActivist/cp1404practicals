MINIUM_PASSWORD_LENGTH = 8

password = input("Enter password: ")

while len(password) < MINIUM_PASSWORD_LENGTH:
    print(f"Password must be at least {MINIUM_PASSWORD_LENGTH} characters long")
    password = input("Enter password: ")

print("*" * len(password))
