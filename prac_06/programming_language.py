"""
Programming Language
Estimate: 3 minutes
Actual:   1 minutes, 20 seconds
"""


class ProgrammingLanguge:

    def __init__(self, typing: str, reflection: bool, year: int) -> None:
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        return self.typing == "dynamic"
