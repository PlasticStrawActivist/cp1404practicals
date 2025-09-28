"""
CP1404/CP5632 - Practical
Program get and display a password
"""

MINIUM_PASSWORD_LENGTH = 8


def main():
    """Get a valid password from the user and display it as stars."""
    password = get_password()

    while len(password) < MINIUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIUM_PASSWORD_LENGTH} characters long")
        password = get_password()

    print_obsuciated_password()


def get_password():
    """Get a password from the user."""
    return input("Enter password: ")


def print_obsuciated_password(password):
    """Print a password as stars."""
    print("*" * len(password))


main()
