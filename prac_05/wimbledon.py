FILENAME = "prac_05/wimbledon.csv"


def main():
    """Wimbledon program."""
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        data = [line.split(",")[:3] for line in file]
    data.pop(0)

    champion_to_number_of_wins = {}
    winning_countries = set()
    for _, country, name in data:
        winning_countries.add(country)
        if name in champion_to_number_of_wins:
            champion_to_number_of_wins[name] += 1
        else:
            champion_to_number_of_wins[name] = 1

    print(
        "\n".join(
            [
                f"{name} {number_of_wins}"
                for name, number_of_wins in champion_to_number_of_wins.items()
            ]
        )
    )

    print(f"\nThese {len(winning_countries)} have won Winbledon:")
    print(", ".join(sorted(winning_countries)))


main()
