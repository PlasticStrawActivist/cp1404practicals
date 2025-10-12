"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_data(FILENAME)
    display_subject_details(subjects)


def load_data(filename=FILENAME):
    """
    Read data from file formatted like: subject,lecturer,number of students.
    Returns a list of subject contaiing a list of subject data.
    """
    data = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(",")  # Separate the data into its parts
        print(
            parts
        )  # See what the parts look like (notice the integer is a string)
        parts[2] = int(
            parts[2]
        )  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(subjects):
    """
    Prints a subject info based on the parsed subject data.
    Requires a list of subjects containing a list of the subject code, lecturer and number of students
    """
    lecturer_length = max([len(subject[1]) for subject in subjects])
    number_of_student_length = max(
        [len(str(subject[2])) for subject in subjects]
    )

    for subject_code, lecturer, number_of_students in [
        tuple(subject) for subject in subjects
    ]:
        print(
            f"{subject_code} is taught by {lecturer:{lecturer_length}} and has {number_of_students:{number_of_student_length}}"
        )


main()
