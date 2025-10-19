FILENAME = "prac_05/wimbledon.csv"


def main():
    """Wimbledon program."""
    records = read_records()
    champion_to_number_of_wins, winning_countries = proccess_records(records)
    display_results(champion_to_number_of_wins, winning_countries)


def proccess_records(
    records: list[list[str, str, str]],
) -> tuple[dict[str, int], set[str]]:
    """Proccess Wimbledon records."""
    champion_to_number_of_wins = {}
    winning_countries = set()

    for _, country, name in records:
        winning_countries.add(country)
        if name in champion_to_number_of_wins:
            champion_to_number_of_wins[name] += 1
        else:
            champion_to_number_of_wins[name] = 1

    return champion_to_number_of_wins, winning_countries


def read_records() -> list[list[str, str, str]]:
    """Read Wimbledon records from csv file."""
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        records = [line.split(",")[:3] for line in file]
    records.pop(0)
    return records


def display_results(
    champion_to_number_of_wins: dict[str, int], winning_countries: set[str]
) -> None:
    """Display Wimbledon results."""
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
