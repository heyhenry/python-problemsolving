"""
Given a filename ending with `csv`
If that filecontains a `name` column, returns if `name` is in that column
Examples:
contains_name("tables/table1.csv", "goblin") -> True
contains_name("tables/table1.csv", "Eve") -> False // uppercase
contains_name("tables/table2.csv", "bob") -> False // no name column
contains_name("tables/table3.csv", "Taylor Swift") -> True
contains_name("tables/table3.csv", "Sabaton") -> False
"""
def contains_name(filename : str, name : str) -> bool:

    result = False

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()
            content = []

            for row in split_lines:
                content.append(row.split(','))

            name_found = False
            name_index = -1

            for column in range(len(content[0])):
                if content[0][column] == 'name':
                    name_found = True
                    name_index = column

            if name_found:

                actual_name_found = False
                for row in content:
                    if row[name_index] == name:
                        actual_name_found = True
                
                if actual_name_found:

                    result = True

    return result
            
def main():
    print(contains_name("tables/table1.csv", "goblin"))
    print(contains_name("tables/table1.csv", "Eve"))
    print(contains_name("tables/table2.csv", "bob"))
    print(contains_name("tables/table3.csv", "Taylor Swift"))
    print(contains_name("tables/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()