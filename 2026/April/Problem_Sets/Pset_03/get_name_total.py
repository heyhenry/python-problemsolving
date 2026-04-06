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
        
        content = content.splitlines()

        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)

        categories =  updated_content[0]

        name_index = None
        first_name_index = None
        last_name_index = None
        total_index = None

        for col_name in range(len(categories)):
            if "name" == categories[col_name]:
                name_index = col_name
            elif "first name" == categories[col_name]:
                first_name_index = col_name
            elif "last name" == categories[col_name]:
                last_name_index = col_name
            elif "total" == categories[col_name]:
                total_index = col_name
        
        if total_index is not None:
            if name_index is not None:
                for row in range(1, len(updated_content)):
                    if updated_content[row][name_index] == name:
                        return updated_content[row][total_index]
            elif first_name_index is not None:
                for row in range(1, len(updated_content)):
                    if f"{updated_content[row][first_name_index]} {updated_content[row][last_name_index]}" == name:
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