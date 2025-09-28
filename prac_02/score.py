"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def determine_score_category(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


def main():
    user_score = float(input("Enter score: "))
    random_score = randint(0, 100)
    print(determine_score_category(user_score))
    print(f"Random score of {random_score} {determine_score_category(random_score)}")


main()
