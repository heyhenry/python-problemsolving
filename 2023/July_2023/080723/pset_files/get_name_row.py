"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("tables_csv/table1.csv", "goblin") -> -1 // no total
get_name_total("tables_csv/table2.csv", "bob smith") -> 1234
get_name_total("tables_csv/table2.csv", "alice jones") -> 6712
get_name_total("tables_csv/table3.csv", "Calvin Harris") -> 64953382
get_name_total("tables_csv/table3.csv", "The Weeknd") -> 108390904
get_name_total("tables_csv/table3.csv", "Test") -> -1
"""
def get_name_total(filename : str, name : str) -> int:

    d_ext = '.csv'
    ext = filename[-4:]

    if ext == d_ext:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content: 

                split_lines = read_content.splitlines()

                converted = []

                for row in split_lines:
                    line = row.split(',')
                    converted.append(line)

                name_exists = False
                fn_exists = False
                ln_exists = False
                total_exists = False

                name_pos = -1
                fn_pos = -1
                ln_pos = -1
                total_pos = -1

                for i in converted[0]:
                    name_pos += 1
                    if 'name' == i:
                        name_exists = True
                        break

                for i in converted[0]:
                    fn_pos += 1
                    if 'first name' == i:
                        fn_exists = True
                        break
                
                for i in converted[0]:
                    ln_pos += 1
                    if 'last name' == i:
                        ln_exists = True
                        break

                for i in converted[0]:
                    total_pos += 1
                    if 'total' == i:
                        total_exists = True
                        break

                if name_exists == True and total_exists == True:

                    for row in converted:
                        if name == row[name_pos]:
                            return row[total_pos]

                elif fn_exists == True and ln_exists == True and total_exists == True:

                    fullname = name.split(' ')

                    for row in converted:
                        if fullname[0] == row[fn_pos] and fullname[1] == row[ln_pos]:
                            return row[total_pos]

            return -1

    return 'Invalid file extension. Please use .csv'

def main():
    print(get_name_total("tables_csv/table1.csv", "goblin"))
    print(get_name_total("tables_csv/table2.csv", "bob smith"))
    print(get_name_total("tables_csv/table2.csv", "alice jones"))
    print(get_name_total("tables_csv/table3.csv", "Calvin Harris"))
    print(get_name_total("tables_csv/table3.csv", "The Weeknd"))
    print(get_name_total("tables_csv/table3.csv", "Test"))

if __name__ == "__main__":
    main()