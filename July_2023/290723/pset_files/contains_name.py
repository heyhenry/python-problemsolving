"""
Given a filename ending with `csv`
If that file contains a `name` column, returns if `name` is in that column
Examples:
contains_name("table1.csv", "goblin") -> True
contains_name("table1.csv", "Eve") -> False // uppercase
contains_name("table2.csv", "bob") -> False // no name column
contains_name("table3.csv", "Taylor Swift") -> True
contains_name("table3.csv", "Sabaton") -> False
"""
from utilites import check_extension_csv

def contains_name(filename : str, name : str) -> bool:

    if check_extension_csv(filename[-4:]):

        with open(filename, 'r') as file:

            read_content = file.read()

            splitlines = read_content.splitlines()
            lines = []

            for row in splitlines:
                line = row.split(',')
                lines.append(line)

            name_position = -1
            

            for i in lines[0]:
                name_position += 1
                if i == 'name':
                    break

            if name_position != -1:

                for row in range(len(lines)):
                    if name == lines[row][name_position]:
                        return True
                    
                return False
            
            else:

                return False

    else:

        return 'Invalid file extension type.'

def main():
    print(contains_name("tables/table1.csv", "goblin"))
    print(contains_name("tables/table1.csv", "Eve"))
    print(contains_name("tables/table2.csv", "bob"))
    print(contains_name("tables/table3.csv", "Taylor Swift"))
    print(contains_name("tables/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()    