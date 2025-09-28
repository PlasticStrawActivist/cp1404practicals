"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def main():
    """Determine the user's score status and generates a random score and score status."""
    user_score = float(input("Enter score: "))
    random_score = randint(0, 100)
    print(determine_score_status(user_score))
    print(f"Random score of {random_score} {determine_score_status(random_score)}")


def determine_score_status(score):
    """Determine the score status."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


if __name__ == "__main__":
    main()
