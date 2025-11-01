"""
Emails
Estimate: 12 minutes
Actual:   10 minutes, 21 seconds
"""

email_to_name = {}


def main() -> None:
    """Email program."""
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        user_input = input(f"Is your name {name}? (Y/n) ")
        is_name_correct = (
            user_input.strip() == "" or user_input.strip().lower() == "y"
        )

        if not is_name_correct:
            name = input("Name: ")

        email_to_name[email] = name

        email = input("Email: ")

    print(
        "\n"
        + "\n".join(
            [f"{name} ({email})" for email, name in email_to_name.items()]
        ),
    )


def extract_name_from_email(email: str) -> str:
    """Extract a name from the given email."""
    suffix = email.split("@")[0]
    return suffix.replace(".", " ").title()


main()
