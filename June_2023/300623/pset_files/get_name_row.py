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
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            remove_nl = read_content.splitlines()

            results = []

            for row in remove_nl:
                line = row.split(',')
                results.append(line)

            name_location = -1
            total_location = -1
            first_name_location = -1
            last_name_location = -1
            name_exists = False
            total_exists = False

            for row in results[0]:
                name_location += 1
                if 'name' == row:
                    name_exists = True
                    break

            for row in results[0]:
                total_location += 1
                if 'total' == row:
                    total_exists = True
                    break

            check_name_with_surname = 0

            for row in results[0]:
                first_name_location += 1
                if 'first name' == row:
                    check_name_with_surname += 1
                    break
                
            for row in results[0]:
                last_name_location += 1
                if 'last name' == row:
                    check_name_with_surname += 1
                    break

            total_result = -1

            if check_name_with_surname == 2:

                new_results = []

                for row in results:
                    temp = []
                    temp.append(row[0] + ' ' + row[1])
                    temp.append(row[2])
                    new_results.append(temp)

                fullname_location = -1
                fullname_total_location = -1
                fullname_exists = False
                fullname_total_exists = False

                for row in new_results[0]:
                    fullname_location += 1
                    if 'first name last name' == row:
                        fullname_exists = True
                        break

                for row in new_results[0]:
                    fullname_total_location += 1
                    if 'total' == row:
                        fullname_total_exists = True
                        break

                if fullname_exists == True and fullname_total_exists == True:
                    
                    for row in range(len(new_results)):
                        if name == new_results[row][fullname_location]:
                            total_result = new_results[row][fullname_total_location]

                    return total_result

            elif name_exists == True and total_exists:

                for row in range(len(results)):
                    if name == results[row][name_location]:
                        total_result = results[row][total_location]

                return total_result
            
            else:

                return total_result

    else:

        return 'Invalid file extension. Ensure it uses .csv'

def main():
    print(get_name_total("tables_csv/table1.csv", "goblin")) # -1
    print(get_name_total("tables_csv/table2.csv", "bob smith")) # 1234
    print(get_name_total("tables_csv/table2.csv", "alice jones")) # 6712
    print(get_name_total("tables_csv/table3.csv", "Calvin Harris")) # 64953382
    print(get_name_total("tables_csv/table3.csv", "The Weeknd")) # 108390904
    print(get_name_total("tables_csv/table3.csv", "Test")) # -1

if __name__ == "__main__":
    main()