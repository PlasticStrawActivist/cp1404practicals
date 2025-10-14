"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_KEY_MAP = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}

for short_name, long_name in STATE_KEY_MAP.items():
    print(f"{short_name:3} is {long_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", STATE_KEY_MAP[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
