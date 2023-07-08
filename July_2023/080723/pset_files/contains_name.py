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

    d_ext = '.csv'
    ext = filename[-4:]

    if ext == d_ext:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content: 

                split_lines = read_content.splitlines()

                converted = []

                for row in split_lines:
                    line = row.split(',')
                    converted.append(line)

                name_col_exists = False
                name_pos = -1

                for i in converted[0]:
                    name_pos += 1
                    if 'name' == i:
                        name_col_exists = True
                        break

                if name_col_exists:

                    for row in converted:
                        if name == row[name_pos]:
                            return True
                    return False
                
                return False

            return False

    return 'Invalid file extension. Use .csv'

def main():
    print(contains_name("tables_csv/table1.csv", "goblin"))
    print(contains_name("tables_csv/table1.csv", "Eve"))
    print(contains_name("tables_csv/table2.csv", "bob"))
    print(contains_name("tables_csv/table3.csv", "Taylor Swift"))
    print(contains_name("tables_csv/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()