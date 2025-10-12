"""
CP1404/CP5632 - Practical
Quick picks
"""

from random import randint

NUMBERS_PER_LINE = 6
QUICK_PICK_FLOOR = 1
QUICK_PICK_CEILING = 45


def main():
    """Quick picks program"""

    max_number_length = len(str(QUICK_PICK_CEILING))
    number_of_quick_picks = int(input("How many quick picks? "))

    while number_of_quick_picks < 0:
        print("Must be greater than 0")
        number_of_quick_picks = input("How many quick picks? ")

    for _ in range(number_of_quick_picks):
        chosen_numbers = []
        possible_numbers = list(range(QUICK_PICK_FLOOR, QUICK_PICK_CEILING + 1))
        for _ in range(NUMBERS_PER_LINE):
            chosen_number = possible_numbers[
                randint(0, len(possible_numbers) - 1)
            ]
            possible_numbers.remove(chosen_number)
            chosen_numbers.append(chosen_number)

        chosen_numbers.sort()
        print(
            " ".join(
                f"{number:{max_number_length}}" for number in chosen_numbers
            )
        )


main()
