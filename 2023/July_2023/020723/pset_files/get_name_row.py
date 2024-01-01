"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("tables_csv/table1.csv", "goblin") -> -1 // no total
get_name_total("table2.csv", "bob smith") -> 1234
get_name_total("table2.csv", "alice jones") -> 6712
get_name_total("table3.csv", "Calvin Harris") -> 64953382
get_name_total("table3.csv", "The Weeknd") -> 108390904
get_name_total("table3.csv", "Test") -> -1
"""
def get_name_total(filename : str, name : str) -> int:

    given_extension = filename[-4:]
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()

                proper_table = []

                for row in split_lines:
                    temp = row.split(',')
                    proper_table.append(temp)
                
                if 'name' in proper_table[0] and 'total' in proper_table[0]:
                    
                    name_counter = -1
                    total_counter = -1

                    for i in proper_table[0]:
                        name_counter += 1
                        if 'name' == i:
                            break
                    
                    for i in proper_table[0]:
                        total_counter += 1
                        if 'total' == i:
                            break
                    
                    for row in proper_table:
                        if name == row[name_counter]:
                            return row[total_counter]

                elif 'first name' in proper_table[0] and 'last name' in proper_table[0] and 'total' in proper_table[0]:
                    
                    fn_counter = -1
                    ln_counter = -1
                    fntotal_counter = -1

                    for i in proper_table[0]:
                        fn_counter += 1
                        if 'first name' == i:
                            break
                    
                    for i in proper_table[0]:
                        ln_counter += 1 
                        if 'last name' == i:
                            break

                    for i in proper_table[0]:
                        fntotal_counter += 1
                        if 'total' == i:
                            break

                    fullname = name.split(' ')
                    
                    for row in proper_table:
                        if fullname[0] == row[fn_counter] and fullname[1] == row[ln_counter]:
                            return row[fntotal_counter]

                else:
                    
                    return -1
            
            return -1
            

    else:

        return 'Invalid file extension naming. Please use .csv as your file extension.'

def main():
    print(get_name_total("tables_csv/table1.csv", "goblin"))
    print(get_name_total("tables_csv/table2.csv", "bob smith"))
    print(get_name_total("tables_csv/table2.csv", "alice jones"))
    print(get_name_total("tables_csv/table3.csv", "Calvin Harris"))
    print(get_name_total("tables_csv/table3.csv", "The Weeknd"))
    print(get_name_total("tables_csv/table3.csv", "Test"))

if __name__ == "__main__":
    main()