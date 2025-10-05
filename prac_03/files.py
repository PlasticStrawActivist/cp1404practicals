"""
CP1404/CP5632 - Practical

"""

PATH = "prac_03"

# 1
name = input("Enter your name: ")
name_file = open(f"{PATH}/name.txt", "w")
print(name, file=name_file)
name_file.close()

# 2
name_file = open(f"{PATH}/name.txt", "r")
print(f"Hi {name_file.read().strip()}!")
name_file.close()

# 3
with open(f"{PATH}/numbers.txt", "r") as file:
    print(int(file.readline()) + int(file.readline()))

# 4
total = 0
with open(f"{PATH}/numbers.txt", "r") as file:
    for line in file.readlines():
        total += int(line)
print(total)
