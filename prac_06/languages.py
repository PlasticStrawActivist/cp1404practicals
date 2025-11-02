"""
Languages
Estimate: 2 minutes
Actual:   2 mintues, 34 seconds
"""

from prac_06.programming_language import ProgrammingLanguge

python = ProgrammingLanguge("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguge("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguge("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
print(
    "\n".join(
        [language.name for language in languages if language.is_dynamic()]
    )
)
