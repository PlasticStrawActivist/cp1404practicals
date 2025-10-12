"""
CP1404/CP5632 Practical
List exercises
"""

numbers = []

for _ in range(5):
    numbers.append(int(input("Number: ")))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The averge of the numbers is {sum(numbers) / len(numbers)}")
