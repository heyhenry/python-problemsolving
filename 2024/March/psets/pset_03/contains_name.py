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

    name_found = False
    desired_extension = '.csv'
    given_extension = filename[filename.rfind('.'):]

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                lines = read_content.splitlines()  
                content = []

                for row in lines:
                    content.append(row.split(','))

                if 'name' in content[0]:
                    for row in content:
                        if name == row[content[0].index('name')]:
                            name_found = True
                            break

    return name_found

def main():
    print(contains_name("tables/table1.csv", "goblin"))
    print(contains_name("tables/table1.csv", "Eve"))
    print(contains_name("tables/table2.csv", "bob"))
    print(contains_name("tables/table3.csv", "Taylor Swift"))
    print(contains_name("tables/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()