"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("files/table1.csv", "goblin") -> -1 // no total
get_name_total("files/table2.csv", "bob smith") -> 1234
get_name_total("files/table2.csv", "alice jones") -> 6712
get_name_total("files/table3.csv", "Calvin Harris") -> 64953382
get_name_total("files/table3.csv", "The Weeknd") -> 108390904
get_name_total("files/table3.csv", "Test") -> -1
"""
def get_name_total(filename : str, name : str) -> int:

    if filename[filename.rfind('.')::] == '.csv':

        result = -1  

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()
                content = []

                for row in split_lines:
                    content.append(row.split(','))

                name_column_found = False
                total_column_found = False
                fname_column_found = False
                lname_column_found = False

                name_index = -1
                total_index = -1
                fname_index = -1
                lname_index = -1

                for column in range(len(content[0])):
                    if content[0][column] == 'name':
                        name_index = column
                        name_column_found = True
                    elif content[0][column] == 'total':
                        total_index = column
                        total_column_found = True
                    elif content[0][column] == 'first name':
                        fname_index = column
                        fname_column_found = True
                    elif content[0][column] == 'last name': 
                        lname_index = column
                        lname_column_found = True

                if name_column_found and total_column_found: 

                    for row in content:
                        if name == row[name_index]:
                            result = row[total_index]

                elif fname_column_found and lname_column_found and total_column_found:

                    full_name = name.split(' ')

                    for row in content:
                        if full_name[0] == row[fname_index] and full_name[1] == row[lname_index]:
                            result = row[total_index]

        return result

def main():
    print(get_name_total("files/table1.csv", "goblin"))
    print(get_name_total("files/table2.csv", "bob smith"))
    print(get_name_total("files/table2.csv", "alice jones"))
    print(get_name_total("files/table3.csv", "Calvin Harris"))
    print(get_name_total("files/table3.csv", "The Weeknd"))
    print(get_name_total("files/table3.csv", "Test"))

if __name__ == "__main__":
    main()