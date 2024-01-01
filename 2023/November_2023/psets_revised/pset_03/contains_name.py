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

    desired_ext = '.csv'
    given_ext = filename[-4:]

    if given_ext == desired_ext:
        with open(filename, 'r') as file:
            read_content = file.read()
            result = False
            if read_content:
                split_content = read_content.splitlines()
                content = []
                for row in split_content:
                    temp = []
                    for i in row.split(','):
                        temp.append(i)
                    content.append(temp)
                name_exists = False
                counter = -1
                name_index = 0
                for i in content[0]:
                    counter += 1
                    if 'name' == i:
                        name_exists = True
                        name_index = counter
                if name_exists:
                    for i in content:
                        if name == i[name_index]:
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