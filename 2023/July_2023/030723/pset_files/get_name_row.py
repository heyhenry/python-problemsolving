"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("table1.csv", "goblin") -> -1 // no total
get_name_total("table2.csv", "bob smith") -> 1234
get_name_total("table2.csv", "alice jones") -> 6712
get_name_total("table3.csv", "Calvin Harris") -> 64953382
get_name_total("table3.csv", "The Weeknd") -> 108390904
get_name_total("table3.csv", "Test") -> -1
"""
def get_name_total(filename : str, name : str) -> int:

    given_extension = filename[-4:]
    desired_exntesion = '.csv'

    if given_extension == desired_exntesion:

        with open(filename, 'r') as file:

            read_content = file.read()

            split_lines = read_content.splitlines()

            results = []

            for row in split_lines:
                line = row.split(',')
                results.append(line)

            if 'first name' in results[0] and 'last name' in results[0] and 'total' in results[0]:
                
                fn_counter = -1
                ln_counter = -1
                total_counter = -1

                for i in results[0]:
                    fn_counter += 1
                    if i == 'first name':
                        break

                for i in results[0]:
                    ln_counter += 1
                    if i == 'last name':
                        break

                for i in results[0]:
                    total_counter += 1
                    if i == 'total':
                        break

                fullname = name.split(' ')

                for row in results:
                    if fullname[0] == row[fn_counter] and fullname[1] == row[ln_counter]:
                        return row[total_counter]
                return -1
            
            elif 'name' in results[0] and 'total' in results[0]:

                name_counter = -1
                total_counter = -1

                for i in results[0]:
                    name_counter += 1
                    if i == 'name':
                        break

                for i in results[0]:
                    total_counter += 1
                    if i == 'total':
                        break

                for row in results:
                    if name == row[name_counter]:
                        return row[total_counter]
                return -1
            
            return -1

    return 'Invalid file extension. Must use .csv'

def main():
    print(get_name_total("tables_csv/table1.csv", "goblin"))
    print(get_name_total("tables_csv/table2.csv", "bob smith"))
    print(get_name_total("tables_csv/table2.csv", "alice jones"))
    print(get_name_total("tables_csv/table3.csv", "Calvin Harris"))
    print(get_name_total("tables_csv/table3.csv", "The Weeknd"))
    print(get_name_total("tables_csv/table3.csv", "Test"))

if __name__ == "__main__":
    main()