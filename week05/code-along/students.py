import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a dictionary.
    Args:
        filename (str): The name of the CSV file.
        key_column_index (int): The index of the column to use as the key.
    Returns:
        dict: A dictionary with keys from the key column and values as rows.
    """
    s_dictionary = {}
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # Skip header line

        for row in csvreader:
            if len(row) == 0:
                continue  # skip empty lines

            key_value = row[key_column_index].replace("-", "").strip()
            s_dictionary[key_value] = row

    return s_dictionary


def main():
    KEY_INDEX = 0
    NAME_INDEX = 1

    students = read_dictionary("students.csv", KEY_INDEX)
    print("Welcome to the Student Lookup System!")
    print("Enter 'quit' to exit at any time.\n")

    while True:
        inumber = input("Please enter an I-NUMBER: ").strip()

        if inumber.lower() == "quit":
            print("\nExiting program. Goodbye!")
            break

        # Remove dashes if user includes them
        inumber = inumber.replace("-", "")

        # Validate ID Number
        if not all(ch.isdigit() for ch in inumber):
            print("Invalid I-NUMBER: must contain only digits or dashes.\n")

        elif len(inumber) < 9:
            print("Invalid I-NUMBER: too few digits.\n")

        elif len(inumber) > 9:
            print("Invalid I-NUMBER: too many digits.\n")

        else:
            # Lookup student
            if inumber in students:
                student = students[inumber]
                name = student[NAME_INDEX]
                print(f"Student Found: {name}\n")
            else:
                print("No such student.\n")


if __name__ == "__main__":
    main()
