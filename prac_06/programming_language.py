"""
Programming Language
Estimate: 3 minutes
Actual:   1 minutes, 20 seconds
"""


class ProgrammingLanguge:
    """Represent a Programming Language object."""

    def __init__(
        self, name: str, typing: str, reflection: bool, year: int
    ) -> None:
        """Initialise a ProgrammingLanguge instance.

        name: str, name of language
        reflection: bool, if language has reflection
        year: int, year of language
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        """Return True if 'typing' is equal to 'dynamic'."""
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        """String method for ProgrammingLanguge object."""
        return f"{self.name}, {self.typing.title()} Typing, Reflection={self.reflection}, First appeared in {self.year}"
