from score import determine_score_category

MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    print_menu()
    score = get_valid_score()

    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            print(f"Score is {score}")
        elif choice == "P":
            print(determine_score_category(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid option")

        print_menu()
        choice = get_choice()

    print("Goodbye")


def get_choice():
    return input(">>> ").upper()


def print_menu():
    print(MENU)


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100 inclusive")
        score = int(input("Enter score: "))
    return score


def print_score(score):
    print(f"Score is {score}")


def print_result(score):
    print(f"Score is {score}")


def print_stars(score):
    print("*" * score)


main()
