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

    contains_name = False

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            store_lines = read_content.splitlines()

            name_found = False

            for i in store_lines[0].split(','):
                if 'name' == i:
                    name_found = True    

            if name_found: 
                
                for row in store_lines:
                    for col_name in row.split(','):
                        if col_name == name:
                            contains_name = True

    return contains_name

def main():
    print(contains_name("tables/table1.csv", "goblin"))
    print(contains_name("tables/table1.csv", "Eve"))
    print(contains_name("tables/table2.csv", "bob"))
    print(contains_name("tables/table3.csv", "Taylor Swift"))
    print(contains_name("tables/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()
