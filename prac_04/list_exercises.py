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

usernames = [
    "jimbo",
    "giltson98",
    "derekf",
    "WhatSup",
    "NicolEye",
    "swei45",
    "BaseInterpreterInterface",
    "BaseStdIn",
    "Command",
    "ExecState",
    "InteractiveConsole",
    "InterpreterInterface",
    "StartServer",
    "bob",
]

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
