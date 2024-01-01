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

    desired_extension = '.csv'
    given_extension = filename[-4:]

    if given_extension == desired_extension:

        with open(filename, 'r') as file:
            
            read_content = file.read()

            if read_content:

                content_splitlines = read_content.splitlines()
                content = []
                for line in content_splitlines:
                    content.append(line.split(','))

                name_pos = 0
                total_pos = 0
                fname_pos = 0
                lname_pos = 0

                contains_total = False
                contains_name = False
                contains_fname = False
                contains_lname = False
                
                # checks name type column
                for i in range(len(content[0])):
                    if content[0][i] == 'name' and len(content[0][i]) == 4:
                        name_pos = i
                        contains_name = True
                    if content[0][i] == 'total' and len(content[0][i]) == 5:
                        total_pos = i
                        contains_total = True

                # checks first name, last name type columns
                for i in range(len(content[0])):
                    if content[0][i] == 'first name' and len(content[0][i]) == 10:
                        fname_pos = i
                        contains_fname = True
                        
                for i in range(len(content[0])):
                    if content[0][i] == 'last name' and len(content[0][i]) == 9:
                        lname_pos = i
                        contains_lname = True
                    if content[0][i] == 'total' and len(content[0][i]) == 5:
                        total_pos = i
                        contains_total = True

                if contains_name and contains_total:
                    
                    for row in range(len(content)):
                        if content[row][name_pos] == name:
                            return content[row][total_pos]

                elif contains_fname and contains_lname and contains_total:
                    
                    full_name = name.split(' ')    

                    for row in range(len(content)):
                        if content[row][fname_pos] == full_name[0] and content[row][lname_pos] == full_name[1]:
                            return content[row][total_pos]
                return -1
            
            return -1

    return -1

def main():
    
    print(get_name_total("tables/table1.csv", "goblin"))
    print(get_name_total("tables/table2.csv", "bob smith"))
    print(get_name_total("tables/table2.csv", "alice jones"))
    print(get_name_total("tables/table3.csv", "Calvin Harris"))
    print(get_name_total("tables/table3.csv", "The Weeknd"))
    print(get_name_total("tables/table3.csv", "Test"))

if __name__ == "__main__":
    main()