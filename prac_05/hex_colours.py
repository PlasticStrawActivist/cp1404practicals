"""
CP1404/CP5632 Practical
Color names in a dictionary
"""

COLOUR_TO_HEX = {
    "absolute zero": 0x0048BA,
    "acid Green": 0xB0BF1A,
    "alice blue": 0xF0F8FF,
    "alizarin crimson": 0xE32636,
    "amaranth": 0xE52B50,
    "amber": 0xFFBF00,
    "amethyst": 0x9966CC,
    "antique white": 0xFAEBD7,
    "apricot": 0xFBCEB1,
    "aqua": 0x00FFFF,
    "aquamarine": 0x7FFFD4,
}


colour_code = input("Enter colour name: ").lower()
while colour_code != "":
    try:
        print(
            colour_code.title(),
            "is",
            hex(COLOUR_TO_HEX[colour_code]).replace("0x", "#"),
        )
    except KeyError:
        print("Invalid colour name")
    colour_code = input("Enter colour name: ").lower()
