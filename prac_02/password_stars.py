MINIUM_PASSWORD_LENGTH = 8


def get_password():
    return input("Enter password: ")


def print_password(password):
    print("*" * len(password))


def main():
    password = get_password()

    while len(password) < MINIUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIUM_PASSWORD_LENGTH} characters long")
        password = get_password()

    print_password()


main()
