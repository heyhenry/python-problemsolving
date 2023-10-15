"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
get_name_total("data1.csv", "goblin") -> -1 // no total
get_name_total("data2.csv", "bob smith") -> 1234
get_name_total("data2.csv", "alice jones") -> 6712
get_name_total("data3.csv", "Calvin Harris") -> 64953382
get_name_total("data3.csv", "The Weeknd") -> 108390904
get_name_total("data3.csv", "Test") -> -1
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

                containsTotal = False
                containsName = False

                fname_pos = 0
                lname_pos = 0
                total_pos = 0

                for i in range(len(content[0])):
                    if content[0][i] == 'first name' and len(content[0][i]) == 10:
                        
                        if content[0][i] == 'last name' and len(content[0][i]) == 9:
                            containsName = True
                            if content[0][i] == 'total' and len(content[0][i]) == 5:
                                containsTotal = True
                
            
                

            return -1

    return -1

def main():
    
    print(get_name_total("tables/data1.csv", "goblin"))
    print(get_name_total("tables/data2.csv", "bob smith"))
    print(get_name_total("tables/data2.csv", "alice jones"))
    print(get_name_total("tables/data3.csv", "Calvin Harris"))
    print(get_name_total("tables/data3.csv", "The Weeknd"))
    print(get_name_total("tables/data3.csv", "Test"))

if __name__ == "__main__":
    main()