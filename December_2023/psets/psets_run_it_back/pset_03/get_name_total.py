"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("tables/table1.csv", "goblin") -> -1 // no total
get_name_total("tables/table2.csv", "bob smith") -> 1234
get_name_total("tables/table2.csv", "alice jones") -> 6712
get_name_total("tables/table3.csv", "Calvin Harris") -> 64953382
get_name_total("tables/table3.csv", "The Weeknd") -> 108390904
get_name_total("tables/table3.csv", "Test") -> -1
"""
# Note: used thes same algorithm/logic as contains_name problem
def get_name_total(filename : str, name : str) -> int:

    result = -1

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()
            content = []

            for row in split_lines:
                content.append(row.split(','))

            name_found = False
            name_index = -1

            firstname_found = False
            lastname_found = False
            firstname_index = -1
            lastname_index = -1

            total_found = False
            total_index = -1

            for column in range(len(content[0])):
                if content[0][column] == 'name':
                    name_found = True
                    name_index = column
                elif content[0][column] == 'first name':
                    firstname_found = True
                    firstname_index = column
                elif content[0][column] == 'last name':
                    lastname_found = True
                    lastname_index = column
                elif content[0][column] == 'total':
                    total_found = True
                    total_index = column

            if name_found and total_found:

                for row in content:
                    if row[name_index] == name:
                        result = row[total_index]

            elif firstname_found and lastname_found and total_found:

                fullname = name.split(' ')

                for row in content:
                    if row[firstname_index] == fullname[0] and row[lastname_index] == fullname[1]:
                        result = row[total_index]

    return result

def main():
    print(get_name_total("tables/table1.csv", "goblin"))
    print(get_name_total("tables/table2.csv", "bob smith"))
    print(get_name_total("tables/table2.csv", "alice jones"))
    print(get_name_total("tables/table3.csv", "Calvin Harris"))
    print(get_name_total("tables/table3.csv", "The Weeknd"))
    print(get_name_total("tables/table3.csv", "Test"))

if __name__ == "__main__":
    main()