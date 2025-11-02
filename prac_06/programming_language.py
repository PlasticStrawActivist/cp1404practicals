"""
Programming Language
Estimate: 3 minutes
Actual:   1 minutes, 20 seconds
"""


class ProgrammingLanguge:

    def __init__(
        self, name: str, typing: str, reflection: bool, year: int
    ) -> None:
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        return f"{self.name}, {self.typing.title()} Typing, Reflection={self.reflection}, First appeared in {self.year}"
