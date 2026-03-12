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
        # read and store csv file data
        content = file.read()

        # exit early if file is empty
        if not content:
            return -1
        
        # create a list of element per line from csv data
        content = content.splitlines()

        # reform content's elements into its own list of elements 
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)
        
        # flags to validate usable table.csv file
        has_name = False
        has_full_name = False
        has_total = False
        
        # variables to save column indexes for future referencing
        name_index = 0
        first_name_index = 0
        last_name_index = 0
        total_index = 0

        # check if name, first name + last name or total columns exist
        for i in range(len(updated_content[0])):
            if updated_content[0][i] == "name":
                has_name = True
                name_index = i
            elif updated_content[0][i] == "total":
                has_total = True
                total_index = i
            elif i < len(updated_content[0])-1 and (updated_content[0][i] == "first name" and updated_content[0][i+1] == "last name"):
                has_full_name = True
                first_name_index = i
                last_name_index = i+1

        # check and proceed only if required columns exists
        if has_total and has_name:
            for i in range(1, len(updated_content)):
                if updated_content[i][name_index] == name:
                    return updated_content[i][total_index]

        elif has_total and has_full_name:
            for i in range(1, len(updated_content)):
                if f"{updated_content[i][first_name_index]}" + " " + f"{updated_content[i][last_name_index]}" == name:
                    return updated_content[i][total_index]

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