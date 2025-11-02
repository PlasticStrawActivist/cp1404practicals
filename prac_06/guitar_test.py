"""
Guitar Test
Estimate: 4 minutes
Actual:   6 minutes, 11 seconds
"""

from prac_06.guitar import Guitar


guitars = [Guitar("Gibson L-5 CES", 1922), Guitar("Another Guitar", 2013)]

for index, age in enumerate([103, 12]):
    guitar = guitars[index]
    print(f"{guitar.name} get_age(): Expected {age}. Got {guitar.get_age()}")

for index, is_vintage in enumerate([True, False]):
    guitar = guitars[index]
    print(
        f"{guitar.name} is_vintage(): Expected {is_vintage}. Got {guitar.is_vintage()}"
    )
