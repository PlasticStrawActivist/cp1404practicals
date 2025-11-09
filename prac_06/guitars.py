"""
Guitar
Estimate: 20 minutes
Actual:   21 minutes, 28 seconds
"""

from prac_06.guitar import Guitar


def main():
    """Guitar program."""
    print("My guitars")
    guitars = []
    name = input("Name: ")
    while name != "":
        while True:
            try:
                year = int(input("Year: "))
            except ValueError:
                print("Year must be an int")
                continue
            else:
                break

        while True:
            try:
                cost = float(input("Cost: $"))
            except ValueError:
                print("Cost must be a float")
                continue
            else:
                break

        guitars.append(Guitar(name, year, cost))
        print(f"{guitars[-1]} added.\n")
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}"
        )


main()
