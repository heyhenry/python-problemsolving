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
def get_name_total(filename : str, name : str) -> int:

    if filename[filename.rfind('.'):] == '.csv':

        result = -1

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()

                content = []

                for row in split_lines:
                    content.append(row.split(','))

                # check if columns exist
                name_found = False
                total_found = False
                fname_found = False
                lname_found = False

                # note index position of columns
                name_position = 0
                total_position = 0
                fname_position = 0
                lname_position = 0

                if 'name' in content[0]:
                    name_found = True
                    name_position = content[0].index('name')
                if 'total' in content[0]:
                    total_found = True
                    total_position = content[0].index('total')
                if 'first name' in content[0]:
                    fname_found = True
                    fname_position = content[0].index('first name')
                if 'last name' in content[0]:
                    lname_found = True
                    lname_position = content[0].index('last name')

                if name_found and total_found:
                    
                    for row in content:
                        if row[name_position] == name:
                            result = row[total_position]

                elif fname_found and lname_found and total_found:

                    full_name = name.split(' ')

                    for row in content:
                        if row[fname_position] == full_name[0] and row[lname_position] == full_name[1]:
                            result = row[total_position]
        
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