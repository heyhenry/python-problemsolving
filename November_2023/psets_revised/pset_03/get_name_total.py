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

    desired_ext = '.csv'
    given_ext = filename[-4:]

    if given_ext == desired_ext:
        with open(filename, 'r') as file:
            read_content = file.read()
            result = -1
            if read_content:
                split_content = read_content.splitlines()
                content = []
                for row in split_content:
                    temp = []
                    for i in row.split(','):
                        temp.append(i)
                    content.append(temp)
                name_exists = False
                total_exists = False
                fname_exists = False
                lname_exists = False
                counter = -1
                name_index = 0
                total_index = 0
                fname_index = 0
                lname_index = 0

                for i in content[0]:
                    counter += 1
                    if 'name' == i:
                        name_exists = True
                        name_index = counter
                    elif 'first name' == i:
                        fname_exists = True
                        fname_index = counter
                    elif 'last name' == i:
                        lname_exists = True
                        lname_index = counter
                    elif 'total' == i:
                        total_exists = True
                        total_index = counter

                if name_exists and total_exists:
                    for row in content:
                        if name == row[name_index]:
                            result = row[total_index]
                elif fname_exists and lname_exists and total_exists:
                    full_name = name.split(' ')
                    for row in content:
                        if full_name[0] == row[fname_index]:
                            if full_name[1] == row[lname_index]:
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