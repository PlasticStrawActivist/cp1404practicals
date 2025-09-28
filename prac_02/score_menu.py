"""
CP1404/CP5632 - Practical
Program to show a score menu
"""

from score import determine_score_status

MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    """Get a valid score from the user and display a menu to the user."""
    score = get_valid_score()
    print_menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print(print_stars(score))
        else:
            print("Invalid option")

        print_menu()
        choice = get_choice()

    print("Goodbye")


def get_choice():
    """Get user choice from the user."""
    return input(">>> ").upper()


def print_menu():
    """Print the menu to the user."""
    print(MENU)


def get_valid_score():
    """Get a score form the user until it is valid."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100 inclusive")
        score = int(input("Enter score: "))
    return score


def print_stars(score):
    """Print n amount of stars according the the score."""
    print("*" * score)


main()
