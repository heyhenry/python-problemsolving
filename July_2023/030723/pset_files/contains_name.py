"""
Given a filename ending with `csv`
If that filecontains a `name` column, returns if `name` is in that column
Examples:
contains_name("table1.csv", "goblin") -> True
contains_name("table1.csv", "Eve") -> False // uppercase
contains_name("table2.csv", "bob") -> False // no name column
contains_name("table3.csv", "Taylor Swift") -> True
contains_name("table3.csv", "Sabaton") -> False
"""
def contains_name(filename : str, name : str) -> bool:

    given_extension = filename[-4:]
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()

                results = []

                for row in split_lines:
                    results.append(row.split(','))

                name_exists = False

                for i in results[0]:
                    if 'name' == i:
                        name_exists = True

                if name_exists:

                    name_counter = -1

                    for i in results[0]:
                        name_counter += 1
                        if 'name' == i:
                            break
    
                    for row in results:
                        if name == row[name_counter]:
                            return True
                    return False

                return name_exists

            return False

    return 'Invalid file extension. Must use .csv'

def main():
    print(contains_name("tables_csv/table1.csv", "goblin"))
    print(contains_name("tables_csv/table1.csv", "Eve"))
    print(contains_name("tables_csv/table2.csv", "bob"))
    print(contains_name("tables_csv/table3.csv", "Taylor Swift"))
    print(contains_name("tables_csv/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()