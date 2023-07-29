"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("tables/table1.csv", "goblin") -> -1 // no total
get_name_total("table2.csv", "bob smith") -> 1234
get_name_total("table2.csv", "alice jones") -> 6712
get_name_total("table3.csv", "Calvin Harris") -> 64953382
get_name_total("table3.csv", "The Weeknd") -> 108390904
get_name_total("table3.csv", "Test") -> -1
"""
from utilites import check_extension_csv

def get_name_total(filename : str, name : str) -> int:

    if check_extension_csv(filename[-4:]):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content: 

                splitlines = read_content.splitlines()
                lines = []

                for row in splitlines:
                    line = row.split(',')
                    lines.append(line)

                name_position = -1
                total_position = -1
                fname_position = -1
                lname_position = -1

                if 'first name' in lines[0] and 'last name' in lines[0] and 'total' in lines[0]:

                    for i in lines[0]:
                        fname_position += 1
                        if i == 'first name':
                            break

                    for i in lines[0]:
                        lname_position += 1
                        if i == 'last name':
                            break

                    for i in lines[0]:
                        total_position += 1
                        if i == 'total':
                            break

                    if total_position != -1 and lname_position != -1 and fname_position != 1:

                        fullname = name.split(' ')

                        for row in range(len(lines)):
                            if fullname[0] == lines[row][fname_position]:
                                if fullname[1] == lines[row][lname_position]:
                                    return lines[row][total_position]

                elif 'name' in lines[0] and 'total' in lines[0]:

                    for i in lines[0]:
                        name_position += 1
                        if i == 'name':
                            break
                    
                    for i in lines[0]:
                        total_position += 1
                        if i == 'total':
                            break 

                    if total_position != -1 and name_position != -1:

                        for row in range(len(lines)):
                            if name == lines[row][name_position]:
                                return lines[row][total_position]

                        return -1

                    else:

                        return -1
                    
                else:

                    return -1

            return -1


    else:

        return 'Invalid extension file type provided.'

def main():
    print(get_name_total("tables/table1.csv", "goblin"))
    print(get_name_total("tables/table2.csv", "bob smith"))
    print(get_name_total("tables/table2.csv", "alice jones"))
    print(get_name_total("tables/table3.csv", "Calvin Harris"))
    print(get_name_total("tables/table3.csv", "The Weeknd"))
    print(get_name_total("tables/table3.csv", "Test"))

if __name__ == "__main__":
    main()