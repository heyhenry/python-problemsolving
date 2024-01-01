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

    result = -1

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            # splits each new line of text into a new list
            store_lines = read_content.splitlines()

            content = []

            # store each stored line (new line) into their own respective list of elements
            for row in store_lines:
                temp = []
                for line in row.split(','):
                    temp.append(line)
                content.append(temp)
            
            # marker to check if column name found
            name_found = False
            fname_found = False
            lname_found = False
            total_found = False
        
            # locations of each relevant column
            name_index = -1
            fname_index = -1
            lname_index = -1
            total_index = -1

            # flags to know when to turn off counting for each index
            name_index_found = True
            fname_index_found = True
            lname_index_found = True
            total_index_found = True

            # finding the positions and column names 
            for title in content[0]:
                
                if name_index_found:
                    name_index += 1
                if fname_index_found:
                    fname_index += 1
                if lname_index_found:
                    lname_index += 1
                if total_index_found:
                    total_index += 1

                if 'name' == title:
                    name_found = True
                    name_index_found = False
                elif 'first name' == title:
                    fname_found = True
                    fname_index_found = False
                elif 'last name' == title:
                    lname_found = True
                    lname_index_found = False
                elif 'total' == title:
                    total_found = True
                    total_index_found = False
                
            if name_found and total_found:
                # searches for the name and then its respective total
                for row in range(len(content)):
                    if content[row][name_index] == name:
                        result = content[row][total_index]

            elif fname_found and lname_found and total_found:

                full_name = name.split(' ')
                # searches for the name in 2 parts: first name, then last name
                # afterwards finds the total
                for row in range(len(content)):
                    if content[row][fname_index] == full_name[0]:
                        if content[row][lname_index] == full_name[1]:
                            result = content[row][total_index] 

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