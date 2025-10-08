def main():
    try:
        # 1. open the file for reading
        with open("provinces.txt", "rt") as file:
            # 2. Read each line into a list (strip newline characters)
            provinces = [line.strip() for line in file]

            # 3. Print the entire list
            print("original list of provinces:")
            print(provinces)
            print()

            # 4. Remove the first element

            if provinces:
                provinces.pop(0)

            # 5. Remove the last element

            if provinces:
                provinces.pop(-1)

            # 6. Replace all occurances of "AB" with "Alberta"
            provinces = ["Alberta" if province == "AB" else province for province in provinces]

            # 7. Count the number of times "Alberta" appears
            alberta_count = provinces.count("Alberta")

            # Display the results
            print("Modified list of provinces:")
            print(provinces)
            print()
            print(f"Number of times 'Alberta' appears: {alberta_count}")

    except FileNotFoundError:
        print("Error: Could not find 'provinces.txt'. Make sure it is in the same folder as this script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
