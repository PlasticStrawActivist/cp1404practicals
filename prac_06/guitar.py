"""
Guitar
Estimate: 4 minutes
Actual: 2 minutes, 30 seconds
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0) -> None:
        """Initialise a Guitar instance.

        name: float, name of guitar
        year: int, year the guitar was made
        cost: float, cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        """String method for Guitar object."""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self) -> int:
        """String age of guitar."""
        return 2025 - self.year

    def is_vintage(self) -> bool:
        """Return True if the age is greater than or equal to 50."""
        return self.get_age() >= 50
