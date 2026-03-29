""" 
Given a filename ending with `csv` 

Returns the total associated with `name` 
If the table has no `total` column or `name` is not found, returns -1 

If the file contains `first name` and `last name` rather than `name` 
Then this function should treat those as concatenated by a space 

Examples: 
    contains_name("table_data/table1.csv", "goblin") -> -1 // no total 
    contains_name("table_data/table2.csv", "bob smith") -> 1234 
    contains_name("table_data/table2.csv", "alice jones") -> 6712 
    contains_name("table_data/table3.csv", "Calvin Harris") -> 64953382 
    contains_name("table_data/table3.csv", "The Weeknd") -> 108390904 
    contains_name("table_data/table3.csv", "Test") -> -1 
"""
def get_name_total(filename : str, name : str) -> int:
    
    with open(filename, "r") as file:
        content = file.read()

        # organise file data into list of lists
        content = content.splitlines()
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)
        
        # create variable to store column headers (for future referencing)
        categories = updated_content[0]

        # find indexes for total, name, first name, last name
        name_index = None
        first_name_index = None
        last_name_index = None
        total_index = None
         
        for i in range(len(categories)):
            if categories[i] == "name":
                name_index = i
            elif categories[i] == "first name":
                first_name_index = i
            elif categories[i] == "last name":
                last_name_index = i
            elif categories[i] == "total":
                total_index = i

        # end program early if total column is not found OR
        # end program if either name or first name (and last name) columns are not found
        # this ensure that the required information to reach the results is found
        if total_index is None:
            return -1
        elif name_index is None and first_name_index is None:
            return -1
        
        # search for given name under the name column
        if name_index is not None:
            for row in range(len(updated_content)):
                if name == updated_content[row][name_index]:
                    return updated_content[row][total_index]
        
        # search for the given name under the first name + last name columns concatenated
        else:
            for row in range(len(updated_content)):
                full_name = f"{updated_content[row][first_name_index]} {updated_content[row][last_name_index]}"
                if name == full_name:
                    return updated_content[row][total_index]
                
        return -1

test_cases = [
    ("table_data/table1.csv", "goblin"),
    ("table_data/table2.csv", "bob smith"),
    ("table_data/table2.csv", "alice jones"),
    ("table_data/table3.csv", "Calvin Harris"),
    ("table_data/table3.csv", "The Weeknd"),
    ("table_data/table3.csv", "Test")
]

for case in test_cases:
    print(get_name_total(case[0], case[1]))