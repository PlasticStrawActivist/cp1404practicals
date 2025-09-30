"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the user input can't be converted to an int.
2. When will a ZeroDivisionError occur? When the denominator varible is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Check if the denominator varible is 0 before the division is executed.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
