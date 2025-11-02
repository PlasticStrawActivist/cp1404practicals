"""
Guitar
Estimate: 4 minutes
Actual: 2 minutes, 30 seconds
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0) -> None:
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self) -> int:
        return 2025 - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= 50
