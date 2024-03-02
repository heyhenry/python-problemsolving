"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
contains_name("table1.csv", "goblin") -> -1 // no total
contains_name("table2.csv", "bob smith") -> 1234
contains_name("table2.csv", "alice jones") -> 6712
contains_name("table3.csv", "Calvin Harris") -> 64953382
contains_name("table3.csv", "The Weeknd") -> 108390904
contains_name("table3.csv", "Test") -> -1
"""
def get_total(filename : str, name : str) -> int:

    result = -1
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

                # fname = first name
                fname_exists = False
                total_exists = False
                name_exists = False

                if 'first name' in content[0]:
                    fname_exists = True
                if 'total' in content[0]:
                    total_exists = True
                if 'name' in content[0]:
                    name_exists = True

                if fname_exists and total_exists:
                    
                    full_name = name.split(' ')

                    for row in content:
                        if full_name[0] == row[content[0].index('first name')] and full_name[1] == row[content[0].index('last name')]:
                            result = row[content[0].index('total')]

                elif name_exists and total_exists:

                    for row in content:
                        if name == row[content[0].index('name')]:
                            result = row[content[0].index('total')]

    return result

def main():
    print(get_total("tables/table1.csv", "goblin"))
    print(get_total("tables/table2.csv", "bob smith"))
    print(get_total("tables/table2.csv", "alice jones"))
    print(get_total("tables/table3.csv", "Calvin Harris"))
    print(get_total("tables/table3.csv", "The Weeknd"))
    print(get_total("tables/table3.csv", "Test"))

if __name__ == "__main__":
    main()
