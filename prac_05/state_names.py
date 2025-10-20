"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}

for short_name, long_name in STATE_CODE_TO_NAME.items():
    print(f"{short_name:3} is {long_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", STATE_CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
